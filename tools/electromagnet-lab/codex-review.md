# Codex review: electromagnet-lab
## Played
Cold Grade 8 solo walk through Coil, Static, Field and all Notebook cases before reading the builder's files; then a projector-sized teacher walk. The tactile bench and clip lift are strong.
Played the two finish references from their existing bundles. Kept the rich apparatus, palette, exploratory choices and measured-data payoff.
## Findings fixed
- Blocker, general, Notebook: longest option solved all three cases. Balanced distractor lengths and varied the supported answer's length rank; retained each misconception and every supported claim.
- Blocker, general, Field: a flip plus core change could earn the reversal check. The observation now requires unchanged position, power and coil settings, then expires when the displayed needle settles.
- Blocker, general, Field: following Flip before the first sprinkle stranded the comparison. Each powered sample now records its polarity; sample, new flip, sample recovers without free credit.
- Should fix, general, chart: equally spaced 0/5/10/20/40 rubs distorted the curve. Numeric axes now use numerical distances; Core remains categorical.
- Should fix, general, mode entry: Static inherited Coil's folded class card while its welcome named hidden rows. Bench entry exposes its comparison and restores a matching hint.
- Should fix, general, voice: Notebook referred to an absent chart; queued how lines outlived their actions, and result speech could miss the next case. Shortened results, guarded stale lines and stop only obsolete instructions.
- Should fix, general, Field question: warming could replace the hint while Switch was hidden. Kept Switch available, retained the question hint and restored it after power changes.
- Should fix, general, weak Field setup: an insufficient reversal repeated the same instruction. Added visible, narrated stronger-setup guidance for both full and compact controls.
- Should fix, general, shared settings: Field could speak Coil's hidden Answer/Test instruction. Bench-specific ready hints now stay in their bench.
- Polish, general, Notebook: the three-second demonstration was flat. Its live labels now change from 20 turns/6 clips to 40/12, and show 20 rubs/2 cm/about 8 bits.
- Polish, general, art: replaced the flat Notebook compass circle with the existing painted brass compass, dial ticks, shadow and centered needle. Corrected Field face alignment and rekeyed green spill/loop holes.
- Polish, general: singular clip/bit captions now agree with a count of one.
## Findings left
No confirmed tool blocker or should fix remains, but independent mechanical verification is incomplete. This is not a full audit pass. The supplied default 4-times example also conflicts with its minimum-count rule.
## Break it
- All six fair sets: repeated one setting only replaces a row; one value cannot unlock. Trying every claim and ratio option retains the first pick and its correction status.
- Confounded rows do not join the old set. Zero-spread sets stay blocked. Core needs four cores; Rubbing needs four values including 40 and enough signal.
- Constant "2 times" fails the stronger Turns/Batteries ratios and gap questions. Answers use the nearest option to the actual measured means; no strength/charge meter or supported-answer label appears before the pick.
- Notebook longest-answer sweep: originally 3/3 supported; now 1/3, with the first two explicitly corrected. No fixed length rank solves the three cases. Trying every option cannot repair the first choice.
- Field button sweep, off flips, arbitrary arrows and rapid on/off do not earn observations. The compass cannot overlap the coil; arrows cap at 40.
- Reversal plus a core change or a move cannot earn check 4. A new real flip at a held stronger setup can. Weak reversal gives a recovery instruction.
- Sprinkling twice at one polarity cannot unlock; a fresh opposite-polarity sample can. Fresh before/after patterns match; the first filings answer stays final.
- Setting/mode changes abort trials without logging partial rows. The real five-tap Test mash yields one row. Calm trials still take about 3.6 seconds, with no infinite animation.
- Keyboard-only entry and compass arrows work. Read works with Sound off; mode change releases Read. Five fair-run result events repeat without repeating their how-to.
- Evidence: review-before-*.json, review-after-*.json, review-guards-*.json, review-weak-*.json and review-last-*.json in Scratch. Scenario fixtures are distinguished from real held-click walks.
## Voice walk
Held clicks, 120 ms presses, two-second action gaps, default Sound on, real jittered compass drag; trial animations finish before the next test setting.
Coil: addQ, pickQ, test1, keep, ready, claim, right, howMuch, tested. The first row tap may skip the welcome under baseline 16.
Static: wStatic; compare, add Rubbing, select it, test. Shared addQ/pickQ/keep instructions stay silent after their first hearing.
Field: wField, item1, fieldOn, item2, fieldOff, item3, fieldFlip, item4, fieldSprinkle, filings, right, fieldExplore.
Notebook: wNote, first answer result, fair, caseDone; subsequent answer results and caseDone events repeat, with fair silent after its first hearing.
Side paths: weak full/compact setup recovery, Read with Sound off, five fair reruns and rapid toggles. Full logs, cuts and counts are saved, not inferred from queued lines.
The final main walk (review-voice-release.json) has zero console errors, zero HTTP requests and no cut result events. Actioned how-to lines may be cut; none is falsely marked spoken while merely queued.

| Lines | Kind | Expected | Spoken |
|---|---|---:|---:|
| addQ, pickQ, test1, keep, claim, howMuch, fair | how | 1 each | 1 each |
| wStatic, wField, wNote; wCoil first-tap skip | welcome | 1 / 1 / 1 / 0 | 1 / 1 / 1 / 0 |
| fieldOn, fieldOff, fieldFlip, fieldSprinkle, filings, fieldExplore | how | 1 each | 1 each |
| ready, tested; item1 through item4 | event | 1 each | 1 each |
| right / wrong / caseDone in the main walk | event | 4 / 1 / 3 | 4 / 1 / 3 |
| caseDone in five fair reruns | event | 5 | 5 |
## Facts checked
- Turns/current strengthen a fixed-geometry coil; current reversal reverses its field: [OpenStax 22.9](https://openstax.org/books/college-physics-2e/pages/22-9-magnetic-fields-produced-by-currents-amperes-law).
- Steel strengthens a coil; wood/aluminum do not do the same; an air-core coil still has a field; steel may retain magnetism; nearby scissors confound an on-only test; scrap cranes use electromagnets: [OpenStax 22.2](https://openstax.org/books/college-physics-2e/pages/22-2-ferromagnets-and-electromagnets).
- Compass direction, field-line shape and non-contact magnetic evidence: [OpenStax 22.3](https://openstax.org/books/college-physics-2e/pages/22-3-magnetic-fields-and-magnetic-field-lines); magnetic versus true north: [NOAA NCEI](https://www.ncei.noaa.gov/products/geomagnetism-frequently-asked-questions).
- AA nominal 1.5 V: [Energizer E91](https://energizer.com/eu/spain/wp-content/uploads/sites/9/2024/05/e91_max_na_AA.pdf). Series cells/current/internal resistance: [OpenStax 21.2](https://openstax.org/books/college-physics-2e/pages/21-2-electromotive-force-terminal-voltage); heating at high current: OpenStax 22.2/22.9.
- Rubbing transfers charge: [OpenStax 18.1](https://openstax.org/books/college-physics-2e/pages/18-1-static-electricity-and-charge-conservation-of-charge); neutral-paper polarization: [18.2](https://openstax.org/books/college-physics-2e/pages/18-2-conductors-and-insulators); charge/distance dependence: [18.3](https://openstax.org/books/college-physics-2e/pages/18-3-coulombs-law).
- Saturation model form: Matsusaka et al., CES 65 (2010), DOI 10.1016/j.ces.2010.07.005, corroborated by [Matsusaka, KONA 29 (2011), equation 12](https://www.jstage.jst.go.jp/article/kona/29/0/29_2011007/_pdf/-char/en). Neither source validates this balloon's numerical parameters.
- Exact counts, 2.5 ohms, gap factors, noise and idealized Earth/pole units are declared spec model choices. Independent Python enumerated 192 coil and 20 static settings: current 0.6/1.2/1.8 A, maximum mean 36, non-steel mean at most 0.36, class counts 6/24/0/5, fair Notebook 6/12/about 7.8 bits.
- Runtime means match all 212 independently computed settings. All 24 claim branches and 16 ratio branches pass; too-small ratio guesses and a three-core set with a genuine signal stay blocked. Numeric chart positions are measured, not assumed.
- Small-magnet home precaution: [U.S. CPSC](https://www.cpsc.gov/safety-education/neighborhood-safety-network/toolkits/child-safety). Notes distinguish real heating, remanence, field strength and simplified clip counts.
- Student-question/fair-set work teaches [MS-PS2-3](https://www.nextgenscience.org/pe/ms-ps2-3-motion-and-stability-forces-and-interactions); off/on/flip, gaps and flawed-test evaluation teach [MS-PS2-5](https://www.nextgenscience.org/pe/ms-ps2-5-motion-and-stability-forces-and-interactions).
## Sensitivity
None: no people, cultural, religious, historical or body content. All 20 assets are marked people:false and visually checked.
## Flattest moment left
Retesting an already understood easy Turns set is routine. The weak-field recovery, changed quantities and richer Notebook compass improve the original weakest demonstration without adding topics or scoring.
## Graphics
All 20 paintings checked in scene and on a new contact sheet. No new painting needed; one cutout reprocessed, precise compass drawing upgraded. Art 339.05 KB; bundle 781.90 KB; no recordings.
Phone controls fit with zero horizontal overflow; compact Notebook and Field question frames retain readable evidence and an accessible Switch. Grayscale and Motion off checked.
Independent contrast on paper: ink 14.50:1, muted 5.62:1, brand 5.72:1, ok 4.85:1, focus 5.24:1; white on brand 6.34:1. Labels and marked corrections remain useful in grayscale.
Compared the workbench with Snowy Mail Route and Beat Lab. Kept its richer, age-appropriate laboratory finish.
## Audit
Audit not finished. The one run had a 40-minute process-tree cap, but exited on its own 60-second CDP domain-enable timeout in the initial size stage. No audit.md or PNGs were produced, so there were no partial leads to fix.
Did not rerun it, following the incomplete-audit stop rule. Failure receipt: _scratch/electromagnet-lab/review-audit-failure.md; artifact hashes and cleanup: review-closeout.json. No claim of all-size, resize or mechanical-audit clearance is made.
Direct review frames cover 680x425, 1366x768 and real 375x812 iframe states. Fresh 800x500, 1000x625, 1280x720, 1920x1080 and 760-wide audit checks remain unverified. The 37 focused frames were inspected in ten contact sheets, with phone/compact/main-path frames opened separately.
## Left open
- Done when 1 is impossible as written: at one battery, 10 turns averages 3 clips, below the ratio gate's minimum 4. The eligible default comparison is 20 to 40, about 2 times; two batteries permit 10 to 40, about 4 times. Kept the formula and spec untouched.
- Algenib/gravel-ranger recordings remain absent, as in the build. Verified browser-speech starts and timing through the muted Chrome log; no human listening or physical school-device test was claimed.
- Unattended choice: applied the explicit no-giveaway/length rules to distractor phrasing while preserving the supported claims and misconceptions. The early review draft lived in Scratch so writing codex-review.md remains the final action.
- The first read-only document command used a tool wait limit; subsequent shell commands used explicit hard process deadlines.
- Only tools/electromagnet-lab/ and _scratch/electromagnet-lab/ were intentionally written. No git commits or shared-source changes. No tool-folder host.html. Every assigned Chrome/host port was closed at closeout; Windows denied the extra process-command-line inventory, so no claim of an OS-wide process inventory is made.
