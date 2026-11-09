# Codex build report: class-phone-call

## Summary
- Built `tools/class-phone-call/src.html` and bundled `tools/class-phone-call/index.html` (`675 KB`, well under the `2 MB` ceiling, 0 network requests, offline-ready).
- Implemented the full classroom turn-taking phone call flow with Ranger Sam at Pine Hollow Park across all 6 calls:
  1. **Ring**: ringing classroom speakerphone with pulsing LED, Web Audio ring chime, and `Answer` button.
  2. **Listen and ask**: sentence-by-sentence playback where static eats 3 key details per call (jagged static blank in the caption + animated static sparks around the speakerphone + synthesized Web Audio crackle burst). Students ask out loud and tap one of the 6 always-visible question cards (`Who?`, `What?`, `Where?`, `When?`, `Why?`, `How?`) at the bottom of the stage. Wrong cards trigger `wrongQ[card]`, repeat the crackly line, and pass the turn; after 2 misses on the same gap, the right card wiggles once. Right cards fill the caption blank, stamp a picture + short phrase + question-word badge onto the spiral notepad (`Phone Message Pad`), and pass the turn to the next table group (`Owls`, `Foxes`, `Bears`, `Deer`).
  3. **What does it mean?**: unlocks a 7th gold card (`What does <word> mean?`) when the call's new word is reached (`crew`, `kid`, `habitat`, `trail`, `owlets`, `tracks`) and displays a warm definition badge beside the phone while Ranger Sam explains it.
  4. **Tell me more**: 2 follow-up cards (1 on-topic, 1 off-topic, deterministically ordered `[0, 1]` on odd calls and `[1, 0]` on even calls with positional IDs `#more-card-0` and `#more-card-1`). First tap speaks the card; second tap or `Ask it` asks Ranger Sam. Tapping `Ask it` before choosing a card selects and speaks the first available card rather than submitting unchosen. Off-topic fades the card, clears selection, and passes the turn; on-topic stamps the 4th notepad slot and advances to the Quiz.
  5. **Ranger Sam's Quiz**: 2 comprehension questions per call with 3 picture cards each (deterministically permuted across calls and questions with positional IDs `#quiz-opt-0`..`2` and no DOM answer attributes) while the message pad is hidden. First tap speaks the card; second tap or `This one` submits. Tapping `This one` before choosing a picture selects and speaks the first available picture.
  6. **Take a message (Grade 2)**: 4 numbered boxes (`1` to `4`) over 4 shuffled picture cards (never in `1-2-3-4` order initially). Students tap cards in chronological order and tap `Read the message` (`Skip` also available for K-1). Out-of-order boxes get an amber ring (`msgLook`). All 4 in order transitions to the completed message pad (`4 of 4 in order ✓`) as Ranger Sam reads the full 4-sentence message (`msgRead`) and signs off (`callDone`).

## Option lengths (Tell me more)
- Call 1: On-topic `"Did Mia get her kite back?"` (26 chars) vs Off-topic `"What's your favorite color?"` (27 chars) -> off-topic longer.
- Call 2: On-topic `"What does the baby goat look like?"` (34 chars) vs Off-topic `"Do you have a big red bike at home?"` (35 chars) -> off-topic longer.
- Call 3: On-topic `"Was the turtle big or small?"` (28 chars) vs Off-topic `"Can I have a snack?"` (19 chars) -> on-topic longer.
- Call 4: On-topic `"Was anyone hurt?"` (16 chars) vs Off-topic `"I like pizza with lots of cheese!"` (33 chars) -> off-topic longer.
- Call 5: On-topic `"What do the owlets look like?"` (29 chars) vs Off-topic `"Is it my birthday?"` (18 chars) -> on-topic longer.
- Call 6: On-topic `"Did the fox find food?"` (22 chars) vs Off-topic `"My shoes are new!"` (17 chars) -> on-topic longer.
- Result: On-topic is longer in 3 of 6 calls (50%), off-topic is longer in 3 of 6 calls (50%).

## Art
- Defined all 51 assets in `tools/class-phone-call/art/prompts.json`.
- Painted and processed 25 assets via Google Gemini (`drawn_by: "antigravity"`) and `scripts/art.py class-phone-call --rekey`: `classroom`, `phone`, `notepad`, `owl`, `fox`, `bear`, `deer`, `m1-1`, `m1-2`, `m1-4`, `m2-4`, `m3-3`, `m3-4`, `m4-1`, `m4-2`, `m4-3`, `m4-4`, `m5-2`, `m5-4`, `q-roof`, `q-pond`, `q-moon`, `q-sun`, `q-sandwich`, `q-owlets-1`. All 6 `"people": true` assets (`m1-1`, `m1-4`, `m2-4`, `m3-3`, `m4-4`, `m5-4`) and all 4 table-group medallions (`owl`, `fox`, `bear`, `deer`) are painted in Gemini WebP.
- Remaining 26 picture cards use custom multi-layered SVG illustrations embedded in `src.html` until image model quota resets.

## Art still to paint
- When Gemini image quota resets, generate raw PNGs and run `python scripts/art.py class-phone-call --rekey` for the remaining 26 non-people assets: `m1-3`, `m2-1`, `m2-2`, `m2-3`, `m3-1`, `m3-2`, `m5-1`, `m5-3`, `m6-1`..`m6-4`, `q-kite`, `q-hat`, `q-balloon`, `q-pinetree`, `q-votebox`, `q-namehat`, `q-calendar`, `q-bear`, `q-truck`, `q-owlets-3`, `q-owlets-5`, `q-fox`, `q-deer`, `q-duck`.

## Voice
- Exported all 135 voice lines (`voice/lines.json`) via `python scripts/voice.py class-phone-call --export`.
- Wired `Curio.voice` with `welcomeAfter: true` and `Curio.init({clips: "voice:*", rate: 0.92})`. On Call 1 `Answer`, the queue plays `sentence 1 (gap version) -> welcome -> askHow` in exact spec order.

## Verification
- Verified across `1366x768`, `1920x1080`, `1280x800`, `1280x720`, `1024x768`, `680x425` (embed + `--host`), and `375x812` with `scripts/audit_tool.py` (`0` leads).
