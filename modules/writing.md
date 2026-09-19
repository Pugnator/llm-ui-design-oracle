# Domain module: writing — the words on the screen

**Module ID:** `writing`
**Requires:** UI Oracle core >= 3.0.0
**Status:** stable
**Opt in:** list `writing` under `modules` in your project profile. Doing so
binds `UI-ERR-001`'s writing standard to this module (see `UI-ERR-001`,
"Project binding").

Rule IDs in this module use the `UI-TEXT-` prefix, reserved for it by the core
(`UI_ORACLE_CONTRACT.md`, namespace table).

---

## Why a module and not more core rules

The core has one rule about words (`UI-ERR-001`) and it defers to "a stricter
writing standard" the project may name. Until 3.0.0 no project could name one
without writing it, so every project either wrote its own or had none. This is
the standard, so it can be named.

It is a module rather than core because it is **prescriptive about wording**
in a way the rest of the oracle is not about layout: it names words to avoid,
a sentence shape for a problem report, a ceiling on length. Those are things a
project may have a house style about already. Opting in says "we have not, and
we will use this one".

## The sources, and how they were reconciled

Five bodies of guidance were read in full for this module (the text is
archived under `corpus/writing/`, each file headed with its URL, fetch date
and licence). They were written for four different media — a government web
service, a Windows desktop application, Microsoft's documentation, and the
command line — and they agree far more than they differ:

| Source | Medium | Tier | What it contributes |
|---|---|---|---|
| `GOVUK-DS` GOV.UK Design System: error message, error summary, notification banner, warning text, details, button, validation, "there is a problem with the service", "service unavailable", confirmation pages | Public web service | 2 | The most specific and most research-tested rules on error wording: instruction-or-description, no "please", no "sorry", no "valid"/"invalid", match the message to the label, the same words everywhere the same error appears |
| `GOVUK-WG` GOV.UK writing guidelines: clear language, right tone, clear structure, clear titles, summaries, meet user needs | Public web content | 2 | Plain-English mandate with literacy data behind it; the finding that **specialists prefer plain English more**, not less; frontloading; sentence and paragraph ceilings |
| `MS-WRITING` Windows apps design: Writing style | Windows desktop apps | 1 | The three voice principles; lead with what matters; active voice; "short and sweet" with a before/after; the dialog title-to-buttons "call and response"; button text as verb |
| `WIN7-TEXT` Win32 UX Guide: Error messages, Warning messages, Confirmations, Notifications, User interface text, Style and tone | Windows desktop apps (Windows 7) | 3, retained as `STILL_VALID_INTERACTION_PRINCIPLE` | The anatomy of a message — problem, cause, solution; the scan order users actually read a window in; the inverted pyramid; the do-not-use word list; the three-sentence ceiling on supplemental text; commit-button semantics (Close not OK for a problem); progressive disclosure for detail only when it is detail |
| `MS-STYLE` Microsoft Writing Style Guide: top 10 tips, brand voice, simple words, capitalization, verbs, scannable content, describing UI interactions, numbers, step-by-step instructions, bias-free communication | Documentation and UI | 1 | Sentence-style capitalisation as the default; passive voice **specifically** to avoid blame in errors; input-neutral verbs ("select", not "click"); numerals in UI; parallel structure |
| `CLIG` Command Line Interface Guidelines | Command line | 2 | "Catch errors and rewrite them for humans"; signal-to-noise; suggest the next command; if you change state, say so; debug output only in verbose mode — and one rule that does **not** transfer to a GUI (`C13`) |

Where they disagree, the disagreement is recorded in `UI_CONFLICTS.md` (C13,
C14, C15) and the rule below says which way it went. Where a source's numeric
value is used (a sentence count, a character count) it is quoted exactly and
attributed, per the contract.

The Win32 pages self-identify as Windows 7 guidance not updated since. Their
visual and component advice is `VISUALLY_OBSOLETE` and is not used here. Their
advice about **what a sentence should say** is not tied to a visual style, is
consistent with every current source read, and is retained as
`STILL_VALID_INTERACTION_PRINCIPLE` — the same treatment the core gives
`WIN7-DIALOGS`.

---

## What this module is about

Every string an operator reads: message titles and bodies, button labels,
control labels, status text, tooltips, log lines shown on screen, empty-state
text. It is not about documentation, and it is not about the log *file*, which
is a transcript for a different reader (`UI-TEXT-011`).

The organising idea, stated independently by every source: **people do not
read interface text, they scan it, and they stop the moment they have decided
what to do.** Win32 UI Text gives the scan order — controls in the centre,
commit buttons, other controls, main instruction, supplemental text, window
title, other static text, footnotes — and says "once users have decided what
to do, they will immediately stop reading and do it". GOV.UK gives the
number: most people read 20–28% of the words on a page. Johnson Ch. 6 says
the same from the cognitive side. Every rule below is a consequence of that.

---

## A. What a message is for

### UI-TEXT-001 — A problem report has three parts, in this order, and nothing else
**Level:** MUST **Authority:** Tier 1 + Tier 2 + Tier 3 **Confidence:** HIGH
**Provenance:** SOURCE RULE

A message reporting a problem MUST say, in this order: **what happened**;
**what it means for the operator** (only if not obvious from the first);
**what to do** (only if there is something to do). It MUST NOT contain
anything else on its face — no rationale, no history, no internal state, no
apology, no reassurance.

**Rationale.** Win32 Error Messages: a good error has "a problem, a cause, a
solution", is "brief — as short as possible, but no shorter", and its
supplemental text should "aim for a maximum of three sentences of moderate
length". GOV.UK Error message: "describe what has happened and tell them how
to fix it … get to the point"; do not repeat an example already on screen.
`MS-WRITING`: "lead with what's important … don't pad your words with
unnecessary introductions". `MS-STYLE` brand voice: "give people just enough
information to make decisions confidently"; top 10: "prune every excess
word." `CLIG`, Errors: "signal-to-noise ratio is crucial. The more irrelevant
output you produce, the longer it's going to take the user to figure out what
they did wrong."

The ceiling matters more than the order. A message with the right three parts
and two extra sentences of context has become a paragraph, and the scan-order
evidence says a paragraph is not read.

**Sources.** `WIN7-TEXT` Error Messages (The characteristics of good error
messages; Supplemental instructions); `GOVUK-DS` Error message (Be clear and
concise); `MS-WRITING` (Lead with what's important; Short and sweet);
`MS-STYLE` Brand voice, Top 10 tips; `CLIG` Errors.

**Review test.** Count the sentences. Label each *happened / means / do*.
Anything unlabelled goes. Anything after the third sentence goes into
progressive disclosure (`UI-TEXT-008`) or out.

---

### UI-TEXT-002 — Say the specific thing, not the category
**Level:** MUST **Authority:** Tier 2 + Tier 3 **Confidence:** HIGH
**Provenance:** SOURCE RULE

A message MUST name the specific object, value, place or condition involved.
It MUST NOT report a category where the specific case is known.

**Rationale.** Win32 Error Messages: "be specific … provide specific names,
locations, and values of the objects involved", against *"File not found. Disk
is full. Value out of range."*; and "don't rely on a single error message to
report a problem with several different detectable causes" — if the program
can tell which, it must say which, rather than make the operator
troubleshoot. GOV.UK Error message, "Be specific": *"An error occurred"*,
*"Select an option"*, *"This field is required"* "do not make sense out of
context"; empty, too long, too short and wrong format are different errors and
"an error for a specific situation is more helpful". `MS-STYLE` top 10 gives
the before/after: *"Invalid ID"* → *"You need an ID that looks like this:
someone@example.com"*.

The corollary both sources state: when the program genuinely does not know,
say that plainly rather than guess. Win32: "it is better to be up front about
the lack of information than to present problems, causes, or solutions that
might not be right."

**Sources.** `WIN7-TEXT` Error Messages (Text › Be specific; Troubleshooting;
Handling unknown errors); `GOVUK-DS` Error message (Be specific; Use
instructions and descriptions); `MS-STYLE` Top 10 tips (Write like you
speak).

**Review test.** Could this exact message appear for two different underlying
causes? If so, and the program can tell them apart, it is two messages.

---

### UI-TEXT-003 — Blame the problem, never the person
**Level:** MUST **Authority:** Tier 1 + Tier 2 + Tier 3 **Confidence:** HIGH
**Provenance:** SOURCE RULE

A message MUST NOT accuse, and MUST NOT use words that carry a verdict on the
operator. Specifically it MUST NOT use: *error, failure, failed to, illegal,
invalid, bad, forbidden, prohibited, you forgot, abort, kill, terminate,
catastrophic, fatal*. Where an active sentence would put the operator as the
subject of a mistake, the passive is the right choice and is the one place
this module prefers it.

**Rationale.** This is the one point every source states in its own words.
Win32 Error Messages lists the words, with replacements: *error/failure* →
*problem*; *failed to* → *unable to*; *illegal/invalid/bad* → *incorrect*;
*abort/kill/terminate* → *stop*; *catastrophic/fatal* → *serious*; and:
"don't use phrasing that blames the user or implies user error … use the
passive voice when the user is the subject and might feel blamed for the error
if the active voice were used". GOV.UK Error message: do not use *"words like 'forbidden', 'illegal', 'you
forgot' and 'prohibited'"*, nor *"valid and invalid because they do
not add anything to the message"*. `MS-WRITING`: "more than anything else,
it's important that your error message doesn't blame the user". `MS-STYLE`
Verbs lists, as the first use of the passive: "avoiding condescending text or
blaming the customer, especially in errors, warnings, or notifications",
example *"That site can't be found."* `CLIG` Philosophy: "at worst, it's a
hostile conversation which makes them feel stupid and resentful". Johnson Ch.
15 and Norman Ch. 5 supply the reason the core already cites in
`UI-ERR-002`/`UI-ERR-003`: most "user error" is design-caused and framing it
as the user's teaches nothing.

The word list is not decoration. *Error* and *invalid* are the two most common
words in messages that fail this rule, and each source rejects them for a
different reason that happens to be right: Win32 because the icon already
says it, GOV.UK because they add nothing, and both because they read as a
verdict.

**Sources.** `WIN7-TEXT` Error Messages (Text › General, the word list;
blaming); `GOVUK-DS` Error message (Be clear and concise); `MS-WRITING` (Error
messages); `MS-STYLE` Verbs (Active and passive voice); `CLIG` Philosophy
(Conversation as the norm); core `UI-ERR-002`, `UI-ERR-003`.

**Review test.** Search the string table for the listed words. Then read each
message as if you had just done the thing it reports — does it sound like an
accusation?

---

### UI-TEXT-004 — "Please" and "sorry" are for the operator's cost, not for tone
**Level:** SHOULD **Authority:** Tier 2 + Tier 3 **Confidence:** HIGH
**Provenance:** SOURCE RULE, resolving `C14`

A message SHOULD NOT say *please*, except where it asks the operator to bear an
inconvenience the software has caused (waiting; repeating work). It SHOULD
NOT say *sorry*, except where the operator has lost something — data, time
that cannot be recovered, the ability to continue. Neither word is ever
softening.

**Rationale.** The sources take different positions and the difference is
instructive. GOV.UK Error message: do not use *"please"* "because it implies
a choice", nor *"sorry"* "because it does not help fix the problem"; the
writing guidelines: "there's usually no need to say 'please' or 'please note'".
Win32 Style and Tone and Error Messages: "limit please to situations that
inconvenience the user in some way"; "use sorry only in error messages that
result in serious problems for the user (for example, data loss …). Don't
apologize if the issue occurred during the normal functioning of the
program." GOV.UK's own service-problem pages are titled *"Sorry, there is a
problem with the service"* — the serious case, where the service has failed
the person.

Read together these are one rule with two halves: the default is neither word,
and the exception is cost borne by the operator. That is `C14`'s resolution.

**Sources.** `GOVUK-DS` Error message; `GOVUK-WG` Use the right tone;
`WIN7-TEXT` Style and Tone (Attitude toward the user), Error Messages (Text);
`GOVUK-DS` There is a problem with the service pages (as the exception in
use). `UI_CONFLICTS.md` C14.

**Review test.** For each *please*: what is the operator being asked to put
up with? For each *sorry*: what did they lose? No answer, no word.

---

### UI-TEXT-005 — Match the words to the severity, and the severity to the words
**Level:** MUST **Authority:** Tier 3 + Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

The wording of a message MUST agree with its kind: a **problem** is phrased as
something that has happened; a **warning** as a condition that may cause a
problem; **information** as a statement of fact; a **confirmation** as a
question. The kind chosen MUST be the one the situation is, and the icon,
colour and container MUST match the words.

**Rationale.** Win32 gives the same condition three ways — *"This page cannot
load an unsigned ActiveX control"* (error, a fact), *"This page might not
behave as expected because…"* (warning, a possibility), *"You have configured
… to block…"* (information) — and says "the main instruction text and icons
should always match" and "don't use warning icons for errors … errors aren't
warnings". Warnings: "don't use the terms 'warning' or 'caution' in the text.
When used correctly, the warning icon sufficiently communicates" it. GOV.UK:
do not use error messages "to tell a user that they are not eligible … or to
tell them about a lack of capacity or other problem the user cannot fix —
because the problem is with the service rather than with the information the
user has provided"; and do not use "red text to warn people" on a
service-problem page. Core `UI-COLOR-003` already requires the words to carry
the meaning without the colour; this rule requires the colour not to
contradict the words.

**Sources.** `WIN7-TEXT` Error Messages (Determine the appropriate message
type; Icons), Warning Messages (Determine the appropriate message type; Text);
`GOVUK-DS` Error message (When not to use), There is a problem with the
service pages; core `UI-COLOR-003`.

**Review test.** Cover the icon. Can you tell from the words alone whether
this has happened, might happen, or is a question? Uncover it: does it agree?

---

## B. How it is said

### UI-TEXT-006 — Plain words, and the specialist wants them more
**Level:** MUST **Authority:** Tier 2 + Tier 1 **Confidence:** HIGH
**Provenance:** SOURCE RULE

Interface text MUST use the everyday word where one exists, MUST NOT use a
term the operator would not use themselves without explaining it in place,
and MUST NOT lean on the operator's expertise as a licence for jargon.

**Rationale.** GOV.UK writing guidelines cite the research directly: "the
more educated the person and the more specialist their knowledge, the greater
their preference for plain English … some users can understand complex
specialist language, but they do not want to read it if there's an
alternative." And: "where you need to use specialist terms, you can … you just
need to explain what they mean the first time you use them." `MS-STYLE`: "use
simple words with precise meanings" — *use* not *utilize*, *remove* not
*extract*, *tell* not *inform*; brand voice: "shun jargon and acronyms".
Win32 Style and Tone: "use everyday words when you can and avoid words you
wouldn't say to someone else in person"; Microsoft's own research finding
"overuse of computer terminology and jargon, which many users don't
understand or misinterpret". `MS-WRITING`: "don't use terms they won't
understand". GOV.UK Error message: no *"form post error"*, *"unspecified
error"*, *"error 0x0000000643"*.

This is the rule that decides what to do with a transport's own words. They
are evidence (`UI-TEXT-008`), not the message.

**Sources.** `GOVUK-WG` Use clear language (Write clearly for specialists
too; Use specialist language if needed); `MS-STYLE` Use simple words, concise
sentences; Brand voice; `WIN7-TEXT` Style and Tone (Use real-world language);
`MS-WRITING` (Be crisp and clear); `GOVUK-DS` Error message.

**Review test.** Read it aloud to someone who does not work on the product
(GOV.UK's own test: "read the message out loud to see if it sounds like
something you would say"). Every word they would not say is a candidate.

---

### UI-TEXT-007 — Active voice, present tense, instruction as imperative
**Level:** SHOULD **Authority:** Tier 1 + Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

Interface text SHOULD use the active voice and the present tense. An
instruction SHOULD be an imperative that starts with the verb. The exception
is `UI-TEXT-003`, which takes precedence: where the active voice would make
the operator the subject of a mistake, use the passive (`C15`).

**Rationale.** `MS-WRITING`: "make sure your text uses the active voice
throughout your app" — *"Restart the app to see your changes"* over *"The
changes will be applied when the app is restarted"*. `MS-STYLE` Verbs:
present tense "is often easier to read and understand than the past or future
tense"; imperative for "instructions, procedures, direct commands"; and the
enumerated passive exceptions. GOV.UK: "the active voice is more direct and
puts the focus on the user and the action they need to take. It also keeps
sentences short"; headings should be "active — for example, start them with a
verb". Win32 Error Messages: "use present tense whenever possible". GOV.UK
Error message on the two shapes: an instruction (*"Enter your first name"*)
for an empty field, a description (*"First name must be 35 characters or
less"*) for a wrong one — "use both instructions and descriptions, but use
them consistently".

**Sources.** `MS-WRITING` (Emphasize action); `MS-STYLE` Verbs; `GOVUK-WG`
Use clear language (Use the active voice), Create a clear structure (headings);
`WIN7-TEXT` Error Messages (Main instructions); `GOVUK-DS` Error message (Use
instructions and descriptions); `UI_CONFLICTS.md` C15.

**Review test.** Find the verb. Is it first? Is it in the present? Is the
subject the operator, the object, or an abstraction ("the operation")?

---

### UI-TEXT-008 — Detail is folded, evidence is kept, and neither is the message
**Level:** SHOULD **Authority:** Tier 3 + Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

Information that some operators need and most do not — a transport's own
error string, an error code, a path, a diagnostic — SHOULD be present and
SHOULD be behind a progressive-disclosure control, not on the face of the
message. It MUST NOT be the message. A progressive-disclosure control MUST
reveal something that is not already visible.

**Rationale.** Win32 Error Messages: "use a Show/Hide details progressive
disclosure button to hide advanced or detailed information in an error
message … don't hide needed information, because users might not find it";
"don't use Show/Hide details unless there really is more detail. Don't just
restate the existing information in a more verbose format"; error codes:
"always provide a text description of the problem and solution. Don't depend
just on the error code" — and choose codes "easily searchable on the
Internet". GOV.UK Details: "make a page easier to scan by letting users reveal
more detailed information only if they need it" — and do not use it "to hide
information that the majority of your users will need". `CLIG` Errors: "if
there is an unexpected or unexplainable error, provide debug and traceback
information … consider writing the debug log to a file instead of printing it
to the terminal". Core `UI-ERR-001` and `AP-17` already forbid the
implementation on screen; this rule says where it goes instead.

**Sources.** `WIN7-TEXT` Error Messages (Progressive disclosure; Error codes);
`GOVUK-DS` Details (When to use; When not to use); `CLIG` Errors; core
`UI-ERR-001`, `AP-17`.

**Review test.** Open the disclosure. Is what appears new? Close it. Does the
message still say what happened and what to do?

---

### UI-TEXT-009 — Sentence case, one space, and the punctuation the shape implies
**Level:** MUST **Authority:** Tier 1 **Confidence:** HIGH
**Provenance:** SOURCE RULE

Interface text MUST use sentence-style capitalisation. A complete sentence
ends with a full stop; a label, title, heading or button does not. A question
ends with a question mark wherever it appears. Interface text MUST NOT use
all-capitals for emphasis and MUST NOT use exclamation marks.

**Rationale.** `MS-STYLE` Capitalization: sentence-style for "a sentence,
heading, title, UI label (such as the name of a button or checkbox), or
standalone phrase"; "don't use all uppercase for emphasis"; top 10: "when in
doubt, don't capitalize … don't use title-style capitalization (Like This)";
"don't use a period or a colon at the end of titles, headings, subheadings,
and UI titles"; one space after a full stop. `MS-WRITING`: "use periods to
end full sentences in tooltips, error messages, and dialogs. Don't end text
for buttons, radio buttons, labels, or checkboxes with a period." Win32 UI
Text: "unlike periods, question marks are used for all types of text";
exclamation points — "in business applications, avoid"; capitals — "users
tend to regard it as 'screaming'"; keyboard keys as the keyboard labels them
(*Tab*, *Ctrl+Alt+Del*, not *TAB*). GOV.UK: "do not use block capitals for
large amounts of text. It's hard to read and it can be understood as
shouting." Core `UI-TYPO-004` already requires sentence case; this rule adds
the punctuation half.

The one Win32 exception — title-style capitalisation for dialog titles — is
Windows 7 practice; `MS-STYLE` is current and names titles among the things
that take sentence style. The current source governs.

**Sources.** `MS-STYLE` Capitalization; Top 10 tips; `MS-WRITING` (Periods;
Capitalization); `WIN7-TEXT` User Interface Text (Punctuation;
Capitalization); `GOVUK-WG` Use the right tone; core `UI-TYPO-004`.

**Review test.** Every string: is the first letter the only capital that is
not a proper noun? Does the terminal punctuation match whether it is a
sentence?

---

### UI-TEXT-010 — Numbers as an instrument would show them
**Level:** SHOULD **Authority:** Tier 1 **Confidence:** MEDIUM
**Provenance:** SOURCE RULE + DERIVED (the last clause)

A value on screen SHOULD be a numeral, not a word; SHOULD carry its unit;
SHOULD show a leading zero before a decimal fraction; and SHOULD NOT be shown
in a notation the operator's instruments would not use.

**Rationale.** `MS-STYLE` Numbers: "it's OK to use numerals for zero through
nine when you have limited space, such as in tables and UI"; use numerals for
"measurements of distance, temperature, volume, size, weight, pixels, points,
and so on — even if the number is less than 10"; "add a zero before the
decimal point for decimal fractions less than one"; in tables "align decimals
on the decimal point"; "in UI, avoid the abbreviations [K, M, B] unless space
is too limited to spell out the number". The last clause is derived: no
source read discusses scientific notation, because none imagined a message
writing `1.25e+03` for 1250 rpm. It follows from `UI-TEXT-006` — a form the
reader would not use is jargon — and is recorded as MEDIUM for that reason.

**Sources.** `MS-STYLE` Numbers (Numerals vs. words; Fractions and decimals;
Abbreviations); `UI-TEXT-006`.

**Review test.** Would this number, as written, appear on a gauge, a data
sheet or a workshop manual for the same quantity?

---

## C. Where it is said

### UI-TEXT-011 — The log is a transcript; the screen is a message
**Level:** SHOULD **Authority:** Tier 3 + Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

Text written for the log file SHOULD record what happened in full, with the
transport's own words. Text shown on screen SHOULD follow `UI-TEXT-001`. A
line SHOULD NOT be written once for both, because it will be right for
neither. Where a log is also shown on screen, the shown form is the message
form.

**Rationale.** Win32 Error Messages names the two audiences: "are the primary
target users IT professionals? If so, consider using an alternative feedback
mechanism, such as log file entries … IT professionals strongly prefer log
files for non-critical information"; and lists "log files (for errors targeted
at IT professionals)" among the presentations. `CLIG`: "don't treat stderr
like a log file, at least not by default. Don't print log level labels (ERR,
WARN, etc.) or extraneous contextual information, unless in verbose mode"; "by
default, don't output information that's only understandable by the creators
of the software … only in verbose mode"; and "hiding logs behind progress
bars when things go well makes it much easier for the user to understand
what's going on, but if there is an error, make sure you print out the logs".
Two readers, two forms.

**Sources.** `WIN7-TEXT` Error Messages (Is this the right user interface?;
Error message presentation); `CLIG` Output; Robustness.

**Review test.** Take the string shown in the dialog and the line written to
the file for the same event. Are they the same string? Then one audience is
being short-changed.

---

### UI-TEXT-012 — A dialog is a question and its buttons are the answers
**Level:** MUST **Authority:** Tier 1 + Tier 3 **Confidence:** HIGH
**Provenance:** SOURCE RULE

A dialog's title or main instruction MUST be the one thing it is asking or
telling. Its buttons MUST be specific answers to that, phrased as the action
each performs. A button MUST NOT be labelled *OK* on a problem, because that
says the problem is acceptable; the dismissing button on a problem is *Close*.
*Yes*/*No* MUST only answer a yes-or-no question, always as a pair.

**Rationale.** `MS-WRITING` Dialogs: "most important is the 'call and
response' between the title of a dialog and its buttons. Make sure that your
buttons are clear answers to the question posed by the title"; Buttons: "every
button represents an action. Be sure to use the active voice in button text".
GOV.UK Button: "write button text in sentence case, describing the action it
performs" — *Save and continue*, *Add another*, *Confirm and send*. Win32 UI
Text, commit buttons: "for windows used to perform one specific task, use a
specific label instead that starts with a verb"; "use Yes and No buttons only
to respond to yes or no questions. Never use OK and Cancel for yes or no
questions"; *Done* — "don't use. Done as a command is grammatically
incorrect". Win32 Error Messages: "provide a Close button. Don't use OK for
error messages, because this wording implies that problems are OK." Win32
Warnings: for an awareness warning, "Close. Don't use OK because it suggests
that potential problems are OK." Win32 Confirmations: where the reason not to
proceed is not obvious, add *anyway* to the proceeding button or use
*Yes*/*No*, which "forces users to at least read the main instruction". Core
`UI-DLG-002` already requires task-specific commit verbs on modeless surfaces;
this extends it to modal ones and adds the *OK*-on-a-problem prohibition.

**Sources.** `MS-WRITING` (Dialogs; Buttons); `GOVUK-DS` Button (How it
works); `WIN7-TEXT` User Interface Text (Commit button labels), Error Messages
(Commit buttons), Warning Messages (Commit buttons), Confirmations (Commit
buttons; Make confirmations require thought); core `UI-DLG-002`, `UI-DLG-004`.

**Review test.** Read the title, then each button, as a spoken exchange. Does
each button answer? Is *OK* answering a problem?

---

### UI-TEXT-013 — The same problem is the same words everywhere it appears
**Level:** MUST **Authority:** Tier 2 + Tier 3 **Confidence:** HIGH
**Provenance:** SOURCE RULE

Where one condition is reported in more than one place — a summary and an
inline message, a status bar and a dialog, a message and the label it refers
to — the wording MUST be the same, and MUST reuse the words of the label or
control it concerns. One concept MUST have one term across the product.

**Rationale.** GOV.UK Error summary: "make sure the error messages in the
error summary are worded the same as those which appear next to the inputs
with errors"; Error message, "Be consistent": the same message in both places
so they "look, sound and mean the same; make sense out of context; reduce the
cognitive effort needed to understand what has happened"; "Match up error
messages to labels": *"Address line 1"* → *"Enter address line 1"*. Win32
Style and Tone: "consistent terminology promotes learning … inconsistency
forces users to figure out whether different words and actions mean the same
thing" — *switch/toggle*, *start/run/launch/boot/execute*,
*enable/activate/turn on*. `MS-STYLE`: "use one term consistently to
represent one concept". `CLIG`: "don't have ambiguous or similarly-named
commands … 'update' and 'upgrade'". Core `UI-GLOBAL-003` requires consistent
commands; this is the same rule for the words about them.

**Sources.** `GOVUK-DS` Error summary (How it works), Error message (Be
consistent; Match up error messages to labels); `WIN7-TEXT` Style and Tone
(Be consistent); `MS-STYLE` Use simple words; `CLIG` Subcommands; core
`UI-GLOBAL-003`.

**Review test.** Pick one condition. List every place it is reported. Diff
the strings.

---

### UI-TEXT-014 — Input-neutral verbs, and the place before the action
**Level:** SHOULD **Authority:** Tier 1 **Confidence:** HIGH
**Provenance:** SOURCE RULE

An instruction that names an interaction SHOULD use a verb that is true for
every input method — *select*, *open*, *go to*, *enter*, *turn on*, *clear*,
*drag* — and SHOULD NOT use *click*, *tap*, *press*, *swipe* or *type* where a
neutral verb exists. Where the operator must first be somewhere, the place
comes before the verb.

**Rationale.** `MS-STYLE` Describing interactions with the UI: "use generic
verbs that work with any input method. Don't use input-specific verbs, such as
click or swipe", with the table of replacements — *select F5*, *select
Ctrl+Alt+Delete* are the given forms for keys. Writing step-by-step
instructions: "make sure that customers know where the action should take
place before you describe the action" — *"On the Design tab, select Header
Row."* Win32 Error Messages: "put the results before the action" — *"To
restart Windows, click OK"* not *"Click OK to restart Windows"* — because in
the second form "users are more likely to click OK by accident". Core
`UI-CMD-002` requires both a pointer and a keyboard path; wording that names
one of them contradicts the other.

**Sources.** `MS-STYLE` Describing interactions with the UI; Writing
step-by-step instructions (Tips for writing steps); `WIN7-TEXT` Error
Messages (Supplemental instructions); core `UI-CMD-002`.

**Review test.** Read the instruction with the mouse unplugged. Is it still
true? Read it with the keyboard unplugged.

---

### UI-TEXT-015 — Say what changed
**Level:** SHOULD **Authority:** Tier 2 **Confidence:** HIGH
**Provenance:** SOURCE RULE

When a command changes state that is not visible where the operator is
looking, the interface SHOULD say what changed — in the words of the result,
not of the request — and SHOULD name the thing to do next when there is one.
Success that is expected and visible SHOULD NOT be announced.

**Rationale.** `CLIG` Output: "if you change state, tell the user … so the
user can model the state of the system in their head — particularly if the
result doesn't directly map to what the user requested"; "suggest commands the
user should run"; and against the other extreme, "display output on success,
but keep it brief … it's usually best to err on the side of less". Win32
Notifications: "don't notify of successful operations, except" for security,
after a recent failure, or when success took an unexpected form; "assume that
users take successful operations for granted". GOV.UK Confirmation pages: a
completed transaction says "what happens next and when". GOV.UK Notification
banner: "there's evidence that people often miss them, and using them too
often is likely to make this problem worse". Core `UI-GLOBAL-005` and
`UI-FB-006` carry the visibility and modeless halves; this rule is about the
words.

**Sources.** `CLIG` Output (If you change state, tell the user; Suggest
commands the user should run; Display output on success); `WIN7-TEXT`
Notifications (What to notify); `GOVUK-DS` Confirmation pages, Notification
banner (When not to use); core `UI-GLOBAL-005`, `UI-FB-006`.

**Review test.** After the command, without moving, can the operator say what
is now true that was not? If it was obvious, was it announced anyway?

---

## What this module deliberately does not say

- **A word count for a dialog.** Win32 gives "a maximum of three sentences"
  for supplemental text and "a single, complete sentence" for the main
  instruction; GOV.UK gives 25 words per sentence and 5 sentences per
  paragraph for web content; Win32 Notifications gives 48 and 200 characters
  for a notification's title and body. Those are quoted in the rules that use
  them and are not generalised into one number, because no source gives one.
- **Tone beyond "not hostile".** `MS-WRITING` asks for "warm and relaxed";
  GOV.UK asks for "emotionless" and "brisk, but not terse". They disagree
  because their readers differ, and a professional tool's profile may pick
  either. The module requires only what they share: no blame, no jargon, no
  padding, no shouting.
- **Localisation.** Win32 UI Text and `MS-STYLE` both carry rules (30%
  expansion, no run-time string composition, whole-sentence links). They are
  real and they are out of scope here; a project that localises should read
  them.

---

## Anti-patterns this module adds

See `UI_ANTIPATTERNS.md` AP-23 to AP-26: the wall of text, the verdict word,
the apology as tone, and the transport as the message.

## Relationship to the writing oracle (5.0.0)

This module is the **sentence**: what a message says, in what order, in which
words. Two further documents sit above it and are cumulative with it, never
alternatives:

- `UX_WRITING_ORACLE.md` (`UX-TEXT-`) governs every string on every surface —
  register, concision, the reader's perspective, buttons, tooltips, status,
  progress, empty states, settings, validation — and catalogues the
  anti-patterns of generated text.
- `ERROR_MESSAGE_ORACLE.md` (`UX-ERR-`) governs the decisions made *before*
  wording: whether a condition is reported at all, what severity class it is,
  which surface it belongs on, and which of five layers each fact goes in.

Where they overlap, the stricter governs and the later document names the
`UI-TEXT-` rule it tightens. Nothing here is restated there.
