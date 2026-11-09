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
- Driver: one student; class mode compares ladders (tool.json `driver: "student"`). Every passage is read on tap.
- Text: "After Twenty Years" by O. Henry, from The Four Million (1906), public domain; poem: "Auld Lang Syne" by Robert Burns (1788), public domain, with a glossed line for each Scots word. tool.json `modes: ["Grade 6", "Grade 7", "Grade 8", "Compare ladders"]`, `minutes: "25-35"`, `grades_label: "Grades 6-8"`.
- Nothing is saved; `Print` prints the ladder, the summary and the paragraph.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.6.2 | Write the theme as a full sentence (one word is turned back) | the theme sign at the top of the ladder | 2 |
| RL.6.1, RL.7.1 | Lift passages from the story onto the ladder, including one that implies the theme without saying it | rungs with quotes and paragraph numbers | 3 |
| RL.8.1 | Rank the rungs; a rung that also supports a rival theme wobbles until explained | the wobbling rung and the rival's name | 4 |
| RL.7.2 | Grade 7: lay the ladder along the story's timeline to see where the theme first shows and how it grows | the timeline view | 5 |
| RL.8.2 | Grade 8: tag each rung as working through character, setting or a plot turn | the tag on each rung | 5 |
| RL.6.9 | Test the theme against "Auld Lang Syne" and keep or rewrite it | the poem beside the ladder and the theme's verdict | 6 |
| RL.6.2, RL.7.2, RL.8.2 | Write an objective summary (opinion words flagged) and a paragraph from the top two rungs | the summary and paragraph cards | 7 |

## Screens and modes
Header (kit): title "Theme Evidence Ladder"; `Story`, `Ladder`, `Poem`, `Write`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A tall wooden library ladder leaning on a bookshelf, its rungs empty, a sign at the top that says "My theme" and three theme cards on a reading table. First hint: "Tap the story to hear its first lines." The first tap reads the opening; the welcome is queued after it (`welcomeAfter: true`).

**Story.** The full story in numbered paragraphs (about 1,200 words). The student taps to hear and highlights spans to lift.

**Theme.** Three starter cards ("Time can change people more than their old friends expect.", "Doing your duty can mean hurting someone you care about.", "Keeping a promise shows true friendship.") or the student's own sentence. A single word ("friendship") is turned back: "That's a topic. What does the story say about it?" The other two cards become the rivals.

**Ladder.** Up to five rungs. Each rung is a lifted passage. The tool tests each rung with keyed passage tags:
- Snap: a passage keyed plot only ("The policeman on the beat moved up the avenue impressively.") snaps: "That tells what happens. What does it show?"
- Wobble: a passage keyed as supporting a rival theme as strongly wobbles: "This holds up '{Keeping a promise}' too. Why is it yours?" The student writes a because line; it steadies.
- Strongest: the top rung must be one keyed strongest for that theme (only that theme explains it); otherwise "Is there a rung no rival explains?"

**Grade 7 timeline.** The ladder tips onto its side along the story's paragraphs, so the student sees the theme first hinted (the two friends' promise) and growing to the note at the end.

**Grade 8 tags.** Each rung gets Character, Setting or Plot turn (the dark, rainy, empty street; Jimmy's choice; the note).

**Poem.** "Auld Lang Syne" with each Scots word glossed (auld lang syne: old long since, times long past). The student marks whether the poem treats old friendship the same way as their theme ("Holds", "Holds partly", "Differs") and, for Differs, rewrites the theme or writes how the two works differ (the poem toasts old friends; the story asks whether an old friend is still the same person).

**Write.** An objective summary of about 60 words; opinion words light ("amazing", "I think", "should"). Then a paragraph that uses the top two rungs.

**Compare ladders.** Class ladders for the same theme, with the most common top rung marked.

At 1366x768 the story and ladder fit side by side; at 680x425 the story is a tab.

## Content
- "After Twenty Years" (Project Gutenberg #2776, The Four Million), split into numbered paragraphs with keyed tags per passage: plot only, theme A, theme B, theme C, strongest for each.
- "Auld Lang Syne" (Project Gutenberg #1279, Poems and Songs of Robert Burns), first verse, chorus and two more verses, with glosses.
- Written for Curio Class: theme starter cards, the opinion word list.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Rungs can be dragged to reorder; tests rerun.
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

## Family engine
evidence (`__tool.ev`), described in full in tools/theme-ledger/spec.md. This tool uses: Source pack (story and poem), Spans, Claims with `ev.claimCheck` (the theme as a full sentence), Evidence links with `comment` (the because line), `ev.checks` (offKey for plot-only rungs), `ev.compare` (each rung against the rivals) and `ev.pickStrong` (the top rung). Not Sides, Series, Ledger view or Board view. The ladder and timeline are tool-only drawing.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Theme | Type one word | One word is turned back as a topic. |
| Rungs | Lift any five passages | Plot-only passages snap. |
| Wobble | Type anything in the because line | The because line must name a word from the student's theme; the teacher sees it printed. |
| Top rung | Put the longest passage on top | The top must be keyed strongest for that theme. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the story: opening lines, `welcome` (queued, first time).
2. Theme: `topic` if one word.
3. Ladder: `passage` (whole) on tap; `snap`, `wobble`, `steady` as they fire.
4. Poem: `poem` (whole) on Play.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.6.1 to RL.8.2 and RL.6.9 wording | thecorestandards.org, Reading Literature Grades 6-8 | CCSS ELA 2010 PDF | yes |
| "After Twenty Years" is in O. Henry's The Four Million (1906), public domain | Project Gutenberg eBook #2776 (checked 2026-11-09) | Library of Congress catalog record for The Four Million | yes |
| "Auld Lang Syne" by Robert Burns (1788), public domain; "auld lang syne" means old long since, times long past | Project Gutenberg eBook #1279, Poems and Songs of Robert Burns (checked 2026-11-09) | National Library of Scotland or Burns Encyclopedia entry for Auld Lang Syne | yes |
| A theme is a message about life expressed in a full statement, not a one-word topic | ReadWriteThink, theme | Purdue OWL, literary terms (theme) | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad b20, 2026-11-09): the Gutenberg file is The Four Million and contains "AFTER TWENTY YEARS"; the Burns file contains "Auld Lang Syne"; every sample theme has at least one rung keyed strongest for it alone; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 story and ladder fit; at 680x425 the story is a tab.
2. A one-word theme is turned back; a full sentence is set. (RL.6.2)
3. Rungs are lifted passages with paragraph numbers; plot-only rungs snap. (RL.6.1, RL.7.1)
4. Rival-supporting rungs wobble until explained; the top must be keyed strongest. (RL.8.1)
5. Grade 7 timeline and grade 8 tags work. (RL.7.2, RL.8.2)
6. The poem test sets Holds, Holds partly or Differs and takes a rewrite or a difference line. (RL.6.9)
7. The summary flags opinion words; the paragraph uses the top two rungs. (RL.6.2, RL.8.2)
8. Compare ladders and Print work.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: rungs don't wobble or fall; no network requests.

## Open questions
- None for Cory.
