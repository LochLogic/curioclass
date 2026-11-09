# Codex review: letter-lanterns

## Played

Cold, as a kindergarten child and projecting teacher, before opening the builder's report, handoff, notes or source. Played every activity type, the normal path through the first long/short pair, and the demo/full-village finale. The creature reveal and lantern lift are strong; Village initially felt like small shops beneath a large wall. Evidence: `_scratch/letter-lanterns/review/`.

## Findings fixed

- Should fix, general, compact Village: Read the street read only the visible page and then claimed the whole street. It now visits all open shops across pages, then banners. Partial turns have a different ending.
- Should fix, general, voice: older words could continue after arrows or closed-shop taps. Reading redirects now interrupt ordinary narration and invalidate the old turn. Read retains priority; mode changes, Stop and reset still hush it.
- Should fix, general, Wake voice: Say's cue was dropped at a two-second pace. A shorter action cue leads the intro. Per-stroke miss/shared-letter cues are cached when heard, not queued. Plain first taps now speak the welcome or the saved Wake question. Sound back on restores the current instruction; Hear it again in Say replays the sound.
- Should fix, general, Sign: its heading crossed model letter buttons at 680 and 1366. Moved it aside without removing it; rechecked 680, 1366 and 375.
- Should fix, general, notes: "three single-letter sounds" obscured x's two sounds in box/fox. Changed this skill to blending letter sounds into a short word.
- Polish, general, art/play: redrew the street with low masonry, distant hills and foreground cobbles; enlarged the wide Sign shop and added warm light/goods feedback. Kept all 96 paintings, the palette, creature pairs, letter glass and lantern flight.
- Should fix, general, focus: Read/Stop hid the focused control; a later step could select a disabled model button as fallback. Reading now transfers focus to its replacement, and step fallback chooses a visible, enabled control. First-sign fallback passes at 680 and 1366; its post-fix phone replay is left open below.

## Findings left

- Blocker, general: none of the 31 required isolated recordings is available or listening-approved; 310 fixed lines still use browser fallback. Solo phonics release remains blocked. CODEX-BUILD.md says "Do not download anything or record audio"; this review did not override it or certify TTS as phoneme audio.

## Break it

- Trace: 100 non-dot strokes, guided and independent, gave 800 careful/backward/tap/half checks with zero unexpected results. Two dot strokes are intentionally taps. Real backward A, tap M, half T, scribbled O and free half-stroke reject; a careful shaky S passes. Repeated after fixes.
- Three guided misses demonstrate and advance without an independent badge. A failed optional write followed by Next leaves no badge or stale failure gate.
- Glow: five repeat correct taps earn one credit; wrong then right earns none; two-sound pools earn none. C/k never compete. All 5,200 first-meeting choice samples had three distinct choices/sounds and respected b/d/p/q separation.
- Real held wrong-option attempts covered all 24 signs, 10 twins, 6 long/short pairs, 5 vowel activities and 10 banner checks. Shared twin letters do not advance; wrong pictures do not open shops; repeated tall-flame taps cannot skip the short model. Correction completes guided practice without mastery glow.
- Wake all is a one-star demo. All off/one on, reset cancel/confirm, malformed save and a real mid-stroke reload pass. There is no saved best score or reflection assuming an unobserved mistake. Oral saying is explicitly practice checked together.
- Reading: a real phone run visited all six shops and three banners across all three pages, with no spoken-word/highlight mismatch. Redirecting to pin and tapping a closed shop stop the old turn. Motion on/off both preserve the three-second class turn; Read also works with Sound off.

## Voice walk

Fresh Wake button, m/s/a/t, banners, three Finds, See and say, banner find, p/map Sign, Village, Read the street, Stop. Held taps 120 ms at two seconds, real drags, and a two-second air-writing pause. Nothing spoke before the first tap. First-welcome cuts follow BASELINE 16.
Heard in order: welcome, Say, capital trace, small trace, air, optional writing, two glows, See and say, first Sign, Village. Each how-to starts once, then is silent on repeats. Side paths verify Twins/long-short narration, Sound, Read and correction feedback. Evidence: review/main-voice.json and review/quiz-checks.json.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| Say / capital trace / small trace | how, each | 1 | 1 |
| Air / optional writing / two glows | how, each | 1 | 1 |
| See and say / first Sign / Village | how, each | 1 | 1 |
| Wrong s feedback | event | 5 | 5 |
| Sound m replay | event | 5 | 5 |
| Shared twin letter | once per pair | 1 | 1 |

These are muted browser start logs, not listening approval of missing clips.

## Facts checked

- RF.K.3a-d cover consonant correspondences, five vowel contrasts, sight words and differing sounds in similar words: [Common Core kindergarten reading](https://www.thecorestandards.org/ELA-Literacy/RF/K/). Each has an activity; audio accuracy remains blocked above.
- Upper/lower printing supports L.K.1a: [Common Core kindergarten language](https://www.thecorestandards.org/ELA-Literacy/L/K/). Inspected all 52 forms and 102 strokes. The model is not the only valid handwriting order: [Learning Without Tears formation charts](https://www.lwtears.com/sites/default/files/2022-01/English_print_letterCharts.pdf).
- Printed consonant mappings, hard c/g, c/k equivalence, final x=/ks/ and quail's qu follow the supplied Moats/Reading Rockets table and [WETA articulation guidance](https://readinguniverse.org/skill-explainer/articulation-pronunciation/articulation-skill-explainer/overview-what-is-articulation). The full Moats book was not reread; this mapping check is against the supplied table. No clip pronunciation is certified.
- Short anchors ant/elephant/inchworm/octopus/umbrellabird and long anchors acorn/emu/ivy/ocean/unicorn match the supplied vowel table. The six no/not, go/got, me/met, he/hen, hi/hit and we/wet pairs match [Moats and Tolman, Six Syllable Types](https://www.readingrockets.org/topics/spelling-and-word-study/articles/six-syllable-types). Indexed primary text was available; direct access returned 403.
- All ten banner words belong to both the 40-word [ReadWriteThink Dolch pre-primer list](https://www.readwritethink.org/sites/default/files/resources/lesson_images/lesson301/dolchwordlist.pdf) and [Kingsville ISD Fry first 100](https://www.kingsvilleisd.com/apps/pages/index.jsp?pREC_ID=665709&type=u&uREC_ID=460382). Membership independently recomputed.
- Final-e stays outside this tool: [Common Core RF.1.3c](https://www.thecorestandards.org/ELA-Literacy/RF/1/). Box/fox have three printed letters but four phonemes, consistent with x=/ks/ and the RF.K.2 phoneme definition.
- Recomputed 24 unique three-letter shop spellings, all five short-vowel letters, 10 one-position twins (5 first/3 middle/2 last), all prerequisites and the three-event cap. Default events drain at lantern 25 with 24 shops, 10 twins, 6 contrasts and 10 banners.
- Per-letter glow model: perfect answers brighten after four checks; independent 80% accuracy gives 40.96% after four and 91.16% after eight; guessing gives 1.23% after four. These are model probabilities, not child-validation claims.
- WCAG relative-luminance calculations confirm ink/panel 15.32:1, brand/panel 8.93:1, muted/panel 9.85:1, letter/glass 12.26:1, sign 12.56:1 and focus/night 12.38:1. Long-flame contrast is 14.49:1, not the spec's 15.8; short flame is 8.72:1 and actual button text 8.38:1. Grayscale retains poses, stars and open/closed cues.
- Privacy checked in source: device localStorage only, no microphone or external asset requests. Teacher states device-only saving. Runtime lines equal the 310-line manifest.

## Sensitivity

No human figures, named culture, religion or hard history; this is a fictional animal-lantern village. Later listening review should check US-English short o and long u without treating a child's dialect as an error. The tool does not grade speech.

## Flattest moment left

Long/short remains two word boards with a comparison, as specified. It is quieter than the creature reveal and shop opening; no extra game or topic was added.

## Graphics

All 96 images inspected on contact sheets and in scenes; all 52 glyphs checked together. No people or missing art tokens. Street redrawn with built-in imagegen, processed by free art.py --rekey, final 2400x600 at quality 72. Art 1831.6 KiB; bundle 2865.2 KiB (2,933,986 bytes). Prior painting/raw kept in review Scratch. Saved art: art/raw/street-night.png and art/street-night.webp; production prompt: art/prompts.json, street-night plus house_style.
Every required size was checked, including the 375 iframe on 8765, keyboard-only navigation/tracing, Motion off and grayscale. Sign was re-shot at affected sizes. Contact manifests enumerate inspected frames. Existing Snowy Mail Route and Beat Lab reference frames were also opened; no sibling bundle was rebuilt.

## Audit

One full audit completed in about 26 minutes on Chrome 9961 and host 8765: `_scratch/letter-lanterns/review-audit/audit.md`. Inspected all 74 PNGs. Its 25 leads were one real Read focus fault, 17 consequences of three invalid drag recipes, and seven welcome interruptions permitted by BASELINE 16. Fixed Read focus, added explicit drag returns and corrected the phone-size labels. Valid replay also exposed the disabled fallback focus fault, now fixed. Independent writing passes all three sizes; first-sign replay passes at 680 and 1366. Resume to lowercase s passes at 1366 and phone size. Read/Stop/Enter focus passes at 680, 1366 and phone size. All ten scoped recheck frames were inspected; successful corrected routes have no layout/runtime leads. No second full audit. The focused batch and smaller first-sign retry each reached their 280-second cap before the phone sign; that replay stops here under the brief.

## Left open

- Audio production/listening remains blocked by the no-recording brief. This is a completed code/art review, not a release PASS.
- Check limit: the post-fix phone first-sign input replay did not finish after two bounded batches. Earlier phone Sign layout re-shots were clean; post-fix focus on that full phone route is unverified.
- The spec's historical child-motor percentages lack a reproducible noise recipe. They were not repeated as validated child results; defined attacks were independently checked.
- Kept literal off-letter event dropping; late re-enabling does not backfill dropped events. The named warm-teacher voice wins over the contradictory neighbor-variety sentence.
- No questions in this unattended run, no commits, and direct writes stayed in the two allowed folders. One initial read-only rules command lacked an explicit process deadline; subsequent commands used bounded jobs. Existing scripts' bytecode caches predate this session. Owned Chrome ports and host 8765 are closed; no tool-folder host.html remains.
