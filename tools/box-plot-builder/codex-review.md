# Codex review: box-plot-builder
## Played
Cold Grade 6 solo play: real-dot drag, Histogram, all five San Diego Build steps and Headline before reading builder files. A strong newsroom with an earned result; later checked all three Build sets, keyboard-only completion and projector/phone views.
## Findings fixed
- Blocker, general, Build: Start over erased first-miss counts, allowing unlimited guesses. Attempts now survive resets alongside help marks.
- Blocker, family:data-desk, Pick: pair feedback disclosed the next shape answer. Explanation now waits for the reason commitment.
- Blocker, family:data-desk, Our class: a trailing comma silently became zero. Empty separators are discarded; comma-only input is rejected.
- Should fix, general, voice: long obsolete how-to speech delayed or displaced the next step's instruction. Stale how-to speech now yields to actions; event speech retains its queue. Added the missing File how-to and contextual day/game/value welcomes.
- Should fix, family:data-desk, charts: nearby box labels collided, and tall dot stacks crossed headings. Spaced labels retain fine leaders to exact marks; local dot fitting respects the actual plotting frame. Keyboard point selection now refits the kit's finished redraw too.
- Should fix, general, layout: compact Put back was clipped, small header targets were under 44 px, class input crowded laptop controls, and phone MAD/Pick retained an unnecessary completed grid. Fixed these layouts without changing topics or the laptop palette.
- Should fix, general, focus: File hid its focused control and Headline rebuilt verdict buttons. Focus now enters the report; verdict buttons keep their identity.
- Should fix, general, state/voice: partial Headline checks addressed a now-readonly city, a histogram set switch could invite dragging, and dragging home left a movement hint. Added city-specific how-to lines and matching validity/reset guards; sports titles now use for rather than in a person.
- Blocker, general, repair check: kept Headline identity private rather than exposing a stable answer index in a DOM attribute.
- Polish, general: the report's flat lead only named measures, and the phone payoff showed a cropped title. It now prints actual selected statistics and uses the phone's available height.
- Polish, general: strengthened the headline's paper veil and replaced the weak Aa class-card graphic with a shaded notebook, pencil and tiny chart.
## Findings left
- Nit, art: faint green edge residue on Sam's cutouts. Despill configured, but the permitted rekey environment was denied execution twice; original paintings retained.
- Spec conflict: literal 64 by 44 cards cannot fit ten columns beside a panel at 680x425. Retained ten columns, readable values and the large shared keyboard/pointer selection surface; no scope-changing layout feature added.
## Break it
- n: empty, September 31, Luka 82 and repeated misses; two misses supply help. Reset after one miss now retains the first attempt, blocking unlimited guesses.
- Measured/how/units: wrong then correct and all-options sweeping remain Sam fixed. All three source-card contexts were checked.
- Median/quartiles: same-valued wrong positions, repeated taps and sweeping cards fail. Both even-middle cards are required; supplied fields do not earn found credit.
- Min/max: the actual endpoints are the intended skill; wrong positions consume attempts and retain help credit.
- IQR: range, Q3 and Check mashing fail; both city gates require their own exact IQRs. Supplied answers cannot be turned into found credit.
- Mean/MAD: rejected median, totals, truncated mean, n-minus-one quotients, IQR and half-range on all three sets. Accepted the specified tenths answers. Evidence: numbers-*.json and post-*.json in Scratch.
- Pair/reason: always Median/IQR fails Chicago; each reason differs. One pick locks the field; pair feedback no longer reveals the reason.
- Headline: premature selection is blocked; mean-only and reversed-city guesses get their own explanations; every option was held-clicked and a wrong-then-right sweep stays locked. Four options remain distinct and focus stays on the chosen option.
- Report: a full mashing route earns zero of 14; normal routes earn 14. No best-score meter or saved score exists. A real keyboard-only route also earned 14 with zero exceptions.
- Explore tiles are changes, not scores: real 94 to 110 drag gives mean +0.53 and median 0; crossing the middle gives +0.5 median, Put back restores all. Histogram retains the endpoint observation.
- Custom data: trailing comma now preserves exactly three observations. Sixty identical values stay inside the plot after local stack fitting; all 60 observations remain present. Real keyboard selection also keeps all dots fitted and its ring centered on the selected dot: ring-proof-fixed/fitted-selected-dot.png and ring-proof.json. Clear/privacy and the bounded class entry were inspected.
## Voice walk
Actual browser speech through the unmodified kit queue, muted Chrome, 120 ms held clicks at a two-second action pace. Main path: drag, Histogram, bins, Dot plot, Put back, Build Facts/Box/Mean/MAD/Pick/File, Headline IQRs and headline.
Heard in order: meanMoved, histo, wBuild, facts, lineUp, midEven, quart, ends, iqr, mean, mad, pick, file, filed, wHeadline, pickHead, headRight, with Right results between the relevant prompts.
The first drag may skip the initial welcome. Obsolete how-to speech is cut when its action has happened; no earlier how-to carries into a later step. Several instructions start once and are cut before finishing at this pace; the log records those cuts. Mode changes hush speech as specified.

| Line group | Kind | Expected | Heard |
|---|---|---:|---:|
| Main how lines above | how | 1 each | 1 each |
| Right | event | 17 | 17 |
| Filed / headRight | event | 1 each | 1 each |
| Histogram, five taps on a fresh page | how | 1 | 1 |
| Chicago middle-card side path | how | 1 midOdd | 1 |

Read with Sound off spoke the current hint. Switching mode during Read released the queue; Sound on then spoke the correct mode welcome. The 29 fixed lines match voice/lines.json exactly. Final main-path rerun completed after all voice edits: voice-post-audit/headline-final.json. Class and Luka welcomes said value and game; partial Headline checks spoke denverOnly or miamiOnly, correctly naming only the editable city.
## Facts checked
- All 123 daily temperature values checked directly against NOAA NCEI daily-summaries API, stations USW00023188, USW00094846, USW00012839, USW00003017, standard units, matching the spec. Saved as source-*.json in Scratch.
- Recomputed all five sets independently in recompute.py: every count, sum, five-number summary, IQR, mean and MAD matches.
- Quartile rule and IQR: Illustrative Mathematics Grade 6 Unit 8 Lesson 15, https://im.kendallhunt.com/MS/students/1/8/15/index.html.
- Whiskers to extrema: IM Lesson 16, https://im.kendallhunt.com/MS/students/1/8/16/index.html.
- MAD as average absolute distance: IM Lesson 11, https://im.kendallhunt.com/MS/students/1/8/11/index.html.
- Measure selection by shape and context: IM Lesson 18, https://im.kendallhunt.com/MS/students/1/8/18/index.html.
- TMAX definition: NOAA GHCN-Daily README, https://www.ncei.noaa.gov/pub/data/ghcn/daily/readme.txt.
- 73 points at Atlanta on January 26, 2024: NBA official box score, https://www.nba.com/game/dal-vs-atl-0022300634/box-score.
- All 70 regular-season point values and their dates match ESPN's first-party athlete game-log API, season 2024, excluding its All-Star row: https://site.web.api.espn.com/apis/common/v3/sports/basketball/nba/athletes/3945274/gamelog?season=2024. Saved source-espn.json; 82 minus 12 is 70.
- Dallas' 50 wins and 32 losses confirm 82 team games; combined with the 70 played games, this confirms 12 missed. Source: Dallas Mavericks official 2024-25 Media Guide, https://cdn.nba.com/teams/legacy/www.mavs.com/wp-content/uploads/2025/02/2024-25-Dallas-Mavericks-Media-Guide-2.pdf.
- Derived facts: San Diego sum 2321, mean 77.3667, MAD 5.3133, IQR 8; Chicago 2331, 75.1935, 5.6191, 11; Luka 2370, 33.8571, 6.3755, 10. Miami/Denver both total 2842, mean 91.6774; IQRs 1/9 and ranges 5/24. Source: independently recomputed frozen NOAA/ESPN values, recomputed.json.
- Standards 6.SP.B.4 and B.5a-d: https://www.thecorestandards.org/Math/Content/6/SP/.
## Sensitivity
None for cultural curriculum: this is numerical weather/sports data. Checked all three fictional Sam portraits for consistent adult identity, friendly expression, plausible hands and stereotypes; no substantive concern. Every person asset is marked people:true. Luka is named with his accent and has no generated likeness.
## Flattest moment left
Mean and MAD still involve consecutive quotient entries. This practice is within the spec; the moving distances and earned numerical report provide the payoff. No extra game or topic was added.
## Graphics
Inspected all nine finished paintings at source and displayed sizes: three Sam poses, the newsroom desk, four cities and basketball. Preserved the cohesive editorial paintings, material details, light direction, newsprint and teal/rust distinctions. Improved the class notebook drawing, text-on-art contrast and chart label drawing. No missing art tokens or placeholders. Bundle 839273 bytes (819.6 KiB), art 338.5 KiB; below 2 MB.
## Audit
Audit not finished. Ran once, bounded to 40 minutes, on Chrome 9951 and host 8755. Chrome disconnected with WinError 64 during later Build states, after box-help-path. Saved 71 frames and 14 leads in _scratch/box-plot-builder/review-audit/audit.md; did not rerun.
- Confirmed class-entry clipping at 680x425. Compacted the unit/Show/Clear row at landscape widths; focused final frame places both buttons' bottoms at 375 px and the full entry region at 420 px in the 425 px viewport. Laptop artwork, controls and Put back remain visible.
- Input-name leads are false positives: visible labels are associated by for/id; the helper ignores those associations. The 1 Facts warnings describe an ordinal step heading, not a mismatched observation count.
- Moved-dot overlap leads involve a transparent chart input surface over its readable start text, not colliding painted labels. Facts-chip clipping names the secondary Start over control; all four current answer choices are visible.
- Phone iframe inspection failed; direct same-origin phone frames and Read checks cover the actual tool. Later state, calm, resize and walk sections were not reached; placeholder clean headings are not passes.
- Final narrow rechecks cover the repaired class form, fitted dots, four private verdict choices/focus, rapid card tap, drag-back hint, contextual speech, phone report and all-state score exploits. Final source syntax, exact 29-line inventory, frozen source arrays and inline asset checks passed.
## Left open
Unattended: take the spec's defaults; no questions requested.
- No shared engine/doc edits or git actions. Range-whisker, clamp and endpoint workarounds remain tool-local, with engine requests in handoff.md.
- Chrome transport failures interrupted the full sports-grid matrix even on its smaller retry. Successful targeted checks do not turn missing combinations into passes.
- Optional class entry can require panel scrolling in the shortest previews/phones. Its laptop controls fit and its input row is compact at every landscape size. Showing the entire editor, six 44 px set choices, graph switches and Put back simultaneously in a 425 px preview would need a disclosure flow beyond the specified persistent panel, or smaller targets; left open rather than adding that feature.
- Narration recordings remain absent; this review checked browser speech behavior, not a recorded news-reader performance.
- Browser/test runs were bounded, including the 40-minute audit. Initial short read commands lacked explicit deadlines; subsequent commands used the bounded wrapper. Browser and host ports stayed within the assigned range. No git commits or shared-file writes; evidence and working report drafts stayed in this tool's Scratch folder.
- Cleanup: Chrome ports 9950 through 9957 are closed, and the generated host.html is absent. Port 8755 still serves this tool folder; process ownership inspection was denied and netstat supplied no listener PID, so the unidentified listener was left untouched.
