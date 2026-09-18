# UI Oracle — portable design contract

A versioned, self-contained rule set for **Windows desktop application UI**,
written to be shared between projects and cited by rule ID.

**Version 2.0.0** (`VERSION`). 81 core rules, 5 active OCR module rules plus 1
retired ID, and 22 anti-patterns.

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
| `UI_ORACLE_CONTRACT.md` | Versioning, ID stability, namespaces, derogations, conformance, adoption | Core only |
| `UI_SOURCE_MATRIX.md` | Source metadata, local paths, completeness, authority, strengths and limits | Core only |
| `UI_RESEARCH_GAPS.md` | Resolved/open research gaps and final audit | Core only |
| `UI_EVIDENCE.md` | Question-level source evidence and rule verification ledger | Core only |
| `UI_CONFLICTS.md` | Where sources disagree and how it was resolved | Core only |
| `UI_ANTIPATTERNS.md` | Review catalogue, each with the condition that makes it harmful | Core only |
| `UI_REVIEW_CHECKLIST.md` | The review form | Core only |
| `modules/<id>.md` | Optional domain rules | Core only |
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
a surface missing from the map cannot be reviewed.

---

## Using it in a review

Give an LLM the core, the profile, and the thing being reviewed. Ask for
findings in the format at the end of `UI_ORACLE_CONTRACT.md` §9. A good
finding names the rule, the evidence, and whether it is a **platform
requirement**, an **interaction principle**, or a **project convention** —
because those carry different weight when someone pushes back.

Two failure modes worth watching for in generated reviews:

- **Invented rules.** If no rule applies, the answer is "no rule applies",
  not a plausible-sounding new one.
- **Flattened authority.** A Tier 1 platform requirement and a project
  convention are not the same kind of finding, and a review that presents
  them identically is not usable.

---

## Self-containment

The oracle does not assume you have the books. Appendix A of `UI_ORACLE.md`
restates what each source contributes, in the oracle's own words. Figures are
generated into `img/` as SVG — text, diffable, and legible in light and dark.
Nothing is hot-linked; nothing needs a PDF on disk.

Verbatim quotation survives only for published numeric specifications, where
paraphrase would destroy the value.

---

## Changing it

The core changes when a **source** says something new, not when a project
wants different behaviour — see `UI_ORACLE_CONTRACT.md` §7. Two hard rules
carried over from how it was built:

- No citation may be added that was not read.
- No numeric value may be added without a source. If a number is needed and
  no source gives it, record the gap instead. `UI_SOURCE_MATRIX.md` keeps a
  list of those gaps, and the list is a feature.

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
