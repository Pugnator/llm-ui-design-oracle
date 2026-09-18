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

## Question: Which current Windows claims can the books verify?

The books can corroborate interaction principles—keyboard access, visible
state, grouping, undo, modeless feedback—but cannot verify Windows type ramps,
UI Automation roles, theme behavior, contrast ratios or text-scale APIs. Those
remain `PLATFORM REQUIREMENT` claims sourced only to the non-local Tier 1 pages
in `UI_SOURCE_MATRIX.md`. They must be rechecked if exact current behavior is
material to implementation.

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
| UI-ERR-003 | VERIFIED WITH QUALIFICATION | Direct for voice recognition; explicit analogy to OCR |
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
| UI-A11Y-003 | VERIFIED | `MS-A11Y-TEXT` `[1, 2.25]` range |
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
