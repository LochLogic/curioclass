# Codex report: poets-workbench (Curiosity No. 10)

## Built

A writer's desk, with an editable typewriter page, live pronunciation proof, rhyme drawer, sixteen cloth-bound books,
five papers, four local draft slots, print styles, beat playback and device-local Speak. Maker's plate and Manual are
lower-left; Motion, Sound and Read are on the desk's power panel. The tempo knob works by dragging and by keyboard.
The page opens ready to type, with its real caret after Frost's opening line. No lesson frame or progression layer.

Files: `src.html`, `material.json`, `poets-workbench.html`, `tool.draft.json`, `notes.md`, `voice/lines.json`,
`audit-states.json`, `handoff.md`, `art/prompts.json`, and this report. Build only; no commits or polish round.
Final bundle: 1,185,955 bytes, about 1.186 MB against the 2 MB goal.

## The real material

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

## Break the instrument

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

## Voice walk

The declared bank is smooth-narrator, Algieba. `allLines()` and `voice/lines.json` both contain only Type a line.
The fixed recording was not supplied, and the build instructions prohibit recording it here. Read therefore displays
and announces that fixed hint as text; it never falls through to browser speech or reads the student's writing.
This is an open voice deliverable, not a passed narration check. `__tool.vlog` stays empty without the clip.
Speak is separately gated to installed English voices whose `localService` is true. Its tested utterance selected a
local voice. Sound off cancels playback and speech. The ten-minute walk contains no browser errors or network requests.

## Short test

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

## Lesson creep check

Word-boundary search of source and voice lines for score, points, level, goal, sticker, badge, correct, wrong, try again,
complete and well done: zero hits. No kit header, mode pills, quiz, target list, rewards or ending screen.
Match counts are scansion readouts requested by the spec, rather than an assessment.

## Done when

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

## Audit leads

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

## Frames looked at

Required four models; early first-page/drawer/preview frames; all twelve full size/state captures in `layouts/`;
all six walk frames; all 34 audit PNGs on nine contact sheets, with key small-size/modal frames enlarged;
three final functional frames and all follow-up frames in `final-layouts/`, plus the final sound-repeat frame.
Every generated frame was examined directly or on its labelled contact sheet. Pixel text was checked on enlarged representative states.

## Art made

No painted images. Paper, curl, chrome bail, ruler, walnut, cloth books, index cards, proof marks, knob and engraved plate
are drawn in HTML/CSS and native text. `art/prompts.json` explicitly lists no bitmap assets. No people assets.

## Engine changes wanted

None. Shared files were not edited. The fixed hint clip belongs to the normal voice-preparation pipeline.

## Left open

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
