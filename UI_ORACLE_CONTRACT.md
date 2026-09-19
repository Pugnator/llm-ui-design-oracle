# UI Oracle — Contract

Terms under which a project adopts this oracle, and under which the oracle may
change. The point of the contract is that a rule ID means the same thing in
every project that cites it, and that "we follow the oracle" is a checkable
claim rather than a sentiment.

**Contract version:** 1.0.0 — see `VERSION` for the oracle version in this
copy.

---

## 1. What is being contracted

The **core** — project-neutral, identical in every adopting project:

```
UI_ORACLE.md            the rules
UI_SOURCE_MATRIX.md     source inventory, authority and limits
UI_EVIDENCE.md          question-level evidence and rule audit
UI_RESEARCH_GAPS.md     resolved and open research gaps
UI_CONFLICTS.md         source disagreements and their resolutions
UI_ANTIPATTERNS.md      review catalogue
UI_REVIEW_CHECKLIST.md  the review form
UI_ORACLE_CONTRACT.md   this file
VERSION                 the semantic version of the core
modules/<id>.md         optional domain modules
```

The **profile** — written by the adopting project, never shared:

```
UI_PROFILE.md           this project's bindings, conventions and derogations
```

A project that has a profile and an unmodified core is **conformant**. A
project that edits the core is **forked**, and loses the contract.

---

## 2. Versioning

Semantic, and the rules are the public surface.

| Change | Bump |
|---|---|
| A new rule; a SHOULD tightened to MUST; a new module | **MAJOR** |
| A rule's rationale, sources, review test or confidence strengthened; new anti-pattern; new conflict recorded | **MINOR** |
| Typography, formatting, broken-link repair | **PATCH** |

Adding a rule is MAJOR because a conformant project may now fail a review it
previously passed. That is the whole point of the version number: a project
pins a version, and upgrades deliberately.

Removing or weakening a rule is also MAJOR, and additionally requires a
tombstone (§3).

**Pinning.** A profile states the core version it was written against. A
review MUST report the version it used.

---

## 3. Rule ID stability

1. A rule ID is permanent. It is never reused for a different rule.
2. A retired rule is **tombstoned**, not deleted — the heading stays with
   `**Status:** RETIRED in x.y.z`, the reason, and a pointer to whatever
   replaced it. External review reports cite IDs; a dangling ID is worse than
   a dead one.
3. Renumbering is forbidden. Gaps in a sequence are normal and carry no
   meaning.
4. A rule's *level* may change only with a MAJOR bump, and the change is
   recorded in the rule body, not silently.

---

## 4. Namespaces

So that two projects can extend the oracle without colliding.

| Prefix | Owner | May contain |
|---|---|---|
| `UI-GLOBAL-`, `UI-ARCH-`, `UI-NAV-`, `UI-LAY-`, `UI-CMD-`, `UI-SEL-`, `UI-EDIT-`, `UI-KBD-`, `UI-MOUSE-`, `UI-FB-`, `UI-DLG-`, `UI-ERR-`, `UI-TYPO-`, `UI-ICON-`, `UI-COLOR-`, `UI-A11Y-`, `UI-MODE-`, `UI-EXP-` | **Core only** | Project-neutral rules |
| `UI-OCR-` | Module `ocr` | Domain rules |
| `UI-TEXT-` | Module `writing` | The words on the screen: messages, labels, buttons, status text |
| `AP-` | Core anti-patterns | — |
| `<PROJECT>-` e.g. `KL-` | The adopting project | Project conventions, in the profile |

A project MUST NOT define rules under a core prefix. Project rules live in the
profile under the project's own prefix, and may reference core rules freely.

Claim a new module prefix by adding a row to this table in the same change
that adds the module.

---

## 5. Derogations

A project may need to not follow a rule. That is permitted, and it is not
permitted to be silent.

A **derogation** is recorded in the profile with:

1. the rule ID;
2. what is done instead;
3. why — a reason specific to this project, not a general disagreement;
4. an expiry or a review trigger ("revisit when the editor is rewritten");
5. who decided.

Rules:

- A **MUST** may be derogated only for a stated platform or product
  constraint, never for taste or schedule. Accessibility MUSTs
  (`UI-A11Y-*`, `UI-COLOR-001`) may not be derogated at all — a project that
  cannot meet them is non-conformant and should say so.
- A **SHOULD** may be derogated with a recorded reason.
- A derogation is scoped to named surfaces, never blanket.
- A review reports derogated rules as **DEROGATED**, not PASS. They stay
  visible.

Disagreeing with a rule in general is not a derogation — it is a change
request against the core (§7).

---

## 6. Conformance levels

A profile declares one:

| Level | Meaning |
|---|---|
| **Full** | All core MUSTs met or derogated; SHOULDs met or derogated; modules declared |
| **Core** | All core MUSTs met or derogated; SHOULDs unaudited |
| **Accessibility-only** | `UI-A11Y-*`, `UI-COLOR-001`, `UI-KBD-*` met; rest unaudited |
| **Adopting** | The oracle is in use but the project has not been audited yet |

"Adopting" is an honest starting state and most projects begin there. Claiming
"Full" without a completed checklist run is a false claim, and the checklist
exists so the claim can be checked.

---

## 7. Changing the core

The core changes when a **source** says something new — not when a project
wants different behaviour. That is the difference between an oracle and a
style guide.

A change request carries:

- the rule affected (or "new rule");
- the source, with edition/version/date and the passage;
- which tier it belongs to;
- whether it conflicts with an existing rule, and the proposed resolution for
  `UI_CONFLICTS.md`;
- the version bump implied by §2.

Two constraints, inherited from how the oracle was built:

1. **No citation may be added that was not read.** The matrix records
   verification status per source; a citation from memory is a defect, not a
   shortcut.
2. **No numeric value may be added without a source.** If a number is needed
   and no source gives it, the gap is recorded in the matrix instead. The
   matrix's "known gaps" list is a feature.

---

## 8. Propagating the core between projects

The core is copied, not linked, because a design contract that changes under a
project without warning is not a contract.

To adopt: copy the core files and `modules/` you need, copy
`UI_PROFILE.template.md` to `UI_PROFILE.md`, fill it in, record the version.

To upgrade: replace the core files, read the diff of `VERSION` and the rule
list, and re-run the checklist for any rule that changed level. The profile is
never overwritten.

To contribute back: make the change in one project's copy, then propagate the
identical core to the others. Cores that have drifted are forks; `VERSION`
plus a file hash tells you which.

---

## 9. What a review must report

So that a review from one project is legible in another:

```
Oracle version : <from VERSION>
Modules        : <ids, or none>
Profile        : <project> <profile version>
Conformance    : <declared level>
Result         : n PASS, n FAIL, n N/A, n NEEDS HUMAN JUDGMENT, n DEROGATED
```

Each finding cites a rule ID and its class — **platform requirement** (Tier 1),
**interaction principle** (Tier 2/3/4), or **project convention** (profile).
Those carry different weight in an argument, and collapsing them is how design
review turns into opinion.
