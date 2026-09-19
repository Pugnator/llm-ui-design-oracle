# UX Copy Evidence

Evidence layer for `UX_WRITING_ORACLE.md` and `ERROR_MESSAGE_ORACLE.md`.

It records what the sources say **before** any rule is written, so that a rule
can be traced to evidence rather than evidence hunted to fit a rule. Where the
sources are silent, this file says so and the rule is marked DERIVED or
PROJECT CONVENTION rather than invented.

Locations are section headings in the archived text under `corpus/copy/`,
`corpus/writing/` and `corpus/platform/`, or page numbers in the local books.
No quotation below comes from memory.

## Source labels used here

| ID | Source | Tier | Archived |
|---|---|---|---|
| `GERR` | Google, *Writing Helpful Error Messages* (14 units) | 2 | `corpus/copy/gerr-*.md` |
| `GSTYLE` | Google developer documentation style guide (tone, voice, UI elements, word list, accessibility) | 2 | `corpus/copy/gstyle-*.md` |
| `W32-CTRL` | Win32 UX Guide: progress bars, status bars, tooltips and infotips, balloons, command buttons, standard icons | 3 | `corpus/copy/w32-*.md` |
| `WIN7-TEXT` | Win32 UX Guide: error, warning, confirmation, notification, UI text, style and tone | 3 | `corpus/writing/win32-*.md` |
| `VS-UX` | Visual Studio UX Guidelines: notifications and progress | 2 | `corpus/copy/vs-notifications.md` |
| `MS-STYLE` | Microsoft Writing Style Guide (16 pages across both corpora) | 1 | `corpus/writing/msstyle-*.md`, `corpus/copy/msstyle-*.md` |
| `MS-WRITING` | Windows apps design: Writing style | 1 | `corpus/writing/ms-winapps-writing-style.md` |
| `GOVUK-DS`, `GOVUK-WG` | GOV.UK Design System and writing guidelines; GOV.UK style guide A–Z | 2 | `corpus/writing/govuk-*.md`, `corpus/copy/govuk-a-to-z.md` |
| `CLIG` | Command Line Interface Guidelines | 2 | `corpus/writing/clig-dev.md` |
| `NNG-ERR` | Nielsen Norman Group, *Error-Message Guidelines*, Neusesser and Sunwall, 2023-05-14 | 2 | Not archived (copyright NN/g); SHA-256 `3743275088e5a70729a947f1a16c3672f492cffd5adf3ec0e14e3370b6c05454` |
| `AF4`, `JM3`, `DI3`, `DOET-R` | Cooper, Johnson, Tidwell, Norman — the books already in the matrix | 2 / 4 | `docs/` (not redistributed) |

**Apple was not obtained.** The current Human Interface Guidelines render
only through JavaScript, the legacy `library/archive` pages now redirect to
the same shell, and the Wayback Machine holds no snapshot of the writing or
alerts pages. No Apple citation appears anywhere in this oracle. This is an
open gap, recorded in `UI_SOURCE_MATRIX.md`, not a judgement about Apple's
guidance.

**Three UX-writing books named in the brief** — Podmajersky, *Strategic
Writing for UX*; Metts and Welfle, *Writing Is Designing*; Yifrah,
*Microcopy* — are **not** in the local corpus and were not obtained. Nothing
here is attributed to them.

---

## Q1. Should internal error codes and diagnostics appear in the primary message?

### Microsoft
`WIN7-TEXT` Error Messages, *Error codes*: *"always provide a text
description of the problem and solution. Don't depend just on the error
code"*, and codes should be *"easily searchable on the Internet"*.
*Progressive disclosure*: *"use a Show/Hide details progressive disclosure
button to hide advanced or detailed information in an error message … don't
hide needed information, because users might not find it"*, and *"don't use
Show/Hide details unless there really is more detail. Don't just restate the
existing information in a more verbose format."*

`W32-CTRL` Progress Bars is blunter about diagnostics that serve the vendor
rather than the reader: *"Don't provide unnecessary details. Generally users
don't care about the details of the operation being performed … Providing
details that users don't care about makes the user experience overly
complicated and technical. If you need more detailed information for
debugging, don't display it in release builds."* And *"Don't worry about
technical support … if the operation can fail (as with a setup program),
don't provide additional progress information that is only useful to
technical support. Instead, provide an alternative mechanism such as a log
file to record technical support information."*

### Google
`GERR` *Format error messages to enhance readability* recommends progressive
disclosure by name: *"Some error messages are long … users sometimes ignore
long error messages, intimidated by the 'wall of text.' A good compromise is
to display a briefer version of the error message and then give users the
option to click something to get the full context."* `GERR` *error handling*
separately requires the diagnostic to exist: *"Log error codes, both internal
and external, and document them"*, and *"API implementations should not
swallow the root cause."*

### Nielsen Norman Group
`NNG-ERR`, Communication Guidelines: *"Hide or minimize the use of obscure
error codes or abbreviations; show them for technical diagnostic purposes
only."*

### GOV.UK
`GOVUK-DS` Error message, *Be clear and concise*, rejects the raw form
outright, listing *"form post error"*, *"unspecified error"* and *"error
0x0000000643"* as messages that do not help.

### CLI
`CLIG` Errors: *"Catch errors and rewrite them for humans"*, and for the
unexpected case *"provide debug and traceback information … Consider writing
the debug log to a file instead of printing it to the terminal."*

### Interpretation

Five independent sources describe the same three-place structure: a written
sentence for the reader, a fuller diagnostic reachable on demand, and a log
that keeps everything. None says the diagnostic should be destroyed; all say
it does not belong on the face of the message. Microsoft adds the sharpest
test — information useful only to the vendor's support process is not the
reader's information, and belongs in a log.

### Proposed rules
`UX-ERR-004` (the layered model), `UX-ERR-008` (diagnostics behind
disclosure, copyable), `UX-ERR-012` (no diagnostics in primary copy),
`UX-ERR-009` (logs).

### Applicability
All surfaces, all audiences. Q8 handles the expert-audience objection.

### Confidence
HIGH. Direct, repeated, and consistent across four vendors and one
independent body.

---

## Q2. What must an error message contain?

### Microsoft
`WIN7-TEXT` Error Messages, *The characteristics of good error messages*,
lists three parts and then eight qualities. The parts: *"A problem. States
that a problem occurred."*; *"A cause. Explains why the problem occurred."*;
*"A solution. Provides a solution so that users can fix the problem."* The
qualities are given as *"Relevant"*, *"Actionable"*, *"User-centered"*,
*"Brief"*, *"Clear"*, *"Specific"*, *"Courteous"* and *"Rare"*, each with a
gloss — *"Brief. The message is as short as possible, but no shorter"*, and
*"User-centered. The message describes the problem in terms of target user
actions or goals, not in terms of what the code is unhappy with."*
Supplemental text should *"aim for a maximum of three sentences of moderate
length."*

### Google
`GERR` index: *"Great error messages answer two questions as clearly and
concisely as possible: What went wrong? How does the user fix that
problem?"* The course's own summary lists: identify the cause; specify the
invalid value; specify requirements and constraints; explain how to fix;
provide an example where useful.

`GERR` *Specify requirements* gives the pattern: not *"The combined size of
the attachments is too big"* but *"The combined size of the attachments
(14MB) exceeds the allowed limit (10MB)"*; not *"Time-out period exceeded"*
but *"Time-out period (30s) exceeded."*

### Nielsen Norman Group
`NNG-ERR`: *"Concisely and precisely describe the issue. Generic messages
such as An error occurred lack context"*, and *"Offer constructive advice.
Merely stating the problem is also not enough; offer some potential
remedies."*

### GOV.UK
`GOVUK-DS` Error message: *"describe what has happened and tell them how to
fix it"*; *"Be specific"* — *"An error occurred"*, *"Select an option"* and
*"This field is required"* *"do not make sense out of context"*.

### Books
`AF4` Ch. 21 describes the well-formed case: an error dialog *"should offer
buttons that will take care of the problem in various ways. If a printer is
missing, the message should offer options for deferring the printout or
selecting another printer."*

### Interpretation

Two questions are mandatory (what happened, what to do); the cause is
mandatory *when the program knows it and the reader can act on it*; the
consequence is not named by these sources as a separate part, but Microsoft's
"cause" and NN/g's "constructive advice" together imply it where the effect
is not obvious. Google's contribution is the strongest: specificity means
naming the actual values and limits, not the category.

### Proposed rules
`UX-ERR-005`, `UX-ERR-006`, `UX-ERR-007`, and `UX-TEXT-020` (specific, not
generic).

### Confidence
HIGH for the two mandatory parts. MEDIUM for treating consequence as its own
layer: it is derived from Microsoft's "cause" plus NN/g rather than named by
any source. Recorded as such in the rule.

---

## Q3. Should software apologise, and may it be funny?

### Google
`GERR` *Set the tone*, under the heading *"Don't be overly apologetic"*:
*"While maintaining positivity, avoid the words 'sorry' or 'please.'"* With a
stated caveat:
*"Different cultures interpret apologies differently … be aware of your
target audience's expectations."* On humour: *"Don't attempt to make error
messages humorous"*, because *"Errors frustrate users. Angry users are
generally not receptive to humor"*, *"Users can misinterpret humor"*, and
*"Humor can detract from the goal of the error message."*

`GSTYLE` Voice and tone lists what to avoid, including *"Being too cutesy"*,
*"Wackiness, zaniness, and goofiness"*, *"Placeholder phrases like please
note and at this time"*, and *"Exclamation marks. In general, avoid
exclamation points."* On politeness: *"It's great to be polite, but using
please in a set of instructions is overdoing the politeness."*

### Microsoft
`WIN7-TEXT` Style and Tone: *"limit please to situations that inconvenience
the user"*; *"Use sorry only in error messages that result in serious problems for the
user (for example, data loss, the user can't continue to use the computer, or
the user must get help from a technical representative). Don't apologize if
the issue occurred during the normal functioning of the program."* Win32 UI Text on
exclamation points: *"in business applications, avoid"*.

### GOV.UK
`GOVUK-DS` Error message: do not use *"please"* because *"it implies a
choice"*, nor *"sorry"* because *"it does not help fix the problem"*. Yet
GOV.UK's own service-failure pages mandate the H1 *"Sorry, there is a problem
with the service"*.

### Nielsen Norman Group
`NNG-ERR` agrees for the ordinary case — *"Avoid humor since it can become
stale if users encounter the error frequently"* — and then carves out an
exception: *"Mitigate total failure with novelty … sometimes users may
encounter an error so catastrophic … there is no recourse but to wait or try
again later. It's these specific moments … where blending an apology with
something surprising or novel may salvage a disappointing situation."* It
scopes the exception itself: *"which should be rare and avoided at all
costs"*, and *"low-stakes experiences"*.

### Books
`DI3` Ch. 10, *Error Messages*, gives the opposite advice from the rest:
*"Be polite: 'Sorry, but something went wrong! Please click Go again' versus
'JavaScript Error 693'."*

### Interpretation

Four sources converge: neither word by default, both reserved for a real cost
borne by the reader. This is already `UI-TEXT-004` and conflict `C14`; the new
sources corroborate it rather than change it.

Two sources dissent, and both dissents are scoped. NN/g's exception is for
consumer products, total outages and low stakes, and NN/g says so in the
sentence itself. Tidwell's is a 2020 web-form example whose contrast case is a
raw JavaScript error, so it argues against jargon more than it argues for
apology. Neither dissent reaches a professional tool reporting a routine
operational condition. Recorded as conflict `C20`.

### Proposed rules
`UX-TEXT-002` (no interjections, exclamations or humour), `UX-TEXT-003`
(apology and politeness reserved), both deferring to `UI-TEXT-004`.

### Applicability
Professional desktop and command-line tools. A consumer product with a
public-facing outage page may reasonably take NN/g's exception; the rule says
so rather than pretending the disagreement does not exist.

### Confidence
HIGH for the default, with the dissent recorded.

---

## Q4. Does the software get to have a personality?

### Google
`GSTYLE` Voice and tone asks documentation to be *"conversational, friendly,
and respectful"* and to *"Try to sound like a knowledgeable friend."* But the
same page states the limit: *"remember that the primary purpose of the
document is to provide information to someone who's looking for it and may be
in a hurry"*, and its own "Just about right" column is plain: *"This API lets
you collect data about what your users like."*

### Microsoft
`MS-WRITING` gives three voice principles and asks for warmth. `WIN7-TEXT`
Style and Tone, writing for the same company's desktop software, lists tones
to *avoid*, and `W32-CTRL` Tooltips adds *"Don't use language that sounds
like marketing."*

### GOV.UK
`GOVUK-WG` Use the right tone asks for text that is *"emotionless"* and
*"brisk, but not terse"*.

### Interpretation

The disagreement is about medium, not about quality. Google's warmth
guidance governs *developer documentation*, which the reader chose to open and
reads at length; its error-message course, addressing UI strings, says
something different and stricter. Microsoft asks for warmth in marketing-
adjacent app copy and forbids it in tooltips and messages. The oracle already
recorded the Microsoft/GOV.UK tone split as unresolvable by evidence
(`modules/writing.md`, "What this module deliberately does not say"). The new
evidence does not settle it; it explains it. A message the operator did not
ask to read is not the place for personality.

### Proposed rules
`UX-TEXT-001` (register), which fixes the professional-tool end of the range
as a stated project posture rather than as a universal law.

### Confidence
HIGH that medium explains the split. The choice of register for a given
product remains a profile decision.

---

## Q5. When does a condition deserve a dialog?

### Visual Studio
`VS-UX` gives the fullest surface table in any source read, pairing each
method with when *not* to use it. Modal error dialogs, in the table's two columns — use *"when a user
response is required before proceeding"*, and do not use *"when there is no
need to block the user and interrupt their flow"*, with the instruction
*"Avoid using modal dialogs if it is possible to show the message in another,
less intrusive way."* Status bar:
*"Use when there is ambient textual information … Do not use alone."*
Embedded infobar: *"use to notify of progress, error state, results, and/or
actionable information."* It also states the general constraints: *"Keep the
number of notifications to the minimum effective number"*; *"Remove ambient
notifications when they are no longer valid. Do not require the user to
dismiss a notification if they have already taken action"*; and the
synchronous/asynchronous split — a crash needs *"a manner that requires their
input, such as in a modal dialog"*, whereas a completed build *"should be more
ambient and not interrupt the user's task flow."*

### Microsoft desktop
`WIN7-TEXT` Notifications, *What to notify*: *"don't notify of successful
operations"*, with three exceptions (security, after a recent failure,
success in an unexpected form); *"assume that users take successful
operations for granted."* `W32-CTRL` Standard Icons restricts by surface:
balloons *"shouldn't be used for critical errors"*; banners *"shouldn't be
used for errors."* `W32-CTRL` Progress Bars: *"Don't steal input focus to
show a progress update or completion. Users often switch to other programs
while waiting … Background tasks must stay in the background."*

### Nielsen Norman Group
`NNG-ERR` Visibility Guidelines: *"Design errors based on their impact …
conditionally displayed labels, toast notifications, or banners can be used
for issues needing minimal user interaction, whereas modal dialogs require the
user's attention and resolution and should be reserved for severe errors."*
Also *"Display the error message close to the error's source."*

### Books
`AF4` Ch. 21 is the strongest statement in the corpus: error dialogs
*"stop the proceedings with idiocy"*; alerts *"announcing the obvious"* —
*"Launching an alert to announce an unrequested action is bad enough.
Launching one to announce a requested action is pathological"*; and the
general principle *"A dialog is another room, and you should have a good
reason to go there."*

`DI3` Ch. 10 rejects modal dialogs for form errors on a mechanical ground:
*"you had to click away the modal dialog box to fix the error. And with the
dialog box gone, you couldn't read the error message anymore."*

### Interpretation

Every source treats the modal dialog as the exception requiring
justification, and all of them justify it the same way: the user must decide
something before work can continue. Everything else has a quieter home, and
the sources between them name those homes — inline beside the control, an
infobar on the affected window, the status bar, a notification, a log entry.
`NNG-ERR` supplies the selection criterion (impact), `VS-UX` supplies the
table, and `AF4` supplies the reason it matters.

### Proposed rules
`UX-ERR-001` (triage), `UX-ERR-002` (severity), `UX-ERR-003` (surface
selection). The core's `UI-DLG-001` and `UI-FB-006` already require this at
the interaction level; these rules make the copy consequences explicit.

### Confidence
HIGH.

---

## Q6. What severity classes are real?

### Microsoft
`W32-CTRL` Standard Icons defines exactly three and ties them to message
type, not to how bad the underlying condition is: *"Choose standard icons
based their message type, not the severity of the underlying issue: Error. An
error or problem that has occurred. Warning. A condition that might cause a
problem in the future. Information. Useful information."* It forbids blurring
them: *"Don't use warning icons to 'soften' non-critical errors. Errors
aren't warnings"*, and *"Icons must always match the main instruction."*

`WIN7-TEXT` Warning Messages demonstrates the same condition written three
ways — as an error (a fact), a warning (a possibility), information — and
adds *"don't use the terms 'warning' or 'caution' in the text."*

### Visual Studio
`VS-UX` splits by whether the user must act now (synchronous) or not
(asynchronous), which is a second axis over the same three types.

### Interpretation

Three message types, plus two orthogonal questions — must the user act, and
is work blocked — generate every distinction the sources actually draw. A
longer taxonomy would be invented. Confirmation is a fourth thing: it is a
question, not a report, and `WIN7-TEXT` Confirmations treats it separately.
Fatal failure is a fifth only because its recovery differs (the product
cannot continue), not because its wording differs.

### Proposed rule
`UX-ERR-002`, with five classes: information, status, warning, error
(recoverable or blocking), and confirmation as a question. Each is defined by
attention required, blocking, surface and expected action, as the sources
define them.

### Confidence
HIGH for the three message types (`W32-CTRL`, verbatim). MEDIUM for the
blocking/recoverable split, which is `VS-UX`'s axis applied to Microsoft's
types.

---

## Q7. How short is too short?

### Google
`GERR` *Be concise*: *"Write concise error messages. Emphasize what's
important. Cut unnecessary text."* With the limit stated immediately: *"In
your enthusiasm to be concise, don't remove so many words that the resulting
error message becomes cryptic"* — the example of going too far is reducing a
message to *"Unsupported."* Its worked exercise shortens *"The SiteID
<SiteID> you have entered is invalid"* to *"Invalid SiteID <SiteID>"*, five
words removed.

### Microsoft
`WIN7-TEXT` Error Messages: *"Brief. The message is as short as possible, but
no shorter"*; supplemental instructions *"aim for a maximum of three sentences
of moderate length"*. `W32-CTRL` Tooltips: *"keep tooltips brief typically
five words or less but prefer specific labels over vague ones"*, and infotips
*"Be concise. Use 25 words or less. Longer infotips discourage reading."*
`W32-CTRL` Status Bars: *"Generally, use concise labels. Cut any text that
can be eliminated."* `WIN7-TEXT` Notifications gives 48 and 200 characters
for a notification title and body.

### GOV.UK
`GOVUK-WG` Use clear language: 25 words per sentence, 5 sentences per
paragraph — for web content.

### Books
`JM3` Ch. 6, *Much of the Text in Apps and Websites is Unnecessary*:
*"Minimize the amount of prose text in a user interface … In instructions,
use the least amount of text that gets most users to their intended goals."*
And the operational instruction, attributed to Krug: *"Before releasing an app
or a website, go through every screen and cut the amount of text by at least
half. Then go through the screens again and cut another 50%."*

### Interpretation

There is no single number, and the sources that give numbers give them per
surface: five words for a tooltip, 25 for an infotip, three sentences for
supplemental error text, 48/200 characters for a notification. The general
rule is a procedure, not a count — cut, then cut again, then stop at the point
where removing another word would remove meaning. Google marks that point
precisely: cryptic is a failure too.

### Proposed rules
`UX-TEXT-009` (the deletion test) as the general rule; `UX-TEXT-014` collects
the per-surface numbers the sources give and marks the project's own ceilings
as PROJECT CONVENTION, clearly separated.

### Confidence
HIGH for the per-surface numbers, which are quoted. The project budgets are
policy and are labelled as such.

---

## Q8. Does an expert audience want the raw diagnostic in the message?

### Google
`GERR` *Target audience* is the only source read that addresses this
directly. *"Tailor the error message to the target audience … Be mindful of
what the target audience knows and doesn't know."* It names the failure:
*"Beware of the curse of knowledge when writing error messages. A term
familiar to you might not be familiar to your target audience."* Its example
message *"Exploding gradient problem. To fix this problem, consider gradient
clipping"* is marked *"Recommended for ML experts only"*. Its exercise makes
the same message right for engineers and wrong for people uploading receipts.

### Microsoft
`WIN7-TEXT` Error Messages asks the routing question first: *"Are the primary
target users IT professionals? If so, consider using an alternative feedback
mechanism, such as log file entries … IT professionals strongly prefer log
files for non-critical information."* `W32-CTRL` Progress Bars, quoted in Q1,
says debugging detail does not belong in release builds.

### CLI
`CLIG` Output: *"By default, don't output information that's only
understandable by the creators of the software … only in verbose mode."* The
audience is developers by definition, and the answer is still "not by
default, but one flag away".

### Interpretation

Expertise changes the *vocabulary* a message may use. It does not change
whether raw diagnostics belong on the face of the message. The distinction
the sources draw is between what the reader knows and what the reader needs
at this moment: `CLIG`'s verbose flag, Microsoft's log file, Google's
audience-appropriate terminology. All three keep the detail one deliberate
step away.

This supports separating two states of the same person. Someone competent to
read a protocol trace is not, at this moment, necessarily reading one; they
may be halfway through an unrelated task. No source states this split in those
words, so the rule that draws it is DERIVED.

### Proposed rules
`UX-TEXT-016` (audience vocabulary, SOURCE), `UX-ERR-023` (working versus
debugging, DERIVED), `UX-ERR-008` (the disclosure that serves both).

### Confidence
HIGH for audience-appropriate vocabulary. MEDIUM for the working/debugging
split, which is a reasoned extension.

---

## Q9. Describe the implementation, or the task?

### Microsoft
`WIN7-TEXT` Error Messages names the leading cause of incomprehensible
messages: *"explaining the problem from the code's point of view instead of
the user's."*

### Nielsen Norman Group
`NNG-ERR`: *"beware of excessive technical precision and accuracy that can
undermine understandability. The user's mental model of how the system works
likely differs from the conceptual model of how it was coded."*

### Google
`GERR` *Be concise* prefers *"Can't connect to the SQL database"* over
*"Unable to establish connection to the SQL database"*, and *"Resource <name>
isn't in cluster <name>"* over *"The resource was not found and cannot be
differentiated."*

### Books
`AF4` Ch. 21: *"most error messages simply report when the application gets
confused"*, and users *"don't see the technical rationale behind an error
message. All they see is the application's unwillingness to deal with things
in a human way."*

### Interpretation

Unanimous. The message names the object the user was working on and what
became of it; the machinery that detected the condition is a different fact
for a different reader. This is the translation layer the brief asks for, and
it is what makes a structured internal error model useful: the same condition
must be renderable as one sentence for the operator and as a full diagnostic
for the log.

### Proposed rules
`UX-TEXT-015` (task and object), `UX-ERR-010` (never render UI text from an
exception string), `UX-ERR-011` (structured error model).

### Confidence
HIGH for the writing rule. `UX-ERR-011` is DERIVED: no source read prescribes
an error data structure. It is stated as a writing requirement with an
architectural consequence, not as a framework.

---

## Q10. When is confirmation justified, and what should its buttons say?

### Microsoft
`MS-COMMAND` (core, `corpus/platform/`): confirm actions that *"can't be
undone and have major consequences"*; otherwise *"offering a simple undo
command is usually enough"*, and confirmations *"are a hindrance whenever the
user is trying to perform an action intentionally."* `WIN7-TEXT`
Confirmations, *Make confirmations require thought*: where the reason not to
proceed is not obvious, add *anyway* to the proceeding button, or use
Yes/No, which *"forces users to at least read the main instruction."*
`W32-CTRL` Command Buttons and `WIN7-TEXT` UI Text: *"for windows used to
perform one specific task, use a specific label instead that starts with a
verb"*; *"use Yes and No buttons only to respond to yes or no questions"*;
*"Don't use OK for error messages, because this wording implies that problems
are OK."*

### Books
`AF4` Ch. 21, *Confirmations: the dialog that cried wolf*, supplies the
mechanism the platform sources assume: *"confirmations … work only when they
are unexpected … If confirmations are offered in routine places, users
quickly become inured to them and routinely dismiss them without a glance."*
Hence the test: *"For confirmation dialogs to work, they must appear only
when the user will almost definitely click the No or Cancel button. They
should never appear when the user is likely to click the Yes or OK button."*
Its alternatives are stated as principles: *"Do, don't ask"* and *"Make all
actions reversible."*

`JM3` Ch. 15 supplies the cognitive reason — a familiar dialog is dismissed
by a practised motor sequence, a capture slip.

### Interpretation

Cooper's test is the sharpest instrument in the corpus and is compatible with
Microsoft's rule: if the reader will almost certainly proceed, the
confirmation is protecting nobody and training them to dismiss the next one.
Microsoft supplies what to do when a confirmation is genuinely warranted —
name the action in the button, force reading with *anyway* or a real
question.

### Proposed rules
`UX-ERR-016` (when), `UX-ERR-017` (destructive wording), `UX-ERR-013` (action
labels), extending core `UI-DLG-003`, `UI-DLG-005` and module `UI-TEXT-012`.

### Confidence
HIGH.

---

## Q11. What should status and progress text say?

### Microsoft
`W32-CTRL` Progress Bars: *"Use a concise label … Start the label with a verb
(for example, Copying) and end with an ellipsis"*; *"Make estimates accurate,
but don't give false precision. If largest unit is hours, give minutes (if
meaningful) but not seconds"*; *"Don't give the percentage completed or
remaining because that information is conveyed by the progress bar itself"*;
*"Clearly indicate lack of progress"*; *"Don't restart progress"*; *"Don't
back up progress."* On the Cancel/Stop distinction: *"Label the button Cancel
if canceling returns the environment to its previous state (leaving no side
effects), otherwise label the button Stop to indicate that it leaves the
partially completed operation intact."*

`W32-CTRL` Status Bars: *"Don't change status too frequently. Status bar
icons shouldn't appear noisy, unstable, or demand attention. The eye is
sensitive to changes in the peripheral field of vision, so status changes need
to be subtle."* And *"Prefer sentence fragments, without ending
punctuation."*

### Visual Studio
`VS-UX`: progress indicators are for processes *"that take more than a few
seconds"*, and the choice depends on timing, modality, persistence and
whether progress is determinate.

### Books
`JM3` Ch. 5 supplies the reason the status bar rule works: peripheral vision
is poor, so a change far from the user's gaze is nearly invisible — which is
both why status must be subtle and why it cannot carry anything critical.

### Interpretation

Status text names the activity, not the mechanism, and changes no faster than
it can be read. False precision is a specific failure with a specific
remedy. The duplicated-percentage rule generalises: never state in words what
an adjacent control already states.

### Proposed rules
`UX-TEXT-024` (status), `UX-TEXT-025` (progress), `UX-TEXT-010`
(no duplication), `UX-ERR-013` (Cancel versus Stop).

### Confidence
HIGH; all quoted.

---

## Q12. Should success be announced?

### Microsoft
`WIN7-TEXT` Notifications, *What to notify*: *"don't notify of successful
operations"*, excepting security-relevant success, success after a recent
failure, and success in an unexpected form; *"assume that users take
successful operations for granted."*

### Books
`AF4` Ch. 21 on the synchronisation dialog: *"It announces that the
application successfully completed a synchronization — its sole reason for
existence … Do we really need the application to waste our time demanding
recognition that it managed to do its job?"*

### CLI
`CLIG` Output: *"Display output on success, but keep it brief … it's usually
best to err on the side of less"*, but also *"If you change state, tell the
user"* when the result does not map to the request.

### Interpretation

Not a contradiction: the terminal has no persistent surface, so a state
change leaves no trace unless printed, whereas a GUI can show the new state
itself. The rule is the same underneath — announce a change the reader cannot
otherwise see, and never announce that a requested, visible thing worked.

### Proposed rule
`UX-TEXT-026`, and `UI-TEXT-015` already carries the wording half.

### Confidence
HIGH.

---

## Q13. How consistent must terminology be?

### Google
`GERR` *Use terminology consistently*: *"If you call something a 'datastore'
in one error message, then call the same thing a 'datastore' in all the
other error messages."* With the warning that makes it an LLM problem:
*"Some authoring systems automatically recommend synonyms to ensure that you
don't keep repeating the same word. Yes, variety spices up paragraphs.
However, variety in error messages can confuse users."* And: *"the same
problem must generate the same error message."*

### Microsoft
`WIN7-TEXT` Style and Tone, *Be consistent*: *"consistent terminology
promotes learning … inconsistency forces users to figure out whether
different words and actions mean the same thing"*, with the examples
*switch/toggle* and *start/run/launch/boot/execute*. `MS-STYLE`: *"use one
term consistently to represent one concept."*

### Books
`JM3` Ch. 11, *We Learn Faster When Vocabulary Is Task Focused, Familiar, and
Consistent*: terminology should be task-focused, familiar and consistent, and
*"if they are looking for a Search function but it is labeled 'Query' on the
current screen or page, they may miss it."*

### Interpretation

Three sources, one rule, and Google names precisely the mechanism by which a
language model breaks it: a generator rewards variation, and variation here
is a defect. This is the justification for a controlled vocabulary file
rather than a style note.

### Proposed rules
`UX-TEXT-017` and `TERMINOLOGY.md`.

### Confidence
HIGH.

---

## Q14. Are numeric copy budgets defensible?

### Evidence
The sources give numbers only per surface, and only these: three sentences of
supplemental error text and one sentence for a main instruction
(`WIN7-TEXT`); five words for a tooltip and 25 for an infotip (`W32-CTRL`);
48 and 200 characters for a notification title and body (`WIN7-TEXT`); 25
words per sentence and 5 sentences per paragraph for web content
(`GOVUK-WG`). No source gives a general ceiling for a dialog, and
`UI_SOURCE_MATRIX.md` already records that as a known gap.

### Interpretation

A project may set tighter budgets, and for constraining a generator it
probably should. But a budget the sources do not supply is policy. The
honest treatment is to quote the sourced numbers as rules, state the project
numbers separately as PROJECT CONVENTION, and never present the second kind
as the first.

### Proposed rule
`UX-TEXT-014`, split explicitly into a sourced half and a policy half.

### Confidence
HIGH that the split is necessary; the policy values themselves carry no
source and say so.

---

## Q15. What does the corpus say about text produced by a generator?

### Evidence
No source read studies text generated by a language model; none could, given
their dates. But several describe the failure modes directly:

- `GSTYLE` Voice and tone rejects *"Placeholder phrases like please note and
  at this time"*, *"Choppy or long-winded sentences"*, *"Starting all
  sentences with the same phrase"*, and *"Using phrases like simply, It's that
  simple, It's easy, or quickly in a procedure."*
- `WIN7-TEXT` UI Text: *"too much text discourages reading; the eye tends to
  skip right over it — ironically resulting in less communication rather than
  more."*
- `JM3` Ch. 6 lists *"information buried in repetition"* among the things
  that disrupt reading, and asks for text to be halved twice.
- `GERR` *Use terminology consistently* warns against automatic synonym
  suggestion, quoted in Q13.
- `W32-CTRL` Tooltips: *"Don't just repeat or give a wordy restatement of
  what is already in the label"*, and *"Don't use language that sounds like
  marketing."*
- `AF4` Ch. 21: alerts that announce the obvious, and messages that are
  *"unnecessarily obsequious"*.

### Interpretation

Every characteristic pattern of generated UI text — padding phrases, narrated
reasoning, restated titles, synonym drift, helpful-sounding filler, marketing
register — is already named as a defect by at least one source, for reasons
that have nothing to do with how the text was produced. The anti-pattern
catalogue can therefore be grounded rather than asserted. What is new is only
the *frequency*: a generator produces these patterns by default, so the rules
must be stated as tests a reviewer can run, not as tastes.

### Proposed rules
`AP-31` … `AP-39` in `UX_WRITING_ORACLE.md` §E, each citing the source that
rejects the pattern.

### Confidence
HIGH for each individual pattern. The claim that generators produce them
disproportionately is an observation of this project's own experience and is
labelled PROJECT CONVENTION where it drives a rule.

---

## Known gaps

1. **Apple.** Not obtained in any static form. No Apple rule exists here.
2. **The three UX-writing books** named in the brief are not in the corpus.
3. **Material and Android.** `m3.material.io` and the Material 2 archive are
   JavaScript applications and the Android writing pages 404. Google is
   represented instead by its developer documentation style guide and its
   error-message course, both server-rendered and CC BY 4.0. Material-specific
   surfaces (snackbar, toast) are therefore ungrounded and no rule names them.
4. **Empty states.** No source read gives dedicated guidance. `UX-TEXT-027`
   is DERIVED from the concision and action rules and says so.
5. **Settings descriptions.** Closest evidence is `W32-CTRL`'s Control Panel
   infotips ("be specific", "25 words or less", "start with a present-tense
   imperative verb"). `UX-TEXT-028` is VERIFIED WITH QUALIFICATION on that
   basis.
6. **A general dialog length ceiling.** Still unsourced; still recorded.
