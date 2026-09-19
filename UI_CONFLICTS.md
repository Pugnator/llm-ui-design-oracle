# UI Conflicts

Where the sources disagree, what caused the disagreement, and how the oracle
resolves it. Every conflict below was found by reading the sources, not
anticipated in the abstract.

A conflict is recorded even when the resolution is obvious. Silent choices are
what make a spec untrustworthy later.

---

## C1 — "Calm and decluttered" vs. the density a professional tool needs

**Positions**

- **Tier 1.** Windows 11 design principles: *"Calm — Windows 11 is softer and
  decluttered; it fades into the background."* Color: *"emphasizing significant
  items only when necessary."*
- **Tier 2.** Cooper, *About Face* 4e, Ch. 9 (PDF p.241, book p.213):
  *"Sovereign interfaces should feature a conservative visual style… This gives
  you, the designer, freedom to do more with fewer pixels. Toolbars and their
  controls can be smaller than normal. Auxiliary controls such as screen
  splitters, rulers, and scrollbars can be smaller and more closely spaced."*
  And on colour: *"Big colorful controls may look really cool to newcomers, but
  they seem garish after a couple of weeks of daily use. Tiny dots or accents of
  color will have more effect in the long run."*

**Cause of the difference**

Audience and dwell time, not era. The Windows principles describe the *shell*
and consumer apps, which a user passes through. Cooper is describing
applications a user inhabits for hours and becomes expert in. Both texts are
current in their own domain.

**Resolution**

Not a contradiction once posture is named. The oracle adopts Cooper's posture
distinction as its organising axis (`UI-ARCH-001`) and applies "calm" as
*restraint in colour and ornament*, not as *low information density*:

- Sovereign surfaces (the main workspace) MAY be dense, with tightly spaced
  auxiliary controls and small accents of colour rather than large ones.
- Transient surfaces (popups, flyouts, the word-info card) MUST be bold,
  obvious and generously spaced — Cooper is explicit that transient UI needs
  larger controls and unambiguous labels, which coincides with "calm".

**Confidence** HIGH. The two sources are addressing different postures and
Cooper says so directly.

---

## C2 — Microsoft contradicts itself on truncation, on one page

**Positions**, both from
[Typography in Windows](https://learn.microsoft.com/en-us/windows/apps/design/signature-experiences/typography)
(Microsoft Learn displays “Last updated” 2026-04-14; rechecked 2026-09-18):

- "Typography best practices in Windows 11" table, *Truncation* row:
  *"Use ellipses in most cases; clipping is only used in rare cases."*
- "Clipping and ellipses" section, a few screens later: *"we recommend clipping
  the text and inserting ellipses"*, then a **Do**: *"Clip text, and wrap if
  multiple lines are enabled"* and a **Don't**: *"Don't use ellipses to avoid
  visual clutter."* Followed by a Note: *"If containers are not well-defined
  (for example, no differentiating background color), or when there is a link
  to see more text, then use ellipses."*

**Cause**

Two passages written at different times and never reconciled. The prose section
reads as the Windows 10-era guidance; the best-practices table as the Windows 11
overlay. The page gives no precedence.

**Resolution**

Follow the **Note**, which is the only passage that states a *condition* rather
than a preference, and which both other passages can be read as consistent with:

- Ellipsis when the container edge is not itself visible, or when a "more"
  affordance exists.
- Clipping when the container is clearly bounded (its own background, border or
  pane edge) so the clip is self-evidently a clip.

Recorded as `UI-TYPO-006`, marked MEDIUM confidence precisely because the
source is self-contradictory. **Do not cite this page as settled.**

---

## C3 — Legacy dialog guidance vs. current WinUI dialog controls

**Positions**

- **Tier 3.** Win32 UX Guide, "Windows 7 Dialog Boxes": detailed normative
  rules — *"Don't use OK buttons in modeless dialog boxes. Rather, modeless
  dialogs should use task-specific commit buttons (for example, Find)"*;
  *"Don't use Cancel buttons in modeless dialog boxes. Rather, use Close
  instead"*; *"Use modeless error handling (in-place errors or balloons) for
  user input problems."*
- **Tier 1.** Commanding basics: dialogs are *"modal UI overlays… Dialogs can
  be disruptive and should only be used in certain situations"*, plus a list of
  when to confirm versus when to offer undo. The current guidelines index files
  the Win32 pages under "Historical design guidelines… For apps you build
  today, follow the current Fluent guidance above."

**Cause**

Source age plus scope. The modern page covers *whether* to show a dialog; the
legacy page covers *how a dialog should behave* in far more detail, and current
docs have no replacement for that detail.

**Resolution**

Split by layer, which is the oracle's general legacy policy:

- **Whether/when** a dialog appears → Tier 1 wins.
- **Button semantics, commit/cancel wording, Enter/Escape, modeless behaviour**
  → Tier 3 is `STILL_VALID_INTERACTION_PRINCIPLE` and is adopted, because nothing current supersedes
  it and the rules are about interaction, not appearance.
- **Every visual aspect** of the legacy pages → VISUALLY OBSOLETE, discarded.

**Confidence** HIGH for the split; the modern index explicitly blesses reading
legacy pages for context while forbidding their visuals.

---

## C4 — A source named in the brief turned out not to be a source

**Position**

The brief lists `fluent2.microsoft.design/components/windows` as a primary
source. Fetched 2026-09-18: the page documents **no components**. It is
navigational and states *"To get the building blocks for crafting Windows
experiences, use WinUI."* No sizes, no spacing, no usage rules.

**Resolution**

Recorded in the matrix as unusable, and **no oracle rule cites it**. Component
authority is deferred to WinUI documentation and the WinUI 3 Gallery — neither
of which was verified here, so the oracle issues no control-level rules at all.
This is a gap, stated as one, rather than a set of plausible-sounding invented
defaults.

**Confidence** HIGH (direct observation).

---

## C5 — "Prefer direct manipulation" vs. keyboard-first expert work

**Positions**

- **Tier 1.** Commanding basics: *"Always try to let users manipulate content
  directly rather than through commands that act on the content, such as
  dragging and dropping to rearrange list items rather than up and down command
  buttons."*
- **Tier 2.** Cooper devotes Ch. 12 to *excise* — work the product imposes that
  does not advance the user's goal — and treats repetitive mouse work in a
  sovereign application as exactly that. Johnson Ch. 13 (Fitts' Law, Steering
  Law) quantifies why pointing costs grow with distance and precision.

**Cause**

Consumer/discoverability assumptions versus repeated-use efficiency. Direct
manipulation is the best *first* experience and often the worst *thousandth*.

**Resolution**

Both, ranked by frequency, in `UI-CMD-002` and the expert-workflow section:
direct manipulation MUST exist as the discoverable path; any operation on the
primary repeated loop MUST also have a keyboard path. Neither may be the only
one. Drag-only or mouse-only interactions on a repeated operation are treated
as excise.

**Confidence** HIGH.

---

## C6 — Legibility minimums vs. wanting more on screen

**Positions**

- **Tier 1.** Typography: *"Minimum values — 14px Semibold, 12px Regular. Text
  smaller than these sizes and weights are illegible in some languages."*
  Accessibility: text must survive `TextScaleFactor` up to **2.25**.
- **Pressure from the domain.** A dense OCR workspace invites shrinking text to
  fit more panes.

**Cause**

Not a source conflict — a source constraint colliding with a design wish.

**Resolution**

The minimums are treated as a hard floor (`UI-TYPO-002`, MUST). The Microsoft
wording — *"illegible in some languages"* — is decisive for this application in
particular, which renders Japanese: the same page assigns **Yu Gothic UI** as
the Japanese UI font, and CJK glyphs carry more strokes per em than Latin.
Density is bought with layout, not with type size.

**Confidence** HIGH.

---

## C7 — Colour as the carrier of meaning

**Positions**

- **Tier 1.** Color: *"Use color to indicate interactivity… choose one color to
  indicate elements of your application that are interactive"*; accent colour
  also signals *"the state of an interactive object or control"*. Also: ~8% of
  men and 0.5% of women are red-green colourblind, so *"avoid using these color
  combinations as the sole differentiator."*
- **Tier 2.** Johnson Ch. 4, "Our Color Vision is Limited": discriminability
  depends on presentation, and external factors (size, separation, ambient
  light) degrade it.

**Cause**

The first two Tier 1 statements are in tension with each other: one colour for
interactivity *and* accent for state means accent is doing two jobs.

**Resolution**

Colour is permitted as a **redundant** channel only (`UI-COLOR-003`). Every
state that colour expresses MUST also be expressed by at least one of: shape,
position, icon, text, weight, or border. This satisfies both Microsoft
statements without making either load-bearing alone, and it is the only reading
compatible with the colourblindness figure on the same page.

**Confidence** HIGH.

---

## C8 — A requested foundational source was unavailable — **CLOSED 2026-09-18**

**Original entry.** Norman, *The Design of Everyday Things*, was named in the
brief but absent from `docs/`. Rather than cite it from memory — which
would be fabricating provenance — the oracle attributed affordance, feedback
and mapping reasoning to the sources actually read, or marked it DERIVED, and
§5 was thinner on conceptual vocabulary than the brief envisaged.

**Resolution.** The book was added and read (revised edition, 369 pp.;
Chs. 1, 2 and 5 in detail). The oracle was revised rather than merely
annotated:

- `UI-GLOBAL-005` … `UI-GLOBAL-009` added, quoting the seven fundamental
  design principles (Ch. 2, pp. 72–73) and the affordance/signifier
  distinction (Ch. 1, pp. 13–14).
- `UI-ERR-002` re-grounded: the slip/mistake taxonomy originates with Norman
  (Ch. 5, pp. 189–204), with Johnson applying it to interfaces. Confidence
  raised MEDIUM → HIGH now that two sources support it.
- `UI-ERR-003` re-grounded on *"Human Error? No, Bad Design"* (Ch. 5), which
  states the general case that Johnson states for recognition specifically.

**No rule was contradicted by the addition** — which is the useful outcome to
record. The DERIVED rules written in Norman's absence turned out to be
consistent with him; several are now SOURCE rules instead, and the reasoning
that stood in for him has been replaced by the citation.

**Confidence** HIGH (direct observation, both before and after).

---

## C9 — Progressive disclosure vs. simultaneous expert context

**Positions**

- **Tidwell, Ch. 4, Collapsible Panels:** hide noncritical supporting modules
  and return their space to primary content; this reduces clutter.
- **Tidwell, Ch. 9, Data Brushing; Johnson, Ch. 7:** simultaneous linked views
  reveal the same data in different contexts and avoid moving status into
  fragile working memory.
- **Cooper, Ch. 9:** a sovereign application can spend more pixels on persistent
  tools and supporting information than a transient one.

**Cause**

Task simultaneity and frequency. Progressive disclosure helps when information
is optional or sequential. It hurts when comparison across representations is
the task itself.

**Resolution**

Keep primary comparison context simultaneously visible; make genuinely optional
inspectors/panes collapsible and persist the user's choice. Do not hide repeated
commands or source evidence merely to achieve a sparse appearance. Applied by
`UI-ARCH-003`, `UI-LAY-001`, `UI-SEL-003` and `UI-OCR-002`.

**Confidence** HIGH for the conditional split; no source supplies exact pane
defaults.

---

## C10 — One coherent window vs. Many Workspaces

**Positions**

- **Cooper, Ch. 18, book pp. 439–444:** several top-level windows on a small
  screen are not a good general solution, though they have important occasional
  uses; unmanaged windows create overhead.
- **Tidwell, Ch. 2, book pp. 80–83:** visual editors commonly provide Many
  Workspaces so documents or states can be used in parallel.

**Cause**

One tightly coupled task versus deliberate parallel work; small screen versus
multi-monitor; incidental popups versus user-owned document/workspace windows.

**Resolution**

`UI-ARCH-004` defaults one task/document to a pane-capable sovereign window and
permits deliberate multi-document, comparison or multi-monitor windows. Routine
commands do not spawn windows merely to arrange controls.

**Confidence** MEDIUM. Current WinUI multi-window and accessibility mechanics
remain unverified.

---

## C11 — Avoid modes vs. use modes to reduce controls and gestures

**Positions**

- **Johnson, Ch. 7, book pp. 114–115:** modes can provide more functions with
  fewer controls/gestures, but burden memory and cause mode errors when feedback
  is weak.
- **Johnson, Ch. 15, book pp. 267–269:** avoid modes where appropriate, while
  warning that separate controls can increase description slips; otherwise use
  strong status feedback, reversion and spring-loading.
- **Cooper, Ch. 18, book pp. 494–496:** small modal toolsets can work, while
  large sets create switching excise for intermediate users.

**Cause**

Control/gesture economy versus hidden state, plus working-set size and user
frequency.

**Resolution**

The oracle neither mandates nor bans OCR modes. If the architecture uses them,
`UI-MODE-001` … `003` require visible status, explicit entry/exit and preference
for spring-loaded or bounded exceptional modes. Test the alternative for
description slips rather than manufacturing a compromise by adding controls.

**Confidence** HIGH.

---

## C12 — Spinner until ten seconds vs. progress after a few seconds

**Positions**

- **Oracle 1.0.0 synthesis:** `UI-FB-003` used the 6–30 s unit-task range and a
  ~10 s review threshold for determinate progress.
- **Johnson, Ch. 14, book pp. 248–252:** acknowledge by about 0.1 s; communicate
  continued work by about 1 s; use progress for operations longer than a few
  seconds. The 10 s value describes attention without refresh, not the initial
  progress threshold.

**Cause**

The earlier synthesis collapsed distinct timing contexts from one chapter.
This is an oracle defect, not a disagreement between sources.

**Resolution**

2.0.0 corrects `UI-FB-003` and AP-16: progress/remaining work begins after a few
seconds when estimable; a spinner is for genuinely indeterminate brief work.
The 10 s value remains explanatory evidence about context reconstruction.

**Confidence** HIGH (direct correction against the local EPUB).

## C13 — "Put the most important information at the end" vs. "lead with it"

**Positions**

- **Tier 2, `CLIG` Errors:** *"Consider where the user will look first. Put
  the most important information at the end of the output."*
- **Tier 1, `MS-WRITING`:** *"Lead with what's important … always present
  the core of an idea before you add onto it."* **Tier 2, `GOVUK-WG`:** *"Put
  the most important information first"*, the inverted pyramid. **Tier 3,
  `WIN7-TEXT` UI Text:** the same inverted pyramid, and a measured scan order
  in which static text is read last if at all.

**Cause of the difference**

The medium. Terminal output scrolls upward and the prompt returns at the
bottom, so the last line is the one nearest the cursor and the one the eye
lands on. A dialog does not scroll and the eye enters at the top left. Both
sources are right about where their reader looks first.

**Resolution**

The module takes the GUI position for every surface it covers. `CLIG`'s
rule is recorded here so a reviewer who knows it does not apply it to a
dialog, and so a project with a terminal surface knows it exists. `UI-TEXT-001`
orders a message *happened / means / do* from the top.

**Confidence** HIGH. `CLIG` states its own scope ("if you are creating a GUI
program, this guide is not for you").

---

## C14 — "Never say please or sorry" vs. "say them when it costs the operator"

**Positions**

- **Tier 2, `GOVUK-DS` Error message:** do not use *"please"* "because it
  implies a choice"; do not use *"sorry"* "because it does not help fix the
  problem". `GOVUK-WG`: "there's usually no need to say 'please'".
- **Tier 3, `WIN7-TEXT` Style and Tone / Error Messages:** "limit please to
  situations that inconvenience the user in some way" — waiting, repeating a
  task; "use sorry only in error messages that result in serious problems for
  the user (for example, data loss)". **Tier 1, `MS-WRITING`** carries the
  same apologetic register in its own example: *"But don't worry — your
  picture will be waiting"*.
- And **`GOVUK-DS` itself**, on its "there is a problem with the service" and
  "service unavailable" pages: the mandated H1 is *"Sorry, there is a problem
  with the service"* — the case where the service, not the person, has
  failed. The pattern's own research list includes "if people expect to see
  please and sorry" as an open question.

**Cause of the difference**

Scope. GOV.UK's error-message rule is about **validation** — the person typed
something the form will not take — and there an apology is misplaced and a
"please" implies the field is optional. Win32's rule is about **every**
message, and it reserves both words for the one case GOV.UK also uses
"sorry": the software has cost the person something.

**Resolution**

`UI-TEXT-004`: neither word by default; *please* only where the operator is
asked to bear an inconvenience the software caused; *sorry* only where they
have lost something. Never as softening. This is consistent with every
source's practice, including GOV.UK's.

**Confidence** HIGH. The positions reconcile once the scope of each is read.

---

## C15 — "Active voice" vs. "passive to avoid blame"

**Positions**

- **Every source:** active voice. `MS-WRITING`: "throughout your app".
  `GOVUK-WG`: "the active voice is more direct". `MS-STYLE` Verbs: "keep it
  active whenever you can". `WIN7-TEXT` Style and Tone: "use the active voice".
- **Every Microsoft source, in the same breath:** the passive when the user
  is the subject of a mistake. `MS-STYLE` Verbs lists it first among the
  passive's uses: "avoiding condescending text or blaming the customer,
  especially in errors, warnings, or notifications". `WIN7-TEXT`: "use the
  passive voice when the user is the subject and might feel blamed for the
  error if the active voice were used". GOV.UK does not name the passive but
  bans *"you forgot"* and requires "positive language", which lands in the
  same place.

**Cause of the difference**

Not a conflict but a precedence question, and the sources do not say which
rule wins when both apply. Left unstated, a reviewer can fail a blame-free
passive sentence under the active-voice rule.

**Resolution**

`UI-TEXT-003` (no blame) takes precedence over `UI-TEXT-007` (active voice),
and `UI-TEXT-007` says so in its text. Instructions are active and
imperative; the statement of what went wrong is whichever voice does not
make the operator its subject.

**Confidence** HIGH. The Microsoft sources state the exception explicitly;
the resolution only orders them.

---
