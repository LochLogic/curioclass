# Codex report: blend-bakery
Built by: Antigravity, Gemini 4 Argon, Medium

## Built
- `tools/blend-bakery/src.html`: Complete Grade 1 ELA phonics tool (*Phonics: Blends and Digraphs*, CCSS RF.1.2a-d, RF.1.3a-g) with 2 header modes (`Counters` and `Rush Hour`) and 7 bakery counters (`Digraph Donuts`, `Blend Buns`, `Magic-e Muffins`, `Team Tarts`, `Two-Layer Cakes`, `Ending Eclairs`, `Tricky Treats`), 6 orders per counter (42 orders total).
- `tools/blend-bakery/blend-bakery.html`: Offline bundle (`377 KB`, well under the `2 MB` goal; `2,048 KB - 377 KB = 1,671 KB` headroom).
- `tools/blend-bakery/tool.draft.json`: Draft registry entry (`"stage": "built"`, `"built_by": "antigravity-argon"`, `"driver": "students or teacher"`).
- `tools/blend-bakery/notes.md`: Teacher and parent guide starting with `## What it teaches`, `## Key skills`, and `## Support at home`.
- `tools/blend-bakery/voice/lines.json`: 104 static voice lines configured for `"bank": "upbeat-guide"` (`Zephyr`).
- `tools/blend-bakery/art/prompts.json` and 17 `.webp` assets in `tools/blend-bakery/art/` (`153 KB` total).
- `tools/blend-bakery/audit-states.json` and `tools/blend-bakery/handoff.md`.

## Numbers check
Verified via `_scratch/blend-bakery/verify_numbers.py`:
- WCAG 2.1 contrast ratios:
  - Ink `#2A1219` on paper `#FFF8F6`: `16.69:1` (matches spec `16.69:1`).
  - Muted `#6E4A55` on paper `#FFF8F6`: `6.87:1` (matches spec `6.87:1`).
  - Brand `#A8325E` with white `#FFFFFF`: `6.40:1` (matches spec `6.40:1`).
  - Header button `#882349` with `#E79BB7` border: `6.10:1` (matches spec `6.10:1`).
  - Gold `#F6C94A` with ink `#2A1219`: `11.15:1` (matches spec `11.15:1`).
  - Jar tints (`#FDE8EF`, `#FFF3CC`, `#E3F4FC`, `#E7F6E7`) with ink `#2A1219`: `14.98:1` to `15.80:1`.
- Combinatorics and order counts:
  - 7 counters x 6 orders = 42 orders (`39` unique target words across the 42 orders).
  - Ordered ways per pantry shelf: `6 * 5 * 4 = 120` (6 jars, 3 slots) up to `7 * 6 * 5 * 4 = 840` (7 jars, 4 slots), plus `3` ending choices in `Ending Eclairs` and `3` word boxes in `Tricky Treats`.
  - `Magic-e Muffins`: `3` long-vowel orders (`cape`, `hope`, `kite`) and `3` short-vowel orders (`pin`, `cub`, `tap`).
  - `Ending Eclairs`: `2` `-ed` (`jumped`, `pulled`), `2` `-ing` (`digging`, `baking`), `2` `-s` (`waters`, `sings`).

## Facts checked
- Every word list and phoneme split in `src.html` matches `spec.md` section *Counters and word lists*:
  - Digraphs (`sh`, `ch`, `th`, `wh`, `ck`) are single two-letter phoneme jars (`sh-i-p`, `ch-o-p`, `th-i-n`, `wh-i-p`, `d-u-ck`, `f-i-sh`), whereas consonant blends (`fr`, `st`, `cl`, `dr`, `nd`) are two separate jars side by side (`f-r-o-g`, `s-t-o-p`, `c-l-a-p`, `d-r-u-m`, `n-e-s-t`, `h-a-n-d`).
  - Vowel teams (`ai`, `ay`, `ee`, `ea`, `oa`) are single two-letter vowel team jars (`r-ai-n`, `p-l-ay`, `f-ee-t`, `s-ea-t`, `b-oa-t`, `g-r-ee-n`), with picture disambiguation for homophones (`feet` socks vs `feat` deed; `seat` chair vs `seet`).
  - Two-syllable splits (`rab-bit`, `nap-kin`, `sun-set`, `cup-cake`, `pic-nic`, `muf-fin`) require a vowel jar in each syllable layer (`RF.1.3d`).
  - Inflectional endings (`jumped`, `digging`, `waters`, `pulled`, `baking`, `sings`) teach 1-1-1 doubling (`dig` + `-ing` -> `digging`) and silent-e drop (`bake` + `-ing` -> `baking`) when the oven blends the word, without punishing the student.
  - Irregular words (`said`, `was`, `of`, `come`, `one`, `could`) are chosen by whole-word box comparison (`RF.1.3g`).

## Break it
Tested 8 cheats via `_scratch/blend-bakery/shots-breakit.json` on port 9880:
1. **Blind left-to-right jar tapping (`#jar-0, #jar-1, #jar-2`):** Initially `#jar-0..2` held `ord.jars` in order; fixed by adding deterministic `scramblePantry()` in `src.html` that permutes every pantry and swaps if indices `0..k-1` match `targetSeq`. Retest result: `bakedOk: false, coins: 0, bakedWord: "ais"`.
2. **Spamming `Bake` on an already-solved order (`#bake-btn` x3):** Protected by `state.orderSolved` (`Set` keyed by `mode:counter:order:rushOrders`). Retest result: `coins: 1, streak: 1, solvedCount: 1`.
3. **Skipping all 6 orders with `Next order` without baking (`#next-order-btn` x6):** Protected by `state.counterSolved[counterId]`, which only awards a counter's gold ribbon when all 6 order indices in that counter have been baked. Retest result: `coins: 0, doneCounters: [], solvedCount: 0`.
4. **Wrong tin in `Magic-e Muffins` (`Short Tin` `cap` for `cape`):** Rejected (`bakedOk: false, coins: 0`), prompts `You baked cap. Pick Long Tin for cape!`.
5. **Homophone `feat` for `feet` in `Team Tarts`:** Rejected (`bakedOk: false, coins: 0`), speaks `"That's feat, a big brave deed. I want feet for my socks."` and highlights the middle slot.
6. **Two-Layer Cake syllable without a vowel (`r-b-t` / `b-i-t`):** Rejected before oven slide (`bakedOk: false, coins: 0, diffLayer: 1, diffSlot: 1`), speaks `"Every layer needs a vowel."`.
7. **Wrong inflectional ending in `Ending Eclairs` (`jumps` for `"Yesterday, the frog ___."`):** Rejected (`bakedOk: false, coins: 0`), highlights the ending slot.
8. **Wrong box in `Tricky Treats` (`sad` for `said`):** Rejected (`bakedOk: false, coins: 0`) and resets `state.streak = 0`.

## Voice walk
Walked the main path and side paths at a 2.0 s tap pace with held clicks (`"hold": 0.12`) via `_scratch/blend-bakery/shots-voicewalk.json` (`__tool.vlog`):
- First tap (`#c-digraph`): `welcome` (`"Welcome to Blend Bakery!..."`, `spoken`) -> `cnt:digraph` (`"Digraph Donuts!"`, `spoken`) -> `howDigraph` (`"Some jars hold two letters that make one sound."`, `spoken`) -> `ord:ship` (`"One ship, please!"`).
- Wrong bake (`chip` for `ship`): `"That's a chip. I asked for a ship."` (`spoken`) -> `"Listen to the start of ship."`.
- Correct bake (`ship`): `readIt` (`"Can you read the box?"`, `spoken`) -> `yes:ship` (`"Yum! A ship!"`, `spoken`).
- Switching counters (`#c-muffins`, `#c-tarts`, `#c-cakes`, `#c-eclairs`, `#c-tricky`, `#m-rush`): `V.hush()` cleanly stops prior counter audio and plays each new counter's `how` line once without repeating or nagging.

## Feel check
Compared `_scratch/blend-bakery/frames/digraph-1366x768.png` and `front-1366x768.png` side by side with `_scratch/blend-bakery/frames/feel-snowy-mail-route-1366x768.png`:
- Matches `snowy-mail-route` in card framing, warm palette contrast, character scale, clear bottom shelf strip, and right-hand action panel hierarchy.
- Upgrading customer and Baker Bea art heights (`128px` / `112px`), adding the `Sound Jar Shapes & Colors` guide card on the storefront, and adding tray hood/footer strips made the stage feel full and lively.

## Done when
1. **Criterion 1 (All seven counters playable with six orders each, matching word lists and phoneme splits):** PASS. Verified all 7 counters x 6 orders = 42 orders in `COUNTERS` (`src.html` lines 1268-1371) and tested across `digraph`, `blend`, `muffins`, `tarts`, `cakes`, `eclairs`, and `tricky` frames.
2. **Criterion 2 (Tapping a jar plays its isolated phoneme clip; tapping a filled tray slot returns the jar to the shelf):** PASS. `tapJar()` calls `playPhonemeClip(jar.text)` and fills the next slot; `emptySlot()` returns the jar (`used = false`) and focuses the slot.
3. **Criterion 3 (Digraphs sit in one jar; consonant blends sit in two separate jars):** PASS. Verified in `COUNTERS`: `sh, ch, th, wh, ck` are 1 jar; `f-r, s-t, c-l, d-r, n-d` are 2 separate jars.
4. **Criterion 4 (Magic-e Muffins has 3-slot short tin and 4-slot magic-e tin with dashed arc):** PASS. Verified in `muffins-1366x768.png` and `cheat-4-magic-e-wrong-tin`.
5. **Criterion 5 (Two-Layer Cakes checks each syllable layer has a vowel jar and explains why if not):** PASS. Verified in `cakes-1366x768.png` and `cheat-6-cakes-missing-vowel-syllable` (`diffLayer: 1, diffSlot: 1`, `"Every layer needs a vowel."`).
6. **Criterion 6 (Ending Eclairs shows automatic doubling `digging` and e-drop `baking` with one-line explanation):** PASS. `bakeOrder()` builds `digging` and `baking` automatically and speaks `ruleDoubleG` / `ruleDropE`.
7. **Criterion 7 (Wrong bake keeps matching jars, highlights first differing slot, speaks specific difference):** PASS. `state.diffSlot` applies `.glow-diff` to only the differing slot without clearing matching jars, and speaks `noWord`, `homophoneFeat`, `homophoneSeet`, or the start/middle/end difference.
8. **Criterion 8 (Correct bake shows finished word on box for 3 s with `"Can you read the box?"` before celebrating):** PASS. `bakeOrder()` displays `#baked-box` with `"Can you read the box? (3s...)"` for `3000 ms` before transitioning to `"Yum! ... +1 coin!"`.
9. **Criterion 9 (Rush Hour has Relaxed toggle on by default, and Clear resets saved progress):** PASS. `state.relaxed = true` by default (`#patience-wrap` hidden until toggled off); `#clear-save-btn` resets `localStorage` and counters/best score.
10. **Criterion 10 (Offline bundle works with zero network requests, zero console errors, <= 2 MB, passes STANDARDS.md):** PASS. `blend-bakery.html` is `377 KB` with `0` console/page errors across all `drive.py` shots.

## Wave lessons
- Applied `BASELINE.md` lessons:
  - Kept literal `'art:<name>'` strings in an `ART` lookup map so `scripts/bundle_tool.py` inlines all 17 WebP assets without dynamic template-string misses.
  - Restored keyboard focus (`prevFocusId`) across `renderWork()`, `openCounter()`, `showFront()`, and `emptyAllSlots()` so DOM re-renders and view switches never drop focus to `document.body`.
  - Used singular/plural unit formatting (`1 coin` vs `0 coins`, `1 order` vs `0 orders`, `1 counter` vs `0 counters`).
  - Kept `data-audit-keep` off initially hidden `#work-view` nodes and declared state-specific `keep` regions in `audit-states.json`.

## Audit leads
Ran `scripts/audit_tool.py` on port 9881 (`_scratch/blend-bakery/audit/audit.md`):
- **All 8 viewport sizes (`680x425`, `800x500`, `1000x625`, `1280x720`, `1366x768`, `1920x1080`, `760x900`, `375x812`): `clean`.**
- **`mode Rush Hour`, `digraph-donuts-ship`, `magic-e-muffins`, `Motion off`, `Resized mid-action`: `clean` / `nothing new at any size`.**
- **Leads in `two-layer-cakes` at `680x425` and `375x812`:** `.layer-tag` made `.cake-layer-row` wider than `.tray-card` at `680x425`, and `.customer-stage` made `.bench` + `.cake-trays` touch `#pantry-shelf` at `375x812`.
  - **Action taken:** Hid `.layer-tag` in `body.compact`, tightened `body.compact .bench` side columns to `122px` / `110px`, and hid `.customer-stage` in `body.stack` (`375x812`). Re-bundled and verified in `cakes-680x425-fixed.png` and `cakes-375x812-fixed.png` with zero overlap.

## Frames looked at
- `_scratch/blend-bakery/contact-sheet.png`: All 17 `.webp` art assets on checkerboard (clean edges, no green halo).
- `_scratch/blend-bakery/frames/front-1366x768.png`, `front-680x425.png`, `front-760x900.png`, `host-375x812.png`: Storefront with 7 counters + Rush Hour card, Baker Bea greeting, and jar legend.
- `_scratch/blend-bakery/frames/digraph-1366x768.png`, `digraph-680x425.png`, `digraph-760x900.png`: Digraph Donuts workbench, 3-slot tray, glowing oven with Fresh Baked `ship` box, and `1 coin` singular pill.
- `_scratch/blend-bakery/frames/muffins-1366x768.png`, `cakes-1366x768.png`, `cakes-680x425-fixed.png`, `cakes-375x812-fixed.png`, `eclairs-1366x768.png`, `tricky-1366x768.png`, `grayscale-1366x768.png`: Verified every counter layout and grayscale shape/label distinction.
- `_scratch/blend-bakery/frames/feel-snowy-mail-route-1366x768.png`: Bar-tool comparison frame.

## Art made
- 17 `.webp` files in `tools/blend-bakery/art/` (`bakery.webp`, `bea-stand.webp`, `bea-cheer.webp`, `bea-point.webp`, `bea-think.webp`, `rabbit-happy.webp`, `rabbit-puzzled.webp`, `goat-happy.webp`, `goat-puzzled.webp`, `hedgehog-happy.webp`, `hedgehog-puzzled.webp`, `duck-happy.webp`, `duck-puzzled.webp`, `mouse-happy.webp`, `mouse-puzzled.webp`, `bear-happy.webp`, `bear-puzzled.webp`), all `"people": false`.

## Art still to paint
- None required; optional Gemini image refresh via `python scripts/art.py blend-bakery --force` once API quota resets (`gemini-3.1-flash-image` returned `429 RESOURCE_EXHAUSTED` during build).

## Engine changes wanted
- None.

## Left open
- Voice recordings in `tools/blend-bakery/voice/*.mp3` are ready to generate from `tools/blend-bakery/voice/lines.json` via `python scripts/voice.py blend-bakery` (per `AGY-BUILD.md`, voice recording is not run during build).
