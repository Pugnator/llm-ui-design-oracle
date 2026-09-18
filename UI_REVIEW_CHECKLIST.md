# UI Review Checklist

Work through this against a proposed UI, a screenshot, or a diff. Answer each
item **PASS**, **FAIL**, **N/A**, or **NEEDS HUMAN JUDGMENT**.

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
| 4.2 | Are focus, selection and hover visually distinct? | `UI-SEL-001` |
| 4.3 | Does selection survive scrolling, pane toggles, background completion? | `UI-SEL-002` |
| 4.4 | Do multiple representations of one object highlight together? | `UI-SEL-003`, `UI-OCR-001` |
| 4.5 | Do click / Ctrl+click / Shift+click behave conventionally? | `UI-SEL-004` |
| 4.6 | Can the active mode be named from a screenshot alone? | `UI-MODE-001` |
| 4.7 | Is the mode indicator near the work, not only in a distant bar? | `UI-MODE-001` |
| 4.8 | Can any mode be entered accidentally? | `UI-MODE-002` |

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
| 6.3 | For work that may exceed ~10 s: determinate progress and an estimate? | `UI-FB-003` |
| 6.4 | Is every long operation cancellable, with cancel acknowledged at once? | `UI-FB-004` |
| 6.5 | Does background work leave the rest of the UI interactive? | `UI-FB-005` |
| 6.6 | Is status reported in the UI rather than by interruption? | `UI-FB-006` |

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

## 12. OCR-specific (all DERIVED — weigh accordingly)

| # | Question | Rule |
|---|---|---|
| 12.1 | Is region↔text correspondence perceptual rather than inferred? | `UI-OCR-001` |
| 12.2 | Is the source image visible while correcting text? | `UI-OCR-002`, `UI-ARCH-003` |
| 12.3 | Is low confidence findable in one scan, and in greyscale? | `UI-OCR-003` |
| 12.4 | Is recognised text editable, and failure not blamed on the user? | `UI-OCR-004`, `UI-ERR-003` |
| 12.5 | Does lookup preserve the line, its position and the selection? | `UI-OCR-005` |
| 12.6 | Is learning state visible where words appear, not colour-only? | `UI-OCR-006` |

## 13. Anti-pattern sweep

Scan `UI_ANTIPATTERNS.md` AP-01…AP-20. For each one present, state the
*condition* that makes it harmful here — or record it as acceptable with the
reason. Presence alone is not a finding.

---

## Reporting format

```
FINDING  <rule-id>  <PASS|FAIL|N/A|NEEDS HUMAN JUDGMENT>
Surface  <which surface, and its posture>
Class    <platform requirement | interaction principle | project convention>
Evidence <what was observed>
Source   <the citation from the oracle rule>
Fix      <smallest change that would pass, or the question a human must answer>
```

A review that reports only FAILs is incomplete: record the PASSes that were
checked, so the next reviewer knows what has already been looked at.
