# UI Research Gaps

Gap analysis performed 2026-09-18 against oracle 1.0.0 before revising it to
2.0.0. This is a research ledger, not an extra source of rules. `RESOLVED`
means the supplied corpus answered the question and the named artifact was
updated. `OPEN` means the oracle must remain silent, conditional, derived or
project-specific.

## Baseline findings

The existing work was structurally strong: stable rule IDs, explicit source
tiers, confidence labels, review tests, a legacy policy and conditional
anti-patterns. Its weakest points were provenance granularity and overclaiming:

- there was no evidence layer between raw sources and synthesized rules;
- the matrix listed incorrect local paths and sources not present in this
  checkout;
- rule verification status was implicit in `Provenance` rather than audited;
- linked selection, keyboard focus, modes, dense layouts and multi-window
  behavior had much stronger local evidence than their citations showed;
- the progress rule used the 10-second attention limit as its trigger even
  though Johnson calls for a progress indicator after a few seconds;
- one checklist item still cited retired rule `UI-OCR-006`;
- the README said “87 core rules”; the actual 1.0.0 set had 81 core rules plus
  five active and one retired OCR rule.

## Topic gap ledger

| Priority | Topic | Before the pass | Result | Disposition |
|---|---|---|---|---|
| P0 | Professional workspace architecture | Mostly Cooper posture, with little corroboration | `RESOLVED WITH QUALIFICATION` | Cooper Ch. 9 directly supports sovereign, adjacent-pane workspaces; Ch. 18 supports sidebars for complex authoring. Tidwell Chs. 2/4 supports Canvas Plus Palette and collapsible/movable panels. No source fixes pane placement or count |
| P0 | Selection versus keyboard focus | Semantics asserted but evidence weakly located | `RESOLVED WITH QUALIFICATION` | Tidwell Ch. 1 p. 24 defines keyboard focus as the control receiving keys; Ch. 8 pp. 379–380 describes object selection and tab focus; p. 113 distinguishes selected from hovered/highlighted. Cooper Ch. 18 requires selection state to be visually evident. The full OCR state taxonomy remains a derived application model |
| P0 | Linked representations | Derived only from Gestalt | `RESOLVED` | Tidwell Ch. 9, Data Brushing, pp. 458–460 directly describes simultaneous selection in linked views and explains why coordination reinforces shared identity |
| P0 | Modes and mode errors | Strong principle, but spring-loaded modes were marked LOW/derived | `RESOLVED` | Johnson Ch. 7 pp. 114–115 defines mode errors and requires clear continuous feedback; Ch. 15 pp. 267–269 explicitly recommends strong indication, normal-mode reversion and spring-loaded modes. Cooper Ch. 18 pp. 494–496 explains where modal tools scale poorly |
| P0 | OCR/background processing feedback | Timing evidence present but threshold synthesized incorrectly | `RESOLVED` | Johnson Ch. 14 pp. 235–254: acknowledge by about 0.1 s; busy/progress indication by about 1 s; determinate progress for operations longer than a few seconds; allow abort; keep other work possible; keep indicators honest |
| P0 | OCR correspondence and context | General memory argument only | `RESOLVED WITH QUALIFICATION` | Data Brushing and coordinated views directly ground synchronized region/text/token selection. Johnson Ch. 7 grounds persistent status/context. Exact OCR mapping remains derived because no source studies OCR UI |
| P1 | Dense professional UI | Risk of “more whitespace is always better” rejection without enough nuance | `RESOLVED` | Cooper Ch. 9 permits denser sovereign controls; Tidwell Ch. 2 p. 34 says experienced users can be efficient with densely packed selectors; Tidwell Ch. 4 pp. 212–217 shows low density can weaken grouping and proximity. Density is contextual, never a universal maximum |
| P1 | Keyboard-heavy expert workflows | Supported by accessibility and excise, not the most direct local text | `RESOLVED` | Tidwell Ch. 1 pp. 23–25 gives a Keyboard Only pattern; Ch. 8 p. 380 supports shortcuts and tab order for accessibility and experienced users. About Face Ch. 18 supports visible accelerator annotations |
| P1 | Panes and inspectors | Generic and under-cited | `RESOLVED WITH QUALIFICATION` | About Face Ch. 18 says sidebars manipulate object/document properties without dialogs and streamline complex authoring. Tidwell Ch. 4 gives Collapsible/Movable Panels. Exact docking behavior remains open |
| P1 | Command placement and context menus | Current Microsoft source dominated | `RESOLVED` | Tidwell Ch. 2 p. 33 independently says frequent workflow items should be immediately available; Ch. 8 notes some users never look for context menus and describes menu bars as keyboard/screen-reader accessible; About Face Ch. 18 supports shortcut annotations |
| P1 | Inline editing | Working-memory inference | `RESOLVED WITH QUALIFICATION` | Tidwell Ch. 8 p. 379 identifies double-click-to-edit-in-place as learned desktop behavior; About Face Ch. 21 shows dialogs can obscure the main work area. “Always inline” would still be too broad, so the rule retains exceptions |
| P1 | Undo/redo/history | Well covered by Cooper only | `RESOLVED` | Johnson Ch. 15 pp. 270–271 explicitly recommends reversibility and undo; Tidwell Ch. 8 contains Multilevel Undo and Command History; Cooper Ch. 15 covers mental models and histories |
| P1 | Modal versus modeless | Current and legacy Microsoft split recorded | `RESOLVED` | About Face Chs. 15/21 independently supports rich modeless feedback, sidebars and dialogs as secondary/out-of-flow. Legacy dialog behavior stays interaction-only |
| P1 | Multi-window behavior | “Opt-in, never default” based on one source | `RESOLVED WITH QUALIFICATION` | Cooper Ch. 18 says multiple windows are not a good general small-screen solution but have important occasional uses. Tidwell Ch. 2 says visual editors often offer Many Workspaces. The rule now permits deliberate multi-document/multi-monitor work without treating windows as routine popups |
| P1 | Errors and recognition failure | Good general evidence | `RESOLVED` | Johnson Ch. 15 pp. 273–274 directly states that recognition failure is a system error in the analogous speech domain and says correction is the system’s responsibility; Norman Ch. 5 grounds design-caused error |
| P2 | Accessibility beyond text | Current page covered only accessible text | `OPEN` | Need current, archived Windows/WinUI sources for focus visuals, UI Automation patterns, non-text contrast, high contrast, Narrator and zoom. The oracle must not invent these details |
| P2 | Exact control metrics | Missing | `OPEN` | No spacing, target size, corner radius, animation-duration or non-text contrast source is in the corpus. Numeric silence is intentional |
| P2 | OCR confidence calibration | No OCR-specific source | `OPEN` | The conditional rule can require confidence to be findable and redundant if displayed, but cannot prescribe thresholds, colors or ranking algorithms |
| P2 | Japanese OCR/tokenization/accessibility | No domain source | `OPEN` | No universal rule beyond preserving correspondence and using appropriate script fonts. Segmentation, reading and dictionary conventions require domain research |
| P2 | Multi-window accessibility and synchronization | No platform/API source | `OPEN` | Keep the interaction principle; defer focus restoration, owner/activation mechanics and automation details |
| P2 | “Modern UI” aesthetics | Mostly fashion, not usability evidence | `OPEN BY DESIGN` | Cards, rounding, margins, headers and animation are judged only through hierarchy, grouping, density, motion stability and task cost. The corpus does not justify aesthetic bans |

## Rules that had relied too heavily on model synthesis

These were audited most aggressively:

- `UI-NAV-001`: retained only as a scoped, derived rule for a genuinely
  single-workspace tool; it is not a universal ban on rails or hamburger menus.
- `UI-ARCH-003`, `UI-SEL-003`, `UI-OCR-001`, `UI-OCR-002`, `UI-OCR-005`:
  re-grounded in coordinated views/Data Brushing and working-memory evidence;
  still marked derived where OCR is the transfer.
- `UI-CMD-006`: remains conditional; a disabled command need not explain an
  obvious precondition.
- `UI-MODE-002`: deliberate entry/exit remains a synthesis; Escape behavior is
  separately grounded in Windows dialog convention.
- `UI-COLOR-005`: palette implementation is a project convention, not a
  universal HCI law.
- `UI-ERR-001`: the plain-language principle is general; any stricter writing
  standard is a project binding.

## Final audit

1. Rules relying primarily on non-local platform pages are visibly identified
   in `UI_EVIDENCE.md`; this is unavoidable until local Windows docs exist.
2. No unsupported spacing, target-size, corner-radius, animation-duration or
   non-text-contrast number is present.
3. The 0.1 s, 1 s, “few seconds,” 6–30 s and 10 s timing statements now retain
   their distinct contexts instead of being collapsed into one threshold.
4. Consumer/mobile patterns are not applied without a desktop/posture check.
5. Aesthetic preferences do not fire findings without a task consequence.
6. Legacy Windows visuals are discarded; retained dialog rules are labeled
   interaction principles.
7. OCR rules remain derived and conditional, never represented as empirical OCR
   findings.
8. Every active rule is included in the verification ledger in
   `UI_EVIDENCE.md`; the retired OCR ID is separately tombstoned.
9. Review questions were tightened for state ambiguity, background processing,
   density tradeoffs and multi-window behavior.
10. Remaining open questions are explicit above rather than filled from model
    memory.
