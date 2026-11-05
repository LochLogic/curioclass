# Handoff: Me vs the Counter

Build only, 2026-11-03. No commits. No polish round.

## Structure

`src.html` starts from the kit starter. The kit supplies header settings, sound, browser narration and the voice queue.
CSS re-lays the gym and equipment at actual screen dimensions. It does not scale a fixed scene. The controls precede
the scene in the DOM; explicit tab order follows rack, Drop, hand, Again, Slow, paper stepper, chart rows and chart.
The stand's rendered width and left position are calculated from the column height so its claw follows the ball.
The ball's initial center is 14.5 percent down that column, matching the painted claw. `drawCable` reads the mat
and computer bounds on a relayout rather than keeping a fixed cable endpoint. The fair-test caption sits above
the stand so its words remain readable in the small preview.

The `BALLS` table contains the four specified factors. Hit schedules are computed from square root of 3.6 / 9.8,
retaining bounce flights at least 0.25 seconds. `sync` integrates wall time with a speed of one or one-half, so Slow
changes speed immediately. `frame` logs scheduled and actual hit times in `__tool.state.hitLog` and drives counts,
lights, squashes and pitched ticks. Motion off retains the same clock.

`match` is a dynamic program maximizing in-order pairs, then minimizing total absolute time gap. The asymmetric
window is 0.15 seconds early to 0.40 seconds late. Live tap times are already physical seconds, including Slow.
The final one-second recording window uses physical time, so it lasts two wall seconds in Slow.

Each mode retains finished rows in memory. Interrupted trials are discarded. Rows retain at most three class counts.
A paper stepper replaces the current try's count and hides the tap row, because paper tallies have no timestamps.
Paper comparisons use explicit paper wording rather than directing children to rings that are no longer drawn.
Changing a ball while idle clears the current comparison but preserves completed table rows.

`Curio.voice` uses easy-coach / Umbriel in `voice/lines.json`. No audio was recorded, as directed. Browser speech is
the current fallback. All static narration is enumerated by `__tool.allLines`. Token checks, mode scope and hush
drop stale results when a run restarts. `V.heard` guards the one-time sensor explanation.
Paper changes preserve a ball-result line already playing, replace queued obsolete comparisons, and stop an old
comparison if its totals have changed. Read remains protected by the kit.

## Art and open-question decision

Nine new non-person illustrations were made with the built-in image tool. Their full base prompts and revision
instructions are in `art/prompts.json`; originals are in `art/raw`. The drop stands were redrawn after the first
closed image included a yellow ball and the first open image changed the stand into a gauge. The accepted pair
has an empty claw and consistent equipment. All finished assets passed through `scripts/art.py --rekey`.
The old `gym-wall.webp` and its original prompt were preserved; the new full gym image is used in the stage.

Open question: keep the painted tap-hand rather than permanently substituting an icon. This leans toward the spec's
painted hand and BASELINE's better-art preference. The build instruction forbids generated body parts, so that one
asset remains marked `people: true` and referenced by its token, with a tasteful code-drawn hand silhouette in use.
The owner can arrange and review its painting later. There are no generated people or body parts.

## Model notes

Recomputed counts and times match the spec. The bouncy ball's next omitted flight is 0.249577741 seconds; this is
below 0.25 but rounds to 0.250 at three decimal places, rather than the spec's truncated 0.249. Do not round it
before testing the cutoff. The exact specified factors take precedence over rounded factors derived from standards.
The noisy-child statistic in Sources is illustrative; its random distribution and seed are not fully specified.

## Engine changes wanted

None. Shared kit, docs and scripts were not changed.

## Review next

Read the completed codex-report.md for measured results and mechanical audit leads. Check narration by listening
when easy-coach recordings are available, and try the tap-along with a real kindergarten group. This build makes
no claim of classroom observation. Tiny cutout edge specks on the stand may merit a painter's cleanup later.

## Final build checks

The full audit finished with 28 leads; all base sizes, calm mode, resize stress, console and keyboard activation
checks were clean. The report records each lead's disposition. Fixed compact caption/count overlaps, moved the
prediction star out of text flow, and replaced zero-font button words with real icon spans and hidden labels.
Repeated taps on an active mode or the same idle rack ball preserve its current instruction. A quick Drop still
restarts immediately and makes the tap-along line stale, as required. Read is protected from the first-hit hush.
Focused layout probes after repairs are clean at 680, 800, 1000, 1366 and 375 through an iframe. Six quick held-click
pairs passed without cutting their instructions. The original full audit was not repeated after these focused fixes.
