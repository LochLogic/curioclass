# Choreography Board

## One idea
Revision you can watch: build a dance from 8-count phrases on a timeline, then revise it the way choreographers do, one device at a time (repeat, retrograde, mirror, level, tempo, dynamics, size, canon), and Compare plays any earlier version beside the current one in sync, so you see exactly what each change did to the dance.

## Not like
- stage-blocker (6-8 theater, stage family): places actors, lights and set on a top-down stage. Here there is no top-down placement at all (the overlap note): formations are five presets seen only from the audience, and the subject is movement in time.
- design-fixer (6-8 art): a broken poster fixed toward a goal, with a before-and-after wipe. Here nothing is broken and there is no target: every version is a choice, kept in a history, and compared as motion playing in sync.
- flipbook-studio (6-8 media arts): hand-drawn frames with onion skin. Here no drawing: moves come from a pose library on counts.
- band-practice (6-8 music) and beat-lab (9-12): playing in time and producing music. Here the music is a fixed backing track; the dance is what you make.
- vanishing-point-studio, frame-it, art-through-time (6-8 art): visual art. No shared mechanic.
- Dance siblings: levels-and-pathways (floor ribbons for levels and pathways), dance-pattern-puzzle (find the repeating attribute in move cards), dance-styles-explorer (styles, traces, critique). Only this tool has devices, versions, canon and formations.

## Who and how
- Grade 6-8, arts (dance), module "Choreography (Dance)".
- Topic line: create and revise movement phrases
- Driver: students (pairs on laptops, one dances while one edits), or the teacher on a projector building with the class. Minutes: 20-45.
- tool.json modes: ["Build", "Compare", "Show"]; driver "students or teacher".
- Standards (NCAS dance): DA:Cr1.1.6a to 8b (generate movement), DA:Cr2.1.6a to 8a (choreographic devices and dance structures), DA:Cr3.1.6a to 8a (revise and explain choices).

## Screens and modes
Header: title "Choreography Board", small line "Create and revise movement phrases", modes (`.seg`, keys 1 to 3) **Build** (default), **Compare**, **Show**, then kit `motion`, `sound`, `read`. Stage left, panel right; under 1000 px wide the panel goes below with Play and the device buttons first; in short wide boxes the panel stays beside the stage, compact.

Stage (Build and Show): the engine's `'stage'` view, an audience view of a black box theater: a wood floor in shallow perspective with three depth rows (upstage, center, downstage), black side wings, a cyclorama at the back lit with a soft color wash. Up to 4 dancers, each with a color and a chest badge shape (Look). Under the stage, the **timeline**: one row of up to 8 phrase blocks, each block as wide as its counts (8, 16 or more), with the phrase name, a row of 8 tiny pose thumbnails, and small glyphs for each device on it; count ruler above (1 to 96, every 8 marked); a playhead.

### Build (opens with the starter dance "First Light": Rise, Wave, Turn and point, in Line formation, 2 dancers, track Drift)
- Panel sections (`.sec`):
  - **Play**: **▶ Play** (becomes **⏹ Stop**), **🔁 Loop block**, **Track** select (Pulse, Drift, Strut, Storm), count readout "Count 13 of 24".
  - **Phrases**: the 12 starters and any of your own as chips; tap one, then tap a gap or the end of the timeline to place it (or press Enter to add it at the end). **✏ Make a phrase**.
  - **Selected block** (after tapping a block): **Dancers** 1 2 3 4; **Formation** Line, Two rows, Wedge, Diagonal, Cluster (each with a mini audience-view diagram); **◀ ▶** move the block earlier or later; **🗑 Remove**.
  - **Devices** (for the selected block): **Repeat**, **Retrograde**, **Mirror**, **Level** (Higher / Lower), **Tempo** (Half time / Double time), **Dynamics** (Smooth, Sharp, Swing, Suspend, Collapse, Shake), **Size** (Bigger / Smaller), **Canon** (1 count / 2 counts apart). Tapping an active device again removes it. Each device shows its one-line meaning under it when chosen (Content).
  - **History**: "Version 5" with **↶ Undo** and **↷ Redo**; every change makes a version.
- Make a phrase: the timeline area turns into 8 count slots. Tap a slot, then a move from the move palette (24 moves in four groups, Content), a **Level** (High, Middle, Low) and a **Dynamics** quality; **Hold** keeps the previous shape for that count. The dancer previews each count. **▶ Try it**, **💾 Save phrase** (name it, up to 20 characters), **✕ Cancel**. Starters can be opened as a copy and edited.

### Compare
- Stage splits in two: **Before** (left) and **Now** (right), each the same audience view, the same size. Both play together from count 1 on one clock with the Now track; a block that is longer in one version simply runs longer there, so tempo and repeat changes show as drift.
- Panel: **Before** version picker (default: the version just before the latest change), the version list ("v4: Retrograde on block 2, Wave"), **▶ Play both**, **👻 Ghost** (instead of the split, Before draws as faint outlines over Now on one stage), **↩ Go back to Before** (makes a new version equal to Before; history is never deleted).
- **What changed** readout (computed from both versions, the tool's own measures): length in counts; time at each level (percent of counts High, Middle, Low); dynamics mix (counts per quality); counts in unison and in canon; number of formation changes. Each shown as Before → Now.
- **Why I changed it** (optional, per version): chips Clearer idea, More contrast, Build to a peak, Smoother transition, Feedback from a peer, Just exploring, and a short note box (120 characters). Shown in the version list.

### Show
- Full stage, timeline and panel hidden except a slim bar with **▶ Play**, **⏹ Stop**, **← Back**. The dance title (typed in Build's History section, up to 40 characters, "Untitled dance" at start) shows on the cyclorama for 2 seconds, then the dance plays once with lights: the cyclorama wash changes color on each block. A bow at the end.

## Content
Starter phrases (8 counts each; counts: move):
1. Rise: 1-2 curl low, 3-4 kneel and reach up, 5-6 stand with arms wide, 7-8 relevé reaching up.
2. Fall: 1-2 relevé reach up, 3 hang there (suspend), 4 drop to a crouch (collapse), 5-6 roll to the side on the floor, 7-8 sit and look up.
3. Turn and point: 1-2 step right, 3-4 full turn right, 5-6 point left foot front with arms wide, 7-8 close feet and clap.
4. Wave: 1-2 right arm wave, 3-4 left arm wave, 5-8 body wave from head to knees.
5. Leap across: 1-3 run to the right, 4 leap, 5-7 run, 8 land in plié.
6. Stomp grid: 1 stamp right, 2 stamp left, 3 clap, 4 hold, 5 stamp right, 6 stamp left, 7 jump, 8 freeze.
7. Push and pull: 1-2 lunge right and push both arms out, 3-4 pull back, 5-6 lunge left and push, 7-8 pull back.
8. Shake out: 1-2 shake hands, 3-4 shoulders, 5-6 whole body, 7-8 stand still.
9. Spiral down: 1-2 twist right, 3-4 twist left and lower, 5-6 spiral down to kneel, 7-8 curl low.
10. Star: 1 star jump, 2 land, 3 tuck jump, 4 land, 5-8 arms circle overhead.
11. Gesture: 1-2 hand to heart, 3-4 open the arm out, 5-6 look up, 7-8 bow.
12. Freeze frames: four sharp shapes, each held 2 counts: lunge, arabesque, crouch, reach.

Move palette for Make a phrase (24): Reach: reach up, reach side, reach low, arms wide. Turn: quarter turn, half turn, full turn, spiral. Travel: step, run, leap, slide, skip. Floor: kneel, sit, roll, crouch, lie. Shapes: lunge, arabesque, passé, contraction, release, clap.

Devices (the meaning shown under each when chosen):
- Repeat: do the phrase again, so the block is twice as long.
- Retrograde: perform the phrase backwards, last count first, like rewinding a video.
- Mirror: perform it on the other side; right becomes left.
- Level: perform it higher (on the toes, arms up) or lower (knees bent, closer to the floor).
- Tempo: half time makes every count last twice as long (augmentation); double time makes it twice as fast (diminution).
- Dynamics: change the energy quality: smooth, sharp, swing, suspend, collapse or shake.
- Size: make every movement bigger (more space) or smaller.
- Canon: the dancers start the same phrase one after another, 1 or 2 counts apart. Without it they dance in unison.

Formations (audience view; dancer 1 to 4 positions as across, from stage left, and depth): Line (all downstage, evenly across), Two rows (1 and 2 downstage, 3 and 4 upstage between them), Wedge (1 downstage center, 2 and 3 center row, 4 upstage center), Diagonal (from upstage stage-right to downstage stage-left), Cluster (center, close together, overlapping). Stage left and right are named from the dancer's view facing the audience; a small note on the Formation section says so.

Tracks (original, synthesized, all in 4): Pulse 112 beats a minute (electronic kick, claps on 2 and 4, arpeggio), Drift 76 (pads and soft piano, no drums), Strut 96 swung (walking bass, snaps on 2 and 4), Storm 132 (low toms and strings, an accent on the first count of each 8). A soft swell marks each block start.

## Interactions in detail
- Devices stack on a block in a fixed order: Level, Size, Dynamics, Mirror, Retrograde, Tempo, Repeat, Canon. Retrograde reverses keyframes and travel direction; Repeat doubles the block; Half time doubles its counts; Double time halves them (an 8-count block becomes 4); Canon offsets dancer n by (n − 1) × 1 or 2 counts and the block grows by that much (dancers who finish hold their last shape).
- Canon needs 2 or more dancers: with 1 dancer the button shows the needDancers line and does nothing.
- The dance is at most 96 counts and 8 blocks: a device or block that would go past it is refused with the overLimit line.
- Formation changes: dancers walk to their new spots during the first 2 counts of the block (while doing the block's moves from the waist up); moving from Cluster always takes 2 counts.
- Play from a selected block starts there; Loop block repeats it. Any edit while playing restarts play at the current block.
- Undo, Redo and Go back to Before all make or restore versions; there are at most 40 versions (the oldest drops, with a note in the list).
- Saved on this device (localStorage `choreography-board`): the dance, its versions and reasons, your phrases, the title. **🧽 New dance** (confirm) starts from the starter; **Clear saved** removes everything. No names are asked for.
- Keyboard: Tab through panel sections first, then timeline blocks; Space plays; Delete removes the selected block; Ctrl+Z and Ctrl+Y undo and redo.
- Motion off: dancers show each count's keyframe without in-between motion; timing, music and Compare stay in step.
- Sound off: no music or voice; the count readout and playhead carry the timing.

## Look
- Accent `--brand` #3ddc97 (stage-tape mint) on a dark theater palette set on its own `:root` (not the 9-12 theme): paper #12141c, panel #1a1d28, ink #e9ecf2, muted #a3a9bb, line #2c3142, focus #ffd166, `--brand-ink` #0b1a12 for text on the accent.
- Contrast: accent on paper 10.4:1, on panel 9.5:1; brand-ink on accent 10.15:1; ink on panel 14.19:1; muted on panel 7.16:1.
- Dancers: 1 coral #ff8a7a with a circle badge, 2 sky #7cc4ff square, 3 sun #ffd166 triangle, 4 pink #f7a8d8 diamond (8.0:1 to 12.75:1 on paper); the badge shape always shows which dancer is which.
- The timeline blocks are #232838 with mint outlines when selected; device glyphs are shapes plus a 2-letter tag (Re, Rt, Mi, Lv, Tm, Dy, Sz, Ca).
- Different from design-fixer (indigo #4338ca), art-through-time (#8a2a2b), frame-it (orange on dark #ffb347), stage-blocker (theater, not yet specced: keep it off mint), and the dance siblings (teal, cobalt, lilac).

## Art
none: drawn in code (theater, dancers from simple shapes, timeline, diagrams). people: false.

## Voice
`casual-peer` (Zubenelgenubi): "Say casually and naturally, like a friendly teenager explaining something", here an older student choreographer. Changed at the wave check from easy-coach, which band-practice (6-8 music) also uses. Different from design-fixer (big-sister), art-through-time (upbeat-guide), and the dance siblings (warm-teacher, clear-teacher, knowing-guide). Narration is light; device meanings are read on screen.
| Key | Kind | Line | Stale when |
|---|---|---|---|
| wBuild | how | Here's a short dance to start. Press Play to watch it, then tap a block and try a device. | mode left |
| wCompare | how | Before is on the left, now is on the right. Press Play both and watch what your change did. | mode left |
| wShow | how | Show time. Press Play to see the whole dance from the audience. | mode left or play started |
| placeHow | how | Tap a phrase, then tap a spot on the timeline. | a block placed |
| deviceHow | how | Tap a block, then tap a device to change how it's danced. | a device used |
| compareHow | how | You made a change. Tap Compare to see before and after side by side. | Compare opened |
| makeHow | how | Pick a move for each count. Press Try it, then Save phrase when it feels right. | editor closed |
| dRepeat, dRetro, dMirror, dLevel, dTempo, dDyn, dSize, dCanon | how | Repeat: saying it twice makes it matter. / Retrograde: the phrase runs backwards, last count first. / Mirror: right becomes left. / Level: same phrase, new height. / Tempo: same moves, new speed. / Dynamics: same shapes, new energy. / Size: same moves, more or less space. / Canon: dancers start one after another, like a round. | block deselected |
| needDancers | event | Canon needs two dancers or more. Add a dancer first. | block changed |
| overLimit | event | That makes the dance too long. Remove a block first. | block changed |
| saved | event | Phrase saved. You'll find it with the starters. | editor closed |
- No line plays during Play or Show (lines queued then wait, `wait: true` on Play start; Read stops play first).

## Family engine
**dance** (`kit/dance.js`; full description in levels-and-pathways/spec.md). Uses the shared figure for up to 4 dancers with badges, `Dance.poses` (plus its 24-move palette), `Dance.level`, `Dance.dyn` (all six qualities), `Dance.phrase` with `side` (Mirror) and `travel`, `Dance.clock` (tempo changes, seek), `Dance.play` with `offsets` (Canon), `Dance.floor('stage')`, `Dance.music`, `Dance.counts`. Two `Dance.play` handles on one clock drive Compare. Devices are this tool's own transforms of a phrase (not engine parts), except Mirror (`side`) and Level (`Dance.level`). Feeds it: 12 starter phrases, 4 tracks, 5 formations.

## Sources
- National Core Arts Standards, Dance (2014), grades 6 to 8, DA:Cr1.1, DA:Cr2.1 (choreographic devices, dance structures), DA:Cr3.1 (revise, explain choices): https://www.nationalartsstandards.org/
- Choreographic devices (repetition, retrograde, augmentation and diminution, canon, unison, change of level, size and dynamics): Jacqueline M. Smith-Autard, Dance Composition: A Practical Guide to Creative Success in Dance Making, 6th ed. (Methuen Drama, 2010); Lynne Anne Blom and L. Tarin Chaplin, The Intimate Act of Choreography (University of Pittsburgh Press, 1982).
- The six energy qualities (sustained, percussive, swinging, suspended, collapsing, vibratory): Perpich Center for Arts Education, "The Elements of Dance", Energy section.
- Stage directions (stage left and right from the performer's view, upstage and downstage): J. Michael Gillette, Theatrical Design and Production, 7th ed. (McGraw-Hill, 2013), stage geography.
- Revision with reasons and peer feedback as part of choreography: NCAS DA:Cr3.1.6a to 8a.

## Done when
1. The starter dance plays on first open; Play, Stop and Loop block work; the count readout matches the playhead.
2. Each device changes the block as Content says: Retrograde runs the counts backwards, Mirror swaps sides, Half time makes 8 counts into 16, Double time into 4, Repeat doubles, Canon offsets dancers by 1 or 2 counts and lengthens the block.
3. Canon with 1 dancer and any change past 96 counts are refused with their lines.
4. Compare plays Before and Now from count 1 together; Ghost overlays them; What changed numbers match a hand recount for a Retrograde and a Half time change.
5. Go back to Before makes a new version; Undo and Redo walk the history; nothing is lost on reload, and Clear saved empties it.
6. Make a phrase saves a named phrase that shows with the starters and plays as made.
7. Show plays the whole dance once with the title and a bow, no panel.
8. At 1366x768 the stage, the timeline and Play are visible together without scrolling; at 1000x625 the preview reads (block names 11 px or more); at 375 wide the timeline scrolls sideways inside its own box only.
9. How-to and device lines are spoken once per load; needDancers and overLimit speak every time; no line plays over the music.
