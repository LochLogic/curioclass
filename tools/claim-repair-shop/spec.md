# Claim Repair Shop

## One idea
Broken explanations of why the Berlin Wall opened on November 9, 1989 come into a repair shop, each with a fault: sources that contradict each other, steps out of order, a claim too vague to test, a single cause standing in for many, or evidence from a source that can't know; on a bench beside the workbench sit real sources (Reagan's 1987 speech, Gorbachev's reforms, Hungary cutting its border fence in May 1989 and opening the border in September, the Leipzig march of October 9, Gunter Schabowski's muddled press conference on the evening of November 9, the border guard at Bornholmer Strasse who opened the gate that night); the student tags each fault, checks it against the bench, and repairs the explanation by swapping evidence, reordering steps or narrowing the claim, with faults getting subtler level by level; at the end the student writes their own explanation and the shop runs the same checks on it, so a tenth grader learns to draw on many sources and use their conflicts to revise a claim, to critique the credibility of claims and evidence, and to critique reasoning, order and detail.

## Not like
- alliance-web (9, spec): the causes of World War I. Here a 1989 event, and the fault is in the explanation.
- cold-war-crisis-room (10, concept): choices in 1962. Here explanations of 1989.
- behind-the-podcast (11, concept): tracing a secondary work's sources. Here repairing short claims.
- colonial-newsroom (8, spec): building slanted pages. Here fixing broken arguments.

## Who and how
- Grade 10, Social Studies (History, Inquiry), module "Claim Repair Shop". Standards: D3.3.9-12 (identify evidence that draws information directly and substantively from multiple sources to detect inconsistencies in evidence in order to revise or strengthen claims), D4.4.9-12 (critique the use of claims and evidence in arguments for credibility), D4.5.9-12 (critique the use of the reasoning, sequencing, and supporting details of explanations).
- Format: puzzle. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Eight broken explanations in rising difficulty, the source bench of twelve, five fault tags, the open repair. Extra: Break one (a student breaks an explanation on purpose for a partner to repair; printed with the answer hidden). tool.json `modes: ["Repair shop", "Break one"]`, `minutes: "25-35"`, `grades_label: "Grade 10"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D3.3.9-12 | Check a claim against several bench sources, find where they conflict, and revise | the bench with conflicts highlighted; the revised claim | 2 |
| D4.4.9-12 | Tag credibility faults (a source that couldn't know, a memoir written decades later, a single side) and swap in better evidence | the credibility tag; the source's date and author card | 3 |
| D4.5.9-12 | Tag sequence, vague-claim and missing-detail faults, then reorder steps or add details | the step strip; the claim narrowing; the detail slots | 4 |

## Screens and modes
Header (kit): title "Claim Repair Shop"; `Repair shop`, `Break one`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A workbench with a cracked explanation on it: "The Berlin Wall fell because Reagan said 'tear down this wall.'" Beside it, a bench of source cards and a rack of five fault tags (contradiction, credibility, sequence, vague claim, missing detail). The welcome is queued (`welcomeAfter: true`): "Welcome to the shop. Explanations come in broken. Your job: find the fault, check the sources, and fix it. Tap the cracked explanation." First hint: "Tap the explanation on the bench."

**The bench (focus: the workbench and sources).** At 1366x768 the explanation sits center with the bench at the right; at 680x425 the bench is a sheet. Twelve real sources, each with an author, date and kind:
1. Reagan's speech at the Brandenburg Gate, June 12, 1987.
2. Gorbachev's reforms from 1985 (glasnost and perestroika), and his 1988 United Nations speech saying nations should choose their own path.
3. Hungary begins cutting its border fence with Austria, May 2, 1989.
4. The Pan-European Picnic on the Austrian border, August 19, 1989, where hundreds of East Germans crossed.
5. Hungary opens its border to East Germans, September 11, 1989.
6. East Germans in the West German embassy in Prague allowed to leave, September 30, 1989.
7. The Leipzig Monday march of October 9, 1989, about 70,000 people, with no shooting.
8. Erich Honecker forced out, October 18, 1989.
9. The Alexanderplatz rally in East Berlin, November 4, 1989.
10. Schabowski's press conference, November 9, 1989, around 7 p.m., answering that new travel rules applied "immediately" when they were meant for the next day.
11. Harald Jager, the officer at Bornholmer Strasse, opening the gate about 11:30 p.m. as crowds grew.
12. A memoir written 25 years later by a person who was there (a real published memoir, labeled with its date).

**Levels (focus: the explanation).** Eight explanations, each with one main fault, getting subtler:
1. Single cause and sequence: "Reagan's speech made the Wall fall." (two years apart; many steps between)
2. Vague claim: "Communism just stopped working."
3. Sequence: "After the Wall opened, Hungary opened its border." (reversed)
4. Contradiction: two sources disagree on whether the guards were ordered to open the gates; the student finds the order never came.
5. Credibility: a claim backed only by the late memoir, where a dated source exists.
6. Missing detail: "People protested and the government gave in." (which people, where, when?)
7. Contradiction across kinds: a news report of the time and a later history disagree on the size of the Leipzig march; the student picks how to word the claim.
8. Mixed: a plausible paragraph with a subtle sequence slip and an overclaim.
- For each, the student tags the fault, drags bench sources in as evidence, and repairs: reorder steps on a strip, narrow the claim with tiles, or swap a weak source for a stronger one. A gauge shows the explanation's strength rising.

**The open repair (the aha).** The student writes their own explanation of why the Wall opened on November 9, 1989, using at least four bench sources in order. The shop runs the five checks on it and shows strengths and weak spots, without a single grade. Narrator: "A strong claim isn't the loudest one. It's the one that survives the checks."

**The end.** The eight repaired explanations and the student's own with its check report. `Print` prints them.

**Break one (extra).** The student takes a strong explanation and breaks it on purpose with one fault; it prints with the answer hidden for a partner.

## Content
- Twelve real sources with authors, dates and kinds; eight broken explanations with one designed fault each; five fault tags; repair tiles; the check report; the Break one template.
- All sources, dates, quotes and figures are real and sourced; quotes are under 15 words.
- The explanations are written for this game and labeled so.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A wrong tag plays a hint pointing back at the bench, not the answer.
- Each level opens after the last is repaired; repaired levels can be revisited.
- Keyboard: Tab to the explanation, tags, bench sources, the step strip and tiles; Enter to tag, drag and place.
- With Motion off the gauge fills at once and cracks don't animate.

## Look
- Accent `--brand` #2d5d4b workbench green (header, the bench, tags); gold #f4c542 (the tag in hand, a highlighted conflict); paper #f0f6f3; ink #0a1f18; muted #4f5a55.
- Contrast (WCAG 2.1, computed): white on brand 7.56:1; brand on paper 6.90:1; ink on paper 15.70:1; muted on paper 6.56:1; ink on gold 10.57:1.
- Never color alone: fault tags carry icons and words; conflicts are underlined and labeled.
- Different from this batch (wallet maroon, sea teal, terracotta, circuit violet).

## Art
- Public domain or freely licensed where checked (Reagan Library, Bundesarchiv items under open license, Wilson Center): Reagan at the Brandenburg Gate (1987); the Bornholmer Strasse crossing (1989); the Leipzig march (1989). Each with credit.
- Local FLUX (`scripts/localart.py`): the repair shop workbench (1, 16:9); Berlin at night, November 1989, a crowd at a gate seen from behind (1, 16:9).
- Drawn in code: source cards, tags, the strip, the gauge, the check report.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as the shop's mechanic and hints; `curious-librarian` as the reader of source cards. `Curio.voice` with `scope: () => state.mode + ':' + state.level + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each explanation.
- event, whole, each source card.
- how `tag`: "Tag the fault, then drag in sources to check it."
- how `repair`: "Repair it: reorder, narrow, or swap in a stronger source."
- how `open`: "Write your own explanation with four sources in order."
- event, whole, the check report.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the workbench, the source bench, fault tags, the repair tools, the strength gauge, the check report.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tags | Try every tag | Each wrong tag costs a hint and the level needs a source dragged in as proof. |
| Repair | Paste in every source | The check flags sources that don't support the claim. |
| Open repair | Copy a repaired explanation | The check notes it, and asks for a new order of at least four sources. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). The explanation (whole), waits; source cards (whole) as opened.
2. `tag`; `repair`, for each level.
3. `open`; check report (whole).
4. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D3.3.9-12, D4.4.9-12 and D4.5.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Reagan's Brandenburg Gate speech, June 12, 1987 | Ronald Reagan Presidential Library, speech text | National Archives | yes |
| Gorbachev's reforms and his 1988 UN speech | Wilson Center Digital Archive | Sarotte, "The Collapse" (Basic Books, 2014) | yes |
| Hungary's fence cutting (May 2), the Pan-European Picnic (August 19) and the open border (September 11, 1989) | Sarotte (2014) | Bundeszentrale fur politische Bildung, "Chronik der Mauer" | yes |
| The Prague embassy departures (September 30) and Honecker's fall (October 18) | Chronik der Mauer | Britannica, "Berlin Wall" | yes |
| The Leipzig march of October 9, about 70,000 | Leipzig Contemporary History Forum (Zeitgeschichtliches Forum) | Sarotte (2014) | yes |
| Schabowski's press conference and the word "immediately" | Chronik der Mauer, transcript | Wilson Center Digital Archive | yes |
| Harald Jager opened Bornholmer Strasse about 11:30 p.m. | Sarotte (2014) | Berlin Wall Memorial (Stiftung Berliner Mauer) | yes |
Backed twice: 8. Cut: 0.

Checks run (Python, scratchpad r18, 2026-11-09): bench sources in date order from June 1987 to November 1989; 29 months from Reagan's speech to the opening; each of five fault tags is the main fault of at least one level; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 explanation and bench; at 680x425 sheet.
2. Contradiction levels need two conflicting sources found and the claim revised. (D3.3.9-12)
3. Credibility levels swap a weak source for a dated, closer one. (D4.4.9-12)
4. Sequence, vague and detail levels are repaired on the strip and tiles. (D4.5.9-12)
5. The open repair runs all five checks on the student's explanation.
6. Break one prints with the answer hidden.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no animated cracks; no network requests.

## Open questions
None.
