# Codex review: poets-workbench

## Played

Cold as a grade-7 writer, then an adult revising sound: all sixteen shelf poems, all five papers, the rhyme drawer, stress choices and beat transport.
The continuous cold walk lasted 520.8 seconds; initial play and further control/extreme checks took total use beyond ten minutes. Builder files stayed closed until the cold walk ended.
The desk feels like an instrument: paper, words and red proof marks carry the interaction. No lesson criteria, quiz or reward system were imposed.

## Short test

- Would a kid open it unassigned? Likely: names, nonsense words and instant rhymes invite experiments. This is reviewer judgement, not a child study.
- Would an adult play for fun? Yes: real pronunciation alternatives and revision give the page depth; live tempo and useful rhyme ordering now keep the flow.
- Is the real material the interface? Yes: editable verse, CMU phones, syllables, stress and audible strong/weak beats are the working surface.
- Does it work without a score or finish? Yes. No goals, scores, levels, quiz, finish screen or kit header were added; source/voice lesson-creep search is empty.

## Findings fixed

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

## Findings left

- **Blocker, voice:** the required smooth-narrator “Type a line.” recording is absent. No supplied clip exists. The [Ground rules](../../docs/agents/CODEX-BUILD.md#ground-rules) say “Do not download anything or record audio”; the Curiosity data exception does not authorise recording. I retained the spec's recorded-only privacy guard and did not substitute browser narration. Narration remains unready.
- **Spec conflict:** strict CMU produces Frost `AABA CCDC DDED EEEE`, rather than conventional `AABA BBCB CCDC DDDD`. `here` uses IY R; `queer/year` use IH R. Preserved real phones and the Manual's explanation instead of inventing accent normalisation.
- **Intentional:** the real editor receives initial focus to provide the spec's ready-to-type caret. The quiet hint sits over its empty second line and disappears on action. Modal drawers intentionally cover and disable the page.

## Break it

- No score, check or success meter exists to cheat. Pattern-match counts are descriptive scansion, not rewards.
- Empty/whitespace, punctuation, emoji, numbers and pasted markup stay safe; markup remains text. Unknown invented words retain dotted estimates.
- All foot lenses and paper guides tested; tempo 60/160 tested repeatedly, plus real jittered knob drags to both limits while playing.
- Sixty rapid input events leave the final text intact. A 20,000-letter unknown token generated 10,000 estimated beats without freezing; render took about 187 ms on this desktop.
- `record` cycles real pronunciations; the noun/verb sentence differs. Keyboard Tab/Enter changes stress, arrows/Enter insert a rhyme and focus returns to the editor.
- Orange: 0 perfect, 7,822 same-vowel and 76 same-ending entries in this filtered snapshot. Held clicks traversed every rhyme tab twice. Hot includes lot, not and spot, now near the front.
- Measured gains: weak 0.065, strong 0.22. Measured beat gaps change from about 1 s at 60 BPM to 0.375 s at 160 BPM; playback survives 1366 → 760 → 680 resizing.
- Sound off creates no audio nodes; Motion off leaves zero running animations. Grayscale retains marks, letters and readable controls.
- Corrupt draft cases, loading with rhymes open, empty playback and shortcuts through a modal were replayed after repair. No application exceptions in the rechecks.

## Voice walk

Sound on; held clicks about two seconds apart: type → Play → rhymes → Manual → shelf → papers → Drafts → Read → Sound off → Read → Sound on.
Only one fixed line is declared, exactly matching `allLines()` and `voice/lines.json`. No extra per-mode lesson narration was introduced.

| Line/kind | Expected | Heard |
|---|---|---|
| Type a line / initial hint | once | 0: recording missing |
| Type a line / Read, Sound on and off | each Read | 0: recording missing |
`__tool.vlog` remains empty. Read does not speak student text. Speak separately uses only installed English voices with `localService: true`.

## Facts checked

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

## Sensitivity

Preserved all authors and poems. A later cultural lens should look at Hughes's Black identity, Dunbar's caged-bird imagery, McCrae's war/recruitment language, Longfellow as literary history, death/grief in Poe/Dickinson and Henley's religious imagery. Notes now flag these. Haiku guidance explicitly distinguishes Japanese on from English syllables. No new cultural claims or people art were added.

## Flattest moment left

Some pronunciation choices sound odd in real speech even when they fit a repeating foot. The Manual calls the result a closest-pattern hypothesis; the writer can disagree and revise. The real remaining interruption is silent Read until its recording is supplied.

## Graphics

Kept the walnut, chrome bail, cloth books, paper curl, proof ink and engraved plate. No raster images or people were added. Final bundle: 1,603,263 bytes, below 2 MB.
All cold-walk, required-size and changed-state frames were viewed, individually or on labelled contact sheets; narrow drawer/Drafts fixes were enlarged. Frame comparison:

| This instrument | Reference studio |
|---|---|
| ![Poet's working page](../../_scratch/poets-workbench/review-final/raven-desk.png) | ![Beat Lab](../../_scratch/poets-workbench/review-reference/reference-beat-lab.png) |

## Audit

The single audit finished within its 40-minute limit: **38 leads, 40 frames**, at 44-pixel desk targets. Full evidence: `_scratch/poets-workbench/review-audit/audit.md`.

- Confirmed/fixed: Drafts' short-window choice clipping. Re-shot 680x425 (including blocked saving), 1366x768 and the 375x812 iframe; all eight Save/Load keys and Print are visible. All four slots round-trip text, paper and stress choices. Unbroken draft titles now wrap on phones.
- Intentional: initial ready-to-type focus; a pointer-transparent hint over the empty line; its disappearance after action; modal drawers covering the underlying editor/Manual button. These are Curiosity behaviours, not missing lesson instructions.
- Confirmed functional: Print opens an external dialog, so the page need not change; the knob responds to real drags, not a tap; the shelf scrolls and roving keys reach the final Invictus book. The cold walk loaded the Owl entry that the audit's clipped-centre click missed. Opening rhymes deliberately reserves paper space.
- Motion off and mid-action resize report no exceptions or stuck controls. Missing narration is the open blocker above. Rechecks had no application errors; the standalone test host's favicon 404 is wrapper noise, not an offline-tool request.
The full audit was not repeated after its scoped Drafts repair. The repository checker was run against an isolated Scratch copy with draft metadata as tool.json, using the actual checker functions without rebundling other tools: syntax, contract and notes checks pass.

## Done when

1–4: PASS for live typing/opening, 8-syllable Frost line, real rhyme results and record alternatives. 5: Dickinson PASS; conventional Frost chain conflicts with strict data, documented above.
6–7: PASS for dotted unknowns, strong/weak playback and reduced motion. 8: keyboard/value/privacy PASS, required fixed narration FAIL. 9: required sizes inspected; changed narrow states rechecked.
10: one offline file under 2 MB, licence notices, no em dashes and scoped contract/syntax checks PASS. 11: no lesson progression or rewards, PASS.

## Left open

Supply the specified fixed hint recording before treating the tool as ready. No kit change is needed. Do not silently force Frost's conventional scheme into CMU's exact-phone output.
School Chromebook hardware and a physical printer were unavailable. Desktop timing and print CSS are not hardware certification.
Unattended decisions followed the brief: SCOWL common-word sort, faithful older editions/CMU phones and a large equivalent Stress control. No questions, commits, other-tool edits or second review pass. All owned Chrome/server processes closed; temporary host removed.
