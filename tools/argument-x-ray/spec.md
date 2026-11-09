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
- Driver: one student; pairs compare scans in class mode (tool.json `driver: "student"`). Every sentence is read on tap.
- Three op-eds written for Curio Class: "Recess Before Lunch" (based on real studies), "Ban Homework in Sixth Grade" (practice, made up) and "Every School Needs a Garden" (practice, made up). tool.json `modes: ["Scan", "Compare scans"]`, `minutes: "20-30"`, `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the skeleton and the crack report.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.6.8 (trace the argument) | Tag each sentence claim, reason, evidence or other | the skeleton glowing through the page | 2 |
| RI.6.8 (trace specific claims) | Link each piece of evidence to the reason it supports, and each reason to the claim | bones joined on the light box | 3 |
| RI.6.8 (supported or not) | Run the scan and judge each crack: reason with no evidence, evidence that doesn't fit, a sentence that only sounds like proof | crack marks with labels | 4 |
| RI.6.8 (evaluate) | Write a two-sentence report: which reason is strongest and which is weakest, naming a bone | the report card | 5 |

## Screens and modes
Header (kit): title "Argument X-Ray"; `Tag`, `Link`, `Scan`, `Report`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A dim radiology room with a glowing light box, the op-ed clipped to it like a film, and Dr. Kofi Mensah, a radiologist in scrubs, in a small portrait beside the box. First hint: "Tap the op-ed's title to hear it." The first tap reads the title; the welcome is queued after it (`welcomeAfter: true`).

**Tag.** Sentences are numbered. The student taps a sentence and picks Claim, Reason, Evidence or Other. Tagged sentences glow as bones (claim is the spine, reasons are ribs, evidence is the small bones). The tag key is checked only at Scan.

**Link.** The student drags from an evidence bone to a reason rib, and from a rib to the spine. Links use the evidence engine's Evidence links with `tag` set to the student's tag.

**Scan.** The scan sweeps down the box (Motion off: it appears at once). The engine's checks find:
- unexplained: a reason rib with no evidence linked ("This rib has nothing holding it up.");
- offKey: evidence linked to a reason it doesn't support, by the keyed links ("This bone doesn't fit this rib.");
- sounds like proof: a sentence the student tagged Evidence that the key marks as opinion in disguise ("Everyone knows...", "Studies show..." with no study named). The student confirms or changes each.
A crack can be fixed by changing a tag or a link, or kept as a real weakness of the op-ed ("The author left this unsupported").

**Report.** Two frames: "The strongest reason is ___ because ___." and "The weakest reason is ___ because ___." Each blank needs a bone tapped from the skeleton.

**Compare scans.** Two students' skeletons side by side; differences glow.

At 1366x768 the light box and panel fit side by side; at 680x425 the panel is a tab.

## Content
Written for Curio Class:
- "Recess Before Lunch" (about 350 words): claim (schools should schedule recess before lunch); reasons (kids eat more fruits and vegetables; less food is thrown away; kids are calmer after lunch); evidence from Price and Just (2015), a Utah study of seven schools where switching recess before lunch raised fruit and vegetable eating by about 54 percent; one keyed weakness ("Teachers love it" with no evidence) and one sentence that only sounds like proof ("Experts agree this is best for every child").
- Two practice op-eds labeled "practice, made up" with keyed skeletons and cracks.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Tags and links can be changed any time; the scan reruns on demand.
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
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
evidence (`__tool.ev`), described in full in tools/theme-ledger/spec.md. This tool uses: Source pack (one op-ed), Spans (sentences), Claims (the op-ed's claim, keyed), Evidence links (span to reason, reason to claim, with `tag`), `ev.checks` (unexplained, offKey), and the Board view (drawn as the skeleton). Not Draft, Sides, Series or Ledger view. The "sounds like proof" check is tool-only code from keyed spans.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tags | Tag everything Evidence | The scan shows the spine missing and every keyed reason unlinked. |
| Links | Link everything to one rib | offKey cracks fire for links outside the key. |
| Cracks | Fix every crack by deleting links | A rib with no links still cracks; keeping it needs "the author left this unsupported". |
| Report | Tap any bone | The reason must be a rib, and the "because" blank needs a bone linked to it. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the title: title, `welcome` (queued, first time).
2. Tag and link: `sentence` (whole) on tap.
3. Scan: `unexplained`, `offKey`, `soundsLike` in order down the page.
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

## Done when
1. Focus and fold: at 1366x768 light box and panel fit; at 680x425 the panel is a tab.
2. Tags turn sentences into spine, ribs and bones. (RI.6.8)
3. Links join bones to ribs and ribs to the spine. (RI.6.8)
4. The scan finds unexplained, offKey and sounds-like-proof cracks; each can be fixed or kept. (RI.6.8)
5. The report needs a rib and a linked bone for strongest and weakest. (RI.6.8)
6. Compare scans shows two skeletons and their differences.
7. Print shows the skeleton and crack report.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the scan doesn't sweep; no network requests.

## Open questions
- None for Cory.
