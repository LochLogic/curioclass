# Debate Prep Desk

## One idea
The student preps for a debate at a coach's desk by building both sides of a question from a folder of real sources (should phones be put away at lunch?), sorting evidence cards onto the For and Against sides, writing a reason for each, then hearing the coach raise objections against their own side that they must answer with a rebuttal card, and only when both sides are fairly matched do they pick a side and write a short argument, so they learn that a strong argument knows the other side's best case and answers it.

## Not like
- argument-x-ray (6, spec, this batch): tracing one author's argument. Here building both sides.
- claim-quote-comment (6-8, spec, this batch): one claim built link by link. Here two sides and rebuttals.
- claim-court (5, spec): judging an author's support. Here preparing your own case against objections.
- podcast-listening-club (6-8, spec): judging speakers by ear. Here preparing to speak.
- book-group-table (6, spec): discussion moves about a story. Here debate prep with sources.

## Who and how
- Grade 6, ELA and social studies, module "Both Sides of a Question" (Writing; C3 Inquiry). Standards: W.6.1 (a, b), C3 D3.4.6-8 (develop claims and counterclaims using evidence), C3 D4.1.6-8 (construct arguments with claims and evidence from multiple sources while acknowledging counterclaims).
- Driver: one student; pairs can split sides in class mode (tool.json `driver: "student"`). Role: lesson. Every card is read on tap.
- Change note (spec fix, 2026-11-10): the desk, the coach and the fair-fight meter stay. Added: a fourth real folder (Later School Start), so with the practice folder there are five arguments to write, one a sitting; the argument is now written out as a paragraph from the filled slots, with an opening that sets up the question; each folder has two weak-source cards and the student rates every source; the student writes each side's claim as a sentence; objections go from three to five and need a written rebuttal, and a wrong card now costs; the meter's hint no longer says what the weaker side needs until the second ask. The coach's own filled sheet for the practice folder is the model.
- Four folders: Phones at Lunch, Year-Round School, School Uniforms, Later School Start; plus a practice folder labeled made up, done first with the coach's model sheet beside it. tool.json `modes: ["Prep", "Pair prep"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the two-sided prep sheet and the student's argument.
- Change note (split, 2026-11-11): this tool keeps W.6.1a and W.6.1b. W.6.1c to e (linking words, formal style, a concluding statement) were never carried here and now have their own tool, so nothing was removed. Added the three hooks: the last folder is done on your own with the end screen by code, English learner supports, access.
- English learners: every spoken line is also on screen in short sentences. The words claim, reason, evidence, source and objection each show with an example from the coach's sheet the first time they are used. Every written line offers a frame the student may take or leave ("This counts because __."; "Some people say __, but __."). Coach Rivera's objections use no idioms.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| W.6.1a | introduce claim(s) and organize the reasons and evidence clearly | the student | Fill the slots, then write the argument as a paragraph with an opening that sets up the question, and check it against the guide | 5 arguments, one per folder | the outline beside the paragraph box | 6 |
| W.6.1b | support claims with clear reasons and relevant evidence, using credible sources and showing understanding of the topic | the student | Rate every card's source strong, okay or weak with a reason; pick the strongest card for each reason; write why it counts in your own words | 10 to 12 cards per folder | the source line and the student's rating | 3 |
| D3.4.6-8 | develop claims and counterclaims using evidence | the student | Sort cards to For, Against or Doesn't help; write each side's claim as a sentence and a reason for each | 2 claims per folder, 10 in all | the two trays with claims on top | 2 |
| D4.1.6-8 | construct arguments from multiple sources while acknowledging counterclaims | the student | Answer five coach objections, each with a card and a written rebuttal; balance both sides | 5 objections per folder | objection and rebuttal pairs; the meter | 4, 5 |

## Screens and modes
Header (kit): title "Debate Prep Desk"; `Folder`, `Sides`, `Objections`, `Argument`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A coach's desk in a school library with a timer, a whistle, a podium in the corner and two trays labeled For and Against. Coach Rivera, the debate coach, sits behind the desk. First hint: "Tap the folder to hear the question." The first tap reads the question; the welcome is queued after it (`welcomeAfter: true`).

**Folder.** Eight to ten evidence cards per question, each a short sourced summary with its source line. The student can open a card to hear it.

**The coach's sheet (the model).** The practice folder opens with Coach Rivera's own finished sheet for a different made-up question ("Should the library stay open at lunch?"): two claims, rated sources, one rebuttal and a short paragraph. It stays one tap away in every folder as `Coach's sheet`. The student then does the pet club folder with each step's matching part of the sheet beside it.

**Sources.** Before sorting, the student rates each card's source `Strong`, `Okay` or `Weak` and taps one reason chip (who wrote it; how they know; how old it is; what they gain). Ratings are keyed. A miss can be changed once; after a second miss the coach says why and the card carries a small "coach rated" mark. Each folder holds two weak cards (an unsigned post; a seller's ad). Weak cards can be sorted, but they cannot be picked as a reason's strongest card.

**Sides.** The student drags each card to For, Against or Doesn't help, writes each side's claim as one sentence at the top of its tray, and writes one reason per side that the cards support. Cards are the evidence engine's Evidence links with `side: 'claim'` or `'counter'`.

**Objections.** Coach Rivera raises five objections, three against the side the student has built more and two against the other ("A study of four English cities isn't your school."). The student answers each by dragging one card and writing a one-sentence rebuttal that uses it; these are rebuttal links. A card that does not meet the objection is turned away once with "That doesn't meet the objection." After a second miss the coach shows a card that does, the pair is marked "coach helped", and one more objection is added to the list.

**Fair fight.** The engine's `ev.fairFight` compares the two sides (cards, claims, reasons, rebuttals) and shows a meter from lopsided to even. The student can't pick a side until the meter reads fair. The first hint says only which side is lighter ("The Against side is lighter."). If the student asks again, it names what is missing ("The Against side needs a reason.").

**Argument.** The student picks a side and fills the engine's Draft: claim, two reasons with cards (`ev.pickStrong` asks for the strongest card per reason, and the student types one line on why it counts), one counterclaim from the other tray and the answer to it. The filled slots become an outline on the left. On the right the student writes the argument out as one paragraph of five to eight sentences, starting with a sentence or two that sets up the question for a reader who has not seen the folder. A five-box guide sits under it: opens with the question and the claim; two reasons; each reason names its evidence and where it comes from; the other side's best point and an answer; words that link the parts (because, for example, however). The tool cannot mark the paragraph, so the coach's sheet and the guide do that job. It can be read aloud.

**Pair prep.** Two students each take a side; then they swap objections.

At 1366x768 the folder and trays fit side by side; at 680x425 the folder is a tab.
**On your own.** The last folder, Later School Start, runs with the coach quiet: the coach's sheet and the guide are closed, the meter gives no hints, each source rating and each strongest-card pick takes one answer, and nothing is marked until the paragraph is in. The guide opens afterward for the student's own check.

**The end.** A results strip for the teacher on the last folder: W.6.1a, the paragraph with the guide boxes the student ticked (opens with the question, states the claim, reasons in an order that makes sense); W.6.1b, sources rated right out of the folder's cards, strongest-card picks right out of the reasons, and the "why it counts" lines; then the counts for the four folders before.

## Content
Folders (summaries written for Curio Class from the sources):
- Phones at Lunch: Beland and Murphy (2016, Labour Economics) found that after English schools banned phones, test scores rose, most for lower-achieving students; other cards: students use phones to stay in touch with family; phones are used for lunch payments or schedules at some schools; a practice survey (made up, labeled) of a school's students.
- Year-Round School: Cooper and others (2003, Review of Educational Research) found modified calendars had a small positive effect on achievement, larger for students from low-income families; other cards: summer jobs and camps, building costs, family schedules.
- School Uniforms: Brunsma and Rockquemore (1998, Journal of Educational Research) found no direct effect of uniforms on behavior or achievement; other cards: cost for families, a sense of belonging, freedom of expression.
- Later School Start: the American Academy of Pediatrics (2014, Pediatrics) recommended that middle and high schools start at 8:30 a.m. or later so that students can get enough sleep; the CDC reported in 2015 that most U.S. middle and high schools started earlier than that; other cards: bus routes and their cost, after-school jobs, sports and daylight, family work schedules.
- The practice folder ("Should our school start a pet club?") is labeled made up.
- Every folder has 10 to 12 cards: at least three For, three Against, one Doesn't help and two weak-source cards (made up and labeled: an unsigned online post and an ad from someone who gains), and at least seven keyed objections so five can be asked and two held in reserve.
- What a wrong answer on the last folder means: rating a weak source strong when it agrees with the student's side means the student judges a source by its answer and not by who wrote it and how they know; picking the most striking card over the one that fits the reason means evidence is being chosen for effect and not for relevance; a paragraph that opens with the claim and never sets up the question means the student has not yet seen the reader as someone new to the topic.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards can move between trays any time; the meter updates.
- With Motion off the meter needle jumps.
- Access: every action works by tap and by keyboard. Cards can be dragged, or picked with a tap and placed with a tap on a tray. Ratings are words (Strong, Okay, Weak) and the meter shows its reading in words under the needle, never color alone. Motion can be paused.
- On your own: one answer for each rating and pick, no feedback until the paragraph is in.

## Look
- Accent `--brand` #8a3d00 desk brown (header, desk, trays); gold #f4c542 (the meter's even band, the whistle); paper #fbf5ef; ink #2a1300; muted #66564a. Scene: a library corner with a wooden desk.
- Contrast (WCAG 2.1, computed): white on brand 7.64:1; brand on paper 7.06:1; ink on paper 16.29:1; muted on paper 6.48:1; ink on gold 10.84:1.
- Never color alone: trays have words; the meter has words at both ends.
- Different from this batch (lab teal, thermometer red, x-ray blue, night indigo).

## Art
- People art goes to Gemini: Coach Rivera (a Puerto Rican woman in her thirties with a whistle and a team jacket), 4 poses; "illustrated friendly debate coach <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): library desk with two trays and a podium (1); a cafeteria with no people (1); a school calendar on a wall (1); a closet of school uniforms on hangers (1).
About 8 images. Drawn in code: cards, trays, meter, argument card.

## Voice
Bank voice `hero-coach` as Coach Rivera (unique in this batch); evidence cards are read by `smooth-narrator` (unique in this batch). `Curio.voice` with `scope: () => state.folder + ':' + state.view + ':' + state.card`, `welcomeAfter: true`.
- how `welcome`: "A good debater knows both sides. Build For and Against first, then I'll push back."
- event, whole, `card`: the tapped card.
- event `objection`: the coach's objection.
- event `rebutted`: "Good answer. Next one."
- event `lopsided`: "The {Against} side is lighter." On a second ask: "The {Against} side needs {a reason}."
- how `rate`: "Tap Strong, Okay or Weak for this source. Then tap why."
- how `write`: "Now write it out as a paragraph. Check the guide when you finish."
- event `fair`: "That's a fair fight. Now pick your side."
- event, whole, `argument`: the student's argument.
Read speaks the hint, which names the next action and control and never a disabled one.
- how `own`: "This folder is on your own. I will read it when you finish."
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
evidence (`__tool.ev`), described in full in tools/theme-ledger/spec.md. This tool uses: Source pack (one folder per question), Claims with `ev.claimCheck`, Evidence links with `side`, rebuttal links, `ev.fairFight`, and Draft with `ev.pickStrong` and `ev.draftChecks`. This is the Sides part of the engine named for this tool. Not Spans, Series, Ledger view or Board view. The coach's objections are tool-only keyed lines per card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sources | Rate everything Strong | Two cards per folder are weak and others only okay; one change is allowed, then the card is marked "coach rated" on the printout. |
| Sides | Put every card on one side | The meter stays lopsided and blocks picking a side. |
| Objections | Drag cards until one sticks | One free miss, then the coach shows it, the pair is marked and another objection is added; a written rebuttal is needed either way. |
| Fair fight | Follow the hint; pad the weaker side with Doesn't help cards | The first hint names only the side; cards keyed Doesn't help or weak don't count toward the meter. |
| Argument | Skip the counterclaim; leave the paragraph short | `ev.draftChecks` needs a counterclaim and its answer; the paragraph box needs five sentences before the guide opens, and it prints beside the outline. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the folder: question, `welcome` (queued, first time). `rate` on the first card.
2. Cards: `card` (whole).
3. Objections: `objection`, then `rebutted` per answer.
4. Meter: `lopsided` or `fair`.
5. Argument: `write`; `argument` (whole) on Play.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| W.6.1 wording; C3 D3.4.6-8 and D4.1.6-8 wording | thecorestandards.org, Writing Grade 6; C3 Framework (NCSS 2013) | CCSS ELA 2010 PDF; NCSS C3 Framework PDF | yes |
| After English schools banned phones, test scores rose, most for low-achieving students | Beland and Murphy (2016), "Ill Communication", Labour Economics 41 | LSE Centre for Economic Performance, discussion paper 1350 (2015) | yes |
| Modified (year-round) calendars had a small positive effect, larger for low-income students | Cooper, Valentine, Charlton and Melson (2003), Review of Educational Research 73(1) | ERIC record for the same review | yes |
| Uniforms had no direct effect on behavior or achievement in a national sample | Brunsma and Rockquemore (1998), Journal of Educational Research 92(1) | ERIC record for the same article | yes |
| A strong argument acknowledges and answers counterclaims | Purdue OWL, counterarguments | ReadWriteThink, persuasive and argument writing | yes |
Backed twice: 5. Cut: 0.

Sensitivity note: school uniforms and phone rules touch family cost and home contact; cards present both sides and no folder is framed as the right answer.

Checks run (Python, scratchpad b19, 2026-11-09): every folder has at least three cards on each side and one Doesn't help card; every objection has at least one keyed rebuttal card; contrast as in Look.

Spec fix checks (2026-11-10): card counts per folder as listed (3 + 3 + 1 + 2 is 9, so 10 to 12 leaves room for extra side cards); 7 keyed objections cover 5 asked plus 2 added after misses. The two Later School Start sources were named from memory in this pass and must be opened and confirmed at Build, as must the claim rows below.

## Done when
1. Focus and fold: at 1366x768 folder and trays fit; at 680x425 the folder is a tab.
2. Cards sort onto For, Against and Doesn't help, with each side's claim written as a sentence and a reason per side. (D3.4.6-8)
3. Every card's source is rated with a reason; weak cards cannot be a reason's strongest card; each chosen card has a typed "why it counts" line. (W.6.1b)
4. Five objections each take a card and a written rebuttal; a second miss marks the pair and adds an objection. (D4.1.6-8)
5. The fair-fight meter blocks picking a side until even; its first hint names only the lighter side. (D4.1.6-8)
6. The argument is filled as slots and then written as a paragraph of five or more sentences checked against the guide. (W.6.1a, W.6.1b)
7. The practice folder opens with the coach's sheet, which can be reopened in any folder.
8. Pair prep splits sides and swaps objections.
9. Print shows the prep sheet, the ratings and the paragraph.
10. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
11. Motion off: the meter needle jumps; no network requests.
12. The last folder runs with the coach's sheet and guide closed and one answer for each rating and pick; the end screen shows the result for W.6.1a and W.6.1b. (W.6.1a, W.6.1b)
13. Every spoken instruction is also on screen; each key word shows with an example at first use; the sentence frames can be left.
14. Every action works by keyboard as well as tap, drags have a tap way, nothing is shown by color alone, and motion can be paused.

## Open questions
- None for Cory.
