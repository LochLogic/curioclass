# Warming Evidence Desk: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: warming-evidence-desk

#### Built

Grade 8 MS-ESS3-5 evidence desk with Ask and Argue, four real factor records, five spans, twenty saved answers,
inclusive least squares, 20-year means, eruption brackets, linked year cursors, axis toggles and exact-set comparisons.
Five original paintings are bundled offline. The phone dock mirrors existing questions; phone Compare stays visible.
Build only, no commits or polish round. All intentional repository writes are in this tool and its Scratch area.
Read the required briefs, starter, kit, neighboring implementation and review; bundled both bar tools in scoped mirrors.

#### Numbers check

PASS: 53 source-point, slope, mean, eruption and carbon-budget assertions, plus eight independent NOAA checks.
PASS: 26 numerical assertions run at tool load and throw on mismatch. See number-checks.json and numbers.json.
NASA long change 1.103 °C; trends 0.14037, 0.01976, 0.19650 °C/decade. NOAA independently gives 1.0435;
0.12849, 0.00698, 0.18970. All round to the spec. All four temperature brackets match.
Spec corrections: CMIP7 Agung annual maximum is 1963, not 1964; IPCC human estimate ends in 2010-2019,
whereas its observed 1.09 °C ends in 2011-2020. Real series and correct periods are preserved. Details in handoff.md.
Data was pulled in the supplied snapshot on 2026-11-05 and independently processed on 2026-11-06, not freshly downloaded.

#### Facts checked

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

#### Break it

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

#### Voice walk

Held 120 ms clicks, two-second gaps, Sound on: CO2, Fast, Sun, zero, Volcanoes, Dips, Fossil, Argue,
claims and evidence, Compare. Heard span, zoom, dips, Argue, evidence, agree4, finding, in that order.
The first record tap skips Ask welcome as BASELINE 16 permits. Dips was cut by deliberate mode change;
board was dropped when Argue made it stale. No line was lost after an idle final state.
Side path: Read first, Sun/Early, Sound off, Argue, Sound on. Read kept priority and Argue welcome spoke on re-enable.
Found and fixed repeated Compare evicting a queued finding. After unique per-event keys, both complete sequences
spoke at two-second Compare spacing: agreement, finding, agreement, finding. Logs saved in Scratch.
Scripts contain 13 fixed lines; browser fallback only. No recording service called, no bank-timbre claim made.

#### Feel check

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

#### Done when

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

#### Wave lessons

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

#### Audit leads

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

#### Frames looked at

All early, focused, final, voice, targeted, last, persistence, phone and post-repair frames were opened individually
or in labeled contact sheets. All 53 audit frames were reviewed in fourteen labeled sheets; flagged views were
also checked at native size after repair. Focus checks include compact/wide reparenting and a real citation tap.
Sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, actual 375x812 iframe.
Also looked at Motion off, grayscale, keyboard cursors, full twenty-answer argument, zero axis, Board popover,
real 1992 drag, stored-work and expired-clear states. The phone host's favicon-only 404 was fixed in its temporary
host page; final hosted run has zero console errors. Early stale-state screenshot assumptions were replaced by fresh-state checks.

#### Art made

Five built-in image-tool paintings, 21,150 bytes total (20.7 KiB), people:false. No redraw was needed.
Raw PNGs in art/raw; WebPs use the required free --rekey pipeline. All five final-size images inspected.
Final bundle: 140,257 bytes (137.0 KiB), well under the 2 MB goal. Recorded voice: 0 KiB.

#### Art still to paint

None. The specified five images are made and placed. No people or silhouette stand-ins.

#### Engine changes wanted

Optional kit/curio.js Curio.voice.say replace:false for repeated event sequences. Unique per-Compare part keys
work around same-key queue eviction here; no shared file was changed.

#### Left open

Conditional sulfur dioxide addition unverified: primary CEDS release and Smith inventory identified, but no paired
annual numerical agreement and matching data-licence check completed. Keep the haze note, as the spec permits.
Small Argue tables with evidence scroll; the initial sixteen claim choices now all fit at 680x425.
Bank voice recordings remain for the later voice stage, as Build forbids recording. No unfinished audit or owned
browser/server remains; assigned ports used here are closed, and temporary host.html is removed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: warming-evidence-desk

#### Played

Cold Grade 8 solo play and a projected-class view, before reading builder reports, handoff, notes or src.html.
The instrument desk is strong. Sun/Fast followed by From zero is its best moment. Kept the palette, texture and exact charts.

#### Findings fixed

- Should fix, general, phone: next-action hints were below the scroll. The same hint now stays beside Ask or Compare controls; deep selections move focus to the visible matching control. Native input, Read and breakpoint changes verified.
- Should fix, general, compact citations: three Fast rise links were only 41 pixels wide. Explicit 44-pixel minimum verified at every affected size.
- Should fix, general, compact Argue: two records vanished in the evidence-table scroll. Four record columns now expose all student choices at 680, 800 and 1000 pixels; 44-pixel targets retained.
- Should fix, general, Argue privacy: saved claim/evidence choices had no visible device-only notice. Added one by the overall choices.
- Should fix, general, Ask/Argue interpretation: pattern consistency could read as proof, and Same could imply checked evidence. Both limits are now explicit on screen and in notes.
- Should fix, general, voice: already-playing span, solar-axis and eruption instructions could outlast their step. Stop those clips when the student completes or leaves the step; Read keeps priority.
- Should fix, general, volcanic chart: optical-depth transmission omitted the vertical-path assumption. The note now specifies a vertical sunbeam; exp(-0.1) gives 90.48 percent transmitted.
- Polish, general, Argue labels: Different crowded the record name. Compact sans-serif comparison labels fit the available space.
- Polish, general, art/play: redrew the weak facility medallion with clearer plant, cooling tower and coal train; fixed the flattest case-building view without flattening the laptop desk.

#### Findings left

- Blocker, general, Argue/spec conflict: four guesses reveal the scientists; copying the visible chips yields 4/4 with no questions or evidence. Reproduced with native held clicks before the fix and again on the final bundle. The claim-only qualification mitigates the misleading implication, but the cheap path remains.
- The spec explicitly requires optional evidence and live comparison after edits. A reasoning gate or frozen first response would change that spec, which CODEX-REVIEW forbids. This is not a clean teaching gate.

#### Break it

| Check or signal | Cheap attempt and result after fixes |
|---|---|
| Claim agreement | All first chips: 2/4. All three positive chips: 0/4. Every Doesn't fit: 0/4. Extra claims do not help. |
| Exact full match | Independently swept 4,096 legal claim sets: exactly one returns 4/4; distribution 2401/1372/294/28/1 for 0/1/2/3/4. |
| Reveal and revision | Copy-after-reveal or guessing that one set still gives 4/4 without evidence. Blocker left as the explicit spec conflict above. |
| Evidence choices | Empty, irrelevant and contradictory answers do not change agreement; clearly labeled claim comparison. A third selected answer evicts the oldest. |
| Board and question answers | Tapped all twenty combinations; repeated selections add nothing. Board filling is a question log, with no completion score or mastery reward. |
| Axis/readout | Swept zero/zoom and endpoints; answers never change. 1992 gives +0.22 degrees and haze 0.090; 2025 haze says no data. |
| Reset/save | Guarded local storage saves picks, not a best score. No reflection gate assumes a student mistake. |

#### Voice walk

Held 120 ms clicks, two-second gaps, defaults: CO2/Fast, Sun, From zero, Fossil fuels, Volcanoes/Dips, Argue, claims plus own answers, overall answer, Compare. Log settled before capture.
Heard in order: span, zoom, board, dips, argue, evidence, agree4, finding. First record tap may skip Ask welcome under BASELINE 16.

| Line | Kind | Expected | Started |
|---|---|---|---|
| span, zoom, board, dips, argue, evidence | how/welcome | once each | once each |
| agreement, finding, five Compares | event | five each | five each |
Read works with Sound off; switching to Argue then enabling Sound speaks its unsaid welcome. Step-completion cuts are intentional; no outdated axis instruction continues.
Thirteen fixed scripts match allLines. Browser fallback is used; no recordings or bank-timbre verification claimed.

#### Facts checked

Fresh downloads match all 725 bundled annual values, not only the builder's tests. Independent results and SHA-256 hashes: `_scratch/warming-evidence-desk/review-sources/`.

| Fact checked | Named source and result |
|---|---|
| Temperature annual values, 1951-1980 baseline, -0.32 to +0.78, rise 1.10; trends +0.14/+0.02/+0.20 | [NASA GISTEMP v4 J-D](https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv), independently recomputed. |
| CO2 289.8 in 1880, 427.35 in 2025; means 299/399; trends 3.6/7.0/18.4 ppm per decade | [NOAA Law Dome CO2spl](https://www.ncei.noaa.gov/pub/data/paleo/icecore/antarctica/law/law2006.txt), MacFarling Meure et al. 2006, joined to [NOAA Mauna Loa](https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt) at 1959. |
| Solar +0.37 W/m², 0.03 percent; trends +0.11/-0.07/-0.02; whole swing under 0.2 percent | [LASP NRLTSI2 annual record](https://lasp.colorado.edu/lisird/latis/dap/nrl2_tsi_P1Y.csv), independently recomputed. |
| Solar-cycle means 1361.11 to 1360.94; approximate eleven-year cycle; no sustained recent solar rise | NRLTSI2 means for 1976-1986 and 2008-2019; [NASA Sun FAQ](https://science.nasa.gov/climate-change/faq/is-the-sun-causing-global-warming/). Notes now name the averaging windows. |
| Haze annual values and six span means; eruption peaks | [NASA GISS CMIP7 v2.2.1](https://data.giss.nasa.gov/modelforce/strataer/data/tau_reff_CMIP7-2-2-1.nc), Aubry/Exeter; independently scaled tau, cosine latitude weighting, annual averaging. Agung's peak is 1963, as the build correctly qualified. |
| Four next-year brackets -0.16/-0.22/+0.06/-0.15 | NASA annual temperatures minus the three pre-eruption years, recomputed independently. |
| Eruption dates, transient cooling and El Chichón/El Niño masking | [Smithsonian GVP Krakatau](https://volcano.si.edu/volcano.cfm?bgvn=1&snum=krakatau&vn=262000), [USGS Pinatubo account](https://pubs.usgs.gov/pinatubo/self/), and [Robock 2000](https://climate.envsci.rutgers.edu/pdf/ROG2000.pdf), Table 1 and sections 5.1/6. |
| Haze 0.10 removes about 10 percent of a vertical direct beam | Beer-Lambert 1-exp(-0.10)=9.516 percent; [NASA aerosol transmission example](https://mynasadata.larc.nasa.gov/sites/default/files/2020-10/Seasonal%20Patterns%20of%20Aerosols.pdf). |
| Fossil/cement means 2.8 to 34.3, twelvefold; trends 0.5/4.4/4.7; drops about 25 and 5 percent | [Global Carbon Budget through OWID](https://github.com/owid/co2-data), World co2/1000. Independent means, OLS and 1929-1932/2019-2020 ratios agree. |
| 2,650 Gt emitted, 1,050 Gt or 135 ppm gained, about four in ten retained | Same GCB co2_including_luc sum 2648.904 Gt; NOAA/Law Dome change times 7.8 =1051.518 Gt; ratio 0.397. |
| Pollution haze/ocean swings in the pause; mixed early drivers; CO2 accumulation links fuels to warming | [IPCC AR6 WG1 chapter 3.3.1](https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-3/), consistent with the record and the spec's Wilcox/Hegerl references. |
| Human 1.07 vs observed 1.09 degrees; natural drivers -0.1 to +0.1 | [IPCC AR6 WG1 SPM A.1.3](https://www.ipcc.ch/report/ar6/wg1/chapter/summary-for-policymakers/). Correct separate endpoints 2010-2019 and 2011-2020 retained. Official indexed text checked; direct PDF fetch returned 403. |
| ENSO also changes global temperature; volcanic cooling may be masked | [NOAA ENSO discussion](https://www.climate.gov/news-features/blogs/enso/can-volcanic-eruptions-cause-el-ni%C3%B1o-maybe-maybe-not), USGS and [Robock 2000, section 5.1](https://climate.envsci.rutgers.edu/pdf/ROG2000.pdf), which separates the obscuring ENSO signal. |
Fits is pattern consistency, not a statistical attribution model. The external IPCC finding supplies the broader physical attribution.

#### Sensitivity

None requiring a cultural judgment: no cultural representations, hard-history activity, bodies or people images. The named Hawaiian observatory is an illustrative measurement site, not a claim about a culture. Climate attribution is collective scientific evidence, not individual blame.

#### Flattest moment left

After comparison, finding useful evidence still asks students to read and discuss. It is deliberately a serious investigation. The original low point, losing half the factors while building a case in compact Argue, is fixed.

#### Graphics

All five paintings inspected at 72, 64, 48 and 28 pixels in `review-art-final-sizes.png`; native tool frames checked too. One consistent editorial gouache set; no people or missing art tokens.
Fossil medallion redrawn with built-in imagegen, prompt in `art/prompts.json`, selected raw in `art/raw/icon-fossil.png`, final `art/icon-fossil.webp`; old image retained in Scratch. Required free `art.py --rekey` pipeline used.
Compared the desk with Beat Lab and Snowy Mail Route frames. Kept the rich desk surfaces, instrument trim, record styles and lamp motion. Art 20.0 KiB; final bundle 140.5 KiB.

#### Audit

One full audit completed within its 40-minute command limit: 30 grouped leads and 59 frames. All frames were inspected in ten labeled contact sheets; the affected views were also opened at native size.
13 leads fixed: six hidden-hint states, six grouped citation-width findings and one deep-phone-focus finding. 17 accepted: specified stacked phone scrolling, intentional Board veil coverage, and eight first-record welcome skips allowed by BASELINE 16. Every lead has its own disposition in `review-audit-dispositions.json` and `.md` in Scratch.
The audit's resize stress, Motion off, focus, repeated-how and quick-tap checks had no runtime failures. No second full audit was run.
Post-repair: all 17 scoped frames inspected; zero driver errors. All compact student choices stay visible before Compare; scientific detail remains scrollable after it. Phone hints stay inside the viewport at every tested state, the workspace ends exactly above the 95-pixel footer, and Read matches the current hint with Sound off.
Spec checks 1-6: first question/means, Sun fast slope, both pause notes, four eruption brackets, axis invariance, and real 1992 readout passed. Check 7 works as written but retains the cheap-path blocker above. Checks 8-11 passed layout, rapid replacement, required folds, once-only how lines, repeated events, local privacy and offline-resource checks.
Wave lessons: stable controls/focus, reversible hints, real-pixel charts, no-data states, distinct monochrome record styles, honest units and Motion off checked. The no-giveaway/cheap-revision issue remains explicitly open rather than counted as a pass.
Final hashes and aggregate checks: `review-final-validation.json`; all owned Chrome/host ports closed and temporary host.html removed.
Contrast ratios: ink/paper 16.05:1, muted/panel 8.39:1, Fits 8.78:1, Partly 8.82:1, No fit 7.82:1.

#### Left open

The evidence/mastery gate conflict above needs a spec decision. No unauthorized gate or extra activity added.
Conditional sulfur-dioxide record remains unverified; retained the explicitly allowed pollution-haze note instead of inventing extra claims or data.
Recorded friendly-dad narration belongs to the later voice stage; this review used the real-time browser fallback with Sound on.
Unattended choices followed the spec and BASELINE; no questions, outreach, deployment or commits. Final report is written only after the audit and scoped repairs, then work stops.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Warming Evidence Desk handoff

#### Cold review changes, 2026-11-06

The cold review keeps the original desk and the wide-screen rows. At short landscape sizes, Argue now has four
record columns with distinct claim and evidence buttons, keeping every student choice visible before Compare.
The right-hand reading panel scrolls its longer finding after Compare; its current hint stays above it.
The scientists' detailed reasons and citation links scroll below the student choices in the compact record cards.
The added audit states cover a full board before and after Compare at 680, 800 and 1000 pixels.
The final audit confirmed hidden phone hints and narrow citation targets. The same hint node now moves to the phone
Ask dock or Compare footer, returning to the panel on larger screens. Both phone footers are 95 pixels tall and the
scrolling workspace ends exactly above them. Deep Ask selections hand focus to the matching visible dock control.
Citation buttons have an explicit 44-pixel minimum width. Compact compared views name the scroll action in the hint.

Ask labels Fits as a pattern fit, not proof. Argue states that Same compares claims only and shows its own device-only
save notice. The comparison label uses a compact sans-serif style so Different fits beside the record name.
Already-playing span, solar-axis and eruption instructions stop when the student's action makes them obsolete.
The fixed voice text is unchanged. Read priority and the shared voice engine are unchanged.

The flattest moment was Argue hiding half the records just as the student tried to assemble a case. All four records
and their gathered answers now stay together. The weakest facility icon was redrawn using built-in OpenAI imagegen,
then processed with art.py --rekey. The prompt is in art/prompts.json, the raw image in art/raw/icon-fossil.png and the
finished asset in art/icon-fossil.webp. The older image is preserved only in Scratch. No people were added.

Fresh downloads from NASA, NOAA, LASP, NASA GISS and GCB/OWID match all 725 annual values. Independent arithmetic and
source hashes are in _scratch/warming-evidence-desk/review-sources/. The existing IPCC endpoint correction is sound.

Spec conflict left for its owner: Compare permits a reveal with four unsupported guesses, then copying the visible
scientists' chips yields four claim matches. This is explicitly required by optional evidence and live revisions in
the spec, while CODEX-REVIEW treats a cheap full-agreement path as a blocker. The on-screen claim-only qualification
reduces the false inference but does not certify evidence reasoning. A mastery or evidence gate needs a spec decision.

The cold review's one full audit completed with 30 grouped leads: 13 fixed and 17 accepted as specified phone scrolling,
intentional modal coverage or BASELINE 16 welcome skips. All 59 audit frames and 17 post-repair frames were inspected.
Native post-repair checks cover phone controls, Read with Sound off, deep focus, breakpoint reparenting and jittered
year-cursor input. All owned Chrome and host ports are closed. Detailed evidence: review-audit-dispositions.json and
review-final-validation.json in Scratch. No second full audit was run.

Original builder context: Build only, no commits or deployment. All scratch work is in _scratch/warming-evidence-desk/.

#### Source map

src.html derives from kit/starter/src.html and uses kit:curio CSS, Curio.init, Curio.voice, Curio.tone and Curio.stop.
No family engine is specified. Responsive SVG draws the exact annual series at actual stage dimensions.
data.json is loaded through the json:data bundle token. The records retain separate end years; no extrapolation occurs.
The four keys are co2, sun, volcano and fossil; temp is the reference record. Five spans produce twenty board cells.
mean and regression recompute averages and inclusive-endpoint least squares. validateNumbers throws on mismatch.
buildControls creates stable buttons once. Updating a selection changes attributes and text, not those button nodes.
ask keeps the other choice, saves only a newly asked cell, and replaces the visible answer synchronously.
drawChart owns paths, bars, axes, trend lines, mean bars, eruption markers and cursor. CSS owns only the optional fade.
No delayed callback can overwrite a more recent question. Pointer input and chart keys use the same whole-year cursor.
toggleClaim implements the exclusive Doesn't fit choice. agreement compares exact sets, including extra-chip penalties.
compare inserts the scientists' content only after every row has a claim. Revisions update the comparison live.
Stored work includes board questions, claims, up to two evidence choices, and the optional overall choice.
Storage loading filters invalid values and deduplicates. Compared state is deliberately not restored.
Clear desk confirms for three seconds and resets both saved work and revealed conclusions.
Curio.voice owns narration and Read, with scope equal to state.mode, explicit validity checks and once-only how lines.
Read speaks the current answer and its note in Ask, otherwise the hint. __tool exposes model and voice logs for review.
Axis-use flags are per record, so trying CO2 From zero does not consume the Sun's separate how-to.
The axis slot stays reserved when its controls are hidden, keeping board targets steady between records.
The initial tray hands focus to the matching record control. Scientist links hand focus back to Ask controls.
The Board dialog has a blocking veil, keyboard containment, Escape/Close and focus return.
Span controls retain focus when responsive layout moves them between the panel and the compact dock.

#### Open questions resolved

- Sulfur dioxide: retain the pollution-haze note. No independently paired annual CEDS and second-inventory series,
  including a checked licence, was validated in this Build. The spec expressly permits this fallback. Its term
  sixth record is inconsistent with the four listed factor records; temperature would make the existing total five.
- Frozen data: use the supplied 2026-11-05 source snapshot, recomputed and checked on 2026-11-06. Preserve the date
  on screen. Refresh with climate-dashboard at the yearly review. No runtime network access is needed.

#### Spec corrections and implementation choices

- The user says to stop when codex-report.md is written. Evidence and a draft report accumulate in Scratch;
  codex-report.md is written once, at the end, instead of the build brief's early-report instruction.
- The requested image tool takes precedence over the Art section's older local-FLUX wording. Five images were
  generated during Build, copied to art/raw, processed only through art.py --rekey and inspected at final size.
- IPCC's human-caused 1.07 °C estimate ends in 2010-2019; the observed 1.09 °C ends in 2011-2020. The reveal labels
  both correctly rather than presenting them as precisely the same period, as the spec does.
- The CMIP7 file matches all specified haze point checks, but Agung peaks at 0.03649 in 1963, not in 1964.
  The requested 1964 value 0.02562 is correct. Eruption dates and all four temperature comparisons remain unchanged.
  Distinct annual eruption maxima rank 1884, 1992, 1963, 1983 in this data. Adjacent post-eruption years must not
  be counted as separate eruptions when ranking the events.
- The Argue welcome omits Then tap Compare because that control begins disabled. The hint names Compare once ready.
- STANDARDS' 44-pixel targets take precedence over the spec's 30-pixel board rows. At short landscape sizes the spans
  move into a dock beneath the charts and Board opens a wider popover. This keeps the chart and primary Ask controls
  usable without shrinking type below 10 pixels.
- At short landscape Argue sizes, all claim and collected-evidence choices fit in four columns; the scientists'
  longer reasons scroll after Compare while the overall answer and Compare stay visible. All candidate chips retain
  44-pixel height. The 375-pixel layout follows the spec's stacked order
  and scrolls vertically inside the workspace; its panel is below the charts and answer. A fixed phone question dock mirrors the same
  record, span and axis controls so primary Ask actions remain in view without compressing the real charts.
  Phone Compare is fixed to the bottom too. These are responsive access to existing actions, not extra activities.
  The workspace ends above this opaque footer, and the header stays visible. Mode changes return the workspace to the top.
- Agreement is a literal comparison of selected claims, not a mastery score. Evidence selection is not graded.
  Copying scientists' claims after Compare is possible and intentional for revision. No best score is stored.
- Browser voice is the fallback. friendly-dad / Achird scripts are complete, but no recordings were made during Build.
  The installed browser voice cannot guarantee the bank voice's timbre until recorded clips are provided.
- The two bar tools were bundled into scoped Scratch mirrors. Their original folders were not written.

#### Sensitivity

No people images, personal disclosure, religion, hard history, Indigenous cultural narratives or body judgements.
This is global environmental science. A reviewer should check that the observatory and industrial paintings read
as illustrations, and that Fits is understood as consistency in one span rather than causal proof from correlation.
Mauna Loa and the eruption names identify source locations, with no claims about local cultures.

#### Art

Five scientific gouache paintings, each marked people:false and drawn_by:codex. Largest finished display is 72 pixels;
the 144-pixel WebP assets provide room for sharp display. The raw selected PNGs stay in art/raw. All five are used.
No missing people assets or stand-ins. Rich chart details remain exact SVG rather than painted approximations.
Prompts and style are in art/prompts.json; final paths are art/icon-co2.webp, art/icon-sun.webp,
art/icon-volcano.webp, art/icon-fossil.webp and art/icon-temp.webp. The built-in image tool was used.

#### Engine changes wanted

Optional: kit/curio.js, Curio.voice.say, add an explicit replace:false option that skips same-key queue replacement
for repeatable event sequences. Two Compare taps two seconds apart otherwise drop the first queued finding line.
This tool works around it with unique per-Compare keys on both parts of each sequence. Shared files were not edited.

#### Original build verification map

Scratch prepare.py and check_numbers.py reproduce the source computations. numbers.json, number-checks.json and
snapshot-provenance.json retain outputs and input hashes. functional.js and functional-results.json cover all 4,096
legal claim-set combinations, the main state rules, axis invariance, evidence FIFO, no-data and reveal gating.
Driver shot files, layout readings, frames, voice logs and the final mechanical audit remain in Scratch.
codex-report.md records the final checks, corrections and any remaining limitations for the cold reviewer.

The one full audit completed in about 29 minutes: 53 frames and 250 leads. audit-dispositions.md and .json answer
each original lead. The pre-fix bundle is preserved as audited-before-layout-fixes.html in Scratch.
Post-audit repairs addressed phone clipping, laptop Clear fit, narrow argument heights, eruption labels, graph ticks
and focus. post-frames and repair-*.json supersede earlier frames in those views. No second full audit was run.
Targeted probes have no overlap, tiny text, small targets or clipping; the open modal intentionally covers the background.
Phone dock and deep panel controls were both driven with real input. Header and footer share a workspace boundary
at y=742 in the 375x812 iframe, so content cannot draw under the fixed dock.
focus-repairs.json verifies focus on span-3 across compact/wide reparenting and a real scientist-link jump back to Ask.
The final exhaustive functional check still permits exactly one full-agreement configuration out of 4,096.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)
