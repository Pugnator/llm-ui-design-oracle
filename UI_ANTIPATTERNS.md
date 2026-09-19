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

**Decided by** Johnson Ch. 7, “Modes” (book pp. 114–115), and Ch. 15,
“Mode slips” (book pp. 267–269); Cooper Ch. 18, “Modal tools and palettes.”

**Rules** `UI-MODE-001`, `UI-MODE-002`, `UI-KBD-004`.

---

## AP-08 — Whitespace applied as a virtue

**Looks like** Consumer-app padding in a data-dense working surface; two panes
where four would fit.

**Fine when** Transient surfaces, onboarding, low-density reading.

**Harmful when** It forces scrolling or pane-switching in a comparison task, so
the user pays context switches for air. This is the C1 error.

**Decided by** Cooper Ch. 9 (book pp. 211–214; PDF pp. 241–244) — sovereign UI
may pack more tightly. Tidwell Ch. 4, “Density” (book pp. 212–213), demonstrates
that a less-dense example can be harder to read and group. Bounded by
`UI-TYPO-002`, `UI-COLOR-001` and `UI-A11Y-003`.

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

**Looks like** The primary loop requires pointing, dragging or menu
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
colourblind, and contrast evaluation *"does not account for hue perception"*.

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

**Harmful when** Work lasts more than a few seconds and progress/remaining work
is knowable: the user cannot judge whether to wait. Johnson calls for a progress
indicator after a few seconds; the later ~10 s attention limit explains the
cost of silence but is not the progress trigger.

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

---

## AP-21 — One highlight, several meanings

**Looks like** The same outline or fill is used for keyboard focus, selected OCR
region, current token, inspected item, hover and text caret context.

**Fine when** The states truly coincide and remain distinguishable if they later
diverge.

**Harmful when** The user cannot tell where typing will go, what a command will
act on, or which object the inspector describes. A single screenshot becomes
semantically ambiguous even though it looks visually consistent.

**Decided by** Tidwell Ch. 1, “Keyboard Only” (focus receives keys), Ch. 8
(object selection precedes commands), and Ch. 2 p. 113 (selected versus hovered
highlight); Cooper Ch. 18 requires visible, unambiguous selection.

**Rules** `UI-SEL-001`, `UI-SEL-003`, `UI-OCR-001`.

---

## AP-22 — Mobile command furniture transplanted to desktop

**Looks like** Bottom navigation, a floating action button, giant headers or a
hamburger/ellipsis surface used as the primary command model of a resizable
professional desktop window.

**Fine when** The control solves a demonstrated narrow-window, posture or
single-primary-action problem and does not hide the repeated loop.

**Harmful when** It hides frequent commands, covers working content, creates an
unjustified single visual focal point, or spends permanent comparison space on
navigation intended for another platform.

**Decided by** Tidwell's own web/mobile scope limitation; her Ch. 2 frequency
rule; Cooper Ch. 9 posture; `MS-COMMAND` command placement. Rounded corners or
the visual fashion alone are not a finding.

**Rules** `UI-NAV-001`, `UI-CMD-001`, `UI-CMD-003`, `UI-LAY-003`.

## AP-23 — The wall of text

**Looks like** A message of four or more sentences. Often each sentence is
individually true and well meant: what happened, why, what it means, what to
do, what not to worry about, what to try next.

**Fine when** In a help topic the operator chose to open.

**Harmful when** In a message, dialog, tooltip or status line. Win32 UI Text:
"too much text discourages reading; the eye tends to skip right over it —
ironically resulting in less communication rather than more." The reader
stops at the first sentence that lets them decide, and if the action was in
the fourth they never reach it.

**Decided by** `WIN7-TEXT` Error Messages ("brief — as short as possible, but
no shorter"; "aim for a maximum of three sentences"); `GOVUK-WG` (20–28% of
words read); `MS-STYLE` ("prune every excess word").

**Rules** `UI-TEXT-001`, `UI-TEXT-008`.

---

## AP-24 — The verdict word

**Looks like** *Error*, *invalid*, *illegal*, *failed*, *fatal*, *forbidden*,
*bad* — or a sentence with the operator as the subject of a mistake: *"You
entered…"*, *"You forgot…"*.

**Fine when** Never on screen. In a log file, *error* is a level and is fine.

**Harmful when** Shown to the person who just did the thing. Each word is
either redundant (the icon and the container already say it is a problem) or
an accusation, and the sources agree that an accused reader learns nothing
except to dismiss the next message faster.

**Decided by** `WIN7-TEXT` Error Messages (the word list and its
replacements); `GOVUK-DS` Error message ("forbidden, illegal, you forgot,
prohibited"; "valid and invalid … do not add anything"); `MS-STYLE` Verbs.

**Rules** `UI-TEXT-003`, core `UI-ERR-002`, `UI-ERR-003`.

---

## AP-25 — The apology as tone

**Looks like** *Sorry* or *please* in a message where nothing has been lost
and nothing inconvenient is being asked. *"Sorry, that value is out of
range."* *"Please select a file."*

**Fine when** Data was lost, the operator must wait or redo work, or the
software is at fault and the cost is real — the cases every source reserves
the words for.

**Harmful when** Used to soften. GOV.UK: *please* "implies a choice" — the
field now reads as optional; *sorry* "does not help fix the problem". Used
routinely, both words spend the register that a genuine loss will later need.

**Decided by** `GOVUK-DS` Error message; `WIN7-TEXT` Style and Tone;
`UI_CONFLICTS.md` C14.

**Rules** `UI-TEXT-004`.

---

## AP-26 — The transport as the message

**Looks like** The underlying library's own words on the face of a dialog:
*"PassThruWriteMsgs(ISO15765): ERR_TIMEOUT"*, *"ECONNREFUSED"*, *"could not
disarm before populating"*. Often accurate. Never addressed to the reader.

**Fine when** Behind a disclosure control, in the log file, or in a bug
report — every place where the reader is someone who can act on it.

**Harmful when** It is what the operator is given instead of a sentence.
Win32 names the leading cause: "explaining the problem from the code's point
of view instead of the user's". `CLIG`: "catch errors and rewrite them for
humans". It differs from AP-17 in what it is — AP-17 explains the
implementation, this quotes it — and the fix is the same: keep it, fold it,
write the message.

**Decided by** `WIN7-TEXT` Error Messages (Incomprehensible error messages;
Progressive disclosure; Error codes); `CLIG` Errors; `GOVUK-DS` Details.

**Rules** `UI-TEXT-002`, `UI-TEXT-006`, `UI-TEXT-008`, core `UI-ERR-001`.

---

## AP-27 — The blocking frame

**Looks like** A file open, a network call, a recogniser or a compile called
from inside the frame. The whole window stops painting; the progress bar
freezes; the cancel button is drawn but does nothing.

**Fine when** Never in a product. Tolerable in a throwaway debug tool nobody
else runs.

**Harmful when** Any operation can exceed a frame. In immediate mode there is
no separate painting path — *"if your code doesn't run the UI is gone!"* — so
the freeze is total: `UI-FB-005` fails completely rather than partially, and
`UI-FB-004`'s cancel cannot be reached.

**Decided by** `IMGUI-CPP` (Programmer guide, Read first); `IMGUI-FAQ` (About
Multi-Threading); Johnson Ch. 14.

**Rules** `UI-IMGUI-007`, `UI-FB-004`, `UI-FB-005`.

---

## AP-28 — The colliding ID

**Looks like** Two buttons labelled *Apply* in one window; a list of rows each
with its own *Delete*; a control with an empty label; a label that changes
with state.

**Fine when** Never. The toolkit calls it *"THE MOST COMMON USER MISTAKE"*.

**Harmful when** Always: *"Interacting with either button will trigger the
first one"* — the wrong row is deleted, the second *Apply* applies the first
thing. A changing label without `###` drops keyboard focus every time it
changes, which is `AP-09` at the scale of one control.

**Decided by** `IMGUI-FAQ` (About the ID Stack system); `IMGUI-H`
(`ConfigDebugHighlightIdConflicts`).

**Rules** `UI-IMGUI-005`, `UI-GLOBAL-005`, `UI-NAV-002`.

---

## AP-29 — The Christmas tree in the log

**Looks like** A CI log full of escape codes; a progress bar rendered as a
thousand lines of carriage-return frames; a spinner's characters interleaved
with the output.

**Fine when** The stream is an interactive terminal.

**Harmful when** stdout is not a TTY, `NO_COLOR` is set, or `TERM` is `dumb`.
The decoration was for a person who is not there; the person who is there —
reading the log later — gets noise, and the machine reading the pipe gets
bytes that are not data.

**Decided by** `CLIG` Output (Disable color if…; If stdout is not an
interactive terminal, don't display any animations); `12F-CLI` §6 ("You never
want to output those codes to a file"); `HEROKU-CLI` (Colors).

**Rules** `UI-CLI-009`, `UI-COLOR-003`.

---

## AP-30 — The mandatory prompt

**Looks like** *Continue? [y/N]* with no flag that answers it; a password read
only from the keyboard; a first-run wizard that cannot be skipped.

**Fine when** stdin is a terminal *and* every value the prompt collects can
also be passed as a flag.

**Harmful when** The program is run from a script, a CI job or a pipe. It
hangs, and the hang looks like a crash (`UI-FB-002`). A prompt that cannot be
bypassed is a program that cannot be composed.

**Decided by** `CLIG` Interactivity; Arguments and flags (Never require a
prompt); `12F-CLI` §7 ("Never require a prompt though"); `HEROKU-CLI`
(Prompting: "Ensure that args or flags can always be provided to bypass the
prompt").

**Rules** `UI-CLI-013`, `UI-CLI-015`, `UI-FB-002`.

---

## AP-31 … AP-39 — Anti-patterns of generated text

Nine patterns a language model produces by default: narrative explanation,
restating the obvious, internal reasoning shown, excessive consequences, fake
helpfulness, unnecessary politeness, dramatic language, developer prose in the
product, and documentation inside a dialog.

They share this catalogue's numbering but are **defined in
`UX_WRITING_ORACLE.md` §E**, with the source that rejects each one, a
detection heuristic, the legitimate exception, and a before-and-after. They
are not restated here, because a pattern described in two places drifts.

A review sweeps them from `UI_COPY_REVIEW_CHECKLIST.md` §9, not from this
file.
