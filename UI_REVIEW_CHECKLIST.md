# UI Review Checklist

Work through this against a proposed UI, a screenshot, or a diff. Answer each
item **PASS**, **FAIL**, **N/A**, or **NEEDS HUMAN JUDGMENT** — or **N/A
(TOOLKIT)** where an enabled toolkit module states that the toolkit cannot
implement the rule (`UI_ORACLE_CONTRACT.md` §5).

Rules for using it honestly:

- Cite the rule ID with every FAIL, and say whether it is a **platform
  requirement** (Tier 1), an **interaction-design principle** (Tier 2/3), or a
  **project convention**. Those carry different weight in an argument.
- Use **NEEDS HUMAN JUDGMENT** rather than guessing. Anything needing a
  measurement you have not taken, a decision about product direction, or a
  LOW-confidence rule belongs there.
- Use **N/A** freely; most reviews touch a fraction of this list.
- If nothing in the oracle covers the concern, say so. Do not invent a rule.

---

## 0. Before anything else

| # | Question | Rule |
|---|---|---|
| 0.1 | Is the posture of this surface identified — sovereign or transient? | `UI-GLOBAL-001` |
| 0.2 | Does the density and control sizing match that posture? | `UI-LAY-001`, `UI-ARCH-001` |
| 0.3 | Is this the primary repeated workflow, or occasional? | `UI-CMD-001` |

If 0.1 cannot be answered, stop. Most of what follows depends on it.

For a surface the profile classifies as `cli`, 0.1 is answered by the
classification and the first question is instead the `cli` module's: is this
output read by a person at a terminal, or by another program? Sections 1–11
apply where they make sense; §12d is the form for the rest.

---

## 0b. Foundations (Norman's seven principles)

Cheap to check, and they catch problems the specific sections assume away.

| # | Question | Rule |
|---|---|---|
| 0b.1 | From a static screenshot, can you list what actions are possible here? | `UI-GLOBAL-005` |
| 0b.2 | From the same screenshot, can you tell what state it is in? | `UI-GLOBAL-005` |
| 0b.3 | Does something perceivable mark each interactive element — not hover, not colour alone? | `UI-GLOBAL-006` |
| 0b.4 | Could a new user say what the objects are and how they relate? | `UI-GLOBAL-007` |
| 0b.5 | Is each control adjacent to, or visibly connected to, what it changes? | `UI-GLOBAL-008` |
| 0b.6 | Does the effect follow soon enough to be attributed to the action? | `UI-GLOBAL-008`, `UI-FB-001` |
| 0b.7 | For each warning or confirmation: could a constraint have prevented it instead? | `UI-GLOBAL-009` |

---

## 1. Architecture and layout

| # | Question | Rule |
|---|---|---|
| 1.1 | Does visual prominence match task importance? | `UI-LAY-003` |
| 1.2 | Is grouping carried by proximity/alignment before borders and cards? | `UI-LAY-002` |
| 1.3 | With all borders removed, is the grouping still legible? | `UI-LAY-002` |
| 1.4 | Does every pane define resize behaviour and a minimum size? | `UI-LAY-004` |
| 1.5 | At minimum window size, is every command still reachable? | `UI-LAY-004` |
| 1.6 | Does late-arriving content avoid moving anything clickable? | `UI-LAY-005` |
| 1.7 | Does workspace state persist across sessions? | `UI-ARCH-002` |
| 1.8 | Is navigation chrome justified by more than one destination? | `UI-NAV-001` |
| 1.9 | Do controls stay put between visits (no adaptive reordering)? | `UI-NAV-002` |
| 1.10 | If several top-level windows exist, what parallel task/display need earns each one? | `UI-ARCH-004` |
| 1.11 | Does density preserve simultaneous comparison without sacrificing grouping, legibility, focus or text scaling? | `UI-LAY-001` |

## 2. Commands

| # | Question | Rule |
|---|---|---|
| 2.1 | Are constantly needed commands directly visible, not nested? | `UI-CMD-001`, `UI-CMD-003` |
| 2.2 | Does each canvas command earn its space by frequency? | `UI-CMD-001` |
| 2.3 | Does every command have a second route besides the context menu? | `UI-CMD-004` |
| 2.4 | Is the same action named, iconed and shortcut identically everywhere? | `UI-GLOBAL-003` |
| 2.5 | Are destructive commands separated from frequent ones? | `UI-CMD-005` |
| 2.6 | Is every destructive command either undoable or confirmed? | `UI-CMD-005`, `UI-DLG-003` |
| 2.7 | Do disabled commands make their precondition discoverable? | `UI-CMD-006` |

## 3. Keyboard and pointer

| # | Question | Rule |
|---|---|---|
| 3.1 | Can the primary loop be completed with no mouse? | `UI-KBD-001` |
| 3.2 | Does tab order follow visual reading order? | `UI-KBD-002` |
| 3.3 | Does tabbing ever land on something non-actionable? | `UI-KBD-003` |
| 3.4 | Does Escape mean "leave without applying" in every state? | `UI-KBD-004` |
| 3.5 | Are shortcuts shown beside their commands? | `UI-KBD-005` |
| 3.6 | Are controls near the content they act on (pointer travel)? | `UI-MOUSE-001` |
| 3.7 | Any frequent command behind a third-level submenu or narrow corridor? | `UI-MOUSE-002` |
| 3.8 | Is anything reachable *only* by hover? | `UI-MOUSE-003` |
| 3.9 | Does touch support avoid coarsening the pointer layout? | §25 |

## 4. Selection, focus, modes

| # | Question | Rule |
|---|---|---|
| 4.1 | Is keyboard focus always visible? | `UI-SEL-001` |
| 4.2 | Are keyboard focus, object selection, active/current state, hover and text caret visually distinguishable? | `UI-SEL-001` |
| 4.3 | Does selection survive scrolling, pane toggles, background completion? | `UI-SEL-002` |
| 4.4 | Do multiple representations of one object highlight together? | `UI-SEL-003`, `UI-OCR-001` |
| 4.5 | Do click / Ctrl+click / Shift+click behave conventionally? | `UI-SEL-004` |
| 4.6 | Can the active mode be named from a screenshot alone? | `UI-MODE-001` |
| 4.7 | Is the mode indicator near the work, not only in a distant bar? | `UI-MODE-001` |
| 4.8 | Can any mode be entered accidentally? | `UI-MODE-002` |
| 4.9 | If focus, selected item and inspected item differ, can the user identify all three? | `UI-SEL-001` |
| 4.10 | For multi-selection, are set membership and anchor/lead item unambiguous? | `UI-SEL-001`, `UI-SEL-004` |
| 4.11 | Can an exceptional mode be held/spring-loaded or scoped to an object instead of persisting globally? | `UI-MODE-003` |

## 5. Editing

| # | Question | Rule |
|---|---|---|
| 5.1 | Are reversible edits immediate with undo, rather than confirmed? | `UI-EDIT-001` |
| 5.2 | Does editing keep the surrounding context visible? | `UI-EDIT-002` |
| 5.3 | Does every edit mode define commit and cancel? | `UI-EDIT-003` |
| 5.4 | Is validation in place and non-blocking? | `UI-EDIT-004` |
| 5.5 | Does undo cover the primary workflow, multi-level? | `UI-EXP-003` |

## 6. Feedback and asynchronous work

| # | Question | Rule |
|---|---|---|
| 6.1 | Does every action produce visible acknowledgement within ~0.1 s? | `UI-FB-001` |
| 6.2 | Is busy vs idle always distinguishable? | `UI-FB-002` |
| 6.3 | For work beyond a few seconds: determinate progress or remaining work/time when knowable? | `UI-FB-003` |
| 6.4 | Is every long operation cancellable, with cancel acknowledged at once? | `UI-FB-004` |
| 6.5 | Does background work leave the rest of the UI interactive? | `UI-FB-005` |
| 6.6 | Is status reported in the UI rather than by interruption? | `UI-FB-006` |
| 6.7 | Does a busy/progress animation reflect real work rather than continue after a hang? | `UI-FB-002` |
| 6.8 | Can a late background result overwrite newer selection or edits? | `UI-FB-005`, `UI-SEL-002` |

## 7. Dialogs

| # | Question | Rule |
|---|---|---|
| 7.1 | Is there a stated reason this must block? | `UI-DLG-001` |
| 7.2 | Is the guarded action genuinely unrecoverable? | `UI-DLG-003` |
| 7.3 | Modeless surfaces: task-specific commit verb and Close, not OK/Cancel? | `UI-DLG-002` |
| 7.4 | Are Enter and Escape both defined? | `UI-DLG-004` |
| 7.5 | Is the default button non-destructive? | `UI-DLG-005` |

## 8. Typography

| # | Question | Rule |
|---|---|---|
| 8.1 | Does every size come from the Windows type ramp? | `UI-TYPO-001` |
| 8.2 | Is all text ≥ 14px Semibold / 12px Regular? | `UI-TYPO-002` |
| 8.3 | Emphasis by Semibold, no italic in UI text? | `UI-TYPO-003` |
| 8.4 | Left-aligned and sentence case? | `UI-TYPO-004` |
| 8.5 | Is running prose within 50–60 characters per line? | `UI-TYPO-005` |
| 8.6 | Does truncation match container definition? | `UI-TYPO-006` |
| 8.7 | One font family, plus per-script fonts only where needed? | `UI-TYPO-007` |

## 9. Icons and colour

| # | Question | Rule |
|---|---|---|
| 9.1 | Are icon-only controls confined to surfaces whose posture earns them? | `UI-ICON-001` |
| 9.2 | Does every icon-only control have an accessible name? | `UI-ICON-002` |
| 9.3 | Are standard actions using Segoe Fluent Icons? | `UI-ICON-003` |
| 9.4 | Is text contrast ≥ 4.5:1 in **both** themes? | `UI-COLOR-001` |
| 9.5 | Have both light and dark been checked, not just derived? | `UI-COLOR-002` |
| 9.6 | In greyscale, is every state still distinguishable? | `UI-COLOR-003` |
| 9.7 | Is accent reserved for important or interactive elements? | `UI-COLOR-004` |
| 9.8 | Are semantic colours defined as roles, not literals? | `UI-COLOR-005` |

## 10. Accessibility

| # | Question | Rule |
|---|---|---|
| 10.1 | Is every command keyboard-reachable with visible focus? | `UI-A11Y-001` |
| 10.2 | Static text in Text roles, editable text in Edit roles? | `UI-A11Y-002` |
| 10.3 | Usable at text scale up to 2.25×, nothing clipped? | `UI-A11Y-003` |
| 10.4 | Is any information available only as rendered pixels? | `UI-A11Y-004` |
| 10.5 | Does anything rely on high-contrast mode as its fix? | `UI-COLOR-001` |

## 11. Expert workflow

| # | Question | Rule |
|---|---|---|
| 11.1 | Is this optimised for the intermediate rather than the first run? | `UI-EXP-001` |
| 11.2 | Is repeating the last operation cheap? | `UI-EXP-002` |
| 11.3 | Counting one loop: how much is the task, how much is overhead? | `UI-GLOBAL-004` |

## 12. OCR-specific (module `ocr` — only when the profile opts in; all DERIVED)

| # | Question | Rule |
|---|---|---|
| 12.1 | Is region↔text correspondence perceptual rather than inferred? | `UI-OCR-001` |
| 12.2 | Is the source image visible while correcting text? | `UI-OCR-002`, `UI-ARCH-003` |
| 12.3 | Is low confidence findable in one scan, and in greyscale? | `UI-OCR-003` |
| 12.4 | Is recognised text editable, and failure not blamed on the user? | `UI-OCR-004`, `UI-ERR-003` |
| 12.5 | Does lookup preserve the line, its position and the selection? | `UI-OCR-005` |

`UI-OCR-006` is retired. Review learning state only when the adopting project's
profile defines a project-specific rule for it.

## 12a. User-visible text — delegated

Every string on the surface is governed by `UI_COPY_REVIEW_CHECKLIST.md`, which
applies `UX_WRITING_ORACLE.md` and `ERROR_MESSAGE_ORACLE.md`. Run it, and
record its result line here rather than duplicating its items.

| # | Question | Rule |
|---|---|---|
| 12a.1 | Has the copy review been run, and is its result recorded? | `UX-TEXT-*`, `UX-ERR-*` |
| 12a.2 | For each message on this surface: should it exist at all, and is its severity class and surface right? | `UX-ERR-001` … `UX-ERR-003` |
| 12a.3 | Is `TERMINOLOGY.md` filled in for the concepts named here? | `UX-TEXT-017` |
| 12a.4 | Does any primary copy carry implementation diagnostics? | `UX-ERR-012` |

§12b below remains the sentence-level sweep for the `writing` module. It is
not duplicated by the copy checklist; the two are cumulative.

## 12b. Writing (module `writing` — only when the profile opts in)

Read every string the surface shows. These are cheap to check and the
findings are usually the first thing an operator notices.

| # | Question | Rule |
|---|---|---|
| 12b.1 | Does each problem message say what happened, what it means, what to do — and nothing else? Count the sentences | `UI-TEXT-001` |
| 12b.2 | Does it name the specific object, value or cause, where the program knows it? | `UI-TEXT-002` |
| 12b.3 | Search the strings for *error, invalid, illegal, failed, fatal, forbidden, bad*. Any hit is a finding | `UI-TEXT-003` |
| 12b.4 | Is the operator ever the grammatical subject of a mistake? | `UI-TEXT-003` |
| 12b.5 | For each *please*: what inconvenience? For each *sorry*: what loss? | `UI-TEXT-004` |
| 12b.6 | With the icon covered, can you tell a problem from a warning from a question? Uncovered, do they agree? | `UI-TEXT-005` |
| 12b.7 | Read it aloud to someone outside the project. Which words would they not say? | `UI-TEXT-006` |
| 12b.8 | Is the verb first, present, and the instruction imperative? | `UI-TEXT-007` |
| 12b.9 | Is the transport's own text folded away, and does the fold reveal something new? | `UI-TEXT-008` |
| 12b.10 | Sentence case; full stop on sentences only; no capitals for emphasis; no exclamation marks | `UI-TEXT-009` |
| 12b.11 | Would each number, as written, appear on an instrument for that quantity? | `UI-TEXT-010` |
| 12b.12 | Is the on-screen string the same string as the log line for the same event? If so, which reader is short-changed? | `UI-TEXT-011` |
| 12b.13 | Do the buttons answer the title? Is *OK* dismissing a problem? | `UI-TEXT-012` |
| 12b.14 | One condition, every place it is reported — diff the strings | `UI-TEXT-013` |
| 12b.15 | Does any instruction say *click*, *tap*, *press* or *type* where a neutral verb would do? | `UI-TEXT-014` |
| 12b.16 | After a state change, can the operator say what is now true without moving? Was obvious success announced anyway? | `UI-TEXT-015` |

## 12c. Dear ImGui (module `imgui` — only when the profile opts in)

Read the module's applicability table first: it says which core rules are
reported `N/A (TOOLKIT)` and which are answered here instead.

| # | Question | Rule |
|---|---|---|
| 12c.1 | Does the profile name the ImGui branch and version, and list the toolkit-limited rules as known non-conformance? | `UI-IMGUI-001` |
| 12c.2 | Is `NavEnableKeyboard` set, and is no working window or needed item flagged `NoNavInputs`/`NoNav`? | `UI-IMGUI-002` |
| 12c.3 | Tab through both themes: is the navigation cursor visible on every item, legible, and distinct from hover and selection? | `UI-IMGUI-003` |
| 12c.4 | Across `SameLine` rows and tables, does Tab follow reading order? | `UI-IMGUI-004` |
| 12c.5 | With the ID-conflict highlighter on, any popup on any screen? Do changing labels use `###`? | `UI-IMGUI-005` |
| 12c.6 | Every modal: does Escape cancel, does Enter run a non-destructive default, is the default item focused? | `UI-IMGUI-006` |
| 12c.7 | During the slowest operation, does the UI keep animating and does cancel respond? Any `ImGui::` call on a worker thread? | `UI-IMGUI-007` |
| 12c.8 | Idle with nothing changing: is the process consuming as if busy? | `UI-IMGUI-008` |
| 12c.9 | DPI awareness declared? Sharp at 200%? Any hard-coded pixel sizes in UI code? | `UI-IMGUI-009` |
| 12c.10 | Which font file ships? Is the smallest rendered size at the lowest supported scale at or above the floor? | `UI-IMGUI-010` |
| 12c.11 | Is there a persisted text-scale setting, and is every command reachable at 2.25× at minimum window size? | `UI-IMGUI-011` |
| 12c.12 | Every icon-only control: does its tooltip appear from keyboard navigation? Does a disabled one say why? | `UI-IMGUI-012` |
| 12c.13 | Are both palettes measured at 4.5:1 or better? Does the tool follow the OS theme, or at least offer the choice? | `UI-IMGUI-013` |
| 12c.14 | Grep `IM_COL32` and `ImVec4(` in UI code: roles or literals? | `UI-IMGUI-014` |
| 12c.15 | Where is the settings file written? Launch from another directory: same layout? Delete it and launch: the designed layout? | `UI-IMGUI-015` |
| 12c.16 | Drag from empty space inside a pane: did the pane move? | `UI-IMGUI-016` |
| 12c.17 | For each menu shortcut label, press the chord with the menu closed: does it run? | `UI-IMGUI-017` |
| 12c.18 | Can an error's detail, an identifier or a path be copied without retyping? | `UI-IMGUI-018` |
| 12c.19 | Focus a text field and type every hotkey letter: anything but text? | `UI-IMGUI-019` |
| 12c.20 | If the profile lists a non-Latin script: IME at the caret, glyphs present, a literal checked with `DebugTextEncoding`? | `UI-IMGUI-020` |
| 12c.21 | Release build: force a recoverable toolkit error. What does the operator see, and what is logged? | `UI-IMGUI-021` |

## 12d. Command line (module `cli` — only when the profile opts in)

**Run the checker first.** `python tools/cli_check.py --config <config> --
<command>` decides most of this section automatically and prints its findings
in the format below. The contract requires a clean run — zero FAIL — for a
project that enables this module (§6). Work through the table for the items
the checker reports as NEEDS HUMAN JUDGMENT, and to satisfy yourself that its
config describes the real program.

Automatic items name the check that decides them. Run everything twice where
it matters: once in a terminal, once with stdin and stdout redirected.

| # | Question | Rule | Check |
|---|---|---|---|
| 12d.1 | Zero on success, non-zero on every failure, distinct codes per failure mode, never an error count? | `UI-CLI-001` | `exit-*` |
| 12d.2 | Product on stdout only, messaging on stderr only, a child's stderr passed through? | `UI-CLI-002` | `streams-*` |
| 12d.3 | `-h`, `--help`, `help`, `help <sub>`, `<sub> --help`, and `--help` after other arguments — all print help on stdout and exit 0? | `UI-CLI-003` | `help-flags`, `help-anywhere`, `help-subcommand` |
| 12d.4 | Bare invocation lists subcommands or prints concise help, never a default action and never a wait? | `UI-CLI-003` | `help-bare` |
| 12d.5 | Help carries a usage line, every flag described, at least one example, and a bug address; all within 80 columns? | `UI-CLI-003` | `help-content`, `help-width` |
| 12d.6 | `--version` prints `name version` on stdout, parses, ignores other arguments, exits 0? Is `-V` accepted? | `UI-CLI-004` | `version-*` |
| 12d.7 | Every short option has a long form; conventional names carry conventional meanings; `--quiet`/`--silent` synonymous? | `UI-CLI-005` | `long-forms`, `standard-names`, `quiet-silent-synonym` |
| 12d.8 | Options accepted in any order and after operands? Does the first `--` end option parsing? Is `-` stdin/stdout? | `UI-CLI-005` | `option-order`, `double-dash` |
| 12d.9 | One kind of positional operand, two at most and justified, never three? Output files named by `-o`? | `UI-CLI-006` | `positionals` |
| 12d.10 | Unknown option and unknown subcommand: non-zero, stderr only, nothing on stdout, no default action? | `UI-CLI-007` | `unknown-flag`, `unknown-subcommand` |
| 12d.11 | Is a guessed correction suggested and *not* run? | `UI-CLI-007` | `suggestion`, `suggestion-not-run` |
| 12d.12 | One record per line, no borders, `--json` valid, `--plain` where the layout breaks, `-q` present? Same content piped as on screen? | `UI-CLI-008` | `table-borders`, `json-*` |
| 12d.13 | No escape codes when piped; `NO_COLOR`, `TERM=dumb` and `--no-color` honoured; no animation off a terminal? | `UI-CLI-009` | `no-ansi-piped`, `tty-*`, `accepts--no-color` |
| 12d.14 | After a state-changing command: what is now true, and what to run next? | `UI-CLI-010` | manual |
| 12d.15 | Error lines in the form `program: message`, lower case, no trailing period, naming the object and the system error? | `UI-CLI-011` | `error-prefix`, `error-no-trailing-period` |
| 12d.16 | No log-level labels and no stack traces on stderr by default; the decisive line last; a trace file and a bug path for the unexpected? | `UI-CLI-011` | `no-log-level-labels`, `no-stack-trace` |
| 12d.17 | Paging only when both stdin and stdout are a terminal, and never for one screenful? | `UI-CLI-012` | `no-pager-piped` |
| 12d.18 | No prompt without a terminal; `--no-input` accepted; every prompt has a flag; passwords not echoed? | `UI-CLI-013` | `no-hang-without-terminal`, `accepts--no-input` |
| 12d.19 | No secret taken as a flag value or from the environment? | `UI-CLI-014` | `secrets-in-flags` |
| 12d.20 | Each destructive command: right grade, refuses unattended, has `--force`/`--confirm=<name>` and `--dry-run`? | `UI-CLI-015` | `destructive-*` |
| 12d.21 | `--version` under 500 ms; something printed within 100 ms of starting slow work; a stall distinguishable from a crash? | `UI-CLI-016` | `startup-time`, `first-output` |
| 12d.22 | Interrupt: immediate acknowledgement, prompt exit, clean-up timed out, a second interrupt forces and was advertised? | `UI-CLI-017` | `interrupt-*` |
| 12d.23 | Same flag means the same everywhere; no catch-all; no arbitrary prefixes; no two similar names for different things? | `UI-CLI-018` | `no-catch-all`, `no-abbreviation`, `similar-names` |
| 12d.24 | Nothing written to the working directory or beside the executable; per-user locations used; `TMPDIR` honoured? | `UI-CLI-019` | `no-stray-files` |
| 12d.25 | Precedence flag > environment > project > user > system? Standard environment names honoured, not commandeered? | `UI-CLI-019` | manual |
| 12d.26 | Against the recorded baseline: any subcommand, flag or key removed without a release that warned first? | `UI-CLI-020` | `baseline-diff` |
| 12d.27 | Fresh install with a network monitor: any connection not caused by a command? | `UI-CLI-021` | manual |
| 12d.28 | Name lower-case, two to nine characters, and behaviour independent of the name invoked? | `UI-CLI-022` | `name-*` |
| 12d.29 | A very long line, NUL bytes and UTF-8 survive input and output without truncation? | `UI-CLI-023` | `long-line`, `utf8-*` |
| 12d.30 | Posture map classifies the surface `cli`, the profile names the checker config, and the run is in the review log? | `UI-CLI-024` | manual |

## 13. Anti-pattern sweep

Scan `UI_ANTIPATTERNS.md` AP-01…AP-30, and `UX_WRITING_ORACLE.md` §E for
AP-31…AP-39 (the generated-text patterns). For each one present, state the
*condition* that makes it harmful here — or record it as acceptable with the
reason. Presence alone is not a finding.

---

## Reporting format

```
FINDING  <rule-id>  <PASS|FAIL|N/A|N/A (TOOLKIT)|NEEDS HUMAN JUDGMENT>
Surface  <which surface, and its posture>
Class    <platform requirement | interaction principle | project convention>
Verify   <VERIFIED | VERIFIED WITH QUALIFICATION | DERIVED | PROJECT-SPECIFIC>
Evidence <what was observed>
Source   <the citation from the oracle rule>
Fix      <smallest change that would pass, or the question a human must answer>
```

A review that reports only FAILs is incomplete: record the PASSes that were
checked, so the next reviewer knows what has already been looked at.
