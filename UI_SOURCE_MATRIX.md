# UI Source Matrix

Inventory of the evidence used by the oracle. Revised 2026-09-18 after a
recursive inspection of the repository and a full-text concept search of every
local book; extended 2026-09-19 (4.0.0) when the platform pages were archived
and the toolkit and command-line sources were added. The local corpus is the
primary evidence base. Platform pages are archived snapshots: reproducible,
but the live page wins where they differ.

`Verified` means the cited file or page was read, not merely named. `Complete`
describes the supplied copy, not the work in the abstract.

## Local corpus — primary evidence

| ID | Source and verified metadata | Target / date | Local path and completeness | Tier | Strongest areas | Weak or obsolete areas |
|---|---|---|---|---|---|---|
| `AF4` | Alan Cooper, Robert Reimann, David Cronin, Christopher Noessel, *About Face: The Essentials of Interaction Design*, 4th ed., Wiley. Title and copyright pages verify edition, authors, publisher, copyright 2014, ISBN 978-1-118-76657-6. | Cross-platform digital products; desktop, web and mobile examples; 2014 | `docs/cooper_a_reiman_r_cronin_d_noessel_s_about_face_the_essentia.pdf`; complete supplied PDF, 722 PDF pages; searchable text and TOC present | 2 | Sovereign/transient posture (Ch. 9, book pp. 207–218; PDF pp. 237–248); excise (Ch. 12); modeless feedback and undo (Ch. 15); desktop windows, menus, toolbars, sidebars, selection, direct manipulation and modal tools (Ch. 18); dialogs and error prevention (Ch. 21) | Predates Windows 11; examples and visuals are not platform authority. Some recommendations are argued design positions rather than measurements |
| `DI3` | Jenifer Tidwell, Charles Brewer, Aynne Valencia, *Designing Interfaces*, 3rd ed., O'Reilly. Title/copyright pages verify authors, edition, copyright 2020, January 2020 publication, ISBN 978-1-492-05196-1. | The preface explicitly focuses the edition on screen-based interaction for web and mobile, while retaining desktop patterns | `docs/tidwell_jennifer_brewer_charles_valenciabrooks_aynne_designi.pdf`; complete supplied PDF, 602 PDF pages; searchable text, TOC and index present | 2 | Keyboard Only and Streamlined Repetition (Ch. 1, book pp. 23–25); workflow-dominant apps and Canvas Plus Palette (Ch. 2); layout, density, proximity and panels (Ch. 4, esp. pp. 209–249); lists and multi-selection (Ch. 7, p. 335); actions, keyboard, progress, cancel and undo (Ch. 8, pp. 375–432); linked views/Data Brushing (Ch. 9, pp. 458–460) | Web/mobile bias must be filtered. Patterns are conditional examples, not Windows requirements. Visual examples age faster than the interaction principles |
| `JM3` | Jeff Johnson, *Designing with the Mind in Mind: Simple Guide to Understanding User Interface Design Guidelines*, 3rd ed., Morgan Kaufmann/Elsevier. EPUB title and copyright files verify edition, author, copyright 2021 and ISBN 978-0-12-818202-4. | Cross-platform UI/HCI; 2021 | `docs/Johnson J_Design with the Mind in Mind_3 2021 289.epub`; complete supplied EPUB: front matter, 15 chapters, bibliography and index are in the spine | 2 | Gestalt and grouping (Ch. 2); hierarchy and scanning (Chs. 3, 6); colour/peripheral vision (Chs. 4–5); memory and modes (Ch. 7, pp. 114–115); recognition/recall and learned actions (Chs. 9–11); Fitts/Steering (Ch. 13); response deadlines, progress and background work (Ch. 14, pp. 235–254); error types, spring-loaded modes, undo and recognition failures (Ch. 15, pp. 259–274) | Explains cognitive basis, not Windows components or visual style. Quantitative timing guidance has context and must not be generalized to unrelated animation/style timing |
| `DOET-R` | Don Norman, *The Design of Everyday Things*, revised and expanded ed., Basic Books. Front matter verifies edition, copyright 2013, ISBN 978-0-465-05065-9. | General product design; non-platform-specific; 2013 | `docs/norman_d_the_design_of_everyday_things.pdf`; complete supplied PDF, 369 PDF pages; searchable text, TOC and index present | 4 | Affordances/signifiers (Ch. 1, book pp. 10–19); action cycle, conceptual models, mapping and feedback (Ch. 2, pp. 37–73); constraints/forcing functions (Ch. 4, pp. 123–161); slips, mistakes and design-caused error (Ch. 5, pp. 162–216) | Deliberately not software- or Windows-specific. Supplies concepts, not control, density, typography or accessibility specifications |

No other documentation, HTML archive, Markdown corpus, source repository or UI
sample exists under `docs/` in this checkout. The inventory found exactly three
PDFs and one EPUB. Earlier matrix text referring to `docs/books/` and unrelated
game/Japanese texts was inaccurate for this repository and has been removed.

## Current Windows sources — archived 2026-09-19, `corpus/platform/`

These pages are Tier 1 because the oracle needs current platform and
accessibility requirements that the books cannot provide. Until 4.0.0 they
were cited by URL only; each is now archived as text with its URL, fetch date,
licence (CC BY 4.0) and the page's own `ms.date` in the file header, and the
quotations the core takes from them were checked against the archived text.
Two dates are recorded because they differ: `ms.date` is the page's metadata;
"Last updated" is what Microsoft Learn displayed when the page was rechecked.

| ID | Source | Local path | `ms.date` / displayed "Last updated" | Tier | Strong on | Limit |
|---|---|---|---|---|---|---|
| `MS-PRINCIPLES` | [Windows design principles](https://learn.microsoft.com/en-us/windows/apps/design/design-principles) | `corpus/platform/ms-design-principles.md` | 2025-12-11 / 2025-12-18 | 1 | Current Windows values | Values, not testable control rules; consumer/shell emphasis |
| `MS-INDEX` | [Design guidelines overview](https://learn.microsoft.com/en-us/windows/apps/design/guidelines-overview) | `corpus/platform/ms-guidelines-overview.md` | 2026-09-05 / 2026-09-05 | 1 | Current topic map and explicit classification of Win32 UX pages as historical | Index only |
| `MS-COLOR` | [Color in Windows](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/color) | `corpus/platform/ms-color.md` | 2024-09-19 / 2026-07-14 | 1 | Accent, themes, colour redundancy | No semantic palette and no non-text contrast ratio |
| `MS-TYPE` | [Typography in Windows](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/typography) | `corpus/platform/ms-typography.md` | 2021-06-24 / 2026-04-14 | 1 | Type ramp, minimums, measure and script fonts | Internally contradictory on truncation; see C2 |
| `MS-A11Y-TEXT` | [Accessible text requirements](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/accessible-text-requirements) | `corpus/platform/ms-accessible-text-requirements.md` | 2026-08-21 / 2026-08-26 | 1 | 4.5:1 visible-text contrast, text scale `[1,2.25]`, UIA text roles, static-text tab stops | Text-specific; does not establish non-text contrast or all keyboard behavior |
| `MS-COMMAND` | [Commanding basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/commanding-basics) | `corpus/platform/ms-commanding-basics.md` | 2020-09-24 / 2022-08-01 | 1 | Command placement, direct manipulation, confirm vs undo | Older page with consumer-flavoured examples; little expert-keyboard detail |
| `WIN7-DIALOGS` | [Win32 UX Guide — Dialog Boxes](https://learn.microsoft.com/en-us/windows/win32/uxguide/win-dialog-box) | `corpus/platform/win32-dialog-boxes.md` | 2022-01-25 / 2022-02-08 | 3 | Modeless commit/Close semantics, in-place input errors, non-destructive defaults | `STILL_VALID_INTERACTION_PRINCIPLE` for behaviour; `VISUALLY_OBSOLETE` for appearance; self-identifies as Windows 7 guidance |
| `FLUENT2-WIN` | [Fluent 2 Windows overview](https://fluent2.microsoft.design/components/windows) | not archived | rechecked 2026-09-18 | — | Directs Windows designers to WinUI components and resources | Overview only; no component guidance from which to derive a rule (C4) |

## Writing sources — local snapshots, module `writing`

Added for 3.0.0. Unlike the platform pages above, these **are** archived:
each page was fetched on 2026-09-19, converted to text and stored under
`corpus/writing/` with its URL, fetch date and licence in the file header.
`Verified` here means the archived text was read in full.

| ID | Source | Recorded version/date and verification | Tier | Strong on | Limit |
|---|---|---|---|---|---|
| `GOVUK-DS` | [GOV.UK Design System](https://design-system.service.gov.uk/) — components *error message*, *error summary*, *notification banner*, *warning text*, *details*, *button*; patterns *validation*, *there is a problem with the service*, *service unavailable*, *confirmation pages*. Open Government Licence v3.0 | Live site, no version shown; fetched 2026-09-19; all ten pages read | 2 | The most specific rules on error wording anywhere in the corpus, and the only ones with reported user research behind them | A web service for the public; form-validation framing; nothing on desktop dialogs or status bars |
| `GOVUK-WG` | [GOV.UK writing guidelines](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/) — *clear language*, *right tone*, *clear structure*, *clear titles*, *summaries*, *meet user needs*. Open Government Licence v3.0. (The former `gov.uk/guidance/content-design/writing-for-gov-uk` redirects here) | Fetched 2026-09-19; six pages read | 2 | Plain-English mandate with literacy data; specialists prefer plain English; frontloading; sentence and paragraph ceilings | Web publishing, not application UI; the A–Z style guide it points to was not read |
| `MS-WRITING` | [Writing style — Windows apps](https://learn.microsoft.com/en-us/windows/apps/design/style/writing-style). CC BY 4.0 | `ms.date` 2020-09-24, page shows "last updated 2021-06-24"; fetched 2026-09-19 | 1 | Voice principles; lead with what matters; active voice; dialog "call and response"; button text | Short; examples are consumer-app flavoured |
| `WIN7-TEXT` | Win32 UX Guide — [Error Messages](https://learn.microsoft.com/en-us/windows/win32/uxguide/mess-error), [Warning Messages](https://learn.microsoft.com/en-us/windows/win32/uxguide/mess-warn), [Confirmations](https://learn.microsoft.com/en-us/windows/win32/uxguide/mess-confirm), [Notifications](https://learn.microsoft.com/en-us/windows/win32/uxguide/mess-notif), [User Interface Text](https://learn.microsoft.com/en-us/windows/win32/uxguide/text-ui), [Style and Tone](https://learn.microsoft.com/en-us/windows/win32/uxguide/text-style-tone). CC BY 4.0 | Each page self-identifies as Windows 7 guidance; `ms.date` 2020-10-20 / 2022-01-11; fetched 2026-09-19; all six read | 3 | The anatomy of a message; the scan order; the word list; commit-button semantics; progressive disclosure | `STILL_VALID_INTERACTION_PRINCIPLE` for what a sentence should say; `VISUALLY_OBSOLETE` for task-dialog layout, fonts, colours and icons, none of which the module uses |
| `MS-STYLE` | [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/) — *top 10 tips*, *brand voice*, *use simple words*, *capitalization*, *verbs*, *scannable content*, *describing interactions with the UI*, *numbers*, *writing step-by-step instructions*, *bias-free communication*. CC BY 4.0 | `ms.date` 2018-01-19 to 2026-07-02 per page; fetched 2026-09-19; ten pages read | 1 | Sentence case; passive to avoid blame; input-neutral verbs; numerals in UI; parallel structure | Documentation-first; the A–Z word list was not read |
| `CLIG` | [Command Line Interface Guidelines](https://clig.dev/), Prasad, Firshman, Tashian, Parish. CC BY-SA 4.0 | Live page, no version; fetched 2026-09-19; read in full | 2 | Rewrite errors for humans; signal-to-noise; say what changed; suggest the next step; debug output only when asked | Written for the terminal and says so; "most important information at the end" does not transfer (`C13`) |

## Toolkit documentation — local snapshots, module `imgui`

Added for 4.0.0. Toolkit documentation is a distinct source class, **Tier 1
(toolkit)**: authoritative on what the library does, and on nothing else. A
`UI-IMGUI-` rule that states toolkit behaviour cites these files at HIGH
confidence; the design reasoning that follows is the core's and cites the
core. All files are archived under `corpus/imgui/` with URL, fetch date,
licence (MIT, `corpus/imgui/LICENSE.txt`) and library version in the header.
Version read: 1.93.0 WIP, master, 2026-09-19.

| ID | Source | Local path | Verification | Strong on | Limit |
|---|---|---|---|---|---|
| `IMGUI-README` | Dear ImGui `docs/README.md` | `corpus/imgui/imgui-readme.md` | Read in full | The library's stated purpose and stated gaps: *"accessibility features are not supported"* | Marketing and orientation; no API detail |
| `IMGUI-FAQ` | Dear ImGui `docs/FAQ.md` | `corpus/imgui/imgui-faq.md` | Read in full | ID stack, keyboard navigation, DPI, fonts, non-Latin text and IME, multi-threading, input dispatch, skinning limits | Assumes C++ and a game-loop host |
| `IMGUI-FONTS` | Dear ImGui `docs/FONTS.md` | `corpus/imgui/imgui-fonts.md` | Read in full | Default font and its limits, scalable font loading, icon-font merging, DPI, UTF-8, FreeType | Does not discuss variable-font axes or text shaping |
| `IMGUI-CPP` | `imgui.cpp` documentation block (lines 1–1243) | `corpus/imgui/imgui-cpp-guide.md` | Read in full (mission statement, controls guide, programmer guide); API-breaking-changes log skimmed | What every key does; the frame loop; *"if your code doesn't run the UI is gone!"* | The changelog is history, not guidance |
| `IMGUI-H` | `imgui.h` (complete public header) | `corpus/imgui/imgui-h.md` | Configuration, style, popup, tooltip, menu, shortcut and debug sections read; remainder searched | Every configuration flag with its default and comment; `ImGuiCol_` roles; modal semantics; *"MenuItem() keyboard shortcuts are displayed … but _not processed_"*; ID-conflict detection; no accessibility API (searched) | A header, not a guide; comments are terse |
| `IMGUI-WIKI` | Wiki: Getting Started, Docking, Multi-Viewports | `corpus/imgui/imgui-wiki-*.md` | Read in full | The game-loop assumption and its idle caveat; docking enablement, dockspaces, default layouts; multi-viewport limits | Wiki pages carry no stated licence of their own; treated as project documentation under the repository's MIT terms |

## Command-line sources — module `cli`

Five bodies of guidance, each read in full on 2026-09-19. Two are archived
under `corpus/cli/`; `CLIG` is archived under `corpus/writing/` because the
`writing` module used it first; two cannot be archived for licence reasons and
are recorded with the SHA-256 of the page that was read, so a later reader can
confirm the text has not changed (`corpus/cli/README.md` holds the hashes).

| ID | Source | Local path | Verification | Tier | Strong on | Limit |
|---|---|---|---|---|---|---|
| `POSIX-12` | The Open Group Base Specifications Issue 7, 2018 edition, IEEE Std 1003.1-2017, Ch. 12 *Utility Conventions* | not archived (copyright IEEE/The Open Group); hash recorded | Read in full | 1 (standard) | The fourteen Utility Syntax Guidelines: option form, grouping, `--`, `-`, order independence, utility names | Says nothing about output, errors, colour, prompts or configuration; predates every one of those questions |
| `GNU-STD` | GNU Coding Standards, ch. 4 *Program Behavior for All Programs* (4.1, 4.2, 4.4, 4.5, 4.8 with 4.8.1–4.8.2, 4.10, 4.12, 4.13) | `corpus/cli/gnu-*.md` | Read in full | 2 | `--help`/`--version` semantics; the error-message format; long options and the standard-name table; no arbitrary limits; exit status is not a count; device independence | GFDL, so archived but not relicensable. Unix-centric on paths and signals; silent on colour, JSON and subcommands |
| `CLIG` | [Command Line Interface Guidelines](https://clig.dev/), Prasad, Firshman, Tashian, Parish. CC BY-SA 4.0 | `corpus/writing/clig-dev.md` | Read in full (re-read for 4.0.0) | 2 | The TTY heuristic; help, output, errors, flags, interactivity, subcommands, robustness, signals, configuration, future-proofing, naming, analytics | Practitioners' synthesis, not measurement; Unix vantage; explicitly not for GUI or full-screen terminal programs |
| `12F-CLI` | Jeff Dickey, *12 Factor CLI Apps* | not archived (author's copyright); hash recorded | Read in full | 2 | Every route to help; `-h` reserved; one/two/three positional kinds; `--version`/`-V`; stdout vs stderr; the five parts of an error; start-up budget; no table borders; XDG and `%LOCALAPPDATA%` | A blog post, and partly an advertisement for one framework; numbers are the author's experience, not study |
| `HEROKU-CLI` | *CLI Style Guide*, Heroku Dev Center, last updated 2025-01-31 | not archived (Salesforce copyright); hash recorded | Read in full | 2 | Flags over args with a worked example; prompts always bypassable; 80-column descriptions; grep-parseable rows; `--json`; stdout stable after GA; actions on stderr | House style for one product's plugins; some advice is Node-specific and was not used |

Where the five disagree the conflict is recorded: `C13` (where the decisive
line goes), `C17` (confirmation without undo), `C18` (what an error line
starts with), `C19` (device independence vs the TTY heuristic).

## UX-writing sources — `corpus/copy/`, oracles `UX-TEXT-` and `UX-ERR-`

Added for 5.0.0 for `UX_WRITING_ORACLE.md` and `ERROR_MESSAGE_ORACLE.md`.
All were read in full on 2026-09-19. Thirty-one files are archived under
`corpus/copy/` with URL, fetch date and licence in each header; one could not
be archived and is recorded with the hash of the page read.

| ID | Source | Local path | Tier | Strong on | Limit |
|---|---|---|---|---|---|
| `GERR` | Google, *Writing Helpful Error Messages* — the course index and 14 units (error handling, target audience, identify the cause, invalid inputs, specify requirements, show the fix, provide examples, be concise, avoid double negatives, set the tone, terminology, format for readability, summary, back end). CC BY 4.0 | `corpus/copy/gerr-*.md` | 2 | The two questions an error answers; specificity with actual values; the curse of knowledge; tone without apology or humour; terminology consistency and the synonym warning; progressive disclosure for long errors | Developer-facing bias, stated on the page; says nothing about surfaces or severity |
| `GSTYLE` | Google developer documentation style guide: voice and tone, active voice, UI elements and interaction, word list, accessible documentation. CC BY 4.0 | `corpus/copy/gstyle-*.md` | 2 | The avoid-list that names most padding phrases; politeness limits; exclamation marks | Written for documentation, not UI strings — see conflict `C21` |
| `W32-CTRL` | Win32 UX Guide: progress bars, status bars, tooltips and infotips, balloons, command buttons, standard icons. CC BY 4.0 | `corpus/copy/w32-*.md` | 3 | Per-surface length ceilings; the three message types; false precision; Cancel versus Stop; detail that serves support rather than the reader | Windows 7 era; `STILL_VALID_INTERACTION_PRINCIPLE` for what text says, `VISUALLY_OBSOLETE` for appearance |
| `VS-UX` | Visual Studio UX Guidelines: notifications and progress. CC BY 4.0 | `corpus/copy/vs-notifications.md` | 2 | The fullest surface-selection table in the corpus, each method paired with when not to use it; synchronous versus asynchronous | One product's IDE; some rows are Visual Studio components with no general analogue |
| `MS-STYLE` (extended) | Microsoft Writing Style Guide: global writing tips, accessibility guidelines, formatting common text elements, describing interactions. CC BY 4.0 | `corpus/copy/msstyle-*.md` | 1 | Input-neutral verbs; global audience; formatting | Documentation-first |
| `GOVUK-AZ` | GOV.UK style guide, A to Z. Open Government Licence v3.0 | `corpus/copy/govuk-a-to-z.md` | 2 | Words to avoid, in a government-service register | Web content for the public |
| `NNG-ERR` | Nielsen Norman Group, *Error-Message Guidelines*, Neusesser and Sunwall, 2023-05-14 | **not archived** (copyright NN/g); SHA-256 `3743275088e5a70729a947f1a16c3672f492cffd5adf3ec0e14e3370b6c05454` | 2 | Visibility, proximity, severity-driven surface choice, premature errors, preserving input, codes for diagnostics only | One consultancy's guidance; its novelty exception is scoped by the article itself (`C20`) |

**Apple was not obtained.** The current Human Interface Guidelines are served
only as a JavaScript shell (`developer.apple.com/design/human-interface-guidelines/writing`
and the alerts, notifications, buttons and feedback pages); the DocC JSON
endpoints return 404; the legacy `library/archive` macOS HIG pages redirect to
the same shell; and the Wayback Machine holds no usable snapshot of the
wording or alerts pages. **No rule in this oracle cites Apple.** This is the
same treatment conflict `C4` gave the unusable Fluent 2 page: a gap is
recorded rather than a citation invented.

**Material and Android were not obtained.** `m3.material.io` and the Material 2
archive are JavaScript applications, and the Android writing pages return 404.
Google is represented instead by two server-rendered, CC BY 4.0 properties —
its developer documentation style guide and its error-message course. No rule
names a Material-specific surface.

**Three UX-writing books** named in the research brief — Podmajersky,
*Strategic Writing for UX*; Metts and Welfle, *Writing Is Designing*; Yifrah,
*Microcopy* — are not in `docs/` and were not obtained. Nothing is attributed
to them.

## Legacy Windows source

| ID | Source | Verified | Classification and use |
|---|---|---|---|
| `WIN7-DIALOGS` | Win32 UX Guide — Dialog Boxes | Archived 2026-09-19 (row in the platform table above) | As above |
| `WIN7-OTHER` | Other Win32 UX Guide topics | Only the index was seen | `CONTEXT_DEPENDENT` at best. No rule may cite a specific unseen page. Current guidance supersedes visuals and platform mechanics |

## Authority and legacy labels

- Tier 1: current Windows/accessibility/platform convention.
- Tier 2: interaction-design and HCI evidence.
- Tier 3: legacy Windows behavior used only where current guidance is silent.
- Tier 4: foundational concepts.
- Tier 1 (toolkit): a UI toolkit's own documentation. Authoritative on what
  the toolkit does; carries no authority on a design question.

Legacy claims use: `CURRENT`, `STILL_VALID_INTERACTION_PRINCIPLE`,
`CONTEXT_DEPENDENT`, `VISUALLY_OBSOLETE`, `PLATFORM_OBSOLETE`, or
`SUPERSEDED`. A single source can carry different labels for behavior and
appearance.

## Remaining source gaps

1. The six platform pages the core cites are archived; no other Windows,
   Fluent or WinUI documentation or samples are local. Platform claims
   beyond those pages remain traceable to URLs only.
2. No verified WinUI control behavior, multi-window API guidance, focus-visual
   specification, high-contrast behavior, or screen-reader test procedure.
3. No verified spacing scale, pointer/touch target minimum, corner radii,
   material/elevation values, motion durations, or non-text contrast ratio.
4. No source read gives a single length ceiling for a dialog. Win32 gives
   one sentence for the main instruction and three for the supplement;
   GOV.UK gives 25 words a sentence and 5 sentences a paragraph for web
   text; Win32 Notifications gives 48/200 characters. The `writing` module
   quotes each where it applies and does not invent a general number.
5. No source read discusses scientific notation in a displayed value.
   `UI-TEXT-010`'s last clause is derived from the plain-words rule and is
   marked MEDIUM.
6. No source in the corpus studies OCR correction UI, confidence calibration,
   Japanese segmentation, learning-state presentation or assistive-technology
   behavior for image-text correspondence. OCR rules remain explicit transfers.
7. No empirical source establishes an optimal pane count or universal density.
   Density must be chosen from task simultaneity, frequency, posture and measured
   legibility—not a fashion or a fixed number.
8. No source justifies a universal ban or mandate for cards, rounded corners,
   giant headers, floating action buttons, bottom navigation or animation. The
   oracle may reject them only when a task/rule conflict is demonstrated.
9. No Windows console source was read: virtual-terminal sequences, the legacy
   console host, PowerShell aliasing and the right pager on Windows are
   unverified. `12F-CLI` supplies `%LOCALAPPDATA%` for cache and nothing else
   about Windows. The `cli` module states its requirements generally and
   quotes the Unix mechanisms as the sources' examples; `tools/cli_check.py`
   reports its terminal-colour checks as N/A on Windows rather than guessing.
10. Dear ImGui's documentation states that accessibility is not supported and
    the public header exposes no accessibility API; no source describes a
    workaround. The `imgui` module reports the affected rules as
    `N/A (TOOLKIT)` rather than inventing one. Variable-font axes,
    right-to-left and shaped text in Dear ImGui are likewise undocumented in
    the files read.
11. No source quantifies the cost of an ImGui tool redrawing while idle;
    `UI-IMGUI-008` is SHOULD and MEDIUM for that reason.
12. No source read gives dedicated guidance on **empty states**;
    `UX-TEXT-027` is DERIVED and LOW and says so.
13. No source read gives a general **length ceiling for a dialog**. The
    per-surface ceilings that exist are quoted in `UX-TEXT-014`; the project
    budgets beside them are PROJECT CONVENTION and are labelled.
14. No source read studies **text produced by a language model**. The nine
    patterns in `UX_WRITING_ORACLE.md` §E are each rejected by a source for
    reasons unrelated to how the text was produced; the claim that generators
    produce them disproportionately is this project's observation.
15. **Apple, Material and Android** could not be obtained in any static form
    (above). Their absence is a gap in coverage, not a judgement.
