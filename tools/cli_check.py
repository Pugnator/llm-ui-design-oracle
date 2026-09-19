#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cli_check - automated conformance checks for the UI Oracle `cli` module.

Runs a command-line program through the checks the module marks as
automatic and reports one finding per check in the oracle's format.
Standard library only. Windows and POSIX.

Every check names the rule it serves (UI-CLI-nnn, modules/cli.md). The
report is the gate the contract requires for `cli` conformance: zero FAIL.
"""
import argparse
import io
import json
import os
import re
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time

PROG = "cli_check"
VERSION = "5.0.0"
HOME_URL = "https://github.com/Pugnator/llm-ui-design-oracle"
IS_WIN = os.name == "nt"
ESC = b"\x1b"

STATUSES = ("PASS", "FAIL", "N/A", "NEEDS HUMAN JUDGMENT")

# ----------------------------------------------------------------------------
# result plumbing
# ----------------------------------------------------------------------------


class Run(object):
    """One invocation of the program under test."""

    def __init__(self, args, exit_code, out, err, elapsed_ms, first_ms, timed_out):
        self.args = args
        self.exit_code = exit_code
        self.out = out
        self.err = err
        self.elapsed_ms = elapsed_ms
        self.first_ms = first_ms
        self.timed_out = timed_out

    def text(self, which):
        data = self.out if which == "out" else self.err
        return data.decode("utf-8", "replace")

    def label(self):
        return " ".join(self.args)


class Finding(object):
    def __init__(self, rule, status, check, evidence, fix=""):
        self.rule = rule
        self.status = status
        self.check = check
        self.evidence = evidence
        self.fix = fix

    def as_dict(self):
        return {"rule": self.rule, "status": self.status, "check": self.check,
                "evidence": self.evidence, "fix": self.fix}


class Checker(object):
    def __init__(self, command, config, timeout, workdir, verbose):
        self.command = command
        self.config = config
        self.timeout = timeout
        self.workdir = workdir
        self.verbose = verbose
        self.findings = []
        self.runs = []
        self.help_text = ""
        self.subcommands = []
        self.exe_dir = None
        self.multi = False

    # -- process control -----------------------------------------------------

    def resolve(self):
        exe = self.command[0]
        path = shutil.which(exe) or (exe if os.path.exists(exe) else None)
        if path is None:
            return None
        self.exe_dir = os.path.dirname(os.path.abspath(path))
        self.command = [path] + self.command[1:]
        return path

    def popen_args(self, extra):
        argv = list(self.command) + list(extra)
        if IS_WIN and argv[0].lower().endswith((".cmd", ".bat")):
            argv = ["cmd.exe", "/d", "/c"] + argv
        return argv

    def run(self, extra, stdin_data=None, env=None, timeout=None, record=True,
            interrupt_after=None, exit_within=None, use_pty=False):
        """Run the program with extra args. stdin is /dev/null unless data given."""
        argv = self.popen_args(extra)
        environ = dict(os.environ)
        environ.setdefault("TMPDIR", self.workdir)
        if env:
            environ.update(env)
        timeout = timeout or self.timeout
        if use_pty and not IS_WIN:
            return self._run_pty(extra, argv, environ, timeout, record)
        kwargs = {}
        if IS_WIN:
            kwargs["creationflags"] = subprocess.CREATE_NEW_PROCESS_GROUP
        else:
            kwargs["start_new_session"] = True
        stdin = subprocess.PIPE if stdin_data is not None else subprocess.DEVNULL
        t0 = time.monotonic()
        try:
            proc = subprocess.Popen(argv, stdin=stdin, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, cwd=self.workdir,
                                    env=environ, **kwargs)
        except OSError as exc:
            run = Run(extra, None, b"", str(exc).encode(), 0, None, False)
            if record:
                self.runs.append(run)
            return run
        chunks = {"out": [], "err": []}
        first = {"ms": None}
        lock = threading.Lock()

        def pump(stream, key):
            while True:
                data = stream.read(4096)
                if not data:
                    break
                with lock:
                    if first["ms"] is None:
                        first["ms"] = (time.monotonic() - t0) * 1000.0
                    chunks[key].append(data)

        threads = [threading.Thread(target=pump, args=(proc.stdout, "out")),
                   threading.Thread(target=pump, args=(proc.stderr, "err"))]
        for th in threads:
            th.daemon = True
            th.start()
        if stdin_data is not None:
            try:
                proc.stdin.write(stdin_data)
                proc.stdin.close()
            except OSError:
                pass
        timed_out = False
        interrupted = False
        deadline = t0 + timeout
        if interrupt_after is not None:
            time.sleep(interrupt_after)
            self._interrupt(proc)
            interrupted = True
            deadline = time.monotonic() + (exit_within or 5.0)
        while proc.poll() is None:
            if time.monotonic() > deadline:
                timed_out = True
                self._kill(proc)
                break
            time.sleep(0.01)
        for th in threads:
            th.join(timeout=2.0)
        elapsed = (time.monotonic() - t0) * 1000.0
        run = Run(extra, proc.returncode, b"".join(chunks["out"]), b"".join(chunks["err"]),
                  elapsed, first["ms"], timed_out)
        run.interrupted = interrupted
        if record:
            self.runs.append(run)
        return run

    def _run_pty(self, extra, argv, environ, timeout, record):
        import pty  # POSIX only
        master, slave = pty.openpty()
        t0 = time.monotonic()
        proc = subprocess.Popen(argv, stdin=slave, stdout=slave, stderr=slave,
                                cwd=self.workdir, env=environ, close_fds=True,
                                start_new_session=True)
        os.close(slave)
        buf = []
        timed_out = False
        while True:
            if proc.poll() is not None:
                break
            if time.monotonic() - t0 > timeout:
                timed_out = True
                self._kill(proc)
                break
            try:
                data = os.read(master, 4096)
                if data:
                    buf.append(data)
            except OSError:
                break
        try:
            while True:
                data = os.read(master, 4096)
                if not data:
                    break
                buf.append(data)
        except OSError:
            pass
        os.close(master)
        run = Run(extra, proc.returncode, b"".join(buf), b"", (time.monotonic() - t0) * 1000.0, None, timed_out)
        if record:
            self.runs.append(run)
        return run

    def _interrupt(self, proc):
        try:
            if IS_WIN:
                # Ctrl-C proper cannot be targeted at one process group from
                # here; Ctrl-Break can, and well-behaved programs treat it alike.
                proc.send_signal(signal.CTRL_BREAK_EVENT)
            else:
                os.killpg(proc.pid, signal.SIGINT)
        except OSError:
            pass

    def _kill(self, proc):
        try:
            if IS_WIN:
                subprocess.call(["taskkill", "/F", "/T", "/PID", str(proc.pid)],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                os.killpg(proc.pid, signal.SIGKILL)
        except OSError:
            pass

    # -- reporting helpers ---------------------------------------------------

    def add(self, rule, status, check, evidence, fix=""):
        self.findings.append(Finding(rule, status, check, evidence, fix))

    def human(self, rule, check, question):
        self.add(rule, "NEEDS HUMAN JUDGMENT", check, question)

    # -- help parsing --------------------------------------------------------

    OPT_RE = re.compile(r"^\s{0,12}(?:(-[A-Za-z0-9])(?:[ ,/|]+(--[A-Za-z0-9][\w-]*))?|(--[A-Za-z0-9][\w-]*))", re.M)

    def parse_options(self, text):
        shorts = {}
        longs = set()
        for m in self.OPT_RE.finditer(text):
            short, long_, lonly = m.group(1), m.group(2), m.group(3)
            if short:
                shorts.setdefault(short, None)
                if long_:
                    shorts[short] = long_
                    longs.add(long_)
            elif lonly:
                longs.add(lonly)
        return shorts, longs

    SUB_HEAD = re.compile(r"^\s*(available\s+)?(sub)?commands?\s*:?\s*$", re.I | re.M)

    def parse_subcommands(self, text):
        if self.config.get("subcommands"):
            return list(self.config["subcommands"])
        subs = []
        m = self.SUB_HEAD.search(text)
        if not m:
            return subs
        for line in text[m.end():].splitlines():
            if not line.strip():
                if subs:
                    break
                continue
            if not line.startswith((" ", "\t")):
                break
            tok = line.strip().split()[0].strip(",")
            if re.match(r"^[a-z][a-z0-9:_-]*$", tok):
                subs.append(tok)
        return subs

    # -- checks --------------------------------------------------------------

    def check_all(self):
        cfg = self.config
        name = os.path.basename(self.command[0])
        stem = re.sub(r"\.(exe|cmd|bat|py|sh)$", "", name, flags=re.I)

        # UI-CLI-022 name
        if re.match(r"^[a-z][a-z0-9-]*$", stem):
            self.add("UI-CLI-022", "PASS", "name-lowercase", "program name %r" % stem)
        else:
            self.add("UI-CLI-022", "FAIL", "name-lowercase", "program name %r is not lower-case letters, digits and dashes" % stem,
                     "rename the executable")
        if 2 <= len(stem) <= 9:
            self.add("UI-CLI-022", "PASS", "name-length", "%d characters" % len(stem))
        else:
            self.human("UI-CLI-022", "name-length", "name is %d characters; POSIX guideline 1 says two to nine" % len(stem))

        # --help / -h
        h1 = self.run(["--help"])
        h2 = self.run(["-h"])
        if h1.exit_code is None:
            self.add("UI-CLI-003", "FAIL", "help-flags", "could not start the program: %s" % h1.text("err").strip())
            return
        self.help_text = h1.text("out")
        ok = all(r.exit_code == 0 and r.out.strip() for r in (h1, h2))
        self.add("UI-CLI-003", "PASS" if ok else "FAIL", "help-flags",
                 "--help exit %s (%d bytes stdout); -h exit %s (%d bytes stdout)" % (h1.exit_code, len(h1.out), h2.exit_code, len(h2.out)),
                 "both -h and --help must print help on stdout and exit 0")
        self.add("UI-CLI-001", "PASS" if h1.exit_code == 0 else "FAIL", "exit-success-help", "--help exit code %s" % h1.exit_code)
        self.add("UI-CLI-002", "PASS" if (h1.out.strip() and not h1.err.strip()) else "FAIL", "streams-help",
                 "--help wrote %d bytes to stdout and %d to stderr" % (len(h1.out), len(h1.err)), "help is output; it belongs on stdout, nothing on stderr")

        self.subcommands = self.parse_subcommands(self.help_text)
        self.multi = bool(self.subcommands)

        # help content
        low = self.help_text.lower()
        has_usage = "usage" in low
        has_example = "example" in low
        has_support = bool(re.search(r"https?://|[\w.+-]+@[\w-]+\.[\w.]+", self.help_text))
        self.add("UI-CLI-003", "PASS" if has_usage and has_example and has_support else "FAIL", "help-content",
                 "usage=%s examples=%s support-link=%s" % (has_usage, has_example, has_support),
                 "help must show usage, at least one example, and a bug/support address near the end")
        long_lines = [l for l in self.help_text.splitlines() if len(l.rstrip()) > 80]
        self.add("UI-CLI-003", "PASS" if not long_lines else "FAIL", "help-width",
                 "%d help lines exceed 80 columns" % len(long_lines) if long_lines else "all help lines fit 80 columns",
                 "wrap help to 80 columns")

        # help anywhere
        probe = [self.subcommands[0]] if self.multi else []
        ha = self.run(probe + ["--help"])
        hb = self.run(["--help", "zzz-extra-operand"])
        ok = ha.exit_code == 0 and ha.out.strip() and hb.exit_code == 0 and hb.out.strip()
        self.add("UI-CLI-003", "PASS" if ok else "FAIL", "help-anywhere",
                 "%s --help exit %s; --help with a trailing operand exit %s" % (" ".join(probe) or "<root>", ha.exit_code, hb.exit_code),
                 "--help must work after a subcommand and must ignore other arguments")

        # bare invocation
        bare = self.run([])
        if bare.timed_out:
            self.add("UI-CLI-003", "FAIL", "help-bare", "bare invocation did not exit within %.0fs (prompt or hang?)" % self.timeout,
                     "print concise help and exit when required arguments are missing")
        elif not (bare.out.strip() or bare.err.strip()):
            self.add("UI-CLI-003", "FAIL", "help-bare", "bare invocation printed nothing (exit %s)" % bare.exit_code,
                     "a bare invocation lists the commands or prints concise help")
        else:
            self.add("UI-CLI-003", "PASS", "help-bare", "bare invocation exit %s with %d bytes of output" % (bare.exit_code, len(bare.out) + len(bare.err)))

        # help subcommand for multi-command tools
        if self.multi:
            hs = self.run(["help"])
            self.add("UI-CLI-003", "PASS" if hs.exit_code == 0 and hs.out.strip() else "FAIL", "help-subcommand",
                     "'help' subcommand exit %s" % hs.exit_code, "multi-command programs accept `help` as well as --help")

        # --version
        v = self.run(["--version"])
        first = v.text("out").strip().splitlines()[0] if v.out.strip() else ""
        vtoken = first.split(" ")[-1] if first else ""
        vok = v.exit_code == 0 and bool(re.search(r"\d+(\.\d+)+", vtoken))
        self.add("UI-CLI-004", "PASS" if vok else "FAIL", "version-flag",
                 "--version exit %s, first line %r" % (v.exit_code, first[:80]),
                 "print `name version` on stdout, version number after the last space, exit 0")
        self.add("UI-CLI-002", "PASS" if (v.out.strip() and not v.err.strip()) else "FAIL", "streams-version",
                 "--version wrote %d bytes to stdout, %d to stderr" % (len(v.out), len(v.err)))
        self.add("UI-CLI-001", "PASS" if v.exit_code == 0 else "FAIL", "exit-success-version", "--version exit code %s" % v.exit_code)
        v2 = self.run(["--version", "zzz-extra-operand"])
        self.add("UI-CLI-004", "PASS" if v2.exit_code == 0 and v2.out.strip() else "FAIL", "version-ignores-args",
                 "--version with a trailing operand exit %s" % v2.exit_code, "once --version is seen, other arguments are ignored")
        if v.elapsed_ms <= 500:
            self.add("UI-CLI-016", "PASS", "startup-time", "--version took %.0f ms" % v.elapsed_ms)
        else:
            self.add("UI-CLI-016", "FAIL", "startup-time", "--version took %.0f ms; the budget is 500 ms" % v.elapsed_ms,
                     "cut start-up work; load only what the invoked command needs")

        # options
        shorts, longs = self.parse_options(self.help_text)
        no_long = sorted(s for s, l in shorts.items() if l is None and s not in ("-h", "-V", "-v"))
        self.add("UI-CLI-005", "PASS" if not no_long else "FAIL", "long-forms",
                 "short options without a long form: %s" % (", ".join(no_long) if no_long else "none"),
                 "every short option gets a --long-name")
        std = {"--dry-run": "-n", "--force": "-f", "--quiet": "-q", "--output": "-o", "--all": "-a", "--recursive": "-r"}
        wrong = []
        for long_, short in std.items():
            owner = [s for s, l in shorts.items() if l == long_]
            if owner and owner[0] != short:
                wrong.append("%s is %s (convention %s)" % (long_, owner[0], short))
        if shorts.get("-h") not in (None, "--help"):
            wrong.append("-h is not help")
        self.add("UI-CLI-005", "PASS" if not wrong else "FAIL", "standard-names",
                 "; ".join(wrong) if wrong else "standard letters carry their standard meanings",
                 "use the conventional short letter for a conventional long option")
        if "--quiet" in longs or "--silent" in longs:
            other = "--silent" if "--quiet" in longs else "--quiet"
            r = self.run([other, "--version"])
            self.add("UI-CLI-005", "PASS" if r.exit_code == 0 else "FAIL", "quiet-silent-synonym",
                     "%s --version exit %s" % (other, r.exit_code), "--quiet and --silent are synonyms (GNU)")
        for flag, rule in (("--no-color", "UI-CLI-009"), ("--no-input", "UI-CLI-013")):
            r = self.run([flag, "--version"])
            if r.exit_code == 0:
                self.add(rule, "PASS", "accepts" + flag, "%s accepted" % flag)
            elif flag == "--no-input" and not cfg.get("prompts", True):
                self.add(rule, "N/A", "accepts" + flag, "profile declares the program never prompts")
            else:
                self.add(rule, "FAIL", "accepts" + flag, "%s --version exit %s: %s" % (flag, r.exit_code, r.text("err").strip()[:80]),
                         "accept %s" % flag)

        # positionals in usage lines
        usage_lines = [l for l in self.help_text.splitlines() if re.match(r"^\s*usage:", l, re.I)]
        kinds = set()
        for l in usage_lines:
            for tok in re.findall(r"<([^>]+)>|\b([A-Z][A-Z_-]{2,})\b", l):
                kinds.add((tok[0] or tok[1]).rstrip(". "))
        kinds = {k for k in kinds if k.lower() not in ("options", "option", "flags", "command", "subcommand", "args", "arguments")}
        if len(kinds) >= 3:
            self.add("UI-CLI-006", "FAIL", "positionals", "usage names %d kinds of positional argument: %s" % (len(kinds), ", ".join(sorted(kinds))),
                     "three kinds of positional argument are never good; use flags")
        elif len(kinds) == 2:
            self.human("UI-CLI-006", "positionals", "usage names two kinds of positional argument (%s); is the order obvious, or should they be flags?" % ", ".join(sorted(kinds)))
        else:
            self.add("UI-CLI-006", "PASS", "positionals", "usage names %d kind(s) of positional argument" % len(kinds))

        # unknown flag / subcommand
        u = self.run(["--zzz-definitely-unknown-option"])
        ok = u.exit_code not in (0, None) and u.err.strip() and not u.out.strip() and not u.timed_out
        self.add("UI-CLI-007", "PASS" if ok else "FAIL", "unknown-flag",
                 "unknown option: exit %s, %d bytes stderr, %d bytes stdout" % (u.exit_code, len(u.err), len(u.out)),
                 "an unknown option is an error: non-zero exit, message on stderr, nothing on stdout")
        self.add("UI-CLI-001", "PASS" if u.exit_code not in (0, None) else "FAIL", "exit-failure", "unknown option exit code %s" % u.exit_code)
        self.add("UI-CLI-002", "PASS" if not u.out.strip() else "FAIL", "streams-error", "error case wrote %d bytes to stdout" % len(u.out),
                 "errors go to stderr only")
        self._check_error_text(u, stem)
        if self.multi:
            us = self.run(["zzznotacommand"])
            self.add("UI-CLI-007", "PASS" if us.exit_code not in (0, None) and not us.timed_out else "FAIL", "unknown-subcommand",
                     "unknown subcommand exit %s" % us.exit_code, "an unknown subcommand must fail, never fall through to a default command")
            self.add("UI-CLI-018", "PASS" if us.exit_code not in (0, None) else "FAIL", "no-catch-all",
                     "unknown first argument exit %s" % us.exit_code, "no catch-all subcommand")
            real = max(self.subcommands, key=len)
            if len(real) >= 4:
                typo = real[1] + real[0] + real[2:]
                t = self.run([typo])
                mentions = real in (t.text("err") + t.text("out"))
                if t.exit_code == 0:
                    self.add("UI-CLI-007", "FAIL", "suggestion-not-run", "misspelling %r exited 0: the guess was run" % typo, "suggest, never run the guess")
                elif mentions:
                    self.add("UI-CLI-007", "PASS", "suggestion", "misspelling %r produced a message naming %r" % (typo, real))
                else:
                    self.human("UI-CLI-007", "suggestion", "misspelling %r failed without naming %r; can the program suggest the correction?" % (typo, real))
                prefix = real[:3]
                if prefix not in self.subcommands and prefix not in cfg.get("aliases", []):
                    p = self.run([prefix])
                    self.add("UI-CLI-018", "PASS" if p.exit_code not in (0, None) else "FAIL", "no-abbreviation",
                             "prefix %r exit %s" % (prefix, p.exit_code), "do not accept arbitrary abbreviations; declare explicit aliases")
            close = []
            for i, a in enumerate(self.subcommands):
                for b in self.subcommands[i + 1:]:
                    if len(a) >= 4 and len(b) >= 4 and _lev(a, b) <= 2:
                        close.append("%s/%s" % (a, b))
            if close:
                self.human("UI-CLI-018", "similar-names", "subcommand names within two edits of each other: %s; do they do different things?" % ", ".join(close))
            else:
                self.add("UI-CLI-018", "PASS", "similar-names", "no two subcommand names within two edits of each other")

        # secrets via flags
        secret = [l for l in longs if re.search(r"(password|passwd|token|secret|api-?key|credential)s?$", l) and not l.endswith(("-file", "-stdin", "-path"))]
        self.add("UI-CLI-014", "PASS" if not secret else "FAIL", "secrets-in-flags",
                 "flags that take a secret on the command line: %s" % (", ".join(sorted(secret)) if secret else "none"),
                 "read secrets from a file or stdin (--token-file, --password-stdin)")

        # -- config-driven checks --------------------------------------------
        listc = cfg.get("list_command")
        if listc:
            lr = self.run(listc)
            grid = [l for l in lr.text("out").splitlines() if re.match(r"^\s*[+|]?[-=+|]{4,}[+|]?\s*$", l) or re.search(r"[┼├┤┬┴╋╠╣]", l)]
            self.add("UI-CLI-008", "PASS" if not grid else "FAIL", "table-borders",
                     "%d grid/border lines in output" % len(grid) if grid else "no table borders", "one record per line; no borders")
            if "--json" in longs:
                jr = self.run(listc + ["--json"])
                try:
                    json.loads(jr.text("out"))
                    self.add("UI-CLI-008", "PASS" if not jr.err.strip() else "FAIL", "json-output",
                             "--json parses; %d bytes on stderr" % len(jr.err), "with --json, stdout is exactly the JSON document")
                except ValueError as exc:
                    self.add("UI-CLI-008", "FAIL", "json-output", "--json output is not valid JSON: %s" % exc, "emit one JSON document on stdout")
            else:
                self.add("UI-CLI-008", "FAIL", "json-flag", "help lists no --json flag", "listing commands offer --json")
            if not IS_WIN:
                for envname, val in (("NO_COLOR", "1"), ("TERM", "dumb")):
                    pr = self.run(listc, env={envname: val}, use_pty=True)
                    self.add("UI-CLI-009", "PASS" if ESC not in pr.out else "FAIL", "tty-%s" % envname.lower(),
                             "%s=%s on a terminal: %s" % (envname, val, "no escape codes" if ESC not in pr.out else "escape codes emitted"),
                             "honour %s" % envname)
            else:
                self.add("UI-CLI-009", "N/A", "tty-no_color", "terminal colour tests need a pseudo-terminal; not available on Windows from here")
        else:
            self.human("UI-CLI-008", "list-command", "no list_command in the config; run a listing command piped to a filter: one record per line, --json parses?")

        for entry in cfg.get("failing", []):
            r = self.run(entry["args"])
            want = entry.get("exit")
            ok = r.exit_code not in (0, None) and (want is None or r.exit_code == want)
            self.add("UI-CLI-001", "PASS" if ok else "FAIL", "exit-map",
                     "%s -> exit %s%s" % (" ".join(entry["args"]), r.exit_code, (" (expected %s)" % want) if want is not None else ""),
                     "map each failure mode to a distinct non-zero code")
            self._check_error_text(r, stem)

        oo = cfg.get("option_order")
        if oo and len(oo) == 2:
            a, b = self.run(oo[0]), self.run(oo[1])
            ok = a.exit_code == b.exit_code == 0 and a.out == b.out
            self.add("UI-CLI-005", "PASS" if ok else "FAIL", "option-order",
                     "exit %s/%s, identical stdout: %s" % (a.exit_code, b.exit_code, a.out == b.out), "accept options and operands in any order")

        pc = cfg.get("positional_command")
        if pc:
            r = self.run(pc + ["--", "--zzz-looks-like-an-option"])
            bad = re.search(r"unknown|unrecogni[sz]ed|invalid option|no such option|not a valid", r.text("err"), re.I)
            self.add("UI-CLI-005", "PASS" if not bad else "FAIL", "double-dash",
                     "after `--`, an operand starting with -- was %s" % ("accepted" if not bad else "rejected as an option"),
                     "the first `--` ends option parsing")

        for entry in cfg.get("destructive", []):
            args = entry["args"]
            r = self.run(args)
            refused = r.exit_code not in (0, None) and not r.timed_out
            self.add("UI-CLI-015", "PASS" if refused else "FAIL", "destructive-refuses-unattended",
                     "%s with no terminal and no force flag: exit %s%s" % (" ".join(args), r.exit_code, " (hung)" if r.timed_out else ""),
                     "without a terminal and without --force/--confirm, refuse and name the flag")
            hr = self.run(args[:1] + ["--help"]) if self.multi else self.run(["--help"])
            _, hl = self.parse_options(hr.text("out"))
            has_force = bool(hl & {"--force", "--confirm", "--yes"})
            has_dry = "--dry-run" in hl
            self.add("UI-CLI-015", "PASS" if has_force else "FAIL", "destructive-force-flag",
                     "%s: force/confirm flag %s" % (args[0], "present" if has_force else "absent"), "offer --force or --confirm=<name> for scripts")
            self.add("UI-CLI-015", "PASS" if has_dry else "FAIL", "destructive-dry-run",
                     "%s: --dry-run %s" % (args[0], "present" if has_dry else "absent"), "offer -n/--dry-run")

        lr_cfg = cfg.get("long_running")
        if lr_cfg:
            budget = lr_cfg.get("first_output_ms", 100)
            r = self.run(lr_cfg["args"], interrupt_after=lr_cfg.get("interrupt_after_s", 1.0),
                         exit_within=lr_cfg.get("exit_within_s", 5.0), timeout=lr_cfg.get("interrupt_after_s", 1.0) + lr_cfg.get("exit_within_s", 5.0) + 5)
            if r.first_ms is None:
                self.add("UI-CLI-016", "FAIL", "first-output", "no output before the interrupt", "print what is about to happen before starting")
            else:
                self.add("UI-CLI-016", "PASS" if r.first_ms <= budget else "FAIL", "first-output",
                         "first output after %.0f ms (budget %d ms)" % (r.first_ms, budget), "print something within 100 ms")
            sig = "Ctrl-Break" if IS_WIN else "SIGINT"
            if r.timed_out:
                self.add("UI-CLI-017", "FAIL", "interrupt-exits", "did not exit within %.0fs of %s" % (lr_cfg.get("exit_within_s", 5.0), sig),
                         "exit as soon as possible on interrupt; add a timeout to clean-up")
            else:
                self.add("UI-CLI-017", "PASS", "interrupt-exits", "exited with %s after %s" % (r.exit_code, sig))
                self.add("UI-CLI-017", "PASS" if r.err.strip() or r.out.strip() else "FAIL", "interrupt-says-so",
                         "output after interrupt: %d bytes" % (len(r.err) + len(r.out)), "say something immediately on interrupt")
        else:
            self.human("UI-CLI-016", "first-output", "no long_running command in the config; time the first output of the slowest command")
            self.human("UI-CLI-017", "interrupt", "no long_running command in the config; press Ctrl-C during the longest operation")

        for args in cfg.get("reads_stdin", []):
            blob = b"x" * (1024 * 1024) + b"\n"
            r = self.run(args, stdin_data=blob, timeout=self.timeout * 3)
            crashed = r.exit_code is None or r.timed_out or (r.exit_code < 0 if not IS_WIN else (r.exit_code or 0) > 255)
            self.add("UI-CLI-023", "PASS" if not crashed else "FAIL", "long-line",
                     "1 MiB single line on stdin: exit %s%s" % (r.exit_code, " (hung)" if r.timed_out else ""),
                     "no arbitrary limits on line length")
            ur = self.run(args, stdin_data="héllo — ünïcode ✓\n".encode("utf-8"))
            self.add("UI-CLI-023", "PASS" if ur.exit_code not in (None,) and not ur.timed_out else "FAIL", "utf8-input",
                     "UTF-8 input: exit %s" % ur.exit_code, "handle multibyte input")

        # -- whole-session checks --------------------------------------------
        esc_runs = [r.label() for r in self.runs if ESC in r.out or ESC in r.err]
        self.add("UI-CLI-009", "PASS" if not esc_runs else "FAIL", "no-ansi-piped",
                 "escape codes with output piped in: %s" % (", ".join(esc_runs[:5]) if esc_runs else "none"),
                 "no colour or cursor codes when the stream is not a terminal")
        hung = [r.label() for r in self.runs if r.timed_out and not getattr(r, "interrupted", False)]
        self.add("UI-CLI-013", "PASS" if not hung else "FAIL", "no-hang-without-terminal",
                 "invocations that did not finish with stdin closed: %s" % (", ".join(hung[:5]) if hung else "none"),
                 "never wait for a prompt when stdin is not a terminal; report the missing flag and exit")
        self.add("UI-CLI-012", "PASS" if not hung else "FAIL", "no-pager-piped", "piped runs that waited: %d" % len(hung), "page only when stdout is a terminal")
        bad_utf8 = []
        for r in self.runs:
            for data in (r.out, r.err):
                try:
                    data.decode("utf-8")
                except UnicodeDecodeError:
                    bad_utf8.append(r.label())
        self.add("UI-CLI-023", "PASS" if not bad_utf8 else "FAIL", "utf8-output",
                 "output that is not valid UTF-8: %s" % (", ".join(bad_utf8[:5]) if bad_utf8 else "none"), "emit UTF-8")

        traces = [r.label() for r in self.runs if _looks_like_trace(r.text("err"))]
        self.add("UI-CLI-011", "PASS" if not traces else "FAIL", "no-stack-trace",
                 "stack traces on stderr in: %s" % (", ".join(traces[:5]) if traces else "none"),
                 "catch expected errors; write tracebacks to a file and print how to report the bug")

        # profile bookkeeping: the part of UI-CLI-024 a run can decide
        if not self.config:
            self.add("UI-CLI-024", "FAIL", "profile-config", "no --config given, so the config-driven checks did not run",
                     "write a config (see tools/cli_check.example.json) and name it in the profile")
        elif not cfg.get("profile"):
            self.add("UI-CLI-024", "FAIL", "profile-config", "the config names no profile",
                     "set \"profile\" in the config to the project and profile version this run belongs to")
        else:
            self.add("UI-CLI-024", "PASS", "profile-config", "config names profile %r" % cfg["profile"])
        self.human("UI-CLI-024", "posture-and-log", "is the surface classified `cli` in the profile's posture map, and is this run recorded in the review log?")

        # manual items the checker cannot decide
        self.human("UI-CLI-010", "state-change-output", "after a state-changing command, does the output say what is now true and what to run next?")
        self.human("UI-CLI-019", "config-precedence", "set one option by flag, environment and file: does flag > environment > project > user > system hold?")
        self.human("UI-CLI-021", "telemetry", "fresh install with a network monitor: any connection not caused by a command?")

    def _check_error_text(self, r, stem):
        err = r.text("err").strip()
        first = err.splitlines()[0] if err else ""
        if not first:
            return
        loglevel = re.match(r"^\s*(\[?(ERROR|ERR|WARN|WARNING|INFO|DEBUG|FATAL)\]?\s*[:\]-])", first, re.I)
        if loglevel and not re.match(r"^\s*error:\s", first, re.I):
            self.add("UI-CLI-011", "FAIL", "no-log-level-labels", "stderr starts with a log-level label: %r" % first[:80],
                     "stderr is a message to a person, not a log file")
        else:
            self.add("UI-CLI-011", "PASS", "no-log-level-labels", "first stderr line: %r" % first[:80])
        gnu = re.match(r"^\s*(%s|%s)[:\s]" % (re.escape(stem), re.escape(os.path.basename(self.command[0]))), first, re.I) or re.match(r"^\s*error:\s", first, re.I)
        if not gnu:
            self.human("UI-CLI-011", "error-prefix", "first stderr line %r does not start with the program name (GNU form `prog: message`) or an error title; is the reader told who is speaking?" % first[:60])
        if first.rstrip().endswith("."):
            self.add("UI-CLI-011", "FAIL", "error-no-trailing-period", "error line ends with a period: %r" % first[:80], "GNU: error messages do not end with a period")
        verdict = re.findall(r"\b(invalid|illegal|fatal|forbidden|bad)\b", err, re.I)
        if verdict:
            self.human("UI-CLI-011", "verdict-words", "error text uses %s; the writing module (UI-TEXT-003) replaces these with the specific problem" % ", ".join(sorted({v.lower() for v in verdict})))

    # -- baseline ------------------------------------------------------------

    def snapshot(self):
        shorts, longs = self.parse_options(self.help_text)
        return {"subcommands": sorted(self.subcommands), "options": sorted(longs | set(shorts))}

    def check_baseline(self, path):
        try:
            with io.open(path, encoding="utf-8") as fh:
                base = json.load(fh)
        except (OSError, ValueError) as exc:
            self.add("UI-CLI-020", "N/A", "baseline", "baseline not readable: %s" % exc)
            return
        now = self.snapshot()
        removed = sorted((set(base.get("subcommands", [])) - set(now["subcommands"])) | (set(base.get("options", [])) - set(now["options"])))
        added = sorted((set(now["subcommands"]) - set(base.get("subcommands", []))) | (set(now["options"]) - set(base.get("options", []))))
        self.add("UI-CLI-020", "PASS" if not removed else "FAIL", "baseline-diff",
                 "removed since baseline: %s; added: %s" % (", ".join(removed) or "none", ", ".join(added) or "none"),
                 "removing an interface needs a release that warned first")

    def check_stray_files(self, before):
        after = _listdir(self.workdir) | _listdir(self.exe_dir)
        new = sorted(after - before)
        allowed = set(self.config.get("allow_files", []))
        new = [n for n in new if os.path.basename(n) not in allowed]
        self.add("UI-CLI-019", "PASS" if not new else "FAIL", "no-stray-files",
                 "files created in the working directory or beside the executable: %s" % (", ".join(new[:5]) if new else "none"),
                 "write configuration, cache and logs to the per-user locations, not the working directory")


def _lev(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def _looks_like_trace(text):
    return bool(re.search(r"Traceback \(most recent call last\)|^\s+at [\w.$<>]+ ?\(.*:\d+\)|panicked at|Unhandled exception|Exception in thread|goroutine \d+ \[|^\s*#\d+ +0x[0-9a-f]+", text, re.M))


def _listdir(path):
    out = set()
    if not path or not os.path.isdir(path):
        return out
    for root, _dirs, files in os.walk(path):
        for f in files:
            out.add(os.path.join(root, f))
    return out


# ----------------------------------------------------------------------------
# reporting
# ----------------------------------------------------------------------------


def oracle_version():
    here = os.path.dirname(os.path.abspath(__file__))
    for cand in (os.path.join(here, "..", "VERSION"), os.path.join(here, "VERSION")):
        try:
            with io.open(cand, encoding="utf-8") as fh:
                return fh.read().strip()
        except OSError:
            continue
    return "unknown"


def report_text(findings, command, profile, quiet):
    lines = []
    counts = {s: 0 for s in STATUSES}
    for f in findings:
        counts[f.status] += 1
        if quiet and f.status == "PASS":
            continue
        lines.append("FINDING  %-11s %-21s check=%s" % (f.rule, f.status, f.check))
        lines.append("Evidence %s" % f.evidence)
        if f.fix and f.status == "FAIL":
            lines.append("Fix      %s" % f.fix)
        lines.append("")
    lines.append("Oracle version : %s" % oracle_version())
    lines.append("Modules        : cli")
    lines.append("Profile        : %s" % (profile or "-"))
    lines.append("Command        : %s" % " ".join(command))
    lines.append("Result         : %d PASS, %d FAIL, %d N/A, %d NEEDS HUMAN JUDGMENT" % (
        counts["PASS"], counts["FAIL"], counts["N/A"], counts["NEEDS HUMAN JUDGMENT"]))
    if counts["FAIL"]:
        lines.append("")
        lines.append("Next: fix the FAIL findings above, then run %s again." % PROG)
    return "\n".join(lines) + "\n", counts


def report_json(findings, command, profile):
    counts = {s: 0 for s in STATUSES}
    for f in findings:
        counts[f.status] += 1
    return json.dumps({"tool": PROG, "tool_version": VERSION, "oracle_version": oracle_version(), "module": "cli",
                       "profile": profile, "command": command, "findings": [f.as_dict() for f in findings],
                       "summary": counts}, indent=2, ensure_ascii=False) + "\n"


# ----------------------------------------------------------------------------
# entry point
# ----------------------------------------------------------------------------

EPILOG = """\
examples:
  %(prog)s -- mytool
      run the generic battery against `mytool` found on PATH
  %(prog)s --config mytool.cli_check.json -- mytool
      add the config-driven checks (exit-code map, destructive commands,
      long-running command, list command)
  %(prog)s --json -- mytool | jq '.summary'
      machine-readable report
  %(prog)s --write-baseline mytool.baseline.json -- mytool
      record the current options and subcommands; later runs with
      --baseline fail if any were removed

exit status: 0 no FAIL findings; 1 one or more FAIL; 2 usage or config
problem; 3 the command could not be found.

config file: JSON with any of the keys subcommands, list_command, failing
[{args, exit}], option_order [argsA, argsB], positional_command, destructive
[{args}], long_running {args, first_output_ms, interrupt_after_s,
exit_within_s}, reads_stdin [args...], aliases, allow_files, prompts,
profile. See tools/cli_check.example.json.

report bugs: %(home)s/issues
home page:   %(home)s
"""


def die(msg, code=2):
    sys.stderr.write("%s: %s\n" % (PROG, msg))
    return code


def main(argv=None):
    parser = argparse.ArgumentParser(prog=PROG, add_help=False,
                                     description="check a command-line program against the UI Oracle cli module",
                                     epilog=EPILOG % {"prog": PROG, "home": HOME_URL},
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     usage="%(prog)s [options] -- COMMAND [ARG...]")
    parser.add_argument("-h", "--help", action="help", help="show this help and exit")
    parser.add_argument("--version", action="version", version="%s %s" % (PROG, VERSION), help="print the version and exit")
    parser.add_argument("-c", "--config", metavar="FILE", help="JSON config for the command under test")
    parser.add_argument("-t", "--timeout", metavar="SECONDS", type=float, default=10.0, help="per-invocation timeout (default 10)")
    parser.add_argument("-b", "--baseline", metavar="FILE", help="compare options and subcommands with this snapshot")
    parser.add_argument("--write-baseline", metavar="FILE", help="write the current snapshot and exit")
    parser.add_argument("--json", action="store_true", help="report as JSON on stdout")
    parser.add_argument("-q", "--quiet", "--silent", action="store_true", dest="quiet", help="omit PASS findings from the text report")
    parser.add_argument("--no-color", action="store_true", help="accepted for convention; the report never uses colour")
    parser.add_argument("--no-input", action="store_true", help="accepted for convention; the tool never prompts")
    parser.add_argument("command", nargs=argparse.REMAINDER, metavar="COMMAND", help="the program to check, after --")
    ns = parser.parse_args(argv)

    command = [a for a in ns.command if a != "--"] if ns.command and ns.command[0] == "--" else ns.command
    if not command:
        sys.stderr.write("%s: no command given\n" % PROG)
        sys.stderr.write("usage: %s [options] -- COMMAND [ARG...]\nexample: %s -- mytool\nrun `%s --help` for the full list of options\n" % (PROG, PROG, PROG))
        return 2

    config = {}
    if ns.config:
        try:
            with io.open(ns.config, encoding="utf-8") as fh:
                config = json.load(fh)
        except (OSError, ValueError) as exc:
            return die("cannot read config %s: %s" % (ns.config, exc))
    if ns.timeout <= 0:
        return die("timeout must be positive")

    workdir = tempfile.mkdtemp(prefix="cli_check_")
    checker = Checker(command, config, ns.timeout, workdir, not ns.quiet)
    if checker.resolve() is None:
        return die("command not found: %s" % command[0], 3)

    before = _listdir(workdir) | _listdir(checker.exe_dir)
    if IS_WIN:
        prev = signal.signal(signal.SIGBREAK, signal.SIG_IGN)
    try:
        checker.check_all()
    finally:
        if IS_WIN:
            signal.signal(signal.SIGBREAK, prev)
    if ns.write_baseline:
        with io.open(ns.write_baseline, "w", encoding="utf-8") as fh:
            json.dump(checker.snapshot(), fh, indent=2, sort_keys=True)
        sys.stderr.write("%s: wrote baseline %s\n" % (PROG, ns.write_baseline))
    if ns.baseline:
        checker.check_baseline(ns.baseline)
    checker.check_stray_files(before)
    shutil.rmtree(workdir, ignore_errors=True)

    profile = config.get("profile")
    if ns.json:
        sys.stdout.write(report_json(checker.findings, command, profile))
        fails = sum(1 for f in checker.findings if f.status == "FAIL")
    else:
        text, counts = report_text(checker.findings, command, profile, ns.quiet)
        sys.stdout.write(text)
        fails = counts["FAIL"]
    return 1 if fails else 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.stderr.write("%s: interrupted\n" % PROG)
        sys.exit(130)
