FIX: 1 blocker, 5 should fix, 4 nits. Content, the guess/reveal mechanic, the sensitive-content rules and the voice queue all pass. The problems are Motion off, two scene skies, focus contrast and fit at small sizes.

## Findings

1. **Motion off makes the spotlight flicker** (blocker). src.html:86 `.spot{animation:pulse 2.6s infinite}`. The kit's `.calm *{animation-duration:.01ms}` shortens it but keeps it infinite. With Motion off I sampled the spotlight's opacity on 30 animation frames and got 1, 0.63 and 0.87, changing every frame. With Motion on the same 30 frames gave 29 smooth values. So the setting meant for motion-sensitive students turns a slow pulse into a frame-rate flicker. The spec asks for no spotlight pulse with Motion off. The `.bub` pop is a one-shot and is fine.

2. **Scene skies in Story 1 and Story 3 do not paint** (should fix). src.html:537 and :580: `setting()` writes `<linearGradient id="sky1">` and `id="sky3"`, and `coverArt()` (:733) calls the same function for the shelf covers. The document then holds two `sky1` gradients (checked with `querySelectorAll('[id^=sky]')`: sky1, sky3, sky1). `url(#sky1)` resolves to the first one, which sits inside the hidden shelf, so the story scene's sky rect paints nothing and the flat stage grey `#dfe6ea` shows through. Seen in frames b4char_1366x768 and b4char_760x1000: The Last Goal has a grey sky with a sun where the spec asks for a peach evening sky. The playground is a flat pale grey instead of the grey-blue gradient that preview.svg shows correctly. Covers are unaffected.

3. **Focus ring is invisible on the header buttons** (should fix). src.html:24 `--focus:#1f6f8b`. The kit header background is `--brand #8a5a10`. I computed focus on header at **1.04:1** (needs 3:1). Tabbing to Read shows outline `rgb(31,111,139)` on `rgb(138,90,16)`. The spec's "focus ring on paper 5.22:1" is right (I got 5.22), but the ring on Motion, Sound and Read sits on the header, not on paper. Other ratios, recomputed: ink/paper 14.50, muted/paper 5.85, brand/paper 5.45, white/brand 5.91, ink/bubble 15.75, muted/caption 6.25, brand/panel 5.68, header text 5.68, ink on the three covers 8.23 / 8.61 / 9.11. All of these pass.

4. **Compact layout (the 680x425 and 800x500 preview) hides the Only I know card on page 3** (should fix). src.html:177 `body.compact #acts{order:-1}` puts the 12 chips first. In a character view on page 3 the panel is 498 px tall in a 373 px box. The hint and the secret card fall below the fold, and so do Talk it over, Start over and Stories (top 500 in a 425 viewport). Frames b3guess_680x425 and b3guess_800x500. The spec says the secret is "the first thing a student finds". On page 4 at 680x425 the foot buttons are cut in half (410 to 454 in a 425 viewport, frame b4char_680x425). Back, Next, the rack, the chips, See and the choices are all visible, so Done-when 7 itself holds.

5. **Stack layout at 760 wide puts the chips and choices below the fold** (should fix, STANDARDS "main controls visible at every size"). src.html:970 sets the stage to `clamp(w*.72,240,520)`, which is 520 px at 760 and mostly empty sky. At 760x1000 the choice buttons start at y 1021 (b4char_760x1000) and the chips and See at y 1158 (b3guess_760x1000). At 375 (iframe host) on page 3, See is at 1015 and the choices at 980 in an 812 viewport. At 375 there is no side-by-side option, so scrolling is expected. At 760 a shorter stage would bring the action box up.

6. **Talk it over is cut off at 375 wide** (should fix). src.html:157 `.talk{position:absolute;inset:0;overflow:auto}` sizes the card to the panel. Under the stage on page 1 (Narrator) the panel is only the hint plus the foot, about 180 px tall. Frame h375_talk shows the two questions, then the card ends. The general "You don't have to share it" line and the Close button are hidden in a small inner scroll. Escape still works. Fine at 680x425, 1366x768 and the other sizes.

7. **"You've walked in everyone's shoes" is spoken only once per session, not once per story** (nit). src.html:892 passes `{once: true}`, and `said` (:914) is never cleared. A held-click run (v11) tried all three shoes in The Muddy Sleeve (the line played), then opened The Saved Seat and tried all three: the line never started and `allSaid` stayed `'pending'`. The tracker text still shows in every story, so only the voice is affected. Spec: "shown once per story".

8. **Shift+Tab out of Talk it over lands on a covered button** (nit). src.html:219: the card overlays the panel foot. Shift+Tab from Close focuses `#stories`, and `elementFromPoint` at its center returns the talk card, so the focused control can't be seen.

9. **Spec vs code: Tamsin's page 2 expression** (nit, spec side). The spec lists Tamsin as "nervous" on Story 2 beat 2, but nervous is not one of the six drawn expressions. The code (:290) uses worried, which is the right call. Fix the spec line.

10. **Small things that differ from the spec text** (nit). `choose()` (:870) plays a soft tone that the spec doesn't mention. Read also speaks the Only I know card (:947): the spec says hint then bubble or narration, while notes.md describes the code as built. Neither is harmful. Pick one wording and make the other match.

## Checked and passing

- **Content:** all 115 quoted strings in the spec's Content section appear in the tool word for word, none twice. That covers every beat, thought, secret, choice label, ending, teaser and talk question. Expressions per beat and per ending match the spec (apart from finding 9). The three own-word pairs per story match.
- **Spec behavior** (scripted run over all 3 stories x 4 beats x 4 views x 3 choices, 0 failures):
  - The rack keeps the beat and the secret card shows only in character views.
  - The "?" bubble shows until See or Just show me, and the See label uses the character's name.
  - A third pick replaces the oldest (happy, proud, worried left proud, worried), and a pick toggles off.
  - After a reveal the character stays revealed through Back and through Try another choice.
  - Every ending has its narration and three distinct thoughts.
  - A choice works with the tracker at 0. The tracker never counts Narrator.
  - Start over, Stories and reopening a story all start clean.
  - Next is disabled on pages 4 and 5, Back on page 1.
  - Escape and Close return focus to Talk it over.
- **Keyboard:** Tab reaches the covers, Back, Next, the rack, the 12 chips, See, Just show me and the foot, each with a 4 px solid outline. Keys 1 to 4 and the Left and Right arrows work.
- **Reveal wording:** "You and Juniper both picked worried and frustrated." / "Pip used different words: embarrassed and sorry." Nothing says right or wrong. Matches are bold ink with a brand-color dot (rgb 138,90,16), with no red or green.
- **Sensitive content:**
  - No text input anywhere.
  - Nothing asks the student about themselves. The only personal prompt is the spec's teacher-read general question, which says "You don't have to share it."
  - No scores, timers, stars or end screen.
  - localStorage holds only `curio-motion`. One run also showed `curio-conflict-coach-clean`, written by another tool on the shared file:// origin, not this one.
  - notes.md names the school counselor as the next step.
  - All art is animals drawn in code, with no people and an empty art prompts list.
- **Voice queue** (held clicks, 120 ms, start log):
  - A first tap on a cover plays page 1's narration and skips the shelf welcome, unmarked. A first tap on blank shelf plays the welcome. A first key plays the welcome after the fallback. Read as the first tap speaks the hint and leaves the welcome unmarked.
  - Switching shoes mid-line stops it and starts the new thought within 7 ms.
  - Read then Next, 500 ms later: the next narration starts 2 ms after the click, so hush resolves Read and nothing waits about 10 s.
  - After Read, nothing else starts within 6 s.
  - Sound off: nothing starts through a cover, Next and a shoe. Sound back on at the shelf queues the welcome.
  - On page 3 the thought plays only after See.
- **Lines:** `allLines()` has 156 lines, identical to `voice/lines.json` in the same order. Bank gentle-storyteller (Vindemiatrix), and `voices/gentle-storyteller/ref.wav` exists. Clips are still being recorded (bundle reports none yet), so I did not check them.
- **Contract:**
  - One file of 78 KB. The only URL is the SVG namespace, and the bundle has no external script or link.
  - No console errors or exceptions in about 80 driven shots. The 375 runs showed a favicon 404, but that comes from the host server only.
  - Every button is at least 44 px at every size. Thought bubbles are 18.98 px at 1366x768 and 10.5 px at 680x425, inside the stage at every size.
  - No horizontal scroll at any size: 375, 680, 760, 800, 1000, 1024, 1280, 1366 and 1920.
- **Words:** no em or en dashes in src, notes, spec, tool.draft.json or lines.json, and "Curio" appears only in code (`Curio.*`) or as "Curio Class".

## Re-verify

PASS. All 10 earlier findings are fixed and nothing regressed. Three new nits below; none blocks.

Method: rebuilt with `CURIO_DRAFT=1 python scripts/bundle_tool.py walk-in-their-shoes` (1,736,157 bytes, 1694 KB, under 2 MB), served on 127.0.0.1:8977, headless Chrome `--mute-audio` on devtools 9655, driven over CDP with real key and mouse events. Both are closed.

### Earlier findings, re-checked

1. **Spotlight with Motion off: fixed.** `.calm .spot,.calm #sv.fade,.calm .bub{animation:none!important}` (src.html:96). With Motion off, 30 animation frames of the spotlight gave a single opacity value, 1.000. With Motion on they gave 30 smooth values. With Motion off the spot, the bubble and the scene all compute `animation-name: none`, and Next adds no `fade` class, so scene changes cut.
2. **Scene skies: fixed.** The ids are now unique per call (`sky1-sc`, `sky3-sc`, `sky1-cv-mud`, `sky3-cv-goal`), and the scene rect fills `url(#sky1-sc)`. Frames show The Muddy Sleeve with a grey-blue gradient sky and The Last Goal with a peach evening sky.
3. **Header focus ring: fixed.** `header :focus-visible{outline-color:#fff}`. Motion, Sound and Read now show a 4 px white ring on `#8a5a10`, about 5.9:1. Covers, rack, chips, See, Just show me, choices and the foot buttons keep the 4 px `#1f6f8b` ring on paper.
4. **Compact layout: fixed.** The panel now reads hint, then Only I know, then the action box. At 680x425 on page 3 everything fits inside the 425 px viewport: secret 100-165, chips 179-317, See and Just 321-365, foot 377-421, and Back, Next and the rack end at 420. Page 4: choices 220-360, foot 375-419. 800x500 and 1000x625 (also compact) fit the same way.
5. **760 wide: fixed.** The stage is now `clamp(min(w*.45, h*.34), 220, 400)`. At 760x1000 the two-column panel puts the chips at 672-866 and See and Just at 874-978 on page 3, and the choices at 700-856 on page 4, all above the fold. The page is 1004 px tall on page 3, a 4 px scroll.
6. **Talk it over at 375: fixed, re-shot.** `body.stack .talk{position:fixed;inset:0}`. At 375x812 on page 1 and on page 3, the card fills the window: both questions, the general line (145-209) and Close (229-277) all show (frames b1talk_375x812, b3talk_375x812). The same holds at 760.
7. **All-shoes line once per story: fixed.** `freshStory()` clears it from `said`. With real clips, Story 1 played it after Otto's thought. Then Stories, The Saved Seat and all three shoes played it again after Wren's thought.
8. **Shift+Tab out of Talk: fixed.** Tab and Shift+Tab inside the card both stay on Close (checked at 1366, 680 and 375). Escape and Close return focus to Talk it over. Arrows and 1 to 4 do nothing while the card is open.
9. **Tamsin expression: fixed in the spec** (worried, surprised, worried).
10. **Read and tone wording: fixed.** The spec Voice section now has an "As built" line for both.

### Regression sweep (all pass)

- **Done when 1-6** (scripted, 3 stories x 4 beats x 4 views x 3 choices, 0 failures):
  - All 126 quoted spec strings are present, none twice in the story data. The only misses are the 5 template lines, and their filled forms match.
  - The rack keeps the beat, and the secret card shows only in character views.
  - The "?" bubble holds until See. A third pick replaces the oldest, and a pick toggles off.
  - The hint never says right, wrong or correct. Match marks are brand-colored, never red or green.
  - Back keeps a reveal. Next is disabled on pages 4 and 5.
  - Each of the 9 endings has its narration and 3 distinct thoughts. Try another choice keeps all reveals.
  - Start over, Stories and reopening a story reset everything, and a choice works at tracker 0.
  - No inputs. Only `curio-motion` is in localStorage, with no cookies and no sessionStorage.
- **Sizes** 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000 and 375x812:
  - Every state (shelf, page 1, page 3 guess, page 3 reveal, page 4, page 5, Talk) was shot and looked at.
  - No horizontal scroll anywhere, and no button under 44 px.
  - Thought bubbles stay inside the stage at every size. Bubble text is 10.5 px at 680x425 and 19 px at 1366x768.
  - Back, Next, the rack and the choices are in view at 1366x768, 1280x720 and 680x425. At 375 the page scrolls, as expected.
- **Keyboard:**
  - The shelf tabs Motion, Sound, Read, then the 3 covers, and Enter opens a story.
  - Arrows and keys 1 to 4 work, and a number key focuses the rack button it picks.
  - Story tab order: rack, the 12 chips, See, Just show me, Talk it over, Start over, Stories. On page 4 the 3 choices come before the foot.
- **Voice queue**, with real clips through the page's own `<audio>` (play, playing and ended logged):
  - A first tap on a cover plays page 1's narration with no welcome. A first tap on blank shelf, or a first Tab, plays the welcome. Read as the first tap speaks the hint and leaves the welcome unmarked.
  - Switching shoes 0.8 s into a line pauses it, and the new thought plays within 2 ms.
  - Read then Next 0.5 s later: Next's narration starts at once.
  - Read on its own plays hint, secret and thought back to back, with nothing cut.
  - On page 3 nothing plays until See.
  - Sound off: a shoe, Next and a choice all play nothing.
- **Clips:**
  - All 156 bundled clips match `allLines()` and `voice/lines.json` (156, same order), with none missing or extra.
  - All 156 decode in the browser (`decodeAudioData`) at 16 kbps, 24 kHz, 1.62 to 7.74 s, 615 s in total.
  - Speech rate runs 58 to 106 ms per character, so no clip is truncated or padded. The ones played through the page ended on time.
- **Contract:**
  - No network requests: the resource list is empty, apart from the host's favicon 404.
  - No console errors or exceptions in any run.
  - No em or en dashes in src, notes, spec, tool.draft.json, lines.json or verify.md. "Curio" appears only as code or as "Curio Class".
  - check_tools lists the tool as a draft with no complaints, and notes.md names the school counselor.

### New findings

1. **Print has no print rules** (nit). Printing the 1366 layout to Letter (Chrome printToPDF, story 1 page 3) keeps the pixel-sized scene. The SVG is cut off at the right, along with Pip and the bubble text ("Uh oh. I didn't e..."). The rack shoes overlap and their names truncate to "Na... Ju... Pi... Ot...". The panel prints fine. Nothing in the spec or STANDARDS asks for print, so this is low priority. Suggested fix: an `@media print` block that hides the header buttons, rack and foot, and lets the stage print at a fixed width (or redraws the scene at print width on `beforeprint`).
2. **One clip is much quieter than the rest** (nit). "I kept my promise. So why do I feel bad?" (Rory, Story 2 beat 4) has an RMS of 0.033 and a peak of 0.22, against a median of 0.105 and 0.57: about 10 dB down. The raw source `voice/raw/673086873976.pcm` is just as quiet (0.035), so the 16 kbps re-encode didn't cause it. "I'll just look at my food until lunch is over." is next quietest at 0.047. Suggested fix: loudness-normalize all clips before encoding, or re-record that line.
3. **Focus drops to the page after a choice and after Try another choice** (nit, not a regression). `choose()` and `tryAgain()` re-render and remove the focused button, so `activeElement` becomes `<body>`. After a choice, Chrome's next Tab still lands on Try another choice. After Try another choice, the next Tab lands on Talk it over and skips the new choices, so a keyboard user has to Shift+Tab back. Opening a story with Enter on a cover also leaves focus on `<body>`. Suggested fix: focus `#again` after `choose()`, the first `.choice` after `tryAgain()`, and the Narrator rack button (or Next) after `openStory()`.
