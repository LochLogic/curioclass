# Refine, Teaching lens: graph-studio (Curiosity No. 08), round 1

Cold lens, 2026-11-06. Judged against CODEX-CURIOSITY.md and VISION "Curiosities: the second shape", not lesson norms.
Bundle `tools/graph-studio/graph-studio.html` driven with `scripts/drive.py` (port 9411). My shots, frames and JS
probes: `S:/CurioClass-codex-scratch/graph-studio/teaching/shots.json` and `.../teaching/frames/`.
Shared audit: `S:/CurioClass-codex-scratch/graph-studio/audit-r1/audit.md`.

Counts: blocker 0, should fix 4, polish 5, nit 2. Sensitivity flag: 1.

## Standards on the module (anchor math-9-function-notation-and-graphs: F-IF.A, F-IF.B)

| Code | Exercised by something the student does and sees? |
|---|---|
| F-IF.A.1 (function, domain, range) | Partly. Curves show where they exist, x = ... shows a non-function. No domain or range readout, and one domain is drawn wrong (finding 2). |
| F-IF.A.2 (notation, evaluate) | Yes. `f(x) = x^2 - 3x` then `f(4)` prints `f(4) = 4.000`; `g(x)=f(x)+1`, `g(-1)` prints 5.000 (t-fnotation). |
| F-IF.A.3 (sequences as functions, recursive) | No. There is no sequence form, and recursive definitions are refused ("Recursive definitions have no plotted value"). |
| F-IF.B.4 (key features in context) | Features yes (Key points: zeros, turns, intercept, intersections). In context, barely: Key points ignore data and fitted curves. |
| F-IF.B.5 (domain in context) | No activity relates a domain to a quantity. |
| F-IF.B.6 (average rate of change) | Yes, well. Pins on y = x^2 at 1 and 3 read `Δy/Δx = 4.000 · average rate of change` (t-pins). |

## Findings

1. **should fix** · general · findFeatures/roots, src.html:1050-1061 and 1091. Key points miss a zero wherever the
   curve touches the axis without crossing (a double root). `y = (x-1.3)^2` with Key points shows `1 turn (1.300,
   4.930e-32)` and no zero at all (frame `teaching/frames/t-squared-double.png`). The default `y = x^2` finds its zero
   only because a sample lands exactly on x = 0; pan the paper and it goes. A vertex on the x axis is the most common
   grade 9 case, and the readout `4.930e-32` where the student expects 0 is confusing. Better: when a turn's |y| is
   below a tolerance relative to the view, mark it as a zero too and print 0.000. The Manual's "repeated roots can be
   missed" is honest but this is the textbook case, not an edge.

2. **should fix** · general · evaluate `^`, src.html:598. Negative bases with fractional exponents return NaN, so
   `y = x^(1/3)` draws only the right half (probe: `(-8)^(1/3)` evaluates to NaN). The cube root's domain is all real
   numbers; a student exploring domain (F-IF.A.1, the anchor) is shown a wrong one, on an instrument whose Manual says
   "undefined values are left blank", which reads as "undefined here". Better: when the exponent is a literal fraction
   with an odd denominator (or a `cbrt`/odd-root form), take the real root; or at least say in the Manual that x^(1/3)
   is drawn for x >= 0 only and why. (x^0.5 losing its left half, from the spec's first two minutes, is correct.)

3. **should fix** · family:curiosity · module standards. F-IF.A.3 has no activity at all, and F-IF.B.4 "in context" and
   F-IF.B.5 are not really exercised (table above). Rule 2 says a code on the module must be really taught. Options,
   any one per code: a sequence form (`a(n) = 2a(n-1)`, `a(1) = 3`, drawn as dots on integer n with a table), or the
   module lists F-IF.A.3 against another tool; let Key points (or Trace) run on the fitted curve, so "when does the
   Mauna Loa quadratic reach 450 ppm" or the population curve's features are readable in context; a "Things people
   have found" entry on domain in context (the planets data only exist for x > 0; a year axis has no meaning before
   1959 for this series). Spec already notes there is no plan.md and the tool is a second card beside graph-story-lab,
   so moving the code is acceptable.

4. **should fix** · general · Read, spokenEquation, src.html:1698. `/\^2\b/` matches inside `^2.5`, so Read says
   "y equals x squared .5" for `y = x^2.5` (vlog from shot t-read). Scrubbing the exponent with Alt gives exactly these
   decimals, so the spec's own first action produces a spoken equation that is wrong. Better: only match `^2` and
   `^3` when not followed by a digit or a decimal point.

5. **polish** · general · trace tag, src.html:1223. For an ordinary curve the tag reads `Pen 1 · x 3.000 | x 3.000 ·
   y 9.000`: x printed twice. For an `f(x) =` line this is the place to show the notation the anchor teaches:
   `f(3.000) = 9.000`. Better: drop the duplicate parameter for y and x lines; use the function's name when it has one.

6. **polish** · general · Table drawer, src.html:442. The header is `x | x | y` for ordinary curves (t-table), the
   same doubling. Better: two columns `x | y` (or `x | f(x)`) unless the line is polar or parametric.

7. **polish** · general · Data drawer, fit readout. Fitted equations print in centered form, for example
   `y = exp(5.886 + 0.004599 (x − 1992))` (t-co2). The spec's found fact "about 3.0 percent a year" for 1790 to 1860
   (I recomputed 3.02 percent from the counts, 2.995 percent from a log fit) cannot be read from this without
   computing e^0.0299 - 1 by hand. Better: under an exponential fit also print the growth per step of x
   ("× 1.030 per year, 3.0 percent") and for a line its slope with units ("1.672 ppm per year").

8. **polish** · general · Data drawer, R² readout. Line 0.9806, exponential 0.9897 (log), quadratic 0.9995 sit in
   the same slot. The Manual says log-space R² is not comparable, but a grade 9 student comparing fits will read
   0.9897 > 0.9806 as "exponential beats line". The "(log)" mark is small. Better: say it on the readout itself,
   e.g. "R² 0.9897 in log space, not comparable with a line's".

9. **polish** · general · Manual "Things people have found", `(1 + 1/n)^n`. The made ruler for n runs -10 to 10 (t-e),
   where the value reaches only 2.594; the approach to e is not visible unless the student finds the max end cap.
   Better: a Notebook setup or a sentence in that entry ("set n's maximum to 1000").

10. **nit** · general · axis ticks and Key point labels use JavaScript exponent notation (`6.00e+18`,
    `4.915e+17`, frame t-race.png) on an instrument where `e` also means 2.718. Better: `6.00×10^18`.

11. **nit** · general · words. "Travel limits" (the viewing window) and "Ready for ink" are plotter flavour a grade 9
    student will not decode; the Manual explains, so it is optional. "Window" in the Manual heading would help.

## Sensitivity flag (not judged)

Manual "Sources and permissions" and notes.md "Good to know": "early censuses excluded many Indigenous people" and
the linked Censuses of American Indians page. Native content: send to the sensitivity agent (rule 5).

## Done when, tested

- 1 PASS for the open (default `y = x^2`, hint "Drag the 2 up or down.", t-default); frame rate is Craft's.
- 2 Not tested by me; audit state animated-ruler is clean (no exceptions).
- 3 PASS: `f(4) = 4.000`.
- 4 PASS: crossings at 1.0776 and 58.77 (and -0.93711), race setup; my scipy roots 1.07755, 58.7701, -0.937109.
- 5 PASS: line R² 0.9806 (shows as 0.9806, rounds to 0.981), quadratic 0.9995; numpy agrees (0.98056, 0.99948).
- 6 PASS: planets power fit `y = 1.000 x^1.500`, numpy exponent 1.4997.
- 7 PASS: `Δy/Δx = 4.000`.
- 8 PASS: tan(x) and 1/x drawn with breaks, open circle at (0, 1) for sin(x)/x and at (3, 6) for (x^2-9)/(x-3)
  (t-holes.png).
- 9 to 12: Craft and Play; no score, goal, level or finish seen anywhere.

## Facts checked against a second source

All match. NOAA file fetched 2026-11-06: 1959 315.98, 1960 316.91, 1975 331.13, 1990 354.45, 2000 369.71,
2010 390.10, 2020 414.21, 2023 421.08, 2024 424.61, 2025 427.35, and the Maunakea note (Dec 2022 to 4 July 2023).
Census popchange table: 1910 92.23, 1940 132.17, 1970 203.21, 1980 226.55, 2000 281.42, 2020 331.45 (so notes.md's
"corrected" values are right and the spec's are the old ones). NASA individual sheets: Saturn 9.537 AU and 10,755.7
days (29.45 yr), Neptune 30.07 AU and 60,189 days (164.8 yr). Recomputed: 3.0 percent a year 1790-1860, rose petal
rule, sin(x°)/x limit pi/180, 3:2 Lissajous. Every number on screen I checked has a named source and licence in the
Manual and tool.draft.json. No readout that lies apart from findings 1, 2 and 4.

## Audit pilot

- Leads confirmed: none that bear on teaching.
- Leads wrong (for this lens): "hint out of view" in every state is the first-run hint correctly gone after an
  action; "choices cut short by a scroll panel" in the Manual is ordinary drawer scrolling; the hint/plot overlap is
  the hint sitting on the paper by design.
- What it missed: the double-root zero (1), the cube-root domain (2), Read's "x squared .5" (4), the doubled x in
  the trace tag and table (5, 6). All need maths or spoken-text checks it does not do.
