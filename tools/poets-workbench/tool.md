# poets-workbench: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: poets-workbench (Curiosity No. 10)

#### Built

A writer's desk, with an editable typewriter page, live pronunciation proof, rhyme drawer, sixteen cloth-bound books,
five papers, four local draft slots, print styles, beat playback and device-local Speak. Maker's plate and Manual are
lower-left; Motion, Sound and Read are on the desk's power panel. The tempo knob works by dragging and by keyboard.
The page opens ready to type, with its real caret after Frost's opening line. No lesson frame or progression layer.

Files: `src.html`, `material.json`, `poets-workbench.html`, `tool.draft.json`, `notes.md`, `voice/lines.json`,
`audit-states.json`, `handoff.md`, `art/prompts.json`, and this report. Build only; no commits or polish round.
Final bundle: 1,185,955 bytes, about 1.186 MB against the 2 MB goal.

#### The real material

Fetched and checked 5 November 2026. Raw downloads, original staged dictionary, packing script, secondary comparisons
and hashes are retained in `_scratch/poets-workbench/`. The finished file makes no network requests.

- CMU Pronouncing Dictionary: https://github.com/cmusphinx/cmudict and its `/blob/master/LICENSE`.
  BSD-style redistribution licence; complete copyright, conditions, funding notice and disclaimer are in the Manual.
  Original staged file is 3,618,488 bytes; SHA-256 `81917843c7f44ce2b094ac63873c2c7a4cf802040792c455ba3ca406891c3d22`.
  Retained 125,938 distinct words and 135,037 pronunciations after filtering digit/period entries and duplicate forms.
  All retained entries are bundled. Sixty-nine phone symbols are packed into single characters, gzipped and base64 encoded.
  Base64 payload: 1,069,944 bytes. Full index became ready in 274 ms in the measured desktop Chrome run.
- Rhyme keys use actual sounds after the last stressed vowel. Same vowel and same final consonants are separate slant drawers.
  Names stay; an explicit classroom-language exclusion list suppresses some suggested words and changes displayed counts.
  Unknown words have dotted spelling estimates. No invented pronunciation is presented as dictionary data.
- Meter uses four real feet, starting offsets, alternate dictionary pronunciations and flexible monosyllabic function words.
  A narrow grammatical rule distinguishes record after an article/possessive from record after an auxiliary/to; it is not a general grammar parser.
- Poetry Foundation meter glossary, Harvard Guide to Prosody and Haiku Society of America definitions are named terminology references.
  Reference facts are paraphrased; their editorial prose is not bundled. Sources are linked in the Manual and metadata.

Shelf material, all fetched or compared on the date above:

- William Shakespeare, *Sonnet 18*: https://www.gutenberg.org/ebooks/19221. Public domain in the United States; full poem, not a sample.
- William Blake, *The Tiger*: https://www.gutenberg.org/ebooks/1934. Public domain in the United States; full poem, not a sample.
- Percy Bysshe Shelley, *Ozymandias*: https://www.gutenberg.org/ebooks/19221. Public domain in the United States; full poem, not a sample.
- Edgar Allan Poe, *The Raven*: https://www.gutenberg.org/ebooks/2151. Public domain in the United States; full poem, not a sample.
- Edgar Allan Poe, *Annabel Lee*: https://www.gutenberg.org/ebooks/2151. Public domain in the United States; full poem, not a sample.
- Emily Dickinson, *Because I could not stop for Death*: https://www.gutenberg.org/ebooks/12242. Public domain in the United States; full poem, not a sample.
- Emily Dickinson, *"Hope" is the thing with feathers*: https://www.gutenberg.org/ebooks/12242. Public domain in the United States; full poem, not a sample.
- Robert Frost, *Stopping by Woods on a Snowy Evening*: https://www.gutenberg.org/ebooks/58611. Public domain in the United States; full poem, not a sample.
- Robert Frost, *The Road Not Taken*: https://www.gutenberg.org/ebooks/29345. Public domain in the United States; full poem, not a sample.
- Langston Hughes, *Dream Variations*: https://www.gutenberg.org/ebooks/74745. Public domain in the United States; full poem, not a sample.
- Paul Laurence Dunbar, *Sympathy*: https://www.gutenberg.org/ebooks/18338. Public domain in the United States; full poem, not a sample.
- Edward Lear, *The Owl and the Pussy-cat*: https://www.gutenberg.org/ebooks/13647. Public domain in the United States; full poem, not a sample.
- Henry Wadsworth Longfellow, *Paul Revere's Ride*: https://www.gutenberg.org/ebooks/1365. Public domain in the United States; full poem, not a sample.
- John McCrae, *In Flanders Fields*: https://www.gutenberg.org/ebooks/353. Public domain in the United States; full poem, not a sample.
- Lewis Carroll, *Jabberwocky*: https://www.gutenberg.org/ebooks/12. Public domain in the United States; full poem, not a sample.
- William Ernest Henley, *Invictus*: https://www.gutenberg.org/ebooks/1568. Public domain in the United States; full poem, not a sample.

The fifteen staged texts were checked line by line against their named Gutenberg editions and compared with independent
Academy of American Poets transcriptions. Differences in older editions are retained and logged in
`edition-differences.json`. No modern editorial wrapper is bundled. Invictus matches both Gutenberg 1568 and
https://poets.org/poem/invictus/print word for word, ignoring presentation whitespace.
Repairs: removed the contents page from the Owl entry; retained only Dream Variations from a multi-poem extract;
restored Road Not Taken's five-line stanzas; removed Jabberwocky's title from its verse; rejoined one wrapped Raven line.
Long dashes become commas/spaces and apostrophes are normalised. No shared library file was changed.

Literary notes also checked: Pope's The Rape of the Lock, Gutenberg 9800 and Wikisource Cantos I/III; Poe's The Philosophy
of Composition, Gutenberg 55749 and Wikisource. Original works are public domain; only short factual notes are bundled.
Orange/month zero-rhyme counts and record's three forms were independently recomputed from the staged dictionary.
The spec's 126,052-word count is the unfiltered figure; the live desk labels its actual filtered count.

#### Break the instrument

- Semantic assertions: Frost opening = 8 syllables, iambic tetrameter; pizza line = 8, same meter; hot includes lot/not/spot;
  orange = 0 perfect rhymes with real slant results; record cycles all three sound sequences; noun/verb example differs.
- Dickinson's first stanza = 8, 6, 8, 6; ourselves selects the two-syllable form. All sixteen poems load as editable copies.
- Empty text, symbols, rapid edits and 1,000-word input stay responsive. The latter rendered in 12.8 ms in the measured run.
- Every draft slot round-trips; a blocked-storage test gives a visible fallback without losing the current page.
  Stress choices survive appending text. Pasted markup stays text. Native typing and a native tap on orange were verified.
- Actual Web Audio gains alternate 0.065 and 0.22; measured beat intervals are about 0.6 s at 100 BPM.
  Sound off creates zero sound nodes. Motion off has zero running animations. Playback survives a live resize.
- Real jittered pointer drag changes 100 to 140 BPM; native arrow keys announce 105 BPM. Keyboard navigation loads the sixteenth book.
- Large rhyme sets append 150 entries at a time; the tested slant drawer grows from 150 to 300 without freezing.
- Contextual assonance checks: sunshine/sun both marked; weak I in I think I know is not falsely marked.
  The mirror uses the textarea's client width, including scrollbar space, and print overrides that width for the sheet.
- Final 375 and 680 drawer checks leave the editor clear of the drawer. The 680 editor remains 98 px high;
  its real caret accepts keyboard input immediately on opening without scrolling the outer page.

#### Voice walk

The declared bank is smooth-narrator, Algieba. `allLines()` and `voice/lines.json` both contain only Type a line.
The fixed recording was not supplied, and the build instructions prohibit recording it here. Read therefore displays
and announces that fixed hint as text; it never falls through to browser speech or reads the student's writing.
This is an open voice deliverable, not a passed narration check. `__tool.vlog` stays empty without the clip.
Speak is separately gated to installed English voices whose `localService` is true. Its tested utterance selected a
local voice. Sound off cancels playback and speech. The ten-minute walk contains no browser errors or network requests.

#### Short test

The 600.1-second scripted exploration covered a grade-7-style writing path and an adult's scansion/revision path.
These answers are build judgements from use and frame inspection, not observations of children or a usability study.

- Would a kid open it unassigned? Likely yes: names, invented words and immediate rhymes make the first action interesting.
- Would an adult play for fun? Yes for a writer: real pronunciation alternatives, editable poems and reversible stress decisions have depth.
- Is the real thing the interface? Yes: the words, sounds, syllables and proof marks are the working surface itself.
- Does it work without a score or finish? Yes: nothing asks for an answer, awards success or ends the writing session.

| This desk | Reference studio |
|---|---|
| ![Poet's desk](../../_scratch/poets-workbench/final-check-frames/tempo-knob.png) | ![Beat Lab](../../_scratch/poets-workbench/models-retry/beat-lab.png) |

The density comes from real controls and material. The desk takes the family marks from Span and Spire and Pocket Universe,
while its paper, red pencil, walnut and cloth bindings have their own grammar. All four required models were opened and inspected.

#### Lesson creep check

Word-boundary search of source and voice lines for score, points, level, goal, sticker, badge, correct, wrong, try again,
complete and well done: zero hits. No kit header, mode pills, quiz, target list, rewards or ending screen.
Match counts are scansion readouts requested by the spec, rather than an assessment.

#### Done when

1. PASS: scanned opening and native new-line typing; the 600-second walk recorded counts 8, 8, 8.
2. PASS: opening is 8 syllables and iambic tetrameter, independently asserted.
3. PASS: orange has 0 perfect rhymes plus slant families; hot has lot, not and spot.
4. PASS: all three record pronunciations cycle, with stress changing between noun and verb.
5. FAIL in part: Dickinson is 8, 6, 8, 6; strict CMU gives Frost AABA CCDC DDED EEEE, not the conventional scheme in the spec.
   Here has IY R while queer/year have IH R. The tool keeps the actual sound rule; the Manual explains the literary scheme.
6. PASS: invented Jabberwocky words have dotted estimates; the title is not counted as verse.
7. PASS: strong/weak sound contrast is measured; Motion off removes drawer motion.
8. FAIL in part: native keyboard, value announcements and Read's privacy guard pass; the required recorded hint is absent.
9. PASS: all required sizes inspected, with follow-up fixes at 375 and 680. Scrolling is within the page/drawers only.
10. PASS: one offline file under 2 MB, full CMU notice, no em dashes, short test recorded, scoped repository contract check passes.
11. PASS: no score, goal, level, sticker or finish screen.

#### Audit leads

The required audit ran once to completion with 69 leads. Its full report is `_scratch/poets-workbench/audit/audit.md`.
The pre-fix report is preserved; the full audit was not repeated after the scoped fixes.

- Fixed: source links below target height, the 8.3 px drawer note, narrow drawer/control overlap and the covered rhyme handle.
  Follow-up frames and measurements show source links at least 44 px, drawer note 10 px, and clear page/drawer bounds.
- Intentional: the quiet first hint overlays the transparent editor's empty line and disappears on input.
  Manual and Drafts are modal drawers, so they cover and temporarily disable the page. Short Drafts uses internal scrolling.
- Expected instrument behaviour: opening rhymes changes the paper width; hidden first-run hint after action is deliberate.
- Print's external dialog does not change the headless page; the knob needs drag or arrow input, both explicitly tested.
  Shelf items below the visible rack scroll; roving keyboard navigation reaches the last item and loads it.
- The audit's absent welcome is the missing recording already marked FAIL above. No substitute or repeated voice was invented.
- The real editor intentionally receives focus on open to fulfil the spec's ready-to-type caret; native input is verified.
- Audit Motion off and mid-action resize checks report no exceptions or controls left disabled.

#### Frames looked at

Required four models; early first-page/drawer/preview frames; all twelve full size/state captures in `layouts/`;
all six walk frames; all 34 audit PNGs on nine contact sheets, with key small-size/modal frames enlarged;
three final functional frames and all follow-up frames in `final-layouts/`, plus the final sound-repeat frame.
Every generated frame was examined directly or on its labelled contact sheet. Pixel text was checked on enlarged representative states.

#### Art made

No painted images. Paper, curl, chrome bail, ruler, walnut, cloth books, index cards, proof marks, knob and engraved plate
are drawn in HTML/CSS and native text. `art/prompts.json` explicitly lists no bitmap assets. No people assets.

#### Engine changes wanted

None. Shared files were not edited. The fixed hint clip belongs to the normal voice-preparation pipeline.

#### Left open

- Supply the smooth-narrator recording of Type a line. before treating narration as ready.
- The conventional Frost scheme conflicts with the specified strict dictionary rule. No accent-normalisation rule was invented to force it.
- Meter remains a closest-pattern hypothesis; unknown pronunciations are estimates. The desk exposes these limits in its Manual.
- School Chromebook hardware and a physical printer were not available. Desktop Chrome timing and print styles are not a hardware certification.
- The global check_tools run would rebundle other tools, outside the write boundary. The actual checker was scoped in process to this tool,
  with its neighbour bundling suppressed; metadata, syntax, network patterns, size, headings and contrast were also checked separately.
- SCOWL common-word ordering stays in the later fix round specified by the owner. No extra lexicon was gathered.

Unattended choices: replacement is the default rhyme insertion, with an insertion toggle; all five papers remain free guides;
older poem editions are retained and named. The Curiosity brief overrides old download prohibitions and the lesson frame.
All owned Chrome/server processes are closed. The report is written last to honour the requested stop boundary.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: poets-workbench

#### Played

Cold as a grade-7 writer, then an adult revising sound: all sixteen shelf poems, all five papers, the rhyme drawer, stress choices and beat transport.
The continuous cold walk lasted 520.8 seconds; initial play and further control/extreme checks took total use beyond ten minutes. Builder files stayed closed until the cold walk ended.
The desk feels like an instrument: paper, words and red proof marks carry the interaction. No lesson criteria, quiz or reward system were imposed.

#### Short test

- Would a kid open it unassigned? Likely: names, nonsense words and instant rhymes invite experiments. This is reviewer judgement, not a child study.
- Would an adult play for fun? Yes: real pronunciation alternatives and revision give the page depth; live tempo and useful rhyme ordering now keep the flow.
- Is the real material the interface? Yes: editable verse, CMU phones, syllables, stress and audible strong/weak beats are the working surface.
- Does it work without a score or finish? Yes. No goals, scores, levels, quiz, finish screen or kit header were added; source/voice lesson-creep search is empty.

#### Findings fixed

- **Blocker, general, Drafts:** valid JSON such as `null`, `{}` and malformed slots crashed the drawer. Validate four slots, text, paper, lens and override shapes; ignore invalid pronunciation indices.
- **Should fix, instrument, tempo:** turning either tempo control stopped playback. A single next-beat scheduler now follows the running tempo without restarting the cursor; ended audio nodes are released.
- **Should fix, general, stale drawer:** loading a draft could leave the previous word's rhyme cards visible. Loading/editing now closes them and resets `aria-expanded` consistently.
- **Should fix, access, proof controls:** small printed marks were the only pointer route to stress changes. Added an equivalent 44-pixel Stress key with the current word/value announced; kept exact textarea/proof alignment. Audit threshold is now 44, rather than a global 27-pixel exception.
- **Should fix, general, modal keyboard:** Alt R/F could modify the covered page through an open Manual/Drafts drawer. Modal drawers now guard these shortcuts.
- **Should fix, craft, 680x425 rhymes:** cards had almost no visible height. Compact spacing preserves 44-pixel keys and exposes usable rhyme rows.
- **Should fix, craft, Drafts:** audit confirmed slots 3/4 and Print hidden at 680x425. A compact two-column slot layout exposes the whole short choice set.
- **Polish, play:** alphabetic names flattened rhyme browsing. Applied the spec's SCOWL size-50 lean: within each syllable group, common-word tiers precede remaining entries. All CMU words remain available, subject to the existing classroom exclusion list.
- **Polish, readouts:** one syllable no longer claims “dactylic 0.3 feet”; singular syllable/line labels agree with their numbers.
- **Polish, real material:** removed Annabel Lee's bibliographic `1849` from editable verse. Read no longer replaces the poem's source caption with a build-status message.

#### Findings left

- **Blocker, voice:** the required smooth-narrator “Type a line.” recording is absent. No supplied clip exists. The [Ground rules](../../docs/agents/CODEX-BUILD.md#ground-rules) say “Do not download anything or record audio”; the Curiosity data exception does not authorise recording. I retained the spec's recorded-only privacy guard and did not substitute browser narration. Narration remains unready.
- **Spec conflict:** strict CMU produces Frost `AABA CCDC DDED EEEE`, rather than conventional `AABA BBCB CCDC DDDD`. `here` uses IY R; `queer/year` use IH R. Preserved real phones and the Manual's explanation instead of inventing accent normalisation.
- **Intentional:** the real editor receives initial focus to provide the spec's ready-to-type caret. The quiet hint sits over its empty second line and disappears on action. Modal drawers intentionally cover and disable the page.

#### Break it

- No score, check or success meter exists to cheat. Pattern-match counts are descriptive scansion, not rewards.
- Empty/whitespace, punctuation, emoji, numbers and pasted markup stay safe; markup remains text. Unknown invented words retain dotted estimates.
- All foot lenses and paper guides tested; tempo 60/160 tested repeatedly, plus real jittered knob drags to both limits while playing.
- Sixty rapid input events leave the final text intact. A 20,000-letter unknown token generated 10,000 estimated beats without freezing; render took about 187 ms on this desktop.
- `record` cycles real pronunciations; the noun/verb sentence differs. Keyboard Tab/Enter changes stress, arrows/Enter insert a rhyme and focus returns to the editor.
- Orange: 0 perfect, 7,822 same-vowel and 76 same-ending entries in this filtered snapshot. Held clicks traversed every rhyme tab twice. Hot includes lot, not and spot, now near the front.
- Measured gains: weak 0.065, strong 0.22. Measured beat gaps change from about 1 s at 60 BPM to 0.375 s at 160 BPM; playback survives 1366 → 760 → 680 resizing.
- Sound off creates no audio nodes; Motion off leaves zero running animations. Grayscale retains marks, letters and readable controls.
- Corrupt draft cases, loading with rhymes open, empty playback and shortcuts through a modal were replayed after repair. No application exceptions in the rechecks.

#### Voice walk

Sound on; held clicks about two seconds apart: type → Play → rhymes → Manual → shelf → papers → Drafts → Read → Sound off → Read → Sound on.
Only one fixed line is declared, exactly matching `allLines()` and `voice/lines.json`. No extra per-mode lesson narration was introduced.

| Line/kind | Expected | Heard |
|---|---|---|
| Type a line / initial hint | once | 0: recording missing |
| Type a line / Read, Sound on and off | each Read | 0: recording missing |
`__tool.vlog` remains empty. Read does not speak student text. Speak separately uses only installed English voices with `localService: true`.

#### Facts checked

Data and reference checks are dated 5 November 2026. Raw sources, hashes, comparisons and reproducible scripts are retained in Scratch.

- **CMU:** [Carnegie Mellon dictionary and licence](https://github.com/cmusphinx/cmudict). BSD-style terms retained in full in the Manual. Independently decoded every packed pronunciation: 125,938 filtered words, 135,037 pronunciations, zero missing/extra/mismatched entries versus the staged source. Raw source has 126,052 words and 135,166 pronunciations; this is an identified snapshot, not a claim that all CMU editions are identical.
- **Dictionary claims:** independent phone-tail computation confirms orange/month zero perfect rhymes, record three pronunciations, and brillig/slithy/toves absent. The actual chosen phones explain temperate/date and Frost's split. Evidence: `review-dictionary.json`, `review-packed-verification.json`.
- **Meter/readouts:** [Harvard Guide to Prosody](https://poetry.harvard.edu/guide-prosody), [Poetry Foundation meter](https://www.poetryfoundation.org/education/glossary/meter), and [common measure](https://www.poetryfoundation.org/education/glossary/common-measure). Foot directions and four/five-foot names checked. Fresh engine checks give Frost's opening 8/iambic tetrameter, pizza 8, Dickinson's first stanza 8/6/8/6. These are hypotheses about readings, not grading rules.
- **Haiku:** [HSA definitions, including its 2026 clarification](https://hsa-haiku.org/hsa-definitions.html), cross-checked with [Penn State's sound-unit discussion](https://cgs.la.psu.edu/teaching-resources/k-12-resources/cgs-k-12-curricular-materials/high-school-level-8-12/japanese-painting-and-calligraphy-on-scrolls/understand-haiku/). English 5/7/5 is a writing convention, not Japanese on. Editorial prose is not bundled.
- **SCOWL:** [2020.12.07 source and Copyright](https://github.com/en-wl/wordlist/tree/rel-2020.12.07/scowl), [downloaded release](https://downloads.sourceforge.net/wordlist/scowl-2020.12.07.tar.gz). MIT-like collective permission plus component terms retained verbatim from the release. Sampled only English/American word lists through size 50, lowercase entries intersecting CMU: 44,537 words. This is a browsing tier, not measured frequency. Raw tarball, Copyright and packer are in `data/review-scowl/` and `review_pack_common.py`.
Each shelf text below is a full poem, not an invented sample, and **public domain in the United States**. Named primary editions were freshly downloaded; all bundled lines match after stated typography normalisation.

| Material | Primary edition |
|---|---|
| Shakespeare, Sonnet 18; Shelley, Ozymandias | [The Golden Treasury, PG 19221](https://www.gutenberg.org/ebooks/19221) |
| Blake, The Tiger | [Songs of Innocence and of Experience, PG 1934](https://www.gutenberg.org/ebooks/1934) |
| Poe, The Raven; Annabel Lee | [Works, volume 5, PG 2151](https://www.gutenberg.org/ebooks/2151) |
| Dickinson, Because I could not stop for Death; Hope | [Poems, 1890 edition, PG 12242](https://www.gutenberg.org/ebooks/12242) |
| Frost, Stopping by Woods on a Snowy Evening | [New Hampshire, PG 58611](https://www.gutenberg.org/ebooks/58611) |
| Frost, The Road Not Taken | [Mountain Interval, PG 29345](https://www.gutenberg.org/ebooks/29345) |
| Hughes, Dream Variations | [The Weary Blues, PG 74745](https://www.gutenberg.org/ebooks/74745) |
| Dunbar, Sympathy | [Complete Poems, PG 18338](https://www.gutenberg.org/ebooks/18338) |
| Lear, The Owl and the Pussy-cat | [Nonsense Songs, PG 13647](https://www.gutenberg.org/ebooks/13647) |
| Longfellow, Paul Revere's Ride | [Poetical Works, PG 1365](https://www.gutenberg.org/ebooks/1365) |
| McCrae, In Flanders Fields | [Poems, PG 353](https://www.gutenberg.org/ebooks/353) |
| Carroll, Jabberwocky | [Through the Looking-Glass, PG 12](https://www.gutenberg.org/ebooks/12) |
| Henley, Invictus | [Poems, PG 1568](https://www.gutenberg.org/ebooks/1568) |
Second-source comparisons use the saved Academy of American Poets transcriptions from the same date; direct downloads returned 403 in this review. Fresh web access separately confirmed [Invictus](https://poets.org/poem/invictus/print), [Sonnet 18](https://poets.org/poem/shall-i-compare-thee-summers-day-sonnet-18/print) and Frost via Poetry Foundation. Older-edition contractions and Dickinson's different stanza text are retained and disclosed; see `review-text-verification.json`.

- **Literary observations:** Pope's obey/tea and away/tea pairs checked in [PG 9800](https://www.gutenberg.org/ebooks/9800) and saved Wikisource Cantos I/III; Poe's trochaic/eight-foot/shorter-line account checked in [PG 55749](https://www.gutenberg.org/ebooks/55749) and the [University of Virginia edition](https://anthology.lib.virginia.edu/work/Poe/poe-philosophy). Original works are public domain; notes are paraphrases. Frost's repeated ending and conventional chain are visible in the primary poem and [Poetry Foundation text](https://www.poetryfoundation.org/poems/42891/stopping-by-woods-on-a-snowy-evening).

#### Sensitivity

Preserved all authors and poems. A later cultural lens should look at Hughes's Black identity, Dunbar's caged-bird imagery, McCrae's war/recruitment language, Longfellow as literary history, death/grief in Poe/Dickinson and Henley's religious imagery. Notes now flag these. Haiku guidance explicitly distinguishes Japanese on from English syllables. No new cultural claims or people art were added.

#### Flattest moment left

Some pronunciation choices sound odd in real speech even when they fit a repeating foot. The Manual calls the result a closest-pattern hypothesis; the writer can disagree and revise. The real remaining interruption is silent Read until its recording is supplied.

#### Graphics

Kept the walnut, chrome bail, cloth books, paper curl, proof ink and engraved plate. No raster images or people were added. Final bundle: 1,603,263 bytes, below 2 MB.
All cold-walk, required-size and changed-state frames were viewed, individually or on labelled contact sheets; narrow drawer/Drafts fixes were enlarged. Frame comparison:

| This instrument | Reference studio |
|---|---|
| ![Poet's working page](../../_scratch/poets-workbench/review-final/raven-desk.png) | ![Beat Lab](../../_scratch/poets-workbench/review-reference/reference-beat-lab.png) |

#### Audit

The single audit finished within its 40-minute limit: **38 leads, 40 frames**, at 44-pixel desk targets. Full evidence: `_scratch/poets-workbench/review-audit/audit.md`.

- Confirmed/fixed: Drafts' short-window choice clipping. Re-shot 680x425 (including blocked saving), 1366x768 and the 375x812 iframe; all eight Save/Load keys and Print are visible. All four slots round-trip text, paper and stress choices. Unbroken draft titles now wrap on phones.
- Intentional: initial ready-to-type focus; a pointer-transparent hint over the empty line; its disappearance after action; modal drawers covering the underlying editor/Manual button. These are Curiosity behaviours, not missing lesson instructions.
- Confirmed functional: Print opens an external dialog, so the page need not change; the knob responds to real drags, not a tap; the shelf scrolls and roving keys reach the final Invictus book. The cold walk loaded the Owl entry that the audit's clipped-centre click missed. Opening rhymes deliberately reserves paper space.
- Motion off and mid-action resize report no exceptions or stuck controls. Missing narration is the open blocker above. Rechecks had no application errors; the standalone test host's favicon 404 is wrapper noise, not an offline-tool request.
The full audit was not repeated after its scoped Drafts repair. The repository checker was run against an isolated Scratch copy with draft metadata as tool.json, using the actual checker functions without rebundling other tools: syntax, contract and notes checks pass.

#### Done when

1–4: PASS for live typing/opening, 8-syllable Frost line, real rhyme results and record alternatives. 5: Dickinson PASS; conventional Frost chain conflicts with strict data, documented above.
6–7: PASS for dotted unknowns, strong/weak playback and reduced motion. 8: keyboard/value/privacy PASS, required fixed narration FAIL. 9: required sizes inspected; changed narrow states rechecked.
10: one offline file under 2 MB, licence notices, no em dashes and scoped contract/syntax checks PASS. 11: no lesson progression or rewards, PASS.

#### Left open

Supply the specified fixed hint recording before treating the tool as ready. No kit change is needed. Do not silently force Frost's conventional scheme into CMU's exact-phone output.
School Chromebook hardware and a physical printer were unavailable. Desktop timing and print CSS are not hardware certification.
Unattended decisions followed the brief: SCOWL common-word sort, faithful older editions/CMU phones and a large equivalent Stress control. No questions, commits, other-tool edits or second review pass. All owned Chrome/server processes closed; temporary host removed.

<!-- end part -->

## Refine

<!-- part: refine.md -->

OPEN (round 1, Claude Refine 2026-11-05; Codex fixes next)
Counts: blockers 4 (general 1, family 3), should fix 18 (general 6, family 12), polish accepted 11

### Refine: poets-workbench

Lens files: `refine/teaching.md`, `refine/play.md`, `refine/craft.md`. Frames: Teaching in
`S:/CurioClass-codex-scratch/poets-workbench/teaching/frames/`, Play in `.../play/`, Craft in `.../craft/frames/`,
shared audit in `.../audit-r1/`. Integrator spot-checks (2026-11-05): `BLOCKED` at src.html:287-290 is about 70 words
and "coon" shows in the default Perfect list for "moon" (craft `frames/moon-drawer.png`); `lengthName` at
src.html:406 prints `feetCount.toFixed(1)+' feet'`; the two-letter labels at src.html:424 are joined with no gap at
src.html:469; `#mirror` has a `transform` (own stacking context) and `#editor` comes after it, so `.proof{z-index:3}`
cannot lift the marks over the textarea (src.html:74-75, 84). All four claims hold.

#### Blocker

1. **The rhyme drawer offers slurs and explicit words as rhymes for everyday words.** `BLOCKED` src.html:287-290,
   `rhymeList` src.html:581-596; every drawer kind. "moon" lists coon (in the common-words tier, on screen without
   scrolling), coons, spook, redskin, douche; "like"/"bike" list dyke, gook, polack; "map" lists jap, japs, rape, wop;
   "top" lists wop, darkie, nazi; "hit"/"pick" list tits, prick, redskin, niggard (craft `frames/moon-drawer.png`,
   `frames/like-drawer.png`, `s2.json`: 13 of 72 common test words surface at least one). Rule 6. Fixed looks like:
   (a) a broad classroom offensive-word filter (ethnic, racial, religious, disability, LGBTQ and Native slurs, sexual
   and explicit terms, expletives and their spelling variants and plurals), not a few added words; (b) the words are
   dropped at pack time in the Scratch pack script, so the shipped bundle neither offers them nor lists them in view
   source (this takes in Craft's polish item 9: no slur list in plain text in a public K-12 page or repo); (c) a check
   script in Scratch that runs the Perfect, Same vowel and Same ending lists of every word in the SCOWL common tier
   (and at least moon, like, bike, map, top, hit, pick, late, spot, night, ball, back) against the filter and fails on
   any hit; its output and the final filter list go in notes.md for the exit check. (d) The final filter list goes to
   the fresh-agent sensitivity review (rule 5: it touches Native, ethnic and LGBTQ terms); its PASS is part of the
   gate. Keep the spec's "names stay" rule for ordinary names; a surname that is also a slur goes. (general)

2. **"here"/"hear" do not rhyme with "near", "year", "fear", so Frost's scheme and the drawer are wrong.**
   `pronunciation()` src.html:322 (rhyme keys), `poemAnalysis` src.html:414-428, Manual src.html:840. CMU writes
   here, hear, ear, tier, we're as `IY1 R` (31 entries) but near, year, fear, dear, clear, queer as `IH1 R` (192), a
   dictionary inconsistency, not a real difference in American speech. Seen: Stopping by Woods, the default poem,
   reads `AABA CCDC DDED EEEE` (teaching `t-frost.png`), so Done when 5 fails; the drawer for "hear" lists 34 perfect
   rhymes, mostly surnames, without fear, near, dear, year, clear (`t-hear.png`); a student's own couplet "standing
   here / have you near / sky is clear / another year" reads ABBB (play q09). The Manual note calls the split
   "strict" hearing, which tells students two words they say alike sound different. Fixed: fold `IY R` into `IH R`
   when building rhyme keys (and check the other pre-R vowel pairs CMU mixes the same way), state it in the Manual as
   a normalisation like primary and secondary stress, drop the "strict" note. Frost reads AABA BBCB CCDC DDDD.
   (family:curiosity)

3. **Meter names with fractions of a foot: "anapestic 2.7 feet", "trochaic 3.5 feet".** `scanLine` src.html:405-407.
   227 of 529 shelf lines show a decimal; 85 show thirds (teaching `meters-out.json`). The Tiger: 12 of 24 lines
   "trochaic 3.5 feet"; The Raven: 42 lines "trochaic 7.5 feet"; Invictus "anapestic 2.7 feet"; every classic
   limerick line "anapestic 2.7 feet" even with the Anapest lens on (play q07-limerick-frame.png); "trochaic 39.0
   feet" on a long line (play p15). A grade 7 student learns meter comes in fractions: a meter that misleads when its
   assumption fails. Fixed: name the length from whole feet or stressed beats and say the remainder in words
   ("trochaic tetrameter, last syllable dropped", "anapestic trimeter, missing its first syllable", "iambic
   tetrameter + 1 extra"); never print a decimal; very long lines say "N feet" with a whole number. (family:curiosity;
   Play tagged it general)

4. **The rhyme-scheme strip runs two-letter labels together into a false scheme.** Letters src.html:424, strip
   src.html:469. After Z the letters go AA, AB..., joined with no gap, so The Raven's last stanzas read
   `AABABBBB AABACBBB ADBJBBB AEBAFBBB`, which looks like 8- and 7-line stanzas in a poem of 6-line stanzas (teaching
   `t-raven-end.png`); Paul Revere's Ride the same. Fixed: separate letters inside each stanza group when any label
   has two letters (A·B·AB), or restart lettering where the reader needs it; margin letter and strip use the same
   form. (family:curiosity)

#### Should fix

1. **Tapping a stress mark does not flip it; it opens the rhyme drawer.** `.proof` src.html:84-88 under `#editor`
   src.html:75; handler src.html:928-936. `elementFromPoint` on a mark returns the editor; a click on the "/" over
   "woods" placed the caret and opened the drawer, mark unchanged (craft `frames/proofclick-after.png`). The spec
   control, Things to do 5 and the Manual all promise it. Fixed: lift the marks above the editor (z-index on
   `#mirror` with `pointer-events:none` on everything but `.proof` buttons) so a tap on a mark flips or steps it.
   (general)

2. **Read does nothing visible and carries a build note.** `$('read').onclick` src.html:1042-1050; Manual
   src.html:824-825. With no clip (expected until the Forge, BASELINE rule 18), Read only changes a tooltip and puts
   "Type a line. The recorded hint is not supplied in this build." in the live region; the hint stays hidden
   (play p17-read-press, craft `read-after-typing` in `s3.json`, `vlog` empty). The Manual says Read "shows and
   announces the hint as text", which is not true. Fixed: until the clip lands, Read shows the hint on the page again
   and announces only "Type a line."; remove "not supplied in this build" from the Manual, tooltip and live region
   (it belongs in notes.md). (family:curiosity; Play tagged it general)

3. **Play is silent on the default screen.** The caret opens on the empty line under the Frost line, so the red Play
   key only announces "This line is silent..." to the live region; nothing is seen or heard (play q05-play-mid.png,
   `playing:false`; with the caret on line 1 it works, r01-play-line1.png). Fixed: on an empty line Play taps the
   nearest line above with words (or the poem), so the first press always makes sound and light. (general)

4. **Long poems drop well below 60 fps while typing.** `render()` src.html:450-522 re-scans every line and rebuilds
   the whole mirror 60 ms after each key. The Raven: about 20 ms per render unthrottled, 131 ms at 4x CPU throttle;
   typing into it at 4x, 61 of 208 frames over 33 ms, p95 122 ms (craft `scripts/throttle.py`, `typing` in
   `s2.json`). Fixed: cache `scanLine` by line text, lens and overrides, and patch only changed `.verse` nodes; re-run
   the 4x throttle on The Raven and report p95. (family:curiosity)

5. **One-syllable words with two pronunciations can never be corrected.** src.html:613-614. Stress and Alt F only
   flip stress for one-syllable words; they never step tears (T EH1 R Z / T IH1 R Z), wind, read, lead, live, bow,
   close to their other pronunciation, and the rhyme letter takes whichever variant fit the meter. Invictus reads
   ABAB CDCE FGHG IBIB (tears/years split, unbowed takes B OW1 D against aloud); flipping "tears" left the scheme
   unchanged (play q04-invictus-tears). Fixed: step such words through their pronunciations (then stress), and let
   an end word prefer a variant that rhymes with a nearby line end. (family:curiosity)

6. **Names read stressed on both syllables (secondary stress counted strong).** CMU gives many names a final `IY2`
   (cory `K AO1 R IY2`; 552 entries end `IY2`), so Cory, Kylie, Aiden show `/ /` and Aaliyah `/ / /` (teaching
   `t-name.png`, play p05); "midnight" costs The Raven's first line a match. Things to do 1 is "type your name".
   Fixed: treat secondary stress as flexible (follows the meter, like free function words, shown as such), or at
   least a word-final `IY2` in a two-syllable word as weak; say so in the Manual. (family:curiosity; Play rated it
   polish, general)

7. **Common words outside the dictionary get first-syllable stress and break shelf lines.** `variants()`
   src.html:339-347. "unconquerable" scans /xxxx and Invictus falls to a fractional meter; Paul Revere's Ride has 21
   unknown words, most made of known parts: hyphenated compounds (pea-green, hoof-beats, to-night, belfry-tower),
   possessives (bosom's, demon's, sentinel's), old -'d endings (mock'd, stamp'd, untrimm'd) (teaching
   `meters-out.json`). Fixed: look up hyphenated parts separately, drop 's, read -'d as the -ed word minus a
   syllable; real coinages (brillig) stay guessed and dotted. (family:curiosity)

8. **In Auto, a poem's meter name changes from line to line.** `scanLine` per line, src.html:361. The Road Not Taken
   (iambic tetrameter) names 9 meters in 20 lines and "dactylic trimeter" (6 lines) outnumbers "iambic tetrameter"
   (4); Ozymandias puts 4 of 14 lines in "dactylic 3.3 feet" (teaching `t-road.png`, `meters-out.json`). Fixed inside
   the spec's rule (the line takes the foot that matches most syllables): break ties toward the poem's most common
   foot, and show the poem's meter in the top strip ("mostly iambic tetrameter") so a line that differs reads as a
   variation. The bigger change (judge every line against the poem's foot by default) is under the spec's open
   questions. (family:curiosity)

9. **Sounds shades nearly every word, so The Raven's inner rhymes cannot be found.** src.html:474-485. Assonance
   counts function words and uses one plum for every repeated vowel over the whole word box including its marks: 408
   words shaded on The Raven (play p06-raven-sounds.png, teaching `t-sounds-raven.png`); on "Peter Piper" the IH and
   EH pairs look the same (play q08-sounds-simple.png); function words "alliterate" ("The ... the"). Things to do 8
   and 9 depend on it. Fixed: leave free function words out, one ink per repeated vowel (dreary/weary one,
   napping/tapping/rapping another), shading at text height only, and mark rhymes inside a line (same perfect key)
   distinctly. (family:curiosity; Play rated it polish)

10. **The alliteration underline is the same green as rhyme family B.** `.word.allit` src.html:82 and `COLORS[1]`
    src.html:275 used by `.word.ending`. With Sounds on, B end words and alliterating words carry identical green
    underlines ("lore" and "quaint", "curious", "forgotten" in The Raven, craft `frames/raven-sounds.png`); assonance
    is colour only. Fixed: draw alliteration as a distinct mark (bracket or dotted mark at the first letter, not an
    underline), keep it out of the rhyme inks, and give assonance a shape as well as a colour. (general)

11. **Paper guides are drawn on top of the syllable count.** Left margin, haiku, limerick, common, sonnet. The faint
    guide number or letter overprints the count, so 5 against 5 or 8 against 6 is a smudge (play q06-zoom-margin.png,
    q07-zoom-margin.png, r05-sonnet-paper.png). Fixed: guide beside the count ("5 / 5") or in its own column; letters
    for limerick and sonnet beside the rhyme letter. (family:curiosity)

12. **Paper guides count blank lines.** `guideFor(li)` src.html:430 uses the raw line index, so a stanza break takes
    a guide slot: Sonnet 18 on sonnet paper puts "C" on the blank line and every later letter is off by one (play
    r05-sonnet-paper.png); common meter on Dickinson would shift to 6, 8, 6, 8 after the first break. Fixed: count
    only lines with words; haiku and limerick restart at each stanza. (family:curiosity)

13. **Replace word is on by default.** `state.replace:true` src.html:274; drawer. Tapping "spot" for "I like to eat
    my pizza hot" gives "I like to eat my pizza spot" (play q03-insert-spot). The spec says Enter "inserts at the
    caret". Fixed: default to inserting at the caret as it was before the tap (or at the start of the next line),
    Replace as the option. (general)

14. **The drawer buries common rhymes under surnames.** Groups sort by syllable count first, so the one-syllable
    group of "hot" holds 154 entries and turns to surnames by row five (baht, bhatt, bott, brott; play
    q02-click-hot.png); "think" reaches cinq, finck, hinck within five rows (p13-midline-click.png); forgot and apricot
    sit below about 150 names. Fixed, keeping the spec's syllable grouping: the common-words tier grouped by syllable
    count first, then one "Names and rare words" fold (also grouped) after it. (family:curiosity)

15. **The pronunciation readout has no key.** Drawer head `#phones` src.html:603; Manual. "HH IY1 R" and "/ x · 2/3"
    are never explained, though the Manual's own facts use the symbols ("tea has IY"). Fixed: a short Manual key
    (digits 1 main, 2 second, 0 none; a small table of vowel symbols with example words) and label the index on
    screen ("pronunciation 2 of 3"). (family:curiosity)

16. **Alt R and Alt F do not work on a Mac.** src.html:1028-1029 test `event.key`; Option+R gives "®" and Option+F
    "ƒ", which also get typed into the poem. Found by reading code (no Mac here). Fixed: test `event.code` 'KeyR' and
    'KeyF'. (general)

17. **Form is shown but never linked to meaning (RL.7.5), and notes overstate RL.7.4.** Manual "Things people have
    found" src.html:839 ("its final two lines repeat" stops short of why). Fixed inside the Curiosity shape: a few
    found-entries that join form to meaning (Frost's repeated last line; the short "In Flanders fields." line;
    Sonnet 18's couplet turning to "So long lives this"; "Nevermore" closing every Raven stanza), each sourced, plus
    one form question in notes.md "Talk together"; notes.md "What it teaches" says "the sound half of RL.7.4". No
    goals or prompts on the desk. (general)

18. **Stray ":," marks in two shelf texts.** material.json: The Raven line 26 "here I opened wide the door:,";
    Annabel Lee line 37 "Of the beautiful ANNABEL LEE:,". Left by the dash clean-up. Fixed: one mark each, checked
    against the source text (a semicolon or colon, no em dash). (family:curiosity)

#### Polish accepted

1. **The match count counts free syllables.** src.html:408. "I hear the rain" reads 4 of 4 because free words always
   match. Better: count fixed syllables and show free ones ("6 of 6 · 2 free"). (teaching P1)
2. **Manual wording above grade 7.** src.html:804-836 ("compares a foot at each starting offset", "a universal
   account of speech"). Plain sentences with an example word each. (teaching P2, general)
3. **Content notes under a builder heading.** notes.md "Review care points" mixes shelf content (death, grief, war,
   Hughes) with layout notes. Move the content to a "Content notes" line in Good to know (BASELINE parent-preview
   call); drop the build notes. Not a request for a shelf review. (teaching P3, general)
4. **Unstressed-only forms in perfect rhymes.** "the" (`DH IY0`) ranks high for "tea", "a" for "obey", because a word
   with no stressed vowel falls back to its first vowel (src.html:322-324). Leave unstressed-only forms out of
   perfect rhymes. (teaching N1, family:curiosity)
5. **A click to place the caret reflows the desk twice.** Editor click src.html:919-927 opens the drawer on any click
   in a word; the page narrows 50 px and shifts (848 to 798 wide, 293 to 198 px left), then moves back on the next key
   (play p13-midline-click.png, craft `clickword` in `s2.json`); at 680x425 the tapped word wraps under the drawer
   (play p20-680-drawer.png). Better: the drawer opens over the desk edge without resizing the page grid. (Play 11 +
   Craft 8, general)
6. **Empty page says nothing.** After clearing, the "Type a line." hint never returns and Play and Rhymes answer only
   in the live region (play p14-empty). Bring the hint back whenever the page is empty. (play 13, general)
7. **Marks just appear.** Only `@keyframes drawer-in` exists (src.html:128); the spec's "marks drop in above it" and
   Done when 7 ("Motion off removes the typebar ... animations") assume one. Add a short drop of a finished word's
   marks, removed by `.calm`. (craft 7, family:curiosity)
8. **Sounds gives no readout when it finds nothing.** On the Frost line Sounds lights and nothing changes (audit
   `state-sound-repeats-1366x768.png`). Add a top-strip readout ("repeats: 0 consonant, 0 vowel"). (craft 10, general)
9. **Provenance wording.** src.html:536 "YOUR PAGE / stays on this device only when saved" reads as if unsaved text
   leaves. Use "YOUR PAGE / not saved" (Drafts already states privacy). (Play 15 + Craft 11, nit, general)
10. **Doubled tempo control.** src.html:221-223: the knob (`role=slider`, tabindex 0) and the range input are two
    sliders for one value. Keep one in the tab order and accessibility tree; hide the other. (craft 12, nit, general)
11. **Drawer kind buttons mix roles.** src.html:253-255 set `aria-selected` and `aria-pressed` on `role="tab"`. Drop
    `aria-pressed`. (craft 13, nit, general)

#### Settled calls

- **No shelf poem needs a sensitivity review** (Cory, 2026-11-05, spec open questions). Not re-raised. The only
  sensitivity routing here is Blocker 1's filter list.
- **here/near level:** Teaching rated it a blocker, Play a should fix. Blocker: it is a readout that misleads on the
  default poem and Done when 5 fails (REFINE, "a meter or estimate that misleads").
- **Fractional feet:** both lenses; Teaching blocker, Play should fix. Blocker for the same REFINE rule. Tag
  family:curiosity (it comes from this engine's naming).
- **Sounds overlay and secondary stress:** Teaching should fix, Play polish. Should fix: Things to do 1, 8 and 9 rest
  on them.
- **Read without a clip:** the missing smooth-narrator clip is correct until the collective Forge pass (BASELINE
  rule 18). Do not record or synthesize one; fix only what Read shows and says.
- **The "N of M" readout stays a readout.** Polish 1 refines what it counts; it is not a score and gets no goal,
  colour verdict or praise. Nothing on the list adds a goal, score, level or finish (CODEX-CURIOSITY).
- **Rhyme drawer keeps the spec's syllable grouping** (should fix 14 orders inside it, not across it).
- **SCOWL common-words sort:** already built ("Common words first. Names included." in the drawer); the spec's open
  question is answered by the build. The filter check in Blocker 1 uses that tier.
- **Audit leads that are by design, do not change:** `#editor`/`#hint` overlap, editor focus on load (uses
  `preventScroll`), hint out of view after the first action, Manual and Drafts over the editor (modal dialogs), tempo
  knob "nothing changed" on a plain click (drag and arrows turn it), Print "nothing changed" (headless print dialog),
  shelf books "off screen" and Sympathy "covered" (a scroll list).

#### To the spec's open questions

- **RL.7.4's word-meaning half (figurative and connotative language) is taught by no built tool** on
  ela-7-sound-and-form-in-poetry; Poetry Soundboard, the module's lesson card, is still a concept. Rule 2: decide
  whether Poetry Soundboard carries it or the code half moves; log it for the module, not for this Curiosity.
- **Auto meter default:** whether Auto should judge every line against the poem's best foot by default and show a
  line's own closest foot only where it really differs (Teaching S1). Should fix 8 does the in-spec part (ties, poem
  meter in the strip); the default change alters the spec's scansion rule.

#### Not taken

- Shelf at 1366x768 with six books below the fold (play 14, nit): it is a labelled scroll list ("THE SHELF / 16");
  smaller spines would cost legibility.
- Hughes "Dark like me" / "Black like me" with "me" marked weak (teaching, Sensitivity): the student can flip it, the
  function-word rule is the spec's, and no shelf review is wanted (Cory, 2026-11-05).
- Separate "hash the block list" option (craft 9): taken into Blocker 1 as dropping the words at pack time instead.

<!-- end part -->

<!-- part: refine/craft.md -->

### Craft lens: poets-workbench (Curiosity No. 10), round 1

Cold Craft lens, 2026-11-05. Judged against REFINE.md (Craft), STANDARDS.md, BASELINE.md and CODEX-CURIOSITY.md
(the look rules). Bundle `tools/poets-workbench/poets-workbench.html` as built (1,603,263 bytes). Own frames in
`S:/CurioClass-codex-scratch/poets-workbench/craft/frames/`; throttle script and shot lists beside them.

Counts: blocker 1, should fix 5, polish 4, nit 3.

#### Findings

##### 1. Rhyme drawer offers slurs as rhymes for everyday words (blocker, general)
- Where: `src.html:287-290` (`BLOCKED`), `rhymeList` at `src.html:581-596`; rhyme drawer, every kind.
- What: the block list covers only the worst words. The CMU dictionary keeps many slurs and explicit words, and
  the drawer shows them as rhymes for words a grade 7 (or a K-2 class on a projector) will tap first:
  "moon" lists coon, coons, spook(s), redskin, douche; "like" and "bike" list dyke, dykes, gook, polack;
  "map" lists jap, japs, crap, rape, wop; "top" lists wop, darkie, nazi; "hit" and "pick" list tit, tits,
  prick, redskin, niggard. "coon" sits 14th in the default Perfect list for "moon", in the common-words tier
  (SCOWL puts it in size 50 and above), so it is on screen without scrolling.
- How seen: `frames/moon-drawer.png` (coon visible in the first rows), `frames/like-drawer.png`; the `words` and
  `rhyme-moon` checks in `s2.json` (72 of 100 test words are in the dictionary; 13 common words each surface
  at least one).
- Better: filter the rhyme index with a real classroom list (slurs, ethnic and sexual terms, explicit words), not
  a hand list of about 70; check "moon", "like", "map", "top", "hit", "late" and "pick" after. Rule 6.
  "redskin", "squaw" style entries are Native slurs: route the final list past the sensitivity agent.

##### 2. Long poems drop well below 60 fps while typing (should fix, family:curiosity)
- Where: `render()` at `src.html:450-522` re-scans every line (four feet, every offset, every variant) and
  rebuilds the whole mirror `innerHTML` 60 ms after each keystroke.
- What: one render of The Raven (126 lines) costs about 20 ms on this desktop and 131 ms at 4x CPU throttle (a
  modest Chromebook); Paul Revere's Ride 92 ms. Typing into a loaded Raven at 4x: 61 of 208 frames over 33 ms,
  p95 122 ms, max 154 ms. Unthrottled it is already 24 of 394 frames over 33 ms (p95 34.5 ms). Frost's one line
  is fine (p95 20 ms). The dictionary load also takes 3.9 s at 4x (319 ms unthrottled); its 9 ms chunks keep
  frames smooth, so that part is fine.
- How seen: `scripts/throttle.py` + `scripts/t.js` (CDP `Emulation.setCPUThrottlingRate` 4) and the `typing`
  shot in `s2.json`.
- Better: cache `scanLine` per line text and lens (the overrides key is per line already) and patch only the
  changed `.verse` node; the shelf exists to load long poems, so this is the path students take.

##### 3. Tapping a stress mark does not flip it; it opens the rhyme drawer (should fix, general)
- Where: `.proof` buttons in `#mirror` (`src.html:84-88`, handler `src.html:928-936`) sit under `#editor`
  (`src.html:75`, later in the DOM, same stacking level; the mirror's `transform` makes its own stacking
  context, so `.proof{z-index:3}` never lifts the marks above the textarea).
- What: `document.elementFromPoint` on the first mark returns `editor`. A real click on the "/" over "woods" put
  the caret in the word and opened the drawer for "woods"; the mark stayed "/". The spec's control ("Tap a stress
  mark"), Things to do 5 and the Manual ("Tap a mark ...") all promise it. The Stress key and Alt F do work.
- How seen: `frames/proofclick-after.png`; `proofclick` shot in `s2.json` (`topEl: editor`, before x, after x,
  drawer true).
- Better: give `#mirror` a z-index above the editor with `pointer-events:none` kept on everything but `.proof`,
  or drop the promise from the Manual and spec.

##### 4. Alliteration underline uses the same green as rhyme family B (should fix, general)
- Where: `.word.allit{border-bottom:2px solid #2d6a3e}` (`src.html:82`) and `COLORS[1]='#2d6a3e'`
  (`src.html:275`) used for `.word.ending` underlines (`src.html:81`).
- What: with Sounds on, the end word of every B line carries a green underline that looks the same as an
  alliteration mark. In The Raven, "lore" (rhyme B) and "quaint", "curious", "forgotten" (alliteration) all
  show a green underline at once. Assonance is shown by colour alone (plum shading), and in long lines it
  shades nearly every word, so the overlay stops meaning anything.
- How seen: `frames/raven-sounds.png`.
- Better: draw alliteration as a distinct mark (a small bracket or dotted overline under the first letter, not an
  underline), keep green out of the rhyme inks, and give assonance a shape as well as a colour.

##### 5. Read is a dead control on screen, and the Manual says otherwise (should fix, family:curiosity)
- Where: `$('read').onclick` at `src.html:1042-1050`; Manual text at `src.html:824-825`.
- What: with no clip (expected until the Forge voice pass, BASELINE rule 18), Read only sets the provenance line
  to the value it already has, changes the button's tooltip and sends "Type a line. The recorded hint is not
  supplied in this build." to the live region. After the first action the hint stays hidden. Nothing visible
  happens. The Manual says "Read shows and announces the hint as text", which is not true, and both the Manual
  and the screen reader text carry a build note a student should never meet.
- How seen: `read-after-typing` shot in `s3.json` (hint hidden before and after Read; `vlog` empty).
- Better: until the clip exists, Read re-shows the hint on the page for a few seconds and announces only
  "Type a line."; drop the "not supplied in this build" wording from Manual, tooltip and live region.

##### 6. Alt R and Alt F do not work on a Mac (should fix, general)
- Where: `src.html:1028-1029` tests `event.key.toLowerCase()==='r'` / `'f'`.
- What: on macOS, Option+R gives `event.key` "®" and Option+F "ƒ", so neither shortcut fires (and the symbol is
  typed into the poem). The footer and the Manual advertise both. Found by reading the code; this PC cannot run
  a Mac keyboard, so not seen on a frame.
- Better: test `event.code==='KeyR'` / `'KeyF'`.

##### 7. Motion has almost nothing to turn off (polish, family:curiosity)
- Where: only `@keyframes drawer-in` exists (`src.html:128`).
- What: the spec's typebar drop ("its marks drop in above it with a soft typebar clack") and Done when 7 ("Motion
  off removes the typebar and drawer animations") assume a mark animation that was not built. Typing gives a
  clack (Sound) but marks just appear. Not wrong, but the first-two-minutes moment is flatter than the spec.
- Better: a short drop of the new word's marks on word end, removed by `.calm`.

##### 8. Click to edit a word reflows the whole desk twice (polish, general)
- Where: `editor` click handler `src.html:919-927` opens the drawer on any click inside a word; `edited()`
  (`src.html:535`) closes it on the next keystroke.
- What: at 1366x768 a click into "woods" moves the page 95 px left and narrows the editor by 50 px (text
  rewraps); typing a letter moves it all back. Fixing a typo costs two layout jumps. The audit's held click on
  the rhyme handle shows the same move (19 of 32 controls shifted).
- How seen: `clickword` shot in `s2.json` (`p0 293, p1 198, w0 848, w1 798`).
- Better: open the drawer over the desk edge without resizing the page grid, or open it on a second tap / the
  mark, not on every caret placement.

##### 9. Slurs sit in plain text in the public bundle (polish, general)
- Where: `src.html:287-290`.
- What: the block list puts the slurs themselves in view-source of a K-12 page and in a public repo. Not on
  screen, so not a rule 6 failure, but easy to avoid.
- Better: ship the filtered dictionary (drop the words at pack time) or store hashes.

##### 10. Sounds gives no readout when it finds nothing (polish, general)
- Where: Sounds key, `render()` `src.html:474-485`.
- What: on the opening Frost line, Sounds lights and nothing on the page changes (no repeats there). A student
  cannot tell an empty result from a dead key.
- How seen: audit `state-sound-repeats-1366x768.png`.
- Better: a readout in the top strip such as "repeats: 0 consonant, 0 vowel".

##### 11. "stays on this device only when saved" reads as if unsaved text leaves it (nit, general)
- Where: `src.html:536`, the provenance line after the first edit.
- Better: "YOUR PAGE / not saved" (the Drafts dialog already says drafts stay on this device).

##### 12. Doubled tempo control for assistive tech (nit, general)
- Where: `src.html:221-223`: the knob (`role=slider`, `tabindex=0`) and the range input are two tab stops and two
  sliders for one value, both inside one `<label>`.
- Better: keep the range input as the one control and mark the knob `aria-hidden`, or the reverse.

##### 13. Drawer kind buttons mix tab and toggle roles (nit, general)
- Where: `src.html:253-255`: `role="tab"` with `aria-selected` and `aria-pressed` together.
- Better: drop `aria-pressed` on the tabs.

#### Checks that passed

- Contract: one file, 1.60 MB (under the 2 MB goal); `performance.getEntriesByType('resource')` empty (no network
  requests); no console errors or exceptions in any of my shots; `check_tools.py` lists it as draft with no
  failure. Manual links open only on a person's click.
- Look rules: fills the screen at every size (audit size frames), no kit header, no welcome, score, goal or
  finish; readouts in Courier with units (lines, words, syllables, BPM, "8 of 8"); maker's plate "Curio Class
  Curiosities · No. 10 · Poet's Workbench" and Manual lower-left; Motion, Sound and Read on their own power panel.
- Access: 44 px desk controls; visible focus ring; dialog returns focus; shelf and rhyme lists use roving
  tabindex with arrows; Escape closes the drawer. Proof marks are 27 px tall but have the 44 px Stress key and
  Alt F as the equivalent (see 3 and 6 for where that equivalence breaks).
- Words: no em dashes in src, notes, lines or the bundle; "Curio Class" never "Curio" alone; privacy stated in
  Drafts ("Your drafts stay on this device.").
- Art: no `art:` tokens and an empty prompts list; the desk is drawn in CSS, as the brief asks.

#### Standard voice check

One line exists, the first-run hint, and its clip is not recorded (deferred to the collective Forge pass, BASELINE
rule 18). `voice/lines.json` and `__tool.allLines()` match word for word: ["Type a line."]. `__tool.vlog` stayed empty
in every run, and the audit's held-click table shows nothing spoken on any control.

| line | kind | expected | spoken |
|---|---|---|---|
| Type a line. | how-to (first-run hint) | once on load, then on Read | 0 (no clip; Read announces text to the live region only) |

Repeats, stale lines, order: nothing to count. First tap: nothing speaks before or after any tap. Read: see 5.
Re-run this check when the Forge clip lands.

#### Frames looked at

Own: `frames/moon-drawer.png`, `like-drawer.png`, `proofclick-after.png`, `raven-sounds.png`,
`raven-lens-iamb.png`, `clickword.png`, `read-after-typing.png`. Audit: `size-1366x768.png`, `size-680x425.png`,
`state-sound-repeats-1366x768.png`, `state-rhymes-375x812.png`.

#### Audit pilot

- Leads confirmed: none as defects. "nothing changed" on Print is `window.print()` in headless Chrome; on the
  tempo knob it is a click that does not turn it (drag and arrows do); on The Owl and the Pussy-cat it was not
  re-checked (other books load fine).
- Leads wrong: `#editor` / `#hint` overlap at every size is by design (the hint is a pointer-events-none note on
  the page). "focus taken on load" is deliberate for a typing instrument and uses `preventScroll`. "hint out of
  view" in stress-key, playing-fast and rhymes is the hint correctly gone after the first action. Manual and
  drafts "text hidden under" rows are a modal dialog over the page. Sympathy "covered" and four books "off screen"
  are the shelf's scroll list.
- Missed: the slurs in the rhyme drawer (1), frame times on long poems (2), the stress marks being unclickable
  under the textarea (3: the audit clicks only listed controls, and the marks are `tabindex=-1` inside an
  `aria-hidden` mirror), the green clash (4), Read doing nothing visible (5; the audit row says "ok"), and the Mac
  shortcuts (6).
- Sensitivity: the slur filter (1) touches Native, ethnic and LGBTQ terms; the shelf content notes in notes.md
  (death, war, Hughes) are for the sensitivity agent, not judged here.

<!-- end part -->

<!-- part: refine/play.md -->

### Play lens: poets-workbench (Curiosity No. 10), round 1

Judged against docs/agents/CODEX-CURIOSITY.md and the VISION "Curiosities: the second shape" section, not lesson norms.
Played twice: as a grade 7 student alone at home, and as a teacher projecting at 1920x1080. Frames are in
`S:/CurioClass-codex-scratch/poets-workbench/play/` (p*, q*, r*) unless they name the shared audit folder
`S:/CurioClass-codex-scratch/poets-workbench/audit-r1/`. Driven with `scripts/drive.py` (port 9451), real held clicks.

#### Short test

- **Would a kid open it unassigned?** Yes, a word-loving one: a typewriter that marks the beat of whatever you type
  and finds rhymes on a tap is a real pull. The friction below (Play silent on open, rhymes buried under surnames,
  here/near not rhyming) is what would make a kid close it in the first two minutes.
- **Would an adult play for fun?** Yes. The whole CMU dictionary, live scansion, pronunciation variants and 16 real
  poems make it a desk a working poet could use. Stepping "record" and watching the marks move is a good moment.
- **Is the real thing the interface?** Yes. The page, the proof marks and the margins are the instrument; there is
  no wrapper (audit-r1/size-1366x768.png, p19-1920-raven.png).
- **No score, no finish line?** Passes. No goal, score, level, quiz or finish screen; a lesson-creep grep of src.html
  for score, points, level, goal, sticker, badge, correct, wrong, try again, complete and well done finds nothing.

The short test passes. The findings are about the first two minutes and about readouts that look broken.

#### Findings

1. **should fix · general · default screen, Play.** On open the caret sits on the empty line below the Frost line,
   so the big red Play key (the most inviting control on the desk) does nothing visible: it only sends "This line is
   silent. Type a word to tap its beats." to the screen-reader live region. Seen: q05-play-mid.png, page unchanged
   1.7 s after a held click, `playing:false`. With the caret on line 1 it works well (r01-play-line1.png). Better:
   on an empty line, Play taps the nearest line above (or the poem), so the first press always makes sound and light.

2. **should fix · family:curiosity · paper guides (Haiku, Limerick, Common, Sonnet).** The faint guide number or
   letter is drawn on top of the syllable count in the left margin, so the one comparison the paper exists for (your
   5 against the guide's 5, your 8 against a 6) is an unreadable smudge. Seen: q06-zoom-margin.png (haiku),
   q07-zoom-margin.png (limerick letters over counts), r05-sonnet-paper.png. The audit's overlap check missed it.
   Better: put the guide beside the count ("5 / 5") or in its own column.

3. **should fix · family:curiosity · paper guides count blank lines.** `guideFor(li)` (src.html:430) uses the raw
   line index, so a stanza break takes a guide slot. Sonnet 18 on sonnet paper puts the guide "C" on the blank line
   after the first quatrain and every later letter is off by one (r05-sonnet-paper.png, the lone "C" at y 662).
   Common meter on Dickinson's stanzas would shift 8, 6, 8, 6 to 6, 8, 6, 8 after the first break. Better: count
   only lines with words (and for haiku and limerick, restart at each stanza).

4. **should fix · family:curiosity · rhyme letters, "here" and "near".** CMU writes here as IY R and near, year,
   clear, fear, dear, queer as IH R, so the most common rhyme sound in English songwriting is split. A student's own
   couplet "standing here / have you near / sky is clear / another year" reads ABBB (q09, scheme readout); Frost, the
   opening poem, reads AABA CCDC DDED EEEE instead of its famous chain. The Manual is honest about Frost, but a kid
   writing their own poem sees the margin say their rhyme is not one. Only 31 CMU words end IY1 R against 192 for
   IH1 R (checked in `_scratch/poets-workbench/cmudict.dict`). Better: fold IY R into IH R for rhyme keys (a stated
   normalisation, like primary and secondary stress), and say so in the Manual. Teaching may rate this higher under
   REFINE's "a readout that misleads when its assumption doesn't hold".

5. **should fix · family:curiosity · words with two one-syllable pronunciations.** For a one-syllable word, Stress
   and Alt F only flip the stress; they never step to the word's other pronunciation (src.html:613-614). So tears
   (T EH1 R Z and T IH1 R Z), wind, read, lead, live, bow and close can never be corrected, and the rhyme letter
   uses whichever variant fit the meter first. Invictus, chosen because it "reads cleanly", reads ABAB CDCE FGHG IBIB
   (tears/years split, and unbowed takes B OW1 D, not aloud's AW). Flipping "tears" left the scheme unchanged
   (q04-invictus-tears). Better: step one-syllable words with several pronunciations through them too, and let the
   end-word variant prefer one that rhymes with a nearby line end.

6. **should fix · general · rhyme drawer, Replace word on by default.** The spec's first reaction is "tap hot ... tap
   spot and it can be dropped into the page". With Replace on, tapping spot turns "I like to eat my pizza hot" into
   "I like to eat my pizza spot" (q03-insert-spot). A rhyming dictionary is opened to find a word for another line;
   replacing the word you rhymed against is rarely wanted. Better: default to inserting at the caret as it was before
   the tap (or at the end of the next line), with Replace as the option.

7. **should fix · family:curiosity · rhyme drawer order.** Groups sort by syllable count first, so the one-syllable
   group of "hot" holds 154 entries and turns to surnames by the fifth row: baht, bhatt, bott, brott, clott, cott
   (q02-click-hot.png); "think" reaches cinq, cinque, finck, fincke, hinck within five rows (p13-midline-click.png).
   "forgot" and "apricot" from the spec's first two minutes sit below about 150 names. Better: show the SCOWL tier
   across all syllable groups first, then a single "Names and rare words" fold.

8. **should fix · general · meter names with fractional feet.** The line-end readout says "anapestic 2.7 feet" for
   every classic limerick line, "trochaic 2.5 feet" on haiku, "iambic 3.5 feet" for "I will record a record", and
   "trochaic 39.0 feet" for a long line (p08, q07-limerick-frame.png, p04, p15). It looks like a bug to a student and
   is not how a poet names a line ("anapestic trimeter, missing its first syllable", or "catalectic"). Even with the
   Anapest lens on, the limerick stays "2.7 feet". Better: round to whole feet and name the missing or extra
   syllables.

9. **should fix · general · Read key.** Read makes no sound and changes nothing on screen; it only puts "Type a line.
   The recorded hint is not supplied in this build." in the live region and the button title (p17-read-press,
   `vlog: []`, hint stays hidden). The Manual also says "The smooth-narrator hint recording has not been supplied in
   this build". That is maker talk on a student's desk. The clip waiting for the Forge is fine (BASELINE rule 18);
   until then Read should at least show the hint again on the page, and the build note belongs in notes.md, not in
   the Manual or a tooltip.

10. **polish · family:curiosity · Sounds key.** Assonance shades every word whose stressed vowel repeats anywhere in
    the line in one plum, over the whole 78 px word box including its marks. On The Raven 408 words are shaded and the
    page becomes a wall of purple (p06-raven-sounds.png); on "Peter Piper" you cannot tell the IH pair from the EH pair
    (q08-sounds-simple.png). Function words alliterate ("The ... the"). The alliteration underline sits low enough to
    strike through the meter note below. Better: one ink per repeated vowel (dreary/weary share one, napping/tapping/
    rapping another), skip function words, and keep shading to the text height. That would also make the spec's
    "find the rhymes hiding inside The Raven's lines" possible to see.

11. **polish · general · tap to place the caret opens the drawer.** Any click inside a word opens the rhyme drawer and
    narrows the page 50 px (848 to 798, p13-midline-click.png), so lines re-wrap; the first keystroke closes it and
    they re-wrap back. Revising mid-line by mouse makes the page jump twice each time. At 680x425 the tapped word
    "hot" wraps under the drawer to a row that is cut off (p20-680-drawer.png). Better: keep the page width when the
    drawer opens (it is already a fixed overlay at 1366), or open rhymes on a tap of the end word / double-click.

12. **polish · general · secondary stress always strong.** Names a student types for "Type your name" read oddly:
    Cory (K AO1 R IY2) marks "/ /", Aaliyah "/ / /" (p05). "midnight" in The Raven's first line costs a match
    (15 of 16). Better: treat secondary stress as flexible, like the free function words, so it follows the meter.

13. **polish · general · empty page.** Clear the page and nothing says what to do: the "Type a line." hint never
    returns, and Play and Rhymes only answer in the live region (p14-empty). Better: bring the hint back whenever the
    page is empty.

14. **nit · general · the shelf at 1366x768.** Six of sixteen books (Sympathy onward, including Jabberwocky and
    Invictus) are below the fold of a thin-scrollbar list, with only a sliver of the seventh showing
    (audit-r1/size-1366x768.png; books scrollHeight 899 vs 557). The "THE SHELF / 16" label helps. Smaller spines would
    fit all sixteen.

15. **nit · general · provenance wording.** After typing, the source line reads "YOUR PAGE / stays on this device only
    when saved", which reads as if the page leaves the device otherwise. "YOUR PAGE / not saved" or "YOUR PAGE / save
    in Drafts" says it plainly.

Checked and fine: the opening Frost line reads 8 and iambic tetrameter; typing "I like to eat my pizza hot" scans
x / x / x / x / and iambic tetrameter 8 of 8 (q01); "I will record a record" gives verb then noun stress (p04), and
stepping record moves the marks (r03); orange shows 0 perfect rhymes and slant lists (p03); Dickinson reads
8, 6, 8, 6 (p10); Jabberwocky's invented words carry the dotted underline (p09); The Raven's internal-rhyme lines
scan trochaic octameter 15 of 16 (p06); Play highlights each beat and Stop works (r01); drafts save with the
on-device note (r04); Motion off removes the drawer animation (q13); the dictionary is ready in about 0.3 s, and
re-scanning The Raven on a keystroke takes about 24 ms here (r02); the 680x425 preview is readable and inviting
(audit-r1/size-680x425.png); the 375 iframe and 1920 frames hold. No em dashes in src.html. Nothing cultural,
Native or hard-history needs a sensitivity flag from this lens beyond what notes.md already lists for the shelf.

#### Counts

blocker 0 · should fix 9 · polish 4 · nit 2

#### Audit pilot

- **Leads confirmed:** shelf books "off screen at load" at 1366x768 (finding 14; it is a scroll list, so not broken);
  Sympathy "covered at its centre" is the same scroll edge.
- **Leads wrong:** #editor / #hint overlap at every size (the hint is drawn on the page on purpose); "hint out of view"
  in the states (the hint hides after the first action by design); Manual and Drafts covering the editor (they are
  modal dialogs); Print "nothing changed" (headless print); tempo knob "nothing changed" (a click without a drag does
  not turn it, which is right; the arrow keys and drag work); "focus taken on load" (the editor taking focus is the
  right first state for a typewriter).
- **What it missed:** the guide-over-count overlap in the margins (finding 2), Play silent on the default screen
  (finding 1, the audit clicked Play with no check of sound or light), Read changing nothing visible (it scored "ok"),
  the guide shift on stanza breaks, and every readout question (here/near, tears, fractional feet), which it cannot
  see by design.

<!-- end part -->

<!-- part: refine/teaching.md -->

### Teaching lens: poets-workbench (Curiosity No. 10), round 1

Cold lens. I read the spec, src.html, notes.md, art/prompts.json, voice/lines.json, audit-states.json, the
CODEX-CURIOSITY brief, VISION "Curiosities: the second shape" and the shared audit (audit-r1). I did not read
the codex reports. I drove the bundle myself (drive.py, port 9441). My frames and data are in
`S:/CurioClass-codex-scratch/poets-workbench/teaching/`: `frames/t-*.png`, `facts-out.json` (Done-when checks,
rhyme lists, sample scansions) and `meters-out.json` (meter names and unknown words for all 16 shelf poems,
529 lines).

Counts: blockers 3, should fix 7, polish 3, nit 1.

#### Blockers

**B1. "here" and "hear" do not rhyme with "near", "year", "fear": the Frost rhyme scheme and the rhyme drawer are
wrong.** (rhyme index, `pronunciation()` src.html:322; Frost on the shelf; Done when 5)
CMU lists `here`, `hear`, `ear`, `tier`, `we're` as `IY1 R` but `near`, `year`, `fear`, `dear`, `clear`, `queer`
as `IH1 R` (checked in `_scratch/poets-workbench/cmudict.dict`: 31 entries end `IY1 R`, 192 end `IH1 R`). In
American English these are the same sound before R. That is an inconsistency in the dictionary, not a real
difference. The tool treats it as real:
- Stopping by Woods, the default poem, shows `AABA CCDC DDED EEEE`, not the AABA BBCB CCDC DDDD in Done when 5
  (frame `t-frost.png`; "here" gets B, "queer/near/year" get C).
- The drawer for "hear" lists 34 perfect rhymes. Most are surnames (baehr, grier, keir, speare, teare, keneer,
  manteer) and fear, near, dear, year, clear are missing (frame `t-hear.png`).
- The Manual explains the split as "strict" dictionary hearing (src.html:840). That tells students two words they
  say the same way sound different.
It is a readout that lies, on the first poem and on some of the most common rhyme words in English.
Fix: treat `IY R` as `IH R` when building the rhyme keys, and check the other pre-R vowel pairs CMU mixes the same
way. Then Frost reads AABA BBCB CCDC DDDD, Done when 5 passes and the Manual note can go.
Tag family:curiosity.

**B2. Meter names with fractions of a foot: 227 of 529 shelf lines read "3.5 feet", "2.7 feet", "3.3 feet".**
(`scanLine` src.html:405-407)
`lengthName` divides syllables by foot size, so any line that doesn't divide evenly gets a decimal. 85 lines get
thirds ("anapestic 3.3 feet", "dactylic 2.7 feet"), which isn't a measure anyone uses. The textbook examples are hit
hardest:
- The Tiger: 12 of 24 lines say "trochaic 3.5 feet". It's the standard example of trochaic tetrameter with the last
  syllable dropped.
- The Raven: 42 lines "trochaic 7.5 feet" and 17 refrains "3.5 feet". Poe himself called these octameter and
  tetrameter with a missing syllable.
- Invictus, chosen because it "reads cleanly": "anapestic 2.7 feet" and "dactylic 2.7 feet" (`meters-out.json`).
A grade 7 student learns that meter comes in fractions. Under the brief that is a meter that misleads when its
assumption doesn't hold.
Fix: name the length from the number of stressed beats or whole feet. Say what's left over in words, such as
"trochaic tetrameter, last syllable dropped" or "iambic tetrameter + 1 extra". Never print a decimal.
Tag family:curiosity.

**B3. The rhyme-scheme strip runs two-letter labels together, so long poems show a false scheme.**
(`render()` src.html:469, letters from src.html:424)
After Z the letters become AA, AB, and so on, but the strip joins them with no gap. The Raven's last stanzas read
`AABABBBB AABACBBB ADBJBBB AEBAFBBB`. That looks like 8- and 7-line stanzas in a poem whose stanzas are all 6 lines.
Paul Revere's Ride has the same problem. Confirmed on `t-raven-end.png` (labels AD, AE, AF in the margin, from
`meters-out.json`).
Fix: separate the letters in each stanza group (A·B·AB) or start the letters again where the reader needs them.
Show the margin letter and the strip the same way. This is a narrow fix, but the readout is false as it stands.
Tag family:curiosity.

#### Should fix

**S1. In Auto, a poem's meter name changes from line to line.** (`scanLine` per line, src.html:361)
Every line takes its own closest foot. The Road Not Taken, an iambic tetrameter poem, names 9 different meters in
20 lines, and "dactylic trimeter" (6 lines) beats "iambic tetrameter" (4) (`t-road.png`, `meters-out.json`).
Ozymandias puts 4 of 14 lines in "dactylic 3.3 feet". The Meter lens dial fixes this, but a student never learns
that from the screen. When a poem is loaded or has 3 or more lines, judge each line against the poem's best foot
by default and show the line's own closest foot only where it really differs. "Poets vary meter on purpose" is
then something the student can see.
Tag family:curiosity.

**S2. Common words outside the dictionary get stress on the first syllable, which breaks shelf lines.**
(`variants()` src.html:339-347)
The guess always stresses syllable 1. "unconquerable" (Invictus) comes out /xxxx, and the line falls to
"anapestic 2.7 feet". Many of the shelf's unknown words are made of known parts: hyphenated compounds (pea-green,
five-pound, high-born, hoof-beats, to-night, farm-yard, belfry-tower), possessives (bosom's, demon's, cushion's,
sentinel's, belfry's) and old -'d endings (mock'd, stamp'd, dimm'd, untrimm'd). Paul Revere's Ride has 21. Look up
the hyphenated parts separately, drop the 's, and read -'d as the -ed word minus a syllable. Real coinages like
brillig can stay as guesses.
Tag family:curiosity.

**S3. Names come out stressed on both syllables, which hurts Things to do item 1, "type your name".**
CMU gives many names a secondary stress on the final vowel (`cory K AO1 R IY2`, `kylie ... IY2`,
`aiden EY2 D EH1 N`, `jeremy ... IY2`; 552 entries end in `IY2`). The tool counts secondary stress as strong, so
"Cory", "Kylie" and "Aiden" each show `/ /` (`t-name.png`). A student testing the tool's first suggestion gets a
wrong answer about their own name. Count a word-final `IY2` in a two-syllable word as weak, or draw secondary
stress as a half mark.
Tag family:curiosity.

**S4. The pronunciation readout has no key.** (drawer head `#phones`, src.html:603; Manual)
The drawer shows "HH IY1 R" and "R EH1 K ER0 D · / x · 2/3". The Manual never says what the letters stand for,
what the digits 0, 1 and 2 mean, or what "2/3" counts (I grepped the Manual for any key to these symbols). The
Manual's own facts lean on the symbols too ("tea has IY, obey has EY"). Add a short key: digits mean stress
(1 main, 2 second, 0 none), a small table of the vowel symbols with example words, and "2/3 = pronunciation 2 of
3". Label the "2/3" on screen.
Tag family:curiosity.

**S5. The Sounds key shades nearly every word, so the Raven's inner rhymes can't be found.** (src.html:474-485;
Things to do 8)
The assonance shading counts the stressed vowels of free function words too, and uses one colour for every
repeated vowel. In the Raven's first lines almost every word is shaded, and dreary/weary or napping/tapping look the
same as "upon", "of" and "volume" (`t-sounds-raven.png`). RL.7.4's sound work ("analyze the impact of rhymes and
other repetitions of sounds") needs the student to see which sounds repeat. Leave free syllables out, give each
repeated vowel its own ink, and mark rhymes inside a line (same perfect-rhyme key) separately. The spec's "find
the rhymes hiding inside its lines" then becomes something the tool can show.
Tag family:curiosity.

**S6. RL.7.5's "form contributes to meaning" is shown but not linked to meaning, and RL.7.4's word-meaning half
isn't exercised.** (module ela-7-sound-and-form-in-poetry: RL.7.4, RL.7.5)
The student can see form: rhyme scheme, stanza breaks, line lengths, sonnet paper. Nothing on the desk or in the
Manual connects a form to what the poem means. "Its final two lines repeat" (src.html:839) stops short of saying
why. The cheapest fix inside the Curiosity shape is a few "Things people have found" entries that join the two,
plus one form question in notes "Talk together":
- Frost's repeated last line;
- the short "In Flanders fields." refrain line;
- Sonnet 18's closing couplet turning to "So long lives this";
- "Nevermore" ending every Raven stanza.
RL.7.4's figurative and connotative word-meaning half isn't touched anywhere. That suits a second card, but
Poetry Soundboard, the module's lesson card, is still only a concept. The integrator should make sure notes.md
"What it teaches" says "the sound half of RL.7.4", and should log that the module's word-meaning half has no
built tool yet (rule 2).
Tag general.

**S7. The source texts have stray marks left from the dash clean-up.** (material.json poems)
- The Raven, line 26: "here I opened wide the door:," (the original has a semicolon and a dash).
- Annabel Lee, line 37: "Of the beautiful ANNABEL LEE:,".
Turning a dash into a comma after a colon left ":," in a public-domain text the Manual calls checked. Use one mark.
Tag family:curiosity.

#### Polish

**P1. The "N of M" match count counts free syllables as matches.** (src.html:408)
Free one-syllable function words always take the expected mark, so they always "match". "I hear the rain" reads
4 of 4, and a line of nothing but function words would score full marks. Better: "6 of 6 fixed · 2 free", or count
only fixed syllables.

**P2. The Manual's wording is above grade 7.** Examples: "The lens compares a foot at each starting offset",
"Primary and secondary stresses both count as strong", "rather than a universal account of speech",
"free one-syllable words follow the nearest pattern" (src.html:804-836). Better is plain sentences with an example
word each, such as "Small words like *the* and *of* can go either way, so they're grey and take whatever beat
fits."

**P3. Content notes sit under a builder-style heading.** notes.md lists the shelf's sensitive content (death, grief,
war, religious imagery, Hughes) under "Review care points", mixed in with layout notes ("44-pixel Stress key"). Rule
8 is met, but a teacher would look for a "Content notes" line in Good to know (BASELINE, parent-preview call). Move
it there and drop the build notes.

#### Nit

**N1. Unlabelled pronunciation index, and rhymes that only match an unstressed form.** The "1/1" at the end of the
drawer readout has no label (see S4). Also, "the" (`DH IY0`) appears high in "tea"'s perfect rhymes and "a" in
"obey"'s, because a word with no stressed vowel falls back to its first vowel. Leave unstressed-only forms out of
perfect rhymes.

#### Done when (teaching view)

1. Frost scanned on open, scans as you type: PASS (`t-frost.png`, `t-name.png`).
2. 8 syllables, iambic tetrameter: PASS (`facts-out.json`: 8, "iambic tetrameter", 8 of 8).
3. "orange" 0 perfect plus slant lists; "hot" shows lot, not, spot: PASS (orange: 0 perfect, Same vowel and Same
   ending filled; hot: 154 perfect including lot, not, spot, forgot).
4. "record" steps through 3 pronunciations: PASS (3 variants; "I will record a record" scans x/ then /x,
   `t-record.png`).
5. Dickinson 8, 6, 8, 6: PASS. Frost AABA BBCB CCDC DDDD: **FAIL** (shows AABA CCDC DDED EEEE; see B1).
6. Jabberwocky's invented words are dotted, with guessed counts: PASS (25 unknown words, all coinages).
7 to 10: Play and Craft lenses. 11: no score, goal, level or finish in the code or on screen: PASS from this lens.

#### Facts spot-checked against a second source

1. The Rape of the Lock pairs obey/Tea (Canto III) and away/Tea (Canto I): confirmed in the Gutenberg 9800 text.
2. Gutenberg 1568 is Henley's *Poems* (holds Invictus): confirmed on gutenberg.org.
3. Gutenberg 74745 is Hughes, *The Weary Blues*, Knopf 1926 (so public domain in the US): confirmed.
4. Gutenberg 29345 is Frost, *Mountain Interval* (The Road Not Taken): confirmed.
5. Record has 3 CMU pronunciations, 2 with the beat second and 1 with it first: confirmed in cmudict.dict.
6. "ourselves" has 2- and 3-syllable forms: confirmed (`AA0 R S EH1 L V Z`, `AW0 ER0 S EH1 L V Z`).
7. Orange and month have 0 perfect rhymes: confirmed in the tool, and no `AO1 R AH0 N JH` or `AH1 N TH` match was
   found.
8. Stopping by Woods text, and its conventional AABA BBCB CCDC DDDD with a repeated last line: matches the 1923
   text.
9. Invictus text matches the standard text word for word ("Finds, and shall find, me unafraid"; "how strait the
   gate").
10. In Flanders Fields and Sympathy texts match the standard texts. Dickinson's 1890 text has 5 stanzas without
    "Or rather, he passed us", as the Manual says ("differs from modern editions").
11. Poe on The Raven: trochaic, octameter lines with a syllable dropped, ending on a shorter line. The Manual's
    summary is accurate.
Errors found: only B1's explanation and S7's two stray marks.

#### Sensitivity

The shelf has death, grief, war (In Flanders Fields), Hughes's "Dream Variations" (Black identity) and Dunbar's
"Sympathy". Cory settled on 2026-11-05 that no poem on the shelf needs a sensitivity review (spec, Open
questions). I flag them as the brief asks but don't judge them. One thing for whoever looks: the function-word rule
marks "me" weak in Hughes's closing "Dark like me" / "Black like me", the poem's key word. The student can flip it,
but the default reading undersells it.

#### Audit pilot

- Leads confirmed: the shelf's last books (Paul Revere, Flanders, Jabberwocky, Invictus) are below the fold at
  1366x768 (`t-frost.png`). That's a layout matter for Play and Craft.
- Leads that are wrong or expected: the #editor / #hint overlap and focus on load are intended (the hint sits on
  the page and the caret waits on the empty line). "Beat tempo knob: nothing changed" is expected, because a plain
  click doesn't turn it (keys and drag do). "Print: nothing changed" is the print dialog in headless Chrome.
- Missed (outside what it can see): B1 to B3, S1 to S7. All are about what the readouts teach. Its clean rows
  ("nothing runs forever", no exceptions on resize) hold for the frames I took.

<!-- end part -->

## Fix

<!-- part: polish.md -->

### Polish: poets-workbench (Codex fix, round 1)

Curiosity No. 10. Cwd verified as `S:\CurioClass-codex`. Only this tool and its Scratch folder were written; no commits; `refine.md` and `refine/` were not edited.
Evidence paths below are relative to `_scratch/poets-workbench/`. Browser checks use `scripts/drive.py` through `fix_run.py`, Chrome 9910, host 8715; the final audit uses 9911.

#### Blocker

1. FIXED. Pack-time classroom exclusions replace the public runtime list and filter CMU and SCOWL together. Baseline `before-numbers.json` reproduces the required everyday queries; `fix-before/before-drawer.png` shows the original moon list. Final: 367 excluded entries absent, 125,571 words and 44,286 common entries remain; all 132,858 lists for 44,286 queries pass with zero forbidden hits (`fix-filter-check.json`). The scoped fresh-agent sensitivity review is PASS (`fix-filter-sensitivity.md`). Exact exclusions and policy are in Scratch; notes.md contains the check output and gzip/base64 final list, avoiding a plaintext public slur list. Ordinary-name and neutral-identity probes pass.
2. FIXED. IY R folds into IH R in rhyme keys; original phones remain visible. Baseline Frost `AABA CCDC DDED EEEE` and couplet `ABBB` become `AABA BBCB CCDC DDDD` and `AAAA` (`before-numbers.json`, `after-numbers.json`, `final-verified-checks.json`). Other pre-R alternate pairs were inspected and retained as accent-sensitive, rather than indiscriminately merged (`fix-facts.json`). The misleading strict-dictionary explanation is removed.
3. FIXED. Meter length uses whole feet and explicit missing/extra syllable wording. Baseline has 227 decimal-foot shelf labels; final has zero across every shelf line (`before-numbers.json`, `final-verified-checks.json`). Examples include trochaic octameter, last syllable dropped. No fractional readout remains.
4. FIXED. When any family label has two letters, every stanza separates its labels with middle dots. The Raven's last four groups each contain six distinct labels, for example `AA·B·AB·B·B·B`; margin labels use the same family names (`final-verified-checks.json`; before/after Raven frames at 1366x768).

#### Should fix

1. FIXED. The mirror has an explicit higher stacking layer, with pointer events enabled only on proof marks. Baseline hit testing returned editor. A held real click changes woods from strong to weak and leaves rhymes closed at 1366x768 (`after-proof.json`, `fix-after/after-proof.png`) and 680x425 (`final-proof-small.json`, `fix-retry/final-proof-small.png`).
2. FIXED. Read restores Type a line visibly in the page margin, announces exactly that hint and drops public build-note wording. Baseline hidden hint/build-note live message is in `before-numbers.json`. Final evidence is `fix-read-final/final-read.png` and `final-read.json`; no hint/text collision. The missing recording remains intentional under BASELINE 18, without browser fallback.
3. FIXED. On the initially empty caret line Play finds the nearest earlier line with words. Baseline playing false / zero highlights becomes playing true / one highlight (`before-default-play.json`, `after-default-play.json`, matching 1366x768 frames). A wholly empty page shows the hint.
4. FIXED. Line scans cache text, lens, line identity, end-reading choice and overrides. Unchanged verse nodes stay in place. Raven typing at 4x CPU throttle: frame p95 133.4 ms before, 16.8 ms after; final 456 frames, 16 over 33 ms, maximum 33.5 ms (`before-performance.json`, `final-performance.json`). The independent unchanged-node assertion passes (`final-verified-checks.json`). One initial test incorrectly expected the caret's old line to remain unchanged despite its meter note disappearing; the corrected test follows an actually unchanged verse.
5. FIXED. Single-syllable words cycle all readings, then weak stress; explicit choices persist. Tears, wind, read, lead, live, bow and close each visit both readings and weak stress (`final-verified-checks.json`). End words prefer a nearby rhyme when no user choice overrides it; Invictus becomes `ABAB CDCD EFEF GBGB`.
6. FIXED. Secondary stresses are flexible and grey. Cory alone becomes strong/weak with its second mark flexible; all tested names' secondary marks are flexible (`after-numbers.json`, `final-verified-checks.json`). The Manual explains this estimate rather than declaring one pronunciation universal.
7. FIXED. Known hyphenated parts, possessives and contracted -'d use constituent sounds; some un-/-able forms derive from known roots. All eleven named ordinary examples are no longer spelling-unknown, while brillig remains dotted (`before-numbers.json`, `final-verified-checks.json`). Word-building estimates are named in the Manual.
8. FIXED within the settled scope. Auto still chooses each line's closest foot; ties favour the poem's most common foot and a mostly readout gives the most frequent meter name. A two-trochaic-lines plus all-flexible-line test reads trochee/trochee/trochee (`final-verified-checks.json`). Road's mostly dactylic estimate remains possible under the specified closest-line rule; forcing all lines to the poem's foot remains the explicitly deferred spec question.
9. FIXED. Function words are excluded from repeats; vowel families have distinct inks and shapes at text height; internal perfect-key pairs have dashed ovals. Raven changed from 408 shaded words / zero internal-rhyme marks to 265 shaded / 103 internal-rhyme marks, with zero function words marked (`before-numbers.json`, `final-verified-checks.json`, matching Raven frames).
10. FIXED. Alliteration is a dotted first-letter bracket, separate from coloured end-rhyme underlines. Assonance has explicit shapes as well as colour, and its wash is only 22 px tall (`final-verified-checks.json`, `fix-after/after-raven.png`).
11. FIXED. Numeric paper guides sit below the actual count; form letters have a separate right-margin row. Five paper frames at 1366x768 show distinct entries; `fix-extra/final-phone-guide.png` and `final-phone-guide.json` prove the phone guide stays within the margin. No glyph overprinting remains.
12. FIXED. Guides count nonempty lines. Sonnet letters are `ABABCDCDEFEFGG` across stanza breaks; haiku after a blank line restarts 5/7/5 (`final-verified-checks.json`). Common-meter/Dickinson frame is `fix-extra/final-common-guide.png`.
13. FIXED. Replace starts off; insertion remembers the caret before the word tap and adds word spacing. The test inserts spot after hot, yielding `I like to eat my pizza hot spot`, preserving hot (`final-verified-checks.json`); Replace remains an explicit option.
14. FIXED. Common words, grouped by syllables, precede one closed Names and rare words fold. For hot, forgot is common index 24 and apricot 47, ahead of that fold (`final-verified-checks.json`); the drawer remains syllable-grouped inside each tier.
15. FIXED. The drawer labels pronunciation N of M, and the Manual explains stress digits with a 15-vowel example table. All example words are checked against staged CMU; symbol meanings are independently cross-checked against Yuanming Shi, University of Georgia MS thesis (2019), Appendix Table A.1, via its indexed source excerpt (https://www.ai.uga.edu/sites/default/files/inline-files/theses/shi_yuanming_201908_ms.pdf). Reference only; no thesis prose/table is bundled. Before bare 1/1 and after labelled readout are in `before-numbers.json` / `after-numbers.json`; `fix-extra/final-manual-key.png` shows the key.
16. FIXED for the specified input mechanism. Option-style key events with key values ® and ƒ and codes KeyR/KeyF were unhandled before and prevented/handled after (`before-numbers.json`, `after-numbers.json`). Shortcuts now use event.code. Physical Mac hardware was unavailable; this is event-level verification, not a Mac-device claim.
17. FIXED. Four original, explicitly labelled One reading entries connect form to meaning: Frost's repeated promise, McCrae's short return, Shakespeare's final couplet and Poe's closed-down answer. Two-source literary checks are in `fix-facts.json`; `fix-extra/final-manual-found.png` shows the entries. Notes names the sound half of RL.7.4 and adds a form question. The desk gets no goals or lesson prompts. Poe's earliest stanza endings are more/evermore, so the note accurately says the more sound, often Nevermore.
18. FIXED. The two source colon-plus-comma remnants are now single colons; baseline two affected texts becomes zero (`before-numbers.json`, `after-numbers.json`, `fix-facts.json`). Gutenberg's primary punctuation is retained; the independent Raven witness uses a semicolon. Existing edition wording is otherwise retained.

#### Polish accepted

1. FIXED. I hear the rain now shows 2 of 2 fixed and 2 free, rather than 4 of 4 (`final-verified-checks.json`). This is an uncoloured readout with no passing threshold or reward.
2. FIXED. Manual prose uses plain examples: little words like the, flexible stress, late starts and missing syllables. The unexplained starting-offset and universal-account phrases are gone. The inspected Manual frames are in fix-extra.
3. FIXED. Shelf content notes are in Good to know; the Review care points builder heading is removed. Packing/audit details have their own named technical sections in notes.md, outside student copy.
4. FIXED. Pronunciations without any stressed vowel have an empty perfect key and never enter the Perfect index. The unstressed the forms pass the runtime assertion (`final-verified-checks.json`).
5. FIXED. The drawer overlays the desk rather than changing its columns or tabs. At 1366x768 the page remains x=293, width=850 before and after opening (`final-verified-checks.json`). Matching 680x425 frames show unchanged page width and an uncovered selected word. The 375x812 word bottom is 416 px and sheet top 422.2 px (`final-phone-drawer.json`).
6. FIXED. Clearing the page restores the hint. The runtime assertion and `fix-after/after-numbers.png` show it, including the visible zero readouts.
7. FIXED. A finished word gains a 160 ms proof-drop animation. The runtime sees one new-mark and proof-drop with Motion on, and animation none with Motion off (`final-verified-checks.json`).
8. FIXED. Sounds reports repeats: 0 consonant, 0 vowel on the Frost line (`final-verified-checks.json`).
9. FIXED. Unsaved edits say YOUR PAGE / not saved (`fix-after/after-drawer.png`).
10. FIXED. The native tempo range is the sole accessible/tabbable slider; the draggable decorative knob is aria-hidden (`final-verified-checks.json`).
11. FIXED. Rhyme tabs use aria-selected without aria-pressed (`final-verified-checks.json`).

#### Settled calls

Applied: no shelf review; only the required filter review. Read waits for the collective Forge clip. Match counts stay readouts, with no goals or grading. Syllable grouping stays inside common and rare tiers. SCOWL stays a browsing order rather than a frequency claim. Deliberate modal overlaps, editable textarea/mirror overlap, initial caret focus, shelf scrolling, knob drag/arrows and Print behaviour are retained. No module edits were made; the RL.7.4 word-meaning coverage question and broader Auto-default question remain for the spec/module owner.

#### Cheats tried

- Function-word-only line: all beats remain flexible; fixed matches are not inflated into a score. I hear the rain separates 2 fixed from 2 free.
- Pronunciation/stress cycling of seven ambiguous words: every listed reading and weak option is reachable; no mode creates a best result or saved score.
- Paper switching and guide patterns across blank lines: these only change faint guides. They never award a pass.
- Every shelf line, including shortened lines and long Raven lines: zero decimal-foot names. The readout explicitly says when syllables are missing or extra.
- Rhyme safety: all variants and all three list kinds for every common query, plus all specified probes, covered with zero excluded outputs. Public runtime exclusion text is removed; decoded data and SCOWL are checked independently.

#### Voice walk

Held 120 ms Read and Stress clicks, with 2 s gaps. allLines() is exactly [Type a line.], equal to voice/lines.json. vlog is empty because the one fixed recording is intentionally absent. No recorded line was heard and no claim of recorded narration is made. Read visibly presents and live-announces only Type a line. Speak remains gated to localService English voices. Student text is not passed to Read.

#### The real material

CMU dictionary and its full BSD-style notice, retained raw input fetched 2026-11-05; repacked with 367 classroom editorial exclusions on 2026-11-06. SCOWL 2020.12.07 English/American through size 50, MIT-like and component notices retained, raw fetched 2026-11-05; final common intersection 44,286. Dataset sources/licences are in the Manual and tool.draft.json. No new dictionary or poem dataset was downloaded in this pass.
Touched text and form facts: Gutenberg ebooks 2151 (Poe), 58611 (Frost), 353 (McCrae), 19221 (Shakespeare), checked against independent Academy of American Poets witnesses, all original literary text public domain in the United States. URLs and per-fact checks are in fix-facts.json. Previously documented historical-edition differences are retained; this is not a claim the editions are identical. Original form interpretations and the editorial filter are Curio Class CC0. Cambridge here and Merriam-Webster's pronunciation guide were read as references; none of their copyrighted prose/audio is bundled.

#### Engine changes wanted

None. The shared kit was not edited.

#### Audit

Completed once within the 40-minute limit: `fix-audit/audit.md`, 40 frames, all inspected on sheets 00 to 09. No console errors, endless animations, resize exceptions or stuck controls. Final bundle: 1,612,029 bytes; scoped check_tools checks pass with zero errors (`fix-contract.json`). The full checker is not invoked because its import-time bundle_all() would write other tools; its own check and notes_sections functions run on a Scratch copy with draft metadata mapped to tool.json.

All 65 mechanical leads were assessed by category:
- Default editor/hint overlap and editor focus on load: the transparent native editor sits over the proof, while the hint occupies a blank line. Initial focus uses preventScroll, as the ready-to-type spec requires; retained under the Settled calls.
- Hint out of view after Stress, Play and opening rhymes: it is deliberately dismissed by action, restored on clearing or Read. No lost instruction is inferred from a hidden first-run hint.
- Manual/Drafts keep-region and text-under-dialog leads: deliberate modal drawers, explicitly retained by the merged list.
- Rhyme drawer overlaps with part of the editor, paper tabs, tempo and readout: deliberate overlay required by accepted Polish 5. The page never reflows, the selected word remains usable, close/Escape remains available, and the phone sheet keeps the selected line above it. This is not a claim that the entire underlying editor is unobscured while a drawer is open.
- Print nothing changed: headless print behaviour, already settled. Sympathy covered and lower shelf books off screen: labelled scroll list, already settled. The additional Owl nothing-changed lead was disproved with a real held click after scrolling its spine into view; provenance becomes EDWARD LEAR and the actual poem loads (`post-shelf-owl.json`, `fix-post-audit/post-shelf-owl.png`).
- No fixed narration heard: expected absent Forge clip, not an unverified claim of spoken lines. allLines and the declared line list agree.

The one audit used the retained `fix-audit-input.html` snapshot. Subsequent narrow visual rechecks cover two presentation corrections: selected-tab ink now follows aria-selected, and the phone Replace toggle sits in the drawer head so the list has 79.92 px rather than the earlier thin strip. A real phone tap inserts bought after hot and closes the sheet (`post-phone-insert.json`). Final phone/680/1366 frames are in fix-post-audit. The filter review also added eleven exact expletive entries; all 132,858 final query lists were rechecked. The full audit was not rerun.

Final filter policy SHA-256: `d0f521149c700e7bb1ed7dee5d40d27bc114e0c3ebe05b9c60520e6961619872`. Material SHA-256: `982d236873061d0ec18dffe7b45276f1d14509ac9c349ac0bad50e57087442a2`. Check output and encoded exact exclusion list are in notes.md. The final sensitivity PASS also verifies 60 protected names/identity/neutral-word probes. Every final post-audit shot has zero browser errors. The HTTP test server sometimes logs a connection reset when Chrome closes; this is harness teardown, not a tool exception.

No Chrome or host server started for this pass remains listening on 9910, 9911 or 8715. No host.html remains. The refine.md SHA-256 is unchanged: `82373ab61176e377919ede56b8245532a68da771c163cfc594f78f3bc6d73a84`.

#### Left open

The smooth-narrator recording awaits the collective Forge pass, as settled. No goal, score, level, quiz, finish screen or kit header was added. Source hits for score are internal variant-selection variable names; complete occurs only in autocomplete. There are no such student-facing constructs. No em dashes in the touched source, notes or handoff. No engine changes or external publication.
The initial small-proof test had an invalid driver selector quote, and the phone host requested a missing favicon. Both test causes were corrected; `fix-retry/` has zero errors. A failed optional contact-sheet route lacked Pillow, so a standard-library screenshot compositor was used. Every frame claimed in this report was inspected directly or on its contact sheet.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Poet's Workbench build handoff

#### Structure

`src.html` holds the desk, transparent native textarea and exact matching proof mirror, scansion, local audio, drawer and storage.
`material.json` is loaded by the bundler's `json:material` token. It holds the gzip/base64 dictionary, phone alphabet, poems and licence.
The generated `poets-workbench.html` is the offline instrument. Edit source, then bundle with CURIO_DRAFT=1.

The reproducible packer and raw downloaded text are in `_scratch/poets-workbench/gather_pack.py` and its `data/` folder.
The original staged dictionary is kept in Scratch. The packer verifies the selected texts and records material statistics and hash.

#### Engine changes wanted

None required. The kit's Curio.voice is used. A local Read guard prevents browser speech fallback when the fixed recording is absent.
The smooth-narrator recording of `Type a line.` remains to be supplied by the normal voice preparation process.

#### Care points

The editor and proof mirror must use identical font, width, padding and line height. Never put formatting whitespace into the rendered verse.
The mirror follows the textarea client width, including a scrollbar gutter. Bottom padding is 16 px so short windows retain a usable text area.
The editor receives focus on opening, as the spec's ready-to-type caret requires. Focus never scrolls the outer page.
Scansion considers each foot and offset using dictionary alternatives. Grey marks are flexible, while blue marks are user choices.
The rhyme index uses actual phone sequences; display ordering is the SCOWL common tier grouped by syllables, then a Names and rare words fold, also grouped by syllables.
SCOWL raw source, copyright, packing and data mutation scripts are retained under `_scratch/poets-workbench/review_*` and `data/review-scowl/`.
`material.json` contains the packed lowercase CMU intersection and full SCOWL component notices.
After gathering material, run the final `fix_pack.py` and `fix_verify_data.py` from Scratch before bundling. The final packer restores raw SCOWL tiers then filters both datasets.
Read must never receive student text. Speak must retain the localService voice filter.
Rhyme keys normalise IY R to IH R; original CMU phones stay visible. Frost now reads AABA BBCB CCDC DDDD. Other pre-R vowels stay distinct.
Secondary stress follows the meter as flexible; line-end variants prefer a nearby rhyme unless explicitly overridden.
Single-syllable alternate readings cycle through pronunciations then weak stress. Saved choices preserve both fields.
Rhyme lists append 150 entries at a time so large slant-rhyme families do not create thousands of buttons at once.
Sounds uses the line's chosen stress marks when finding repeated vowels, including all strong vowels of longer words.
Book and rhyme lists use arrow navigation with one Tab stop. Rhyme drawers overlay the desk without changing page width. On a narrow desktop they choose the side away from the word; phone drawers are bottom sheets with matching editor/mirror scroll padding.
The full-size Stress key duplicates tapping a printed proof annotation and Alt F without changing the exact textarea/mirror geometry.
Beat playback schedules one next beat; tempo changes reschedule it without resetting the cursor. Stop clears the transport and active audio nodes.
Saved draft JSON is validated before use. Loading or editing closes rhymes and resets the handle's expanded state.
Alt R and Alt F do not act on the page while a modal drawer is open.
Drafts uses a two-column slot layout in short landscape windows so all four slots and Print stay visible.

#### Owner decisions applied

Curiosity shape replaces the lesson frame. No teacher plan, kit header, check, progression or ending screen is included.
Code drawings are used throughout. No images or paid audio are generated. No commits. The scoped Claude Refine fix is recorded in polish.md.
The Curiosity gathering instruction overrides old offline-prep wording. The cold review added the spec's SCOWL common-word sort.

#### Sensitivity

Keep Hughes's Black identity and Dunbar's caged-bird imagery intact. McCrae's poem contains war and recruitment language;
Poe and Dickinson address death, and Henley includes religious imagery. The Japanese on/English syllable distinction belongs beside haiku guidance.
The owner settled that no shelf poem needs a sensitivity review. These are literary texts for exploration, without moral scoring.
The required separate classroom-filter sensitivity review passed; see `_scratch/poets-workbench/fix-filter-sensitivity.md`.
Do not restore the old runtime exclusion list: excluded entries must be absent from both packed CMU and SCOWL.

#### Refine implementation care

Line scans are cached by text, index, lens, preferred foot, end-word variant and user overrides. Unchanged verse nodes stay in the mirror.
Do not put the mirror below the textarea: its wrapper is above, with pointer events only on proof buttons.
Paper guides count nonempty lines; haiku and limerick reset by stanza. The meter readout uses whole feet and explicit missing/extra syllables.
The tempo range is the sole accessible slider; the visual knob remains draggable but hidden from assistive technology.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: refine.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/craft.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/play.md folded in (last changed 2026-11-07)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-11-07)
- 2026-11-25: polish.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
