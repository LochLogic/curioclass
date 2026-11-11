# Argument X-Ray

## One idea
The student slides an opinion piece onto a light box and x-rays it, tagging each sentence as claim, reason or evidence so the argument's skeleton shows through the page, then links each piece of evidence to the reason it holds up, and the scan shows the cracks: a reason with no evidence, evidence that doesn't fit the reason it's linked to, and a sentence that only sounds like proof, so they learn to trace an author's argument and tell which claims are supported and which are not.

## Not like
- claim-quote-comment (6-8, spec, this batch): building your own paragraph from quotes. Here taking apart someone else's argument.
- debate-prep-desk (6, spec, this batch): preparing both sides with a coach. Here tracing one author's skeleton.
- claim-court (5, spec): judging an author's support for points, grade 5. Here grade 6 with reasons as a middle layer and cracks.
- podcast-listening-club (6-8, spec): arguments by ear. Here on the page.
- logic-gym (7, concept): reasoning errors. Here structure and support.

## Who and how
- Grade 6, ELA, module "Tracing an Argument" (Reading Informational Text). Standard: RI.6.8 (trace and evaluate the argument and specific claims in a text, distinguishing claims that are supported by reasons and evidence from claims that are not).
- Driver: one student; pairs compare scans in class mode (tool.json `driver: "student"`). Role: lesson. Every sentence is read on tap.
- Change note (spec fix, 2026-11-11): the light box, Dr. Mensah, the bones and the cracks stay. Added: Dr. Mensah scans a short sample first as the model; two more op-eds, so there are five; the student stamps each reason "supported" or "not supported" before the scan, which is the standard's own judgment; and a scan now costs something: two scans an op-ed, the first gives only a count. The fifth op-ed is done on your own. Added the three hooks.
- English learners: every spoken line is also on screen in short sentences. The words claim, reason and evidence each show with an example sentence from the sample the first time they are used. The report frames may be taken or left. The op-eds avoid idioms, and any left in for the argument's sake are glossed on tap.
- Five op-eds written for Curio Class: "Recess Before Lunch" (based on real studies) and four labeled "practice, made up": "Ban Homework in Sixth Grade", "Every School Needs a Garden", "Phones Stay in Lockers" and "Start School an Hour Later". tool.json `modes: ["Scan", "Compare scans"]`, `minutes: "40-50"` (two sittings; one or two op-eds a sitting), `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the skeleton and the crack report.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| RI.6.8 (trace the argument) | trace the argument in a text | the student | Tag each sentence claim, reason, evidence or other | 5 op-eds, 12 to 16 sentences each | the skeleton glowing through the page | 2 |
| RI.6.8 (trace specific claims) | trace the specific claims | the student | Link each piece of evidence to the reason it supports, and each reason to the claim | 5 op-eds, 3 reasons each | bones joined on the light box | 3 |
| RI.6.8 (distinguish) | distinguish claims that are supported by reasons and evidence from claims that are not | the student | Stamp each reason "supported" or "not supported" before the scan | 15 reasons (8 supported, 7 not) | the stamps, then the scan's cracks beside them | 4 |
| RI.6.8 (evaluate) | evaluate the argument | the student | Write a two-sentence report: which reason is strongest and which is weakest, naming a bone, then check it against a three-box guide | 5 reports | the report card and guide | 5 |

## Screens and modes
Header (kit): title "Argument X-Ray"; `Tag`, `Link`, `Scan`, `Report`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A dim radiology room with a glowing light box, the op-ed clipped to it like a film, and Dr. Kofi Mensah, a radiologist in scrubs, in a small portrait beside the box. First hint: "Tap the op-ed's title to hear it." The first tap reads the title; the welcome is queued after it (`welcomeAfter: true`).

**Dr. Mensah goes first (the model).** A five-sentence sample, "Walk to School Day", is on the box. Dr. Mensah tags it aloud ("This is what the writer wants: the claim. This says why: a reason. This gives a number from a count: evidence"), links one bone, stamps one reason supported and one not ("Nothing holds this one up"), and runs the scan. It cannot be skipped the first time and `Dr. Mensah's scan` reopens it.

**Tag.** Sentences are numbered. The student taps a sentence and picks Claim, Reason, Evidence or Other. Tagged sentences glow as bones (claim is the spine, reasons are ribs, evidence is the small bones). The tag key is checked only at Scan.

**Link.** The student drags from an evidence bone to a reason rib, and from a rib to the spine. Links use the evidence engine's Evidence links with `tag` set to the student's tag.

**Stamp.** Before any scan, each reason rib needs a stamp from the student: `supported` or `not supported`. The Scan button stays closed until every rib has one.

**Scan.** Each op-ed gets two scans. The first gives counts only: "3 bones are tagged or linked wrong. 1 stamp is wrong." It does not say which. The student goes back and fixes what they can find. The second scan sweeps down the box and names what is still wrong; anything still wrong after it is set by Dr. Mensah and listed on the print as "Dr. Mensah set it". The scan sweeps (Motion off: it appears at once). The engine's checks find:
- unexplained: a reason rib with no evidence linked ("This rib has nothing holding it up.");
- offKey: evidence linked to a reason it doesn't support, by the keyed links ("This bone doesn't fit this rib.");
- sounds like proof: a sentence the student tagged Evidence that the key marks as opinion in disguise ("Everyone knows...", "Studies show..." with no study named). The student confirms or changes each.
A crack can be fixed by changing a tag or a link, or kept as a real weakness of the op-ed ("The author left this unsupported").

**Report.** Two frames: "The strongest reason is ___ because ___." and "The weakest reason is ___ because ___." Each blank needs a bone tapped from the skeleton.

A three-box guide sits under the report: I named a reason, not evidence; my "because" points to a bone on the page (or says none is there); I did not use my own opinion of the topic.

**On your own.** The fifth op-ed, "Start School an Hour Later", has no sample, no hints and one scan, which comes only after tags, links, stamps and report are all in. Nothing is marked before it.

**The end.** A results strip for the teacher, for RI.6.8 part by part on the fifth op-ed: tags right out of 14, links right out of 6, stamps right out of 3, and the report with its guide boxes; then the same counts for the four op-eds before, with anything Dr. Mensah set.

**Compare scans.** Two students' skeletons side by side; differences are outlined and listed in words.

At 1366x768 the light box and panel fit side by side; at 680x425 the panel is a tab.

## Content
Written for Curio Class:
- "Recess Before Lunch" (about 350 words): claim (schools should schedule recess before lunch); reasons (kids eat more fruits and vegetables; less food is thrown away; kids are calmer after lunch); evidence from Price and Just (2015), a Utah study of seven schools where switching recess before lunch raised fruit and vegetable eating by about 54 percent; one keyed weakness ("Teachers love it" with no evidence) and one sentence that only sounds like proof ("Experts agree this is best for every child").
- Four practice op-eds labeled "practice, made up" (their studies and numbers are invented and say so on the page), each about 300 words with one claim, three reasons, a keyed skeleton and keyed stamps:
  - "Ban Homework in Sixth Grade": more sleep (supported, a made-up sleep survey); more family time (not supported, only "Everyone knows families are happier"); higher test scores (not supported, the evidence given is about reading for fun, which does not fit).
  - "Every School Needs a Garden": students try more vegetables (supported); science lessons stick (supported); gardens cost nothing (not supported, no evidence and a cost is named later in the piece).
  - "Phones Stay in Lockers": fewer class interruptions (supported, a made-up count by one school); better grades (not supported, "Studies show" with no study named); students talk more at lunch (supported, a lunchroom tally).
  - "Start School an Hour Later" (on your own): students sleep more (supported); fewer late arrivals (supported); buses would cost less (not supported, a confident sentence with no number).
- "Recess Before Lunch" stamps: eat more fruits and vegetables (supported); less food thrown away (supported); teachers love it (not supported). Across the five op-eds 8 reasons are supported and 7 are not; no op-ed is all one stamp.
- What a wrong answer on the fifth op-ed means: stamping the bus reason "supported" means the student takes a confident sentence for evidence; tagging the claim as a reason means the student has not found what the writer wants; linking evidence to a reason on the same topic that it does not back means the student matches words, not support; naming evidence as the strongest "reason" means the two words are not yet apart.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Tags, links and stamps can be changed any time before a scan. Each op-ed has two scans (the fifth has one); the first gives counts only.
- Access: every action works by tap and by keyboard. A link can be dragged, or made with a tap on the bone and a tap on the rib. Cracks are drawn as a jagged line with a word label, and stamps are words, never color alone. Motion can be paused. Every sentence heard is the sentence shown.
- With Motion off the scan line doesn't sweep.

## Look
- Accent `--brand` #1c4f6e x-ray blue (header, light box frame, bones); gold #f4c542 (cracks, the spine glow); paper #f1f5f8; ink #0a1a24; muted #4c5862. Scene: a dim radiology room around a bright light box.
- Contrast (WCAG 2.1, computed): white on brand 8.78:1; brand on paper 8.01:1; ink on paper 16.15:1; muted on paper 6.65:1; ink on gold 10.89:1.
- Never color alone: bones carry tag words; cracks have labels.
- Different from this batch (lab teal, thermometer red, night indigo, desk brown).

## Art
- People art goes to Gemini: Dr. Kofi Mensah (a Ghanaian American man in his fifties in blue scrubs), 3 poses; "illustrated friendly doctor <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): radiology room with a light box (1); a schoolyard at noon with no people (1).
About 5 images. Drawn in code: bones, links, cracks, scan line.

## Voice
Bank voice `clear-teacher` as Dr. Mensah (unique in this batch); the op-eds are read by `casual-peer` (unique in this batch). `Curio.voice` with `scope: () => state.oped + ':' + state.view + ':' + state.sentence`, `welcomeAfter: true`.
- how `welcome`: "Every argument has a skeleton. Tag each sentence, link the bones, then scan for cracks."
- event, whole, `sentence`: the tapped sentence.
- event `unexplained`: "This rib has nothing holding it up."
- event `offKey`: "This bone doesn't fit this rib."
- event `soundsLike`: "That sounds like proof. Does it name any?"
- how `reportHow`: "Which reason is strongest? Which is weakest? Tap a bone for each."
- how `stamp`: "Stamp each reason: supported or not supported."
- event `count`: "Some bones are not right yet. Look again before your second scan."
- how `own`: "This one is on your own. You get one scan at the end."
- event, whole, Dr. Mensah's scan.
Every `how` line is also shown as text beside its control. Instructions use no idioms.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
evidence (`__tool.ev`), described in full in tools/theme-ledger/spec.md. This tool uses: Source pack (one op-ed), Spans (sentences), Claims (the op-ed's claim, keyed), Evidence links (span to reason, reason to claim, with `tag`), `ev.checks` (unexplained, offKey), and the Board view (drawn as the skeleton). Not Draft, Sides, Series or Ledger view. The "sounds like proof" check is tool-only code from keyed spans.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tags | Tag everything Evidence | The scan shows the spine missing and every keyed reason unlinked. |
| Links | Link everything to one rib | offKey cracks fire for links outside the key. |
| Scan | Rerun the scan and edit until no crack shows | Two scans an op-ed; the first gives only counts, and what the second still finds is set by Dr. Mensah and printed as his. |
| Stamps | Stamp every reason supported; stamp every one not | 8 of 15 are supported and no op-ed is all one stamp; stamps are set before the scan. |
| Cracks | Fix every crack by deleting links | A rib with no links still cracks; keeping it needs "the author left this unsupported". |
| Report | Tap any bone | The reason must be a rib, and the "because" blank needs a bone linked to it. |
| On your own | Use the first scan's count to hunt | The fifth op-ed has one scan, after everything is in. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the title: title, `welcome` (queued, first time), then Dr. Mensah's scan (whole), waits.
2. Tag and link: `sentence` (whole) on tap. `stamp` when the last link is made.
3. First scan: `count`. Second scan: `unexplained`, `offKey`, `soundsLike` in order down the page. Fifth op-ed: `own`.
4. Report: `reportHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.6.8 wording | thecorestandards.org, Reading Informational Text Grade 6 | CCSS ELA 2010 PDF | yes |
| Moving recess before lunch raised fruit and vegetable eating (about 54 percent) and cut waste in Utah schools | Price and Just (2015), "Lunch, recess and nutrition", Preventive Medicine 71 | Brigham Young University news release on the study (2015) | yes |
| An argument has a claim, reasons and evidence; unsupported claims lack reasons or evidence | Purdue OWL, argumentative essays | ReadWriteThink, persuasion and argument | yes |
Backed twice: 3. Cut: 0.

Design choices (not claims): two op-eds are practice, labeled made up on screen.

Checks run (Python, scratchpad b19, 2026-11-09): every sample op-ed key has at least one unexplained rib and one sounds-like-proof sentence; the recess op-ed has 3 reasons and 1 claim; contrast as in Look.
Spec fix checks (2026-11-11), counted not run: 5 op-eds with 3 reasons each is 15 stamps; supported 2 + 1 + 2 + 2 + 1 is 8 and not supported is 7. The four practice op-eds and the sample are made up and say so; only "Recess Before Lunch" cites a real study.

## Done when
1. Focus and fold: at 1366x768 light box and panel fit; at 680x425 the panel is a tab.
2. Tags turn sentences into spine, ribs and bones on five op-eds. (RI.6.8)
3. Links join bones to ribs and ribs to the spine. (RI.6.8)
4. Every reason is stamped supported or not supported before a scan; the first scan gives counts only, the second names what is left, and anything still wrong is printed as set by Dr. Mensah. (RI.6.8)
5. The report needs a rib and a linked bone for strongest and weakest, and is checked against the three-box guide. (RI.6.8)
6. Dr. Mensah's sample scan plays first and can be reopened.
7. The fifth op-ed runs with no sample or hint and one scan at the end; the end screen shows tags, links, stamps and report for it. (RI.6.8)
8. Compare scans shows two skeletons and their differences in words.
9. Print shows the skeleton, the stamps, the crack report and anything set by Dr. Mensah.
10. Every spoken instruction is also on screen; claim, reason and evidence each show with an example at first use; the report frames can be left.
11. Every action works by keyboard as well as tap, links have a tap way, nothing is shown by color alone, and motion can be paused.
12. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
13. Motion off: the scan doesn't sweep; no network requests.

## Open questions
- None for Cory.
