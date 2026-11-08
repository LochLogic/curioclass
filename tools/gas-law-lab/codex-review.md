# Codex review: gas-law-lab

## Played

Cold grade 10 play covered the bench, all apparatus and the complete default noisy two-set experiment before builder notes or source. Strong apparatus feedback; the result initially hid its best evidence. Evidence: review-cold/.

## Findings fixed

- Blocker, general, apparatus switching: native Can to Piston selection carried 0.0200 mol past the 0.0100 limit. Destination limits now clamp it; native recheck returned 0.0100.
- Should fix, family:graphing, graph crossing: a Kelvin-axis fit printed 0.0 degrees Celsius; small molar crossings rounded to zero; compact fit text scrolled away. Correct units/precision and the current hint now carry the computed crossing.
- Should fix, general, keyboard: notebook row deletes preceded experiment controls. Controls now come first in DOM order while explicit grid positions preserve the scene.
- Should fix, general, notebook: deleting unrelated bench data destroyed completed guided work. Unrelated rows preserve fits; deleting B preserves valid A.
- Should fix, general, voice: the 60-degree instruction was ambiguous and named disabled Fit line at 1920. Welcome now names the total span and available controls; fitTip supplies the fitting instruction when enabled.
- Should fix, general, voice: compression/stop speech continued after reversal. Those lines now hush; queued fit results also validate the current fit, axes and visible graph. Five-cycle and Read/axis-race rechecks pass.
- Should fix, general, Motion: the drawn piston volume could remain stale through calm heating and jump on resuming. Calm rendering now synchronizes it; a real Motion click preserved exactly the same piston position.
- Should fix, family:particles, Balloon: a pixel-width cap flattened volume growth in the 760-wide portrait view. The base size now reserves room for maximum volume before cube-root scaling, retaining the same largest artwork and correct proportional growth.
- Polish, general, payoff: comparison card covered the convergence. Laptop result card now leaves the common crossing visible; compact card still fits.
- Polish, general, graphics: redrew the fringe-marked can in the existing style with clean alpha, preserved the other ten assets. Removed the empty decorative magnifier when the real particle canvas is hidden in graph focus.
- Should fix, general, scientific framing: result now labels extrapolation and real-gas condensation; the can scene calls 200 kPa a model cutoff. Its compact caption was shortened after the audit confirmed thermometer overlap at 680.

## Findings left

- Should fix, family:particles, upstream engine: required kit engine and family doc are absent and outside the authorized write roots; see Left open and handoff.
- Polish, general, compact notebook: saved-row management still scrolls. These rows are observations, not a hidden set of answer choices.

No unresolved tool-local blocker or should-fix was found in the tested paths.

## Break it

- No points, best score, quiz, or reflection gate. Gate is two qualified data sets and valid Celsius/volume fits.
- Repeated Record 20 times: one temperature, no progress. Four settings across 3 degrees: no progress; hint names the remaining 57-degree gap.
- Kelvin fit: cannot advance the guided step. Vertical/flat data: no false line. All 15 graph-axis combinations returned a finite fit or a truthful no-line result.
- Unchanged B and two-factor B: cannot finish. Exact valid B at double amount: slope doubles, both crossings -273.15 C.
- A deleted required row invalidates the result. Unrelated bench deletion preserves it; B deletion returns to B with A intact.
- Warm-up Record rhythm across almost 99 degrees with only two bath settings: blocked. A whole-pixel jittered real slider sweep stops the can bath at 80 C, never exceeding 200 kPa.
- Can Pump at 0.016 mol/100 C refused, remains 198.56 kPa. Can 0.017 mol bath clamps to 80 C below 200 kPa. Valve stops at 0.001 mol; piston at 300 mL raises pressure.
- Energy example rechecked in browser: lift 7.267793 mm, weights 0.356363514 J. Picture hits remain labeled picture-only; bars have fixed apparatus scales and signed lift values.
- Balloon width at sea level versus 5,000 m: the 760-wide cap gave a false 1.0160 ratio; fixed ratio is 1.233259, matching the cube root of the volume ratio. The 680 and 1366 checks match too.
- 100 seeded UI fits: none outside 8 C. Independent 291,840 extreme-error cases over 1,140 layouts: largest error 7.553798 C. This is finite evidence, not proof for all possible layouts.

## Voice walk

Held 120 ms clicks, 2 s gaps, Sound and Motion on, default Real lab. Main path: Absolute zero, Ice/Record, Room/Record, Hot/Record, Boiling/Record, Notebook/Fit, Pump, repeat four settings, Notebook/Fit. Heard wZero, fitTip, zero, second, zero, in that order.
Latest checked noisy crossings: -273.8949 and -273.0913 C. The final audit-fix recheck preserved all five spoken lines. Bench/side paths also covered welcome, weight, can refusal and piston stop.

| Line | Kind | Expected starts | Observed |
| --- | --- | --- | --- |
| wZero / fitTip / second | welcome/how | 1 each per main walk | 1 each |
| zero | event | 2 main; 5 repeated fits | 2; 5 |
| weightTip | how | 1 across five actions | 1; hushed on reversal |
| canStop / stop | event | 5 each | 5 each |

First taps on stage, weight, mode, Read, Sound and keyboard behaved correctly. Read interrupted speech and worked with Sound off; rapid mode/reset dropped stale lines. No recorded clips exist; these are browser-fallback start/timing checks.

## Facts checked

- PV=nRT, Kelvin offset, fixed-pressure volume, fixed-volume pressure, extrapolation and condensation: [OpenStax Chemistry 2e 9.2](https://openstax.org/books/chemistry-2e/pages/9-2-relating-pressure-volume-amount-and-temperature-the-ideal-gas-law).
- Collisions and pressure, rms speed sqrt(3RT/M), equal mean translational energy (3/2)kT: [OpenStax Chemistry 2e 9.5](https://openstax.org/books/chemistry-2e/pages/9-5-the-kinetic-molecular-theory).
- Translational (3/2)nRT, nitrogen rotational nRT, expansion work P delta V: [OpenStax University Physics 2, 3.5](https://openstax.org/books/university-physics-volume-2/pages/3-5-heat-capacities-of-an-ideal-gas). Worked example independently gives 1.82918 J work, 2.74377 J motion gain, 4.57295 J heat.
- R, Avogadro and Boltzmann constants: [NIST CODATA](https://physics.nist.gov/cuu/pdf/wallet_2018.pdf), cross-checked with current SI constants. R's specified decimal is truncated, not the entire exact product.
- Representative He 4.0026, N2 28.014 and Ar 39.95 g/mol: [IUPAC CIAAW](https://www.ciaaw.org/abridged-atomic-weights.htm); [PubChem helium](https://pubchem.ncbi.nlm.nih.gov/compound/Helium) and [argon](https://pubchem.ncbi.nlm.nih.gov/element/18). Nitrogen PubChem page challenged the request; CIAAW independently verifies 2 times 14.007.
- Standard atmosphere 101.325 kPa and conventional g = 9.80665 m/s2: [NIST SI Appendix B.8](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b8).
- Altitude pressures and balloon expansion: [NOAA/NASA/USAF U.S. Standard Atmosphere 1976](https://ntrs.nasa.gov/citations/19770009539). Formula gives 101.325/83.5235/70.1085/54.0199 kPa and 2.4465/2.9680/3.5359/4.5890 L at 25 C.
- Piston/can reference values, slopes, rms speeds, kinetic energies and weighted lift recomputed in review-numbers.py/json. Piston area, weights, capacity, can cutoff and error ranges are specified model settings, not equipment ratings.
- [NGSS HS-PS3-2](https://www.nextgenscience.org/pe/hs-ps3-2-energy): students change a heated weighted piston and relate particle-motion energy to raised-weight position energy; the standard is practiced, not only named.

## Sensitivity

None: ideal-gas apparatus and unpeopled landscapes, with no cultural, historical, religious or bodily content. All 11 images inspected; none contains a person, and each is marked people:false. No person is needed for this apparatus-only scene.

## Flattest moment left

Repeating four temperature measurements in set B is still the slowest stretch, but it is the specified controlled replication. The former flat payoff is lifted: the result now sits beside the visible convergence, rather than covering it.

## Graphics

All 11 assets inspected in their scene and/or final-sized files; ten strong assets retained, can redrawn once using the built-in image tool. Replacement prompt: art/prompts.json, raw: art/raw/gl-can.png, finished: art/gl-can.webp. Free art.py --rekey preserved alpha.
Finished art 611.36 KiB; final bundle 921.67 KiB. Compared the lab with the existing Beat Lab reference frame. No placeholder or missing art. Steel-sky brand/panel 9.87:1; brand ink 10.53:1; muted/panel 8.13:1.

## Audit

One complete audit, Chrome 9961 / host 8765, within its 2400-second cap: `_scratch/gas-law-lab/review-audit/audit.md`. All 30 audit PNGs inspected in four sheets; no runtime errors, infinite motion or resize-stuck controls.

- 19 leads resolved: 1 disabled Fit instruction and 1 compact caption overlap fixed; 3 saved-row scroll notices retained; 2 iframe-reader/hint notices independently checked; 12 skipped/cut welcomes allowed by BASELINE rule 16, with instructions retained in hint/Read.
- Focused post-fix checks use the audit's measurement function, not a second audit. Can 680, welcome 1920 and hosted phone: no overlap, clipping, small targets, missing hints or disabled-control instruction. The 1920 saved-data scroll notice remains intentional.
- Every STANDARDS size checked: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, hosted 375x812. Grayscale, Motion off/on, keyboard-only 0/80 C recording and fit, live Record during warming, and all apparatus extremes checked. Current hint and main controls stay visible.
- Console clean in direct-file runs. Hosted runs additionally logged the test server's automatic favicon 404; no tool runtime exception or external resource request. Final proof: `REVIEW_FINAL_VALIDATION.json`; final hashes/line/art checks: `review-static.json`, both in Scratch.
- Closed the three exact gas-law-lab 8765 child hosts left by the LibreOffice launcher after verifying command, workspace and process identity. Ports 9960, 9961 and 8765 now refuse connections; host.html removed. No unrelated process touched.

## Left open

- Spec names kit/particles.js and docs/families/particles.md, neither exists. Writes there are forbidden; the local independent particle picture remains documented in handoff.
- Spec says a gas-only change produces a different slope. Ideal-gas theory and tested data give the same slope; the truthful implementation remains, and the spec is unchanged.
- Browser-fallback timing is verified; final bank-voice recording quality remains untested because recording is outside this pass.
- Compact Notebook data rows scroll intentionally. Main experiment controls, readouts, current hints and fitted crossing remain available; recorded rows are not answer choices.
- Nitrogen PubChem access challenged; independent CIAAW values were used without asking the unattended user. No new feature, external outreach or git commit.
