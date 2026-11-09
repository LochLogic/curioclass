# Claim vs Claim

## One idea
A class group chat is arguing about a new rule (no phones from first bell to last), and the student, as class representative, sorts each message into their side's claim, an opposing claim or neither, merges the opposing messages into the other side's strongest claim, marks the exact point where the two sides part ways, and writes a formal statement for the school board; a board member then restates the opposing claim from the statement and says so if it is a straw man, so they learn to tell their claim apart from the alternatives fairly and to argue in a formal style.

## Not like
- counterclaim-rally (7, spec): answering an opponent point by point in a volley. Here sorting many voices into claims and stating the other side fairly, grade 8.
- debate-prep-desk (6, spec): building both sides from sources. Here distinguishing claims from a messy chat and turning it formal.
- argument-x-ray (6, spec): tracing one author's argument. Here many speakers.
- logic-gym (7, spec, this batch): judging evidence. Here stating and separating claims.
- usage-panel (11, concept): a panel debate on usage. Here a school board statement.

## Who and how
- Grade 8, ELA, module "Argument and Rebuttal" (Writing). Standard: W.8.1 (a, b, c, d, e).
- Driver: one student; a teacher can type the school's own rule and chat prompt (tool.json `driver: "student"`). Every message is read on tap.
- Topics: Phones from bell to bell; Later school start (practice); A four-day week (practice). All chats are written for Curio Class. tool.json `modes: ["Phones", "Later start", "Four-day week", "Our rule"]`, `minutes: "25-35"`, `grades_label: "Grade 8"`.
- Nothing is saved; `Print` prints the sorted chat and the statement. A teacher's own topic stays only while the page is open.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| W.8.1a (distinguish from alternate or opposing claims) | Sort each message: supports my claim, opposing claim, or neither | the sorted chat | 2 |
| W.8.1a | Merge same-point opposing messages into one claim in its strongest form; mark the exact point of disagreement | the opposing claim card and the "where we part" line | 3 |
| W.8.1d (formal style) | Rewrite chat language in formal style; slang, sarcasm and "you guys" are flagged | the rewrite with flags | 4 |
| W.8.1b, W.8.1c (reasons, evidence, transitions) | Build the statement: claim, two reasons with evidence cards, the opposing claim and the answer, transitions | the statement outline | 5 |
| W.8.1a, W.8.1e | The board member restates the opposing claim; a straw man is sent back; the conclusion follows from the argument | the board member's restatement | 5 |

## Screens and modes
Header (kit): title "Claim vs Claim"; `Chat`, `Sort`, `Statement`, `Board`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A phone on a desk showing a busy class group chat (about 30 messages, tempers marked with grawlixes like "#@%!" in place of anything rude) and an invitation card: "School board meeting. Two minutes, in writing, by Friday." First hint: "Tap the invitation to hear it." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**Sort.** The student picks a side, then drags each message to Supports my claim, Opposing claim or Neither (jokes, insults, off-topic). The key accepts some messages in more than one bin when they could be read either way, with a one-line reason.

**Merge.** Opposing messages that make the same point ("what if my mom needs me", "emergencies tho", "my little brother gets picked up by me") are stacked into one claim card. The student writes it in its strongest form ("Families need a way to reach students during an emergency"). A strength check asks for the claim to be a full sentence with no insult and no weakest-version words ("just", "only want to text"). Then the student marks where the sides part: what both agree on (safety) and what they disagree on (whether the office phone is enough).

**Tone translator.** The student rewrites three chat lines in formal style; flags mark slang ("tho", "ngl", "lowkey"), sarcasm markers ("yeah right", "sure, great idea") and "you guys". The student does the rewriting; the tool only flags.

**Statement.** Built from parts: claim; two reasons with evidence cards (written for Curio Class, labeled practice: a teacher's count of class interruptions, the office phone policy, a parent survey); the opposing claim stated fairly and answered; transitions; a conclusion. About 150 to 250 words.

**Board.** Board member Mr. Hollis Grant reads the statement and restates the opposing claim as the statement gives it. If the student's version is weaker than their own merged card (keyed weak words, or it leaves out the merged point), he says "That's not what they said. What's their best version?" and the student revises.

**Our rule.** The teacher types a rule and pastes or types chat messages; sorting and the statement work the same, without keyed bins.

At 1366x768 the phone and panel fit side by side; at 680x425 the phone is a tab.

## Content
Written for Curio Class: three chats of about 30 messages each with keyed bins, merge groups, strongest forms and the point of disagreement; evidence cards labeled practice; the slang, sarcasm and weak-word lists.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Messages can move between bins any time.
- With Motion off messages don't slide.

## Look
- Accent `--brand` #0d5c63 chat teal (header, phone frame, bins); gold #f4c542 (the merged claim card, the point of disagreement); paper #eff7f7; ink #04201f; muted #465b5c. Scene: a desk at home in the evening.
- Contrast (WCAG 2.1, computed): white on brand 7.70:1; brand on paper 7.08:1; ink on paper 15.69:1; muted on paper 6.64:1; ink on gold 10.48:1.
- Never color alone: bins have words; flags have labels.
- Different from this batch (gym brick red, field olive, studio violet, plum).

## Art
- People art goes to Gemini: Mr. Hollis Grant (an older Black man in a cardigan at a board table), 3 poses; "illustrated friendly school board member <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): a desk with a phone at evening (1); a school board meeting room with no people (1).
About 5 images. Drawn in code: phone chat, bins, statement outline.

## Voice
Bank voice `firm-captain` as Mr. Grant and the hint voice (unique in this batch); chat messages are read by `playful-friend` (unique in this batch). `Curio.voice` with `scope: () => state.topic + ':' + state.view + ':' + state.msg`, `welcomeAfter: true`.
- how `welcome`: "Your class is arguing. Sort what they said, find the other side's best point, then write the board something formal."
- event `msg`: the tapped message (grawlixes are read as "bleep").
- event `strongest`: "Is that their best version?"
- event `flag`: "{Tho} is chat talk. Try a formal word."
- event `restate`: Mr. Grant's restatement of the opposing claim.
- event `strawman`: "That's not what they said. What's their best version?"
- event, whole, `statement`: the statement.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: keyed bins with alternates, merge groups, strength and style checks, the statement builder, the restatement.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Put everything in Neither | The merge step needs at least one opposing group; keyed opposing messages show in the print. |
| Strongest form | Paste one message | The strength check needs a full sentence covering the merged point. |
| Statement | Leave out the opposing claim | Mr. Grant can't restate it and asks for it. |
| Formal style | Avoid flagged words only | The lists catch common chat talk; the statement prints for the teacher. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the invitation: invitation, `welcome` (queued, first time).
2. Sort: `msg` on tap.
3. Merge: `strongest` as it fires. Tone: `flag` as it fires.
4. Board: `statement` (whole), then `restate`, then `strawman` if it fires.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.8.1 (a to e) wording | thecorestandards.org, Writing Grade 8 | CCSS ELA 2010 PDF | yes |
| A straw man misstates an opposing argument to make it easier to attack | Merriam-Webster, straw man | Purdue OWL, logical fallacies | yes |
| Strong arguments state opposing claims fairly and answer them; formal academic style avoids slang | Purdue OWL, counterarguments and academic tone | ReadWriteThink, argument writing | yes |
Backed twice: 3. Cut: 0.

Design choices (not claims): chats and evidence cards are written for Curio Class, labeled practice on screen; no real school is named.

Checks run (Python, scratchpad b22, 2026-11-09): each chat has at least three opposing merge groups and one message that fits two bins; a sample weak restatement trips the weak-word check; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 phone and panel fit; at 680x425 the phone is a tab.
2. Messages sort into three bins with keyed alternates. (W.8.1a)
3. Merges take a strongest form and a point of disagreement. (W.8.1a)
4. Tone flags mark slang, sarcasm and "you guys". (W.8.1d)
5. The statement needs a claim, two reasons with cards, the opposing claim and answer, transitions and a conclusion; Mr. Grant restates and sends back straw men. (W.8.1b, c, e)
6. Our rule works with teacher text.
7. Print shows the sorted chat and statement.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: messages don't slide; no network requests.

## Open questions
- None for Cory.
