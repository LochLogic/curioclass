# Rules Referee handoff

## Cold review, 2026-11-07
The cold reviewer played all twelve replays before reading the source and builder notes.
Updated FIBA references to the current 2026 v1.1 rulebook after checking Articles 24.2, 25.2.1 and 34.2.2.
Clip 8 now keeps the schematic hand clear of the net until 1.0 s, matching the contact zoom and caption.
Clip 10 separates the shortstop at (7,18) from the third baseman; the arrival clocks remain 3.1 s and 3.3 s.
The replay header now shows the actual three-light Escape lock after a correct call, connecting the booth to the reward.
Open-locker speech now belongs to the visible locker-room reveal; short Next/Open locker/library prompts are queued once.
Keep going restores the solved, retry or four-open-locker hint instead of naming disabled call cards or completed lockers.
Read's fixed call labels, key-frame hints, locker hints and spoken citations are now in allLines and the 88-line manifest.
Right-aligned canvas counter backings now align behind their text, and volleyball labels no longer collide on phones.
The net symbol was redrawn twice with imagegen. The first transparent attempt was rejected for residue.
The selected second PNG uses a magenta key, holes and despill through art.py --rekey, retaining the painted style.
Original and rejected art, cold-play logs, recheck scripts and final audit evidence are in Scratch with review- prefixes.
The required free-elimination design still allows every lock to be opened without knowing a rule. This remains a blocker,
not a mastery check, and needs a spec decision. SHAPE.S1 still needs motor practice outside this tool and catalog correction.
See codex-review.md for the final review disposition and evidence, including any mechanical audit leads.

The cold-review audit completed once with 33 leads: 27 intended canvas overlays, four permitted first-locker welcome skips,
and two linked iframe-context failures. All standalone sizes, control walks, repeated taps, Motion off and resize tests were clean.
The audit could not attach to its 375 px iframe; direct drive.py phone checks cover that limitation separately.
No shared audit/kit code was changed. review-before-audit.json records the immutable audited implementation snapshot.
The direct-phone follow-up then found offscreen ending focus. The final change only reduces the phone ending stage
and hides its duplicate sidebar heading; the complete recap, hint and Start over remain available.
Three targeted 375 px rechecks confirm visible focus, the final recap entries and real held-click reset.
review-post-audit.diff records these two CSS rules; the audit was not rerun.

## Original build handoff

Build only. All writes are inside this tool and `_scratch/rules-referee`. No commits or polish round.
The report is deliberately written last because the user explicitly requires stopping when it is written.

## Source map
`src.html` is based on the kit starter and uses kit CSS, sound, motion and Curio.voice.
SPORTS and CLIPS hold the twelve rules and sources. `scene` supplies deterministic meter coordinates.
`fieldGeometry` maps each sport to actual canvas pixels; `draw` layers the generated surfaces, tokens and tools.
`openClip`, `seek`, `makeCall` and `next` own booth state. Persistent HTML controls preserve focus and pointer stability.
The canvas uses ResizeObserver and a bounded device-pixel ratio. Animation state survives resizing.
`symbol` validates the entire keypad order; `updateClock` handles expiry without changing progress.
`window.__tool` exposes the model, pure scene function, actions and narration log for checks.

## Decisions and contradictions
- No explicit open-questions section exists. Followed the spec's defaults: Escape, real-time speed, Sound on and Timer off.
- Current owner instructions require generated art and allow people, overriding older no-art and local-model wording.
  Players remain numbered code tokens for coordinate accuracy; all paintings contain no people.
- The existing older `locker-room` prompt was retained as required. The twelve new assets use the spec's rr names.
- Goal posts moved from y 30.3 and 37.7 to 30.34 and 37.66, keeping the center y 34 and using the real 7.32 m width.
- Current IFAB sources identify 2026/27. The three rules are unchanged in the inspected current text.
- Current WBSC numbering replaces the spec's older Rules 1 and 8: fair ball 5.1.16 b), out at first 5.5.2 a) iii,
  caught fly 5.5.2 a) ii. The numeric section on each student rule card is current.
- FIBA's second-dribble rule has shot and opponent-touch exceptions. The rule card is qualified to this exact play.
- Clip labels use neutral sport and clip numbers, avoiding the answer-revealing titles in the content headings.
- Standing no-guessing guidance conflicts with the explicit four free options, elimination and automatic Key moment.
  A wrong call now requires examining another frame with the tool before another answer can be entered.
  This stops a four-tap answer sweep, but cannot establish unaided mastery under the supplied retry design.
  Locks are presented as completed learning clips. There is no best score or persistent mastery record.
- SHAPE.S1 is a motor-skill standard. This laptop activity directly teaches rule application under S2, and only supports S1.
  No unauthorized catalog edits or extra physical activities were added.
- The two short instructions remain on screen, while sources and full rules appear after the decision.
- Switching into Replay booth pauses the optional Escape timer and returning resumes its remaining time.
- The offside line begins on Red 7 rather than automatically choosing the second-last defender.
- A completed call sheet distinguishes first-try calls from calls made after review; it is not a mastery score.

## Art
Twelve generated paintings, prompts in art/prompts.json, originals in art/raw and WebP products from art.py --rekey only.
The original generation locations and QA contact sheet are in Scratch. No audio recording was made.
`firm-captain` / Alnilam is specified in voice/lines.json; runtime falls back to browser speech until recordings exist.

## Sensitivity
No cultural, religious, hard-history or body-health topic. The sport tokens represent teams without identity assumptions.
No generated people need a representation review. A sports-rules reviewer should check the simplified animations.

## Engine changes wanted
None. No shared kit or engine files were edited.

## Validation evidence
Scratch retains arithmetic, bar-tool bundles and frames, art QA, functional probes, shots and the final mechanical audit.
See codex-report.md for measured results, failed checks and remaining limitations.

## Completed build checks
The single mechanical audit completed with 75 leads. The report groups and answers every lead.
Its snapshot predates the final corrections; pre-audit-src.html, the audit's embedded tool and post-audit.diff remain in Scratch.
Final corrections cover compact targets, caption placement, the room reset, phone action rows and repeated active-mode taps.
Crowded player labels now use leaders without changing token coordinates. The basketball arc has a darker stroke.
Pointer snapping distinguishes level players by both coordinates, including White 4 and Red 9 at the same x position.
The final functional run passed 388 assertions. Real keyboard, jittered drag, half-speed, resize and reload checks passed.
Nine targeted layout states and both rapid mode-tap welcomes passed after the audit. The full audit was not rerun.
Final bundle: 736,209 bytes. Twelve painted assets: 482,974 bytes. Recorded voice: zero bytes.
Scratch/validation-manifest.json records final code hashes and checks. The host file was removed and owned test processes closed.
