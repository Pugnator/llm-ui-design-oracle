# Domain module: cli — command-line programs

**Module ID:** `cli`
**Requires:** UI Oracle core >= 4.0.0
**Status:** stable
**Opt in:** list `cli` under `modules` in your project profile and classify
each command-line surface as `cli` in the posture map. A project that also
enables `writing` binds `UI-TEXT-*` to every string the program prints.

Rule IDs in this module use the `UI-CLI-` prefix, reserved for it by the core
(`UI_ORACLE_CONTRACT.md`, namespace table).

---

## Why a module, and why it is strict

The core's first question — sovereign or transient? — has no answer for a
command-line program. A CLI has a different first question, and its sources
state it: *"The most simple and straightforward heuristic for whether a
particular output stream (stdout or stderr) is being read by a human is
whether or not it's a TTY"* (`CLIG`, Output). Everything about a CLI's
behaviour branches on that: colour, prompts, progress, pagers, output format.

This module is stricter than the rest of the oracle, for two reasons. First,
a command line is a **contract with other programs** as much as an interface
for people: exit codes, streams, option syntax and stable output are relied
on by scripts that cannot ask what was meant, so a convention broken here
breaks somebody's automation silently. The sources say so in their own
words: *"Your software will become a part in a larger system — your only
choice is over whether it will be a well-behaved part"* (`CLIG`,
Philosophy), and *"these are all interfaces, and you're committing to keeping
them working"* (`CLIG`, Future-proofing). Second, the conventions are old,
written down, and **mechanically checkable** — which the GUI rules mostly
are not. So nearly every rule here is a MUST, and every rule names the
automatic check that decides it or says plainly that a person must.

## The automatic gate

`tools/cli_check.py` runs the checks marked *automatic* below against a real
binary and reports one finding per check in the contract's format. Under the
contract (§6, *Automated modules*), a project claiming any conformance level
with `cli` enabled MUST have a checker run with **zero FAIL** on record in its
profile's review log, and the profile MUST name the checker's config file.
A FAIL is a defect; a NEEDS HUMAN JUDGMENT is an open question for the
reviewer; N/A is a check the platform could not perform (the checker says
which and why).

```
python tools/cli_check.py --config myproject.cli_check.json -- mytool
```

The checker follows this module itself and is checked with it.

## The sources, and how they were reconciled

Five bodies of guidance, read in full. `corpus/cli/README.md` records where
each is archived or, where the licence forbids archiving, the hash of the
page that was read.

| ID | Source | Tier | What it contributes |
|---|---|---|---|
| `POSIX-12` | IEEE Std 1003.1-2017, Chapter 12 *Utility Conventions* | 1 (standard) | The fourteen Utility Syntax Guidelines: option form, grouping, `--`, `-` for stdin/stdout, order independence, utility names of two to nine lower-case characters |
| `GNU-STD` | GNU Coding Standards, ch. 4 *Program Behavior for All Programs* | 2 | Long options for every short one and the table of standard long names; `--help` and `--version` semantics down to the format of the first line; the error-message format `program: message`; no arbitrary limits; exit status is not an error count; `TMPDIR`; behaviour independent of output device |
| `CLIG` | Command Line Interface Guidelines (clig.dev) | 2 | The TTY heuristic; help, output, errors, flags, interactivity, subcommands, robustness, signals, configuration, future-proofing, naming, analytics — the widest single source, and the one the others converge on |
| `12F-CLI` | Jeff Dickey, *12 Factor CLI Apps* | 2 | All the ways help must be reachable; `-h`/`--help` reserved; one kind of positional fine, two suspect, three never; `--version`/`-V`; stdout is for output, stderr for messaging; the five parts of an error; no ANSI in logs; start-up time budget; no table borders; XDG and the Windows equivalent |
| `HEROKU-CLI` | Heroku CLI Style Guide | 2 | Flags over args with the `fork` example; prompts always bypassable; descriptions that fit 80 columns; grep-parseable rows; `--json`; do not change stdout after general availability; actions on stderr; colour disabled by `--no-color`, `COLOR=false`, or no TTY |

They disagree in three places, each recorded in `UI_CONFLICTS.md`: where the
decisive line of an error goes (`C13`), how confirmation works without undo
(`C17`), whether an error line starts with a label (`C18`), and whether
behaviour may depend on the output device (`C19`). Everything else they say
in different words.

`CLIG` bounds the module's scope: it *"doesn't cover full-screen terminal
programs like emacs and vim"* — those are sovereign surfaces under the core —
and *"if you are creating a GUI program, this guide is not for you."*

---

## A. The contract with the shell

### UI-CLI-001 — Exit status: zero on success, a distinct non-zero code per failure, never a count
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

A program MUST exit zero on success and non-zero on any failure. Distinct
failure modes MUST map to distinct codes. The exit status MUST NOT be a count
of errors. `--help` and `--version` MUST exit zero.

**Rationale.** *"Exit codes are how scripts determine whether a program
succeeded or failed, so you should report this correctly. Map the non-zero
exit codes to the most important failure modes"* (`CLIG`, The Basics). *"Do
not use a count of errors as the exit status for a program. That does not
work, because exit status values are limited to 8 bits (0 through 255). A
single run of the program might have 256 errors … the parent process will
see 0"* (`GNU-STD` 4.2). `--help` and `--version` *"exit successfully"*
(`GNU-STD` 4.8.1, 4.8.2).

**Automatic check.** `exit-success-help`, `exit-success-version`,
`exit-failure`, `exit-map` (from the config's `failing` list).

---

### UI-CLI-002 — Output to stdout, messaging to stderr
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

The program's product MUST go to standard output and only there; log lines,
progress, warnings, actions in progress and errors MUST go to standard error
and only there. Machine-readable output goes to stdout. A child process's
stderr MUST be passed through to the user.

**Rationale.** *"Send output to stdout … this is where piping sends things by
default. Send messaging to stderr … when commands are piped together, these
messages are displayed to the user and not fed into the next command"*
(`CLIG`, The Basics). *"In short: stdout is for output, stderr is for
messaging … If you run a subcommand in your CLI, make sure you pipe the stderr
of that subcommand up to the user always"* (`12F-CLI` §4). *"Actions are
displayed on stderr because they are out-of-band information on a running
task"*; *"Stdout should be used for all output and stderr for warning, errors
and out of band information"* (`HEROKU-CLI`). Help and version text are
output: `GNU-STD` puts both *"on standard output"*.

**Automatic check.** `streams-help`, `streams-version`, `streams-error`.

---

### UI-CLI-003 — Help is reachable every way, fits the screen, and leads with examples
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

`-h` and `--help` MUST print help on stdout and exit zero, from any position
on the command line and for every subcommand; once seen, other arguments are
ignored. `-h` MUST mean help and nothing else. A multi-command program MUST
also accept `help` and `help <subcommand>`. A bare invocation MUST list the
subcommands (multi-command) or print concise help (single-command) and MUST
NOT run a default action or wait. Help MUST contain a usage line, a
description, every flag with a description, at least one example, and — near
the end — where to report bugs and the home page. Descriptions MUST begin
lower-case, MUST NOT end in a period, and help MUST fit 80 columns.

**Rationale.** *"You can't control what the user inputs so all of these must
show help"*: `mycli`, `mycli --help`, `mycli help`, `mycli -h`, `mycli
subcommand --help`, `mycli subcommand -h`; *"-h,--help should be a reserved
flag used for help only"*; *"most importantly: provide examples of common
usage"* (`12F-CLI` §1). *"Ignore any other flags and arguments that are
passed — you should be able to add -h to the end of anything and it should
show help. Don't overload -h"*; *"Lead with examples"*; *"Display the most
common flags and commands at the start of the help text"*; *"Provide a support
path for feedback and issues"* (`CLIG`, Help). *"Near the end of the '--help'
option's output, please place lines giving the email address for bug reports,
the package's home page"* (`GNU-STD` 4.8.2). *"if the user doesn't pass
anything arguments to the CLI, it's always better to list the subcommands (for
multi) or display the help (for single) rather than do some default
behavior"* (`12F-CLI` §11). Descriptions *"should fit on 80 character width
screens, begin with a lowercase character, and should not end in a period"*
(`HEROKU-CLI`, Description).

**Automatic check.** `help-flags`, `help-anywhere`, `help-subcommand`,
`help-bare`, `help-content`, `help-width`.

---

### UI-CLI-004 — `--version` prints a parseable first line and does nothing else
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

`--version` MUST print the program's canonical name and version on stdout,
the version number after the last space of the first line, and exit zero,
ignoring other arguments. `-V` MUST be accepted; `-v` MUST also mean version
unless the program uses it for `--verbose`. A multi-command program MUST also
accept `version`. The remaining lines MAY carry copyright, licence and the
extra facts a bug report needs.

**Rationale.** *"The standard --version option should direct the program to
print information about its name, version, origin and legal status, all on
standard output, and then exit successfully. Other options and arguments
should be ignored … The first line is meant to be easy for a program to
parse; the version number proper starts after the last space … The
program's name should be a constant string; don't compute it from argv[0]"*
(`GNU-STD` 4.8.1). *"Ensure you can get the CLI version through any of the following"* — the
code block lists `mycli version`, `mycli --version` and `mycli -V` — and
*"It's frustrating to run 3 different commands to get the version for a CLI
until you find the right one"*; *"The version command is a
main place you'll ask users for debugging information"* (`12F-CLI` §3).

**Automatic check.** `version-flag`, `version-ignores-args`.

---

### UI-CLI-005 — Option syntax follows POSIX and GNU: short, grouped, long-named, order-free, `--`
**Level:** MUST **Authority:** Tier 1 (standard) + Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

Short options MUST be a single `-` and one alphanumeric character; options
without arguments MUST be groupable behind one `-`; an option-argument MUST
NOT be optional. Every short option MUST have a long form beginning `--`, and
where a conventional long name exists (`--verbose`, `--quiet` with `--silent`
as a synonym, `--output`, `--force`, `--dry-run`, `--all`, `--recursive`,
`--interactive`, `--debug`, `--version`, `--help`) it MUST be used with its
conventional meaning and its conventional letter. The order of options
relative to one another MUST NOT matter; options MUST be accepted before and
after operands; the first `--` MUST end option parsing. `-` as a file operand
MUST mean stdin or stdout.

**Rationale.** `POSIX-12` Utility Syntax Guidelines 3–14: *"Each option name
should be a single alphanumeric character"*; *"All options should be preceded
by the '-' delimiter character"*; *"One or more options without
option-arguments, followed by at most one option that takes an
option-argument, should be accepted when grouped behind one '-'"*;
*"Option-arguments should not be optional"*; *"The first -- argument that is
not an option-argument should be accepted as a delimiter indicating the end
of options"*; *"The order of different options relative to one another should
not matter"*; *"the '-' operand should be used to mean only standard input
(or standard output …)"*. POSIX's own note that its utilities *"shall
conform completely to these guidelines as if these guidelines contained the
term 'shall' instead of 'should'"* is the level this rule takes. `GNU-STD`
4.8: *"Please define long-named options that are equivalent to the
single-letter Unix-style options … users should be able to expect the
'verbose' option of any GNU program which has one, to be spelled precisely
'--verbose'"*, with the table of long options; 4.1: GNU permits
*"intermixing of options with ordinary arguments"*, which this rule adopts
because *"the most common things users do … is to hit the up arrow to get
the last invocation, stick another option on the end, and run it again"*
(`CLIG`, Arguments and flags). *"Have full-length versions of all flags"*;
*"Use standard names for flags, if there is a standard"*; *"If input or
output is a file, support - to read from stdin or write to stdout"* (`CLIG`).
`12F-CLI` §2: *"the flag parser should accept a -- argument to denote that
it should stop parsing"*.

**Automatic check.** `long-forms`, `standard-names`,
`quiet-silent-synonym`, `option-order` (config), `double-dash` (config).

---

### UI-CLI-006 — Flags over arguments; one kind of operand, never three
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

Input MUST be taken through named flags except for one kind of positional
operand whose meaning is obvious (the file to act on, repeated for many
files). Two kinds of positional operand are a finding to justify; three MUST
NOT occur. Output files MUST be named by `-o`/`--output`, not by position.
A prompt or a positional MUST have a flag equivalent.

**Rationale.** *"A good rule of thumb is 1 type of argument is fine, 2 types
are very suspect, and 3 are never good. For variable length arguments, it's
fine to have multiple arguments"* (`12F-CLI` §2). *"Flags are preferred to
args … `heroku fork destapp -a sourceapp` … confusing to the user since it
isn't clear which app they are forking from and which one they are forking
to"* (`HEROKU-CLI`, Flags). *"Prefer flags to args … If you've got two or
more arguments for different things, you're probably doing something wrong.
The exception is a common, primary action"* (`CLIG`). *"It is usually a good
idea for file names given as ordinary arguments to be input files only; any
output files would be specified using options (preferably '-o' or
'--output')"* (`GNU-STD` 4.8).

**Automatic check.** `positionals` (counts operand kinds in the usage
lines; two is NEEDS HUMAN JUDGMENT, three is FAIL).

---

### UI-CLI-007 — Wrong input is an error; a guess is suggested, never run
**Level:** MUST **Authority:** Tier 2 + Tier 4 **Confidence:** HIGH
**Provenance:** SOURCE RULE

An unknown option or subcommand MUST fail: non-zero exit, message on stderr,
nothing on stdout, no default action. Where the intended command can be
guessed the program MUST say so and MAY offer to run it, but MUST NOT run it
unasked.

**Rationale.** *"If the user did something wrong and you can guess what they
meant, suggest it … You can ask if they want to run the suggested command,
but don't force it on them"*; a wrong command *"can often mean the user has
made a logical mistake, or misused a shell variable. Assuming what they meant
can be dangerous, especially if the resulting action modifies state"*, and
*"if you change what the user typed, they won't learn the correct syntax"*
(`CLIG`, Help). *"In the case of $ mycli subcommand help … it's better to
only show the help if it would otherwise error out with an invalid argument
error"* (`12F-CLI` §1). The core's `UI-ERR-002` and `UI-ERR-003` give the
reasons: a slip and a mistake need different remedies, and the program's
guess is the program's responsibility.

**Automatic check.** `unknown-flag`, `unknown-subcommand`,
`suggestion-not-run`, `suggestion`.

---

## B. Output

### UI-CLI-008 — Rows a person can read and `grep`; `--json` for structure; no borders
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

Human output MUST put one record on one line so that `grep` and `wc` work on
it, MUST NOT draw table borders, and SHOULD show column headers that can be
hidden. A command that lists or reports data MUST offer `--json`, and MUST
offer `--plain` (or `--terse`) wherever the human layout breaks one record
per line. `-q`/`--quiet` MUST suppress non-essential output. The data and its
meaning MUST NOT depend on whether the output is a terminal; only its
presentation may.

**Rationale.** *"It's important that each row of your output is a single
'entry' of data. Never output table borders. It's noisy and a huge pain for
parsing … you can do things like pipe to wc to get the count of lines, or
grep to filter each line"* (`12F-CLI` §8). *"Human-readable output should be
grep-parseable, but not necessarily awk-parseable … commands should offer a
--json and/or a --terse flag when valuable"* (`HEROKU-CLI`). *"Have
machine-readable output where it does not impact usability … If
human-readable output breaks machine-readable output, use --plain … Display
output as formatted JSON if --json is passed"*; *"provide a -q option to
suppress all non-essential output"* (`CLIG`, Output). `GNU-STD` 4.5: *"don't
make the behavior of a command-line program depend on the type of output
device"* — reconciled with the TTY heuristic in `C19`: what varies is
presentation, never content.

**Automatic check.** `table-borders`, `json-output`, `json-flag` (all from
the config's `list_command`).

---

### UI-CLI-009 — Colour and motion only for a terminal, never alone, and switchable off
**Level:** MUST **Authority:** Tier 2 + Tier 1 **Confidence:** HIGH
**Provenance:** SOURCE RULE

Colour MUST NOT be the only carrier of a meaning (`UI-COLOR-003`). Colour and
any cursor-moving output — spinners, progress bars, redrawn lines — MUST be
disabled when the stream is not a terminal (stdout and stderr checked
separately), when `NO_COLOR` is set and non-empty, when `TERM` is `dumb`, or
when `--no-color` is passed; `--no-color` MUST be accepted. Log files MUST
NOT contain escape codes. Red MUST be reserved for problems.

**Rationale.** *"Disable color if your program is not in a terminal or the
user requested it"*, with the list: not a TTY, `NO_COLOR` *"set and it is
not empty (regardless of its value)"*, `TERM` *"has the value dumb"*,
`--no-color`; *"If stdout is not an interactive terminal, don't display any
animations. This will stop progress bars turning into Christmas trees in CI
log output"*; *"The eye will be drawn to red text, so use it intentionally
and sparingly"* (`CLIG`, Output; Errors). *"Spinners and progress bars are
also not a good idea when it's not a tty … You never want to output those
codes to a file … Respect this if TERM=dumb, NO_COLOR is set, or if they
specify --no-color"*; error logs *"don't contain ansi color codes"*
(`12F-CLI` §5, §6). *"Yellow and red … typically are saved for errors and
warning messages. Color can be disabled by the user by adding --no-color,
setting COLOR=false, or when the output is not a tty"* (`HEROKU-CLI`,
Colors).

**Automatic check.** `no-ansi-piped` (every invocation), `accepts--no-color`,
`tty-no_color` and `tty-term` (POSIX only, under a pseudo-terminal; N/A on
Windows).

---

### UI-CLI-010 — Say what changed, show the state, name the next command
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

A command that changes state MUST say what it changed, in terms of the
result. Where state is not visible in the filesystem, a command MUST exist to
show it. Where commands form a workflow, output MUST name the command to run
next. Success output MUST be brief. Actions that cross the program's
boundary — files not named on the command line, network — MUST be explicit.

**Rationale.** *"If you change state, tell the user … so the user can model
the state of the system in their head"*; *"Make it easy to see the current
state of the system"*; *"Suggest commands the user should run"*; *"Display
output on success, but keep it brief"*; *"Actions crossing the boundary of
the program's internal world should usually be explicit"* (`CLIG`, Output).
`UI-TEXT-015` carries the wording; this rule carries the obligation.

**Automatic check.** Manual (`state-change-output`): the checker cannot know
which commands change state.

---

### UI-CLI-011 — Errors are for people: prefixed, specific, actionable, and not a trace
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

An expected error MUST be caught and restated. A non-interactive program's
error line MUST take the form `program: message` (or `program:file:line:
message`), lower-case after the prefix, no trailing period. The message MUST
name the object and include the system's error text where a system call
failed, MUST say how to fix it where that is known, and SHOULD give a URL for
more. The line that tells the operator what to do goes **last**. Repeated
errors of one kind MUST be grouped. Stderr MUST NOT carry log-level labels
or stack traces by default; an unexpected error writes its trace to a file
and prints how to report it. A `DEBUG` environment variable or `--debug`
turns the detail on.

**Rationale.** `GNU-STD` 4.4: *"Error messages from other noninteractive
programs should look like this: program:sourcefile:lineno: message … or
program: message … The string message should not begin with a capital letter
when it follows a program name … Also, it should not end with a period"*;
4.2: *"Include the system error text (from strerror, or equivalent) in every
error message resulting from a failing system call, as well as the name of
the file if any and the name of the utility. Just 'cannot open foo.c' or
'stat failed' is not sufficient."* `12F-CLI` §5: a great error has, as five bullets, an *"Error code"*, an
*"Error title"*, an *"Error description (Optional)"*, *"How to fix the
error"* and a *"URL for more information"*; for the unexpected, *"have a way to view full
traceback information as well as full debug output"*. `CLIG`, Errors:
*"Catch errors and rewrite them for humans"*; *"Signal-to-noise ratio is
crucial … consider grouping them under a single explanatory header"*; *"Put
the most important information at the end of the output"*; *"Consider
writing the debug log to a file instead of printing it to the terminal"*;
Output: *"Don't treat stderr like a log file … Don't print log level labels
(ERR, WARN, etc.)"*. On the `Error:` title `12F-CLI` shows and `CLIG`
forbids, see `C18`: the program-name prefix is the required form, a
single title line is tolerated, a level label is not.

**Automatic check.** `no-log-level-labels`, `error-no-trailing-period`,
`no-stack-trace` (every invocation), `error-prefix` (NEEDS HUMAN JUDGMENT
when the GNU form is absent), `verdict-words` (NEEDS HUMAN JUDGMENT; the
`writing` module's word list).

---

### UI-CLI-012 — Page only for a person
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

A command that emits more than a screen MUST page it only when both stdin
and stdout are a terminal and MUST NOT page otherwise; the pager MUST NOT
engage for output that fits one screen and MUST leave the output on screen
when it exits.

**Rationale.** *"Use a pager (e.g. less) if you are outputting a lot of text
… Use a pager only if stdin or stdout is an interactive terminal. A good
sensible set of options to use for less is less -FIRX. This does not page if
the content fills one screen … and leaves the contents on the screen when
less quits"* (`CLIG`, Output).

**Automatic check.** `no-pager-piped` (no piped invocation may wait).

---

## C. Input

### UI-CLI-013 — Prompt only a terminal, never require a prompt, honour `--no-input`
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

The program MUST NOT prompt unless stdin is a terminal, and MUST NOT prompt
when `--no-input` is passed; `--no-input` MUST be accepted by any program
that ever prompts. A missing value MUST be reported with the flag that
supplies it. Every value a prompt can collect MUST also be passable as a
flag or operand. A password prompt MUST NOT echo.

**Rationale.** *"Only use prompts or interactive elements if stdin is an
interactive terminal"*; *"If --no-input is passed, don't prompt … If the
command requires input, fail and tell the user how to pass the information as
a flag"*; *"Never require a prompt"*; *"don't print it as the user types"*
(`CLIG`, Interactivity; Arguments and flags). *"if stdin is a tty then
prompt rather than forcing the user to specify a flag. Never require a
prompt though. The user needs to be able to automate your CLI in a script"*
(`12F-CLI` §7). *"if prompting is required to complete a command, this means
the user will not be able to script the command. Ensure that args or flags
can always be provided to bypass the prompt"* (`HEROKU-CLI`, Prompting).

**Automatic check.** `no-hang-without-terminal` (every invocation runs with
stdin closed and must finish), `accepts--no-input`.

---

### UI-CLI-014 — Secrets never on the command line or in the environment
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

A secret MUST NOT be accepted as a flag value or read from an environment
variable. It is read from a file named by a flag, from stdin, or from
another IPC channel.

**Rationale.** *"Do not read secrets directly from flags … the flag value
will leak the secret into ps output and potentially shell history"*;
*"Do not read secrets from environment variables … they have proven too
prone to leakage"*; *"Secrets should only be accepted via credential files,
pipes, AF_UNIX sockets, secret management services, or another IPC
mechanism"* (`CLIG`, Arguments and flags; Environment variables).

**Automatic check.** `secrets-in-flags` (help scanned for value-taking
`--password`, `--token`, `--secret`, `--api-key`, `--credential` flags;
`-file`, `-stdin` and `-path` variants are the accepted forms).

---

### UI-CLI-015 — Danger is confirmed in proportion, always scriptably, with a dry run
**Level:** MUST **Authority:** Tier 2 + Tier 1 **Confidence:** HIGH
**Provenance:** SOURCE RULE

A destructive command MUST behave according to the scale of the loss: a
small local change MAY proceed when the command's own name says what it
does; a larger local or any remote change MUST confirm on a terminal and
MUST take `-f`/`--force` when there is none; a severe loss MUST be hard to
confirm by accident — typing the name of the thing, or `--confirm=<name>`
for scripts. Every destructive command MUST offer `-n`/`--dry-run`. Without
a terminal and without the force flag it MUST refuse and name the flag.
Non-obvious paths to destruction MUST be treated as severe.

**Rationale.** The three grades are `CLIG`'s (Arguments and flags): *"Mild …
if the user is explicitly running a command called something like 'delete,'
you probably don't need to ask. Moderate … You usually want to prompt for
confirmation here. Consider giving the user a way to 'dry run' … Severe …
make it hard to confirm by accident. Consider asking them to type something
non-trivial such as the name of the thing they're deleting. Let them
alternatively pass a flag such as --confirm="name-of-thing", so it's still
scriptable"*; *"changing a number in a configuration file from 10 to 1 means
that 9 things will be implicitly deleted — this should be considered a severe
risk"*. `12F-CLI` §7: *"when destroying a Heroku app, you'll need to type the
app name again to confirm"*. `-f` is *"'-f' in cp, ln, mv, and rm"* and
`--dry-run` *"'-n' in make"* (`GNU-STD` 4.10). Reconciled with the core's
"confirm only the unrecoverable" in `C17`.

**Automatic check.** `destructive-refuses-unattended`,
`destructive-force-flag`, `destructive-dry-run` (from the config's
`destructive` list).

---

## D. Time and signals

### UI-CLI-016 — Start in under half a second; print something within 100 ms of starting slow work
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

`--version` and `--help` MUST complete in under 500 ms. Before work that
will not finish immediately — a network request, a large read — the program
MUST print what it is about to do within 100 ms. Work that takes long MUST
show progress, and a stalled progress display MUST be distinguishable from
a crash (time remaining, or continued animation).

**Rationale.** *"CLIs need to start quickly … <100ms: very fast … 100ms–500ms:
fast enough, aim here … 500ms-2s: usable, but not going to impress anyone …
2s+: languid, users will prefer to avoid your CLI at this point"* (`12F-CLI`
§9). *"Responsive is more important than fast. Print something to the user in
<100ms. If you're making a network request, print something before you do it
so it doesn't hang and look broken"*; *"If the progress bar gets stuck in one
place for a long time, the user won't know if stuff is still happening or if
the program's crashed. It's good to show estimated time remaining, or even
just have an animated component"* (`CLIG`, Robustness). The 100 ms figure is
the same order as Johnson's 0.1 s deadline in `UI-FB-001`, reached
independently.

**Automatic check.** `startup-time`, `first-output` (from the config's
`long_running` command).

---

### UI-CLI-017 — Interrupt: acknowledge at once, exit promptly, a second one forces
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

On the interrupt signal the program MUST say something immediately and exit
as soon as it can; clean-up MUST have a timeout; a second interrupt during
clean-up MUST skip it, and the program MUST have said what a second one does
if that is destructive. Interrupt MUST work during network waits. A program
that wraps another so that Ctrl-C cannot quit MUST say how to get out.
Network operations MUST time out by default, configurably. The program MUST
be safe to start after an interrupted run.

**Rationale.** *"If a user hits Ctrl-C (the INT signal), exit as soon as
possible. Say something immediately, before you start clean-up. Add a timeout
to any clean-up code so it can't hang forever … If a user hits Ctrl-C during
clean-up operations that might take a long time, skip them. Tell the user
what will happen when they hit Ctrl-C again"*; *"If your program hangs on
network I/O etc, always make Ctrl-C still work"*; *"Make things time out"*;
*"Make it recoverable … Make it crash-only"*; *"Your program should expect to
be started in a situation where clean-up has not been run"* (`CLIG`, Signals
and control characters; Interactivity; Robustness).

**Automatic check.** `interrupt-exits`, `interrupt-says-so` (from the
config's `long_running` command; on Windows the checker sends Ctrl-Break to
the process group, which a well-behaved program treats as Ctrl-C, and says
so in the evidence).

---

## E. Structure, configuration and change

### UI-CLI-018 — Subcommands: consistent, unambiguous, explicit, and never guessed
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

Across subcommands the same flag name MUST mean the same thing. Two-level
commands MUST keep one ordering and one set of verbs; the root of a topic
lists its nouns and there is no separate `list` command. No two subcommands
MAY have similar names for different things. There MUST NOT be a catch-all
subcommand, and the program MUST NOT accept arbitrary unambiguous prefixes;
aliases are explicit, documented and stable.

**Rationale.** *"Be consistent across subcommands. Use the same flag names
for the same things"*; *"Be consistent with the verbs you use across
different types of objects"*; *"Don't have ambiguous or similarly-named
commands … 'update' and 'upgrade'"* (`CLIG`, Subcommands). *"Don't have a
catch-all subcommand … now you can never add a subcommand named echo — or
anything at all — without risking breaking existing usages"*; *"Don't allow
arbitrary abbreviations of subcommands … There's nothing wrong with aliases
… but they should be explicit and remain stable"* (`CLIG`, Future-proofing).
*"the root command of a topic usually lists those nouns … Never create a
*:list command such as heroku config:list"* (`HEROKU-CLI`, Naming the
command).

**Automatic check.** `no-catch-all`, `no-abbreviation`, `similar-names`
(NEEDS HUMAN JUDGMENT for names within two edits).

---

### UI-CLI-019 — Configuration is layered, lives in the per-user place, and touches nothing else
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

Configuration MUST be applied in the precedence: flags, then the shell's
environment, then project configuration, then user configuration, then
system configuration. Per-invocation choices are flags; per-machine ones are
environment variables; per-project ones a version-controlled file. User
configuration, data and cache MUST live in the platform's per-user locations
— the XDG directories where they apply, `%LOCALAPPDATA%` for cache on
Windows — never in the working directory, never beside the executable, never
a new dot-file in the home directory. Temporary files MUST honour `TMPDIR`.
The program MUST NOT modify configuration it does not own without consent.
Environment variable names MUST be upper-case letters, digits and
underscores; the general-purpose names (`NO_COLOR`, `DEBUG`, `EDITOR`,
`HTTP_PROXY`, `TMPDIR`, `HOME`, `PAGER`, `LINES`, `COLUMNS`) MUST be honoured
and not commandeered.

**Rationale.** The precedence list, the three categories and their
mechanisms, *"Follow the XDG-spec"*, *"If you automatically modify
configuration that is not your program's, ask the user for consent"*, the
naming constraint and the general-purpose list are `CLIG` (Configuration;
Environment variables). *"use ~/.config/myapp for config files, and
~/.local/share/myapp for data files. For cache files though, use
~/.cache/myapp on Unix … On Windows you can use %LOCALAPPDATA%\myapp"*
(`12F-CLI` §12). *"If you make temporary files, check the TMPDIR environment
variable"* (`GNU-STD` 4.2); files *"modified for internal purposes"* do not
belong in the installation tree (`GNU-STD` 4.13).

**Automatic check.** `no-stray-files` (every run happens in a fresh
directory; anything left there or beside the executable is a FAIL);
`config-precedence` is manual.

---

### UI-CLI-020 — Interfaces are contracts: add, warn, then change
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

Subcommands, flags, configuration keys, environment variables and
machine-readable output are interfaces. Changes MUST be additive; a
non-additive change MUST be preceded by a release that warns when the old
form is used, names the new form, and is silent once the user has switched.
Human-readable output MAY change; machine-readable output MUST NOT change
incompatibly after general availability.

**Rationale.** *"these are all interfaces, and you're committing to keeping
them working … Keep changes additive where you can … Warn before you make a
non-additive change … Changing output for humans is usually OK"* (`CLIG`,
Future-proofing). *"commands do not change their inputs and stdout after
general availability in ways that will break current scripts. Generally this
means additional information is OK, but modifying existing output is
problematic"* (`HEROKU-CLI`).

**Automatic check.** `baseline-diff` (`--write-baseline` records the
options and subcommands; a later run with `--baseline` fails on any
removal).

---

### UI-CLI-021 — No telemetry without consent
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

The program MUST NOT send usage or crash data without the operator's consent,
MUST disclose what it collects and why, and MUST make it easy to disable;
opt-in is the default.

**Rationale.** *"Do not phone home usage or crash data without consent. Users
will find out, and they will be angry … Ideally, ask users whether they want
to contribute data ('opt-in')"* (`CLIG`, Analytics).

**Automatic check.** Manual (`telemetry`): network monitoring is outside
the checker.

---

### UI-CLI-022 — The name is lower-case, short, and does not change behaviour
**Level:** MUST (case) / SHOULD (length) **Authority:** Tier 1 (standard) + Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

The executable name MUST be lower-case letters and digits, with a dash only
where unavoidable, and SHOULD be two to nine characters. Behaviour MUST NOT
depend on the name the program was invoked by.

**Rationale.** *"Utility names should be between two and nine characters,
inclusive … should include lowercase letters … and digits only"* (`POSIX-12`
Guidelines 1–2). *"Use only lowercase letters, and dashes if you really need
to … Keep it short … Make it easy to type"* (`CLIG`, Naming). *"Please don't
make the behavior of a utility depend on the name used to invoke it"*
(`GNU-STD` 4.5).

**Automatic check.** `name-lowercase`, `name-length` (NEEDS HUMAN JUDGMENT
outside two to nine).

---

### UI-CLI-023 — No arbitrary limits; bytes preserved; UTF-8 in and out
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

The program MUST NOT impose arbitrary limits on the length or number of
lines, file names, files or symbols, and MUST NOT silently truncate. Input
MUST pass through NUL and non-printing bytes. Text MUST be handled as UTF-8
and output MUST be valid UTF-8. Every failing system call MUST be reported
with the system's error text and the file name.

**Rationale.** *"Avoid arbitrary limits on the length or number of any data
structure, including file names, lines, files, and symbols … In most Unix
utilities, 'long lines are silently truncated'. This is not acceptable"*;
*"Utilities reading files should not drop NUL characters, or any other
nonprinting characters. Programs should work properly with multibyte
character encodings, such as UTF-8"*; *"Check every system call for an error
return"* (`GNU-STD` 4.2). *"Validate user input … Check early and bail out
before anything bad happens, and make the errors understandable"* (`CLIG`,
Robustness).

**Automatic check.** `long-line` and `utf8-input` (from the config's
`reads_stdin` list), `utf8-output` (every invocation).

---

### UI-CLI-024 — The `cli` posture and the review's first question
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

A profile that enables this module MUST classify each command-line surface as
`cli` in its posture map, MUST name the checker config file, and MUST record
each checker run in the review log. A review of a `cli` surface MUST begin
with the module's question — read by a person at a terminal, or by a
program? — and MUST apply every rule above in both cases.

**Rationale.** The TTY heuristic is the sources' shared premise (`CLIG`,
Output; `12F-CLI` §6; `HEROKU-CLI`, Colors), and `GNU-STD` 4.5 is the reason
both cases must be reviewed: the content must be the same in each. The
contract's gate (§6) is what makes the module's strictness checkable rather
than aspirational.

**Automatic check.** The checker's own summary block records the run; the
profile entries are manual.

---

## What this module deliberately does not say

- **Windows console mechanics.** Virtual-terminal sequences, the legacy
  console host and PowerShell conventions were not covered by any source
  read; `12F-CLI` supplies only the `%LOCALAPPDATA%` cache location. The
  checker's terminal-colour tests are therefore N/A on Windows and the matrix
  lists the gap.
- **Full-screen terminal programs.** Out of `CLIG`'s scope; the core's
  sovereign rules apply, with `UI-CLI-009` for colour and `UI-CLI-017` for
  Ctrl-C.
- **Distribution and packaging.** `CLIG`'s single-binary advice and
  `12F-CLI`'s contribution guidance are about the project, not the
  interface.
- **Wording.** Every string the program prints is governed by the `writing`
  module where enabled; this module says where a line goes and what it must
  contain, not how it reads.

## Anti-patterns this module adds

See `UI_ANTIPATTERNS.md` AP-29 (the Christmas tree in the log) and AP-30 (the
mandatory prompt).
