# Polish: poets-workbench (Codex fix, round 1)

Curiosity No. 10. Cwd verified as `S:\CurioClass-codex`. Only this tool and its Scratch folder were written; no commits; `refine.md` and `refine/` were not edited.
Evidence paths below are relative to `_scratch/poets-workbench/`. Browser checks use `scripts/drive.py` through `fix_run.py`, Chrome 9910, host 8715; the final audit uses 9911.

## Blocker

1. FIXED. Pack-time classroom exclusions replace the public runtime list and filter CMU and SCOWL together. Baseline `before-numbers.json` reproduces the required everyday queries; `fix-before/before-drawer.png` shows the original moon list. Final: 367 excluded entries absent, 125,571 words and 44,286 common entries remain; all 132,858 lists for 44,286 queries pass with zero forbidden hits (`fix-filter-check.json`). The scoped fresh-agent sensitivity review is PASS (`fix-filter-sensitivity.md`). Exact exclusions and policy are in Scratch; notes.md contains the check output and gzip/base64 final list, avoiding a plaintext public slur list. Ordinary-name and neutral-identity probes pass.
2. FIXED. IY R folds into IH R in rhyme keys; original phones remain visible. Baseline Frost `AABA CCDC DDED EEEE` and couplet `ABBB` become `AABA BBCB CCDC DDDD` and `AAAA` (`before-numbers.json`, `after-numbers.json`, `final-verified-checks.json`). Other pre-R alternate pairs were inspected and retained as accent-sensitive, rather than indiscriminately merged (`fix-facts.json`). The misleading strict-dictionary explanation is removed.
3. FIXED. Meter length uses whole feet and explicit missing/extra syllable wording. Baseline has 227 decimal-foot shelf labels; final has zero across every shelf line (`before-numbers.json`, `final-verified-checks.json`). Examples include trochaic octameter, last syllable dropped. No fractional readout remains.
4. FIXED. When any family label has two letters, every stanza separates its labels with middle dots. The Raven's last four groups each contain six distinct labels, for example `AA·B·AB·B·B·B`; margin labels use the same family names (`final-verified-checks.json`; before/after Raven frames at 1366x768).

## Should fix

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

## Polish accepted

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

## Settled calls

Applied: no shelf review; only the required filter review. Read waits for the collective Forge clip. Match counts stay readouts, with no goals or grading. Syllable grouping stays inside common and rare tiers. SCOWL stays a browsing order rather than a frequency claim. Deliberate modal overlaps, editable textarea/mirror overlap, initial caret focus, shelf scrolling, knob drag/arrows and Print behaviour are retained. No module edits were made; the RL.7.4 word-meaning coverage question and broader Auto-default question remain for the spec/module owner.

## Cheats tried

- Function-word-only line: all beats remain flexible; fixed matches are not inflated into a score. I hear the rain separates 2 fixed from 2 free.
- Pronunciation/stress cycling of seven ambiguous words: every listed reading and weak option is reachable; no mode creates a best result or saved score.
- Paper switching and guide patterns across blank lines: these only change faint guides. They never award a pass.
- Every shelf line, including shortened lines and long Raven lines: zero decimal-foot names. The readout explicitly says when syllables are missing or extra.
- Rhyme safety: all variants and all three list kinds for every common query, plus all specified probes, covered with zero excluded outputs. Public runtime exclusion text is removed; decoded data and SCOWL are checked independently.

## Voice walk

Held 120 ms Read and Stress clicks, with 2 s gaps. allLines() is exactly [Type a line.], equal to voice/lines.json. vlog is empty because the one fixed recording is intentionally absent. No recorded line was heard and no claim of recorded narration is made. Read visibly presents and live-announces only Type a line. Speak remains gated to localService English voices. Student text is not passed to Read.

## The real material

CMU dictionary and its full BSD-style notice, retained raw input fetched 2026-11-05; repacked with 367 classroom editorial exclusions on 2026-11-06. SCOWL 2020.12.07 English/American through size 50, MIT-like and component notices retained, raw fetched 2026-11-05; final common intersection 44,286. Dataset sources/licences are in the Manual and tool.draft.json. No new dictionary or poem dataset was downloaded in this pass.
Touched text and form facts: Gutenberg ebooks 2151 (Poe), 58611 (Frost), 353 (McCrae), 19221 (Shakespeare), checked against independent Academy of American Poets witnesses, all original literary text public domain in the United States. URLs and per-fact checks are in fix-facts.json. Previously documented historical-edition differences are retained; this is not a claim the editions are identical. Original form interpretations and the editorial filter are Curio Class CC0. Cambridge here and Merriam-Webster's pronunciation guide were read as references; none of their copyrighted prose/audio is bundled.

## Engine changes wanted

None. The shared kit was not edited.

## Audit

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

## Left open

The smooth-narrator recording awaits the collective Forge pass, as settled. No goal, score, level, quiz, finish screen or kit header was added. Source hits for score are internal variant-selection variable names; complete occurs only in autocomplete. There are no such student-facing constructs. No em dashes in the touched source, notes or handoff. No engine changes or external publication.
The initial small-proof test had an invalid driver selector quote, and the phone host requested a missing favicon. Both test causes were corrected; `fix-retry/` has zero errors. A failed optional contact-sheet route lacked Pillow, so a standard-library screenshot compositor was used. Every frame claimed in this report was inspected directly or on its contact sheet.
