# Genre Remix

## One idea
The student remixes one short prose scene (a girl and her grandfather fixing a kite in the wind) into a script and then into a poem, moving each piece into the parts each form uses (description into a setting line and stage directions, talk into character lines, feeling into images, line breaks and a beat), and the three versions end side by side with two questions, what the script could show that the story couldn't and what the poem had to leave out, so they learn the parts of prose, drama and poetry by building with them.

## Not like
- story-building-blocks (3, spec): ordering chapters, scenes and stanzas. Here turning one scene into each form.
- dialogue-director (3, spec): a comic into prose with dialogue marks. Here prose into a script and a poem.
- script-read-through (3-5, spec): performing a written script. Here writing one from prose.
- shakespeare-remix (9, concept): changes from a source play. Here grade 4 form parts.
- side-by-side-reader (spec): comparing two texts. Here one text in three forms.

## Who and how
- Grade 4, ELA, module "Poetry, Drama and Prose" (Reading Literature). Standard: RL.4.5.
- Driver: one student (tool.json `driver: "student"`). The story, script and poem are read on tap; the poem is read with its beat.
- One main scene ("The Kite on Hawk Hill") and a second scene for a second round ("The Lost Mitten", winter). tool.json `modes: []`, `minutes: "25-35"`, `grades_label: "Grade 4"`.
- Saving: the three versions are kept in this browser; footer: "Your remix stays on this device." `Clear my remix` removes it.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.4.5 (drama: cast, setting) | Script tab: build the cast list and the setting line from the story | the script page's top | 2 |
| RL.4.5 (drama: dialogue, stage directions) | Drag talk into character lines and actions into stage directions; fix narration no actor could say | the script page | 3 |
| RL.4.5 (poetry: verse, stanza) | Poem tab: pick the strongest images, break them into lines and stanzas | the poem page with line breaks | 4 |
| RL.4.5 (poetry: rhythm, meter) | Pick a beat from the beat bar (da-DUM or DUM-da); the poem is read with taps on the strong beats | the beat bar and stressed syllables | 5 |
| RL.4.5 (differences from prose) | Answer the two compare questions with tagged examples from the three versions | three columns and two answers | 6 |

## Screens and modes
Header (kit): title "Genre Remix"; `Scenes`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A windy hilltop studio: a story page, a script page and a poem page clipped to a line like kites, and Remy, a red fox in a scarf with a pencil behind one ear. First hint: "Tap the story to hear the scene." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**Story tab.** The prose scene (about 180 words), each sentence tagged in the data as description, action, talk, thought or feeling. Tags are hidden until the Script tab.

**Script tab.** An empty script page with four zones: Cast, Setting, Stage directions (in italics, in brackets) and Lines (character name and colon). The student drags each story sentence to a zone. Talk sentences become lines with the speaker's name and lose the quotation marks and said-words (the tool strips them and shows how). Thought and feeling sentences have no zone; they glow with "No actor can say what she thinks. Turn it into a line she says or an action she does." The student picks: make it a line (types it) or a stage direction (picks an action from three). A parts checklist ticks: cast, setting, dialogue, stage directions.

**Poem tab.** The story sentences shown as image cards (the strongest images marked by count of sense words). The student picks 6 to 10 images, trims each to a line (word chips can be removed), orders them, and inserts stanza breaks. The beat bar offers two beats: da-DUM (iambic, like "the KITE goes UP") and DUM-da (trochaic, like "WIND is PULLing"). The poem is read with soft taps on the stressed syllables of each line (from a stress dictionary in the data); lines that fight the beat show their stress pattern so the student can swap a word. A parts checklist ticks: verse lines, stanza, rhythm, meter.

**Side by side.** The three versions in three columns. Two questions: "What could the script show that the story couldn't?" and "What did the poem have to leave out?" The student answers each by tagging a line from the versions and finishing a sentence frame.

At 1366x768 a tab and the story fit side by side; at 680x425 the story is a drawer.

## Content
- "The Kite on Hawk Hill" (original, about 180 words, 14 sentences: 4 description, 3 action, 4 talk, 2 thought, 1 feeling): Mina and Grandpa Teo patch a torn kite on a windy hill; she worries it won't fly; it does.
- "The Lost Mitten" (original, about 150 words, 12 sentences): Jonah and his big sister search the snow for a mitten.
- Stress data: every word in both scenes has its syllable stress listed (one-syllable words marked as can be stressed or not).
- Parts glossary: verse, stanza, rhythm, meter, cast of characters, setting, dialogue, stage directions, each with a one-line kid meaning.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Every drag has a keyboard path (pick a sentence, then a zone).
- The poem's beat taps are quiet clicks; with Sound off, stressed syllables are shown bold.
- Nothing the student writes is refused; checklists are guides.

## Look
- Accent `--brand` #a0306a kite magenta (header, tabs, kite pages); gold #f4c542 (beat marks, ticked parts); paper #fcf3f8; ink #2a0d1c; muted #66505c. Scene: a windy hilltop with clouds.
- Contrast (WCAG 2.1, computed): white on brand 6.72:1; brand on paper 6.18:1; ink on paper 16.47:1; muted on paper 6.74:1; ink on gold 11.01:1.
- Never color alone: zones are labeled; stressed syllables are bold as well as marked.
- Different from this batch (lagoon teal, word violet, brick orange, storm slate).

## Art
- People art goes to Gemini: Mina (a girl about 9) and Grandpa Teo on a windy hill with a patched kite, 3 scenes; Jonah and his sister in snow, 2 scenes; "illustrated children's book scene <description>, soft watercolor, no text"; 16:9.
- Local FLUX (`scripts/localart.py`): studio (1); Remy (4 poses: read, write, think, cheer), "A friendly red fox writer in a scarf with a pencil behind one ear <pose>, soft gouache, plain white background"; 1:1; cutout yes.
About 10 images. Drawn in code: script page, poem page, beat bar, columns.

## Voice
Bank voice `warm-teacher` as Remy (unique in this batch). The story and poem are read by `smooth-narrator`; script lines are read by `friendly-dad` (Grandpa Teo) and `playful-friend` (Mina), with `smooth-narrator` reading stage directions (all unique in this batch). `Curio.voice` with `scope: () => state.scene + ':' + state.tab + ':' + state.step`, `welcomeAfter: true`.
- how `welcome`: "One scene, three ways to tell it. First a script, then a poem. Each one has its own parts."
- event, whole, `storyLine`: the tapped sentence.
- how `scriptHow`: "Drag each sentence to a part of the script: cast, setting, stage directions or lines."
- event `noActor`: "No actor can say what she thinks. Turn it into a line she says or an action she does."
- how `poemHow`: "Pick the strongest pictures, cut them into lines, and choose a beat."
- event `beat`: the poem read with its beat.
- how `compareHow`: "What could the script show that the story couldn't? Tag a line to show it."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: sentence tags, script zones, poem builder, stress data, beat reader.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Script zones | Drop everything in Lines | Description sentences in Lines glow "Who says this? It sounds like the setting." The checklist won't tick setting or stage directions. |
| Thought sentences | Leave them | The script checklist stays open until each is turned into a line or an action. |
| Poem | Paste the whole story as one line | The poem needs 6 to 10 lines and a stanza break; the beat reader shows the line fighting the beat. |
| Compare | Tag any line | Each answer must tag a line from the version it names. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the story: the scene (whole), `welcome` (queued, first time).
2. Script tab: `scriptHow`; thought sentences: `noActor`.
3. Poem tab: `poemHow`; `Hear it`: `beat`.
4. Side by side: `compareHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.4.5 wording, naming verse, rhythm, meter, casts of characters, settings, descriptions, dialogue and stage directions | thecorestandards.org, Reading Literature Grade 4 | CCSS ELA 2010 PDF | yes |
| Iambic meter is an unstressed then stressed pattern (da-DUM); trochaic is stressed then unstressed (DUM-da) | Poetry Foundation, glossary (iamb, trochee) | Academy of American Poets, poets.org glossary | yes |
| Stage directions describe actions, settings and how lines are said; scripts list a cast and give speaker names before lines | Britannica, stage direction and dramatic literature | ReadWriteThink, elements of drama | yes |
Backed twice: 3. Cut: 0.

Sensitivity note: people art goes to the fresh-agent review.

Checks run (Python, scratchpad b12, 2026-11-09): the Hawk Hill scene's 14 tagged sentences cover all five tags (4, 3, 4, 2, 1); both sample beat lines match their stated stress pattern; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 a tab and the story fit; at 680x425 the story is a drawer.
2. The script builds cast and setting. (RL.4.5)
3. Talk becomes lines; actions become stage directions; thought sentences must be changed. (RL.4.5)
4. The poem takes 6 to 10 lines and stanza breaks. (RL.4.5)
5. The beat bar reads the poem with stresses and shows lines that fight the beat. (RL.4.5)
6. Side by side answers two questions with tagged lines. (RL.4.5)
7. The remix survives a reload where storage works and prints.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: kite pages don't sway; no network requests.

## Open questions
- None for Cory.
