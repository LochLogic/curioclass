# Craft lens: letter-lanterns (round 1)

Cold Craft lens on the built bundle `tools/letter-lanterns/letter-lanterns.html` (2,930,709 bytes). Not a Curiosity
(K ELA lesson tool), so lesson norms apply. My frames and logs: `S:/CurioClass-codex-scratch/letter-lanterns/craft/out/`
(frames), `craft/voiceA.txt`, `craft/v56.txt`, `craft/v5.json` (voice logs), `craft/shots/*.json` (the shots).

Counts: blockers 1, should fix 6, polish 3, nit 5.

## Contract (clean)

- One file, kit used (Curio.voice, Curio.yes, Motion, Sound, Read). No network requests: no http(s) URL, fetch or XHR
  in the bundle; `performance.getEntriesByType('resource')` empty after a full start (probe shot). No console errors
  or exceptions in any of my 60 shots (the only log line was the iframe host page's own favicon 404, not the tool).
- Frame times, Village with 12 lit lanterns and fireflies at 1366x768: median 16.7 ms, p95 16.7, max 16.8 over 3 s
  (P-frames-village).
- Art: all 96 `art:` tokens have a prompts.json entry and every entry is used; all `people: false` (creatures, goods,
  shops, scenes).
- Words: no em dashes in src, notes, spec or lines; "Curio Class" never "Curio" alone; privacy line in Teacher
  ("Lanterns are saved on this device only. Nothing leaves it.") and spoken on open.
- Targets: every visible control 60 px or more at 680x425, 800x500, 1000x625, 1366x768, 1920x1080 in the flames,
  twins, long/short, banner, banner find, sign and Village states (button sizes printed in each L-* shot). Keyboard:
  lanterns take a visible focus ring (K-focus-lantern-1366); the slate traces by keyboard (Space, 29 x ArrowDown,
  Space passed stroke 1 of capital M, v8c).

## Findings

1. **blocker** (general). `src.html:679-692` `glyph()`, used for shop signs (`:1510`) and long/short boards (`:1601`).
   Each letter's SVG viewBox is cropped to that letter's own bounds, so every letter is scaled and centered on its own:
   x-height letters grow to near capital height and there is no shared baseline. Lowercase c and o on the "cot" sign
   read as capitals ("COt"), the descenders of p and g float up level with the other letters instead of dropping below
   the line ("pup", "pig", "dog"), and the o in "dog" sits high. These are the words kindergartners are asked to read,
   and the tool teaches letter forms. Seen: `out/Z-signs-village2.png` (zoomed signs), `out/L-sign-680x425.png`,
   `out/L-twins-1366x768.png`, `out/H-twins-375x812.png`. Better: lay each word out on one shared slate box (top line
   0, baseline 1, descender 1.5) with fixed advance widths, the way the trace slate already does.
2. **should fix** (general). `src.html:1764` and `:578-580`. Opening Teacher speaks `teacher`, `privacy` and
   `glowHonesty` as event lines every time. "Tap letters and sight words to turn them on or off. Tap Close to go back."
   is a how-to: five opens spoke it 5 of 5 (`v2-teacher-repeats`, voiceA.txt). Make it `how`; the privacy line can stay
   on screen and in Read.
3. **should fix** (general). `src.html:817`. A right Find queues `[say (how), intro.<l>]`, so the child hears "Say its
   sound. Tap the lantern to check." and then at once the model "Mmm. M says mmm, like moth." The instruction to say it
   first is answered before the class can try, and "tap to check" is stale by the time the model ends. Spec order is
   intro first, then the turn line ("Your turn. Say its sound out loud. Then tap the lantern to check.", which the
   built text also shortened). Seen: v1 log 32274 `say` spoken, 35830 `intro.m` spoken; v4 and v8c the same.
4. **should fix** (general). `src.html:1514-1515` vs lines `sign` and `twinIntro`. The lines say "Tap each lantern to
   hear it" and "Only one lantern is different. Tap the different lantern", but the screen shows cream letter tiles
   over the sign, not lanterns (spec: lit lanterns hang over the sign's letters). A child who can't read is told to
   find a lantern that isn't there. Seen: `out/L-sign-680x425.png`, `out/L-twins-1366x768.png`. Either hang the small
   awake lantern art (already loaded) over each letter, or say "tile"/"letter".
5. **should fix** (general). `voice/lines.json` `bank: warm-teacher` (Sulafat). The two nearest K neighbors that are
   built, calm-corner and sight-words, also use warm-teacher/Sulafat (checked their lines.json); STANDARDS Variety asks
   for a voice different from the nearest neighbors. The spec named it while noting Sulafat is a neighbor's voice.
   Pick another kept K-friendly voice before the Forge records about 310 lines.
6. **should fix** (general). `notes.md:53` and `:57`. Public teacher notes talk about the pipeline: "the listening review
   described in the build report", "The build is a draft and is not ready for a solo nonreader", "spec.md and
   codex-report.md", "recomputed in Scratch". A teacher can't open those. Replace with the real sources (the spec's
   Sources table, short) and drop the draft sentence once clips land.
7. **should fix** (general). `src.html:199` banner font `'Century Gothic','Trebuchet MS',sans-serif`. Banners are the
   one place words are set in a system font instead of the drawn ball-and-stick glyphs. Where Century Gothic is missing
   (Chromebooks, Macs, many school images) the fallback has a two-story a and g, against the spec's "single-story a and
   g" and against every other word in the tool; "I" also becomes a bare bar like l. Not visible on this PC (Century
   Gothic is installed), so seen by reading the stack. Draw banners with the fixed glyph layout from finding 1.
8. **polish** (general). `src.html:189` vs `kit/curio.css:11`. The "different lantern" marker on twins is `outline:4px
   solid #7fe3ff`, the exact kit focus ring. One look means two things: a keyboard user can't tell focus from the
   answer, and a class sees what looks like a selection. Seen: `out/L-twins-1366x768.png`. Better: the spec's flicker,
   or an amber glow plus a small mark, distinct from focus.
9. **polish** (general). Twins at 680x425 and 800x500: the sound-tile row sits on top of the "Find what changed" label
   and crowds the "9 lit" chip (`out/L-twins-680x425.png`, `out/K-focus-sign-680.png`). The audit did not list the
   twins state, so it never saw this. Move the label (as `.signing` already does for Sign) or drop it on short boxes.
10. **polish** (general). `src.html:195-197`. Long/short boards show the two flames as plain CSS blobs (a cream rounded
    slab and an orange oval) floating above the banners, with no vowel lantern over each as the spec says; next to the
    painted art they read as placeholders (BASELINE rule 3). Seen: `out/L-long-1366x768.png`, `out/L-long-680x425.png`.
    Better: the vowel's awake lantern over each board with the same short/tall flame shapes used in the flames step.
11. **nit** (general). `src.html:1840`. Sound back on calls `narrateStep()`, so every Sound off/on re-speaks the current
    question (v8d: `find.m` spoken again). The kit rule is the welcome only if never said; repeating the question is
    arguably helpful, so optional.
12. **nit** (general). `listenLantern`, `listenBanner`, `listenSign`, `listenWord` are in lines.json (so they would be
    recorded) but are never spoken: Read speaks `hintSpoken` (the real question). Mark them hint-only or drop them from
    the recording list.
13. **nit** (general). 2.93 MB, over the 2 MB goal (art 2.58 MB as base64; `lesson.json` `paths` is 248 KB of
    pre-sampled stroke points that could be built at load from the spec's stroke formulas). About 300 recorded clips
    still to come will likely pass 6 MB: plan the `Size:` line in notes.md now.
14. **nit** (general). `src.html:1631`. On the first screen "Hear it again" shows disabled at half opacity; a dead
    button on the first screen of a K tool. Hide it until there is something to hear.
15. **nit** (general). spec.md Art says "All local FLUX"; prompts.json says every image was drawn by Codex with OpenAI
    gpt-image. The art is fine; the spec line is out of date.

No cultural, Native or hard-history content: no sensitivity review needed from this lens.

## Standard voice check

Held clicks (0.12 s), Sound and Motion on, 1366x768 (1920x1080 for the check run), log from `__tool.vlog`.

| line | kind | action | expected | spoken |
|---|---|---|---|---|
| welcome | how | Wake the village, then a wrong tap at 5 s | 1 (a cut is fine, rule 16) | 1 (cut by the tap) |
| find.m | event | 5 wrong taps | 5 | 5 |
| wrong.s | event | 5 wrong taps | 5 | 5 |
| say | how | right Find | 1 | 1 (but before intro, finding 3) |
| intro.m | event | right Find | 1 | 1 |
| sound.m | event | 5 taps in Say | 5 | 5 |
| teacher | how-to text, queued as event | 5 Teacher opens | 1 | **5** (finding 2) |
| twinSame | how, once per pair | 5 taps on a shared tile | 1 | 1 (4 silent) |
| twinDiff.1, then twinWhich.1 | event | different tile | 1 each | 1 each |
| word.cat + twinWhich.1 | event | 3 wrong sign picks | 3 each | 3 each |
| yes | event | right sign; 6 check finds; 2 banner finds | 1; 6; 2 | 1; 6; 2 |
| missStart | how, once per stroke per cause | 2 misses on stroke 1, 2 on stroke 2 | 1 + 1 | 1 + 1 (silent after) |
| together | once per letter | third miss on two strokes | 1 | 1 (silent second time) |
| checkIntro | event | 2 Lantern checks | 2 | 2 |
| find.x (check) | event | 6 check finds | 6 | 6 |
| seeSay | how | 2 checks | 1 | 1 (silent second) |
| bannerFind.x | event | 2 checks | 2 | 2 |
| village | how | Wake all, 2 returns from check | 1 | 1 (silent after) |

- Stale lines (v6: taps 0.25 s apart on Wake the village, s, a, s, then Village, then Wake): each wrong line cut by
  the next tap, Village welcome cut by Wake, then `find.m` for the step on screen. Nothing played after its moment.
- First tap: stage background tap, welcome at +133 ms then the start line; Tab key, welcome at +17 ms. Read, Sound,
  lanterns, Teacher, mode buttons: audit rows, confirmed in my logs where I touched them (Read speaks the hint only;
  a lantern speaks only its own line).
- Read: Read during the welcome cut it and spoke the question; a wrong tap 1.2 s later waited for Read and played after
  it (v8a); Read with Sound off spoke (v8d); a mode change right after Read started the Village welcome at once (v8b).
- Order: lines followed the actions in every run.

## Audit pilot

- Leads confirmed: welcome not heard after a first tap on Teacher or a cart lantern (true, and fine under rule 16:
  the premise is not needed later, and Wake the village still plays it); two quick taps cut a mode welcome (rule 16,
  not reported).
- Leads wrong: "#begin Wake the village: welcome not heard". It is heard: `start()` queues it as a `how` line inside
  its own sequence (v1, v4, v8a logs: `welcome` spoken), so the audit's welcome detector misread it. "Five held
  clicks: #teacher clean" missed that the Teacher how-to is spoken on every open (finding 2).
- Missed: audit-states.json has no flames, twins, long/short, banner or banner-find state, and Sign only at three
  sizes, so the sign glyph layout (finding 1), the twins overlap at 680x425 (finding 9), the focus-colored twin marker
  (finding 8) and the placeholder-looking board flames (finding 10) never appeared in its frames. It also can't see
  line order against the screen (findings 3 and 4).
