# Domain module: OCR and text recognition

**Module ID:** `ocr`
**Requires:** UI Oracle core >= 1.0.0
**Status:** stable
**Opt in:** list `ocr` under `modules` in your project profile.

Every rule in this module is **DERIVED** or **PROJECT CONVENTION**. No source
in the core matrix discusses OCR interfaces; these transfer general principles
to the domain, and the reasoning is shown so it can be challenged.

Rule IDs in this module use the `UI-OCR-` prefix, reserved for it by the core
(see `UI_ORACLE_CONTRACT.md`, namespace table).

---

The object chain this module is about:

```
IMAGE → OCR REGION → RECOGNIZED TEXT → TOKEN → DICTIONARY ENTRY
                                     → READING / MEANING / TRANSLATION
                                     → ANNOTATION
```

Most of the module concerns keeping the correspondence between those objects
visible, because the user's real task is comparing one against another.

### UI-OCR-001 — Correspondence must be perceptual, not inferred
**Level:** SHOULD **Authority:** Tier 2 (derived) **Confidence:** MEDIUM
**Provenance:** DERIVED RULE

Where two representations of the same object are visible, their correspondence
SHOULD be shown by a perceptual cue — linked highlight, shared colour plus a
second channel, or spatial adjacency.

**Rationale.** Gestalt similarity and common fate (Johnson Ch. 2) make the link
free to perceive. Otherwise the user maintains the mapping in working memory,
which Ch. 7 says is small and fragile.

**Review test.** Select a region. Is the corresponding text marked, and vice
versa, without further action?

---

### UI-OCR-002 — Correct next to the evidence
**Level:** SHOULD **Authority:** Tier 2 (derived) **Confidence:** MEDIUM
**Provenance:** DERIVED RULE

Correcting recognised text SHOULD happen with the source image region visible,
ideally adjacent.

**Rationale.** `UI-ARCH-003` plus Fitts (Johnson Ch. 13): correction is a
compare-and-type loop, and separating the comparison from the typing adds both
memory load and travel.

**Review test.** During correction, are the pixels and the text both visible
without scrolling?

---

### UI-OCR-003 — Confidence is information, not decoration
**Level:** SHOULD **Authority:** Tier 2 (derived) **Confidence:** LOW
**Provenance:** DERIVED RULE

Where recognition confidence is shown, it SHOULD be encoded so that low
confidence is *findable* — not colour alone (`UI-COLOR-003`), and not so
prominent that it competes with the text.

**Rationale.** The user's task is finding what needs fixing: a scanning task
(Johnson Chs. 3, 5). LOW confidence because no source addresses confidence
display and the right encoding depends on measurement.

**Review test.** Can a user locate the least reliable text in one scan? In
greyscale?

---

### UI-OCR-004 — Recognition is a proposal
**Level:** MUST **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** DERIVED RULE (from a directly analogous source statement)

Recognised text MUST be presented as editable output, and a misrecognition MUST
NOT be framed as user error.

**Rationale.** Johnson Ch. 15 states the analogous case outright for speech:
*"Voice-Recognition Failure and Misrecognition are Not User Errors."*

**Review test.** What does the UI say when recognition is poor? Who does the
wording blame?

---

### UI-OCR-005 — Lookup must not cost the reading context
**Level:** SHOULD **Authority:** Tier 2 (derived) **Confidence:** MEDIUM
**Provenance:** DERIVED RULE

Looking up a token SHOULD NOT hide the line it came from, move it, or discard
the selection.

**Rationale.** The unit task is reading a line (Johnson Ch. 14: 6–30 s);
occluding the line restarts it. Compare `UI-SEL-002`, `UI-LAY-005`.

**Review test.** Look up a word mid-line. Is the line still visible and the
position kept?

---

### UI-OCR-006 — Learning state is durable and visible where words appear
**Status:** RETIRED in 1.0.0 — relocated, not withdrawn.

This was a PROJECT CONVENTION about a learning tool's progress display: no
source required it, and "learning state" is not a concept the OCR domain has.
A shared module is the wrong home for one product's idea of what it is for.

**Moved to** the adopting project's profile, under that project's own prefix.
A project that wants it defines it under its own prefix in `UI_PROFILE.md`,
unchanged in substance.

The ID is tombstoned rather than deleted, and is never reused
(`UI_ORACLE_CONTRACT.md` §3): reports written before 1.0.0 may cite it, and a
dangling ID is worse than a dead one.

---
