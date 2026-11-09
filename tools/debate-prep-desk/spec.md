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
- Driver: one student; pairs can split sides in class mode (tool.json `driver: "student"`). Every card is read on tap.
- Three folders: Phones at Lunch, Year-Round School, School Uniforms; plus a practice folder labeled made up. tool.json `modes: ["Prep", "Pair prep"]`, `minutes: "25-35"`, `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the two-sided prep sheet and the student's argument.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D3.4.6-8 | Sort evidence cards onto For and Against and write a reason for each side | the two sides with cards and reasons | 2 |
| D3.4.6-8, W.6.1b | For each card, note the source and why it counts | the source line and a "why it counts" chip | 2 |
| D4.1.6-8 | Answer the coach's objections with rebuttal cards | objection and rebuttal pairs | 3 |
| D4.1.6-8 | Balance both sides until the fair-fight meter reads even | the meter | 4 |
| W.6.1a, W.6.1b | Pick a side; write an argument with a claim, two reasons with evidence and one answered counterclaim | the argument card | 5 |

## Screens and modes
Header (kit): title "Debate Prep Desk"; `Folder`, `Sides`, `Objections`, `Argument`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A coach's desk in a school library with a timer, a whistle, a podium in the corner and two trays labeled For and Against. Coach Rivera, the debate coach, sits behind the desk. First hint: "Tap the folder to hear the question." The first tap reads the question; the welcome is queued after it (`welcomeAfter: true`).

**Folder.** Eight to ten evidence cards per question, each a short sourced summary with its source line. The student can open a card to hear it.

**Sides.** The student drags each card to For, Against or Doesn't help, and writes one reason per side that the cards support. Cards are the evidence engine's Evidence links with `side: 'claim'` or `'counter'`.

**Objections.** Coach Rivera raises three objections against whichever side the student has built more ("A study of four English cities isn't your school."). The student answers each by dragging a rebuttal card or writing a rebuttal that names a card; these are rebuttal links.

**Fair fight.** The engine's `ev.fairFight` compares the two sides (cards, reasons, rebuttals) and shows a meter from lopsided to even. The student can't pick a side until the meter reads fair; the hint names what the weaker side needs ("The Against side needs a reason.").

**Argument.** The student picks a side and builds a short argument with the engine's Draft: claim, two reasons with cards (`ev.pickStrong` asks for the strongest card per reason), one counterclaim from the other tray and the answer to it. It can be read aloud.

**Pair prep.** Two students each take a side; then they swap objections.

At 1366x768 the folder and trays fit side by side; at 680x425 the folder is a tab.

## Content
Folders (summaries written for Curio Class from the sources):
- Phones at Lunch: Beland and Murphy (2016, Labour Economics) found that after English schools banned phones, test scores rose, most for lower-achieving students; other cards: students use phones to stay in touch with family; phones are used for lunch payments or schedules at some schools; a practice survey (made up, labeled) of a school's students.
- Year-Round School: Cooper and others (2003, Review of Educational Research) found modified calendars had a small positive effect on achievement, larger for students from low-income families; other cards: summer jobs and camps, building costs, family schedules.
- School Uniforms: Brunsma and Rockquemore (1998, Journal of Educational Research) found no direct effect of uniforms on behavior or achievement; other cards: cost for families, a sense of belonging, freedom of expression.
- The practice folder ("Should our school start a pet club?") is labeled made up.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards can move between trays any time; the meter updates.
- With Motion off the meter needle jumps.

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
- event `lopsided`: "The {Against} side needs {a reason}."
- event `fair`: "That's a fair fight. Now pick your side."
- event, whole, `argument`: the student's argument.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
evidence (`__tool.ev`), described in full in tools/theme-ledger/spec.md. This tool uses: Source pack (one folder per question), Claims with `ev.claimCheck`, Evidence links with `side`, rebuttal links, `ev.fairFight`, and Draft with `ev.pickStrong` and `ev.draftChecks`. This is the Sides part of the engine named for this tool. Not Spans, Series, Ledger view or Board view. The coach's objections are tool-only keyed lines per card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sides | Put every card on one side | The meter stays lopsided and blocks picking a side. |
| Objections | Drag any card as a rebuttal | Each objection has keyed rebuttal cards; others are answered "That doesn't meet the objection." |
| Argument | Skip the counterclaim | `ev.draftChecks` needs a counterclaim and its answer. |
| Fair fight | Pad the weaker side with Doesn't help cards | Cards keyed Doesn't help don't count toward the meter. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the folder: question, `welcome` (queued, first time).
2. Cards: `card` (whole).
3. Objections: `objection`, then `rebutted` per answer.
4. Meter: `lopsided` or `fair`.
5. Argument: `argument` (whole) on Play.

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

## Done when
1. Focus and fold: at 1366x768 folder and trays fit; at 680x425 the folder is a tab.
2. Cards sort onto For, Against and Doesn't help with a reason per side and a source line. (D3.4.6-8, W.6.1b)
3. Objections need keyed rebuttals. (D4.1.6-8)
4. The fair-fight meter blocks picking a side until even and names what's missing. (D4.1.6-8)
5. The argument needs a claim, two reasons with cards and an answered counterclaim. (W.6.1a, W.6.1b)
6. Pair prep splits sides and swaps objections.
7. Print shows the prep sheet and the argument.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the meter needle jumps; no network requests.

## Open questions
- None for Cory.
