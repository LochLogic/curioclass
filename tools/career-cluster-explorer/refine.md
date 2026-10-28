PASS
Counts: blockers 3 (general 2, family 1), should fix 12 (general 8, family 4), polish accepted 16

# career-cluster-explorer: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C), refine/sensitivity.md (SE, CHANGES).
Read them for frames and detail. Facts held: Teaching checked 23 careers against the live Handbook pages (edu, outlook
and pay 23 of 23, all 7 Handbook quotes word for word) and recomputed all 81 bar widths and the 14 cluster counts;
Craft found kit/careers.js matches docs/families/careers.md apart from the items below. "family" = family:careers
(kit/careers.js, scripts/careers_data.py, careers.json).

## Blockers
1. **"Ways in at N of 5 levels" reads as the whole cluster** (T-B1; general). The count covers only this tool's 83
   careers, so Financial Services and Management read "1 of 5" (Bachelor's only), against the spec's own claim that
   every cluster has ways in at every level, and notes question 3 steers the class to "finance needs a degree". Do both:
   (a) add real Handbook careers so each cluster has ways in at every level the Handbook supports (same edition and
   fields as the rest, each checked on its Handbook page and added in scripts/careers_data.py; sources.md updated), and
   (b) label what is counted ("Careers in this tool: N of 5 levels") wherever a column stays empty, with a line that the
   real cluster has more. Reword notes question 3 so it doesn't lead to a false conclusion.
2. **Two careers in the wrong cluster** (T-B2; family). Advance CTE 2024: Hairstylist belongs in Healthcare and Human
   Services (Personal Care Services), Real Estate Agent in Financial Services (Real Estate). Fix in
   scripts/careers_data.py and rebuild careers.json; update counts, ladders and any line that names them.
3. **A marker tapped near the edge of the view opens nothing** (P-B1; general). src.html:683: the press focuses the
   marker, focus starts a 420 ms pan and the marker slides out from under the pointer before release. In the 680x425
   preview the edge bands cover about half the town. Don't pan on a pointer focus (pan only for keyboard focus, or after
   the card opens); nothing moves under the pointer.

## Should fix
4. **Fourteen ladder taps light every lantern** (T-S1; general, BR1 cheap solve). Only careers opened from the festival
   (card, List, trail stop) light lanterns; ladder and Similar opens show the sheet without lighting it, and the sheet's
   lantern line says so honestly for each route. Where? stays as a help (T-P2: it may stop listing all 14 from the first
   screen, as the builder judges).
5. **"People doing it" undercounts self-employed jobs** (T-S2, C-S6; family, BR1 honest numbers). Farmer 6,500 vs the
   linked Handbook's 788,700. Use the Handbook's "Number of jobs, 2025" (same edition as edu and outlook), in the engine
   and the data, and say on the sheet where the number comes from.
6. **The psychologist sheet contradicts itself** (T-S3; family). Path: "A master's or doctoral degree in psychology
   (clinical psychologists need a doctorate)." In scripts/careers_data.py.
7. **The 14 clusters are named, never explained** (T-S4; general, rule 2). One plain line per cluster from Advance CTE's
   "The Cluster Defined", under the ladder heading and on the sheet's lit line; add the page to the spec's Sources.
8. **allLit is lost if the 14th lantern lights during the first-tap welcome** (P-S1; general). It never appears in the
   log and allDone is saved, so it never comes back (Done when 3 and 9). Queue it so it plays after the welcome.
9. **Focus drops at a trail's ends** (P-S2, C-S1; general, BR1 lesson). Next at the last stop and Back at the first
   disable themselves with focus; use aria-disabled or move focus to the next sensible control.
10. **Cluster names clipped mid-word in the grid at 375** (P-S3; general). "Educati", "Manufa", "Constru"; wrap or
    shorten, never cut.
11. **The lantern line is dropped or plays in the wrong mode** (P-S4, C-S5; general). lanternHow is dropped as "newer"
    when panHow queues, so a fast student hears it only on the second lantern; and it plays in Trails and Clusters,
    where the strip shows something else. Queue it as a sequence with panHow, and only where the lanterns show.
12. **Esc on the Start over confirm drops focus** (C-S2; general). Return focus as No does.
13. **The career sheet ignores Esc after a click on its text** (C-S3; family). kit/careers.js:179 listens on the
    overlay only; listen on the sheet (or document) while it is open. Document it.
14. **Read says "Press the ✕"** (C-S4; general). Name the control in words ("Press Close").
15. **People emoji gender jobs unevenly** (SE1; family). In scripts/careers_data.py: Family Doctor 🧑‍⚕️, Chef 🧑‍🍳,
    Hairstylist ✂️ (lines 72, 82, 87 per SE), then rebuild careers.json.

## Polish accepted
16. The sheet's big education fact in plain grade 6-8 words; the Handbook phrase ("See How to Become One",
    "Postsecondary nondegree award") goes underneath (T-P1).
17. Say when the sheet's pay is for a narrower job than the linked Handbook profile (T-P4).
18. ATC and pilot path lines read cleanly beside their Handbook entries (T-N1).
19. The police figure's head uses the scene's lavender (#c9c3ea) as a stylized silhouette (SE2).
20. Fashion Designer 🧵; Musician "places of worship"; Hotel Manager "Plan a pretend weekend trip and compare three
    places to stay online." (SE3-5).
21. The trail result is in view at 375 and 760 (P-P1).
22. The Ways in ladder isn't a small scroll box at 680x425 and 375 (P-P2, C-P4).
23. Lanterns larger for a projector at 1920 (P-P3).
24. At 1000x625 the Still dark list shows (P-P4).
25. The lantern pop and shimmer show after the sheet closes, not under it (P-P5; family).
26. "Stuck? Tap Where?." punctuation (P-P6); the trail stop header doesn't wrap at 1366 (P-P7).
27. Where? by keyboard puts focus on the circled marker (C-P1).
28. A place opened from List returns focus to the list (C-P2).
29. The card's "✓ met" updates without reopening (C-P3).
30. The bar scale line is in view with the bars (C-P5).
31. docs/families/careers.md documents the fixed ids `cr-title` and `cr-close` and the other gaps in C-N3, and the
    Tab-wrap focus passes preventScroll (C-N1).
32. The privacy line says what is saved (lanterns, careers and places met) (C-N6). Other nits as the builder judges.

## Spec open questions (not for the builder)
- A guess-the-cluster moment before a job's cluster shows (T-P3).

## Settled calls
- Flight Attendant and PR placements stay; mark them unconfirmed in sources.md (T-N2).
- The braids booth, the crosswalk officer and the help booth wording stay (SE: checked and fine).
- career-match-quiz keeps its own data copy for now; the fixes in items 2, 5, 6 and 15 reach it when it moves onto
  kit/careers.js (a board item, not for this builder).

## Exit check, round 1

Cold check, 2026-10-28, against REFINE.md (exit check), STANDARDS.md, BASELINE.md and the BR1 lessons in BUILD.md.
Draft bundle `CURIO_DRAFT=1 python scripts/bundle_tool.py career-cluster-explorer`: 196 KB, clean. Driven with
scripts/drive.py, held clicks (0.12 s), Sound and Motion on unless named; frames and logs in the exit agent's scratch
folder (out/sizes, out/n375, out/voice, out/b, out/compat). Every frame named below was looked at.

### Items
1. PASS. Ladder line "Careers in this tool: ways in at 3 of 5 levels. This tool shows 5 of this cluster's careers; the
   real cluster has many more..." (fin, read from the DOM), empty columns read "None in this tool (the real cluster may
   have some)", the panel says "careers in this tool: ways in at N of 5 levels"; notes question 3 now asks what jobs
   would fill Hospitality's empty columns. Part (a) is partial: 10 careers added, but Hospitality, Management and
   Marketing still show 2 of 5 here (honestly labeled, so not open; see Left open).
2. PASS. stylist in health, realtor in fin (careers.json); n375-sheet shows Hairstylist, Healthcare and Human
   Services; ladder-760x900 lists Hairstylist under Certificate or some college.
3. PASS. Held press on a marker in the edge bands at 680x425 (ferris right, stage left, bank right, clinic left) and
   gate at 1366x768: the card opened every time (e1 to e5); the pan moves only after the card opens.
4. PASS. A ladder tap (i4) and Similar careers (i4b) leave the lanterns unlit and the sheet says "lantern: not lit yet.
   Meet this job at the festival to light it."; List, card, job lights it (i4c).
5. PASS. "People doing it" uses oohJobs: Psychologist 209,000, "counting people who work for themselves. Handbook count
   for all Psychologists"; Farmer's oohJobs 788,700 matches the Handbook.
6. PASS. Path: "A master's or doctoral degree in psychology (clinical psychologists need a doctorate)."; the eduNote
   matches the Handbook's Education sentence word for word.
7. PASS. The DEF line sits under each ladder heading and on the sheet's lantern line; checked against the careertech.org
   cluster pages (health, fin, mgmt, edu, mkt, trans, build, energy); the spec's Sources names the pages.
8. PASS. v6: 13 lit, the first tap opens the ridge, Wind Turbine Technician lights the 14th during the welcome; log:
   welcomeFestival spoken at 1385 ms, allLit spoken at 6514 ms (after the welcome); allDone true.
9. PASS. Held Next to the last stop: focus on Open career (i9); Back at the first stop: focus on Next (i9b); by keyboard
   too (i9c).
10. PASS. n375-grid: Manufacturing, Construction, Education and the rest whole; no clipping found by measure.
11. PASS. v7 (0.6 s gaps): lanternHow spoken at 6549 ms, then panHow at 10685 ms, in order; v7b: first lantern lit at a
    trail stop, no lanternHow in Trails; v3 (0.2 s gaps): nothing stale played.
12. PASS. Start over, then Esc: confirm closed, focus on Start over (i12).
13. PASS. Held click on the sheet's text, then Esc: the sheet closed, focus back on the job (i13).
14. PASS. Hint while a sheet is open: "Press Close, or Esc, to go back to the fair."
15. PASS. Family Doctor 🧑‍⚕️, Chef 🧑‍🍳, Hairstylist ✂️.
16. PASS. "A master's degree or more" in big type, the Handbook phrase and eduNote underneath (sheet-1366x768).
17. PASS. "The Handbook page covers a larger group, Psychologists: $99,110 a year." (Hairstylist: Barbers,
    Hairstylists, and Cosmetologists, $35,880).
18. PASS. The ATC path and the pilot eduNote read cleanly beside their Handbook entries.
19. PASS. Police head fill #c9c3ea (src.html line 693).
20. PASS. Fashion Designer 🧵; Musician "places of worship"; Hotel Manager's Try it now as written.
21. PASS. Trail result in view at 760x900 and 375 (trailend-760x900, n375-trailend).
22. PASS. At 375 the ladder is part of the page scroll (page 1808 px); at 680x425 the board fills the stage height.
23. PASS. 1920x1080: lanterns "big", labels 14.5 px.
24. PASS. 1000x625: the Still dark list shows with 13 Where? buttons (fest-1000x625).
25. PASS. Lantern pop: no pop while the sheet is open, pop on close (i25).
26. FAIL (polish). "Stuck? Tap Where?" is fixed; the trail stop header still wraps at 1366x768 ("BEHIND THE KETTLE
    CORN: / STOP 5 OF 5", trailend-1366x768).
27. PASS. Where? by keyboard puts focus on the circled marker (mk-ferris); Enter opens it (i27, i27b).
28. PASS. A place opened from List, then Esc: focus back on the list item (i28).
29. PASS. "✓ met" appears on the open card without reopening it (i29).
30. PASS. The scale line sits right above the bars at every size (ladder frames).
31. PASS. careers.md documents cr-title and cr-close; the Tab wrap uses preventScroll.
32. PASS. "Your lanterns and the careers and places you opened are saved in this browser on this device only."
Settled calls: Flight Attendant and PR are marked unconfirmed in sources.md (PASS).

### Facts checked
Live Handbook pages (WebFetch), 14 careers: the 10 added (Administrative Assistant, Retail Sales Worker, Computer
Research Scientist, Childcare Worker, Teacher Assistant, Home Health Aide, Bookkeeper, Warehouse Worker, Drafter,
Environmental Technician) plus Hairstylist, Real Estate Agent, Farmer and Psychologist. Entry-level education, outlook,
number of jobs 2025 and the page's median pay: 14 of 14 match (all the 2025-35 edition). Hairstylist's and Real
Estate Agent's job pay ($35,790, $52,830) match the narrower medians on the Handbook's Pay tab. The psychologist
eduNote is word for word. Clusters (careertech.org, 2024 framework): all 14 placements fit a named sub-cluster
(Personal Care Services; Real Estate; Behavioral and Mental Health; Early Childhood Development; Learner Support;
Retail and Customer Experience; Purchasing and Warehousing; Architecture and Civil Engineering; Environmental
Protection; Accounting; Leadership and Operations, "administrative support"; Agriculture). Advance CTE's pages name no
occupations, so these are judged by sub-cluster.
Recomputed from careers.json: 93 careers, each in exactly one hotspot; cluster counts (4 4 11 8 6 7 7 5 13 5 4 4 7 8)
equal the grid; every ladder column count equals the DOM; all 93 bar widths equal min(100, pay / 2500) percent
(musician and actor hourly, no bar); levels used per cluster equal the ways-in lines; trail counts 4, 3, 2, 2, 3.

Engine: kit/careers.js matches docs/families/careers.md line by line (data fields, helpers, FACTS wording, sheet
options, Esc read on document in the capture phase, Tab wrap, fixed ids, sizes). Backward compatible:
Careers.sheet({data}) on career-match-quiz's own careers.json (scratch copy) draws Typical pay, Training, People doing
it and the quiz's source line for 83 of 83, with the same pay and job text as the quiz's openDetail; on the explorer's
data (83 with Job Zones) it runs with no errors. A scratch copy of career-match-quiz bundles and loads with no console
errors; its own files were not touched.

### Regressions looked for
Sizes 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 (drive.py --host): Festival,
card, sheet, trail end, Clusters grid and ladder. No horizontal scroll, no button under 44 px, markers 44 px or more,
the hint never clipped (at 760x900 the Clusters board is page scroll by design). Motion off: no animations; none
infinite with Motion on either. Saving survives a new tab; Start over clears storage. Focus kept on rebuilds (Where?,
List, trail ends, the card's ✓ met). allLines() equals voice/lines.json word for word (9 of 9). No console errors in any
shot (the only log was the iframe host's favicon 404), no resource requests, no fetch or XHR in the bundle, 196 KB.

Voice (held clicks, each action five times in a row):

| line | kind | expected | spoken |
|---|---|---|---|
| welcomeFestival | how | 1 | 1 |
| lanternHow | how | 1 | 1 |
| panHow | how | 1, then silent | 1 (silent x4) |
| welcomeTrails | how | 1 | 1 |
| trailEnd4 | event | 5 | 5 |
| trailEnd2, trailEnd3 | event | 1 each | 1 each |
| allLit | event | 1 | 1 |
| welcomeClusters | how | 1 | 1 |

First tap: the stage, a marker and a key get the welcome within 25 ms; a mode button gets only its welcome; Read speaks
the hint only; Sound says nothing and Sound on brings the skipped welcome once. Read during the welcome speaks the hint,
also with Sound off; a mode change right after Read starts its welcome at once. Stale: fast taps then a mode switch
drop lanternHow, panHow and trailEnd4 (hush, chain, newer); nothing played after its moment. Order follows the actions.

### Gate
1. Done when 1 to 9 pass (check(): 93 careers, no duplicate or missing; Handbook spot-checks; lanterns, Where?, trails,
   ladders, keyboard, sizes and voice as above).
2. CTE Career Clusters is taught by what a solo student does: meeting jobs to light all 14 lanterns, each sheet's
   cluster line and definition, the trails and the ladders.
3. The defaults work for a solo student (Festival with its hint, Where?, List).
4. Sensitivity items applied (emoji, police head, Fashion Designer, Musician, Hotel Manager).
5. No blocker or should-fix open.
6. Bundle clean, 196 KB, no console errors, no network requests.
7. Voice counts right.

### New findings
- polish (general): Where? for Energy never suggests the barn (Solar Installer). where() indexes a pool that changes
  with the last pick, so it cycles ridge, river, weather (dw4). "Never the same twice running" still holds.
- nit (general): on a slow first meeting lanternHow plays while the sheet covers the lantern strip (v1, 6608 ms, sheet
  open); the sheet's own lamp line is in view, so it still reads.
- nit (general): at 680x425 the Ferris wheel card's fourth job runs to the stage edge (card-680x425).

### Left open (polish, not blocking)
- Item 26, second half: the trail stop header wraps at 1366x768.
- Item 1(a), partial: Hospitality, Management and Marketing have careers at 2 of 5 levels here (labeled as this tool's
  careers only).
- The three new findings above.
