# Cereal Ad Questions build handoff

## Structure

`src.html` uses the kit starter's header, kit controls, palette variables and Curio.voice. All activity code is in one readable IIFE.
The three mode containers and every frequent control retain their DOM identities. Only TV paintings, chart bars and day-scene objects rebuild.
The ART table contains each bundled image token once. There are ten named paintings, including two Comet poses.
`paintTV` places paintings over a softly blurred copy so the entire bowl remains visible in unusually wide TVs.
`frame` owns the fifteen-second ad and three-second clip clocks. Motion changes transformations, never elapsed time.
The jingle uses the kit AudioContext with a dedicated, disconnectable bus. No audio was recorded.

## Votes and interruption

`finishedKey` identifies the last completed switch combination. Live switch changes label the current run; its final combination owns the next votes.
Votes during a new run still belong to the previous completed version. New playback and post-play switch changes commit that pair.
Finishing the new run commits any edits made during playback, then starts its fresh poll at zero. Replayed versions replace their earlier poll.
`chartOrder` preserves first-play order despite numeric-looking object keys. The latest count overwrites a version's old bars.
Both vote steppers clamp zero through forty. When a stepper disables under focus, focus moves to its enabled opposite with preventScroll.
Switches and Stop act synchronously. Turning Words on mid-shot waits for the next shot's line. Turning it off cancels speech immediately.
Host events have a not-playing validity guard. Read stops the ad before speaking. Mode switches and resets hush the voice queue.
How-to lines use Curio.voice's heard set, while results, switch announcements, truth cards and hotspot discoveries are events.

## Spec decisions and ambiguities

- There are no explicit open-question choices in this spec.
- The Art section says eleven images but names ten. All ten named assets were generated and used. No extra unnamed image was invented.
- The three-second Words clip cannot contain all five clearly spoken slogans. It plays the opening slogan over the plain bowl for three seconds. The full ad contains all five. This is a reported spec limitation.
- Message part controls use one persistent evidence strip beneath the TV and cards, enabled for the selected card. This keeps all five choices and all sixty-pixel controls visible in compact frames rather than expanding a card over its neighbors.
- The plain-bowl start host line conflicts with the rule that host lines never play during an ad. The plain bowl appears immediately; that start line is not automatically spoken. The big question is an event after voting.
- The family photograph is represented as a family keepsake picture of a house and tree. No people were generated. The store's tiny safety pictogram was removed with the image tool too.
- Pictures-off and Words-off contain no in-ad marketing text. The TV casing retains its fictional-ad label, which is an interface label.
- The Sources timing rounds the loop tail to 0.4 seconds. The exact remainder is 0.454545 seconds. Other supplied contrast values match to rounding.
- Nothing saves votes, discoveries or message selections. The shared kit remembers Motion as required by STANDARDS.md.
- News-reader Rasalgethi and the separate announcer performance are specified in voice/lines.json. Build forbids recording, so the browser fallback is used and does not reproduce those performances.
- The report is written last because the user's explicit instruction requires stopping as soon as it is written.

## Engine changes wanted

- No kit change is required. Optional future kit capability in `kit/curio.js`, Motion initialization and `init` handler: allow an in-memory preference when a spec requests no persistence. This build follows the standing requirement to remember Motion.
- Audit helper improvement, `scripts/audit_tool.py`, `MODES_JS`: recognize `.seg button` inside a navigation region without requiring a header ancestor. The current selector misses this tool's separate mode navigation. Explicit states and manual input checks covered both other modes, but the automatic per-control walk covered the initial mode only.

## Checks and next owner

Scratch is `S:/CurioClass-codex/_scratch/cereal-ad-questions`. All child commands have bounded runtimes.
Muted Chrome uses ports 9970 through 9973; host port 8775. The host is stopped after its frames and host.html removed.
The full seven desktop sizes plus 375-wide iframe were shot once across all three modes. Targeted repairs may have newer frames.
Functional evidence covers all eight fifteen-second combinations, live audio and picture switches, both count bounds, fifteen clips, five truth cards, eighteen hotspots and reset.
See the final report for audit leads and visual evidence. Cold review is next. Build only, no commits and no polish round.

## Final build repairs and audit limits

The one full audit completed with 53 leads. Its initial sizes, Motion off, resize stress and repeated-click voice checks were clean.
Thirty-eight leads concern intentional labels drawn on tappable signs; two concern the background hint behind an open modal; five concern correctly skipped first-tap welcomes.
Five phone counter overlaps and three same-mode welcome cuts were fixed after that audit. No full audit was rerun.
Additional targeted repairs clear the playing badge on Stop, restore hints after Escape, hush stale card welcomes, remove sign-covering checkmarks,
and preserve painting proportions in portrait layouts. Targeted frames and JSON assertions in Scratch document those changes.
The news-reader and announcer recordings, the all-five-lines Words clip conflict, and the unspoken plain-bowl start line remain for owner review.
