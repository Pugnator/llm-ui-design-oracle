# UI Source Matrix

Inventory of the evidence used by the oracle. Revised 2026-09-18 after a
recursive inspection of the repository and a full-text concept search of every
local book. The local corpus is the primary evidence base; current platform
pages retained from the first research pass are listed separately because they
are not local snapshots and can change.

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

## Current Windows sources — rechecked, non-local

These pages remain Tier 1 because the oracle needs current platform and
accessibility requirements that the books cannot provide. They were rechecked
on 2026-09-18, but the repository contains no archival copy. “Last updated” is
the date currently displayed by Microsoft Learn, not an inferred publication
date.

| ID | Source | Recorded version/date and verification | Tier | Strong on | Limit |
|---|---|---|---|---|---|
| `MS-PRINCIPLES` | [Windows design principles](https://learn.microsoft.com/en-us/windows/apps/design/design-principles) | Last updated 2025-12-18; rechecked 2026-09-18 | 1 | Current Windows values | Values, not testable control rules; consumer/shell emphasis |
| `MS-INDEX` | [Design guidelines overview](https://learn.microsoft.com/en-us/windows/apps/design/guidelines-overview) | Last updated 2026-09-05; rechecked 2026-09-18 | 1 | Current topic map and explicit classification of Win32 UX pages as historical | Index only |
| `MS-COLOR` | [Color in Windows](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/color) | Last updated 2026-07-14; rechecked 2026-09-18 | 1 | Accent, themes, colour redundancy | No semantic palette and no non-text contrast ratio |
| `MS-TYPE` | [Typography in Windows](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/typography) | Last updated 2026-04-14; rechecked 2026-09-18 | 1 | Type ramp, minimums, measure and script fonts | Internally contradictory on truncation; see C2 |
| `MS-A11Y-TEXT` | [Accessible text requirements](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/accessible-text-requirements) | Last updated 2026-08-26; rechecked 2026-09-18 | 1 | 4.5:1 visible-text contrast, text scale `[1, 2.25]`, UIA text roles, static-text tab stops | Text-specific; does not establish non-text contrast or all keyboard behavior |
| `MS-COMMAND` | [Commanding basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/commanding-basics) | Last updated 2022-08-01; rechecked 2026-09-18 | 1 | Command placement, direct manipulation, confirm vs undo | Older page with consumer-flavoured examples; little expert-keyboard detail |
| `FLUENT2-WIN` | [Fluent 2 Windows overview](https://fluent2.microsoft.design/components/windows) | Rechecked 2026-09-18 | — | Directs Windows designers to WinUI components and resources | Overview only; contains no component guidance from which to derive a rule |

## Legacy Windows source

| ID | Source | Verified | Classification and use |
|---|---|---|---|
| `WIN7-DIALOGS` | [Win32 UX Guide — Dialog Boxes](https://learn.microsoft.com/en-us/windows/win32/uxguide/win-dialog-box) | Rechecked 2026-09-18; page displays “Last updated” 2022-02-08 and self-identifies as Windows 7 guidance | `STILL_VALID_INTERACTION_PRINCIPLE` for modeless commit/Close semantics, in-place input errors and non-destructive defaults; `VISUALLY_OBSOLETE` for appearance; not used as current component authority |
| `WIN7-OTHER` | Other Win32 UX Guide topics | Only the index was seen | `CONTEXT_DEPENDENT` at best. No rule may cite a specific unseen page. Current guidance supersedes visuals and platform mechanics |

## Authority and legacy labels

- Tier 1: current Windows/accessibility/platform convention.
- Tier 2: interaction-design and HCI evidence.
- Tier 3: legacy Windows behavior used only where current guidance is silent.
- Tier 4: foundational concepts.

Legacy claims use: `CURRENT`, `STILL_VALID_INTERACTION_PRINCIPLE`,
`CONTEXT_DEPENDENT`, `VISUALLY_OBSOLETE`, `PLATFORM_OBSOLETE`, or
`SUPERSEDED`. A single source can carry different labels for behavior and
appearance.

## Remaining source gaps

1. No local Windows, Fluent, WinUI documentation or samples. Platform claims
   remain traceable to URLs but are not reproducible from the local corpus.
2. No verified WinUI control behavior, multi-window API guidance, focus-visual
   specification, high-contrast behavior, or screen-reader test procedure.
3. No verified spacing scale, pointer/touch target minimum, corner radii,
   material/elevation values, motion durations, or non-text contrast ratio.
4. No source in the corpus studies OCR correction UI, confidence calibration,
   Japanese segmentation, learning-state presentation or assistive-technology
   behavior for image-text correspondence. OCR rules remain explicit transfers.
5. No empirical source establishes an optimal pane count or universal density.
   Density must be chosen from task simultaneity, frequency, posture and measured
   legibility—not a fashion or a fixed number.
6. No source justifies a universal ban or mandate for cards, rounded corners,
   giant headers, floating action buttons, bottom navigation or animation. The
   oracle may reject them only when a task/rule conflict is demonstrated.
