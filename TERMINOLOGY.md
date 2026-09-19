# Terminology

A controlled vocabulary for user-visible text. One concept, one term, used in
every string.

**Requires:** UI Oracle core >= 5.0.0. Enforces `UX-TEXT-017` and
`UI-TEXT-013`.

---

## Why this file exists

Three sources require terminological consistency, and one of them names
exactly the mechanism that breaks it in generated text:

> *"Some authoring systems automatically recommend synonyms to ensure that you
> don't keep repeating the same word. Yes, variety spices up paragraphs.
> However, variety in error messages can confuse users."*
> — `GERR`, *Use terminology consistently*

> *"consistent terminology promotes learning … inconsistency forces users to
> figure out whether different words and actions mean the same thing"*
> — `WIN7-TEXT`, *Style and Tone*, with the example
> *start / run / launch / boot / execute*

Johnson gives the cost: a reader looking for Search may miss it when it is
labelled Query (`JM3` Ch. 11).

A language model is a synonym engine. Left to itself it will call the same
thing a *device*, a *unit*, a *module* and a *controller* across four
messages, each locally reasonable. A word list is the cheapest defence, and it
only works if it is **closed**: a term not in the list is not used.

---

## How to use it

**Writing.** Look up the concept. Use the preferred term exactly, including
its capitalisation. If the concept is not here, add it before writing the
string.

**Reviewing.** For each noun in the string, check the Avoid column. A hit is a
finding under `UX-TEXT-017`.

**Extending.** Add a row when a concept first appears in user-visible text.
Record the internal name too, when it differs — that column is what stops an
implementation term leaking into copy (`UX-ERR-010`).

---

## Row format

| Field | Meaning |
|---|---|
| **Preferred** | The only term that may appear in user-visible text |
| **Avoid** | Synonyms and near-misses that must not appear |
| **Capitalisation** | Sentence case unless the term is a proper noun or an established acronym |
| **Means** | What the reader should understand by it |
| **Internal** | The name used in code, if different. Never shown outside layer 4 or 5 |

---

## Part 1 — General software vocabulary

These rows are grounded in the sources this oracle read. They apply to any
product and should not be edited by a project; a project that needs a
different term records a derogation.

### Interaction verbs

Microsoft requires input-neutral verbs, and `UI-TEXT-014` already carries the
rule. The preferred forms are Microsoft's.

| Preferred | Avoid | Means |
|---|---|---|
| select | click, tap, press (for a control), choose, hit | Activate a control, by any input method |
| enter | type, key in, input (as a verb) | Put a value into a field |
| open | bring up, pull up, launch (a document) | Open a document, file or window |
| go to | navigate to, browse to | Move to a location in the product |
| turn on / turn off | enable / disable (in user-facing text), activate, deactivate | Change a setting's state |
| clear | uncheck, untick, deselect | Remove a selection or a checkbox state |
| start | run, launch, boot, execute, fire, kick off | Begin an operation |
| stop | halt, kill, terminate, abort, end | End an operation |

*Source:* `MS-STYLE` *Describing interactions with the UI*; `WIN7-TEXT`
*Style and Tone* (the *start/run/launch/boot/execute* example, and the word
list that rejects *kill*, *terminate* and *abort*); `UI-TEXT-003`,
`UI-TEXT-014`.

**Note on *enable* and *disable*.** They remain correct in developer-facing
text and in this oracle's own prose. In product text, *turn on* and *turn off*
are the reader's words.

### Problem vocabulary

| Preferred | Avoid | Means |
|---|---|---|
| problem | error, failure, fault (as a noun in copy) | Something has gone wrong |
| could not / cannot | failed to, was unable to (as a stock opener), unsuccessful | The product did not do the thing |
| incorrect | invalid, illegal, bad, wrong, malformed | The value is not one the product accepts |
| not supported | unsupported (alone), forbidden, prohibited, disallowed | The product does not handle this case |
| stopped | aborted, killed, terminated, crashed (unless it crashed) | An operation ended early |
| serious | fatal, catastrophic, critical (unless genuinely so) | High severity |

*Source:* `WIN7-TEXT` *Error Messages*, the do-not-use list with its
replacements; `GOVUK-DS` *Error message*; `NNG-ERR` (*"invalid, illegal, or
incorrect"* as blame words). `UI-TEXT-003`, `UX-TEXT-005`, `UX-TEXT-018`.

**Note.** *Error* is correct as a log level and in this oracle's own rule
names. It is not correct as the word shown to the reader, where the icon and
container already carry it.

### Product surfaces

Call each surface by one name, in text and in documentation.

| Preferred | Avoid |
|---|---|
| status bar | status line, status strip |
| tooltip | tool tip, hover text, hint |
| dialog | dialogue, dialog box (in copy), popup, modal |
| notification | toast, alert, popup |
| settings | preferences, options, config (in copy) |
| details | advanced, more info, technical info |
| log | log file, trace (in copy) |

*Source:* `W32-CTRL` *Status Bars* (*"Refer to status bars as status bars, not
status lines or other variations"*) and *Tooltips*. The remaining rows are
`UX-TEXT-017` applied consistently and are **PROJECT CONVENTION**; a project
with a house term records it here instead.

---

## Part 2 — Project vocabulary

**Empty by design.** Domain terms are not invented during source research.
A project fills this in from its own specification and its own users' words,
subject to `UX-TEXT-016`: the term the reader already uses wins, even where
the internal name differs.

Copy the table and fill it in:

```markdown
| Preferred | Avoid | Capitalisation | Means | Internal |
|---|---|---|---|---|
|  |  |  |  |  |
```

### A worked row, for shape only

This illustrates the format. It is **not** a rule of this oracle and must be
deleted or replaced by an adopting project.

| Preferred | Avoid | Capitalisation | Means | Internal |
|---|---|---|---|---|
| ECU | controller unit, engine computer, control box, the unit, module | Always uppercase; no article in labels | The vehicle control module the product communicates with | `EcuSession`, `target_node` |

The reasoning shown here is the reasoning a project should record: the term is
preferred **because the intended audience already uses it**, which is
`UX-TEXT-016` — not because it is more precise, and not because it is shorter.

### How to choose a preferred term

1. **Ask what the reader calls it.** Not what the code calls it, not what the
   specification calls it. Johnson's example is a system whose developers
   planned *categories* and *subcategories* while the teachers who would use
   it said *subject* and *unit* (`JM3` Ch. 11).
2. **Prefer the plain word** where one exists and means the same thing
   (`UI-TEXT-006`). GOV.UK's finding stands: specialists prefer plain English
   more, not less.
3. **Keep a term of art** when the audience uses it daily. Replacing it with a
   plain paraphrase costs precision and signals that the product does not know
   the domain.
4. **Explain a term the first time** if some readers will not know it
   (`UI-TEXT-006`), and record that decision here.
5. **Record the internal name** whenever it differs, so a reviewer can spot
   leakage.

---

## Part 3 — Terms that must never reach user-visible text

These are categories, not a list, because the list is per product. Anything in
them belongs in layer 4 or layer 5 (`UX-ERR-012`).

- Function, method and class names.
- Exception type names.
- Protocol, bus, library and framework names, unless the reader selects them
  by name in the product's own UI.
- Numeric and symbolic error codes, except under the condition in
  `UX-ERR-012`.
- Internal state and enum names.
- Thread, buffer, handle, socket, descriptor, callback, null.
- File paths inside the installation, as opposed to the reader's own files.

**Review test.** Grep the string table for the product's namespace prefixes,
for `0x`, and for the words in the last bullet. Each hit is a finding.

---

## Maintenance

- A new user-visible concept gets a row **before** its first string.
- A term that changes gets changed everywhere in the same commit
  (`UX-ERR-020`).
- Removing a preferred term is an interface change where it appears in
  machine-readable output (`UI-CLI-020`).
- Where the product is localised, this file is the source list for
  translators; a synonym introduced in translation is the same defect.
