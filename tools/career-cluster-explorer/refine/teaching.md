# Teaching lens: career-cluster-explorer

Round 1, 2026-10-28. Cold lens: read spec.md, src.html, notes.md, careers.json, sources.md, handoff.md, art/prompts.json,
voice/lines.json, kit/careers.js and docs/families/careers.md; bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py
career-cluster-explorer` (175 KB, clean); ran `scripts/audit_tool.py` (ports 9930-9931) and `scripts/drive.py` (port 9932)
with held clicks for the voice checks. Frames and logs are in my scratch folder (d1 to d5, audit/).

Counts: blockers 2 (general 1, family 1), should fix 4 (general 2, family 2), polish 4 (general 2, family 2), nits 2 (family 2).

## Blockers

**B1. Clusters: "Ways in at N of 5 levels" describes the 83-career sample as if it were the whole cluster.** (general)
- Where: src.html drawBoard() line ~930 (`Ways in at ${used} of 5 levels`), drawPanel() line ~1010 (`ways in at N of 5
  levels`), notes.md "Talk about it" question 3.
- What: recomputed from careers.json: Financial Services 1 of 5 (accountant, financial advisor, actuary: all Bachelor's),
  Management and Entrepreneurship 1 of 5 (all Bachelor's), Digital Technology 2 of 5, Marketing and Sales 2 of 5; only
  Public Service and Safety reaches 5 of 5. A grade 7 student reads "Financial Services: ways in at 1 of 5 levels" and
  four "None in this tool" columns as "you need a bachelor's degree to work in finance". That is false for the real
  cluster (Advance CTE 2024 Financial Services includes Banking & Credit, Insurance and Real Estate, which have
  high-school entry jobs such as real estate agent, a Handbook "High school diploma or equivalent" career already in this
  tool). Notes question 3 ("Find one where most jobs need a bachelor's degree. What does that mean for someone who wants
  to start working right after high school?") steers the class to that wrong conclusion. The spec's own "Not like" line
  says the Clusters view "shows that every cluster has ways in at every level of training": the data contradicts it for
  13 of 14 clusters (STANDARDS, Facts: trust the computation and say so). A meter that misleads when its assumption (the
  sample covers the cluster) does not hold is a blocker (REFINE, Rounds).
- How seen: frame d1/ladder_fin.png ("Ways in at 1 of 5 levels"); the dw6 run printed all 14 counts.
- Better: either fill the empty columns with real careers from each cluster (the spec's intent; a spec and data change,
  so the integrator decides, possibly with Cory), or say plainly what is counted: "Careers in this tool: 1 of 5 levels.
  The real cluster has more ways in, like (example)." and reword notes question 3. Do not leave the bare count.

**B2. Two careers are in the wrong Advance CTE 2024 cluster.** (family:careers: the data comes from the shared
careers.json that the live career-match-quiz also bundles)
- Where: careers.json `stylist` (cluster `hosp`) and `realtor` (cluster `mkt`); shown on the festival cards, sheets,
  ladders, the lantern-lit line and the cluster counts.
- What: careertech.org (fetched 2026-10-28): Healthcare & Human Services has the sub-cluster "Personal Care Services"
  with Barbering and Cosmetology as its programs, so Hairstylist belongs in Healthcare and Human Services, not
  Hospitality, Events and Tourism (whose sub-clusters are Accommodations, Conferences & Events, Culinary & Food Services,
  Travel & Leisure). Financial Services has the sub-cluster "Real Estate" (buying, selling, leasing property), so Real
  Estate Agent belongs in Financial Services, not Marketing and Sales (Market Research, Marketing & Advertising, Retail &
  Customer Experience, Strategic Sales; real estate not mentioned). Which cluster a job belongs to is the fact this tool
  teaches.
- How seen: d1/sheet_stylist.png ("Hairstylist / Hospitality, Events and Tourism"), d2 sheet_realtor text ("Marketing
  and Sales"); the careertech.org cluster pages.
- Knock-on after the fix: counts become Hospitality 5, Health 12, Marketing 3, Finance 4; the Finance ladder becomes 2
  of 5 (realtor is High school). No trail uses either career, so the trail counts (4, 3, 2, 2, 3) stay. Where? still works
  (the braids booth and the For sale sign keep their careers). The live career-match-quiz shows the same two labels: tell
  whoever owns it.

## Should fix

**S1. All 14 lanterns can be lit from the Clusters ladder in 14 taps, and allLit then says "One night at the fair took
every cluster."** (general)
- Where: src.html careerOpened() (line ~490) runs on every sheet open (`onOpen`), including `{from: 'ladder'}` and
  Similar careers.
- What: Clusters mode names every cluster and lists its careers, so opening the first chip of each of the 14 clusters
  lights all 14 lanterns with no finding at all. The spec's reason for lanterns ("finding a cluster means reading about a
  job in it") and the allLit line both assume the student found them at the fair. BUILD wave lesson "No meter or puzzle
  can be solved ... trying every option for free": missed.
- How seen: drive shot cheap_clusters: `{"lit":14,"allDone":true}` after one ladder tap per cluster.
- Better: only careers opened from the festival (card, List, trail stop) light lanterns; ladder and Similar opens show the
  sheet without lighting, or light only once that career's festival place has been opened. Keep the sheet's "lantern: lit"
  line honest for each route.

**S2. "People doing it" shows OEWS wage-and-salary counts that badly undercount some jobs, one tap from a Handbook page
with very different numbers.** (family:careers)
- Where: kit/careers.js FACTS.jobs ("jobs in the US (wage and salary)"); this tool's facts include `jobs`.
- What: Farmer or Rancher shows 6,500; the linked Handbook page says 788,700 jobs (67 percent self-employed). Musician
  36,180 vs 170,400 (48 percent self-employed). Real Estate Agent 193,000 vs 530,600. "Wage and salary" means nothing to a
  grade 6 to 8 student; they will read "only 6,500 farmers in the US". BUILD wave lesson "Honest numbers: a meter or
  estimate says on screen what it assumes": the assumption is stated only in jargon.
- How seen: d1/sheet_farmer.png; Handbook Quick Facts fetched for farmers, musicians and real estate.
- Better: show the Handbook's "Number of jobs, 2025" (same edition as edu and outlook; a data change), or keep OEWS and say
  it plainly: "people who work for an employer; most farmers run their own farm, so the real number is much bigger".

**S3. The psychologist sheet contradicts itself.** (family:careers)
- Where: careers.json `psychologist`: eduNote "Psychologists typically need at least a master's degree to enter the
  occupation." (verbatim on the Handbook page) and, a few lines lower, path "A doctoral degree in psychology."
- What: two different answers to "how much school?" on one sheet.
- How seen: d1/sheet_psych.png.
- Better: path "A master's or doctoral degree in psychology (clinical psychologists need a doctorate)." Fix it in
  scripts/careers_data.py so career-match-quiz gets it too.

**S4. The "14 clusters" half of the standard is named but never explained.** (general)
- Where: Clusters grid and ladder heading (drawBoard), the sheet's lantern-lit line; no Advance CTE text is used anywhere.
- What: CTE.Career Clusters is "the 14 clusters and the occupations in them". The occupations side is taught well by what
  a solo student does (meets each job at a place, sees its cluster, follows trails across clusters, compares ways in). But
  nothing says what any cluster is: a student who lights "Management and Entrepreneurship" or "Supply Chain and
  Transportation" learns only the name and 3 to 7 examples, and tool.draft.json's outcome promises "Name the 14 career
  clusters". BASELINE rule 2 asks for taught well, above the minimum.
- How seen: d1/clusters_grid text (names and counts only), d1/ladder_fin.png.
- Better (inside the spec): one plain line per cluster from Advance CTE's "The Cluster Defined" (for example Financial
  Services: "Managing money: banking, insurance, accounting, investing and real estate") under the ladder heading and on
  the sheet's lit line. Add the page to the spec's Sources.

## Polish

**P1. The sheet's big education fact is jargon for grades 6-8.** (family:careers) Seven sheets show "See How to Become
One" in bold as the entry-level education (it reads like an instruction), and eleven show "Postsecondary nondegree award".
The exact Handbook wording must stay (spec), but add the plain column name beside it ("No degree needed", "Certificate or
some college") as the ladder's key does. Seen: d1/sheet_psych.png, d1/sheet_stylist.png.

**P2. Where? lists all 14 clusters from the first screen.** (general) A solo student can light everything by tapping 14
Where? buttons and the circled marker, never looking at the town. It is a fair scaffold and each lantern still costs a job
read, but the "find" would land better if Still dark appeared after a few lanterns or after a minute. Seen:
audit/size-1366x768.png (14 Where? buttons on load).

**P3. A predict moment (spec open question, not for the builder).** Before a job's cluster shows, let the student guess
which lantern it lights ("Which lantern will a forensic science technician light?"), with the chip's cluster label hidden
until they guess. This would teach the clusters by doing; it changes the format, so it goes to the spec's open questions.

**P4. Pay on the sheet can differ from the linked Handbook page.** (family:careers) The sheet shows the OEWS median for
the one detailed job (right per the spec), but the profile link shows the profile's median: Business Manager $105,770 vs
Top Executives $108,780; Airline Pilot $232,140 vs Airline and Commercial Pilots $210,020; Psychologist $100,580 vs
$99,110; Social Worker $59,550 vs $61,780; IT Support Specialist $61,860 vs $62,890; CNC Machinist $58,750 vs $59,620.
Label the box "Median pay for this job, 2025" or add "(the Handbook page covers a larger group)" to the source line.

## Nits

**N1. Two paths sit oddly beside the Handbook entry.** (family:careers) Air Traffic Controller sits under Associate's
but its path says only "FAA Academy training; most start before age 31"; Airline Pilot's path says "many airlines want a
degree" beside the Handbook's "Airline pilots typically need a bachelor's degree". Small rewording in careers_data.py.

**N2. Two cluster placements I could not confirm.** (family:careers) Flight Attendant (Hospitality: Travel & Leisure, or
Supply Chain: Air & Space Transportation, "air cargo and passenger services"?) and Public Relations Specialist (Marketing
and Sales, or Arts' "communications"?). The careertech.org cluster pages name neither occupation; check Advance CTE's
occupation crosswalk when B2 is fixed.

## For the sensitivity agent (rule 5: flagged, not judged)

- Emoji: only two careers use gendered person emoji, Family Doctor (woman health worker) and Chef (man cook); Human
  Resources uses the neutral person. Hairstylist is the haircut emoji and Fashion Designer a dress. They also appear in
  Similar careers. Check whether the set reads as stereotyping who does which job.
- "The braids and face paint booth" (the Hairstylist's place) and the stylist's Try it now ("Practice braids"): check the framing.
- A police officer figure is drawn in code at the crosswalk; check it reads neutral.
- The community help booth (counselor, social worker, psychologist: "Someone to talk to, and help finding help"): mental
  health framing; probably fine, worth one look.
- Pay comparisons can touch students' family incomes; consider a line in notes.md "Good to know". No standard here covers
  a sensitive topic, so rule 8 needs nothing more.

## Done when (spec)

1. PASS. check(): 37 hotspots, 83 careers, none duplicated or missing; all 83 sheets show "Median pay, 2025", the exact
   `edu`, "2025-35" and a link equal to `ooh` (drive dw1, `bad: []`).
2. PASS. 23 careers checked live (below), including the three larger profiles and all seven "See How to Become One".
3. PASS. Opening two places lit nothing; opening Welder lit Manufacturing; it survived a reload; Start over cleared it and
   localStorage. allLit was spoken once on the real held tap that lit the 14th (d5: `allLit:spoken`); allDone resets on
   Start over, so it plays again on the next run. (See S1: it can be reached without the fair.)
4. PASS. where() called 4 times per cluster: every pick holds an unopened career of that cluster, never the same place
   twice running except Manufacturing (all four careers are at the Ferris wheel, and the hint says so).
5. PASS. Each trail steps in order ("Stop n of m"); end rows 4, 3, 2, 2, 3 with the right cluster chips.
6. PASS. Every ladder chip sits in column `level` (matches the Handbook wording map, and the eduNote for the seven); bar
   widths recomputed as pay / $250,000, all 81 match to 0.1 percent in style and in measured pixels (doctor 97.7 widest,
   pilot 92.9); musician and actor show hourly with no bar. Grid counts recomputed: 4, 4, 11, 7, 5, 5, 6, 3, 11, 6, 3, 4,
   7, 7 = 83, all match the screen.
7. PASS. 50 real Tabs moved through the markers left to right; page scroll stayed 0, the town's scrollLeft stayed 0 and
   the pan followed focus. The List has all 37.
8. Left to Play and Craft (the audit lists no target under 44 px; see Audit pilot).
9. PASS. Five actions in a row: welcomeFestival, lanternHow and panHow each spoken once, panHow then silent; trailEnd3
   spoken on three of three arrivals (held clicks, d4); pickTrail drops a queued trailEnd.

## Facts checked

Handbook pages fetched live 2026-10-28 (WebFetch); each page uses the 2025-35 projections:
machinist, it-support, social-worker, psychologist, cook, police, pilot (the seven "See How to Become One": Quick Facts
says so on each, and each eduNote is the Handbook sentence verbatim; the psychologist sentence is present word for word);
game-design (Video Game Designers, 15-1255.01, listed under More Information), robotics-tech (Robotics Technicians,
17-3024.01, listed), ops-mgr ("General and operations managers held about 3.6 million jobs in 2025") (the three larger
profiles); graphic-design, athletic-trainer, web-dev, farmer, wind-tech, data-sci, hotel-mgr, atc, realtor, paralegal,
musician, trucker, dispatcher (the Public Safety Telecommunicators title confirmed).
- `edu`: 23 of 23 match. `level`: 23 of 23 right.
- `outlook` percent and word: 23 of 23 match.
- Pay (OEWS May 2025 for the detailed occupation, from the Handbook's Quick Facts or Pay tab): 23 of 23 match (cook: the
  restaurant cooks hourly $17.98 matches; the page gives no annual figure).
- Jobs: not a Handbook field in this tool; 3 of 3 checked differ widely from the Handbook (S2).
- Clusters: the 14 names match careertech.org; about 30 placements checked against the cluster pages, 2 wrong (B2), 2
  unconfirmed (N2).
- notes.md: every claim checked (the Ferris wheel holds all four Manufacturing careers; the kettle corn trail has 5 stops
  and 4 clusters; the larger-profile examples; the privacy line), except question 3 (B1).
- The spec's "every cluster has ways in at every level": false for 13 of 14 (B1).

No giveaways: there is no quiz, predict or hidden mode; the card naming each job's cluster is the explorer format the spec
asks for (P3 is the idea for more). Guardrails: grades 6-8, no hard history, no health topic beyond job descriptions.

## Audit pilot

- Confirmed: Motion off is clean; the five-click voice runs are clean (they match my held-click counts); the stacked
  layouts (760x900, 375 host) put most Where? buttons below the fold (the panel sits under the stage there; Play to judge).
- Wrong: every marker/panel and marker/privacy-line overlap from 680x425 to 1920x1080 is a marker clipped by the stage
  (#town hides it; audit/size-1366x768.png shows nothing over the panel); the "37 of 60 moved" rows on Where? are the
  intended pan; the four "focus lost" markers I did not confirm and suspect the same clipped-marker cause.
- Missed (as expected, all teaching): both blockers (the misleading ways-in count, two wrong clusters), the 14-tap cheap
  solve from the ladder, the job-count undercount, the self-contradicting psychologist sheet, the unexplained clusters.

Note: a `host.html` (14:08) is in the tool folder; I did not run `--host`, so it belongs to another agent and I left it.
