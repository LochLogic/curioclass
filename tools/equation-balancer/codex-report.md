# Codex report: equation-balancer

## Built
Built Workbench, five Levels with 25 equations, and ten Predict cards in a self-contained Grade 10 tool. Whole-molecule steppers, editable integer coefficients, atom and mass ledgers, intact-group counting, subscript inspection, saved equation checks and three-mode narration are implemented.
The first tap adds a shaded model and moves the ledger immediately. A solved lowest-term Level reveals its painted context and a specific atom/mass proof. Later equations add parentheses, intact groups, combustion parity and five-substance accounting.
Bundle: 1,585,898 bytes (1,585.9 KB). Generated WebPs: 1,110,134 bytes (1,110.1 KB). Recorded voice: 0 KB. Below the 2 MB goal.
Only this tool and its Scratch folder were written. No commits, shared engine edits, deployment or polish round. Tool-owned Chrome/server processes are closed; temporary host.html is removed.

## Numbers check
PASS: independent SymPy null spaces for all 35 equations have dimension one and reproduce the specified lowest integer coefficients. All Level totals and specified Predict totals match the repository's Elements Inspector masses.
Water: 36.03 g; octane: 1,028.41 g; lead nitrate case: 663.21 g. Integer thousandths are summed before two-decimal rounding. Maximum needed coefficient is 25, below the cap of 30.
Parentheses and hydrate parsing, each drawing's atom inventory and element-level comparison were checked. Group display never replaces the underlying conservation test.
Evidence: `_scratch/equation-balancer/check_numbers.py`, `numbers.json`, `functional.json` (143 assertions), `final-verification.json` (21 evidence checks).

## Facts checked
Sources below distinguish verified chemistry from story context inherited from the spec. Images illustrate contexts; they do not instruct laboratory work.
- Coefficients change amounts; subscripts change substances; balance conserves every element; simplest whole-number ratios: [OpenStax Chemistry 2e 4.1](https://openstax.org/books/chemistry-2e/pages/4-1-writing-and-balancing-chemical-equations).
- Atomic masses and symbols/colors: existing Elements Inspector table, attributed to the [RSC periodic table](https://periodic-table.rsc.org/). Independently recomputed all displayed solution totals, rather than treating rounded totals as conservation tests.
- Names of all listed ions and compounds: [OpenStax 2.7](https://openstax.org/books/chemistry-2e/pages/2-7-chemical-nomenclature); source content enumerated in Scratch/content.json.
- Usual Group 1 +1, Group 2 +2, aluminum +3, halide -1 and oxide -2 charges; P1-P7 neutral product formulas: [OpenStax 2.6](https://openstax.org/books/chemistry-2e/pages/2-6-ionic-and-molecular-compounds). These are the usual simple-ion patterns, not universal compound predictions.
- P8-P10 metal/water or acid patterns, hydroxide and released hydrogen: [OpenStax 4.2](https://openstax.org/books/chemistry-2e/pages/4-2-classifying-chemical-reactions), with the exact worked equations independently balanced.
- Water formation, ammonia synthesis, salt formation and magnesium oxidation: OpenStax 4.1 and 4.2; equation identities and coefficients checked against the spec and computation.
- Peroxide decomposition to water and oxygen: [PubChem hydrogen peroxide, CID 784](https://pubchem.ncbi.nlm.nih.gov/compound/784). Wound-care wording removed; the image is a cotton-pad context only.
- Ozone differs from oxygen, and CO differs from CO2: [PubChem ozone, CID 24823](https://pubchem.ncbi.nlm.nih.gov/compound/24823) and [carbon monoxide, CID 281](https://pubchem.ncbi.nlm.nih.gov/compound/281).
- MgO2 is real magnesium peroxide: [PubChem CID 61745](https://pubchem.ncbi.nlm.nih.gov/compound/61745). Corrected the spec's unstable-substance lookup. H3 is qualified as not an ordinary stable neutral molecule; NaCl2 is explained through usual charges, without universal impossibility claims.
- Rust/hand-warmer oxidation, protective aluminum oxide and white magnesium light: spec story contexts, consistent with oxidation chemistry in OpenStax 4.2 and [18.2](https://openstax.org/books/chemistry-2e/pages/18-2-occurrence-and-preparation-of-the-representative-metals). The exact hand-warmer and surface-film context was not independently established by those pages; retain as a factual-review item.
- Potassium chlorate decomposition and limestone calcination: [OpenStax chapter 4 exercises](https://openstax.org/books/chemistry-2e/pages/4-exercises). Emergency chlorate-generator context is inherited from the spec; wording avoids saying the pictured equipment specifically uses potassium chlorate.
- Yeast fermentation produces ethanol and carbon dioxide: OpenStax Organic Chemistry, alcohol preparation/fermentation context, and the spec. Bread-rise wording refers to the released gas, not the drawn vessel's precise recipe.
- White AgCl and yellow PbI2 precipitation, neutralization and aluminum/copper displacement: OpenStax 4.2 reaction classes; exact equations from the spec, independently balanced. Color details remain spec-sourced rather than newly established by a live measurement.
- Methane, propane, ethanol, ethane and octane combustion; glucose respiration: OpenStax 4.1/4.2 and [5.1](https://openstax.org/books/chemistry-2e/pages/5-1-energy-basics), plus specified story contexts. Complete-combustion equations are symbolic models, not claims about every real flame.
- Ammonia oxidation as the first nitric-acid step: [OpenStax 18.7](https://openstax.org/books/chemistry-2e/pages/18-7-occurrence-preparation-and-properties-of-nitrogen).
- CO reduces iron oxide in a blast furnace: [OpenStax 19.1](https://openstax.org/books/chemistry-2e/pages/19-1-occurrence-preparation-and-properties-of-transition-metals-and-their-compounds).
- Baking soda/acetic acid releases carbon dioxide: OpenStax 4.2 gas-forming acid/base reaction and the spec's equation.
- Sulfuric acid and phosphate rock produce phosphoric acid: [OpenStax 18.9](https://openstax.org/books/chemistry-2e/pages/18-9-occurrence-preparation-and-compounds-of-oxygen).
- Sodium/water safety wording: spec and ACS, Guidelines for Chemical Laboratory Safety in Secondary Schools (2016). The PDF could not be read live in this run; no experiment procedure is supplied. Safety wording persists after Reset.
- HS-PS1-7 is exercised by balancing and both ledgers; HS-PS1-2 by usual ion charges in Predict. Adopted the spec's recommended scope; no unfamiliar-fuel prediction added. Standards attribution: NGSS Lead States (2013).

## Break it
- Lowest terms: 4,14,8,12 ethane balances but is rejected for a done mark; 2,7,4,6 earns it. Multiplying a solution cannot earn a check.
- Zero/fractional/invalid inputs: 0, -1, 31, 1.5, NaN, Infinity and string 2.2 refused without mutating valid state. Cap buttons disable at 1/30. Emptying substances cannot satisfy conservation.
- Every wrong Predict option (14 total) rejects; all seven intended choices accept. Product ledger stays unknown until a valid selection. Choices rotate so a fixed screen position is not always correct.
- Cheapest Predict shortcut is trying every option. Required retries permit this; there is no saved prediction score, mastery badge or done mark to exploit. This remains instructional feedback, not independent assessment. Blanket no-enumeration guidance conflicts with the retrying spec; disclosed rather than adding an unauthorized gate.
- Already-balanced equations at all ones truthfully pass; changing to arbitrary easy inputs does not. No timer, high score or adjustable tolerance exists.
- Total mass alone cannot pass: atom equality is required, then GCD=1. Count groups still tests every element; ethanol OH is not mistaken for an intact hydroxide group.
- Formula-card opening/restoration cannot change coefficients. Clear progress removed all 25 saved checks in a fresh page. Reset returns every count to one, including worked examples.
- Five real held taps during animation gave counts 2,3,4,5,6 and hydrogen tallies 4,6,8,10,12 without a lost tap. Removal motion also leaves the ledger current.
- Disabled-advice exploit fixed: odd-oxygen hint is restricted to fuel=1 and an enabled recommended plus control; at 30 it gives ordinary guidance.
Evidence: functional.json, storage.json, fast-taps.json, hint-cap.json, remove-animation.json.

## Voice walk
Browser fallback only, no audio recording. 21 fixed strings use Curio.voice, bank casual-peer, voice metadata Zubenelgenubi. Sound off is respected; Read speaks the current hint.
Main held-click path at two-second pace heard: wBench, adjust, balanced, wLevels, balanced, wPredict, choose, right, balanced. All three how lines started; each is once per page load. Balanced repeated three times.
Side walk: subTip, first staged hint, current group explanation via Read, Sound off/on and Workbench return. Stale queued hints were dropped after the student moved on. notLowest fired twice; one stale utterance was cut on a change, the next completed.
Evidence: voice-main-fixed.json, voice-side.json, events-repeat.json. These supersede the earlier interrupted voice trial.
Fast repeated mode taps and Reset can cut speech. Current instructions remain in hint/Read; this is a disclosed fast-tap limitation, not a claim that every utterance always completes.

## Feel check
Played representative student paths across all three modes, with automatic verification of all 25 Levels. This was not a 35-minute study with students.
Best moment: double ethane, resolve the odd oxygen count, watch every row match and reveal the flare painting with the student's lowest-ratio equation and mass proof.
Flat moment 1: showing the story before a Level was solved weakened its payoff. Changed Levels to reveal the large context only when earned; Workbench keeps exploration artwork.
Flat moment 2: repeated drawings crowded out useful controls. Bounded the model region, drew compact copies through eight, then multipliers, and kept the primary ledger and steppers visible.
Viewed Snowy Mail Route and Beat Lab before building. Compared the earned ethane frame beside Beat Lab in Scratch/feel-comparison.png: rich warm art against a shaded bench, immediate model movement and specific proof provide a comparable visual finish. Chemistry progression comes from structural difficulty, not speed or confetti.

## Done when
1. PASS: water at ones has the oxygen mismatch; 2,1,2 matches H/O and 36.03 g both sides. functional.json and targeted frames.
2. PASS: water subscript opens peroxide card; Put it back preserves counts. Functional and voice-side checks.
3. PASS: doubled ethane refused for done; lowest ratio earns mark, flare and proof. Functional and final frames.
4. PASS: octane 2,25,16,18 gives 1,028.41 g; plus caps at 30; lead case gives 663.21 g. Exact arithmetic and browser checks.
5. PASS: nitrate and sulfate group rows appear where intact. Underlying atoms still checked. Group frames and functional.json.
6. PASS: P6 CaCl explains charge mismatch; CaCl2 then balances at ones. Functional and Predict frames.
7. PASS: 25 marks survive reload; Clear gives an empty saved array; Reset all ones. storage.json and functional.json.
8. PASS: primary trays/ledger dominate Workbench/Levels at 1366 and 680; Predict choices occupy the main decision area. Viewed final frames.
9. PASS: five real fast held taps each changed count and ledger during copy animation. fast-taps.json.
10. PASS at required two-second pace: all mode hows heard, balance/reduce events repeat, cap hint names no disabled plus. Voice logs and hint-cap.json; rapid interruptions disclosed above.
11. PASS with audit qualification: all required sizes manually viewed, phone primary controls visible, keyboard play/focus checked, all 25 images present without people, no console errors/external requests/em dashes. Full audit's phone iframe did not run; separate final host shots cover all modes. Complex structures remain counting inventories rather than complete molecular geometry.

## Wave lessons
BR1 lessons:
- Hint and voice: PASS at two-second pace; Read=current hint, immediate state text and stale-line cancellation. Rapid interruptions disclosed.
- Focus and layout: PASS for real scrolled menu click and keyboard ledger path; controls retained, stable hint/caption areas. rust-focus.json and keyboard-ledger.json.
- Sizes: PASS final targeted measurements and all-size frames, including 680x425 and 375x812 host. Read is now at least 44px.
- No giveaways: PARTIAL/FAIL against literal no-free-enumeration rule. Formula choices rotate, products begin unknown, and no prediction score is stored; retrying all choices still reveals the answer as the spec requires. Do not treat it as assessment.
- Honest numbers: PASS; visible mole assumption, exact counts beside capped dots, totals sum before rounding. Counts do not claim physical scale.
- Standards: PASS student activities for both codes; FAIL shared family/engine parity because both files are absent. Local chemistry API is documented.
- Motion off: PASS full audit and viewed calm/grayscale frame, no infinite animations.
Network-help-desk lessons:
- Short choice sets visible: PASS all three product choices visible in compact desktop and phone; ten-card Predict menu fits compact desktop. Long 25-equation navigation is intentionally scrollable.
- Resize mid-animation: PASS audit stress, no exception or disabled controls left behind.
- No delayed welcome: PASS no welcomeAfter; action may cancel premise rather than deliver it late, per BASELINE 16.
- Unknown shown unknown: PASS products/ledger concealed before the student's product choice.
- One look/meaning: PASS CPK colors supported by symbols, mismatch words and numeric rows; no color-only status.
- Badge truthful: PASS only lowest-term Level balance earns check, Predict no mastery badge; already-balanced examples remain truthful.
- State hints restore: PASS wrong/correct/reset/mode/cap paths checked, P8 safety persists.
- No answer by copied words: PASS no highlighted correct formula before choice; charges support reasoning. Enumeration limitation remains explicit.

## Audit leads
Ran the full audit once on Chrome 9991/host 8795 with a 40-minute bound. It finished with 40 leads, zero console errors, clean motion-off and resize stress. All 59 audit PNGs were inspected. No second audit was run; the audit is a pre-fix snapshot, with targeted final evidence below.
All 40 lead entries are accounted for in these groups:
- 3 small Read targets (680, 800, portrait): fixed min-width 44px. post-predict.json measures 44px.
- 2 phone harness leads (iframe context and missing hint): a tool-owned stale host served the wrong folder. Verified exact process commands, stopped only this tool's hosts, then separately checked all three final phone modes. Not a successful full audit phone pass.
- 10 Predict overlaps (five mode entries, repeated in wrong/correct state): fixed five-by-two navigation, empty-mark space, shorter labels and storage spacing. post-predict.json menuFits/choicesFit=true; final Predict frame viewed.
- 5 tiny subscript entries (two five-substance, three nitrate): fixed formula/equation/ledger subscripts to at least 10px. post-subs.json measured nine sizes >=10px and no horizontal overflow.
- 1 formula modal keep-region lead: background hint is intentionally covered by modal; foreground instructions and Put it back remain visible. Updated audit-states keep regions to describe the foreground, not the obscured background.
- 17 missing/cut welcome entries (14 first actions and three quick same-mode taps): retained intentional early-action cancellation allowed by BASELINE 16. No late welcome; current instructions remain visible and Read works. All three hows heard on the required main path.
- 1 Rust focus lead: audit clicked the center of a partly clipped long-list item. A fully scrolled real held click preserved focus on pick-L2-1. rust-focus.json. No controls rebuild under the pointer.
- 1 quick-double Reset cut-how lead: retained reset hush to avoid stale instructions. Read speaks the current reset hint; two-second held Reset audit was clean. Rapid speech completeness remains open.
Also fixed uncounted movement observations: reserved initial Sound icon width and story-caption height. Offscreen entries in the long 25-equation list are ordinary scroll navigation, not hidden product choices.

## Frames looked at
Viewed every PNG shot, including all 59 audit frames via 15 readable contact sheets. Manifest: audit-frames-inspected.json. Four art sheets and the bar comparison were also inspected.
Required sizes: 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900, and 375x812 in the host iframe.
Evidence folders: early-frames, bar-frames, test-frames, final-frames, targeted-frames, voice-frames, voice-recheck-frames, final-phone-frames, post-frames, post-phone-frames, safety-frames and phone-copies-frames, all under Scratch.
Viewed extremes include count 30, five substances, nitrate groups, modal lookup, arrival/removal, reduced motion, grayscale octane, earned ethane, keyboard focus, phone Predict and phone repeated molecules.
Final sodium-safety-fixed.json confirms the safety hint is visible after Reset and stepperBottom < ledgerTop. Earlier sodium-safety.json is superseded.

## Art made
25 separately generated illustrations: slate bench plus 24 specified story contexts. All OpenAI imagegen, drawn_by=codex, people=false, consistent editorial gouache with teal shadows and warm directional light. Precise atom models use shaded SVG rather than invented painted chemistry.
All WebPs were processed only with art.py --rekey. Raw PNGs, prompts and generated-path provenance are retained. No images needed redraw after visual inspection. Art totals 1,110.1 KB; bundle 1,585.9 KB; voice 0 KB, against initial budgets of 1,300 KB art and 0 KB voice.
Credits are in tool.draft.json. No downloaded illustration or paid art script used.

## Art still to paint
None. All 25 planned images are generated, used and inspected. No people were requested or drawn.

## Engine changes wanted
Missing kit/molecules.js and docs/families/molecules.md: supply the bond-battle spec API, shared masses/colors and accurate SUBSTANCES atom coordinates, bonds and ionic/polyatomic clusters for all Content formulas. Current local parse/tally/compare/molarMass/draw functions preserve counting and balance functionality.
Full structural geometry for complex compounds is NOT complete. Large structures explicitly use atom inventories without invented bonds. This is an open spec gap, not a claim of full shared-engine compliance. See handoff.md for replacement/parity guidance. Shared files were untouched.

## Left open
- Cold review required; no polish round performed. Full audit is pre-fix, with targeted final retests rather than a second complete audit.
- Complete shared molecular structures/family documentation absent; local counting model is the disclosed workaround.
- Predict retries allow enumeration, with no earned prediction score. Quick repeated mode/Reset taps may interrupt speech. Browser narration only; recorded voice is outside this Build.
- A few story details remain spec-sourced, as marked in Facts checked. ACS safety PDF was not read live; this tool supplies no laboratory procedure.
- Phone secondary navigation/story panels scroll; tiny repeated models prioritize primary controls. Compact screens retain total mass but omit per-element gram detail.
- Seven source expressions exceed the approximate 160-character style target; source otherwise has 2,005 readable lines and passed Node syntax checking.
- Final CO bond was corrected to triple and the bundle/syntax checked; no separate CO screenshot was taken after that one-line fix.
- Final evidence: final-verification.json has hashes and 21 true checks. Ports 8795, 9990, 9991 and 9992 are closed; host.html is absent. No other tool's process was stopped.
