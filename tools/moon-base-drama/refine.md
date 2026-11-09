OPEN (round 1, Claude Refine 2026-11-05; Codex fixes next)
Counts: blockers 1 (general 1, family 0), should fix 5 (general 5, family 0), polish accepted 7

# Refine: moon-base-drama

Merged from refine/teaching.md, refine/play.md and refine/craft.md. No sensitivity review needed (no cultural, Native
or hard-history content; all three lenses agree). Not a Curiosity. Integrator spot-checks: src.html:390-412 (choice
glyphs), :585-595 and :640-665 (rewind buttons and map), :709-725 (goBeat), :847-853 (radioState).

## Blocker
1. **A rewind past skipped choices plays a story the map contradicts.** src.html:651 (`button.disabled = n >
   state.visited`) with :709-725 (`goBeat`: `invalidateFrom(beat)` moves later choices to `oldChoices`, but
   `state.visited` stays at its maximum). After a full run, Rewind to Batteries, then Rewind to Warmth jumps straight to
   beat 6 with no Batteries or Water choice made. The map still shows the sun-battery and ice icons on those nodes, not
   faded (they are before the current beat), while the meter reads Light 1, Water 1; choosing the blanket ends on "the
   plants are droopy" under a map showing three good choices. Integrator check: the same happens through Back (Back
   from beat 8 to beat 3 also invalidates later choices and leaves `visited` at 8). Seen in teaching
   out/rw-d-jump6-end.png (meter 1,1,3, endLow) and the rw-b/rw-c drive shots. Fixed looks like: whenever choices are
   invalidated (rewind or Back), `state.visited` drops to that beat, so a map button is enabled only for a choice beat
   already reached on the current path; a node with no current choice shows its number or faded old icon, never a
   live-looking old choice before the current beat. This also covers the play nit that Rewind offers Batteries on beat
   3 before any battery choice exists (audit state-rewind-open-1366x768.png): enable a node only once it is behind the
   current beat or has a current choice. Re-run Done when 3 with two rewinds in a row and with Back then Rewind. (general)

## Should fix
1. **A child alone never hears the question or the two choices.** Choice beats 3, 4, 6; src.html:335-336 (choice
   buttons), :469 (`read`). BASELINE rule 4 (defaults work for a solo user) and STANDARDS K-2 ("a narrator voices every
   fixed line"): the question is only on Ada's card (never spoken, by design) and the choice words are never spoken, so
   a pre-reader hears a fact, then "Commander, read your card...", then faces two buttons it cannot read. Seen: audit
   state-batteries-1366x768.png; teaching log v-slow; play finding 3. Fixed looks like: Mission Control voices the two
   crew lines on each choice beat, after the beat's fact line, as the crew's options ("Crew, you could say: Fill the
   batteries now! Or: Wait until dark."), in the shuffled order shown on screen, and Read on an open choice beat speaks
   the beat line plus the options. Ada's card stays unspoken (Done when 4 still holds). New lines go in voice/lines.json
   and `allLines()`. (general)
2. **The night ending barely changes, so "watch the story change" does not land.** Beat 8; src.html:113-115, :657-663.
   The painted greenhouse behind is lush and lit on every ending; the only change is the lamp beam count and a
   `scaleY(.55)` on one foreground planter, which reads as shorter, not wilted, and the two-full and none-full endings
   look the same. "The plants are droopy" plays over a thriving greenhouse. Seen: play/shots/b8-allB.png (1,2,1),
   b8-two.png (3,2,3), audit state-night-1366x768.png (3,3,3), teaching out/rw-d-jump6-end.png. Fixed looks like: each
   meter gap has its own picture, drawn in code: leaves that clearly hang and yellow (not a vertical squash) when Water
   is low, a frost or blue chill tint when Warm is low, the whole scene (background too) darker and desaturated in
   proportion to Light, so a class comparing two runs can point at what changed. Motion off: the end state at once.
   (general)
3. **Choice icons are text glyphs a pre-reader cannot read; the door is an empty box.** src.html:397 "☀ ▣", :399 "☾",
   :403 "≈", :409 "▧", :410 "▯" (only :402 🧊 is a real picture). Seen: play b6-warmA.png, b6-warmB.png,
   b8-map-open.png; craft out/warm-680.png, out/zoom-map-375.png (the two-glyph "☀ ▣" spills out of its 20 px map
   diamond and "▯" renders as an emoji box). Fixed looks like: small drawn SVG icons (battery with a sun, moon, ice
   cube, wave, folded blanket, door), one icon each, the same on the choice button, the map node (fits the diamond) and
   the Rewind dialog; `.choice-icon` and the map dots get `aria-hidden="true"` so screen readers read the words, and
   `#map-strip` gets a role to match its aria-label (craft nit 7). (general)
4. **The premise is lost when the first tap is a job badge, and never comes back.** src.html:467 (welcome valid only
   while no job is checked). The screen invites a badge tap first; then "Teacher, you are Commander Ada" is never
   heard: Sound off and on and Crew re-entry bring nothing, so standard voice check item 3 fails. Mission first gives
   "Tap a job badge" and the welcome is never heard either. Seen: craft log v-job-first-then-sound, play vlog-mf.json,
   audit rows 1 and 5-10. Fixed looks like: a welcome form that stays true once jobs exist (the premise without "Tap a
   job badge"), brought once by Sound on or the next Crew entry, or carried once at Start mission. (general)
5. **The radio glow follows speech synthesis, not Mission Control.** src.html:847-853 (`radioState` uses
   `speechSynthesis.speaking`). `Curio.init({clips:"voice:*"})` plays recorded clips through `Audio` first, so once
   this tool's clips land the radio will never glow while Mission Control talks, and a Read line will not show in the
   caption (spec: "The radio glows only while Mission Control speaks"). Seen: code against kit/curio.js speakOne.
   Fixed looks like: glow and Read caption follow `V.playing` or an active Read, whatever the audio path. (general)

## Polish accepted
1. **Endings: the story line first, then the how-to.** src.html:458 (`guide('reflect', ...)`). The full-success
   ending opens with "Tell Ada which choice helped. Tap Rewind." before "Great work, crew!", and tells a crew that just
   won to rewind. On the three ending lines only, speak the ending line first and the reflect how-to after it, and word
   it for both ways on ("Tap New mission, or Rewind to try another way."). Seen: audit state-night-1366x768.png caption,
   play vlog-full.json, teaching v-five. (general)
2. **Warmth choice A has no referent.** src.html:409: "Wrap it in a blanket" becomes "Wrap the greenhouse in a
   blanket" (button, map, rewind card, lines.json). Seen: play b6-warmA.png. (general)
3. **Ada's card reacts to each result.** src.html:623-624. After a choice the card keeps the question just answered;
   only beat 3 B has a response. Add one short in-role reaction per result on the card (for example "Great work, Rover
   Driver! Bring it home."; for a B result, a nudge toward Rewind like the existing one). Card only, never spoken. Seen:
   play b3-choiceA.png, b4-choiceA.png, b6-warmB.png. (general)
4. **Rewind invites the crew to say the new line their own way.** On a rewound choice beat, Ada's card adds "Say the
   new line in your own words. What will you tell me?" This gives grade 2 TH:Cr3 (adapt dialogue) a real ask. Card only.
   (general)
5. **Teacher notes name what TH:Re9 actually asks.** notes.md "Good to know": name the real asks: choose a prop for
   your job, say how the crew met each moon problem, which choice mattered most and why; Talk about it may add "How did
   the crew act when the doors opened?" (general)
6. **"Back to base" in the Rewind dialog becomes "Back to the story".** src.html:363; "base" is also the Crew screen.
   Seen: play b8-map-open.png. (general)
7. **Crew at 1920x1080: label and subtitle crowding.** The scaled watering can (scale 1.12) touches the "Plant Keeper"
   label and the subtitle "Choose a job. Mime your prop." sits on the first badge's top border. Give both a little
   room; props may also grow inside the large badges. Seen: craft out/zoom-crew-1920.png. (general)

## Settled calls
- Solo child versus teacher in role (teaching 2 "may be a spec question", play 3 should fix): BASELINE rule 4 wins, so
  it is a should fix, and the fix stays inside the spec: voice the crew's two options, never Ada's card. A fuller solo
  path goes to the spec's open questions below.
- Ending picture (teaching polish, play should fix): should fix. It is the Re9 payoff and the picture contradicts the
  spoken ending.
- How-to inside the transmission ahead of the story (play polish 4, teaching nit 7): keep the order on beats 2 to 7.
  It is deliberate (src.html:440-441: a fast Next cannot strand a how-to behind a cut line) and the voice check passes.
  Only the endings change (polish 1), where no fast Next follows.
- Two quick taps cutting a line (audit rows): correct, not a fault. Done when 5 says any tap stops the radio at once;
  job lines are events that replay on the next tap.
- Ada's card toggle and Motion stopping the radio (craft nit 8): to spec ("any tap stops the radio"); Radio again
  recovers the line. Do not change.
- Facts and the 8 meter paths: all three lenses passed them; the on-screen wording ("colder than a home freezer", "no
  air to breathe outside") is a little softer than the spec and still true. Do not change.

## To the spec's open questions
- Should a solo child have a path that does not start with "Teacher, you are Commander Ada" (for example the child plays
  Ada, with the card read aloud in that mode)? Today the spec makes the teacher the commander and never speaks the card.
- Warmth choice B "Open the doors for air" answers a different question than "How do we keep the plants warm?", so it
  reads as a joke more than a misconception (teaching 5, play 5). A warmth idea the radio's facts refute (for example
  "Open the windows to let the Sun in") would teach better, but it changes the spec's content and result line.

## Not taken
- Job badge cannot be unchecked (play nit 9): a repeat tap replaying the job line is useful in class; not worth the change.
- Hint text 11 px at 375 wide (craft nit 6): the radio caption carries the same words at a readable size.
- Droop following Light (teaching 6): the spec ties Light to the lamps; should fix 2 darkens the scene by Light instead.
