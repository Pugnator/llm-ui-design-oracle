# UI Copy Review Checklist

The procedure for generating and for reviewing user-visible text. It is the
executable half of `UX_WRITING_ORACLE.md` and `ERROR_MESSAGE_ORACLE.md`.

Answer each item **PASS**, **FAIL**, **N/A**, or **NEEDS HUMAN JUDGMENT**.
Cite the rule with every FAIL, and give its class — platform rule,
content-design principle, derived rule, or project convention — because the
four carry different weight when someone disagrees.

---

# Part 1 — The generation procedure

Run this **before** writing any string. Answering these in order produces the
message; writing first and editing afterwards does not, because the draft's
shape survives editing.

1. **What is the reader's current task?** Name it. If you cannot, you do not
   yet know what the message should say.
2. **What actually prevents or affects that task?** One condition. If there
   are two, there are two messages, or one of them is not worth reporting.
3. **Does the reader need to know?** Apply `UX-ERR-001`. If the product can
   recover, or the information is diagnostic only, stop here and log it.
4. **What is it?** Information, status, warning, error, or question
   (`UX-ERR-002`).
5. **Where does it belong?** The least interrupting surface they will actually
   see (`UX-ERR-003`). A dialog only if work cannot continue.
6. **What is the shortest accurate description?** One sentence, naming the
   object and its condition, in the reader's terms (`UX-ERR-005`).
7. **Is there an action the reader can take?** If yes, state it as an
   imperative and offer it as a control. If no, do not invent one
   (`UX-ERR-007`).
8. **Is a consequence important enough to mention?** Only if it is not obvious
   **and** changes what they do next (`UX-ERR-006`).
9. **What is diagnostic only?** Move it behind disclosure, copyable, and to
   the log (`UX-ERR-008`, `UX-ERR-009`).
10. **Now cut.** Remove every sentence that fails `UX-TEXT-009`. Then check
    that nothing is repeated across title, body, buttons and adjacent controls
    (`UX-TEXT-010`).

Then verify against Part 2. Do not keep a sentence because it is true.
Accuracy is necessary, not sufficient.

---

# Part 2 — The review checklist

## 0. Before anything else

| # | Question | Rule |
|---|---|---|
| 0.1 | Is the surface and its posture known, and is the audience declared in the profile? | `UI-GLOBAL-001`, `UX-TEXT-016` |
| 0.2 | Is the product's register declared — professional tool, or something warmer? | `UX-TEXT-001` |
| 0.3 | Is `TERMINOLOGY.md` filled in for the concepts this text names? | `UX-TEXT-017` |

If 0.3 fails, stop. Consistency cannot be reviewed against a list that does
not exist.

## 1. Should this text exist at all?

| # | Question | Rule |
|---|---|---|
| 1.1 | Which of the four dispositions is this condition — intervention, self-recovered, informational, diagnostic? | `UX-ERR-001` |
| 1.2 | If it is self-recovered or diagnostic, why is it on screen? | `UX-ERR-001` |
| 1.3 | Is any failure going unreported anywhere, including the log? | `UX-ERR-019` |
| 1.4 | Is success being announced that was requested and is visible? | `UX-TEXT-026` |
| 1.5 | Would the reader do anything differently if this string never appeared? | `UX-TEXT-007` |

## 2. Class and surface

| # | Question | Rule |
|---|---|---|
| 2.1 | Is it exactly one of information, status, warning, error, confirmation? | `UX-ERR-002` |
| 2.2 | Cover the icon: do the words alone say whether this happened, might happen, is a fact, or is a question? Uncover it — do they agree? | `UX-ERR-002`, `UX-TEXT-005` |
| 2.3 | Is a warning being used to soften an error that already happened? | `UX-ERR-018` |
| 2.4 | For each dialog: what decision does it require before work continues? | `UX-ERR-003`, `UX-ERR-014` |
| 2.5 | Does any dialog have a single dismissing button? | `UX-ERR-014` |
| 2.6 | Is a critical condition reported only in the status area or only in a transient message? | `UX-TEXT-024`, `UX-ERR-015` |
| 2.7 | Is the message near what it concerns? | `UX-ERR-003`, `UX-TEXT-029` |

## 3. Layering

| # | Question | Rule |
|---|---|---|
| 3.1 | Label every clause 1–5. Any clause without a layer? | `UX-ERR-004` |
| 3.2 | Does any fact appear in two layers, or twice on the surface? | `UX-TEXT-010`, `UX-ERR-004` |
| 3.3 | Does layer 1 name the specific object and its condition? | `UX-ERR-005`, `UX-TEXT-020` |
| 3.4 | Delete the consequence: would the next action change? | `UX-ERR-006` |
| 3.5 | Perform the stated recovery: does it resolve the condition? | `UX-ERR-007` |
| 3.6 | Is *Try again later* used where trying again later will not help? | `UX-ERR-007` |
| 3.7 | Are diagnostics present, folded, and copyable in one action? | `UX-ERR-008` |
| 3.8 | Does the fold reveal something not already visible? | `UX-TEXT-013` |
| 3.9 | Are the on-screen string and the log line the same string? | `UX-ERR-009` |

## 4. Diagnostics and audience

| # | Question | Rule |
|---|---|---|
| 4.1 | Does primary copy contain an API, function, protocol, library or subsystem name? | `UX-ERR-012` |
| 4.2 | Does it contain a raw numeric or symbolic code? If so, is it accompanied by a description and searchable? | `UX-ERR-012` |
| 4.3 | Does the reader need that information to decide what to do next? | `UX-ERR-012` |
| 4.4 | Is any user-facing string produced from an exception, HRESULT, errno or driver string? | `UX-ERR-010` |
| 4.5 | Is an expert reader shown diagnostics during ordinary workflow, rather than one deliberate step away? | `UX-ERR-023` |
| 4.6 | Is a term used that this audience would not use themselves, without explanation? | `UX-TEXT-016` |
| 4.7 | Does the same condition produce the same string in every place it is reported? | `UX-ERR-020`, `UX-ERR-011` |

## 5. Voice and tone

| # | Question | Rule |
|---|---|---|
| 5.1 | Grep for `!`, *oops*, *uh-oh*, *whoops*, *great*, *awesome*, *yay*. | `UX-TEXT-002` |
| 5.2 | For each *sorry*: what was lost? For each *please*: what inconvenience? | `UX-TEXT-003` |
| 5.3 | Grep for *unfortunately*, *don't worry*, *rest assured*, *simply*, *just*, *easily*, *please note*, *keep in mind*. | `UX-TEXT-006`, `AP-35` |
| 5.4 | Is the software the subject of a mental verb — *I could not*, *we're trying*? | `UX-TEXT-004` |
| 5.5 | Is the reader the subject of a mistake anywhere? | `UX-TEXT-018` |
| 5.6 | Grep for *critical*, *fatal*, *catastrophic*, *lost*, *corrupted*. Is each one true? | `UX-TEXT-005`, `AP-37` |
| 5.7 | Does anything read as marketing or praise of the product? | `UX-TEXT-006` |

## 6. Concision

| # | Question | Rule |
|---|---|---|
| 6.1 | For every sentence: if removed, would the reader make a worse decision? | `UX-TEXT-009` |
| 6.2 | Halve the text. Is anything needed now missing? | `UX-TEXT-008` |
| 6.3 | Is the result cryptic rather than concise? | `UX-TEXT-008` |
| 6.4 | Does the body restate the title? Does a tooltip restate its label? | `UX-TEXT-010`, `UX-TEXT-023` |
| 6.5 | Does the text state what an adjacent control already shows? | `UX-TEXT-010`, `UX-TEXT-012` |
| 6.6 | Are there past-tense clauses narrating what the program did? | `UX-TEXT-011`, `AP-31` |
| 6.7 | Does the text explain what a well-labelled control will do? | `UX-TEXT-012` |
| 6.8 | Count against the budgets in `UX-TEXT-014`. Which are sourced, which are project policy? | `UX-TEXT-014` |

## 7. Surfaces

| # | Question | Rule |
|---|---|---|
| 7.1 | Does every button name its action, starting with a verb? | `UX-TEXT-021`, `UX-ERR-013` |
| 7.2 | Does *OK* appear on a problem? Is *Yes/No* answering something that is not a question? | `UX-TEXT-021` |
| 7.3 | Is a halt button labelled *Cancel* while leaving partial work? | `UX-ERR-013` |
| 7.4 | Is the same action named identically in menu, button and tooltip? | `UX-TEXT-022`, `UX-TEXT-017` |
| 7.5 | Is any tooltip longer than a phrase, or a restatement of its label? | `UX-TEXT-023` |
| 7.6 | Does status text change faster than it can be read? | `UX-TEXT-024` |
| 7.7 | Does progress text name an activity, and avoid precision it cannot have? | `UX-TEXT-025` |
| 7.8 | Does progress restate the percentage the bar already shows? | `UX-TEXT-025`, `UX-TEXT-010` |
| 7.9 | Does the empty state distinguish "nothing matches" from "nothing yet", and offer one action? | `UX-TEXT-027` |
| 7.10 | Do settings descriptions say what happens when the setting is on, without repeating the label? | `UX-TEXT-028` |
| 7.11 | Do validation messages sit with the field, reuse its label, and wait until the reader has finished? | `UX-TEXT-029`, `UX-ERR-021` |

## 8. Confirmations and destruction

| # | Question | Rule |
|---|---|---|
| 8.1 | Is the guarded action genuinely irreversible? If not, where is undo? | `UX-ERR-016`, `UI-EDIT-001` |
| 8.2 | How often will the reader press the proceeding button? If usually, delete the confirmation. | `UX-ERR-016` |
| 8.3 | Does the title ask the real question rather than *Are you sure?* | `UX-ERR-017` |
| 8.4 | Does the proceeding button name the destruction? | `UX-ERR-017` |
| 8.5 | Press Enter blindly: what happened, and is it reversible? | `UI-DLG-005`, `UX-ERR-017` |
| 8.6 | Is input preserved when the condition is reported? | `UX-ERR-022` |

## 9. Anti-pattern sweep

Scan `UX_WRITING_ORACLE.md` §E, AP-31 to AP-39. For each present, state the
condition that makes it harmful here, or record it as acceptable with the
reason. Presence alone is not a finding — except AP-35 and AP-36, whose
sources reject them unconditionally in interface text.

| Pattern | One-line detection |
|---|---|
| AP-31 narrative explanation | two or more past-tense clauses about the software |
| AP-32 restating the obvious | *an error occurred* with no object and no cause |
| AP-33 internal reasoning | *since*, *therefore*, linking program state to program conclusion |
| AP-34 excessive consequences | more than one consequence sentence |
| AP-35 fake helpfulness | *please note*, *keep in mind*, *simply*, *you may want to* |
| AP-36 unnecessary politeness | *sorry*, *please*, *unfortunately*, with nothing lost |
| AP-37 dramatic language | severity words on a routine condition |
| AP-38 developer prose | identifiers, codes or frames in primary copy |
| AP-39 documentation in a dialog | more than three sentences, or any architecture explained |

Also sweep the core writing anti-patterns `AP-17`, `AP-23` to `AP-26`, which
this checklist does not duplicate.

---

# Part 3 — Reporting

```
Oracle version : <from VERSION>
Documents      : UX_WRITING_ORACLE, ERROR_MESSAGE_ORACLE, TERMINOLOGY
Profile        : <project> <profile version>
Scope          : <which strings were reviewed>
Result         : n PASS, n FAIL, n N/A, n NEEDS HUMAN JUDGMENT
```

Each finding:

```
FINDING  <rule-id>  <PASS|FAIL|N/A|NEEDS HUMAN JUDGMENT>
Surface  <where the string appears>
Class    <platform rule | content-design principle | derived rule | project convention>
String   <the text as shipped>
Evidence <what is wrong with it>
Rewrite  <the shortest version that passes, or the question a human must answer>
```

A review that reports only FAILs is incomplete: record the strings that were
checked and passed, so the next reviewer knows what has been looked at.

---

# Part 4 — Test strings

Use these to check that a reviewer, human or otherwise, is calibrated. Each is
technically accurate, grammatical and helpful-sounding. Each must be rejected,
and the expected findings are given.

| # | String | Must be rejected for |
|---|---|---|
| 1 | *Oops! Something went wrong. Please try again later.* | `UX-TEXT-002` (interjection, exclamation), `AP-32` (no object, no cause), `UX-TEXT-003` (*please*), `UX-ERR-007` (*later* will not help) |
| 2 | *The application was previously connected to the device, but the communication channel has now been interrupted and the session could not be maintained.* | `AP-31`, `UX-TEXT-011`, `UX-TEXT-008` |
| 3 | *PassThruWriteMsgs(ISO15765): ERR_TIMEOUT* | `UX-ERR-012`, `UX-ERR-010`, `AP-38`, `AP-26` |
| 4 | *Error: The operation could not be completed because an error occurred.* | `AP-32`, `UX-TEXT-005` (self-labelling), `UX-TEXT-020` |
| 5 | *Are you sure?* [Yes] [No] | `UX-ERR-017`, `UX-TEXT-021`, `UX-ERR-016` |
| 6 | *We're sorry, but unfortunately your file could not be saved at this time. Don't worry — your work is still open.* | `UX-TEXT-003`, `UX-TEXT-006`, `AP-35`, `AP-36`, `UX-TEXT-020` |
| 7 | *Saved successfully.* [OK] | `UX-TEXT-026`, `UX-ERR-014`, `UX-ERR-003` |
| 8 | *Since the device has stopped responding to status requests, the application can no longer determine the session state and will therefore terminate the session.* | `AP-33`, `UX-TEXT-011`, `UX-TEXT-004`, terminology (*terminate*) |
| 9 | *Critical failure: connection catastrophically lost.* | `AP-37`, `UX-TEXT-005` |
| 10 | *Invalid input. You entered an illegal value.* | `UX-TEXT-018`, `UI-TEXT-003`, `UX-TEXT-020` |
| 11 | A dialog reading *The device is not connected.* [OK] | `UX-ERR-003`, `UX-ERR-014`, `UX-ERR-007` |
| 12 | *Scanning requires an active session, which is established when the device handshake completes. Handshakes typically take two to three seconds. If the device is in bootloader mode…* | `AP-39`, `UX-TEXT-009`, `UX-TEXT-014` |

A reviewer that accepts any of these has not applied the oracle. String 7 is
the discriminating one: it is short, correct, polite and entirely unnecessary,
and a reviewer tuned only for verbosity will pass it.
