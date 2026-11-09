# Claim Court

## One idea
An author's article is on trial: as the court clerk, the student drags each reason and piece of evidence from the article ("Our Middle School Should Start Later") to the point banner it supports and marks it strong, weak or off topic, the judge cross-examines any link that doesn't fit ("How does a fact about bus costs hold up a point about sleep?"), and on the verdict board a point with only weak support wobbles until the student writes one sentence per point explaining how the author backs it up, so they learn to see how an author uses reasons and evidence and to spot evidence that supports nothing.

## Not like
- quote-picker (4, spec): choosing quotes for the student's own writing. Here judging an author's support.
- main-idea-pinboard (3-5, spec): main ideas and details. Here an argument's points and their support.
- argument-x-ray (6, concept): color-coding an op-ed. Here grade 5, linking support to points in a courtroom.
- research-rover (4, spec): gathering notes from sources. Here weighing one author's support.
- radio-hour-notes (concept): listening to a speaker. Here reading an article.

## Who and how
- Grade 5, ELA, module "Reasons and Evidence" (Reading Informational Text). Standard: RI.5.8.
- Driver: one student, or the class as a jury (tool.json `driver: "student"`). Every sentence is read on tap.
- Two cases: "Our Middle School Should Start Later" and "Our Town Needs Bike Lanes on Main Street". tool.json `modes: ["Solo", "Jury"]`, `minutes: "25-35"`, `grades_label: "Grade 5"`.
- Nothing is saved; `Print` prints the verdict board.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.5.8 (which reasons support which points) | Drag each reason and piece of evidence to the point banner it supports | evidence cards pinned under three banners | 2 |
| RI.5.8 (how) | Mark each link strong, weak or off topic, and answer the judge's cross-examination | the mark on each card and the judge's question | 3 |
| RI.5.8 (spot what supports nothing) | Send off-topic evidence to the "Supports nothing" box | the box | 4 |
| RI.5.8 (explain) | Write one sentence per point on how the author backs it up | the verdict board with three sentences | 5 |

## Screens and modes
Header (kit): title "Claim Court"; `Cases`, `Verdict`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A small courtroom with a bench, three banners hanging over it and the article lying on the bench, and Judge Amara Sol, a calm judge in a black robe with reading glasses. First hint: "Tap a case to open the article." The first tap reads the article's title; the welcome is queued after it (`welcomeAfter: true`).

**The article.** About 450 words in numbered paragraphs (tap a sentence to hear it). Its claim sits on top; its three points hang as banners (for the start time case: Teens need more sleep than they get; Rested students do better in class; The change can work for families).

**Link.** The student picks a span (tap the first and last word, inside one paragraph) and drags it to a banner. Each link is an evidence link (`ev` Evidence links) with the point as its claim. A link the case key rates 0 for that point (`offKey`) brings the judge's cross-examination: "How does {a fact about bus costs} hold up {a point about sleep}?" with three answers: "It doesn't; move it", "It does, because..." (a type box) and "It belongs to another point". The student may keep a link with a typed because.

**Mark.** Each link gets strong (a number or study that shows the point), weak (an opinion, a single story, or a fact only near the point) or off topic. The key has a mark per span; a mark that differs gets "One reading calls this {weak}: it's {one family's story}." The student may keep theirs.

**Supports nothing.** Two spans in each article back no point (a line about the school's new paint; a quote that only repeats the claim). They go to a box under the bench.

**Verdict board.** Board view: each banner with its cards stacked under it and a coverage meter (`ev.coverage`, share of the key's strong spans the student linked). A banner with only weak cards wobbles. The student writes one sentence per point ("The author backs up the sleep point with a doctors' group's advice and a sleep study."); `ev.claimCheck` asks again for a sentence that's only a topic, and the sentence must name at least one kind of support (a number, a study, an expert, an example, a story) from a chip row.

**Jury.** The class votes on the weakest point with a show of hands entered as counts; the board shows the tally.

At 1366x768 the article and banners fit side by side; at 680x425 the banners are a tab.

## Content
Written for Curio Class from sourced facts:
- Start time case: the claim (our middle school should start at 8:30 or later). Point 1 support: a doctors' group (the American Academy of Pediatrics) recommends middle and high schools start at 8:30 a.m. or later; sleep experts say teens need 8 to 10 hours of sleep a night; at puberty, body clocks shift so teens tend to fall asleep later. Point 2 support: a CDC report found most middle and high schools in the United States started before 8:30 in 2011-12; a student's own story of falling asleep in first period (weak). Point 3 support: California passed a law in 2019 so that by 2022 most public middle schools start no earlier than 8:00 and high schools no earlier than 8:30; one parent's worry about later pickups (weak, and it argues the other way). Off topic: the new paint; a line that only restates the claim.
- Bike lanes case: points on safety, health and local shops, with a mix of strong and weak support (written for Curio Class from Federal Highway Administration and CDC facts; numbers checked twice before use).
- Keys: each paragraph and span rated 0 to 3 per point, with a mark.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Links can be moved or removed any time.
- Marks and checks are advice; nothing is refused, but a banner wobbles until it has at least one strong card.
- With Motion off a weak banner shows a "weak" label instead of wobbling.

## Look
- Accent `--brand` #5e2a2a courtroom mahogany (header, bench, banner rods); gold #f4c542 (strong marks, the gavel); paper #faf4f3; ink #211010; muted #625251. Scene: a warm wood courtroom.
- Contrast (WCAG 2.1, computed): white on brand 11.41:1; brand on paper 10.49:1; ink on paper 16.84:1; muted on paper 6.78:1; ink on gold 11.26:1.
- Never color alone: marks are words; the meter shows a number.
- Different from this batch (detective navy, stage pink, film sepia, track teal).

## Art
- People art goes to Gemini: Judge Amara Sol (a South Asian woman in her fifties, black robe, reading glasses), 4 poses; the clerk seen from behind at a desk (1); "illustrated courtroom character <description> <pose>, warm gouache, plain white background"; 1:1; cutout yes. Topic scenes: a sleepy class at 7:30 a.m. and a street with a bike lane (2), "children's book illustration <scene>, no text"; 4:3.
- Local FLUX (`scripts/localart.py`): courtroom (1), gavel (1); no people.
About 9 images. Drawn in code: banners, cards, meter, box.

## Voice
Bank voice `calm-professor` as Judge Sol (unique in this batch); the articles are read by `news-reader` (unique in this batch). `Curio.voice` with `scope: () => state.case + ':' + state.point + ':' + state.link`, `welcomeAfter: true`.
- how `welcome`: "This article makes three points. Clerk, show me what holds up each one."
- event, whole, `sentence`: the tapped sentence.
- event `cross`: "How does {a fact about bus costs} hold up {a point about sleep}?"
- event `markDiff`: "One reading calls this {weak}: it's {one family's story}."
- event `nothing`: "Into the box. This supports nothing."
- event `wobble`: "{Rested students do better} is wobbling. It needs something strong."
- how `verdictHow`: "Write one sentence for each point: how does the author back it up?"
- event `verdict`: "Court is adjourned. Every point is explained."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
evidence (`__tool.ev`), described in full in tools/theme-ledger/spec.md. This tool uses: Source pack (two articles with keys), Spans, Claims (the three points; `ev.claimCheck` for the verdict sentences), Evidence links (with a mark as `tag`), checks (`offKey` drives the cross-examination; `unexplained` on the because), Strength (`ev.coverage` for the meter, `ev.compare` for marks), Board view. Not Ledger view, Series, Draft or Sides.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Links | Drop every span on one banner | Off-key links are cross-examined; the other banners stay empty and wobble. |
| Marks | Mark everything strong | Marks are compared to the key and differences are named. |
| Supports nothing | Ignore the box | The meter doesn't count them, but the verdict board lists unlinked off-topic spans as "Still on the bench". |
| Verdict sentences | Type the point again | `claimCheck` and the support-kind chip both apply. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a case: title, `welcome` (queued, first time).
2. Sentences: `sentence` (whole). Links: `cross` and `markDiff` as they fire; `nothing`.
3. Verdict: `wobble` per weak banner, `verdictHow`, then `verdict`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.5.8 wording | thecorestandards.org, Reading Informational Text Grade 5 | CCSS ELA 2010 PDF | yes |
| The American Academy of Pediatrics (2014) recommends middle and high schools start at 8:30 a.m. or later | AAP policy statement, "School Start Times for Adolescents", Pediatrics, 2014 | CDC, "Schools Start Too Late" (2015) | yes |
| Teens 13 to 18 need 8 to 10 hours of sleep a night | American Academy of Sleep Medicine, consensus statement (Paruthi and others, 2016) | CDC, sleep in middle and high school students | yes |
| Most US middle and high schools started before 8:30 a.m. in 2011-12 | CDC, Wheaton and others, MMWR, August 2015 | CDC, "Schools Start Too Late" (2015) | yes |
| California law (SB 328, 2019) set start times from July 2022: high schools no earlier than 8:30 a.m., middle schools no earlier than 8:00 a.m. | California Legislative Information, SB 328 (2019) | California Department of Education, school start times | yes |
| At puberty, the body clock shifts so teens tend to fall asleep later | AAP policy statement (2014) | National Sleep Foundation, teens and sleep | yes |
Backed twice: 6. Cut: 1 (an exact share of students who sleep under 8 hours; reported numbers vary by survey year and grade, so the article says "many" and names no number).

Design choices (not claims): the strong, weak and off topic marks and their meanings.

Checks run (Python, scratchpad b15, 2026-11-09): in the sample start time key every point has at least one strong span and at least one weak span, and exactly two spans rate 0 for all three points; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the article and banners fit; at 680x425 the banners are a tab.
2. Spans link to banners. (RI.5.8)
3. Off-key links bring cross-examination; marks are compared to the key. (RI.5.8)
4. The Supports nothing box takes off-topic spans. (RI.5.8)
5. The verdict board shows coverage, wobbles weak banners and checks one sentence per point. (RI.5.8)
6. Jury mode tallies votes.
7. Print shows the verdict board.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: banners show "weak" instead of wobbling; no network requests.

## Open questions
- None for Cory.
