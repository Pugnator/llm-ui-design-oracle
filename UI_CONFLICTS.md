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
(`ms.date` 2021-06-24, updated 2026-07-14):

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
  → Tier 3 is STILL RELEVANT and is adopted, because nothing current supersedes
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
brief but absent from `docs/books/`. Rather than cite it from memory — which
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
