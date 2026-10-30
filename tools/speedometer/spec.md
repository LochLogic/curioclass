# Speedometer

## One idea
A car drives a trip whose position is a formula, and its speedometer needle is the derivative of that formula; you
write your own derivative and it drives a second, ghost needle, so a correct derivative is one whose needle stays
locked to the real one for the whole trip, and a wrong rule shows exactly where the needles split.

## Not like
- motion-graph-match (gr 11, built simulator): you drive and match position, velocity and acceleration graphs. The overlap pass gave graph matching to it; here there is nothing to match by hand: the derivative is a formula you write, checked by a needle, and the graph is only a small position strip with a tangent.
- zoom-to-the-limit (this group): average rates closing in at one point, no rules. Here the rules of differentiation (power, product, quotient, chain, exponential, log, inverse trig) are the work.
- two-trains (gr 8, simulator): constant speeds and meeting times; no changing speed.
- rain-gauge (this group): runs the other way: from a rate to an amount.
- optimization-workshop (this group): uses derivatives to find a best design; here the derivative itself is the thing on the dial.

## Who and how
Grade 12, AP Calculus (The Derivative). Students drive, 25 to 45 minutes. Explore first: Test drive opens with a trip
loaded and `Drive` ready.
Topic line: "the derivative as a rate of change".
Standards: AP-CALC.U2 (2.1 to 2.10: derivative as instantaneous rate, difference quotient, power, sum, product and
quotient rules, sin, cos, eˣ, ln x), AP-CALC.U3 (3.1 to 3.6: chain rule, derivatives of inverse functions and inverse
trig functions; implicit differentiation is not in this tool).
tool.json: driver "students", minutes "25-45", modes ["Test drive", "Needle lock", "Your trip"].

## Screens and modes
Header (kit, 9-12 theme): "Speedometer", small line "The needle is the derivative." Modes `Test drive`,
`Needle lock`, `Your trip`; kit `Motion`, `Sound`, `Read`.

Stage (top to bottom): the road strip: a painted roadside (art: roadside-strip) scrolling slowly behind a painted
asphalt road (art: asphalt-strip, tiled) that scrolls with the car, painted marker posts (art: marker-post) every 10 m
with their distances in code on the blank plates, the car (art: car-side, with two painted wheels, art: car-wheel,
turning in code), and an odometer box "s = 125.0 m" in code. Below it the dashboard, the largest part of the stage: a
round speedometer in a painted chrome bezel (art: gauge-bezel) with the dial drawn in code on its blank face (0 to 160
km/h, ticks every 10, labels every 20; toggle `mph` makes it 0 to 100 mph), the main needle (white) and, in Needle
lock, a ghost needle in `--brand`; a gear light `D` or `R` (R when velocity is negative); a digital readout "v = 20.00
m/s (72.0 km/h)". Beside the dial, a small position strip (s against t, the whole trip) with a dot at the current t and
the tangent line through it (slope = v).

Panel: trip picker (cards), the trip's formula large ("s(t) = 25t - 1.25t² meters, t from 0 to 10 s"), and the time
controls: `Drive`, `Pause`, a time scrubber t (0 to T, step 0.1), `Restart`, speed `x1` / `x2`.

### Test drive (explore, default)
Focus: the speedometer dial and its needle, centered and the largest thing on the stage (about 45 percent of the stage
height); the road strip runs above it and the position strip sits beside it.
- `Drive` plays the trip in real time when T is 20 s or less; longer trips play faster so any drive takes at most
  20 s (a badge shows the playback speed, such as "x2"; the clock and every readout show the trip's own time). `x2`
  halves the playing time. Scrubbing t moves the car, the needle and the tangent together.
- Card "Rate check": at the current t, the difference quotient (s(t + Δt) - s(t)) / Δt for Δt = 1, 0.1, 0.01 s, next
  to the needle's value. Line: "The needle is the limit of these."
- Card "What the needle shows": velocity v(t) = s'(t) in m/s, speed |v|, and acceleration v'(t) as a word ("speeding
  up", "slowing down", "steady") from the signs of v and v'.

### Needle lock (the main task)
Focus: the dial with both needles, the largest thing on the stage, with the scrubber and its split mark directly under
it; the box and `Lock in` sit at the top of the panel.
- A box "v(t) = " for the student's derivative of the current trip. `Lock in` parses it and puts the ghost needle on
  the dial; `Drive` (or scrubbing) moves both needles.
- Lock meter: "Locked for the whole trip" when the formulas agree at every check point; otherwise "Split at t = 4.0 s:
  real 15.00, yours 18.00" with a red mark on the scrubber at the first split, and the car pauses there when driving.
- `Rule hint` names the rule the trip needs ("Chain rule: the inside is t/4.") but never the answer; `Show me` appears
  after two failed locks and writes the derivative with a one-line reason.
- Each trip card gets a lock mark when locked.

### Your trip
Focus: the dial, as in Test drive, once a trip is loaded; before that, the box and `Load trip` at the top of the panel.
- A box "s(t) = ", an end time T (2 to 60 s) and `Load trip`. The tool checks s is defined and finite at every check
  point on [0, T] and that its speed stays under 160 km/h (44.4 m/s), else it says where it fails. Then everything from
  Test drive works, and a Needle lock box is there too, checked against a numerical derivative (symmetric difference
  with step 1e-5) since the tool has no symbolic rules.

## Content
Trips (s in meters, t in seconds; the true derivative used by the checker):
| # | Name | s(t) | T | v(t) | Rule |
|---|---|---|---|---|---|
| 1 | Steady cruise | 20t | 10 | 20 | constant multiple |
| 2 | Pulling away | t² | 12 | 2t | power |
| 3 | Braking | 25t - 1.25t² | 10 | 25 - 2.5t | power, sum |
| 4 | Highway merge | 0.05t³ + 10t | 10 | 0.15t² + 10 | power, sum |
| 5 | Back it up | 6t - t² | 8 | 6 - 2t | power (velocity turns negative after t = 3) |
| 6 | Rolling traffic | 15t + 20 sin(t/4) | 30 | 15 + 5 cos(t/4) | chain, sin |
| 7 | Parking | 100t / (t + 5) | 20 | 500 / (t + 5)² | quotient |
| 8 | Coasting | 400(1 - e^(-t/20)) | 40 | 20e^(-t/20) | chain, exponential |
| 9 | Uphill | 40 ln(1 + t) | 20 | 40 / (1 + t) | ln, chain |
| 10 | On-ramp | 2t√(t + 1) | 15 | 2√(t + 1) + t/√(t + 1) | product, chain |
| 11 | Gentle stop | 40 arctan(t/5) | 20 | 200 / (25 + t²) | inverse trig, chain |
Worked values for checks: trip 3 at t = 10: v = 0, s = 125 m. Trip 4 at t = 5: 13.75 m/s. Trip 5 at t = 4: v = -2 (gear
R, speed 2 m/s). Trip 6 at t = 0: 20 m/s. Trip 7 at t = 5: 5 m/s (18 km/h); rate check 4.5455, 4.9505, 4.9950. Trip 8 at
t = 20: 20/e ≈ 7.358 m/s. Trip 9 at t = 4: 8 m/s. Trip 10 at t = 3: 5.5 m/s; rate check 5.8885, 5.5404, 5.5041.
Trip 11 at t = 5: 4 m/s.
Top speeds: every trip stays on the dial; the fastest is trip 9 at t = 0, 40 m/s = 144 km/h ≈ 89.5 mph.
Unit lines: "1 m/s = 3.6 km/h" and "1 m/s ≈ 2.237 mph". Trip 1: 20 m/s = 72 km/h ≈ 44.7 mph.
Accepted equivalent answers are automatic (checked by values): for trip 7, 500/(t + 5)^2, 500(t+5)^-2 and
(100(t + 5) - 100t)/(t + 5)^2 all lock.

## Interactions in detail
- Parser (the tool's own, small): numbers (decimals), t, + - * / ^, parentheses, implicit multiplication ("2t",
  "3sin(t)", "(t+1)(t-1)"), unary minus, functions sin cos tan exp ln sqrt abs arctan (also "atan"), constants e and pi.
  `^` is right-associative; -t^2 means -(t^2). Errors name the problem: "Missing a closing parenthesis.", "Unknown
  word: snx."; nothing is evaluated with eval().
- Lock check: 61 evenly spaced times on [0, T] plus the trip's special times (t = 3 for trip 5); at each,
  |yours - true| ≤ 1e-6 x max(1, |true|). Points where the student's formula is undefined count as a split ("Your
  formula is undefined at t = 0.").
- Needles: the dial shows speed |v| converted to km/h (or mph); values over the top of the dial pin the needle at the
  stop with "off the dial" in the readout (only a Your trip formula can get there between check points). The gear
  light uses the sign of v. Needle motion eases over 80 ms (none with Motion off).
- Rate check uses the trip formula directly; for t + Δt beyond T it uses the backward quotient and says so.
- Driving: the road and posts scroll so the car stays in view, the roadside scrolls at a third of that speed, and the
  wheel cutouts turn at the car's speed; at negative velocity the car rolls backward with reverse lights (a code glow
  at the car's rear).
- Taps while it plays: during Drive, the scrubber, `Pause`, `x1` / `x2`, `mph`, `Lock in` and the trip cards all act on
  that frame (a new trip stops the drive and loads at once); the needle never waits for the next tick.
- Sound (on as the kit sets it, off with Sound): a soft engine hum whose pitch follows speed (Web Audio), and one click
  when the ghost needle locks. Nothing else.
- Keyboard: the scrubber is a range input (arrows 0.1 s, PageUp/PageDown 1 s); Enter in the v(t) box locks in; Enter
  in the s(t) box loads the trip.
- Mode change: `Curio.stop()`, `V.hush()`. Lock marks per device (localStorage `curio-speedometer`, try/catch),
  `Clear marks`. Your trip's formula is not saved.

## Look
Accent (`--brand`) #c7d2de, chrome silver (dashboard trim and the ghost needle): 11.29:1 on --panel #141b25, 10.70:1 on
--sec-bg #18202b; --brand-ink #10161f on it 11.85:1. No 9-12 math tool uses a neutral accent; motion-graph-match's cyan
is far from it.
Dashboard: the painted chrome bezel with its blank dark face (about #0b0f15); in code on the face: tick marks #a6b3c4,
main needle #f2f2f2 with a red-orange tip #ff7a59 (decorative), ghost needle in the accent with a dashed outline so the
two needles differ by shape, gear light text on #10161f. Road: the painted asphalt and roadside set the scene palette
(dusk greens and greys); post labels #e8edf3 on the posts' blank dark plates (about #1c2129, 13.7:1).

## Art
Local FLUX (`scripts/localart.py`); no people. One style: clean painted illustration, early evening light.
- car-side: "A small rounded mint green hatchback car seen exactly from the side, facing right, windows tinted dark,
  clean painted illustration, plain white background"; 16:9; cutout yes; people no; the car on the road strip (its
  painted wheels are covered by the car-wheel cutouts, placed from two measured points).
- car-wheel: "A single black car tire with a silver five-spoke rim seen straight from the side, clean painted
  illustration, plain white background"; 1:1; cutout yes; people no; used twice over the car's wheels, rotated at the
  car's speed (still with Motion off).
- asphalt-strip: "A straight two-lane asphalt road seen from the side at road level, dark grey asphalt with a
  white edge line, a gravel shoulder in front, clean painted illustration, full frame texture"; 5:1; cutout no; people
  no; tiled side by side and scrolled with the car; lane paint and distance marks stay painted, the 10 m spacing comes
  from the posts.
- roadside-strip: "Gentle green hills with a wooden fence, scattered trees and a few distant farm buildings under an
  early evening sky, wide side view, clean painted illustration"; 4:1; cutout no; people no; behind the road, tiled
  and scrolled at a third of the road's speed.
- marker-post: "A single short white roadside marker post with a blank dark rectangular plate near its top, clean
  painted illustration, plain white background"; 3:4; cutout yes; people no; one every 10 m along the road, with the
  distance in code on the blank plate.
- gauge-bezel: "A round polished chrome car gauge bezel seen straight on, with a smooth blank dark face and a thin
  glass reflection, clean painted illustration, plain white background"; 1:1; cutout yes; people no; the speedometer
  frame; ticks, numbers, needles and the gear light are drawn in code on its blank face.
The dial markings, needles, readouts, position strip, tangent, scrubber marks and preview.svg (two locked needles) are
drawn in code (they are a gauge and a graph that move every frame).

## Voice
`easy-coach` (Umbriel), style "Say in an easy-going, encouraging way, like a relaxed driving instructor." Not used by a
group sibling or 9-12 math neighbor. `Curio.voice`, `scope: () => state.mode`. Cards and readouts are read on screen;
Read speaks the hint.
- drive (how, Test drive welcome; stale on the first Drive or scrub): "Pick a trip and press Drive. The needle shows how fast the position is changing."
- rate (how, first scrub; stale on Drive or a trip change): "The rate check divides a small change in position by a small change in time. The needle is where those numbers head."
- reverse (event, velocity turns negative in trip 5; stale when it turns back or the trip changes): "Velocity went negative. The car is backing up."
- lock (how, Needle lock welcome; stale on the first Lock in): "Type the derivative of this trip in the box, then press Lock in. Your needle should ride with the real one."
- locked (event, a full lock; stale on a new trip): "Locked for the whole trip."
- split (event, a split found; stale on the next Lock in or a new trip): "The needles split. Look at the red mark on the scrubber, then fix your formula and press Lock in."
- own (how, Your trip welcome; stale on the first Load trip): "Type your own trip and an end time, then press Load trip. Keep it under one hundred sixty kilometers per hour."

## Family engine
none. The position strip may use `kit/graphing.js` `Plane` (`g.fn`, `g.trace`, `g.segment` for the tangent); the road
layers and dial are the tool's own.

## Sources
- Derivative as instantaneous rate, difference quotient, power, product, quotient and chain rules, derivatives of sin,
  cos, eˣ, ln x and arctan x: College Board, AP Calculus AB and BC CED (2020), Units 2 and 3,
  https://apcentral.collegeboard.org/courses/ap-calculus-ab ; OpenStax, Calculus Volume 1, 3.1 to 3.9,
  https://openstax.org/books/calculus-volume-1/pages/3-3-differentiation-rules
- Velocity, speed, and backing up as negative velocity: OpenStax, Calculus Volume 1, 3.4 "Derivatives as Rates of
  Change", https://openstax.org/books/calculus-volume-1/pages/3-4-derivatives-as-rates-of-change
- 1 mile = 1609.344 m (so 1 m/s = 2.23694 mph) and 1 km/h = 1/3.6 m/s: NIST SP 811, Appendix B,
  https://www.nist.gov/pml/special-publication-811
- Trips are made up.
- Checks run (Python, numpy, 2026-10-29): every trip's v(t) matches a symmetric difference of s(t) to 2e-8 relative
  over 2,001 times; every worked value and rate check reproduces. Top speeds: trips 1 to 8, 10 and 11 at most 25 m/s
  (90 km/h). The first draft's trip 9, 50 ln(1 + t), started at 50 m/s = 180 km/h (111.8 mph), off its own dial and
  over the 160 km/h limit Your trip enforces; it is now 40 ln(1 + t): 40 m/s = 144 km/h at t = 0, 8 m/s at t = 4.
  Your trip's numerical check (step 1e-5, tolerance 1e-6 relative) on 3t, 30 sin(t/5), 2000 ln(1 + t/50), 0.0002t⁴,
  1000 + 40t and e^(t/6): largest error 1e-9, so true derivatives always lock. t³ with T = 10 reaches 300 m/s
  (refused). Trips 6 and 8 run 30 s and 40 s of trip time, so Drive now compresses any trip to at most 20 s.
- Contrast ratios in Look computed with the WCAG 2.1 formula.

## Done when
1. Trip 3 driven to t = 10 shows v = 0 and the odometer 125.0 m; at t = 0 the dial reads 90 km/h.
2. Trip 7 at t = 5: needle 18 km/h; the rate check shows 4.5455, 4.9505, 4.9950.
3. Needle lock trip 2: "2t" locks; "t" splits at t > 0 with the first split marked (the check at t = 0 agrees).
4. Trip 7 locks for 500/(t+5)^2 and for (100(t+5)-100t)/(t+5)^2.
5. Trip 10 locks for 2sqrt(t+1)+t/sqrt(t+1); "2sqrt(t+1)" alone splits.
6. Trip 5 turns the gear light to R after t = 3 and the car rolls backward; at t = 4 speed reads 2 m/s. Trip 9 at t = 0
   reads 144 km/h, on the dial.
7. Your trip: "t^3" with T = 10 is refused for passing 160 km/h (300 m/s at the end); "3t" with T = 20 loads and
   drives, and "3" locks.
8. Bad input "2(t+1" says a parenthesis is missing; nothing throws.
9. Focus: at 1366x768 and 1000x625 the dial is the largest thing on the stage in every mode; the car's wheels sit on
   the road and turn with it.
10. Tap while it plays: during Drive, dragging the scrubber or pressing `mph` moves the needle on that frame; trip 8
    (40 s of trip time) drives in 20 s or less.
11. How-to lines spoken once each in five actions; "Locked for the whole trip." each lock; dial, road and controls
    visible without scrolling at 1366x768 and 1280x720; dial labels at least 10 px in the 680x425 preview; no network,
    no em dashes.

## Open questions
- speedometer: AP-CALC.U3 also covers implicit differentiation, which a position formula cannot show. Leave it out
  (said in "Who and how"), or add a trip in another tool later?
