# Theme Evidence Ladder

## One idea
The student states a theme for O. Henry's "After Twenty Years" as a full sentence and builds a ladder of quoted passages with the strongest support at the top, and the ladder tests every rung: a passage that holds up a rival theme just as well wobbles until the student explains why it belongs to theirs, and a passage that only retells the plot snaps, so they learn that a theme is proved by the passages that point to it, and that the strongest evidence is the one no rival theme explains; then Robert Burns's "Auld Lang Syne" tests whether the theme holds in a poem about the same subject.

## Not like
- theme-ledger (9-12, spec): two themes tracked across a novel in a ledger. Here one theme proved by ranked passages in a short story.
- summary-squeeze (6, spec): compressing a fable down to its theme. Here proving a theme with ranked quotes.
- theme-tracker (4, spec): details lighting theme lamps. Here rival themes testing each rung.
- claim-quote-comment (6-8, spec): building an evidence paragraph about an article. Here ranking literary evidence.
- main-idea-pinboard (3-5, spec): pinning details to a main idea. Here grades 6-8 theme with rivals.

## Who and how
- Grades 6-8, ELA, module "Theme and Textual Evidence" (Reading Literature). Standards: RL.6.1, RL.6.2, RL.6.9, RL.7.1, RL.7.2, RL.8.1, RL.8.2.
- Driver: one student; class mode compares ladders (tool.json `driver: "student"`). Role: lesson. Every passage is read on tap.
- Three grade paths, each with its own five texts (one anchor story and four short texts), its own job on the ladder and that grade's wording on the goal card. No path needs another. One text a sitting.
  - Grade 6 (RL.6.1, RL.6.2, RL.6.9): cite evidence for what the text says outright and for what it implies; say the theme and the details that carry it; summarize without opinion; compare a story and a poem on one theme.
  - Grade 7 (RL.7.1, RL.7.2): cite several pieces of evidence; say the theme and trace how it develops across the text; summarize objectively.
  - Grade 8 (RL.8.1, RL.8.2): cite the evidence that most strongly supports the reading; say the theme and how it depends on character, setting and plot; summarize objectively.
- Change note (spec fix, 2026-11-11): the ladder, snap, wobble and the poem stay. Before, all three grades shared one story and each standard met one item. Now each grade has five texts of its own; the host builds one ladder first as the model; grade 6 students say whether each rung states or implies; grade 7 students build the timeline themselves and write how the theme grows; grade 8 tags are keyed and each needs a line; the poem needs an explanation whatever the verdict; rung tests have a limit; the last text of each path is done on your own. Added the three hooks.
- English learners: every spoken line is also on screen in short sentences. The words theme, topic, evidence, implies, summary and objective each show with an example from the host's ladder the first time they are used. Every written line offers a frame the student may take or leave ("The story shows that __."; "This line shows it because __."). Old or Scots words are glossed on tap.
- tool.json `modes: ["Grade 6", "Grade 7", "Grade 8", "Compare ladders"]`, `minutes: "30-40"` for the anchor and about 15 for each short text, `grades_label: "Grades 6-8"`.
- Nothing is saved; `Print` prints the ladder, the summary and the paragraph.

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| RL.6.1 | cite textual evidence for what the text says explicitly and for inferences drawn from it | the student | Lift passages onto the ladder and mark each `says it` or `shows it without saying`; at least one of each | 5 texts, 3 to 5 rungs each | rungs with quotes, paragraph numbers and the student's mark | 3 |
| RL.6.2 | determine a theme and how it is conveyed through particular details; summarize without personal opinions | the student | Write the theme as a sentence, write for each rung what the detail shows, write an objective summary | 5 texts | the theme sign, the rung notes, the summary | 2, 7 |
| RL.6.9 | compare and contrast texts in different forms in terms of their approaches to similar themes | the student | Set the story's theme against the poem, mark Holds, Holds partly or Differs, and write how each form goes at the theme | 1 pair, 2 written lines | the poem beside the ladder | 6 |
| RL.7.1 | cite several pieces of textual evidence | the student | Lift at least three rungs, one each from the beginning, middle and end | 5 texts | rungs with paragraph numbers | 3 |
| RL.7.2 | determine a theme and analyze its development over the course of the text; objective summary | the student | Place each rung on the story line, mark where the theme is first hinted, where it turns and where it is clearest, and write how it grows | 5 texts | the timeline the student built | 5, 7 |
| RL.8.1 | cite the textual evidence that most strongly supports an analysis | the student | Rank the rungs; steady a rung that a rival theme could claim; put on top one no rival explains | 5 texts | the wobbling rung and the rival's name | 4 |
| RL.8.2 | determine a theme and analyze its development, including its relationship to the characters, setting and plot; objective summary | the student | Tag each rung character, setting or plot turn, and write one line for each of the three on how the theme leans on it | 5 texts, 3 lines each | the tags and the three lines | 5, 7 |

## Screens and modes
Header (kit): title "Theme Evidence Ladder"; `Story`, `Ladder`, `Poem` (grade 6), `Write`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word. The goal card gives the grade's standards in their own words.

**On load and first tap.** A tall wooden library ladder leaning on a bookshelf, its rungs empty, a sign at the top that says "My theme" and three theme cards on a reading table. First hint: "Tap the story to hear its first lines." The first tap reads the opening; the welcome is queued after it (`welcomeAfter: true`).

**The host goes first (the model).** On a fable of five sentences, "The Ant and the Grasshopper", the host builds a whole ladder aloud: turns down "work" as a topic, writes a theme sentence, lifts two passages and says what each shows, puts on top the one no other theme explains, and writes a two-sentence summary with no opinion in it. Then the grade's own step: for grade 6 she marks one rung `says it` and one `shows it`; for grade 7 she places the rungs on the story line; for grade 8 she tags them. It cannot be skipped the first time and `The host's ladder` reopens it.

**Story.** The text in numbered paragraphs or lines. The student taps to hear and highlights spans to lift.

**Theme.** On the anchor story, three starter cards or the student's own sentence; on the four short texts, the student's own sentence only. A single word ("friendship") is turned back: "That's a topic. What does the story say about it?" On the anchor the other two cards become the rivals. A student-written theme is matched to the nearest keyed theme by its key words; if none is near, the rungs are tested only for plot-only passages and the ladder prints "theme not in the key: for the teacher".

**Ladder.** Three to five rungs. Each rung is a lifted passage with a note in the student's words on what it shows. The tool tests each rung with keyed passage tags:
- Snap: a passage keyed plot only snaps: "That tells what happens. What does it show?"
- Wobble (grade 8; shown in grades 6 and 7 as a note only): a passage keyed as supporting a rival theme as strongly wobbles: "This holds up '{Keeping a promise}' too. Why is it yours?" The student writes a because line; it steadies.
- Strongest (grade 8): the top rung must be one keyed strongest for that theme; otherwise "Is there a rung no rival explains?"
The ladder can be tested twice. After the second test any rung still snapped or out of place is explained by the host and printed as "host explained".

**Grade 6: says it or shows it.** Each rung gets the student's mark, `says it` or `shows it without saying`, keyed for each passage. A ladder needs at least one of each. The marks are tested with the ladder.

**Grade 7: build the timeline.** The story line lies under the ladder as an empty strip of paragraph numbers. The student drags each rung to its place, needs one from the beginning, middle and end, and sets three flags: `first hint`, `turn`, `clearest`. Flags are keyed to paragraph ranges. Then two or three sentences on how the theme grows, with a guide: where it starts; what changes it; how it ends.

**Grade 8: tags and lines.** Each rung gets `character`, `setting` or `plot turn`, keyed for each passage, and the ladder needs all three. Then one line for each: how the theme leans on this character, this setting, this turn.

**Poem (grade 6).** "Auld Lang Syne" with each Scots word glossed (auld lang syne: old long since, times long past) beside the grade 6 anchor. The student marks whether the poem treats old friendship the same way as their theme ("Holds", "Holds partly", "Differs"), and whatever the mark writes two lines: how the story goes at the theme (through what happens to two people) and how the poem does (a speaker's toast, a repeated chorus). For Differs the student may also rewrite the theme. A three-box guide: I named something each form does; I pointed to a line in each; I said how they are alike or not. The mark is not keyed; the lines print for the teacher.

**Write.** An objective summary (about 60 words for an anchor, 30 for a short text); opinion words light ("amazing", "I think", "should") and must be taken out. On the anchor, a paragraph that uses the top two rungs.

**On your own.** The fifth text of each path runs with the host quiet: no starter cards, no snap or wobble messages, no guides, and one test of the whole ladder after the summary is in. The guides open afterward.

**The end.** A results strip for the teacher under the grade's codes, for the fifth text: rungs that held out of those lifted, with the grade's step (marks, flags or tags) right or not; the theme sentence and whether it matched the key; opinion words left in the summary. Then the counts for the four texts before and anything printed as "host explained".

**Compare ladders.** Class ladders for the same theme, with the most common top rung marked and named in words.

At 1366x768 the story and ladder fit side by side; at 680x425 the story is a tab.

## Content
All texts are public domain, split into numbered paragraphs or lines with keyed tags per passage: plot only; each keyed theme; strongest for each; says or shows; beginning, middle or end with the three flag ranges; character, setting or plot turn. Each anchor has three keyed themes; each short text has two.
- Grade 6. Anchor: "After Twenty Years" by O. Henry (The Four Million, 1906; about 1,200 words). Short texts: "The Old Man and His Grandson" (Grimm, Margaret Hunt's 1884 translation); "The Bundle of Sticks" (Aesop); "I'm Nobody! Who are you?" (Emily Dickinson); "The Arrow and the Song" (Longfellow), which is the one done on your own. Poem for the pair: "Auld Lang Syne" by Robert Burns (1788), first verse, chorus and two more verses, with glosses.
- Grade 7. Anchor: "Three Questions" by Leo Tolstoy (1903, in the Maudes' translation; about 1,500 words). Short texts: "The Road Not Taken" (Robert Frost, 1916); "We Wear the Mask" (Paul Laurence Dunbar, 1896); "Mother to Son" (Langston Hughes, 1922); "'Hope' is the thing with feathers" (Emily Dickinson), done on your own.
- Grade 8. Anchor: "The Last Leaf" by O. Henry (The Trimmed Lamp, 1907; about 2,300 words). Short texts: "Ozymandias" (Percy Bysshe Shelley, 1818); "O Captain! My Captain!" (Walt Whitman, 1865); "If" (Rudyard Kipling, 1910); "The Open Window" (Saki, 1914; about 1,200 words), done on your own.
- Written for Curio Class: the model fable retelling, theme starter cards for the three anchors, the opinion word list.
- What a wrong answer on the fifth text means: a one-word theme means topic and theme are not yet apart; a ladder of plot-only passages means the student is retelling; grade 6, every rung marked `says it` means the student does not yet see evidence that is implied; grade 7, all rungs from the last lines means the theme is read off the ending and not traced; the `first hint` flag set at the end means the same; grade 8, a top rung that a rival theme also explains means the student picks the most striking line and not the strongest; a setting tag on a line about what a person chooses means the three are not yet apart.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Rungs can be reordered until the ladder is tested; each ladder has two tests (one on the fifth text).
- Access: every action works by tap and by keyboard. A span is lifted by tapping its first and last word, or with Shift and the arrow keys; rungs and flags can be dragged, or picked with a tap and placed with a tap. A snapped or wobbling rung carries the word "snapped" or "wobbles", and opinion words are underlined and labeled, never color alone. Motion can be paused.
- On your own: one test, no feedback until the summary is in.
- With Motion off rungs don't wobble or fall; a "wobbles" or "snapped" label shows.

## Look
- Accent `--brand` #2e5e3a ivy green (header, ladder rails, theme sign); gold #f4c542 (the top rung, lifted passages); paper #f2f7f2; ink #0c1f10; muted #4f5c51. Scene: a quiet library with a tall shelf.
- Contrast (WCAG 2.1, computed): white on brand 7.56:1; brand on paper 6.97:1; ink on paper 15.88:1; muted on paper 6.49:1; ink on gold 10.59:1.
- Never color alone: rungs carry labels (steady, wobbles, snapped).
- Different from this batch (cart amber, coaster magenta, roots blue, rally orange).

## Art
- Local FLUX (`scripts/localart.py`): library with a tall ladder (1); a dark rainy city street in 1900 with a doorway of a closed hardware store, no faces shown (1); a candlelit table with two cups, for the poem (1).
- No people art: the two friends are never shown, so the twist (who is who) isn't given away by a picture.
About 3 images. Drawn in code: ladder, rungs, timeline, theme sign.

## Voice
Bank voice `wise-mentor` as the host (unique in this batch); the story is read by `gentle-storyteller` and the poem by `soft-breath` (each unique in this batch). `Curio.voice` with `scope: () => state.level + ':' + state.view + ':' + state.rung`, `welcomeAfter: true`.
- how `welcome`: "Say what the story means in a full sentence. Then build a ladder of passages to hold it up, strongest at the top."
- event, whole, `passage`: the tapped passage.
- event `topic`: "That's a topic. What does the story say about it?"
- event `snap`: "That tells what happens. What does it show?"
- event `wobble`: "This holds up {Keeping a promise} too. Why is it yours?"
- event `steady`: "Steady."
- event, whole, `poem`: the poem.
Read speaks the hint, which names the next action and control and never a disabled one.
- how `mark`: "Does this line say it, or show it without saying? Mark each rung."
- how `line`: "Drag each rung to its place in the story. Then set the three flags."
- how `tag`: "Tag each rung: character, setting or plot turn."
- how `own`: "This one is on your own. Build the ladder, then test it once."
- event, whole, the host's ladder.
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
evidence (`__tool.ev`), described in full in tools/theme-ledger/spec.md. This tool uses: Source pack (story and poem), Spans, Claims with `ev.claimCheck` (the theme as a full sentence), Evidence links with `comment` (the because line), `ev.checks` (offKey for plot-only rungs), `ev.compare` (each rung against the rivals) and `ev.pickStrong` (the top rung). Not Sides, Series, Ledger view or Board view. The ladder and timeline are tool-only drawing.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Theme | Type one word; pick any starter card | One word is turned back as a topic; starter cards exist only on the anchor, and all three are defensible, so the work is in the rungs. |
| Rungs | Lift any five passages; test and swap until it stands | Plot-only passages snap, and a ladder has two tests before the host explains and it prints. |
| Says or shows | Mark them all the same | Each ladder needs one of each, and the marks are keyed. |
| Timeline | Drop rungs anywhere | Places are the passages' own paragraphs; the three flags are keyed to ranges and one rung must come from each third. |
| Tags | Use one tag | All three are needed and each is keyed; each needs a written line. |
| Wobble | Type anything in the because line | The because line must name a word from the student's theme; the teacher sees it printed. |
| Top rung | Put the longest passage on top | The top must be keyed strongest for that theme. |
| On your own | Use the snap messages to sort passages | No messages and one test, after the summary. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the story: opening lines, `welcome` (queued, first time), then the host's ladder (whole), waits.
2. Theme: `topic` if one word.
3. Ladder: `passage` (whole) on tap; `mark`, `line` or `tag` by grade; at a test, `snap`, `wobble`, `steady` as they fire.
4. Poem (grade 6): `poem` (whole) on Play.
5. Fifth text: `own`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.6.1 to RL.8.2 and RL.6.9 wording | thecorestandards.org, Reading Literature Grades 6-8 | CCSS ELA 2010 PDF | yes |
| "After Twenty Years" is in O. Henry's The Four Million (1906), public domain | Project Gutenberg eBook #2776 (checked 2026-11-09) | Library of Congress catalog record for The Four Million | yes |
| "Auld Lang Syne" by Robert Burns (1788), public domain; "auld lang syne" means old long since, times long past | Project Gutenberg eBook #1279, Poems and Songs of Robert Burns (checked 2026-11-09) | National Library of Scotland or Burns Encyclopedia entry for Auld Lang Syne | yes |
| A theme is a message about life expressed in a full statement, not a one-word topic | ReadWriteThink, theme | Purdue OWL, literary terms (theme) | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad b20, 2026-11-09): the Gutenberg file is The Four Million and contains "AFTER TWENTY YEARS"; the Burns file contains "Auld Lang Syne"; every sample theme has at least one rung keyed strongest for it alone; contrast as in Look.
Spec fix notes (2026-11-11): the eleven texts added in this pass (the Grimm tale, the Aesop fable, two Dickinson poems, Longfellow, Tolstoy, Frost, Dunbar, Hughes, "The Last Leaf", Shelley, Whitman, Kipling, Saki) were chosen from memory as public domain in the United States and were not opened: Build must confirm each text, its date, its translation and its word count, and key its passages, before the path is built. A sensitivity read of the grade 7 and grade 8 texts is left for the final review.

## Done when
1. Focus and fold: at 1366x768 story and ladder fit; at 680x425 the story is a tab.
2. Each grade path has its own five texts, goal card and step, and none needs another; a one-word theme is turned back and a full sentence is set. (RL.6.2, RL.7.2, RL.8.2)
3. Rungs are lifted passages with paragraph numbers and a note; plot-only rungs snap; grade 6 rungs are marked says or shows with one of each; grade 7 ladders have a rung from each third. (RL.6.1, RL.7.1)
4. In grade 8, rival-supporting rungs wobble until explained and the top must be keyed strongest. (RL.8.1)
5. Grade 7 students place the rungs and three flags on the story line and write how the theme grows; grade 8 students tag every rung, use all three tags and write three lines. (RL.7.2, RL.8.2)
6. The poem test takes a mark and two written lines on how each form goes at the theme, whatever the mark. (RL.6.9)
7. The summary flags opinion words until they are taken out; the anchor paragraph uses the top two rungs.
8. The host's ladder plays first and can be reopened; a ladder has two tests, then the host explains and it prints.
9. The fifth text runs with no cards, messages or guides and one test; the end screen shows the result under the grade's codes.
10. Compare ladders and Print work.
11. Every spoken instruction is also on screen; each key word shows with an example at first use; the frames can be left.
12. Every action works by keyboard as well as tap, drags have a tap way, nothing is shown by color alone, and motion can be paused.
13. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
14. Motion off: rungs don't wobble or fall; no network requests.

## Open questions
- None for Cory.
