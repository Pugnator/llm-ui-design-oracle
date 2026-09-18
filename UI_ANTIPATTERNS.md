# UI Anti-patterns

Patterns to look for during review. **None of these is unconditionally wrong.**
Each entry states the condition that makes it harmful, because a rule that
fires on every occurrence teaches reviewers to ignore it.

Format: what it looks like → when it is fine → when it is harmful → the source
that decides → the oracle rule.

---

## AP-01 — Dashboardization

**Looks like** The workspace becomes a grid of summary tiles; the primary
object is one card among many.

**Fine when** The surface's job really is overview across many items.

**Harmful when** A sovereign tool has one primary object. Tiles spend the space
the object needs and add a level of indirection to reach it.

**Decided by** Cooper Ch. 9 — a sovereign application *"begs to take up the
full screen"* for its content. Johnson Ch. 3 — visual hierarchy must match
information hierarchy.

**Rules** `UI-ARCH-001`, `UI-LAY-003`.

---

## AP-02 — Card layout as default container

**Looks like** Every group wrapped in a rounded, shadowed, padded card.

**Fine when** Items are genuinely peer objects in a collection.

**Harmful when** Used as generic grouping. Each card spends perimeter on
padding and border; nested cards multiply it. Cooper notes sovereign UI can
afford tighter spacing precisely because familiarity does the work ornament
would.

**Decided by** Johnson Ch. 2 — proximity and common region already group
without ornament. Cooper Ch. 9 (PDF p. 241).

**Rules** `UI-LAY-002`, `UI-LAY-001`.

---

## AP-03 — Navigation rail for a single-workspace app

**Looks like** A permanent left rail with icons for three or four destinations.

**Fine when** There are several genuinely separate top-level activities.

**Harmful when** There is one workspace. It permanently occupies horizontal
space in a tool that wants it for content, and imports a web solution to a
problem the app does not have.

**Decided by** Tidwell Ch. 3 read in scope with the preface (p. 15), which
scopes the book to *"Screen-Based, Web, and Mobile"*.

**Rules** `UI-NAV-001`.

---

## AP-04 — Hamburger menu on the desktop

**Looks like** Primary commands collapsed behind a single glyph.

**Fine when** Genuinely narrow layouts, for genuinely secondary commands.

**Harmful when** It hides frequent commands in a window with room to show them:
one extra click each time, and a command that must be recalled rather than
recognised.

**Decided by** Johnson Ch. 9 (recognition vs recall). Microsoft Commanding
basics — constantly needed commands belong on the canvas.

**Rules** `UI-CMD-001`, `UI-CMD-003`.

---

## AP-05 — Icon-only command overload

**Looks like** A toolbar of unlabelled glyphs, meanings available only on
hover.

**Fine when** A sovereign workspace the user sees daily, with accessible names
and tooltips (Cooper's *"do more with fewer pixels"*).

**Harmful when** On transient surfaces, or where glyphs are ambiguous or
custom. Cooper on transient posture: *"This is not the place for
artistic-but-ambiguous images and icons."*

**Decided by** Cooper Ch. 9 (PDF pp. 241, 243).

**Rules** `UI-ICON-001`, `UI-ICON-002`.

---

## AP-06 — Modal dialog proliferation

**Looks like** Dialogs for confirmation, for errors, for editing, for progress.

**Fine when** The interaction genuinely must block — an unrecoverable action
needing consent.

**Harmful when** Used for reversible actions or for input validation. It stops
the workflow and hides the context the decision depends on.

**Decided by** Microsoft: *"Dialogs can be disruptive and should only be used
in certain situations"*; confirm only what *"can't be undone"*. Legacy UX
guide: *"Use modeless error handling (in-place errors or balloons) for user
input problems."* Cooper Ch. 15 on rich modeless feedback.

**Rules** `UI-DLG-001`, `UI-DLG-003`, `UI-EDIT-004`, `UI-FB-006`.

---

## AP-07 — Hidden modes

**Looks like** The same click does different things depending on invisible
state.

**Fine when** The mode is continuously visible near the work and exits on
Escape.

**Harmful when** The indicator is distant (a far status bar is effectively
invisible — Johnson Ch. 5 on peripheral vision) or absent. Produces mode
errors: a well-learned action executed in the wrong context.

**Decided by** Johnson Chs. 5, 15.

**Rules** `UI-MODE-001`, `UI-MODE-002`, `UI-KBD-004`.

---

## AP-08 — Whitespace applied as a virtue

**Looks like** Consumer-app padding in a data-dense working surface; two panes
where four would fit.

**Fine when** Transient surfaces, onboarding, low-density reading.

**Harmful when** It forces scrolling or pane-switching in a comparison task, so
the user pays context switches for air. This is the C1 error.

**Decided by** Cooper Ch. 9 (PDF p. 241) — sovereign UI may pack *"more tightly
than you otherwise could"*. Bounded by `UI-TYPO-002` and `UI-COLOR-001`.

**Rules** `UI-LAY-001`, `UI-GLOBAL-002`.

---

## AP-09 — Controls that move

**Looks like** Recently-used commands float to the top; toolbars reorder;
late-loading content pushes buttons down.

**Fine when** The user explicitly rearranged it, and it then persists.

**Harmful when** Adaptive or asynchronous. It destroys motor memory and can
cause a click on the wrong thing.

**Decided by** Johnson Ch. 10 (learned actions), Ch. 13 (Fitts' Law assumes a
known location), Ch. 15 (slips).

**Rules** `UI-NAV-002`, `UI-LAY-005`.

---

## AP-10 — Context loss on selection or lookup

**Looks like** Selecting an item replaces the view; a lookup popup covers the
line being read; a background refresh clears the selection.

**Fine when** The user asked to navigate away.

**Harmful when** The new information is *about* the thing now hidden. The user
must hold the source in working memory — a few items at best.

**Decided by** Johnson Ch. 7; Cooper Ch. 15 (modeless feedback).

**Rules** `UI-SEL-002`, `UI-OCR-005`, `UI-ARCH-003`.

---

## AP-11 — Mouse-only repetition

**Looks like** The correction loop requires pointing, dragging or menu
traversal every iteration.

**Fine when** The operation is genuinely occasional.

**Harmful when** On the primary repeated loop: pure excise, multiplied by every
repetition, and it locks out keyboard users entirely.

**Decided by** Cooper Ch. 12 (excise); Johnson Ch. 13 (Fitts, Steering);
accessibility baseline.

**Rules** `UI-CMD-002`, `UI-KBD-001`, `UI-EXP-002`.

---

## AP-12 — Essential commands in overflow

**Looks like** A "…" menu holding something needed every session.

**Fine when** Genuinely rare or destructive commands.

**Harmful when** Frequency says otherwise. Overflow is for the tail.

**Decided by** Microsoft Commanding basics; Cooper Ch. 12.

**Rules** `UI-CMD-001`, `UI-CMD-003`.

---

## AP-13 — Hover as the only discovery mechanism

**Looks like** Controls that appear on hover; meaning available only in
tooltips.

**Fine when** Hover *supplements* a visible affordance — progressive
disclosure of detail.

**Harmful when** It is the sole route. Hover does not exist for keyboard or
touch, leaves no trace in a screenshot, and requires knowing where to point.

**Decided by** Johnson Ch. 9; accessibility baseline.

**Rules** `UI-MOUSE-003`, `UI-CMD-004`.

---

## AP-14 — Colour as the only signal

**Looks like** Confidence, learning state or validity shown by hue alone.

**Fine when** Colour is redundant with another channel.

**Harmful when** Sole carrier. About 8% of men and 0.5% of women are red-green
colourblind, and contrast checks *"do not account for hue perception"*.

**Decided by** Microsoft Color; Johnson Ch. 4.

**Rules** `UI-COLOR-003`.

---

## AP-15 — Confirmation instead of undo

**Looks like** "Are you sure?" on reversible actions.

**Fine when** The action is genuinely unrecoverable.

**Harmful when** Reversible. Microsoft: confirmations *"are a hindrance
whenever the user is trying to perform an action intentionally"* — and a dialog
answered by reflex protects nobody.

**Decided by** Microsoft Commanding basics; Cooper Ch. 15; Johnson Ch. 15
(capture slips).

**Rules** `UI-DLG-003`, `UI-EDIT-001`, `UI-DLG-005`.

---

## AP-16 — Spinner instead of progress

**Looks like** An indeterminate animation for an operation of unknown length,
with no cancel.

**Fine when** The work is reliably shorter than about a second.

**Harmful when** It can exceed the unit-task window: the user cannot judge
whether to wait, and past ~10 s attention leaves and must be rebuilt. Johnson
names the exact failure — *"no progress bar (just a busy bar) and no cancel"*.

**Decided by** Johnson Ch. 14 (Figs. 14.1, 14.2).

**Rules** `UI-FB-003`, `UI-FB-004`.

---

## AP-17 — Explaining the implementation on screen

**Looks like** A message describing what the software tried, what state it is
in, or why it behaves this way.

**Fine when** In logs, commits and design docs.

**Harmful when** On screen. The reader did not write the program and can act
only on the result or the next step.

**Decided by** Guidelines overview (Writing); Johnson Ch. 6; and any stricter
writing standard the project names in its profile (`UI-ERR-001`).

**Rules** `UI-ERR-001`.

---

## AP-18 — Blaming the user for recognition failure

**Looks like** "Invalid input", "Could not understand", after OCR misreads.

**Fine when** The user genuinely supplied something the system cannot accept
and can fix.

**Harmful when** The system guessed and guessed wrong. Guessing is its job.

**Decided by** Johnson Ch. 15: *"Voice-Recognition Failure and Misrecognition
are Not User Errors."*

**Rules** `UI-ERR-003`, `UI-OCR-004`.

---

## AP-19 — Static text in the tab order

**Looks like** Tabbing lands on labels and read-only values.

**Fine when** Never, as a way of exposing text to screen readers.

**Harmful when** Always: *"Users expect tab stops to be actionable, and static
content in tab order is usually a usability regression."* Screen readers reach
it through reading modes anyway.

**Decided by** Microsoft Accessible text requirements.

**Rules** `UI-KBD-003`, `UI-A11Y-002`.

---

## AP-20 — Designing for the first five minutes

**Looks like** Permanent onboarding, oversized primary actions, explanatory
text that never goes away.

**Fine when** Transient surfaces, or dismissible first-run help.

**Harmful when** It permanently occupies a sovereign workspace. Every session
after the first pays for the first.

**Decided by** Cooper Ch. 9, "Target intermediate users" (PDF p. 240).

**Rules** `UI-EXP-001`, `UI-ARCH-001`.
