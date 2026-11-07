# Codex report: warming-evidence-desk

## Built

Grade 8 MS-ESS3-5 evidence desk with Ask and Argue, four real factor records, five spans, twenty saved answers,
inclusive least squares, 20-year means, eruption brackets, linked year cursors, axis toggles and exact-set comparisons.
Five original paintings are bundled offline. The phone dock mirrors existing questions; phone Compare stays visible.
Build only, no commits or polish round. All intentional repository writes are in this tool and its Scratch area.
Read the required briefs, starter, kit, neighboring implementation and review; bundled both bar tools in scoped mirrors.

## Numbers check

PASS: 53 source-point, slope, mean, eruption and carbon-budget assertions, plus eight independent NOAA checks.
PASS: 26 numerical assertions run at tool load and throw on mismatch. See number-checks.json and numbers.json.
NASA long change 1.103 °C; trends 0.14037, 0.01976, 0.19650 °C/decade. NOAA independently gives 1.0435;
0.12849, 0.00698, 0.18970. All round to the spec. All four temperature brackets match.
Spec corrections: CMIP7 Agung annual maximum is 1963, not 1964; IPCC human estimate ends in 2010-2019,
whereas its observed 1.09 °C ends in 2011-2020. Real series and correct periods are preserved. Details in handoff.md.
Data was pulled in the supplied snapshot on 2026-11-05 and independently processed on 2026-11-06, not freshly downloaded.

## Facts checked

| Student-facing fact or number | Checked source and evidence |
|---|---|
| Every annual temperature value, 1880-2025, and 1951-1980 baseline | NASA GISTEMP v4 J-D column; source hash and nine named point checks |
| Long temperature -0.32 to +0.78; rise 1.10; Early/Pause/Fast +0.14/+0.02/+0.20 per decade | Independent NASA computation, corroborated by NOAA NCEI snapshot |
| CO2 1880-1958 ice core; 1959-2025 air; units ppm | Law Dome CO2spl, MacFarling Meure et al. 2006; NOAA GML Mauna Loa; six named point checks |
| CO2 means 299 to 399, up a third; trends 3.6/7.0/18.4 ppm per decade; smooth through eruptions | Same annual series and independent calculations; all four event windows inspected |
| Solar units at top of air; range; means +0.37 W/m², 0.03 percent; whole swing under 0.2 percent | NRLTSI2 annual, Coddington et al. 2016, LASP LISIRD; computed bounds |
| Solar trends +0.11/-0.07/-0.02; cycle means 1361.11 to 1360.94 | NRLTSI2 least squares and the specified complete-cycle means |
| About 11-year cycles, under 0.1 percent; little recent warming contribution | NRLTSI2 cycle swings 0.6825-1.2389 W/m²; NASA sun-role explainer; IPCC WG1 chapter 2 |
| Haze values, averages 0.007/0.005; early 0.014/0.005; pause 0.004/0.009 | CMIP7 v2.2.1 tau scaled 0.0001, cosine-latitude mean, then annual mean; file attributes checked |
| Four eruption dates 1883/1963/1982/1991, short cooling, El Chichón masking | Smithsonian GVP as named by spec; NOAA GML volcano sheet; USGS Pinatubo; Robock 2000 |
| Next-year differences -0.16/-0.22/+0.06/-0.15 | NASA annual values minus preceding three-year means; NOAA independently -0.13/-0.21/+0.05/-0.12 |
| Haze 0.10 dims a direct beam about 10 percent | Beer-Lambert exp(-0.10)=0.90484; NASA My NASA Data aerosol example |
| Fossil fuels plus cement, 1880-2024, billion tonnes CO2 per year | GCB via OWID World co2/1000; five named source-point checks |
| Fossil means 2.8 to 34.3, 12 times; trends 0.5/4.4/4.7 | Same annual record: means 2.8494/34.2799, ratio 12.03; slopes independently recomputed |
| Burning fell a quarter in 1929-1932 and 5 percent in 2020 without matching temperature dips | GCB: -25.55 and -5.20 percent; NASA temperatures in both intervals |
| Emitted about 2,650 Gt including land; air gained 1,050 Gt or 135 ppm; about 4 in 10 | OWID co2_including_luc sum 2648.904 Gt; NOAA/Law Dome difference times 7.8 = 1051.518 Gt; ratio 0.397 |
| Pollution haze and ocean swings help explain the pause; early drivers mixed | IPCC AR6 WG1 chapter 3.3.1; Wilcox et al. 2013; Hegerl et al. 2018, as in spec |
| CO2 accumulation links fuel burning to long warming; natural drivers insufficient | IPCC AR6 WG1 SPM A.1.3 and chapter 3; NASA solar explainer |
| Human estimate 1.07 °C; observed 1.09; natural drivers -0.1 to +0.1 | IPCC AR6 WG1 SPM A.1.3; corrected endpoint periods are explicit on screen |
| El Niño and La Niña affect global temperature | NOAA Climate.gov ENSO and USGS volcanic-climate discussion, as named in spec |
| No data after a record's actual final year | Source file coverage; 2025 volcanic readout tested as no data |

Source URLs are in notes.md. Each graph uses a published record, including reconstructions, not an attribution simulation. Fits is consistency
within the chosen span, not proof of causation from two lines.

## Break it

PASS: swept all 4,096 legal four-row claim combinations. Exactly one gives 4/4: CO2 long, Sun decades,
Volcanoes decades plus dips, Fossil long. Distribution 0/1/2/3/4 agreements: 2401/1372/294/28/1.
All first-three chips gives 0; every Doesn't fit gives 0; everything drove gives 2; sun drove gives 3;
natural-only gives 0; volcano dips-only gives 3. No best or mastery score exists.
PASS: Compare blocked before claims, scientists absent before reveal, overall choice optional, extra chips penalized,
exclusive Doesn't fit clears alternatives, third evidence evicts the oldest, and live comparisons update correctly.
PASS: all twenty questions can be asked and reopened; repeated same selection adds nothing. Zoom never changes answers.
PASS: 2025 no-data refusal, rapid question replacement, real jittered cursor drag, arrow/Shift-arrow input.
PASS: saved work restores without restoring the reveal. Expired Clear confirmation preserves the work.
Copying after Compare is intentionally possible for revision. Agreement compares claims; it does not certify reasoning.

## Voice walk

Held 120 ms clicks, two-second gaps, Sound on: CO2, Fast, Sun, zero, Volcanoes, Dips, Fossil, Argue,
claims and evidence, Compare. Heard span, zoom, dips, Argue, evidence, agree4, finding, in that order.
The first record tap skips Ask welcome as BASELINE 16 permits. Dips was cut by deliberate mode change;
board was dropped when Argue made it stale. No line was lost after an idle final state.
Side path: Read first, Sun/Early, Sound off, Argue, Sound on. Read kept priority and Argue welcome spoke on re-enable.
Found and fixed repeated Compare evicting a queued finding. After unique per-event keys, both complete sequences
spoke at two-second Compare spacing: agreement, finding, agreement, finding. Logs saved in Scratch.
Scripts contain 13 fixed lines; browser fallback only. No recording service called, no bank-timbre claim made.

## Feel check

Best moment: Sun/Fast draws a nearly flat fitted slope under the sharp temperature rise, then From zero flattens
the solar trace without changing its answer. Compare returns a specific case built from the student's questions.
Flattest moment 1: an early hidden SVG left the selected record blank. Fixed the SVG hidden attribute handling;
the first question now pays off with the real trace, mean bars, answer and stamp together.
Flattest moment 2: a completed argument crowded its evidence into neighboring rows. Reworked four claims into one
row and put scientists' reasons beside the student's choices, preserving every 44-pixel target at laptop size.
Played the Ask-to-Argue path as a student. The pause and eruption exceptions create useful second questions;
this remains an evidence investigation, with no invented score or reward system.
Inspected feel-comparison.jpg beside Beat Lab and both original bar frames. The amber instrument desk, rich icons,
layered surfaces, responsive traces and restrained comparison have a coherent finish; there is no placeholder art.

## Done when

1. PASS: first CO2 tap shows Long run, both averages and the filled cell. fixed-co2 and runtime assertions.
2. PASS: Sun/Fast -0.02 W/m²/decade, temperature +0.20, Doesn't fit. Desktop and real phone keys.
3. PASS: both Pause cards include Doesn't fit and the pollution-haze note. Functional checks and size frames.
4. PASS: four eruption lines and all four requested brackets. Real-hover and calm-dips frames.
5. PASS: Sun From zero flattens the line; answer identical. Functional assertion and phone-controls frame.
6. PASS: real jittered pointer drag to 1992 reads +0.22 °C and haze 0.090. hover-1992.json.
7. PASS: gated reveal, exact scientists' sets give four agreements, no prior scientists' DOM text. Exhaustive sweep.
8. PASS: charts/answer dominate Ask and claim table dominates Argue at 1366x768. Frames inspected.
9. PASS: synchronous state replacement during fades, with no pending animation state. Functional rapid questions.
10. PASS at required 1366/680 cases: controls and Compare visible, compact Board popover and 10+ pixel text.
    Small Argue tables with many evidence candidates scroll, retaining Compare and full-size targets.
11. PASS: how lines once, complete repeated event sequences, privacy text, guarded storage, offline bundle, no em dashes.

## Wave lessons

- Hint and voice: PASS. Hints update synchronously; V.heard selects how lines; Read speaks the current answer or hint.
- Focus and layout: PASS. Stable controls, preventScroll focus, keyboard portal after panel controls, responsive SVG.
- Sizes: PASS for tested Ask controls and laptop argument. Small full evidence tables require explicit table scrolling.
- No giveaways: PASS. No score or answer flags; reveal gated; exact set equality rejects mashing. Open revision is intentional.
- Honest numbers: PASS. Real source coverage, explicit units/baselines, OLS versus means, no extrapolation or fitted attribution.
- Standards: PASS. Students build record-by-span questions and attach their own answers to claims; no unused engine.
- Motion off: PASS. Zero infinite animations; same evidence and results.
- Short choices: PASS at laptop size; LIMIT at small argument sizes with evidence, where the four-row table scrolls.
- Resize mid-animation: PASS. Full audit stress had no exceptions or stuck controls; focus survives dock reparenting.
- Welcome timing: PASS. No welcomeAfter; first tap's own instruction wins; current-mode taps do nothing new.
- Unknown stays unknown: PASS. Unasked cells are dots, empty tray is empty, no extrapolation, scientists absent before Compare.
- One look/one meaning and truthful badges: PASS. Distinct line styles, verdict words/icons, exact-set Same/Different.
- Hint reversibility: PASS. Clear resets hints, readout, saved work and revealed summary; same selection preserves focus.
- No copying words: PASS within this explorer's comparison purpose. Claims require synthesis across spans; later revision is open.

## Audit leads

The one full audit completed in about 29 minutes, within its 40-minute limit, using Chrome 9981 and host 8785.
Original result: 250 leads and 53 frames. Every lead is individually answered in audit-dispositions.md and .json.
100 leads fixed: 65 phone viewport/focus, 1 Clear fit, 2 eruption labels, 7 tick spacing, 1 question wrap,
20 narrow argument height and 4 disappearing-tray focus cases. Focus also returns correctly from scientist links.
150 accepted: 117 expected secondary phone-scroll leads, 25 rear-control occlusions under the opaque Board,
and 8 first-record welcome skips permitted by BASELINE 16. Header coverage while the modal is open is intentional;
its Close control, focus containment and Escape path are tested.
Post-fix targeted probes show no overlap, clipping, small targets, tiny text, hidden short choices or horizontal scroll.
The phone workspace now ends exactly where its opaque dock begins; real native and deep-panel input both pass.
All original audit resize checks, repeat-how checks and quick-tap checks were clean. No runtime exception occurred.
No second full audit was run. The audited pre-fix bundle is retained, and post-frames supersede its affected views.

## Frames looked at

All early, focused, final, voice, targeted, last, persistence, phone and post-repair frames were opened individually
or in labeled contact sheets. All 53 audit frames were reviewed in fourteen labeled sheets; flagged views were
also checked at native size after repair. Focus checks include compact/wide reparenting and a real citation tap.
Sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, actual 375x812 iframe.
Also looked at Motion off, grayscale, keyboard cursors, full twenty-answer argument, zero axis, Board popover,
real 1992 drag, stored-work and expired-clear states. The phone host's favicon-only 404 was fixed in its temporary
host page; final hosted run has zero console errors. Early stale-state screenshot assumptions were replaced by fresh-state checks.

## Art made

Five built-in image-tool paintings, 21,150 bytes total (20.7 KiB), people:false. No redraw was needed.
Raw PNGs in art/raw; WebPs use the required free --rekey pipeline. All five final-size images inspected.
Final bundle: 140,257 bytes (137.0 KiB), well under the 2 MB goal. Recorded voice: 0 KiB.

## Art still to paint

None. The specified five images are made and placed. No people or silhouette stand-ins.

## Engine changes wanted

Optional kit/curio.js Curio.voice.say replace:false for repeated event sequences. Unique per-Compare part keys
work around same-key queue eviction here; no shared file was changed.

## Left open

Conditional sulfur dioxide addition unverified: primary CEDS release and Smith inventory identified, but no paired
annual numerical agreement and matching data-licence check completed. Keep the haze note, as the spec permits.
Small Argue tables with evidence scroll; the initial sixteen claim choices now all fit at 680x425.
Bank voice recordings remain for the later voice stage, as Build forbids recording. No unfinished audit or owned
browser/server remains; assigned ports used here are closed, and temporary host.html is removed.
