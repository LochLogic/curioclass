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
- Cold review restored a genuine family portrait inside the breakfast frame, marked people:true. The three scenes otherwise retain their painted style.
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
See the final report for audit leads and visual evidence. The cold review is documented in codex-review.md. No commits or additional polish round.

## Final build repairs and audit limits

The one full audit completed with 53 leads. Its initial sizes, Motion off, resize stress and repeated-click voice checks were clean.
Thirty-eight leads concern intentional labels drawn on tappable signs; two concern the background hint behind an open modal; five concern correctly skipped first-tap welcomes.
Five phone counter overlaps and three same-mode welcome cuts were fixed after that audit. No full audit was rerun.
Additional targeted repairs clear the playing badge on Stop, restore hints after Escape, hush stale card welcomes, remove sign-covering checkmarks,
and preserve painting proportions in portrait layouts. Targeted frames and JSON assertions in Scratch document those changes.
The news-reader and announcer recordings, the all-five-lines Words clip conflict, and the unspoken plain-bowl start line remain for owner review.

## Cold review repairs

The first-vote how-to and first plain-bowl question now start immediately, superseding the already-answered vote prompt. The big question repeats on a new completed plain-bowl poll, once per poll. Hotspot narration switches immediately to the selected object; the completion line drops if that object is no longer selected.
The chart highlights the current completed poll and gives a small count/bar response, suppressed with Motion off. Fictional selling copy now appears on the tablet banner, billboard and bus poster. The breakfast family-photo asset has been redrawn and marked people:true in prompts.json.
Source URLs and the corrected 2015 CSPI date are in notes.md. Review evidence uses Chrome 9940-9947 and host 8745, all owned sessions closed after checks.

## Sensitivity

The breakfast keepsake now shows a family with varied skin tones. Review its warmth, representation and clarity at final size; it is one family, not a template for all families. Avoid judging children or families by their food choices or whether an ad changes their opinion. No nutrition or body-health claim is made.

## Review limits needing a spec decision

Five spoken slogans cannot fit a clear three-second Words clip. The existing opening-only clip remains explicit. The day hunt is specified as reveal-on-tap exploration, so sweeping all targets completes the discovery counter without proving ad recognition; adding a prediction gate would change the interaction spec. The plain-bowl artwork also changes rings to flakes as specified, so it does not isolate presentation perfectly.

Additional review repairs: the dense eight-version phone chart uses horizontal bar pairs with readable counts; sparse charts retain their vertical bars. Box text and painting now share one SVG coordinate system, with measured fitting on resize, so lettering stays on the blank panel at 760 wide and during motion. Safety-sign explanations now name their function precisely, matching FHWA and OSHA guidance; voice/lines.json matches.

## Final cold review verification

One review audit completed with 62 raw leads. Its desktop states, Motion off, repeated input and resize checks completed; its phone execution-context discovery failed. Independent drive.py iframe checks cover the phone. The retained audit snapshot predates two narrow corrections: compact final-shot caption headroom and immediate switch-event priority. Focused frames and the final held-click voice walk verify those corrections without another audit.

Review harness limit: the phone audit returned no iframe execution context. Cleanup later discovered seven preview-server children that survived termination of the LibreOffice Python launcher. They were closed by an exact tool/host command match, and every assigned port was verified closed. Whether those surviving servers interfered with the audit host is unverified. Do not infer a tool defect or change Audit.size from this result alone. Independent phone frames and metrics are retained. The scratch preview helper now closes the matched host children as well as its launcher.
