# UI Evidence

Evidence layer between the raw corpus and `UI_ORACLE.md`. It records what the
sources say before the oracle synthesizes a rule. Page numbers are book pages
unless explicitly marked “PDF page.” EPUB locations use chapter, heading and
the EPUB's printed page markers. No quotation or location below comes from
memory.

## Question: What architecture fits a professional desktop workspace?

### Local evidence

- `AF4`, Ch. 9, “Sovereign posture,” book pp. 207–218 (PDF pp. 237–248):
  sovereign applications dominate long sessions, often fill the screen, and may
  use multiple adjacent panes for navigation and supporting information. Users
  spend relatively little of their lifetime as beginners; frequent/intermediate
  use can justify compact auxiliary controls and a conservative visual style.
- `AF4`, Ch. 18, “Sidebars,” book p. 457 (PDF p. 487): sidebars let users
  manipulate object or document properties without modal/modeless dialogs and
  streamline complex authoring workflows.
- `DI3`, Ch. 2, “Designing for Task and Workflow-Dominant Apps,” book pp. 33–34:
  frequent items should be immediately available; experienced users can work
  efficiently with densely packed information/selectors, shortcuts,
  customization and keyboard-only input. Ch. 2 also identifies Canvas Plus
  Palette and Many Workspaces as established visual-editor patterns.
- `DI3`, Ch. 4, “Collapsible Panels,” book pp. 249–253: supporting modules may
  be opened together and can return space to primary content when closed.

### Interpretation

A stable, pane-capable workspace is supported for this class of tool. Neither
book establishes a universal pane count, docking side or default layout.
Persistent pane state is a reasoned reduction of excise, not a quoted platform
requirement.

### Oracle rules

`UI-ARCH-001` … `UI-ARCH-004`, `UI-LAY-001`, `UI-EXP-001`.
Confidence: HIGH for posture and panes; MEDIUM for persistence and the precise
multi-window policy.

## Question: When should multiple windows be used?

### Local evidence

- `AF4`, Ch. 18, “Windows on the Desktop,” book pp. 439–444 (PDF pp. 469–474):
  multiple windows on a small screen are not a good general solution, though
  they have important occasional uses; window-management overhead can become
  excise.
- `DI3`, Ch. 2, “Visual editors,” book pp. 80–83: applications of this class
  often provide Many Workspaces so documents/states can be worked on in
  parallel.

### Interpretation

These positions differ by task and display, not by a simple yes/no rule. A
single coherent workspace is the default for one document/task. Deliberate
multi-document or multi-monitor work may justify extra top-level windows. A
routine command must not spawn one merely to organize ordinary controls.

### Oracle rule

`UI-ARCH-004`. Confidence: MEDIUM. See conflict C10.

## Question: How should dense interfaces trade space for comprehension?

### Local evidence

- `AF4`, Ch. 9, book pp. 211–214 (PDF pp. 241–244): compact controls are
  appropriate in frequently used sovereign applications; transient interfaces
  need larger, precisely labeled controls.
- `DI3`, Ch. 4, “Density,” book pp. 212–213: density is spacing between screen
  elements; the book's less-dense example is harder to read and harder to group.
  “Proximity,” pp. 217–218, says closeness communicates relationship and
  isolation communicates distinction.
- `DI3`, Ch. 2, book p. 34: experienced users can be fast and efficient in
  complicated interfaces densely packed with information and selectors.
- `JM3`, Chs. 2–3: proximity/common region and visual hierarchy make structure
  perceptible and scannable.

### Interpretation

Whitespace is a relational signal, not a virtue measured by volume. High
density is justified when simultaneous comparison and repeated expert work save
context switches; low density is justified for infrequent sequential decisions.
Both fail when grouping, hierarchy, typography or accessibility fails.

### Oracle rules

`UI-LAY-001` … `UI-LAY-003`, `UI-GLOBAL-002`. Confidence: HIGH. No numeric
density, gap or pane-count rule is supported.

## Question: How should frequent commands be exposed?

### Local evidence

- `DI3`, Ch. 2, book p. 33: frequent workflow tasks, controls and commands
  should be immediately available; infrequent settings/help may be hidden.
- `DI3`, Ch. 8, book pp. 378–380: some users never think to look in context
  menus; menu bars can remain valuable for accessibility; shortcuts and tab
  order support experienced and keyboard-only users.
- `AF4`, Ch. 18, “Menus” and “Accelerators,” book pp. 448–454: menus explain
  functions and provide stable command locations; displaying keyboard
  equivalents beside commands teaches the faster route.
- `JM3`, Chs. 9, 11 and 13: recognition is easier than recall; consistent
  practice builds learned operation; pointing cost depends on target distance
  and size.
- `MS-COMMAND`: frequent core commands belong on canvas/persistent command
  surfaces; direct manipulation is preferred where suitable.

### Interpretation

Frequency selects exposure. Context menus and direct manipulation are useful
routes, but cannot monopolize a repeated or accessibility-relevant command. A
desktop expert path and a discoverable path should coexist.

### Oracle rules

`UI-CMD-001` … `UI-CMD-006`, `UI-KBD-001`, `UI-KBD-005`.
Confidence: HIGH for frequency and keyboard access; MEDIUM for explanatory
tooltips on disabled commands.

## Question: What are selection, focus and related states?

### Local evidence

- `DI3`, Ch. 1, “Keyboard Only,” book pp. 23–25: keyboard focus is the control
  that receives keyboard input; Tab/Shift+Tab move it. List selection can be
  changed by keyboard and modifiers.
- `DI3`, Ch. 8, book pp. 379–380: a single click conventionally selects an
  object for a later command; tab focus selects a UI component to receive
  keyboard commands. The text sometimes uses “focus” and “selection” loosely,
  so semantic disambiguation is necessary in the oracle.
- `DI3`, Ch. 2, book p. 113: an Excel example distinguishes a selected tool from
  a temporarily hovered/highlighted tool.
- `AF4`, Ch. 18, “Pointing, Selection, and Direct Manipulation,” book p. 480
  (PDF p. 510): selection state should be visually evident and unambiguous.
- `DI3`, Ch. 7, book p. 335: multiple selection should use platform conventions
  such as Shift-selection or visible checkboxes.

### Interpretation

The semantic states are not interchangeable:

| State | Meaning | Required question |
|---|---|---|
| Keyboard focus | Destination of the next keyboard input | Where will a key go? |
| Selected object(s) | Object set a command will act on | What will Delete/Copy/etc. affect? |
| Active/current object | Object governing context, even if selection is elsewhere | Which document/region owns the active tools? |
| Hover | Temporary pointer location | What is under the pointer? |
| Text caret | Insertion point inside editable text | Where will typed text be inserted? |
| Inspected item | Object whose properties/details are displayed | What does the inspector describe? |
| OCR region/token | Domain selection at different granularities | Which source/text unit is the current subject? |
| Multi-selection | A set, potentially with an anchor/lead item | What is in the set, and which item anchors range extension? |

One element may hold several states at once, but one visual treatment must not
stand for different meanings. The exact visuals are a later design decision.

### Oracle rules

`UI-SEL-001` … `UI-SEL-004`. Confidence: HIGH for visible selection and
keyboard focus semantics; MEDIUM for the derived full state model.

## Question: How should multiple representations stay coordinated?

### Local evidence

- `DI3`, Ch. 9, “Data Brushing,” book pp. 458–460: selecting items in one view
  should show those same data selected simultaneously in another. Coordinated
  views can synchronize selection, zoom and panning and thereby reinforce that
  the views are perspectives on the same data.
- `JM3`, Ch. 2: similarity, proximity and common fate provide perceptual
  grouping. Ch. 7 warns against requiring users to remember system status.
- `DI3`, Ch. 9, book pp. 439–440: overview plus detail helps orientation;
  linked search results preserve spatial context.

### Interpretation

This is direct support for linked selection. Transferring it from charts/tables
to image region, OCR string, token, reading, dictionary entry, meaning,
translation and annotation is derived but structurally equivalent. Selection
propagation must not silently change edit focus or collapse a multi-selection.

### Oracle rules

`UI-SEL-003`, `UI-ARCH-003`, `UI-OCR-001`, `UI-OCR-002`, `UI-OCR-005`.
Confidence: HIGH for coordinated views; MEDIUM for OCR application.

## Question: How should modes behave if the product has them?

### Local evidence

- `JM3`, Ch. 7, “Modes,” book pp. 114–115: modes reduce controls/gestures but
  burden working memory; people make errors when they forget the mode. Clear,
  continuous feedback is required even when users entered the mode themselves.
- `JM3`, Ch. 15, “Mode slips,” book pp. 267–269: indicate status clearly and
  strongly; consider returning to normal after a unit-task timeout or reentry;
  make exceptional modes spring-loaded; avoid modes when separate controls do
  not create worse description slips.
- `AF4`, Ch. 18, “Modal tools and palettes,” book pp. 494–496 (PDF pp. 524–526):
  modal tools can introduce a small toolset well but scale poorly for
  intermediate users as switching excise grows; cursor changes indicate the
  active tool and shortcuts can mitigate switching cost.

### Interpretation

Modes are a tradeoff, not an automatic defect. If used, entry and exit must be
deliberate, status must be strong and local to the work, and exceptional modes
should be transient/spring-loaded when that fits the task. The oracle does not
mandate OCR modes or exact Escape behavior for every control.

### Oracle rules

`UI-MODE-001` … `UI-MODE-003`, `UI-KBD-004`. Confidence: HIGH for mode
feedback and spring-loading; MEDIUM for a universal exit policy.

## Question: How should editing, undo and confirmation interact?

### Local evidence

- `DI3`, Ch. 8, book p. 379: double-clicking text may conventionally mean edit
  in place. Ch. 8, pp. 418–424 covers multilevel undo and command history.
- `JM3`, Ch. 15, book pp. 270–273: make actions reversible, provide undo, make
  risky operations hard, and avoid destructive default confirmations because
  confirmations become automatic capture sequences.
- `AF4`, Ch. 15, book pp. 363–375: undo should follow the user's mental model
  and support reversible histories. Ch. 21, book pp. 625–640: dialogs are
  secondary, appropriate for dangerous, rare or out-of-flow functions; they
  should not become the primary interface.
- `MS-COMMAND`: confirm actions that cannot be undone and have major
  consequences; otherwise prefer undo.

### Interpretation

Edit in context when the reference material matters; use separate surfaces
when the edit genuinely needs substantial controls. Prefer immediate reversible
change to repeated confirmation. Undo scope and multi-object semantics must be
explicit; no source justifies a fixed history depth.

### Oracle rules

`UI-EDIT-001` … `UI-EDIT-004`, `UI-DLG-001` … `UI-DLG-005`, `UI-EXP-003`.
Confidence: HIGH except the exact inline-edit boundary (MEDIUM).

## Question: What feedback is required for OCR/background work?

### Local evidence

- `JM3`, Ch. 14, Table 14.1, book pp. 239–240: 0.1 s is the perceptual-cycle
  scale; 0.14 s is the approximate causal-link ceiling; a unit task spans about
  6–30 s.
- `JM3`, Ch. 14, “0.1 second,” pp. 247–248: show action acknowledgment by
  about 0.1 s; completion need not occur by then. If work continues, show busy
  or progress indication by about 1 s.
- `JM3`, Ch. 14, “Use busy indicators” and “Use progress indicators,” pp.
  250–252: an indicator must reflect real work rather than animate independently;
  progress is better than busy state because it exposes remaining time; use it
  for operations longer than a few seconds.
- `JM3`, Ch. 14, pp. 236–237 and 253–254: unabortable blocking work and ignored
  input are responsiveness failures; process low-priority work in the background,
  prioritize user input and display important results first.
- `DI3`, Ch. 8, “Loading or Progress Indicators” and “Cancelability,” book pp.
  409–417: keep the rest of the UI alive, place cancel near progress, and allow
  time-consuming/background work to be cancelled without side effects.

### Interpretation

The old 10-second trigger conflated attention loss with the earlier need for
progress. The corrected sequence is: acknowledge by about 0.1 s; communicate
continued work by about 1 s; prefer determinate progress/remaining work after a
few seconds; preserve interaction and cancellation. OCR result publication must
also identify which source/region/version it belongs to so background completion
cannot overwrite newer edits—this last clause is a derived concurrency safeguard.

### Oracle rules

`UI-FB-001` … `UI-FB-006`. Confidence: HIGH. Numeric values retain Johnson's
scope and are not Windows platform requirements.

## Question: How should recognition errors be framed?

### Local evidence

- `JM3`, Ch. 15, “Voice-Recognition Failure and Misrecognition are Not User
  Errors,” book pp. 273–274: the user neither slipped nor made a mistake; the
  system made the error and must help correct/work around it.
- `DOET-R`, Ch. 5, “Human Error? No, Bad Design,” book pp. 162–216: slips and
  mistakes require different remedies; design conditions frequently create
  what gets called human error.

### Interpretation

Speech and OCR are not identical technologies, so OCR application is an explicit
analogy. Both are recognition systems proposing an interpretation of human-made
input. The system must expose correction and provenance rather than blame.

### Oracle rules

`UI-ERR-002`, `UI-ERR-003`, `UI-OCR-004`. Confidence: HIGH for the recognition
principle; MEDIUM for product-specific wording.

## Question: What should a message say, and how?

Added for 3.0.0 with the `writing` module. The evidence is the archived
corpus under `corpus/writing/`; locations are section headings of the
archived pages.

### Local evidence

- `WIN7-TEXT` Error Messages, "The characteristics of good error messages":
  a problem, a cause, a solution; relevant, actionable, user-centered, brief,
  clear, specific, courteous, rare. "Supplemental instructions": "aim for a
  maximum of three sentences of moderate length." "Text › General": the
  do-not-use list with replacements; "don't use phrasing that blames the
  user"; "be specific … specific names, locations, and values"; "avoid the
  word 'please' except …"; "use the word 'sorry' only …". "Commit buttons":
  Close, not OK. "Progressive disclosure": details only when there is more
  detail; "Error codes": always a text description as well.
- `WIN7-TEXT` User Interface Text, "A design model for UI text": the scan
  order, and "once users have decided what to do, they will immediately stop
  reading and do it." "Use the inverted pyramid." "Punctuation",
  "Capitalization", "Commit button labels" (the table).
- `WIN7-TEXT` Style and Tone: tones to avoid; "use everyday words"; "be
  consistent" with the *start/run/launch/boot/execute* example; the *please*
  and *sorry* limits.
- `WIN7-TEXT` Warning Messages, "Determine the appropriate message type": the
  same condition phrased three ways; "don't use the terms 'warning' or
  'caution' in the text". Confirmations, "Make confirmations require
  thought": *anyway*, Yes/No. Notifications, "What to notify": not success,
  with three exceptions.
- `GOVUK-DS` Error message, "Be clear and concise", "Be consistent", "Be
  specific", "Use instructions and descriptions", "Match up error messages to
  labels". Error summary, "How it works": same wording in both places.
  Details, "When (not) to use". Button, "How it works": sentence case,
  describing the action. Problem-with-service pages: the mandated *"Sorry,
  there is a problem with the service"* H1; no jargon, no red text.
- `GOVUK-WG` Use clear language: literacy data; "the more educated the
  person and the more specialist their knowledge, the greater their
  preference for plain English"; 25 words, 5 sentences; active voice with
  named exceptions. Use the right tone: the tone list; no *please*; no block
  capitals. Create a clear structure: 20–28% read; frontload; active headings.
- `MS-WRITING`: the three voice principles; "Lead with what's important";
  "Emphasize action"; "Short and sweet" with the before/after; "Periods";
  "Capitalization"; "Error messages"; "Dialogs" (call and response);
  "Buttons".
- `MS-STYLE` Top 10 tips; Capitalization; Verbs ("Active and passive voice"
  table — passive to avoid blaming, first listed); Use simple words;
  Scannable content; Describing interactions with the UI (the verb table);
  Writing step-by-step instructions ("make sure that customers know where the
  action should take place before you describe the action"); Numbers.
- `CLIG` Errors: "catch errors and rewrite them for humans"; "signal-to-noise
  ratio is crucial"; "put the most important information at the end" (C13).
  Output: "if you change state, tell the user"; "suggest commands"; "don't
  treat stderr like a log file"; debug output "only in verbose mode".

### Interpretation

Four media, one finding: a message is scanned, not read, and it is scanned
for what to do. Every specific rule — order, length, words, voice, case,
buttons — falls out of that. The sources disagree in three places, all
resolved by reading their scope (C13, C14, C15). The Win32 material is
retained for what a sentence says, not for how a Windows 7 dialog looked.

### Oracle rules

`UI-TEXT-001` … `UI-TEXT-015` (module `writing`); `UI-ERR-001` gains a
binding. Confidence: HIGH throughout except `UI-TEXT-010`'s derived clause.

## Question: What does Dear ImGui do, and what can it not do?

Added for 4.0.0 with the `imgui` module. The evidence is the toolkit's own
documentation, archived under `corpus/imgui/`; locations are section headings
or identifiers in the archived files.

### Local evidence

- `IMGUI-README`, The Pitch: for *"content creation tools and visualization /
  debug tools (as opposed to UI for the average end-user)"*; *"full
  internationalization … and accessibility features are not supported."*
- `IMGUI-CPP`, Mission statement: *"Designed primarily for developers and
  content-creators, not the typical end-user!"*; weaknesses *"Doesn't look
  fancy by default"*, *"Limited layout features"*. Read first: *"Your code
  creates the UI every frame of your application loop, if your code doesn't
  run the UI is gone!"* Controls guide: the full key map, including *"Drag on
  any empty space: Move window (unless io.ConfigWindowsMoveFromTitleBarOnly =
  true)"* and *"ESCAPE: Revert text to its original value."*
- `IMGUI-H`: `ImGuiConfigFlags_NavEnableKeyboard` is the *"Master keyboard
  navigation enable flag"*, default off; `ConfigNavCursorVisibleAuto` (*"Mouse
  click hides the cursor"*); `ConfigNavEscapeClearFocusItem` default true;
  `IniFilename` *"relative to current working dir!"*; `FontScaleMain` *"May be
  set by application once, or exposed to end-user"*; the scaling identity
  `GetFontSize() == FontSizeBase * (FontScaleMain * FontScaleDpi * …)`;
  Popups: *"BeginPopupModal(): block every interaction behind the window,
  cannot be closed by user"*; Menus: shortcuts *"displayed as a convenience
  but _not processed_"*; Tooltips: `ForTooltip` flags chosen by input type,
  mouse default *"Stationary | DelayShort"*, `AllowWhenDisabled` by default;
  `ConfigDebugHighlightIdConflicts` default true; `StyleColorsLight` *"best
  used with borders and a custom, thicker font"*; `ImGuiInputTextFlags_ReadOnly`;
  `ConfigWindowsCopyContentsWithCtrlC` experimental; error-recovery seats
  distinguished. A search of the header for "accessib" finds no API.
- `IMGUI-FAQ`: ID stack (*"THE MOST COMMON USER MISTAKE"*; *"Interacting with
  either button will trigger the first one"*; `###` keeps state across label
  changes); input dispatch via `WantCapture*`; DPI (*"you need to inform
  Windows that your application is DPI aware!"*; *"avoid using hardcoded
  constants for size and positioning"*); non-Latin text (UTF-8; IME via
  `PlatformHandleRaw`); *"A same Dear ImGui context may be not used from
  multiple threads in parallel"*; skinning *"Somewhat"*; serious tools
  *"running all day"*.
- `IMGUI-FONTS`: default *"ProggyClean.ttf … 13 pixels high … does not scale
  very nicely"*; scalable fonts, merging, icon fonts; `imgui_freetype` for
  small sizes; UTF-8 tools.
- `IMGUI-WIKI` Getting Started: *"expected to update continuously at
  interactive framerates (e.g. 60 FPS)"*, idle *"currently not well supported
  by default"*; `NavEnableKeyboard` set in every example. Docking: *"there is
  no great API for this yet"* for default layouts; the ini/`DockBuilder`
  routes.

### Interpretation

The toolkit is precise about its scope and its gaps, which makes the
applicability of the core decidable rule by rule. Three core requirements
cannot be met (accessibility tree); several are met by a mechanism the
toolkit leaves off or unconfigured by default (keyboard navigation, text
scale, DPI, settings path, modal keys); one class of failure — the blocked
frame — has no analogue in the retained-mode sources and needed its own rule.
Toolkit statements are cited at HIGH confidence as facts about the toolkit;
the design consequences cite the core.

### Oracle rules

`UI-IMGUI-001` … `UI-IMGUI-021`; contract §5 (`N/A (TOOLKIT)`) and §6
(qualifier); conflict C16. Confidence: HIGH for toolkit behaviour; MEDIUM
where the toolkit documents an option without recommending it (`UI-IMGUI-008`,
`UI-IMGUI-016`, the OS-theme half of `UI-IMGUI-013`).

## Question: What does a command-line program owe its user and the shell?

Added for 4.0.0 with the `cli` module; rewritten in the same release when four
further sources were read. Locations are section headings or guideline numbers
in each source.

### Local evidence

- `POSIX-12`, 12.2 Utility Syntax Guidelines 1–14: names *"between two and
  nine characters"* of lower-case letters and digits; *"Each option name
  should be a single alphanumeric character"*; *"All options should be
  preceded by the '-' delimiter"*; grouping behind one `-`;
  *"Option-arguments should not be optional"*; *"All options should precede
  operands"*; *"The first -- argument … should be accepted as a delimiter
  indicating the end of options"*; *"The order of different options relative
  to one another should not matter"*; `-` for standard input or output. The
  chapter states that conforming utilities follow these *"as if these
  guidelines contained the term 'shall' instead of 'should'."*
- `GNU-STD` 4.1: outside standards are *"suggestions, not orders"*, and GNU
  departs from POSIX by permitting long options and *"intermixing of options
  with ordinary arguments."* 4.2: *"Avoid arbitrary limits on the length or
  number of any data structure"*; *"long lines are silently truncated … is
  not acceptable in a GNU utility"*; NUL and multibyte input preserved;
  *"Include the system error text … in every error message resulting from a
  failing system call"*; *"Do not use a count of errors as the exit status"*;
  `TMPDIR`. 4.4: the `program: message` form, lower case, no trailing period,
  and the interactive exception. 4.5: *"don't make the behavior of a utility
  depend on the name used to invoke it"* and device independence. 4.8: long
  options for every short one, the `--verbose` example, output files by
  `-o`/`--output`, *"All programs should support two standard options:
  '--version' and '--help'."* 4.8.1: name and version on stdout, *"the
  version number proper starts after the last space"*, other arguments
  ignored, *"don't compute it from argv[0]"*. 4.8.2: help on stdout, and the
  bug address and home page *"Near the end of the '--help' option's output"*.
  4.10: the standard long-option table, including `--quiet`/`--silent` as
  required synonyms, `--force`, `--dry-run`, `--interactive`, `--recursive`.
  4.13: internal files do not live in the installation tree.
- `CLIG` Philosophy: *"if a command is going to be used primarily by humans,
  it should be designed for humans first"*; *"your only choice is over whether
  it will be a well-behaved part"*; *"The terminal's conventions are hardwired
  into our fingers"*; discoverability, citing Norman. The Basics, Help,
  Output, Errors, Arguments and flags, Interactivity, Subcommands, Robustness,
  Future-proofing, Signals, Configuration, Environment variables, Naming and
  Analytics as quoted rule by rule in the module.
- `12F-CLI` §1 every route to help and *"-h,--help should be a reserved flag
  used for help only"*; §2 *"1 type of argument is fine, 2 types are very
  suspect, and 3 are never good"* and the `--` pass-through; §3 the three
  version invocations; §4 *"stdout is for output, stderr is for messaging"*
  and passing a child's stderr up; §5 the five parts of an error and
  tracebacks behind a debug switch, error logs without ANSI; §6 the fallbacks
  when not a TTY, `TERM=dumb`, `NO_COLOR`, `--no-color`; §7 prompt if stdin is
  a TTY, *"Never require a prompt"*, typing the name to confirm a destroy; §8
  *"Never output table borders"*, `--columns`, `--no-truncate`, `--no-headers`,
  `--sort`, csv/json; §9 the start-up bands *"<100ms … 100ms–500ms: fast
  enough, aim here"*; §11 bare invocation lists subcommands or shows help;
  §12 XDG, and `%LOCALAPPDATA%` on Windows.
- `HEROKU-CLI` Mission statement (*"for humans before machines"*); Naming the
  command (lower case, no `*:list` command); Description (80 columns, lower
  case, no full stop); Flags (the `fork --from/--to` example); Prompting
  (*"Ensure that args or flags can always be provided to bypass the prompt"*);
  Output (actions on stderr); Colors (disable on `--no-color`, `COLOR=false`,
  or no TTY; red and yellow reserved); Human-readable vs machine-readable
  (grep-parseable rows, `--json`, and stdout stable after general
  availability).

### Interpretation

Five sources, four decades apart, converge. POSIX fixes the syntax, GNU fixes
the two universal options and the error form, and the three modern guides add
what a terminal does now: TTY detection, structured output, colour, progress,
interrupts, configuration and the interface promise. Where they differ, the
difference is in subject rather than substance: `C13` (where the decisive line
goes), `C17` (confirmation without undo), `C18` (what an error line starts
with), `C19` (device independence versus presentation).

Two consequences shaped the module. First, the conventions are a contract with
other programs, not a matter of taste, so the rules are MUSTs. Second, most of
them are decidable by running the program, so the module ships
`tools/cli_check.py` and the contract requires a clean run (§6). The 100 ms
figure in `UI-CLI-016` is the same order as Johnson's 0.1 s deadline in
`UI-FB-001`, reached independently by practitioners: corroboration, not a
second source for the number.

### Oracle rules

`UI-CLI-001` … `UI-CLI-024`; conflicts C17, C18, C19; the `cli` posture value;
the contract's automated-module gate. Confidence: HIGH throughout — every rule
is stated by at least one source and contradicted by none.

## Question: What should user-visible text say?

Answered at length in `UX_COPY_EVIDENCE.md`, which is the evidence layer for
`UX_WRITING_ORACLE.md` and `ERROR_MESSAGE_ORACLE.md`. It runs fifteen
questions across Google's error-message course and style guide, the Win32
control and message pages, Visual Studio, the Microsoft Writing Style Guide,
GOV.UK, NN/g and the four books. It is not duplicated here.

The `writing` module's own evidence — what a message says, in what order —
remains in the question below it.

## Question: Which current Windows claims can the books verify?

The books can corroborate interaction principles—keyboard access, visible
state, grouping, undo, modeless feedback—but cannot verify Windows type ramps,
UI Automation roles, theme behavior, contrast ratios or text-scale APIs. Those
remain `PLATFORM REQUIREMENT` claims sourced to the Tier 1 pages in
`UI_SOURCE_MATRIX.md`, archived under `corpus/platform/` since 4.0.0 so that
the quoted text is reproducible. The live pages must still be rechecked if
exact current behavior is material to implementation.

No local source supports numeric spacing, target size, corner radius, animation
duration or non-text contrast requirements. The oracle intentionally has none.

## Rule verification ledger

Statuses mean:

- `VERIFIED`: source says the operative proposition directly.
- `VERIFIED WITH QUALIFICATION`: supported, but only for stated posture,
  platform, era or condition.
- `DERIVED`: synthesis/transfer is shown; no source states the exact rule.
- `PROJECT-SPECIFIC`: belongs in a project profile, not the core.
- `WEAKLY SUPPORTED`, `OUTDATED`, `CONTRADICTED`: require revision/removal
  before release.

The 2.0.0 audit leaves no active rule in the last three categories. This is not
a claim that every rule is direct: derived rules remain visibly derived.

### Module `writing` (3.0.0)

| Rule | Verification | Evidence note |
|---|---|---|
| UI-TEXT-001 | VERIFIED | `WIN7-TEXT` problem/cause/solution and the three-sentence ceiling; `GOVUK-DS`, `MS-WRITING`, `MS-STYLE`, `CLIG` all state brevity and order |
| UI-TEXT-002 | VERIFIED | `WIN7-TEXT` "be specific" with the counter-examples; `GOVUK-DS` "be specific" with its own; `MS-STYLE` before/after |
| UI-TEXT-003 | VERIFIED | The word list is `WIN7-TEXT`'s and `GOVUK-DS`'s verbatim; the passive-to-avoid-blame clause is `MS-STYLE` Verbs and `WIN7-TEXT` |
| UI-TEXT-004 | VERIFIED WITH QUALIFICATION | Reconciles `GOVUK-DS` (never) with `WIN7-TEXT` (when it costs the operator) via GOV.UK's own practice; see C14 |
| UI-TEXT-005 | VERIFIED | `WIN7-TEXT` three-phrasings example and "icons should always match"; `GOVUK-DS` scope of error messages |
| UI-TEXT-006 | VERIFIED | `GOVUK-WG` specialist finding; `MS-STYLE` word table; `WIN7-TEXT` real-world language |
| UI-TEXT-007 | VERIFIED WITH QUALIFICATION | Active/present/imperative from four sources; qualified by the C15 precedence |
| UI-TEXT-008 | VERIFIED | `WIN7-TEXT` progressive disclosure and error codes; `GOVUK-DS` Details; `CLIG` debug output |
| UI-TEXT-009 | VERIFIED WITH QUALIFICATION | `MS-STYLE` and `MS-WRITING` current; `WIN7-TEXT`'s title-case-for-titles exception superseded by `MS-STYLE` and noted |
| UI-TEXT-010 | VERIFIED WITH QUALIFICATION | Numerals, units, leading zero from `MS-STYLE` Numbers; the notation clause is DERIVED and marked MEDIUM |
| UI-TEXT-011 | VERIFIED | `WIN7-TEXT` names log files as a presentation for IT professionals; `CLIG` stderr/verbose |
| UI-TEXT-012 | VERIFIED | `MS-WRITING` call and response; `WIN7-TEXT` commit-button table and Close-not-OK; `GOVUK-DS` Button |
| UI-TEXT-013 | VERIFIED | `GOVUK-DS` error summary and message must match; `WIN7-TEXT` and `MS-STYLE` one term per concept |
| UI-TEXT-014 | VERIFIED | `MS-STYLE` verb table; place-before-action from `MS-STYLE` and `WIN7-TEXT` |
| UI-TEXT-015 | VERIFIED | `CLIG` say what changed; `WIN7-TEXT` Notifications on not announcing success |

### Module `imgui` (4.0.0)

| Rule | Verification | Evidence note |
|---|---|---|
| UI-IMGUI-001 | VERIFIED | `IMGUI-README` states the accessibility gap; the header confirms the absence |
| UI-IMGUI-002 | VERIFIED | `IMGUI-H` flag comment; `IMGUI-CPP` controls guide; every Getting Started example |
| UI-IMGUI-003 | VERIFIED WITH QUALIFICATION | Cursor visibility rules are the header's; the distinctness requirement is the core's `UI-SEL-001` |
| UI-IMGUI-004 | DERIVED | Submission-order tab traversal follows from the FAQ's no-retained-tree statement |
| UI-IMGUI-005 | VERIFIED | `IMGUI-FAQ` ID stack section and `IMGUI-H` remedy list, near-verbatim |
| UI-IMGUI-006 | VERIFIED | `IMGUI-H` popup comments: modals cannot be closed by the user; Escape closes only non-modals |
| UI-IMGUI-007 | DERIVED | Frame-loop and threading statements are the toolkit's; the consequence for `UI-FB-005` is reasoned |
| UI-IMGUI-008 | DERIVED | Game-loop assumption and idle caveat from the wiki; cost unquantified by any source |
| UI-IMGUI-009 | VERIFIED | FAQ DPI section and header scaling identity, quoted |
| UI-IMGUI-010 | VERIFIED WITH QUALIFICATION | Default-font limits from `IMGUI-FONTS`; the floor is `MS-TYPE`'s |
| UI-IMGUI-011 | VERIFIED WITH QUALIFICATION | Mechanism from `IMGUI-H`; the 2.25 range is `MS-A11Y-TEXT`'s, transferred |
| UI-IMGUI-012 | VERIFIED | Tooltip flag defaults from `IMGUI-H`; tightening of `UI-ICON-002` is a module prerogative |
| UI-IMGUI-013 | VERIFIED WITH QUALIFICATION | Built-in style comments quoted; OS-theme following is derived (no mechanism documented) |
| UI-IMGUI-014 | VERIFIED WITH QUALIFICATION | `ImGuiCol_` enumeration has no semantic roles; the requirement is `UI-COLOR-005` |
| UI-IMGUI-015 | VERIFIED WITH QUALIFICATION | Ini-path warning and DockBuilder statement quoted; the default-layout SHOULD is derived |
| UI-IMGUI-016 | DERIVED | Default move behaviour quoted; the slip argument is Johnson's |
| UI-IMGUI-017 | VERIFIED | `IMGUI-H` menus comment, quoted |
| UI-IMGUI-018 | DERIVED | Read-only input and experimental copy documented; the requirement is `UI-A11Y-004`'s residue |
| UI-IMGUI-019 | VERIFIED | `IMGUI-FAQ` dispatch section, quoted |
| UI-IMGUI-020 | VERIFIED | `IMGUI-FAQ` non-Latin section and `IMGUI-FONTS`, quoted |
| UI-IMGUI-021 | VERIFIED | `IMGUI-H` error-recovery seat guidance, quoted |

### Module `cli` (4.0.0)

Checks named in the table are the ones `tools/cli_check.py` performs.

| Rule | Verification | Evidence note |
|---|---|---|
| UI-CLI-001 | VERIFIED | `CLIG` The Basics (map codes to failure modes); `GNU-STD` 4.2 (exit status is not a count), 4.8.1–4.8.2 (help and version exit successfully) |
| UI-CLI-002 | VERIFIED | `CLIG` The Basics; `12F-CLI` §4; `HEROKU-CLI` Stdout/Stderr; `GNU-STD` puts help and version on stdout |
| UI-CLI-003 | VERIFIED | `12F-CLI` §1 (six routes, `-h` reserved, examples) and §11 (bare invocation); `CLIG` Help; `GNU-STD` 4.8.2 (bug address, home page); `HEROKU-CLI` Description (80 columns, lower case, no period) |
| UI-CLI-004 | VERIFIED | `GNU-STD` 4.8.1, quoted in full; `12F-CLI` §3 for `-V` and the `version` subcommand |
| UI-CLI-005 | VERIFIED | `POSIX-12` Guidelines 3–14, quoted; `GNU-STD` 4.8 and the 4.10 table; `CLIG` Arguments and flags; `12F-CLI` §2 for `--` |
| UI-CLI-006 | VERIFIED | `12F-CLI` §2 (the one/two/three rule, verbatim); `HEROKU-CLI` Flags (the worked example); `CLIG`; `GNU-STD` 4.8 on output files |
| UI-CLI-007 | VERIFIED | `CLIG` Help (suggest, never run, with both reasons); `12F-CLI` §1 on `subcommand help`; core `UI-ERR-002`, `UI-ERR-003` |
| UI-CLI-008 | VERIFIED WITH QUALIFICATION | `12F-CLI` §8 and `HEROKU-CLI` (rows, no borders, `--json`); `CLIG` Output; the device-independence clause is `GNU-STD` 4.5 as resolved in C19 |
| UI-CLI-009 | VERIFIED | The disable list is `CLIG` Output and `12F-CLI` §6 verbatim; `HEROKU-CLI` Colors adds `COLOR=false`; redundancy is core `UI-COLOR-003` |
| UI-CLI-010 | VERIFIED | `CLIG` Output, four statements; wording delegated to `UI-TEXT-015` |
| UI-CLI-011 | VERIFIED WITH QUALIFICATION | Form from `GNU-STD` 4.4 and the system-error clause from 4.2; content from `12F-CLI` §5; the last-line rule from `CLIG` Errors, scoped by C13; the label prohibition from `CLIG` Output, reconciled with the `Error:` title in C18 |
| UI-CLI-012 | VERIFIED | `CLIG` Output, including the `less -FIRX` reasoning |
| UI-CLI-013 | VERIFIED | `CLIG` Interactivity; `12F-CLI` §7; `HEROKU-CLI` Prompting — three sources, same rule |
| UI-CLI-014 | VERIFIED | `CLIG` Arguments and flags, and Environment variables, both quoted |
| UI-CLI-015 | VERIFIED WITH QUALIFICATION | The three grades are `CLIG` verbatim; `12F-CLI` §7 corroborates the typed name; `-f` and `-n` from `GNU-STD` 4.10; reconciled with `UI-DLG-003` in C17 |
| UI-CLI-016 | VERIFIED | Start-up bands from `12F-CLI` §9; the 100 ms first-output rule and the stalled-bar argument from `CLIG` Robustness |
| UI-CLI-017 | VERIFIED | `CLIG` Signals and control characters, Interactivity, Robustness |
| UI-CLI-018 | VERIFIED | `CLIG` Subcommands and Future-proofing; `HEROKU-CLI` on topic roots and `*:list` |
| UI-CLI-019 | VERIFIED WITH QUALIFICATION | Precedence and XDG from `CLIG` Configuration; `%LOCALAPPDATA%` from `12F-CLI` §12; `TMPDIR` and the installation-tree rule from `GNU-STD` 4.2 and 4.13. No source covers the Windows configuration location beyond cache |
| UI-CLI-020 | VERIFIED | `CLIG` Future-proofing; `HEROKU-CLI` on stdout after general availability |
| UI-CLI-021 | VERIFIED | `CLIG` Analytics |
| UI-CLI-022 | VERIFIED | `POSIX-12` Guidelines 1–2 (two to nine, lower case); `CLIG` Naming; `GNU-STD` 4.5 on invocation name |
| UI-CLI-023 | VERIFIED | `GNU-STD` 4.2, quoted (limits, truncation, NUL, multibyte, system calls); `CLIG` Robustness on validation |
| UI-CLI-024 | DERIVED | The TTY heuristic is the sources' shared premise and `GNU-STD` 4.5 is why both cases are reviewed; the profile and gate requirements are the contract's |

### Core rules

| Rule | Verification | Evidence note |
|---|---|---|
| UI-GLOBAL-001 | VERIFIED | `AF4` Ch. 9 defines posture as behaviorally consequential |
| UI-GLOBAL-002 | DERIVED | Resolves calm styling against sovereign information needs |
| UI-GLOBAL-003 | DERIVED | Consistency + recognition/learning synthesis |
| UI-GLOBAL-004 | VERIFIED | `AF4` Ch. 12 directly defines and rejects excise |
| UI-GLOBAL-005 | VERIFIED | `DOET-R` Ch. 2 discoverability principle |
| UI-GLOBAL-006 | VERIFIED | `DOET-R` Ch. 1 signifier distinction |
| UI-GLOBAL-007 | VERIFIED | `DOET-R` Ch. 2 conceptual model principle |
| UI-GLOBAL-008 | VERIFIED | `DOET-R` Ch. 2 mapping principle |
| UI-GLOBAL-009 | VERIFIED | `DOET-R` Ch. 4 constraints/forcing functions |
| UI-ARCH-001 | VERIFIED WITH QUALIFICATION | `AF4` sovereign workspace; concrete satellites remain profile decisions |
| UI-ARCH-002 | DERIVED | Persistence reduces excise and protects spatial memory |
| UI-ARCH-003 | DERIVED | Working memory + coordinated views transferred to source/derived content |
| UI-ARCH-004 | DERIVED | Reconciles `AF4` window cost with `DI3` Many Workspaces |
| UI-NAV-001 | DERIVED | Scoped rejection of unnecessary global navigation, not a universal law |
| UI-NAV-002 | VERIFIED WITH QUALIFICATION | `DI3` Ch. 1 directly warns against automatic rearrangement; persistence is derived |
| UI-LAY-001 | VERIFIED WITH QUALIFICATION | `AF4` posture density, bounded by platform/accessibility floors |
| UI-LAY-002 | VERIFIED | `JM3` Ch. 2 and `DI3` Ch. 4 proximity/common region |
| UI-LAY-003 | VERIFIED | `JM3` Ch. 3 and `DI3` Ch. 4 visual hierarchy |
| UI-LAY-004 | DERIVED | Resize policy is a completeness test, not a quoted source rule |
| UI-LAY-005 | DERIVED | Fitts/learned-action/slip consequences of moving targets |
| UI-CMD-001 | VERIFIED | `MS-COMMAND` and `DI3` Ch. 2 frequency rule |
| UI-CMD-002 | DERIVED | Direct manipulation + keyboard/accessibility synthesis |
| UI-CMD-003 | DERIVED | Frequency, excise and menu-traversal synthesis |
| UI-CMD-004 | VERIFIED WITH QUALIFICATION | `DI3` says context menus are not sought by all; exceptions preserve other routes |
| UI-CMD-005 | VERIFIED WITH QUALIFICATION | Confirm/undo directly supported; physical separation is slip prevention |
| UI-CMD-006 | DERIVED | Discoverability applied to disabled preconditions; obvious cases excepted |
| UI-SEL-001 | DERIVED | Sources distinguish states; exact visual differentiation is synthesized |
| UI-SEL-002 | DERIVED | Excise and memory consequences of gratuitous selection loss |
| UI-SEL-003 | VERIFIED WITH QUALIFICATION | `DI3` Data Brushing directly supports coordinated selected data |
| UI-SEL-004 | VERIFIED WITH QUALIFICATION | `DI3` supports platform-standard Shift selection; exact Windows modifiers need current control docs |
| UI-EDIT-001 | VERIFIED | `MS-COMMAND`, `JM3` Ch. 15 and `AF4` Ch. 15 |
| UI-EDIT-002 | VERIFIED WITH QUALIFICATION | In-place editing supported; substantial/multi-object edits excepted |
| UI-EDIT-003 | VERIFIED WITH QUALIFICATION | Legacy dialog behavior retained, visuals discarded |
| UI-EDIT-004 | VERIFIED WITH QUALIFICATION | Legacy in-place errors + `AF4` modeless feedback |
| UI-KBD-001 | VERIFIED | `DI3` Ch. 1 Keyboard Only; accessibility corroborates |
| UI-KBD-002 | VERIFIED WITH QUALIFICATION | `DI3` tab traversal; exact order follows visible/logical order by synthesis |
| UI-KBD-003 | VERIFIED | `MS-A11Y-TEXT` direct requirement |
| UI-KBD-004 | VERIFIED WITH QUALIFICATION | Legacy dialog convention generalized to transient/edit modes |
| UI-KBD-005 | VERIFIED | `DI3` and `AF4` directly support shortcuts shown at command locations |
| UI-MOUSE-001 | DERIVED | Fitts' law applied to the repeated loop |
| UI-MOUSE-002 | VERIFIED | `JM3` Ch. 13 Steering Law |
| UI-MOUSE-003 | VERIFIED WITH QUALIFICATION | `DI3` documents hover's pointer dependence; keyboard route is accessibility requirement |
| UI-FB-001 | VERIFIED | `JM3` Ch. 14 0.1-second acknowledgment deadline |
| UI-FB-002 | VERIFIED | `JM3` Ch. 14 busy/idle status guidance |
| UI-FB-003 | VERIFIED | Corrected to `JM3` progress-after-a-few-seconds guidance |
| UI-FB-004 | VERIFIED | `JM3` Ch. 14 and `DI3` Cancelability |
| UI-FB-005 | VERIFIED | `JM3` background/priority guidance; `DI3` keep UI alive |
| UI-FB-006 | VERIFIED | `AF4` rich modeless feedback; current Microsoft corroboration |
| UI-DLG-001 | VERIFIED WITH QUALIFICATION | Current Microsoft and `AF4`; dialogs remain valid out of flow |
| UI-DLG-002 | VERIFIED WITH QUALIFICATION | `WIN7-DIALOGS` interaction retained; appearance obsolete |
| UI-DLG-003 | VERIFIED | `MS-COMMAND` confirm-vs-undo rule |
| UI-DLG-004 | VERIFIED WITH QUALIFICATION | Legacy keyboard convention; current component specifics unverified |
| UI-DLG-005 | VERIFIED | `JM3` Ch. 15 destructive-default/capture-slip evidence |
| UI-ERR-001 | DERIVED | Clear/actionable writing synthesized; stricter wording is project-bound |
| UI-ERR-002 | VERIFIED | `DOET-R` Ch. 5 and `JM3` Ch. 15 |
| UI-ERR-003 | VERIFIED WITH QUALIFICATION | Direct for voice recognition (`JM3`) and for design-caused error in general (`DOET-R`); generalised to any machine inference in 4.0.0 |
| UI-TYPO-001 | VERIFIED | `MS-TYPE` current platform source |
| UI-TYPO-002 | VERIFIED | `MS-TYPE` stated minimums |
| UI-TYPO-003 | VERIFIED | `MS-TYPE` stated ramp exclusions |
| UI-TYPO-004 | VERIFIED | `MS-TYPE` stated alignment/case guidance |
| UI-TYPO-005 | VERIFIED WITH QUALIFICATION | `MS-TYPE`; scoped to running prose |
| UI-TYPO-006 | VERIFIED WITH QUALIFICATION | Source self-conflict resolved conditionally; see C2 |
| UI-TYPO-007 | VERIFIED | `MS-TYPE` font-family/script guidance |
| UI-ICON-001 | VERIFIED WITH QUALIFICATION | `AF4` posture argument; ambiguous glyphs still fail |
| UI-ICON-002 | DERIVED | Accessible equivalent + recognition synthesis |
| UI-ICON-003 | VERIFIED WITH QUALIFICATION | `MS-TYPE`; current icon availability still must be checked |
| UI-COLOR-001 | VERIFIED | `MS-A11Y-TEXT`; text only |
| UI-COLOR-002 | VERIFIED | `MS-COLOR` theme guidance |
| UI-COLOR-003 | VERIFIED | `MS-COLOR` plus `JM3` Ch. 4 |
| UI-COLOR-004 | VERIFIED | `MS-COLOR` and `AF4` restraint |
| UI-COLOR-005 | PROJECT-SPECIFIC | Role names/values live in the profile; core only requires consistency |
| UI-A11Y-001 | DERIVED | Keyboard pattern + platform accessibility baseline; breadth exceeds text page |
| UI-A11Y-002 | VERIFIED | `MS-A11Y-TEXT` roles |
| UI-A11Y-003 | VERIFIED | `MS-A11Y-TEXT` `[1,2.25]` range |
| UI-A11Y-004 | VERIFIED | `MS-A11Y-TEXT` equivalent-content requirement |
| UI-MODE-001 | VERIFIED | `JM3` Chs. 7/15 clear continuous/strong feedback |
| UI-MODE-002 | DERIVED | Deliberate entry/exit synthesized from mode-error prevention |
| UI-MODE-003 | VERIFIED WITH QUALIFICATION | `JM3` explicitly recommends spring-loaded modes; object scope is derived |
| UI-EXP-001 | VERIFIED | `AF4` Ch. 9 target intermediate users |
| UI-EXP-002 | VERIFIED WITH QUALIFICATION | `DI3` Streamlined Repetition; exact mechanism is contextual |
| UI-EXP-003 | VERIFIED | `JM3`, `DI3` and `AF4` reversibility/undo |

### OCR module

| Rule | Verification | Evidence note |
|---|---|---|
| UI-OCR-001 | DERIVED | `DI3` Data Brushing transferred to OCR representations |
| UI-OCR-002 | DERIVED | Coordinated views + working memory + in-context editing |
| UI-OCR-003 | DERIVED | Visual search/Data Spotlight + redundant color; no confidence-calibration source |
| UI-OCR-004 | DERIVED | `JM3` voice-recognition statement transferred explicitly to OCR |
| UI-OCR-005 | DERIVED | Orientation/context evidence transferred to token lookup |
| UI-OCR-006 | PROJECT-SPECIFIC | Retired/tombstoned; learning state belongs in the adopting profile |

## Release gate

If later evidence makes an active rule `WEAKLY SUPPORTED`, `OUTDATED` or
`CONTRADICTED`, the rule must be revised, downgraded/retired with the contract's
required version bump, or removed via tombstone before the oracle is released.
Merely recording the adverse status is not sufficient.
