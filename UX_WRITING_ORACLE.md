# UX Writing Oracle

Rules for every string the product shows a person: message bodies and titles,
button labels, menu commands, control labels, tooltips, status and progress
text, notifications, empty states, settings descriptions, validation
messages, and the technical detail shown alongside any of them.

**Requires:** UI Oracle core >= 5.0.0. Error-specific rules live in
`ERROR_MESSAGE_ORACLE.md`; this file governs everything, including errors,
and the error oracle tightens it. Sentence-level mechanics — the three parts
of a problem report, the word list, voice, case, punctuation — remain in
`modules/writing.md` (`UI-TEXT-001` … `UI-TEXT-015`), which this file extends
rather than restates.

**Evidence:** `UX_COPY_EVIDENCE.md`. Every rule below names the question it
came from. Rule IDs use the `UX-TEXT-` prefix.

---

## How to use this file

**Generating text.** Write the shortest accurate version first, then apply
§B. Do not write a draft and trim it; the draft's shape survives trimming.

**Reviewing text.** Run `UI_COPY_REVIEW_CHECKLIST.md`. It is the procedure;
this file is the authority it cites.

**The one test that matters most.** For each sentence: *if this sentence were
removed, would the reader make a worse decision?* If no, it does not belong
in primary copy (`UX-TEXT-009`).

## Rule format

Each rule carries **Level**, **Class**, **Authority**, **Confidence**,
**Applicability**, **Source**, **Exceptions** and a **Review test**, per
`UI_ORACLE_CONTRACT.md` §9. Class is one of:

- **PLATFORM RULE** — a current platform requirement (Tier 1).
- **CONTENT-DESIGN PRINCIPLE** — stated by a content-design or HCI source
  (Tier 2/3/4), strong without being a platform requirement.
- **DERIVED RULE** — reasoned from sources that do not state it outright;
  the reasoning is shown.
- **PROJECT CONVENTION** — local policy. No source requires the chosen value.

A reviewer reports the class, because the four carry different weight when
someone pushes back.

---

# §A. Voice and tone

### UX-TEXT-001 — Write as a precise tool, not as a companion
**Level:** SHOULD **Class:** DERIVED RULE **Authority:** Tier 1 + Tier 2
**Confidence:** HIGH

Interface text SHOULD read as an instrument reporting a fact: plain, specific,
unhurried, without personality. The product's register is declared once in the
profile; for a professional tool it is this one.

**Rationale.** The sources disagree about warmth, and the disagreement tracks
the medium rather than quality (Q4). Google asks documentation to sound like
*"a knowledgeable friend"*, and on the same page warns that the reader *"may
be in a hurry"*; its error guidance is stricter. Microsoft asks for warmth in
app copy and, in the same company's desktop guidance, forbids marketing
register in tooltips. GOV.UK asks for text that is *"emotionless"*. A string
the operator did not choose to read is not the place to establish a
relationship.

**Applicability.** All surfaces. A consumer product may declare a warmer
register in its profile; the rest of this file still applies.

**Source.** `GSTYLE` Voice and tone; `MS-WRITING`; `GOVUK-WG` Use the right
tone; `W32-CTRL` Tooltips (*"Don't use language that sounds like
marketing"*). Q4.

**Exceptions.** Onboarding and marketing surfaces the reader opened
deliberately.

**Review test.** Read the string aloud in the voice of a multimeter. Does
anything sound out of place? That part is the personality.

---

### UX-TEXT-002 — No interjections, no exclamation marks, no jokes
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 1 + Tier 2 + Tier 3
**Confidence:** HIGH

Interface text MUST NOT open with an interjection — *Oops*, *Uh-oh*, *Whoops*,
*Aw snap*, *Great*, *Awesome*, *Perfect*, *Yay* — MUST NOT use exclamation
marks, and MUST NOT attempt humour.

**Rationale.** Three reasons, each from a source rather than from taste.
Google on humour: *"Errors frustrate users. Angry users are generally not
receptive to humor"*, *"Users can misinterpret humor"*, and *"Humor can
detract from the goal of the error message."* Google on punctuation: *"In
general, avoid exclamation points"*, alongside *"Being too cutesy"* and
*"Wackiness, zaniness, and goofiness"*. Win32 UI Text on exclamation points
in business applications: *"avoid"*. NN/g notes the decay: humour *"can
become stale if users encounter the error frequently"* — and interface text is
encountered repeatedly by definition.

*Oops!* fails for a further reason: it reports the writer's embarrassment
instead of the reader's situation, which is `UX-TEXT-015` as well.

**Applicability.** All surfaces. Strongest on anything the reader sees more
than once.

**Source.** `GERR` Set the tone; `GSTYLE` Voice and tone; `WIN7-TEXT` User
Interface Text (Punctuation); `NNG-ERR`. Q3.

**Exceptions.** One, narrow and recorded as conflict `C20`: a consumer
product's total-outage page, where NN/g permits novelty. A professional tool
reporting an operational condition is never this case.

**Review test.** Search the string table for `!`, *oops*, *uh-oh*, *whoops*,
*great*, *awesome*, *yay*. Every hit is a finding.

---

### UX-TEXT-003 — *Sorry* and *please* are reserved for the reader's cost
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 1 + Tier 2 + Tier 3
**Confidence:** HIGH

Text MUST NOT say *sorry* unless the reader has lost something — data, time
that cannot be recovered, the ability to continue — and MUST NOT say *please*
unless it is asking the reader to bear an inconvenience the software caused.
Neither word softens. *Unfortunately* is not an alternative; it is the same
move with more syllables.

**Rationale.** This is `UI-TEXT-004` with a fourth source. Google: *"avoid
the words 'sorry' or 'please'"*. GOV.UK: *please* *"implies a choice"*,
*sorry* *"does not help fix the problem"*. Win32: *please* limited to
*"situations that inconvenience the user"*, *sorry* to *"error messages that result in serious problems for the user"*
— the source instances data loss, being unable to continue, and needing help
from a technical representative — and *"Don't apologize if the issue occurred
during the normal functioning of the program."*

**Applicability.** All surfaces.

**Source.** `UI-TEXT-004`; `GERR` Set the tone; `GOVUK-DS` Error message;
`WIN7-TEXT` Style and Tone. `UI_CONFLICTS.md` C14, C20. Q3.

**Exceptions.** Google records that apology expectations differ by culture; a
localised product may follow its market. The default stands.

**Review test.** For each *sorry*: what did the reader lose? For each
*please*: what are they being asked to put up with? No answer, no word.

---

### UX-TEXT-004 — The software is not a person
**Level:** MUST **Class:** DERIVED RULE **Authority:** Tier 2 + Tier 4
**Confidence:** MEDIUM

Text MUST NOT give the software intentions, feelings or effort. Not *I could
not find*, not *we're working on it*, not *the app is trying to*, not *I
noticed that*. The product reports; it does not narrate its inner life.

**Rationale.** Cooper states the asymmetry that makes this matter:
*"Humans have emotions and feelings; applications don't."* He names the
resulting register — a dialog that is *"unnecessarily obsequious"*,
announcing *"that the application successfully completed a synchronization —
its sole reason for existence"* — and asks *"Do we really need the
application to waste our time demanding recognition that it managed to do its
job?"* Norman's account of blame attribution supplies the other half: a
system presented as an agent invites the reader to argue with it rather than
act.

MEDIUM because no source read states an anthropomorphism prohibition
directly; the rule is assembled from Cooper's observation and the register
rules above.

**Applicability.** All surfaces.

**Source.** `AF4` Ch. 21; `DOET-R` Ch. 5. Q4.

**Exceptions.** A product whose interface genuinely is a conversational
agent.

**Review test.** Find the grammatical subject of each sentence. If it is the
application, and the verb is a mental one, rewrite around the object.

---

### UX-TEXT-005 — Severity words match the severity
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 3
**Confidence:** HIGH

Text MUST NOT use *critical*, *fatal*, *severe*, *catastrophic*, *lost*,
*corrupted*, *destroyed* or *failed catastrophically* for a condition that is
routine, expected or recoverable. It MUST NOT use the words *warning*,
*caution* or *error* to label its own severity where a container or icon
already carries it.

**Rationale.** Win32 gives the same condition written three ways — as a fact,
as a possibility, as information — and requires the wording to match the type
chosen: *"the main instruction text and icons should always match"*, and
*"don't use warning icons for errors … errors aren't warnings."* On
self-labelling: *"don't use the terms 'warning' or 'caution' in the text. When
used correctly, the warning icon sufficiently communicates"* it. The word list
in `UI-TEXT-003` already bans *fatal* and *catastrophic* as verdicts; this
rule bans them as exaggeration.

A device that is not connected is not *lost*. An operation that ended in the
documented way did not *fail catastrophically*.

**Applicability.** All surfaces; most often violated in status text and logs
promoted to the screen.

**Source.** `W32-CTRL` Standard Icons; `WIN7-TEXT` Warning Messages;
`UI-TEXT-003`, `UI-TEXT-005`. Q6.

**Exceptions.** Conditions that genuinely are those things.

**Review test.** Ask what the reader loses if they ignore the message for ten
minutes. If the answer is "nothing", the severity words are wrong.

---

### UX-TEXT-006 — No reassurance, no marketing, no filler politeness
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 1 + Tier 3
**Confidence:** HIGH

Text MUST NOT include *Don't worry*, *No problem*, *Rest assured*, *as you may
know*, *simply*, *just*, *easy*, *quickly*, or phrases that praise the product.

**Rationale.** Google's avoid-list names the mechanism: *"Placeholder phrases
like please note and at this time"*, and *"Using phrases like simply, It's
that simple, It's easy, or quickly in a procedure"* — words that tell the
reader how they should feel about a task rather than how to do it, and that
read as condescension when the task then fails. Win32 on tooltips: *"Don't use
language that sounds like marketing."* Reassurance also competes for the
attention the actual instruction needs (`JM3` Ch. 6).

**Applicability.** All surfaces.

**Source.** `GSTYLE` Voice and tone; `W32-CTRL` Tooltips; `JM3` Ch. 6. Q15.

**Exceptions.** Naming a genuine safety fact is not reassurance: *Your
unsaved changes are kept* is information the reader can act on.

**Review test.** Delete the phrase. Did the reader lose a fact, or a feeling?

---

# §B. Concision

### UX-TEXT-007 — Knowing something is not a reason to show it
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 3 + Tier 2
**Confidence:** HIGH

Information MUST earn its place by changing what the reader understands or
does. That the program has the value at hand is not a reason to display it.

**Rationale.** Microsoft states this about progress detail and the reasoning
generalises: *"Generally users don't care about the details of the operation
being performed. For example, users of a setup program don't care about the
specific file being copied or that system components are being registered
because they have no expectations about these details … Providing details that
users don't care about makes the user experience overly complicated and
technical."* And decisively: *"provide additional progress information only if
users can do something with it."*

**Applicability.** All surfaces. This is the rule most often broken by
generated text, which treats available context as relevant context.

**Source.** `W32-CTRL` Progress Bars; `JM3` Ch. 6. Q1, Q7.

**Exceptions.** Values the reader must copy, quote or check — an identifier, a
measured figure, a path they will navigate to.

**Review test.** For each fact in the string: what would the reader do
differently without it? If nothing, cut it or move it to detail.

---

### UX-TEXT-008 — Cut twice
**Level:** SHOULD **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 2
**Confidence:** HIGH

Every string SHOULD be written, cut by half, and cut again, stopping at the
point where removing another word removes meaning.

**Rationale.** Johnson gives the procedure: *"Before releasing an app or a
website, go through every screen and cut the amount of text by at least half.
Then go through the screens again and cut another 50%."* Microsoft gives the
reason: *"too much text discourages reading; the eye tends to skip right over
it — ironically resulting in less communication rather than more."* Google
gives the floor in the same breath as the instruction: *"In your enthusiasm to
be concise, don't remove so many words that the resulting error message
becomes cryptic"* — its example of overshooting is the single word
*"Unsupported."*

**Applicability.** All surfaces.

**Source.** `JM3` Ch. 6; `WIN7-TEXT` User Interface Text; `GERR` Be concise.
Q7.

**Exceptions.** Legal and safety text with a required form.

**Review test.** Halve it. Is anything the reader needed now missing? If not,
the halved version is the string.

---

### UX-TEXT-009 — Remove non-actionable explanation
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 2 + Tier 3
**Confidence:** HIGH

Every sentence in primary copy MUST change what the reader understands or
does. A sentence that fails MUST be removed, moved behind disclosure, moved to
documentation, or moved to the log.

**Rationale.** This is the operative form of `UX-TEXT-007` and the test most
of this file reduces to. Microsoft requires an error to be *"Relevant"*, *"Actionable"*,
*"User-centered"* and *"Brief"* — the last glossed as *"The message is as
short as possible, but no shorter."* Google's course reduces the whole
subject to two questions, *"What went wrong?"* and *"How does the user fix
that problem?"*;
NN/g requires messages to *"Concisely and precisely describe the issue"* and
to *"Offer constructive advice"*. A sentence that answers neither question and
offers no remedy is doing none of the jobs the sources recognise.

**Applicability.** All surfaces. The destination matters: this rule deletes
nothing that is useful somewhere else, it relocates it.

**Source.** `WIN7-TEXT` Error Messages; `GERR` index and *Show how to fix*;
`NNG-ERR`. Q2, Q7.

**Exceptions.** A consequence the reader cannot infer stays, even if it
prescribes no action (`UX-ERR-006`). Knowing that a partial write remains on
the device changes what they do next, even when the message offers no button.

**Review test.** Remove the sentence and read what is left. Would the reader
make a worse decision? If not, it goes.

---

### UX-TEXT-010 — Say it once
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 1 + Tier 3
**Confidence:** HIGH

A fact MUST appear once per surface. The body MUST NOT restate the title; a
status line MUST NOT restate the body; a tooltip MUST NOT restate its
control's label; text MUST NOT state what an adjacent control already shows.

**Rationale.** Microsoft states each case separately. On tooltips: *"Don't
just repeat or give a wordy restatement of what is already in the label."* On
progress: *"Don't give the percentage completed or remaining because that
information is conveyed by the progress bar itself."* On dialog titles: the
incorrect example is one where *"the dialog box title text is a restatement of
the progress bar label."* On disclosure: *"Don't just restate the existing
information in a more verbose format."* Johnson lists *"information buried in
repetition"* among the things that disrupt reading.

**Applicability.** All surfaces, and across surfaces that are visible at the
same time.

**Source.** `W32-CTRL` Tooltips, Progress Bars; `WIN7-TEXT` Error Messages
(Progressive disclosure); `JM3` Ch. 6. Q11, Q15.

**Exceptions.** GOV.UK requires an error summary and the inline message to use
the *same words* (`UI-TEXT-013`). Deliberate repetition that aids navigation
between two places is not this rule's target; padding is.

**Review test.** Read title, body, buttons and adjacent controls in sequence.
Does any fact appear twice?

---

### UX-TEXT-011 — Do not narrate internal state
**Level:** MUST **Class:** DERIVED RULE **Authority:** Tier 2 + Tier 3
**Confidence:** HIGH

Text MUST NOT describe what the program did internally, what it was about to
do, which subsystem noticed, or the sequence of states it passed through.

**Rationale.** Microsoft names the leading cause of incomprehensible messages
as *"explaining the problem from the code's point of view instead of the
user's"*, and Cooper observes that most error messages *"simply report when
the application gets confused."* The narrative form — *the connection was
established, then the handshake completed, then the read timed out* — is the
code's point of view expanded into prose. The reader's question is what is
true now.

**Applicability.** All surfaces. The narrative belongs in the log, in full
(`UX-ERR-009`).

**Source.** `WIN7-TEXT` Error Messages; `AF4` Ch. 21; `AP-17`. Q9, Q15.

**Exceptions.** A debugging surface the reader opened on purpose
(`UX-ERR-023`).

**Review test.** Does the text contain a sequence of past-tense clauses about
the program? Collapse them to the present state.

---

### UX-TEXT-012 — Do not explain what the control already says
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 3
**Confidence:** HIGH

Text MUST NOT explain what an adjacent, well-labelled control will do.

**Rationale.** Win32's tooltip guidance forbids the exact case — a tip that
repeats its button — and its Quick Launch rule generalises it: *"Don't use
additional text to describe the program or what it does. Because users choose
the programs displayed in the Quick Launch bar, they already know their
purpose."* If the label does not convey the action, the defect is the label
(`UX-TEXT-021`), not the absence of a paragraph.

**Applicability.** Tooltips, helper text, dialog bodies that gloss their own
buttons.

**Source.** `W32-CTRL` Tooltips. Q15.

**Exceptions.** A non-obvious consequence of pressing it, which is
`UX-ERR-006`, not an explanation of the label.

**Review test.** Cover the sentence. Does the label still tell the reader what
the control does? Then the sentence is redundant.

---

### UX-TEXT-013 — Secondary information goes behind disclosure
**Level:** MUST **Class:** PLATFORM RULE **Authority:** Tier 1 + Tier 3
**Confidence:** HIGH

Information some readers need and most do not MUST be present and MUST be
behind a disclosure control, not on the face of the message. The control MUST
reveal something not already visible.

**Rationale.** Microsoft: *"use a Show/Hide details progressive disclosure
button to hide advanced or detailed information in an error message … don't
hide needed information, because users might not find it"*, and *"don't use
Show/Hide details unless there really is more detail."* Google recommends the
same shape for long errors, naming the failure it avoids: readers *"ignore
long error messages, intimidated by the 'wall of text.'"* GOV.UK's Details
component carries the same caution against hiding what most readers need.

**Applicability.** All surfaces that can hold a disclosure. Where none exists
— a status line, a toast — the detail goes to the log and the surface links to
it.

**Source.** `WIN7-TEXT` Error Messages; `GERR` Format for readability;
`GOVUK-DS` Details; `UI-TEXT-008`. Q1.

**Exceptions.** None. If there is no more detail, there is no control.

**Review test.** Open the disclosure. Is what appears new? Close it. Does the
message still say what happened and what to do?

---

### UX-TEXT-014 — Length budgets
**Level:** MUST (sourced half) / SHOULD (project half) **Class:** PLATFORM RULE + PROJECT CONVENTION
**Authority:** Tier 1 + Tier 3 **Confidence:** HIGH / n/a

**Sourced ceilings — these are quoted, and are rules:**

| Surface | Ceiling | Source |
|---|---|---|
| Main instruction | a single, complete sentence | `WIN7-TEXT` Error Messages |
| Supplemental error text | *"a maximum of three sentences of moderate length"* | `WIN7-TEXT` Error Messages |
| Tooltip | *"typically five words or less"* | `W32-CTRL` Tooltips |
| Infotip, Start menu and Control Panel descriptions | *"25 words or less"* | `W32-CTRL` Tooltips |
| Notification | 48 characters title, 200 body | `WIN7-TEXT` Notifications |
| Web sentence and paragraph | 25 words, 5 sentences | `GOVUK-WG` |

**Project ceilings — PROJECT CONVENTION, no source, chosen to constrain a
generator:**

| Surface | Budget |
|---|---|
| Error or dialog title | one phrase, no terminal punctuation, ≤ 8 words |
| Primary body | 1–2 sentences |
| One dialog | one problem, plus at most one consequence and one recovery |
| Status line | one clause, no terminal punctuation |
| Button label | 1–3 words, starting with a verb |

**Rationale.** No source read supplies a general dialog ceiling, and the
matrix records that gap. A project may still need one: a budget is the
cheapest instrument for stopping a generator from producing plausible,
grammatical, unnecessary prose. Presenting these as Microsoft or GOV.UK
requirements would be a false citation, so they are separated.

**Applicability.** The project half applies where the profile adopts it, and
a profile may set different numbers.

**Source.** As tabled. Q14.

**Exceptions.** A budget is a ceiling, never a target, and never a reason to
produce something cryptic (`UX-TEXT-008`).

**Review test.** Count. Then ask whether the string is short because it is
complete, or short because it was truncated.

---

# §C. The reader's perspective

### UX-TEXT-015 — Write from the task and the object
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 2 + Tier 3
**Confidence:** HIGH

Text MUST name what the reader was doing and which object it happened to. It
MUST NOT make the implementation the subject.

**Rationale.** Microsoft: the leading cause of incomprehensible messages is
*"explaining the problem from the code's point of view instead of the
user's."* NN/g: *"beware of excessive technical precision and accuracy that
can undermine understandability. The user's mental model of how the system
works likely differs from the conceptual model of how it was coded."* Cooper:
users *"don't see the technical rationale behind an error message."*

*A TCP read timed out* names the mechanism. *The connection to the device was
lost* names the object and its state. Both are true; only one is addressed to
the reader. The first is not deleted — it goes to detail and to the log
(`UX-ERR-008`, `UX-ERR-009`).

**Applicability.** All surfaces.

**Source.** `WIN7-TEXT` Error Messages; `NNG-ERR`; `AF4` Ch. 21. Q9.

**Exceptions.** A debugging surface (`UX-ERR-023`).

**Review test.** Underline the subject of each sentence. Is it something the
reader was working on, or something the program contains?

---

### UX-TEXT-016 — Use the reader's vocabulary, not yours
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 2
**Confidence:** HIGH

Terms MUST be ones the intended reader already uses. A term they would not
use MUST be explained where it first appears, or replaced.

**Rationale.** Google names the failure mode: *"Beware of the curse of
knowledge when writing error messages. A term familiar to you might not be
familiar to your target audience."* Its worked example — *"Exploding gradient
problem. To fix this problem, consider gradient clipping"* — is marked
*"Recommended for ML experts only"*, and its exercise shows one message that
is right for engineers and wrong for people uploading receipts. Johnson's
chapter on learning says the same from the cognitive side: vocabulary should be
*"task focused, familiar, and consistent"*, and unfamiliar jargon *"slows
learning and frustrates users"*. GOV.UK adds the counter-intuitive finding
already cited in `UI-TEXT-006`: specialists prefer plain English **more**, not
less.

Expertise widens the vocabulary a message may use. It does not license raw
diagnostics in primary copy — that is `UX-ERR-012`, and the two are separate
questions (Q8).

**Applicability.** All surfaces. The audience is declared in the profile.

**Source.** `GERR` Target audience; `JM3` Ch. 11; `GOVUK-WG`; `UI-TEXT-006`.
Q8.

**Exceptions.** Terms of art the declared audience uses daily. Those belong
in `TERMINOLOGY.md` as preferred terms.

**Review test.** Read it to someone in the target audience who did not build
the product. Which words do they not use themselves?

---

### UX-TEXT-017 — One concept, one term, every time
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 1 + Tier 2 + Tier 3
**Confidence:** HIGH

Each concept MUST have exactly one user-facing term, recorded in
`TERMINOLOGY.md`, used in every string. Synonyms MUST NOT be introduced for
variety. One condition MUST produce one message wherever it is reported.

**Rationale.** Google states both halves, including the warning that makes
this a generator problem: *"Some authoring systems automatically recommend
synonyms to ensure that you don't keep repeating the same word. Yes, variety
spices up paragraphs. However, variety in error messages can confuse users."*
And: *"the same problem must generate the same error message."* Win32:
*"consistent terminology promotes learning … inconsistency forces users to
figure out whether different words and actions mean the same thing"*, with
*start/run/launch/boot/execute*. Johnson: a reader looking for Search may miss
it when it is labelled Query.

**Applicability.** All surfaces, all languages, logs included where the log is
shown.

**Source.** `GERR` Use terminology consistently; `WIN7-TEXT` Style and Tone;
`MS-STYLE`; `JM3` Ch. 11; `UI-TEXT-013`. Q13.

**Exceptions.** Quoted third-party text inside a diagnostic block, which is
evidence and is not rewritten.

**Review test.** Pick a concept. Grep every string for it and for its likely
synonyms. More than one term is a finding.

---

### UX-TEXT-018 — Never make the reader the subject of a mistake
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 1 + Tier 2 + Tier 3
**Confidence:** HIGH

Text MUST NOT blame. Where an active sentence would make the reader the
subject of an error, the passive or an object-focused rewrite is correct.

**Rationale.** `UI-TEXT-003` already carries the word list. The new sources
add unanimity: Google, *"If possible, focus the error message on what went
wrong rather than assigning blame"*; NN/g, *"Don't use phrasing that blames
users or implies they are doing something wrong, such as invalid, illegal, or
incorrect. The proper usage of any system lies with its creators and not with
the system's users"*; Norman, *"Do not blame people when they fail to use your
products properly"*; Cooper, *"When the user sees an error message, it is as
if someone has told her she is stupid."*

**Applicability.** All surfaces.

**Source.** `UI-TEXT-003`; `GERR` Set the tone; `NNG-ERR`; `DOET-R` Ch. 5;
`AF4` Ch. 21. Q2, Q3.

**Exceptions.** None.

**Review test.** Read each message as though you had just done the thing it
reports. Does it sound like an accusation?

---

### UX-TEXT-019 — Say what to do, not what was not done
**Level:** SHOULD **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 2
**Confidence:** HIGH

Where an instruction exists, text SHOULD give it in positive form rather than
describing the omission.

**Rationale.** Google: *"Instead of telling the user what they did wrong, tell
the user how to get it right"* — *"You didn't enter a name"* becomes *"Enter a
name"*; and for a compiler, *"ANSI C++ forbids declaration 'ostream' with no
type"* becomes *"ANSI C++ requires a type for declaration 'ostream'."* The
same course forbids double negatives for the same reason.

**Applicability.** Validation, empty required values, constraint violations.

**Source.** `GERR` Set the tone, Avoid double negatives; `GOVUK-DS` Error
message. Q2.

**Exceptions.** Where no action exists, stating the condition is correct;
inventing an instruction is worse (`UX-ERR-007`).

**Review test.** Does the sentence describe an absence? Turn it into an
imperative and see if it is shorter and clearer.

---

### UX-TEXT-020 — Name the specific thing, with its values
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 2 + Tier 3
**Confidence:** HIGH

Where the program knows the object, the value, the limit or the location, the
message MUST name it. Category messages MUST NOT stand in for known
specifics.

**Rationale.** Google's pattern is the clearest in the corpus: not *"The
combined size of the attachments is too big"* but *"The combined size of the
attachments (14MB) exceeds the allowed limit (10MB)"*; not *"Time-out period
exceeded"* but *"Time-out period (30s) exceeded"*; not *"Permission denied"*
but *"Permission denied. Only users in <group name> have access."* Win32:
*"provide specific names, locations, and values of the objects involved."*
NN/g: *"Generic messages such as An error occurred lack context."*

This is the rule that makes concision safe. Short and specific is the target;
short and vague is the failure Google calls cryptic.

**Applicability.** All surfaces.

**Source.** `GERR` Identify the cause, Specify requirements; `WIN7-TEXT`
Error Messages; `NNG-ERR`; `UI-TEXT-002`. Q2, Q7.

**Exceptions.** Where the program genuinely does not know, say so plainly
rather than guessing — Win32: *"it is better to be up front about the lack of
information."*

**Review test.** Could this message appear for two different underlying
causes? If the program can tell them apart, it is two messages.

---

# §D. Surfaces

### UX-TEXT-021 — Buttons name their action
**Level:** MUST **Class:** PLATFORM RULE **Authority:** Tier 1 + Tier 3
**Confidence:** HIGH

A command button MUST be labelled with the action it performs, starting with a
verb. *OK* MUST NOT acknowledge a problem; the dismissing button on a problem
is *Close*. *Yes* and *No* MUST be used only to answer a yes-or-no question,
always as a pair. A destructive button MUST name the destruction.

**Rationale.** Carried from `UI-TEXT-012` and `UI-DLG-002`, with the button
sources added: *"for windows used to perform one specific task, use a specific
label instead that starts with a verb"*; *"Don't use OK for error messages,
because this wording implies that problems are OK"*; *"use Yes and No buttons
only to respond to yes or no questions."* Microsoft's dialog guidance requires
the *"'call and response' between the title of a dialog and its buttons"*.
GOV.UK: *"write button text in sentence case, describing the action it
performs."*

Generic acknowledgement is acceptable in one case only: a message that reports
a fact, offers no choice, and whose dismissal has no consequence. Then *Close*
is the label, and the question is whether the message needed a dialog at all
(`UX-ERR-003`).

**Applicability.** All command buttons, in dialogs and on surfaces.

**Source.** `UI-TEXT-012`; `WIN7-TEXT` User Interface Text, Error Messages;
`W32-CTRL` Command Buttons; `MS-WRITING` Dialogs; `GOVUK-DS` Button. Q10.

**Exceptions.** Platform-standard dismissal in a system-provided dialog the
product does not control.

**Review test.** Read the title and then each button aloud as an exchange.
Does each button answer? Is *OK* answering a problem?

---

### UX-TEXT-022 — Menu commands are verbs, and the same verb everywhere
**Level:** MUST **Class:** DERIVED RULE **Authority:** Tier 1 + Tier 2
**Confidence:** MEDIUM

A menu command MUST name an action with a verb, MUST use the same verb as the
button and tooltip for the same action, and MUST take an ellipsis when it
needs further input before acting.

**Rationale.** Assembled: `UI-GLOBAL-003` requires one action to carry one
name, icon and shortcut everywhere; `UI-TEXT-014` requires input-neutral
verbs; Win32 requires an ellipsis *"if the label is for a command that needs
additional information"*; `UX-TEXT-017` requires one term per concept. No
source read gives a menu-wording section of its own, so the rule is DERIVED.

**Applicability.** Menus, context menus, command palettes, ribbons.

**Source.** `UI-GLOBAL-003`; `UI-TEXT-014`; `W32-CTRL` Tooltips (ellipsis).
Q13.

**Exceptions.** Top-level menu titles, which are nouns by convention.

**Review test.** List every place an action appears. Same verb?

---

### UX-TEXT-023 — Tooltips name, they do not lecture
**Level:** MUST **Class:** PLATFORM RULE **Authority:** Tier 3
**Confidence:** HIGH

A tooltip MUST label an unlabelled control in about five words, as a sentence
fragment without terminal punctuation, and MUST NOT restate a visible label.
Where it adds detail, the detail MUST be new. Keyboard shortcuts and default
values in parentheses are encouraged and do not count against the length.

**Rationale.** Quoted: *"Use tooltips to provide labels for unlabeled
controls"*; *"keep tooltips brief typically five words or less but prefer
specific labels over vague ones"*; *"Don't just repeat or give a wordy
restatement of what is already in the label"*; *"make tooltips more helpful by
providing keyboard shortcuts and default values … Don't consider this
additional text when evaluating the conciseness of a tooltip."* Infotips, the
longer form, take *"25 words or less"* and full sentences.

**Applicability.** Tooltips and infotips. In a toolkit without accessible
names, the tooltip is the control's only name and becomes mandatory
(`UI-IMGUI-012`).

**Source.** `W32-CTRL` Tooltips. Q7, Q15.

**Exceptions.** Infotips in nonstandard places, where Win32 prefers
consistency over brevity.

**Review test.** Does any tooltip repeat its label? Is any longer than a
phrase?

---

### UX-TEXT-024 — Status text is a stable clause
**Level:** MUST **Class:** PLATFORM RULE **Authority:** Tier 3 + Tier 2
**Confidence:** HIGH

Status text MUST be a short sentence fragment without terminal punctuation,
MUST name the current condition rather than the machinery producing it, and
MUST NOT change faster than it can be read. Status MUST NOT be the only place
a critical condition appears.

**Rationale.** Win32: *"Generally, use concise labels. Cut any text that can
be eliminated. Prefer sentence fragments, without ending punctuation"*, and
*"Don't change status too frequently … The eye is sensitive to changes in the
peripheral field of vision, so status changes need to be subtle."* Johnson
Ch. 5 explains why the last clause follows: peripheral vision is poor, so a
distant change is nearly invisible — which is also why Visual Studio says the
status bar is *"best used for informational purposes or as a redundant cue"*
and that *"Any kind of critical information that the user must resolve
immediately should be provided in a dialog."*

**Applicability.** Status bars, embedded status areas, ambient indicators.

**Source.** `W32-CTRL` Status Bars; `VS-UX`; `JM3` Ch. 5. Q11.

**Exceptions.** None.

**Review test.** Watch the status area through one full operation. Could you
read every state it passed through? Is anything there that only appears there?

---

### UX-TEXT-025 — Progress text names the activity, without false precision
**Level:** MUST **Class:** PLATFORM RULE **Authority:** Tier 3
**Confidence:** HIGH

A progress label MUST start with a verb in the gerund and end with an
ellipsis. It MUST NOT restate what the indicator shows. Estimates MUST NOT
claim precision the program does not have. Progress MUST NOT restart or move
backwards. Detail MUST be shown only where the reader can act on it.

**Rationale.** All quoted from `W32-CTRL` Progress Bars: *"Start the label
with a verb (for example, Copying) and end with an ellipsis"*; *"Don't give
the percentage completed or remaining because that information is conveyed by
the progress bar itself"*; *"Make estimates accurate, but don't give false
precision. If largest unit is hours, give minutes (if meaningful) but not
seconds"*; *"Don't restart progress"*; *"Don't back up progress"*; *"provide
additional progress information only if users can do something with it."*
Core `UI-FB-003` already governs when progress must appear.

**Applicability.** Progress bars, spinners with labels, long-operation status.

**Source.** `W32-CTRL` Progress Bars; `VS-UX`; `UI-FB-002`, `UI-FB-003`.
Q11.

**Exceptions.** Filenames during a copy the reader selected — Microsoft's own
example of detail that is meaningful.

**Review test.** Read the progress label at five random moments. Does it name
an activity, or a function? Does the estimate claim seconds it cannot know?

---

### UX-TEXT-026 — Do not announce expected, visible success
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 3 + Tier 2
**Confidence:** HIGH

Success MUST NOT be announced when it was requested and its result is visible.
It MUST be reported when the change is not visible where the reader is
looking, when it follows a recent failure, when it took an unexpected form, or
when it is security-relevant.

**Rationale.** Win32 Notifications: *"don't notify of successful operations"*
with exactly those exceptions, and *"assume that users take successful
operations for granted."* Cooper supplies the register: a dialog announcing a
completed synchronisation is *"unnecessarily obsequious"*, and *"Launching one to announce a requested action is pathological."* `CLIG`'s "if you
change state, tell the user" is the same rule in a medium with no persistent
surface (Q12).

**Applicability.** All surfaces.

**Source.** `WIN7-TEXT` Notifications; `AF4` Ch. 21; `CLIG` Output;
`UI-TEXT-015`. Q12.

**Exceptions.** As listed in the rule.

**Review test.** For each success message: what would the reader not know
without it?

---

### UX-TEXT-027 — An empty state says why it is empty and what to do
**Level:** SHOULD **Class:** DERIVED RULE **Authority:** Tier 2
**Confidence:** LOW

An empty region SHOULD state why there is nothing to show and name the action
that would put something there. It SHOULD NOT be decorative, apologetic or
instructional beyond that.

**Rationale.** No source read addresses empty states. The rule is assembled
from `UX-TEXT-009` (every sentence earns its place), `UX-TEXT-020` (name the
specific reason — no results for *this filter* differs from nothing imported
yet), and `UX-TEXT-021` (the action is a button, not a paragraph). Marked LOW
and DERIVED because of that; a project that finds a source should raise it.

**Applicability.** Lists, tables, panes and canvases with nothing in them.

**Source.** None direct; recorded as gap 4 in `UX_COPY_EVIDENCE.md`.

**Exceptions.** A first-run state may carry one line of orientation, subject
to `UI-EXP-001` — it is paid for on every later launch.

**Review test.** Does the empty state distinguish "nothing matches your
filter" from "nothing exists yet"? Is there one action?

---

### UX-TEXT-028 — Settings descriptions say what the setting does when on
**Level:** SHOULD **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 3
**Confidence:** MEDIUM

A setting's description SHOULD start with a present-tense verb, state the
effect of enabling it, name specifics rather than categories, and stay within
about 25 words. It SHOULD NOT restate the setting's label.

**Rationale.** The closest evidence is Win32's guidance for Control Panel and
Start menu descriptions, which is the same job: *"Be helpful. Focus on what
users can do. Don't just repeat the item name or even use it in the
description at all"*; *"Be specific. Avoid generic verbs and catch-all phrases
like and other hardware"*; *"Be concise. Use 25 words or less. Longer infotips
discourage reading"*; *"Start with a present-tense, imperative verb … Prefer
specific verbs over generic verbs such as manage and open."* MEDIUM because
the transfer from Control Panel items to in-app settings is ours.

**Applicability.** Settings pages, preference dialogs, option descriptions.

**Source.** `W32-CTRL` Tooltips (Control Panel and Start menu infotips);
the transfer is recorded as gap 5 in `UX_COPY_EVIDENCE.md`.

**Exceptions.** A setting with a genuinely non-obvious consequence may add one
sentence for it (`UX-ERR-006`).

**Review test.** Cover the label. Does the description still say what happens
when the setting is on?

---

### UX-TEXT-029 — Validation messages sit with the field and use its words
**Level:** MUST **Class:** CONTENT-DESIGN PRINCIPLE **Authority:** Tier 2
**Confidence:** HIGH

A validation message MUST appear beside the control it concerns, MUST reuse
the control's label, MUST state the requirement rather than the failure, and
MUST NOT appear before the reader has had a chance to finish.

**Rationale.** GOV.UK requires the message to match the label
(*"Address line 1"* → *"Enter address line 1"*) and the summary to match the
inline message word for word (`UI-TEXT-013`). Tidwell rejects the modal form
on mechanical grounds: *"you had to click away the modal dialog box to fix the
error. And with the dialog box gone, you couldn't read the error message
anymore."* NN/g adds the timing: *"Avoid prematurely displaying errors …
It's like grading a test before the student has had a chance to answer"*, and
*"Preserve the user's input."* Core `UI-EDIT-004` already forbids blocking
typing.

**Applicability.** Forms, inline editing, parameter entry.

**Source.** `GOVUK-DS` Error message, Error summary; `DI3` Ch. 10; `NNG-ERR`;
`UI-EDIT-004`, `UI-TEXT-013`. Q2, Q5.

**Exceptions.** Fields where an early check genuinely helps, which NN/g allows
for *"error-prone interactions where users are unlikely to enter the correct
information on their first try."*

**Review test.** Type something invalid. Where does the message appear, when,
and does it use the field's own words?

---

# §E. Anti-patterns of generated text

Nine patterns a language model produces by default. Each is already rejected
by at least one source for reasons unrelated to how the text was produced;
the citation is given so none of these rests on taste. They share the
anti-pattern numbering of `UI_ANTIPATTERNS.md`, which points here.

Format: definition → detection → legitimate exception → before and after.

---

## AP-31 — Narrative explanation

**Definition.** The message tells the story of what happened, in sequence,
usually in the past tense and usually about the program.

**Detection.** Two or more past-tense clauses about the software; the
connectives *previously*, *had been*, *and then*, *at which point*; any
sentence whose subject is a subsystem.

**Exception.** A debugging surface the reader opened deliberately
(`UX-ERR-023`), and the log, which should contain exactly this.

**Before.** *The application was previously connected to the device, but the
communication channel has now been interrupted and the session could not be
maintained.*

**After.** *Connection to the device was lost.*

**Decided by** `WIN7-TEXT` Error Messages (*"explaining the problem from the
code's point of view instead of the user's"*); `AF4` Ch. 21.
**Rules** `UX-TEXT-011`, `UX-TEXT-015`.

---

## AP-32 — Restating the obvious

**Definition.** A sentence whose content is that something happened, when the
reader can already see that something happened.

**Detection.** *because an error occurred*, *was not successful*, *could not
be completed*, *something went wrong*, with no object and no cause. Also any
body that paraphrases its own title.

**Exception.** None. If the program truly does not know the cause, say that
plainly — Win32: *"it is better to be up front about the lack of
information."*

**Before.** *The operation could not be completed because an error occurred.*

**After.** *Could not save the project: the drive is full.*

**Decided by** `NNG-ERR` (*"Generic messages such as An error occurred lack
context"*); `GERR` Identify the cause; `GOVUK-DS` Error message.
**Rules** `UX-TEXT-010`, `UX-TEXT-020`.

---

## AP-33 — Internal reasoning shown

**Definition.** The message exposes the inference chain by which the program
reached its conclusion.

**Detection.** *Since*, *because of this*, *as a result*, *therefore*,
*given that*, used to link a program state to a program conclusion.

**Exception.** Where the reasoning is the content — a diagnostic report the
reader asked for.

**Before.** *Since the device has stopped responding to status requests, the
application can no longer determine the current session state and will
therefore end the session.*

**After.** *The device stopped responding. The session ended.*

**Decided by** `WIN7-TEXT` Error Messages; `GERR` Be concise.
**Rules** `UX-TEXT-011`, `UX-TEXT-009`.

---

## AP-34 — Excessive consequences

**Definition.** The message enumerates everything that might follow, instead
of the one consequence that bears on the reader's next decision.

**Detection.** Lists of possible effects; *this may also*, *in addition*,
*note that this can*; more than one consequence sentence.

**Exception.** Genuine safety information, and irreversible loss, which must
be stated even when unwelcome.

**Before.** *Disconnecting now will end the session. Any unsaved calibration
will be lost, the log will be closed, background polling will stop, and you
will need to re-authenticate the next time you connect.*

**After.** *Disconnect now? Unsaved calibration will be lost.*

**Decided by** `WIN7-TEXT` Error Messages (three-sentence ceiling);
`UI-TEXT-001`.
**Rules** `UX-TEXT-009`, `UX-ERR-006`.

---

## AP-35 — Fake helpfulness

**Definition.** Padding that performs helpfulness without carrying
information.

**Detection.** *Please note that*, *Keep in mind that*, *It's important to
understand that*, *You may want to*, *Remember that*, *As you may know*, *at
this time*, *simply*, *just*, *easily*.

**Exception.** None in interface text.

**Before.** *Please note that it's important to understand that the device
must be powered on before scanning. You may want to check this first.*

**After.** *Turn on the device, then scan.*

**Decided by** `GSTYLE` Voice and tone (the avoid-list, verbatim: *"Placeholder
phrases like please note and at this time"*, *"Using phrases like simply, It's
that simple, It's easy, or quickly in a procedure"*).
**Rules** `UX-TEXT-006`, `UX-TEXT-009`.

---

## AP-36 — Unnecessary politeness

**Definition.** *Please*, *sorry*, *unfortunately*, *we apologise*, used where
nothing has been lost and nothing inconvenient is being asked.

**Detection.** Search for the words. For each, ask what the reader lost or is
being asked to bear.

**Exception.** Real cost to the reader, per `UX-TEXT-003`; and the consumer
total-outage case in `C20`.

**Before.** *Sorry, we were unable to load the file. Please try again.*

**After.** *Could not open report.csv: the file is in use by another program.*

**Decided by** `GERR` Set the tone; `GOVUK-DS` Error message; `WIN7-TEXT`
Style and Tone.
**Rules** `UX-TEXT-003`, `UI-TEXT-004`.

---

## AP-37 — Dramatic language

**Definition.** Severity vocabulary attached to an ordinary operational
condition.

**Detection.** *critical*, *fatal*, *severe*, *catastrophic*, *lost*,
*destroyed*, *corrupted*, *emergency*, applied to something recoverable,
expected or already handled.

**Exception.** Conditions that are those things. Data loss is loss.

**Before.** *Critical failure: connection to the ECU was catastrophically
lost.*

**After.** *The ECU is not responding. Reconnect.*

**Decided by** `W32-CTRL` Standard Icons (*"Don't use warning icons to
'soften' non-critical errors"*, and match the words to the type);
`UI-TEXT-003`.
**Rules** `UX-TEXT-005`.

---

## AP-38 — Developer prose in the product

**Definition.** Text written for a bug report, a commit message or a design
discussion, appearing on screen.

**Detection.** Function and class names, exception types, protocol
identifiers, numeric codes, *thread*, *buffer*, *handle*, *null*, *callback*,
*deserialise*, in primary copy. Stack frames anywhere outside a diagnostic
block.

**Exception.** A diagnostic block, a log, or a debugging surface — where it is
required, complete and copyable (`UX-ERR-008`).

**Before.** *PassThruWriteMsgs(ISO15765) returned ERR_TIMEOUT (0x9) after 3
retries on channel 1.*

**After.** *The device did not respond. Check the cable and reconnect.*
With, under Details: *PassThruWriteMsgs(ISO15765): ERR_TIMEOUT (0x9), channel
1, 3 retries.*

**Decided by** `NNG-ERR` (codes *"for technical diagnostic purposes only"*);
`W32-CTRL` Progress Bars (debug detail not in release builds); `CLIG` Errors.
**Rules** `UX-ERR-012`, `UX-TEXT-015`. See also `AP-26`.

---

## AP-39 — Documentation inside a dialog

**Definition.** Paragraphs teaching the reader how the system works, in a
surface they did not open to learn.

**Detection.** More than three sentences; any sentence explaining
architecture, workflow or rationale; the words *note*, *typically*, *in
general*, *this is because*.

**Exception.** A help topic the reader opened. Long explanation belongs behind
a link — Google: *"When an error requires a lengthy explanation … use links to
redirect users to more detailed documentation."*

**Before.** *The scan could not start. Scanning requires an active session,
which is established when the device handshake completes. Handshakes typically
take two to three seconds. If the device is in bootloader mode, the handshake
will not complete and the session cannot be established. In general it is best
to ensure the device has finished starting up before scanning.*

**After.** *Cannot scan: the device is still starting up. Wait a few seconds,
then scan.*

**Decided by** `GERR` Format for readability; `WIN7-TEXT` Error Messages;
`JM3` Ch. 6.
**Rules** `UX-TEXT-009`, `UX-TEXT-013`, `UX-TEXT-014`. See also `AP-23`.

---

# Appendix A — Before and after

A small corpus illustrating transformations, not templates. Each names the
rule doing the work. Examples are drawn from professional desktop software
and hardware communication, the class of product this oracle serves.

**Developer error → reader's error**

> *Unhandled exception: System.IO.IOException: The process cannot access the
> file 'C:\proj\run.log' because it is being used by another process.*

> *Cannot write to run.log. Another program has the file open.*
> Details: `System.IO.IOException — The process cannot access the file
> 'C:\proj\run.log' because it is being used by another process.`

`UX-ERR-010`, `UX-ERR-012`, `UX-TEXT-015`.

**Verbose → concise**

> *The import operation has finished processing, however it should be noted
> that not all of the records that were present in the source file could be
> imported successfully due to validation problems.*

> *Imported 1,412 of 1,500 records. 88 were rejected.* → *Review rejected
> records*

`UX-TEXT-008`, `UX-TEXT-020`, `UX-TEXT-021`.

**Vague → specific**

> *Invalid configuration.*

> *Baud rate 250000 is not supported by this adapter. Supported rates: 9600,
> 19200, 38400, 115200.*

`UX-TEXT-020`, `GERR` Specify requirements.

**Passive warning → actionable warning**

> *It is possible that the firmware version may not be compatible.*

> *This file is for firmware 2.x. The device is running 1.4. Update the device
> before flashing.*

`UX-TEXT-019`, `UX-TEXT-020`, `UX-ERR-007`.

**Yes/No confirmation → action-labelled confirmation**

> *Are you sure?* [Yes] [No]

> *Erase the calibration table? This cannot be undone.* [Erase table]
> [Cancel]

`UX-TEXT-021`, `UX-ERR-017`, `UI-DLG-005`.

**Modal error → non-modal state**

> A dialog: *The device is not connected.* [OK]

> The connect button stays enabled, the status area reads *Not connected*, and
> the toolbar's device indicator shows the disconnected state. No dialog.

`UX-ERR-003`, `UI-FB-006`, `UI-DLG-001`.

**Inline diagnostics → expandable diagnostics**

> *Flash failed: erase verify mismatch at 0x0801F400 (expected 0xFF, read
> 0x3C), sector 7, retry 2 of 3.*

> *Flashing stopped. The device rejected the erase.* [Retry] [Close]
> Details (copyable): `erase verify mismatch at 0x0801F400 — expected 0xFF,
> read 0x3C; sector 7; retry 2 of 3`

`UX-ERR-008`, `UX-ERR-012`, `UX-ERR-013`.

**Success noise → silence**

> *The file was saved successfully.* [OK]

> The title bar drops its modified marker. Nothing else.

`UX-TEXT-026`, `AF4` Ch. 21.

---

# What this oracle deliberately does not say

- **A universal register.** Warmth is a profile decision (Q4). The rules
  constrain what register may do, not which one a product picks.
- **Apple's position on anything.** Not obtained; no rule cites it.
- **Snackbar, toast and other Material surfaces.** Ungrounded here; the
  surface-neutral rules still apply.
- **A general dialog word count.** Unsourced. The project ceiling in
  `UX-TEXT-014` is labelled as policy.
- **Localisation.** Expansion, string composition and whole-sentence links are
  real and out of scope; `modules/writing.md` already records this.
