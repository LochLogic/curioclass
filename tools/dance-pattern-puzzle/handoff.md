# Dance Pattern Puzzle: handoff after cold review

## Structure

`src.html` contains the 18 puzzle records, four-attribute maker, responsive festival scene and My dance rules.
`letters`, `patternName`, `challengeFits` and `firstBroken` are separate rule functions exposed through `window.__tool`.
Card buttons and maker controls persist during edits. Navigation rebuilds the strip and deliberately focuses its first blank with preventScroll.
`dance` owns one engine clock, player and music bus. Every interrupt invalidates its run token.
`retime` pauses, changes BPM and resumes at the same fractional count. The shared kit was not edited.

## Painted dancers

The stage, card icons, move buttons and chapter map all use painted dancers.
`art/dancer-cast.webp` is one swappable atlas: three people, each with front, profile and back views.
The cast varies skin tone, age, hair and body build. Its manifest entry carries `people: true` and `drawn_by: codex`.
Full prompt and provenance are in `art/prompts.json`; the generated master is `art/raw/dancer-cast.png`.

`PAINTED_ATLAS`, `CAST_RECTS` and `paintDancer` form the adapter. Source rectangles use the original 1254-pixel master coordinates.
The re-keyed atlas is mapped back into those coordinates with x=15, y=8, width=1225 and height=1240.
The adapter puts painted head, shirt, arm, trouser and shoe pieces over the engine's projected joints.
The engine's original figure shapes are hidden; its skeleton, depth ordering, poses and timing remain in use.
There are three master views per person rather than a separate painting for every combination of move, side, level and facing.
Back views use an actual back painting; profile heads are mirrored only for the opposite profile.
Shoes render after their shin and foreshortened arms retain a readable hand/forearm length.
`actor.paintCast(index)` changes the cast. Chapters cycle through it; My dance uses the tan child.

The fresh sensitivity review passed the cast and placed poses after the kick was clarified.
Evidence: `_scratch/dance-pattern-puzzle/sensitivity.md`, `kick-frames/kick-clear.png` and the targeted review frames.
The original five non-person paintings remain, including the unused water-well image. No existing painting was deleted.

## Review changes

- The card maker and Play stay fixed while occasional settings scroll separately in short landscape views.
- Compact Side and Level share a row. All maker choices remain visible and at least 44 pixels tall.
- Phones show the strip, hint, maker and Play together. The culture card follows the settings on compact views;
  it remains above the strip on larger screens. Read includes its full text in either position.
- Side marks no longer wrap and inflate compact cards. Tinikling uses its numbered cards and tap/tap/close row in short views.
- Preview and completion hold the characteristic movement pose, matching the caption and card.
- A solved finish has a gold stage edge. The low forward kick is lifted enough to read from the front.
- The challenge card reserves its height, so changing its prompt does not shift Clear.
- My dance labels and the count strip count the filled cards that actually play, including after removals.
- Header keyboard focus is white against cobalt. Idle given-card previews preserve a still-relevant spoken introduction.

## Teaching and culture

All four attributes are checked, except that Clap and Jump ignore side.
The two facing-pattern letter displays deliberately ignore facing; answer checking still includes it.
Around the square has no letter labels. Adding-on groups and Seven Jumps round boundaries have thicker borders.

The owner's baseline drops Mayim Mayim. The former puzzle is now a general grapevine pattern exercise.
Seven Jumps is explicitly a short classroom adaptation using knee lifts and kneeling.
Burchenal's 1915 primary text begins with stamps, then knees, elbows and forehead; the tool no longer claims that its knee lifts are that historical sequence.
Tinikling keeps the Philippines attribution, bird connection, three-count pattern and tape/rope classroom alternative.
Tunes are original synthesized music, not traditional melodies. Source links and the adaptation explanation are in notes.md.

Tinikling has nine one-count cards. Its poles close every third count, with the dancer outside.
The solved replay has four passes at base BPM, base+8, base+16 and base+24, capped at 120.
Other cards have two counts. Motion off keeps time and holds each characteristic end pose.

## Voice and storage

`Curio.voice` provides once-only how lines, repeating events, stale-line checks and Read priority.
`voice/lines.json` matches `allLines()` including the revised culture text. Narration uses browser fallback; no recordings were made.
Count-in waits for its spoken line when needed. Lens and Read keep the dance running.
Local storage is guarded, validated and disclosed. Clear confirms, clears the dance and solved dots, and removes the save.

## Verification and remaining scope

Cold play covered every puzzle, wrong answers and My dance before the builder report, handoff and systematic source read.
An early DOM dump accidentally included a source tail; the cold review report records this process slip.
Independent calculations confirm count durations, capped replay timing and the ordinary letter sequences.
Standard-size, phone-host, Motion-off, grayscale, held-click voice, keyboard and targeted pose evidence is in Scratch.
The single final audit completed in 2141.8 seconds with 89 mechanical leads: `_scratch/dance-pattern-puzzle/review-audit/audit.md`.
Final repairs were checked only with targeted frames and held-input logs; no second audit was run.
The cold review report groups every lead and explains expected disabled, hidden and optional-scrolling cases.

The spec's misplaced K-2 codes and overbroad claim that every facing chain returns front need a later spec/catalog correction.
Puzzle 4-2 correctly ends facing back after two left quarter turns. No new K-2 activity was added.
Compact culture text and occasional settings require scrolling; the frequently used strip, maker and Play remain together.

## Engine changes wanted

- `kit/dance.js`, `clock().setBpm`: optionally support immediate fractional retiming. The tool's pause/set/resume workaround works now.
- `kit/dance.js`, `floor().resize`: consider a smaller dancer-height minimum for short scenes. The tool currently adjusts actor scale.

No commits, branch operations or shared source edits were made.
