# Podcast Listening Club

## One idea
The student listens to a short student podcast where two hosts argue about a cashless cafeteria, dragging each claim card that pops up on the waveform into Supported, Unsupported or Off topic (scrubbing back to re-hear it, and reading the chart in the episode notes to judge one host's numbers), then three club members each disagree with one of the student's tags and the student must build on, question, challenge with evidence or change their mind, so they learn to follow a speaker's argument by ear and to discuss it with people who heard it differently.

## Not like
- book-group-table (6, spec): discussing a story with talk moves. Here judging a spoken argument, then discussing the judgments.
- discussion-dashboard (6, concept): a book-group discussion. Here a podcast and its claims.
- logic-gym (7, concept): written arguments. Here arguments by ear.
- argument-x-ray (6, concept): an op-ed on the page. Here audio.
- claim-court (5, spec): an author's support on paper. Here speakers' support in audio.

## Who and how
- Grades 6-8, ELA, module "Listening to Speakers and Discussing" (Speaking and Listening). Standards: SL.6.2, SL.6.3, SL.7.1, SL.7.2, SL.7.3, SL.8.1, SL.8.3.
- Driver: one student; pairs can compare tags in class mode (tool.json `driver: "student"`). The episode plays with a transcript that can be shown or hidden.
- Three episodes at rising difficulty: "Cashless Cafeteria" (grade 6), "Phones in Lockers" (grade 7, adds is the evidence enough), "A Four-Day School Week" (grade 8, adds true but irrelevant facts). tool.json `modes: ["Episode 1", "Episode 2", "Episode 3", "Pair compare"]`, `minutes: "25-35"`, `grades_label: "Grades 6-8"`.
- Nothing is saved; `Print` prints the tags, the club round and the summary.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| SL.6.2, SL.7.2 | Read the episode notes' chart and use it to judge one host's claim; name the main ideas from audio and chart | the chart with the read value and the main idea card | 2 |
| SL.6.3 | Tag each claim card Supported, Unsupported or Off topic as it plays | claim cards in three bins | 3 |
| SL.7.3 | Episode 2: for supported claims, mark whether the evidence is enough and relevant | the enough meter on each card | 3 |
| SL.8.3 | Episode 3: catch a true fact that doesn't bear on the claim | the irrelevant tag | 3 |
| SL.7.1, SL.8.1 | Club round: answer each member's disagreement with a move and a line; at grade 8, qualify or justify your view | the club bubbles and the student's lines | 4 |
| SL.6.3, SL.7.2 | Summary: each host's argument in one sentence and which held up better | the summary card | 5 |

## Screens and modes
Header (kit): title "Podcast Listening Club"; `Episodes`, `Club`, `Summary`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A club room with beanbags, a laptop showing a podcast player and a waveform, and the episode notes card. First hint: "Tap Play to start Episode 1." The first tap plays the intro jingle and the episode title; the welcome (by the club's student leader, Jae) is queued after it (`welcomeAfter: true`).

**Episode.** About 4 minutes, two hosts: Theo (for the cashless cafeteria) and Nia (against). Each claim is a timed card on the waveform that pops up as it is spoken; the student drags it to a bin or leaves it in a holding tray to decide later. `Back 10 s` and scrubbing re-hear it. A transcript toggle shows the words, with the current line lit.

**Chart.** The notes include a chart (drawn in code): average lunch line wait in minutes at a made-up middle school, before and after card readers (labeled "practice data"). Theo claims "Card readers cut the line in half"; the chart shows 9 minutes to 6, so the student marks it unsupported (a third, not half) and types the numbers.

**Episodes 2 and 3.** Episode 2 adds an enough meter for each supported claim (one example, a survey of 20 students, or a study across many schools). Episode 3 adds the Irrelevant tag: a host says "Four-day weeks are popular in Colorado" (true in the made-up notes but not about learning).

**Club.** Jae, Rosa and Dev each disagree with one of the student's tags, in a bubble with their reason. For each, the student picks a move (build on, ask a question, challenge with evidence, change my mind) and writes a line. If the member's reason uses a fact from the episode, changing your mind is shown as reasonable; if not, the member admits it when challenged. At grade 8 a "qualify" frame helps: "I still think ___, but ___."

**Summary.** One sentence per host's argument and a pick of which held up better, with a reason that names a claim card.

**Pair compare.** Two students' tags side by side, with the same move cards for talking about differences.

At 1366x768 the player, bins and notes fit; at 680x425 the notes are a tab.

## Content
Written for Curio Class:
- Three scripts (about 550 words each) with 10 to 12 claim cards, each keyed Supported, Unsupported, Off topic, with enough and irrelevant keys in episodes 2 and 3.
- Charts with practice data, labeled made up.
- Club members' disagreements and reaction rules.
- Produced audio: two host voices per episode from the bank, with short music beds from the kit's sound set; a transcript for every episode.

## Interactions in detail
- Every tap acts at once; a new line stops the old one, except the episode, which pauses while a hint plays and resumes after.
- Cards in the holding tray stay until tagged; the summary needs all tagged.
- With Motion off cards appear without popping.

## Look
- Accent `--brand` #a8324a raspberry (header, player, bins); gold #f4c542 (the playhead, the enough meter); paper #fcf3f5; ink #2b0a12; muted #68515a. Scene: a bright after-school club room.
- Contrast (WCAG 2.1, computed): white on brand 6.52:1; brand on paper 5.99:1; ink on paper 16.69:1; muted on paper 6.62:1; ink on gold 11.18:1.
- Never color alone: bins have words; the meter shows "one example", "some", "strong".
- Different from this batch (studio slate, camera purple, mixer cyan, press olive).

## Art
- People art goes to Gemini: hosts Theo (a white boy about 13 with headphones) and Nia (a Black girl about 13 with a mic), club members Jae (a Korean American boy about 13), Rosa (a Puerto Rican girl about 13) and Dev (an Indian American boy about 13); 3 poses each; "illustrated middle school student <description> <pose>, warm gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): club room (1).
About 16 images. Drawn in code: player, waveform, charts, bins, bubbles.

## Voice
Hosts: Theo `upbeat-guide`, Nia `big-sister`; club: Jae `playful-friend` (also the hint voice), Rosa `easy-coach`, Dev `hero-coach`. Each is unique in this batch. `Curio.voice` with `scope: () => state.episode + ':' + state.view + ':' + state.card`, `welcomeAfter: true`.
- how `welcome`: Jae: "Listen for every claim. Is it backed up, not backed up, or off topic? Drag each card as you go."
- event, whole, `episode`: the episode audio.
- event `chartCheck`: "Check the chart. Is it really half?"
- event `disagree`: the member's bubble.
- how `moveHow`: "Pick a move: build on it, ask, challenge with evidence, or change your mind."
- event `concede`: the member's answer to a challenge.
- how `summaryHow`: "Sum up each host in one sentence. Who held up better?"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: timed claim cards on an audio timeline, bins with keys, chart, club round with reaction rules, summary.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Tags | Tag everything Supported | Each card is keyed; the club members challenge the mistagged ones with reasons from the episode. |
| Chart claim | Accept the host's number | The chart check asks for the two values. |
| Club | Always "change my mind" | Members whose reason has no episode fact admit it when challenged; changing your mind there is shown as giving up a good tag. |
| Summary | Copy a host line | It must name a claim card for the "held up better" reason. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap Play: jingle and title, `welcome` (queued, first time), then `episode` (whole).
2. Chart claim: `chartCheck` when the card is tagged.
3. Club: `disagree` per member; `moveHow` (first time); `concede` as it fires.
4. Summary: `summaryHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| SL.6.2, SL.6.3, SL.7.1 to SL.7.3, SL.8.1, SL.8.3 wording | thecorestandards.org, Speaking and Listening Grades 6-8 | CCSS ELA 2010 PDF | yes |
| Relevant and sufficient evidence: evidence must bear on the claim and be enough to support it | Purdue OWL, using evidence | ReadWriteThink, evaluating arguments | yes |
Backed twice: 2. Cut: 0.

Design choices (not claims): the episodes and charts use practice data, labeled made up on screen, so no real school or study is misquoted.

Checks run (Python, scratchpad b18, 2026-11-09): 9 minutes to 6 is a cut of one third, not half; each sample episode key has all three tags; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 player, bins and notes fit; at 680x425 notes are a tab.
2. The chart claim needs the two values. (SL.6.2, SL.7.2)
3. Claim cards tag into bins; episode 2 adds enough, episode 3 irrelevant. (SL.6.3, SL.7.3, SL.8.3)
4. The club round takes moves and lines; grade 8 qualify frame works. (SL.7.1, SL.8.1)
5. The summary takes two sentences and a reason with a card. (SL.6.3)
6. Transcripts show and hide; Back 10 s and scrubbing work.
7. Print shows tags, club round and summary.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: cards appear without popping; no network requests.

## Open questions
- None for Cory.
