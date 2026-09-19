# UI Oracle — portable design contract

A versioned, self-contained rule set for **Windows desktop application UI**,
written to be shared between projects and cited by rule ID. The core names no
toolkit; the `imgui` module binds it to **Dear ImGui**, and the `cli` module
extends it to **command-line programs**.

**Version 5.0.0** (`VERSION`). 81 core rules; four modules — `ocr` (5 active
rules plus 1 retired ID), `writing` (15), `imgui` (21), `cli` (24); a writing
oracle of 52 rules for user-visible text; and 39 anti-patterns. Licensed
[WTFPL](LICENSE).

Two parts of it check themselves. The `cli` module is **automated**: most of
its rules are decided by `tools/cli_check.py` running against a real binary,
and a clean run is what the contract accepts as evidence. And every
quotation in the repository — 587 of them — is verified against the archived
source text by `tools/verify_quotes.py`.

---

## Why this exists

So that "does this UI make sense?" has an answer that is checkable, traceable
and the same next month. A review here cites a rule; the rule cites its
authority; the authority is ranked. Disagreement becomes a conversation about
which rule or which tier, not about taste.

It is deliberately **not** a style guide. It contains no brand, no palette, no
spacing scale — those belong to a project, and a project records them in its
own profile.

---

## What is in the package

| File | What it is | Edited by |
|---|---|---|
| `UI_ORACLE.md` | The rules, plus Appendix A (source digest) | Core only |
| `UI_ORACLE_CONTRACT.md` | Versioning, ID stability, namespaces, derogations, toolkit limitations, conformance, adoption | Core only |
| `UI_SOURCE_MATRIX.md` | Source metadata, local paths, completeness, authority, strengths and limits | Core only |
| `UI_RESEARCH_GAPS.md` | Resolved/open research gaps and final audit | Core only |
| `UI_EVIDENCE.md` | Question-level source evidence and rule verification ledger | Core only |
| `UI_CONFLICTS.md` | Where sources disagree and how it was resolved | Core only |
| `UI_ANTIPATTERNS.md` | Review catalogue, each with the condition that makes it harmful | Core only |
| `UI_REVIEW_CHECKLIST.md` | The review form | Core only |
| `modules/<id>.md` | Optional modules — `ocr`, `writing`, `imgui`, `cli` | Core only |
| `UX_WRITING_ORACLE.md` | Rules for every user-visible string, and the anti-patterns of generated text | Core only |
| `ERROR_MESSAGE_ORACLE.md` | Whether a condition is reported at all, its severity, surface and five information layers | Core only |
| `UX_COPY_EVIDENCE.md` | The evidence layer behind both | Core only |
| `UI_COPY_REVIEW_CHECKLIST.md` | The copy generation and review procedure | Core only |
| `TERMINOLOGY.md` | Controlled vocabulary — Part 1 general, Part 2 **the project's** | Part 2 |
| `corpus/platform/` | Archived text of the Microsoft pages the core quotes, with URL, `ms.date`, fetch date and licence | Core only |
| `corpus/writing/` | Archived text of the writing sources (GOV.UK, Microsoft, Win32 UX Guide, clig.dev) | Core only |
| `corpus/imgui/` | Archived Dear ImGui documentation and public header, with version | Core only |
| `corpus/cli/` | Archived GNU Coding Standards chapter 4; hashes of the sources whose licence forbids archiving | Core only |
| `tools/cli_check.py` | The `cli` module's checker: runs a binary and reports findings | Core only |
| `img/*.svg` | Figures, generated locally, theme-aware | Core only |
| `VERSION` | Semantic version of the core | Core only |
| `UI_PROFILE.template.md` | Starting point for an adopting project | Copy it |
| `UI_PROFILE.md` | **Your** bindings, conventions, derogations | **The project** |

Core files are byte-identical across adopting projects. That is what makes a
rule ID portable. A project that edits the core has forked and left the
contract.

---

## Adopting it in another project

1. Copy the core files and any `modules/` you want.
2. `cp UI_PROFILE.template.md UI_PROFILE.md` and fill it in — at minimum the
   binding table, the platform table, and the **posture map**.
3. Declare a conformance level. `Adopting` is the honest place to start.
4. Run `UI_REVIEW_CHECKLIST.md` when you are ready to claim more.

The posture map is the part that cannot be skipped: nearly every layout, icon
and density rule branches on whether a surface is sovereign or transient, and
a surface missing from the map cannot be reviewed. A command-line surface is
classified `cli` and reviewed under the `cli` module, whose first question is
different: is the output read by a person at a terminal, or by a program?

**Dear ImGui projects** enable the `imgui` module and name the branch and
version in the profile. The module's applicability table says which core
rules the toolkit cannot implement (three, all accessibility) and how a
review reports them — `N/A (TOOLKIT)`, never PASS — and restates the rules
the toolkit meets in a different form.

**Command-line projects** enable the `cli` module, which is stricter than the
rest of the oracle because a command line is a contract with other programs
as much as an interface for people, and because the conventions are old,
written down and mechanically checkable. Nearly every rule is a MUST, and
each names the check that decides it:

```
python tools/cli_check.py --config myproject.cli_check.json -- mytool
```

The checker reports one finding per check in the contract's format and exits
non-zero on any FAIL, so it drops into CI unchanged. A project claiming
conformance with `cli` enabled must have a clean run on record in its profile
(`UI_ORACLE_CONTRACT.md` §6). Start from `tools/cli_check.example.json`; the
checker follows the module itself and is checked with it.

---

## Using it in a review

Give an LLM the core, the profile, and the thing being reviewed. Ask for
findings in the format at the end of `UI_ORACLE_CONTRACT.md` §9. A good
finding names the rule, the evidence, and whether it is a **platform
requirement**, an **interaction principle**, or a **project convention** —
because those carry different weight when someone pushes back.

**What to load.** For a review: `UI_ORACLE.md`, `UI_ANTIPATTERNS.md`,
`UI_REVIEW_CHECKLIST.md`, the enabled `modules/*.md`, and the project's
`UI_PROFILE.md`. For anything the product says in words, load instead
`UX_WRITING_ORACLE.md`, `ERROR_MESSAGE_ORACLE.md`, `TERMINOLOGY.md` and
`UI_COPY_REVIEW_CHECKLIST.md` — that last one is the procedure to follow.
Load `UI_CONFLICTS.md`, `UI_EVIDENCE.md`, `UX_COPY_EVIDENCE.md`,
`UI_SOURCE_MATRIX.md` and `UI_RESEARCH_GAPS.md` only when a rule is disputed
or a new rule is proposed. The `corpus/` directories are the evidence behind
the citations and are not needed at review time.

**Writing or reviewing text.** The copy checklist opens with a ten-step
generation procedure, because a message written first and trimmed afterwards
keeps the shape of the draft. It closes with twelve test strings that are
accurate, grammatical and helpful-sounding, and must all be rejected — use
them to check that a reviewer is calibrated.

Two failure modes worth watching for in generated reviews:

- **Invented rules.** If no rule applies, the answer is "no rule applies",
  not a plausible-sounding new one.
- **Flattened authority.** A Tier 1 platform requirement and a project
  convention are not the same kind of finding, and a review that presents
  them identically is not usable.

---

## Self-containment

The oracle does not assume you have the books or the web. Appendix A of
`UI_ORACLE.md` restates what each book contributes, in the oracle's own words.
Every web page a rule quotes — the Microsoft platform pages, the writing
guidance, the Dear ImGui documentation, clig.dev, the GNU Coding Standards —
is archived under `corpus/` with its URL, fetch date and licence, so a
citation can be checked against what was actually read rather than against a
live page that may have changed. Three command-line sources forbid
redistribution; for those the SHA-256 of the page that was read is recorded
instead, so a re-fetch can be compared. Figures are generated into `img/` as
SVG. Nothing is hot-linked.

Verbatim quotation survives only for published numeric specifications and for
statements of what a toolkit does, where paraphrase would destroy the value.

---

## Changing it

The core changes when a **source** says something new, not when a project
wants different behaviour — see `UI_ORACLE_CONTRACT.md` §7. Two hard rules
carried over from how it was built:

- No citation may be added that was not read.
- No numeric value may be added without a source. If a number is needed and
  no source gives it, record the gap instead. `UI_SOURCE_MATRIX.md` keeps a
  list of those gaps, and the list is a feature.

The first of those is enforced, not merely intended:

```
python tools/verify_quotes.py
```

It extracts every quotation in every document and looks for it in the
archived text, reporting anything it cannot find. Set `ORACLE_SCRATCH` to a
directory holding the books and the three sources whose licence forbids
archiving if you want those checked too.

To regenerate the figures: `python tools/make_figures.py` from the repository
root.

---

## Using it as a submodule

This repository is the canonical core. A project consumes it read-only:

```
git submodule add git@github.com:Pugnator/llm-ui-design-oracle.git docs/ui/oracle
```

and keeps its own `UI_PROFILE.md` *outside* the submodule — typically at
`docs/ui/UI_PROFILE.md`, beside it. The submodule pin is the project's
version pin: updating the oracle is `git -C docs/ui/oracle pull` plus a commit
of the new pin, which is a deliberate act with a diff, exactly as
`UI_ORACLE_CONTRACT.md` §2 intends.

Never edit files inside the submodule from a consuming project. That is the
fork the contract warns about, and git will make it obvious.

See `NOTICE.md` for third-party material and the licence position.
