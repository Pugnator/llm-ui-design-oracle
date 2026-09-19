# UI Profile — `<PROJECT NAME>`

Copy to `UI_PROFILE.md` and fill in. This file is the only part of the oracle
package a project edits; the core stays byte-identical so a rule ID means the
same thing everywhere (`UI_ORACLE_CONTRACT.md`).

Delete the guidance in *italics* as you go.

---

## 1. Binding

| Field | Value |
|---|---|
| Project | `<name>` |
| Oracle core version | `<from VERSION, e.g. 4.0.0>` |
| Profile version | `<your own, starts at 1.0.0>` |
| Modules enabled | `<any of ocr, writing, imgui, cli — or none>` |
| Conformance level | `Adopting` / `Core` / `Full` / `Accessibility-only` — add `(toolkit-limited)` when a module reports N/A (TOOLKIT), contract §6 |
| Last checklist run | `<date, or never>` |
| Rule prefix | `<2–3 letters, e.g. KL->` |

---

## 2. Platform

*The core assumes Windows desktop. If that is not true here, say so — many
Tier 1 rules become inapplicable and the review must know.*

| Field | Value |
|---|---|
| Target OS | |
| UI toolkit | *name, branch and version. Dear ImGui: enable the `imgui` module — it lists the core rules the toolkit cannot meet* |
| Minimum window size | |
| Theme support | `light` / `dark` / `both` |
| Primary input | |
| Scripts rendered | *matters for `UI-TYPO-002`* |

---

## 3. Posture map

*`UI-GLOBAL-001` requires every surface to be classified before it is
designed, and this is where the classification lives. A reviewer reads this
table first. Surfaces missing from it cannot be reviewed.*

| Surface | Posture | Notes |
|---|---|---|
| | `sovereign` / `transient` / `daemonic` / `cli` (module `cli`) | |

---

## 4. Project conventions

*Choices no source dictates. Use your own prefix — never a core prefix. Format
them like core rules so a review can cite them the same way.*

### <XX>-001 — <title>
*Heading format matches the core so one grep finds every rule:*
*`### <PREFIX>-<NNN> — <title>`, no backticks.*
**Level:** **Confidence:** **Provenance:** PROJECT CONVENTION

**Rule**

**Rationale** *why this project chose it*

**Review test**

---

## 5. Bindings for core rules that defer to the project

*Some core rules deliberately point at a project artifact. Name it here, or
state that the core default applies.*

| Core rule | Needs | This project |
|---|---|---|
| `UI-ERR-001` | A writing standard for on-screen text | `<path, or "core rule as written">` |
| `UX-TEXT-001` | The product's register — professional tool, or warmer | `<declared register>` |
| `UX-TEXT-016` | The declared audience for on-screen text | `<who reads this product's messages>` |
| `UX-TEXT-014` | Project copy budgets, if tighter than the sourced ceilings | `<or "oracle defaults">` |
| `UX-TEXT-017` | The controlled vocabulary | `TERMINOLOGY.md` Part 2 |
| `UX-ERR-023` | The product's debugging surface, if any | `<verbose mode, diagnostics pane, log viewer>` |
| `UI-COLOR-005` | Where semantic colour roles are defined | `<path>` |
| `UI-TYPO-007` | Font families, incl. per-script | `<fonts>` |
| `UI-ARCH-002` | Where workspace state is persisted | `<path or mechanism>` |
| `UI-EXP-003` | Undo scope | `<what is undoable>` |
| `UI-IMGUI-015` (module `imgui`) | Per-user settings path; default docking layout | `<path; ini or DockBuilder>` |
| `UI-CLI-019` (module `cli`) | Configuration file locations and precedence | `<paths>` |
| `UI-CLI-024` (module `cli`) | The `cli_check` config file, required by contract §6 | `<path to the JSON config>` |

---

## 6. Derogations

*Rules this project does not follow. Silence is not an option — an
undocumented deviation is a defect, a documented one is a decision.
`UI-A11Y-*` and `UI-COLOR-001` may not be derogated (contract §5).*

### `<RULE-ID>`
- **Instead** *what is done*
- **Why** *specific to this project, not general disagreement*
- **Scope** *named surfaces only*
- **Expires / revisit when** *date or trigger*
- **Decided by** *person, date*

---

## 7. Known non-conformance

*Things that are simply wrong and not yet fixed. Distinct from a derogation: a
derogation is a decision, this is a debt. Link issues. Rules an enabled
toolkit module reports as `N/A (TOOLKIT)` are listed here too, citing the
module (contract §5).*

| Rule | Surface | Issue | Noted |
|---|---|---|---|

---

## 8. Review log

| Date | Oracle version | Scope | Result | By |
|---|---|---|---|---|

*A project with an automated module enabled records its clean checker run
here: date, checker version, oracle version, and the config used (contract
§6).*
