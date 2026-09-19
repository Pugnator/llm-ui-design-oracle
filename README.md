# UI Oracle

A rule set for Windows desktop and command-line software that an LLM can
apply and cite. Every rule says what to do, who says so, and how to test it.

**Version 5.0.0.** 198 active rules, 39 anti-patterns, 21 recorded source
conflicts. Licensed [WTFPL](LICENSE). Nothing here is hot-linked: every page a
rule quotes is archived under `corpus/`, and all 587 quotations are checked by
a tool that ships with it.

It is not a style guide. It contains no brand, no palette, no spacing scale.
Those belong to a project, in its own profile.

---

## Do one of these three things

### Review a UI

Give the model `UI_ORACLE.md`, `UI_ANTIPATTERNS.md`, `UI_REVIEW_CHECKLIST.md`,
your `UI_PROFILE.md`, and the thing being reviewed. Then:

> Review this against the UI Oracle. Work through `UI_REVIEW_CHECKLIST.md` in
> order. Cite a rule ID for every finding and give its class: platform
> requirement, interaction principle, or project convention. If no rule
> applies, say so — do not invent one. Report in the format at the end of
> `UI_ORACLE_CONTRACT.md` §9.

### Write or review the words on screen

Give the model `UX_WRITING_ORACLE.md`, `ERROR_MESSAGE_ORACLE.md`,
`TERMINOLOGY.md` and `UI_COPY_REVIEW_CHECKLIST.md`. Then:

> Follow the ten-step procedure in `UI_COPY_REVIEW_CHECKLIST.md` Part 1
> before writing anything. Then check the result against Part 2. Cite rule
> IDs. Do not keep a sentence because it is true.

Before trusting a reviewer, run it against the twelve strings in Part 4. Each
is accurate, grammatical and helpful-sounding, and each must be rejected. A
reviewer that passes any of them has not applied the oracle.

### Check a command-line program

```
python tools/cli_check.py --config myproject.cli_check.json -- mytool
```

Most `cli` rules are decided by this, not by reading. It exits non-zero on any
FAIL, so it drops into CI unchanged.

---

## What to load

Context is finite. Load the set for the task, not the repository.

| Task | Load | Size |
|---|---|---|
| Review a UI | `UI_ORACLE.md`, `UI_ANTIPATTERNS.md`, `UI_REVIEW_CHECKLIST.md`, enabled `modules/*.md`, your profile | ~34k tokens |
| Write or review text | `UX_WRITING_ORACLE.md`, `ERROR_MESSAGE_ORACLE.md`, `TERMINOLOGY.md`, `UI_COPY_REVIEW_CHECKLIST.md` | ~28k tokens |
| Dispute a rule, or propose one | add `UI_CONFLICTS.md`, `UI_EVIDENCE.md`, `UX_COPY_EVIDENCE.md`, `UI_SOURCE_MATRIX.md`, `UI_RESEARCH_GAPS.md` | ~39k tokens |
| Adopt, version or derogate | `UI_ORACLE_CONTRACT.md` | ~3k tokens |

`corpus/` is the evidence behind the citations. It is not needed at review
time and should not be loaded then.

---

## Adopt it in a project

1. Add the repository read-only:

   ```
   git submodule add git@github.com:Pugnator/llm-ui-design-oracle.git docs/ui/oracle
   ```

   The submodule pin is your version pin. Upgrading is `git -C docs/ui/oracle
   pull` plus a commit of the new pin — a deliberate act with a diff.

2. Copy `UI_PROFILE.template.md` to `docs/ui/UI_PROFILE.md`, **outside** the
   submodule, and fill in at minimum:

   - the binding table, including the core version you are writing against;
   - the platform table, including the UI toolkit and the scripts you render;
   - the **posture map**, which cannot be skipped. Nearly every layout, icon
     and density rule branches on whether a surface is sovereign or transient,
     and a surface missing from the map cannot be reviewed.

3. Enable the modules you need (below). Fill in `TERMINOLOGY.md` Part 2 with
   your own vocabulary before writing any product text.

4. Declare a conformance level. `Adopting` is the honest place to start.

5. Run the checklists when you are ready to claim more.

Never edit files inside the submodule. Core files are byte-identical across
adopting projects, and that is what makes a rule ID portable. A project that
edits the core has forked and left the contract.

---

## Modules

Enable a module by listing it under `modules` in your profile.

| Module | Rules | Enable it when |
|---|---|---|
| `writing` | 15 `UI-TEXT-` | The product shows words. In practice, always |
| `imgui` | 21 `UI-IMGUI-` | The UI toolkit is Dear ImGui |
| `cli` | 24 `UI-CLI-` | The product has a command-line surface |
| `ocr` | 5 `UI-OCR-` | The product recognises text in images |

Two need a word of warning.

**`imgui`** states that the toolkit cannot implement three accessibility
rules, because Dear ImGui has no accessibility tree and says so itself. A
review reports those as `N/A (TOOLKIT)`, never PASS, and the profile lists
them under known non-conformance. The declared conformance level then carries
`(toolkit-limited)`. This is not a loophole: everything the toolkit *can* do —
keyboard navigation, a text scale, a tooltip on every icon — is still required
in full.

**`cli`** is stricter than the rest of the oracle and nearly every rule is a
MUST, because a command line is a contract with other programs as much as an
interface for people. A project claiming conformance with `cli` enabled needs
a clean `cli_check` run on record in its profile.

---

## The tools

### `tools/cli_check.py`

Runs the `cli` module against a real binary. Standard library only, Windows
and POSIX.

```
python tools/cli_check.py -- mytool                         # generic battery
python tools/cli_check.py --config mytool.json -- mytool    # adds config-driven checks
python tools/cli_check.py --json -- mytool | jq .summary    # machine-readable
python tools/cli_check.py --write-baseline base.json -- mytool
python tools/cli_check.py --baseline base.json -- mytool    # fails on a removed flag
```

| Exit | Meaning |
|---|---|
| 0 | No FAIL findings |
| 1 | One or more FAIL |
| 2 | Usage or config problem |
| 3 | The command was not found |

Start from `tools/cli_check.example.json`. The config tells the checker which
commands are destructive, which are long-running, which list data, and which
failures should map to which exit codes. Without it, 22 of the 24 rules still
get checked; with it, all of them do.

### `tools/verify_quotes.py`

Checks that every quotation in every document appears in the archived source
text.

```
python tools/verify_quotes.py
ORACLE_SCRATCH=/path/to/books python tools/verify_quotes.py   # also check books
```

Run it after any edit that touches a quotation. Exit 0 means every quotation
is accounted for. This is not decoration: writing 5.0.0 found fabricated
quotations, two of them inherited from an earlier release. The recurring
failure is merging a heading with its following sentence, or a table's two
cells, or a bulleted list, into one quoted phrase — which reads as faithful
and is not.

### `tools/make_figures.py`

Regenerates `img/*.svg`. Run from the repository root.

---

## How to read a rule

Every rule carries the same fields, and a review must report two of them.

| Field | What it tells you |
|---|---|
| **Level** | MUST / MUST NOT — violation is a defect. SHOULD — violation needs a recorded reason. MAY — permitted |
| **Authority** | Tier 1 current platform, Tier 2 interaction-design literature, Tier 3 legacy Windows, Tier 4 foundational theory, Tier 1 (toolkit) |
| **Confidence** | HIGH, MEDIUM, LOW. A LOW-confidence rule is never a MUST |
| **Provenance / Class** | Where the rule came from: source, derived, or project convention |
| **Review test** | The question that decides it |

Report the **class** with every finding — platform requirement, interaction
principle, content-design principle, derived rule, or project convention.
Those carry different weight when someone pushes back, and a review that
presents them identically is not usable.

Two failure modes to watch for in generated reviews:

- **Invented rules.** If no rule applies, the answer is "no rule applies".
- **Flattened authority.** A Tier 1 platform requirement and a project
  convention are not the same kind of finding.

---

## Change it

The core changes when a **source** says something new, not when a project
wants different behaviour. That is the difference between an oracle and a
style guide. A change request carries the rule affected, the source with its
edition and date, the tier, any conflict it creates, and the version bump
implied (`UI_ORACLE_CONTRACT.md` §7).

Two hard rules:

- **No citation may be added that was not read.** Enforced by
  `tools/verify_quotes.py`.
- **No numeric value may be added without a source.** If a number is needed
  and none exists, record the gap. `UI_SOURCE_MATRIX.md` keeps that list, and
  the list is a feature.

To not follow a rule, record a derogation in your profile: the rule ID, what
you do instead, why, an expiry or review trigger, and who decided. A MUST may
be derogated only for a stated platform or product constraint. Accessibility
MUSTs may not be derogated at all — a project that cannot meet them is
non-conformant and should say so.

---

## What it does not cover

Stated so that the silence is not mistaken for an oversight.

- **No spacing scale, control sizes, corner radii, target sizes, motion
  durations or non-text contrast ratio.** No source supplied them. Do not
  infer them from this document's silence.
- **Apple, Material and Android.** All three serve their guidance only through
  JavaScript and could not be read. No rule cites them.
- **A general length ceiling for a dialog.** Unsourced. The project budgets in
  `UX-TEXT-014` are labelled as local policy, not as anyone's requirement.
- **Windows console specifics.** Virtual-terminal sequences, PowerShell
  conventions and the per-user configuration path are unverified.
- **Localisation.** Real, and out of scope.

---

## Files

| Path | What it is | Edited by |
|---|---|---|
| `UI_ORACLE.md` | 81 core rules, plus Appendix A (source digest) | Core |
| `UX_WRITING_ORACLE.md` | 29 rules for every user-visible string; anti-patterns of generated text | Core |
| `ERROR_MESSAGE_ORACLE.md` | 23 rules: whether to report a condition, its severity, surface and five layers | Core |
| `modules/*.md` | `writing`, `imgui`, `cli`, `ocr` | Core |
| `UI_REVIEW_CHECKLIST.md` | The UI review form | Core |
| `UI_COPY_REVIEW_CHECKLIST.md` | The copy procedure, review form and calibration strings | Core |
| `TERMINOLOGY.md` | Controlled vocabulary. Part 1 general, **Part 2 yours** | Part 2 |
| `UI_ORACLE_CONTRACT.md` | Versioning, ID stability, namespaces, derogations, conformance | Core |
| `UI_ANTIPATTERNS.md` | 39 anti-patterns, each with the condition that makes it harmful | Core |
| `UI_CONFLICTS.md` | 21 places the sources disagree, and how each was resolved | Core |
| `UI_EVIDENCE.md`, `UX_COPY_EVIDENCE.md` | What the sources say, before any rule was written | Core |
| `UI_SOURCE_MATRIX.md` | Every source, its date, its authority, its limits, and the gaps | Core |
| `UI_RESEARCH_GAPS.md` | Resolved and open research questions | Core |
| `corpus/` | The archived text of every source read: 94 files | Core |
| `tools/` | `cli_check.py`, `verify_quotes.py`, `make_figures.py` | Core |
| `UI_PROFILE.template.md` | Copy it to start | Copy |
| `UI_PROFILE.md` | **Your** bindings, conventions, derogations | You |

---

## A note on this file

The writing oracle governs product text, not documentation — a distinction the
sources themselves draw, and one recorded as conflict `C21`. Google asks
documentation to sound like a knowledgeable friend and its error-message
course to do nothing of the kind.

So this README applies the transferable rules and not the per-surface
ceilings: lead with what the reader came for, name the specific command rather
than describe it, one term per concept, no padding and no reassurance, and
every sentence earns its place or goes. If you find one that does not, it is a
defect — the same defect the oracle exists to catch.

See `NOTICE.md` for third-party material and the licence position.
