# UI Source Matrix

What was consulted to build `UI_ORACLE.md`, what each source is good for, and
where it must not be trusted. Compiled 2026-09-18.

**Verification status** says whether *this* matrix was built by reading the
source directly. Nothing in the oracle cites a source marked "not available".

---

## Tier 1 — Current Windows platform authority

| Source | Version / date | Verified | Scope | Strong on | Weak / obsolete |
|---|---|---|---|---|---|
| [Design principles](https://learn.microsoft.com/en-us/windows/apps/design/design-principles) | `ms.date` 2025-12-11, updated 2026-07-14 | Read in full | Windows 11 design values | The five principles (Effortless, Calm, Personal, Familiar, Complete + Coherent); names the signature experiences | Values, not rules. Nothing testable. Written for consumer Windows, not professional tools |
| [Design guidelines overview](https://learn.microsoft.com/en-us/windows/apps/design/guidelines-overview) | `ms.date` 2026-09-05 | Read in full | Index of guidance areas | Authoritative list of current topic areas; explicitly links the legacy archive and says to use it "for historical context" only | Index only |
| [Color in Windows](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/color) | `ms.date` 2024-09-19, updated 2026-07-14 | Read in full | Color modes, accent, usability | Accent = emphasis + interactive state; light/dark; colorblindness figures (~8% of men, 0.5% of women, red-green) | No contrast ratios here (they live in the accessibility topic); no semantic error/warning/success palette |
| [Typography in Windows](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/typography) | `ms.date` 2021-06-24, updated 2026-07-14 | Read in full | Type ramp, fonts, legibility | **The only verified numeric type scale.** Weights, minimum sizes, line length, per-language fonts incl. **Yu Gothic UI for Japanese** | Oldest `ms.date` of the Tier 1 set. **Contains an internal contradiction on truncation** — see `UI_CONFLICTS.md` C2 |
| [Accessible text requirements](https://learn.microsoft.com/en-us/windows/apps/design/accessibility/accessible-text-requirements) | `ms.date` 2026-08-21, updated 2026-08-26 | Read in full | Contrast, UIA text roles, text scaling | **4.5:1** contrast (aligned to W3C WCAG 2.0 G18); `TextScaleFactor` range **[1, 2.25]**; static text must not be a tab stop; don't rely on high-contrast mode as the mitigation | Contrast guidance stated for text; non-text contrast not covered here |
| [Commanding basics](https://learn.microsoft.com/en-us/windows/apps/design/basics/commanding-basics) | `ms.date` 2020-09-24, updated 2026-06-27 | Read in full | Command surfaces and placement | Canvas vs command bar vs menu vs dialog; direct manipulation preferred; **confirm only unrecoverable actions, otherwise offer undo** | Older `ms.date`; examples are consumer-flavoured; says little about keyboard-first workflows |
| [Fluent 2 — Windows components](https://fluent2.microsoft.design/components/windows) | Fetched 2026-09-18 | Fetched — **contains no component documentation** | — | — | **Not usable as a rule source.** The page is promotional/navigational and defers: "To get the building blocks for crafting Windows experiences, use WinUI." No components, no values. Recorded so nobody cites it as authority |
| WinUI 3 Gallery | Referenced by MS pages; **app not installed here** | Not verified | Live control examples | Would be the authority for real control behaviour and defaults | Not consulted — no rule in the oracle cites it |

## Tier 2 — General interaction-design authority

| Source | Edition | Verified | Strong on | Weak / caution |
|---|---|---|---|---|
| Cooper, Reiman, Cronin, Noessel — *About Face: The Essentials of Interaction Design* | 4th ed. (PDF, `docs/books/`, 722 pp.) | TOC + targeted chapters read | **Posture** (Ch. 9, PDF p.235): sovereign / transient / daemonic — the single most load-bearing concept for this app. Excise (Ch. 12, p.301). Errors, undo, modeless feedback (Ch. 15, p.387–393). Menus (p.478), toolbars/palettes/sidebars (p.485), pointing/selection/direct manipulation (p.495). Dialogs (p.655). Eliminating errors, alerts, confirmations (p.671) | Pre-dates Windows 11 visuals entirely. Use for behaviour and structure, never for styling. Opinionated; some claims are argued rather than measured |
| Tidwell, Brewer, Valencia-Brooks — *Designing Interfaces* | 3rd ed. (PDF, `docs/books/`, 602 pp.) | TOC read; chapter map established | Pattern catalogue. Ch. 2 Information Architecture (p.47), Ch. 3 Navigation (p.149), Ch. 4 Layout of Screen Elements (p.229), Ch. 7 Lists (p.355), Ch. 8 Actions and Commands (p.395), Ch. 9 **Showing Complex Data** (p.453), Ch. 10 Forms and Controls (p.491) | The preface states the focus is "Screen-Based, Web, and Mobile" — so web/mobile assumptions must be filtered out before applying to a desktop tool |
| Johnson — *Designing with the Mind in Mind* | 3rd ed., 2021 (EPUB, `docs/books/`) | TOC + Ch. 14 read in detail | **Table 14.1 durations** — the only verified quantitative basis for latency rules. Gestalt (Ch. 2), visual hierarchy (Ch. 3), color vision limits (Ch. 4), peripheral vision (Ch. 5), recognition vs recall (Ch. 9), Fitts' & Steering laws (Ch. 13), errors: mistakes vs slips (Ch. 15) | Explains *why*, rarely prescribes platform specifics. Numbers are human constants, not Windows requirements |

## Tier 3 — Legacy Windows interaction guidance

| Source | Date | Verified | Status |
|---|---|---|---|
| [Win32 UX Guide — Dialog Boxes](https://learn.microsoft.com/en-us/windows/win32/uxguide/win-dialog-box) | `ms.date` 2022-01-25, updated 2025-07-24 | Read (9,003 words) | Page title self-identifies as **"Windows 7 Dialog Boxes"**. Interaction rules largely STILL RELEVANT (e.g. "Don't use OK buttons in modeless dialog boxes… use task-specific commit buttons"; "Don't use Cancel buttons in modeless dialog boxes… use Close"; "Use modeless error handling (in-place errors or balloons) for user input problems"). All visuals VISUALLY OBSOLETE |
| Win32 UX Guide — other topics (menus, keyboard, visuals) | Various | Index seen via guidelines-overview | The current guidelines page lists these under "Historical design guidelines" and says: use them for historical context; "For apps you build today, follow the current Fluent guidance above." Treated per the legacy classification scheme in the oracle |

## Tier 4 — Foundational

| Source | Edition | Verified | Strong on | Weak / caution |
|---|---|---|---|---|
| Norman — *The Design of Everyday Things* | Revised ed. (PDF, `docs/books/`, 369 pp.) | **Added 2026-09-18.** TOC + Chs. 1, 2, 5 read in detail | **The seven fundamental design principles** (Ch. 2, book pp. 72–73) quoted verbatim in the oracle: discoverability, feedback, conceptual model, affordances, signifiers, mappings, constraints. The **affordance vs signifier** distinction the revised edition exists to make (Ch. 1, pp. 13–14). Seven stages of action and the gulfs of execution/evaluation (p. 57–59). Feedforward vs feedback (p. 72). Four kinds of constraints and forcing functions (Ch. 4, pp. 142–168). **The origin of the slip/mistake taxonomy** and *"Human Error? No, Bad Design"* (Ch. 5, pp. 181–235) | Deliberately not software-specific — most examples are doors, stoves and faucets. Says nothing about Windows, controls, density or typography, and must never be used to override Tier 1 on appearance. Concepts, not measurements |

**Note on the first draft.** This book was unavailable when the oracle was
first written, and that absence was recorded rather than papered over with
remembered citations. It has now been read and the oracle revised: five new
Tier 4 rules, two error rules re-grounded, conflict C8 closed.

## Present but out of scope

`docs/books/` also holds game-design texts (Schell, Koster, Engelstein) and
Japanese-language textbooks. Not consulted: neither bears on Windows desktop
UI. Listed so the omission is visible rather than accidental.

## Known gaps in this matrix

Recorded so the oracle does not pretend to cover them:

1. **No verified spacing/sizing scale.** The Fluent/Windows layout and
   geometry pages were not fetched. The oracle therefore states **no** numeric
   margins, paddings, corner radii or control sizes. Any such number appearing
   in future UI work must be sourced then, not invented now.
2. **No verified minimum target size.** Neither a mouse nor a touch target
   minimum was read from a current Microsoft page. Deliberately absent.
3. **WinUI 3 Gallery not exercised.** Control-level behaviour is unverified.
4. **Motion, materials (Mica/Acrylic), elevation, haptics, widgets** — named
   by the guidelines index, not read. No rules issued for them.
5. **Non-text contrast** (icons, focus rings, borders) — the accessibility
   page read covers *text* contrast. No non-text ratio is asserted.
