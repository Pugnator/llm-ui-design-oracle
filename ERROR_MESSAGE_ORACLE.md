# Error Message Oracle

Rules for conditions the product must tell someone about: errors, warnings,
confirmations, notifications, and the diagnostics that accompany them.

**Requires:** UI Oracle core >= 5.0.0 and `UX_WRITING_ORACLE.md`, which
governs the words. This file governs what is reported at all, how severe it
is, where it appears, what belongs in each layer, and what the reader is
offered. It is stricter than the writing oracle: nearly every rule is a MUST,
because an error surface is where a product does the most damage per word.

**Evidence:** `UX_COPY_EVIDENCE.md`. Rule IDs use the `UX-ERR-` prefix. Rule
format and classes are as in `UX_WRITING_ORACLE.md`.

---

## The five questions, in order

Work through these before writing a word. Most bad error messages are bad
because the writer started at question five.

1. **Should this be shown to a person at all?** (`UX-ERR-001`)
2. **What is it?** Information, status, warning, error, or a question.
   (`UX-ERR-002`)
3. **Where does it belong?** Inline, status, banner, notification, dialog,
   log. (`UX-ERR-003`)
4. **What goes in each layer?** (`UX-ERR-004` … `UX-ERR-009`)
5. **What is the reader offered?** (`UX-ERR-013` … `UX-ERR-015`)

---

# §A. Whether, what, and where

### UX-ERR-001 — Triage before writing
**Level:** MUST **Class:** DERIVED RULE **Authority:** Tier 2 + Tier 3
**Confidence:** HIGH

Every condition MUST be assigned to exactly one of four dispositions before
any text is written:

| Disposition | Meaning | Destination |
|---|---|---|
| **Intervention required** | The reader must decide or act before the task can continue | A surface they will see now (`UX-ERR-003`) |
| **Recoverable by the product** | The product can retry, fall back or continue correctly | Nothing, or ambient status; log it |
| **Informational state** | The reader benefits from knowing, but need not act | Ambient state: status, indicator, inline |
| **Diagnostic only** | Meaningful only to whoever maintains the product | Log; never a surface |

A condition MUST NOT be shown merely because it was detected.

**Rationale.** Cooper supplies the negative case in the strongest terms: most
error dialogs *"stop the proceedings with idiocy"*, and most messages *"simply
report when the application gets confused."* Microsoft supplies the positive
discipline: *"Don't provide unnecessary details … provide additional progress
information only if users can do something with it"*, and, on support-only
information, *"provide an alternative mechanism such as a log file."* Google supplies the constraint that stops this becoming silence — under the
heading *"Don't fail silently"*, *"Failure is inevitable; failing to report
failures is inexcusable."* But its remedy for the non-actionable case is the log, not the
screen. Visual Studio: *"Keep the number of notifications to the minimum
effective number."*

**Applicability.** Every condition, including ones inherited from a library or
driver.

**Source.** `AF4` Ch. 21; `W32-CTRL` Progress Bars; `GERR` error handling;
`VS-UX`. Q1, Q5.

**Exceptions.** Security-relevant events are reported even when the reader
cannot act, because the knowledge itself matters (`WIN7-TEXT`
Notifications).

**Review test.** For each message in the product, name its disposition. Then
ask what the reader would do differently if it never appeared.

---

### UX-ERR-002 — Severity is a small, fixed set
**Level:** MUST **Class:** PLATFORM RULE **Authority:** Tier 3 + Tier 2
**Confidence:** HIGH

Every reported condition MUST be exactly one of these, and the wording, icon,
container and offered action MUST all agree with the choice:

| Class | Definition | Attention | Blocks work | Usual surface | Wording |
|---|---|---|---|---|---|
| **Information** | A fact worth knowing | No | No | Inline, status | Statement of fact |
| **Status** | The current condition of an object or process | No | No | Status area, indicator | Fragment, present tense |
| **Warning** | A condition that **might** cause a problem later | Yes, once | No | Inline, banner, dialog if consequential | Conditional: *may*, *will not* |
| **Error** | A problem that **has** occurred | Yes | *Recoverable*: no. *Blocking*: yes | Inline or infobar; dialog only if blocking | Fact, plus recovery |
| **Confirmation** | A question before an irreversible act | Yes | Yes | Modal dialog | Question, answered by its buttons |

A sixth case, **fatal failure**, is an error whose recovery is "the product
cannot continue"; it uses the error wording and offers only exit and
diagnostics.

**Rationale.** The three message types are Microsoft's, verbatim and
deliberately not severity-based: *"Choose standard icons based their message
type, not the severity of the underlying issue: Error. An error or problem
that has occurred. Warning. A condition that might cause a problem in the
future. Information. Useful information."* Blurring them is forbidden:
*"Don't use warning icons to 'soften' non-critical errors. Errors aren't
warnings"*, and *"Icons must always match the main instruction."* Win32's
warning page shows the same condition written all three ways, which is why
the class must be chosen before the sentence. Visual Studio's
synchronous/asynchronous split supplies the blocking axis. Confirmation is
separate because it is a question, not a report (`WIN7-TEXT` Confirmations).

**Applicability.** All reported conditions.

**Source.** `W32-CTRL` Standard Icons; `WIN7-TEXT` Warning Messages,
Confirmations; `VS-UX`. Q6.

**Exceptions.** None. More classes may not be invented; the corpus does not
support them.

**Review test.** Cover the icon. From the words alone, is this something that
happened, something that might happen, a fact, or a question? Uncover it: do
they agree?

---

### UX-ERR-003 — The surface is chosen by impact, and a dialog is the last one
**Level:** MUST **Class:** PLATFORM RULE **Authority:** Tier 2 + Tier 3
**Confidence:** HIGH

A modal dialog MUST be used only when the reader must decide or act before
work can continue. Everything else MUST use the least interrupting surface
that the reader will actually see:

| Surface | Use when | Never |
|---|---|---|
| Inline, beside the control | The condition belongs to one field or object | For conditions with no on-screen origin |
| Infobar on the affected window | The condition affects this document or tool and offers an action | For conditions unrelated to that window |
| Status area | Ambient condition, redundant with something else | As the only place a critical condition appears |
| Notification | Asynchronous completion or a background problem | For anything requiring an immediate decision |
| Modal dialog | Work cannot continue until the reader answers | To report something they can only acknowledge |
| Log only | Diagnostic | — |

**Rationale.** Visual Studio's table is quoted almost directly: modal dialogs are for *"when a user response is required before
proceeding"* and not for *"when there is no need to block the user and
interrupt their flow"*, with the instruction to *"Avoid using modal dialogs
if it is possible to show the message in another, less intrusive way"*; the status bar *"Do not use alone"*; and critical information *"should
be provided in a dialog or in the Notifications tool window"* rather than the
status bar. NN/g gives the selection criterion: *"Design errors based on their
impact … modal dialogs require the user's attention and resolution and should
be reserved for severe errors"*, and *"Display the error message close to the
error's source."* Microsoft restricts by surface: balloons *"shouldn't be used
for critical errors"*, banners *"shouldn't be used for errors"*, and
background operations *"must stay in the background"*. Cooper supplies the
principle: *"A dialog is another room, and you should have a good reason to go
there."* Tidwell supplies the mechanical objection to modal error reporting:
dismissing the dialog removes the message you needed in order to fix the
problem. Core `UI-DLG-001` and `UI-FB-006` already require this at the
interaction level.

**Applicability.** All reported conditions.

**Source.** `VS-UX`; `NNG-ERR`; `W32-CTRL` Standard Icons, Progress Bars;
`AF4` Ch. 21; `DI3` Ch. 10; `UI-DLG-001`, `UI-FB-006`. Q5.

**Exceptions.** A condition that will destroy data if unacknowledged.

**Review test.** For each dialog: what decision does it require? If the only
button is a dismissal, it should not be a dialog.

---

# §B. The layered model

### UX-ERR-004 — Five layers, and each holds one kind of thing
**Level:** MUST **Class:** DERIVED RULE **Authority:** Tier 1 + Tier 2 + Tier 3
**Confidence:** HIGH

Information about a condition MUST be assigned to exactly one layer:

| Layer | Contains | Shown |
|---|---|---|
| **1. Primary message** | What happened, in the reader's terms | Always |
| **2. Consequence** | What it means for them — **only if not obvious** | Only when it changes their next decision |
| **3. Recovery** | What they can do — **only if they can do something** | Only when a real action exists |
| **4. Diagnostics** | Codes, protocol names, exception text, raw responses | Behind disclosure, copyable |
| **5. Log / report** | Everything, with timestamps and context | Never on the primary surface |

A fact MUST NOT appear in two layers. Layers 2 and 3 are conditional;
1, 4 and 5 are not.

**Rationale.** The model is assembled, and the assembly is shown rather than
assumed. Layer 1 and layer 3 are Google's two questions: *"What went wrong?"* and
*"How does the user fix that problem?"* Microsoft's three parts — *"A
problem"*, *"A cause"* and *"A solution"* — map to 1, 2 and 3, with the
cause serving the reader only when it changes what they do. Layer 4 is Microsoft's progressive disclosure
and NN/g's *"show them for technical diagnostic purposes only"*. Layer 5 is
Microsoft's log-file routing for IT professionals and `CLIG`'s debug file.

Two departures from a naive five-level reading, both forced by the evidence.
First, layers 2 and 3 are **conditional**, because Microsoft requires supplemental text only *"unless there really is more
detail"* — the source states it as a prohibition and `UX-TEXT-009`
deletes anything non-actionable. A rigid five-part template would manufacture
the padding this oracle exists to prevent. Second, the consequence layer is
the weakest-sourced part of the model: no source names it separately, so it is
marked DERIVED and is permitted only under the test in `UX-ERR-006`.

**Applicability.** Errors and warnings. Confirmations use layers 1–3 with the
question form. Status and information use layer 1 only.

**Source.** `GERR` index, Format for readability; `WIN7-TEXT` Error Messages;
`NNG-ERR`; `CLIG` Errors. Q1, Q2.

**Exceptions.** A fatal failure may omit layer 3 where no recovery exists, and
says so plainly rather than inventing one.

**Review test.** Label every clause with its layer number. Any clause without
a number does not belong. Any number appearing twice is duplication.

---

### UX-ERR-005 — Layer 1 names the object and what became of it
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 2 + Tier 3
**Confidence:** HIGH

The primary message MUST be one sentence, MUST name the specific object, and
MUST state its condition in the reader's terms. It MUST NOT name the
mechanism that detected the condition.

**Rationale.** `UX-TEXT-015` and `UX-TEXT-020` applied to the most important
sentence in the product. Microsoft requires the main instruction to be *"a
single, complete sentence"* and *"specific names, locations, and values of the
objects involved"*. Google's rewrites are the pattern: *"Resource <name> isn't
in cluster <name>"*, *"Time-out period (30s) exceeded"*.

**Applicability.** Every error, warning and confirmation.

**Source.** `WIN7-TEXT` Error Messages; `GERR` Identify the cause, Specify
requirements. Q2, Q9.

**Exceptions.** Where the object genuinely is not known, say so; do not guess.

**Review test.** Read layer 1 alone. Can the reader name what is affected?

---

### UX-ERR-006 — Layer 2 exists only when the consequence is not obvious
**Level:** MUST **Class:** DERIVED RULE **Authority:** Tier 2 + Tier 3
**Confidence:** MEDIUM

A consequence sentence MUST be included only when the effect is not evident
from layer 1 **and** changes what the reader does next. Otherwise it MUST be
omitted. At most one consequence per message.

**Rationale.** The layer is derived (`UX-ERR-004`), so its test is strict.
Microsoft's disclosure rule sets the principle — do not add a layer that
restates — and `UX-TEXT-009` supplies the test. `AP-34` is what happens
without the limit: a message that lists every downstream effect instead of the
one that matters.

*The connection was lost* does not need *so data is no longer being received*.
It does need *the last 40 seconds of the recording were not saved*, because
that changes whether the reader repeats the run.

**Applicability.** Errors, warnings, confirmations.

**Source.** `WIN7-TEXT` Error Messages; `UX-TEXT-009`; `AP-34`. Q2.

**Exceptions.** Irreversible loss is always stated, obvious or not.

**Review test.** Delete the consequence. Would the reader's next action
change? If not, it stays deleted.

---

### UX-ERR-007 — Layer 3 offers only actions the reader can actually take
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 2 + Tier 3
**Confidence:** HIGH

Where a recovery exists it MUST be stated as an imperative and, where the
product can perform it, offered as a control. Where none exists, the message
MUST NOT invent one; *Try again later* MUST NOT appear unless trying again
later is genuinely likely to work.

**Rationale.** Google: *"Create actionable error messages. That is, after
explaining the cause of the problem, explain how to fix the problem."* NN/g:
*"Merely stating the problem is also not enough; offer some potential
remedies."* Cooper requires the remedy to be a control rather than prose:
the message *"should offer buttons that will take care of the problem in
various ways. If a printer is missing, the message should offer options for
deferring the printout or selecting another printer."* Norman puts it as a
design instruction: *"Make it possible to correct problems directly from help
and guidance messages … Never make people start over."*

The prohibition is the other half. An instruction the reader cannot follow is
worse than silence: it costs a sentence and returns nothing.

**Applicability.** Errors and warnings.

**Source.** `GERR` Show how to fix; `NNG-ERR`; `AF4` Ch. 21; `DOET-R` Ch. 5.
Q2.

**Exceptions.** Where the only honest recovery is contacting support, say
that, and make the diagnostic easy to send (`UX-ERR-008`).

**Review test.** For each recovery sentence, perform it. Does it resolve the
condition?

---

### UX-ERR-008 — Layer 4 is present, folded, and copyable
**Level:** MUST **Class:** PLATFORM RULE **Authority:** Tier 1 + Tier 2 + Tier 3
**Confidence:** HIGH

Diagnostics MUST be available from the message, MUST be behind a disclosure
control, and MUST be selectable and copyable in one action. The disclosure
MUST reveal information not already shown. Diagnostics MUST NOT be discarded
because they do not belong in layer 1.

**Rationale.** Microsoft: *"use a Show/Hide details progressive disclosure
button to hide advanced or detailed information in an error message … don't
hide needed information"*; and on codes, *"always provide a text description
of the problem and solution. Don't depend just on the error code."* NN/g:
*"Hide or minimize the use of obscure error codes or abbreviations; show them
for technical diagnostic purposes only."* Google recommends the same shape for
long errors. Copyability is the practical requirement that makes the
diagnostic reach a bug report; `UI-IMGUI-018` already requires it where a
toolkit cannot select text.

**Applicability.** Every error with an underlying technical cause.

**Source.** `WIN7-TEXT` Error Messages; `NNG-ERR`; `GERR` Format for
readability; `UI-TEXT-008`; `UI-IMGUI-018`. Q1, Q8.

**Exceptions.** A surface with no room for disclosure routes to the log and
says where it is.

**Review test.** Trigger an error. Can you get the full diagnostic onto the
clipboard without retyping it? Does the fold reveal something new?

---

### UX-ERR-009 — Layer 5 keeps everything the other layers dropped
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 2 + Tier 3
**Confidence:** HIGH

Every reported condition, and every condition handled silently, MUST be logged
in full: timestamp, operation, object, the transport's own words, and the
internal identity of the condition. The log line MUST NOT be the string shown
on screen.

**Rationale.** `UI-TEXT-011` states the two-reader principle; the new sources
supply the obligation. Microsoft routes non-critical information for IT
professionals to log files because *"IT professionals strongly prefer log
files"*, and keeps support-only detail off the progress surface entirely, instructing
authors instead to *"provide an alternative mechanism such as a log file to
record technical support information"*. Google forbids
the opposite failure: *"Don't fail silently"*, and *"Log error codes, both
internal and external."*

**Applicability.** All conditions, including those dispositioned "recoverable
by the product".

**Source.** `WIN7-TEXT` Error Messages; `W32-CTRL` Progress Bars; `GERR`
error handling; `UI-TEXT-011`. Q1, Q12.

**Exceptions.** Secrets are never logged.

**Review test.** Take the on-screen string and the log line for one event. Are
they the same string? Then one reader is short-changed.

---

# §C. Diagnostics and the two readers

### UX-ERR-010 — Never render primary copy from a raw error string
**Level:** MUST **Class:** DERIVED RULE **Authority:** Tier 2 + Tier 3
**Confidence:** HIGH

Primary copy MUST NOT be produced from `exception.what()`, an `HRESULT`
description, `errno`, a Win32 error string, a driver or protocol error, or any
other text the product did not write for this purpose. Those strings are
evidence for layer 4 and layer 5.

**Rationale.** `CLIG` states the rule for its medium: *"Catch errors and
rewrite them for humans. If you're expecting an error to happen, catch it and
rewrite the error message to be useful."* Microsoft names the resulting defect
class — explaining the problem from the code's point of view — and GOV.UK
lists the symptoms: *"form post error"*, *"unspecified error"*, *"error
0x0000000643"*. `AP-26` already catalogues the pattern.

DERIVED because no source read states the prohibition in terms of a program's
internal error types; it is `UX-TEXT-015` plus `UX-ERR-012` applied to where
the string came from.

**Applicability.** All surfaces.

**Source.** `CLIG` Errors; `WIN7-TEXT` Error Messages; `GOVUK-DS` Error
message; `AP-26`. Q9.

**Exceptions.** A debugging surface (`UX-ERR-023`), where the raw string is
the content.

**Review test.** Grep the UI layer for exception, status and error-string
accessors. Each hit: does it reach a user-facing string?

---

### UX-ERR-011 — Errors are structured internally, not pre-formatted
**Level:** SHOULD **Class:** DERIVED RULE **Authority:** Tier 2
**Confidence:** MEDIUM

An internal error SHOULD carry structure rather than a finished English
sentence: an identity, the operation, the object, severity, recoverability,
the available actions, and the raw diagnostic. The user-facing string SHOULD
be produced from that structure at the surface.

**Rationale.** This is a writing requirement with an architectural
consequence, not an architecture. Three rules cannot be satisfied without it:
`UX-ERR-002` needs severity to be a property rather than a guess from wording;
`UX-TEXT-017` needs one condition to produce one string everywhere, which
Google states as *"the same problem must generate the same error message"*;
and `UX-ERR-004` needs the same condition rendered two ways, briefly on screen
and fully in the log. A pre-formatted string cannot do any of those.

MEDIUM and SHOULD deliberately: no source read prescribes an error model, and
the oracle does not design software. The requirement is the separation, not a
particular framework.

**Applicability.** Products where the same condition surfaces in more than one
place.

**Source.** Derived from `GERR` Use terminology consistently; `UX-ERR-002`,
`UX-ERR-004`, `UX-TEXT-017`. Q9, Q13.

**Exceptions.** A small product with one surface per condition.

**Review test.** Pick a condition reachable from two places. Are the two
strings identical, and do both have the full diagnostic?

---

### UX-ERR-012 — Do not expose implementation diagnostics in primary copy
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 1 + Tier 2 + Tier 3
**Confidence:** HIGH

Layer 1 MUST NOT contain API or function names, protocol or library names,
subsystem names, numeric or symbolic error codes, exception class names, raw
device responses, or stack frames.

**Review questions.**

- Does the primary text contain an API or function name?
- Does it contain a protocol, library or subsystem name?
- Does it contain a raw numeric or string error code?
- Does the reader need that information to decide what to do next?
- Could it instead sit under Details, or in a copyable diagnostic block?

If the answer to the fourth question is no and the answer to the fifth is yes,
the text is in the wrong layer.

**Rationale.** NN/g: *"Hide or minimize the use of obscure error codes or
abbreviations; show them for technical diagnostic purposes only."* Microsoft
requires a text description alongside any code, and keeps debugging detail out
of release builds. GOV.UK rejects the code-only message by example. `AP-38`
gives the before and after.

**Applicability.** All surfaces, all audiences. Expertise changes vocabulary,
not layering (`UX-ERR-023`).

**Source.** `NNG-ERR`; `WIN7-TEXT` Error Messages; `W32-CTRL` Progress Bars;
`GOVUK-DS` Error message. Q1, Q8.

**Exceptions.** A code the reader is expected to quote to support may appear
in layer 1 **if** it is accompanied by the description and is searchable —
Microsoft's condition. A debugging surface is exempt.

**Review test.** The five questions above, on every error string in the
product.

---

### UX-ERR-023 — Distinguish a technical reader from a reader who is debugging
**Level:** MUST **Class:** DERIVED RULE **Authority:** Tier 2 + Tier 3
**Confidence:** MEDIUM

Expertise MUST NOT be treated as consent to raw diagnostics in ordinary
workflow. Diagnostic density MUST follow the reader's current task, not their
qualifications. A product MAY offer an explicit debugging surface — a verbose
mode, a diagnostics pane, a log viewer — where layer 4 becomes layer 1, and
that surface MUST be entered deliberately.

**Rationale.** Google establishes that terminology follows the audience: an
ML-expert message is *"Recommended for ML experts only"*, and the same string
is right for engineers and wrong for other readers. It does not follow that an
expert wants a protocol trace while doing something else. `CLIG` resolves the
same tension for an audience that is developers by definition: *"By default,
don't output information that's only understandable by the creators of the
software … only in verbose mode."* Microsoft routes IT-professional detail to
log files rather than dialogs. All three keep the detail one deliberate step
away.

DERIVED: no source read separates the person's expertise from their current
task in these words. The synthesis is ours and is marked as such.

**Applicability.** Professional and technical products — the class most likely
to get this wrong in the permissive direction.

**Source.** `GERR` Target audience; `CLIG` Output; `WIN7-TEXT` Error Messages.
Q8.

**Exceptions.** A product whose entire purpose is diagnosis. Even there,
layer 1 names what failed before the trace begins.

**Review test.** Take one expert reader mid-task. Does the ordinary path show
them a protocol identifier? Can they reach one in a single deliberate action?

---

# §D. What the reader is offered

### UX-ERR-013 — Buttons on an error name the recovery
**Level:** MUST **Class:** PLATFORM RULE **Authority:** Tier 1 + Tier 3
**Confidence:** HIGH

Buttons MUST name the action: *Retry*, *Reconnect*, *Open settings*,
*Choose another file*, *Save as*, *Discard*. *OK* MUST NOT appear on a
problem; the dismissing button is *Close*. Where an operation can be halted,
the button is *Cancel* if stopping leaves no trace and *Stop* if it leaves
partial work.

**Rationale.** `UX-TEXT-021` plus the specific sources. Win32 Error Messages:
*"provide a Close button. Don't use OK for error messages, because this
wording implies that problems are OK."* Progress bars: *"Label the button
Cancel if canceling returns the environment to its previous state (leaving no
side effects), otherwise label the button Stop to indicate that it leaves the
partially completed operation intact."* Cooper requires the buttons to
resolve the problem rather than acknowledge it.

**Applicability.** Errors, warnings, confirmations, long operations.

**Source.** `WIN7-TEXT` Error Messages; `W32-CTRL` Progress Bars, Command
Buttons; `AF4` Ch. 21; `UI-TEXT-012`. Q10, Q11.

**Exceptions.** None.

**Review test.** Does any error dialog carry *OK*? Does any halt button say
*Cancel* while leaving partial work behind?

---

### UX-ERR-014 — Acknowledgement must be worth the interruption
**Level:** MUST **Class:** DERIVED RULE **Authority:** Tier 2 + Tier 3
**Confidence:** HIGH

A message MUST NOT require acknowledgement unless the reader must decide
something. A dialog whose only button dismisses it MUST be moved to a
non-blocking surface.

**Rationale.** Cooper: *"Launching an alert to announce an unrequested action
is bad enough. Launching one to announce a requested action is pathological"*,
and the arithmetic of an alert over a Find dialog — *"the user's burden would
be reduced by half"* if the information were built into the surface it
concerns. Visual Studio: use modal dialogs *"only when necessary to prevent
the user from taking further action before acknowledging the message or making
a decision"*, and *"Do not require the user to dismiss a notification if they
have already taken action."*

**Applicability.** All blocking surfaces.

**Source.** `AF4` Ch. 21; `VS-UX`; `UI-DLG-001`. Q5.

**Exceptions.** Data loss about to occur.

**Review test.** Count the dialogs with one button. Each is a finding until
its blocking decision is named.

---

### UX-ERR-015 — Transient messages are for things that need no response
**Level:** MUST **Class:** DERIVED RULE **Authority:** Tier 2 + Tier 3
**Confidence:** MEDIUM

A message that disappears on its own MUST NOT carry information the reader
needs later, MUST NOT be the only report of an error, and MUST be removed when
it stops being true.

**Rationale.** Visual Studio: *"Remove ambient notifications when they are no
longer valid"*, and bubbles are *"inappropriate for critical information that
the user must solve right away."* Win32 restricts balloons from critical
errors. Johnson Ch. 5 and Ch. 7 supply the cost: peripheral changes are easily
missed and nothing should require the reader to remember status. MEDIUM
because no source read gives durations.

**Applicability.** Toasts, balloons, auto-dismissing banners, transient status.

**Source.** `VS-UX`; `W32-CTRL` Standard Icons, Balloons; `JM3` Chs. 5, 7.
Q5.

**Exceptions.** Confirmation of a reversible action, where the undo affordance
travels with the message and its disappearance ends the window to undo — which
must then be stated.

**Review test.** Look away for ten seconds during the operation. What did you
miss, and where else can you find it?

---

# §E. Warnings, confirmations and timing

### UX-ERR-016 — Confirm only what the reader would want stopped
**Level:** MUST **Class:** PLATFORM RULE **Authority:** Tier 1 + Tier 2
**Confidence:** HIGH

A confirmation MUST be used only where the action is irreversible **and** has
a consequence the reader may not have intended. Where undo is possible, undo
MUST be offered instead. A confirmation MUST NOT appear on a path the reader
takes routinely.

**Rationale.** Microsoft draws the line: confirm actions that *"can't be
undone and have major consequences"*; otherwise *"offering a simple undo
command is usually enough"*, because confirmations *"are a hindrance whenever
the user is trying to perform an action intentionally."* Cooper supplies the
sharper operational test and the mechanism behind it: *"confirmations … work
only when they are unexpected"*, and therefore *"they must appear only when
the user will almost definitely click the No or Cancel button. They should
never appear when the user is likely to click the Yes or OK button."* His
alternatives are *"Do, don't ask"* and *"Make all actions reversible."*
Johnson Ch. 15 explains why a routine confirmation is worse than none: it is
dismissed by a practised motor sequence.

**Applicability.** Every confirmation in the product.

**Source.** `MS-COMMAND`; `AF4` Ch. 21; `JM3` Ch. 15; `UI-DLG-003`,
`UI-EDIT-001`. Q10.

**Exceptions.** A regulatory or safety requirement to obtain explicit consent.

**Review test.** For each confirmation, estimate how often the reader presses
the proceeding button. If it is most of the time, delete the confirmation and
add undo.

---

### UX-ERR-017 — A destructive confirmation names the destruction
**Level:** MUST **Class:** PLATFORM RULE **Authority:** Tier 1 + Tier 3
**Confidence:** HIGH

The title MUST ask the actual question, the body MUST state what will be lost,
and the proceeding button MUST name the destructive act. *Are you sure?* MUST
NOT be the question. The default MUST NOT be the destructive button
(`UI-DLG-005`). Where the reason not to proceed is not obvious, the
proceeding button takes *anyway*, or the pair becomes a real question.

**Rationale.** Microsoft's confirmation guidance: where the reason not to
proceed is not obvious, add *anyway* or use Yes/No, which *"forces users to at
least read the main instruction"*; and buttons should *"start with a verb"*.
The call-and-response requirement makes the title and buttons one unit. Cooper
supplies the objection to the generic form: *"Every time we delete a file in
Windows, we get this confirmation dialog asking if we're sure. Yes, we're
sure. We're always sure."*

**Applicability.** All destructive confirmations.

**Source.** `WIN7-TEXT` Confirmations; `MS-WRITING` Dialogs; `AF4` Ch. 21;
`UI-DLG-005`, `UI-TEXT-012`. Q10.

**Exceptions.** None.

**Review test.** Read the title and buttons as an exchange. Does a button name
what is destroyed? Press Enter blindly: what happened?

---

### UX-ERR-018 — A warning states the condition, not the alarm
**Level:** MUST **Class:** PLATFORM RULE **Authority:** Tier 3
**Confidence:** HIGH

A warning MUST describe a condition that might cause a problem later, in
conditional form, and MUST NOT use the words *warning* or *caution* to
announce itself. It MUST NOT be used to soften an error that has already
occurred.

**Rationale.** Win32 Warnings: *"don't use the terms 'warning' or 'caution' in
the text. When used correctly, the warning icon sufficiently communicates"*
it; and Standard Icons: *"Don't use warning icons to 'soften' non-critical
errors. Errors aren't warnings."* The three-way example — has happened, might
happen, is a fact — is the discipline this rule enforces.

**Applicability.** All warnings.

**Source.** `WIN7-TEXT` Warning Messages; `W32-CTRL` Standard Icons. Q6.

**Exceptions.** None.

**Review test.** Does the warning describe something that already happened? It
is an error.

---

### UX-ERR-019 — Do not fail silently
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 2
**Confidence:** HIGH

A failure MUST NOT pass unreported. Where the reader need not act, it is
reported to the log (`UX-ERR-009`); where they must, to a surface.

**Rationale.** Google: *"Failure is inevitable; failing to report failures is
inexcusable"*, with both costs named — *"Users wonder whether something has
gone wrong"* and *"Customer support wonders what caused a problem."* NN/g adds
the preventive half: *"The very worst error messages are those that don't
exist. When users make a mistake and receive no feedback, it can create a
cascade of misunderstanding."*

This rule exists to bound `UX-ERR-001`. Triage decides where a condition is
reported, never whether it is recorded.

**Applicability.** All failures, including handled ones.

**Source.** `GERR` error handling; `NNG-ERR`. Q1.

**Exceptions.** None.

**Review test.** Force a handled failure. Is there a log line?

---

### UX-ERR-020 — One condition, one message, everywhere
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 2 + Tier 3
**Confidence:** HIGH

The same condition MUST produce the same text wherever it is reported, and
different conditions MUST NOT share a message where the product can tell them
apart.

**Rationale.** Google states both halves: *"the same problem must generate the
same error message"*, and, on distinguishing, the whole of *Identify the
cause*. Win32: *"don't rely on a single error message to report a problem with
several different detectable causes."* GOV.UK requires the summary and the
inline message to match word for word (`UI-TEXT-013`).

**Applicability.** All surfaces, including logs where shown.

**Source.** `GERR` Use terminology consistently, Identify the cause;
`WIN7-TEXT` Error Messages; `UI-TEXT-013`. Q13.

**Exceptions.** None.

**Review test.** Pick one condition. List every place it is reported. Diff the
strings.

---

### UX-ERR-021 — Do not report an error before the reader has finished
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 2
**Confidence:** HIGH

Validation MUST NOT fire while the reader is still working on the value.
Leaving a field untouched MUST NOT be treated as an error.

**Rationale.** NN/g: *"Avoid prematurely displaying errors. Timing is a
crucial aspect … Presenting errors too early is a hostile pattern. It's like
grading a test before the student has had a chance to answer"*, and *"Don't
assume that exploratory interactions … are errors."* Tidwell names the
specific annoyance: a message that appears as soon as the user begins typing
and does not clear until the entry is complete. Cooper's account of
out-of-sequence input is the general form: *"Software usually jumps to the
erroneous conclusion that out-of-sequence input means wrong input."*

**Applicability.** Forms, inline editing, parameter entry.

**Source.** `NNG-ERR`; `DI3` Ch. 10; `AF4` Ch. 21; `UI-EDIT-004`. Q2.

**Exceptions.** NN/g's own: error-prone fields where immediate guidance
demonstrably helps.

**Review test.** Tab through an empty form without typing. How many errors
appeared?

---

### UX-ERR-022 — Never make the reader start over
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 2 + Tier 4
**Confidence:** HIGH

Input MUST be preserved when a condition is reported. The reader MUST be able
to correct the problem from where they are.

**Rationale.** NN/g: *"Preserve the user's input. Let users correct errors by
editing their original action instead of starting over"*, and *"Reduce
error-correction effort"* by offering the likely fix. Norman: *"Make it
possible to correct problems directly from help and guidance messages. Allow
people to continue with their task … Never make people start over"*, and
*"Assume that what people have done is partially correct."*

**Applicability.** All conditions that interrupt work in progress.

**Source.** `NNG-ERR`; `DOET-R` Ch. 5; `UI-SEL-002`. Q2.

**Exceptions.** Where continuing would corrupt data.

**Review test.** Trigger the error mid-task. Is the work still there?

---

# What this oracle deliberately does not say

- **A dialog length ceiling.** Unsourced; the project figure lives in
  `UX-TEXT-014` and is labelled policy.
- **Auto-dismiss durations.** No source read gives numbers.
- **An error framework.** `UX-ERR-011` states a separation, not a design.
- **Apple's alert conventions.** Not obtained.
- **Retry policy.** When to retry automatically is an engineering decision;
  this oracle governs only what the reader is told about it.
