# Poet's Workbench build handoff

## Structure

`src.html` holds the desk, transparent native textarea and exact matching proof mirror, scansion, local audio, drawer and storage.
`material.json` is loaded by the bundler's `json:material` token. It holds the gzip/base64 dictionary, phone alphabet, poems and licence.
The generated `poets-workbench.html` is the offline instrument. Edit source, then bundle with CURIO_DRAFT=1.

The reproducible packer and raw downloaded text are in `_scratch/poets-workbench/gather_pack.py` and its `data/` folder.
The original staged dictionary is kept in Scratch. The packer verifies the selected texts and records material statistics and hash.

## Engine changes wanted

None required. The kit's Curio.voice is used. A local Read guard prevents browser speech fallback when the fixed recording is absent.
The smooth-narrator recording of `Type a line.` remains to be supplied by the normal voice preparation process.

## Care points

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

## Owner decisions applied

Curiosity shape replaces the lesson frame. No teacher plan, kit header, check, progression or ending screen is included.
Code drawings are used throughout. No images or paid audio are generated. No commits. The scoped Claude Refine fix is recorded in polish.md.
The Curiosity gathering instruction overrides old offline-prep wording. The cold review added the spec's SCOWL common-word sort.

## Sensitivity

Keep Hughes's Black identity and Dunbar's caged-bird imagery intact. McCrae's poem contains war and recruitment language;
Poe and Dickinson address death, and Henley includes religious imagery. The Japanese on/English syllable distinction belongs beside haiku guidance.
The owner settled that no shelf poem needs a sensitivity review. These are literary texts for exploration, without moral scoring.
The required separate classroom-filter sensitivity review passed; see `_scratch/poets-workbench/fix-filter-sensitivity.md`.
Do not restore the old runtime exclusion list: excluded entries must be absent from both packed CMU and SCOWL.

## Refine implementation care

Line scans are cached by text, index, lens, preferred foot, end-word variant and user overrides. Unchanged verse nodes stay in the mirror.
Do not put the mirror below the textarea: its wrapper is above, with pointer events only on proof buttons.
Paper guides count nonempty lines; haiku and limerick reset by stanza. The meter readout uses whole feet and explicit missing/extra syllables.
The tempo range is the sole accessible slider; the visual knob remains draggable but hidden from assistive technology.
