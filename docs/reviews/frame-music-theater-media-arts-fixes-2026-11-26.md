# Frame fixes: music, theater and media arts, K to 12 (2026-11-26)

One fix pass over the twelve music, theater and media arts band frames (docs/courses/<id>/frame.md), settling the three expert reads (frame-<subject>-grades-k-to-12-2026-11-25.md, "E") and the twelve second-model reads (frame-<id>-codex-2026-11-25.md, "C-K2", "C-35", "C-68", "C-HS"). Model: frame-visual-arts-grades-k-to-2-fixes-2026-11-25.md.

## Gates

| Gate | Result |
|---|---|
| `python -X utf8 scripts/frame.py sync` | frames.csv 117 courses, calendar.csv 2119 rows |
| `python -X utf8 scripts/frame.py check <id>`, all 12 | 0 failures each; K to 8 frames 192 days (180 in units); music 9 to 12 640 (624), theater 9 to 12 640 (624), media arts 9 to 12 640 (616) |
| `python -X utf8 scripts/progression.py check arts` | 498 rows, 0 failures |
| `python -X utf8 scripts/stale.py check` | 121 files, 0 failures |

Shared files changed: data/progressions/arts.csv (notes cells through a locked exact-replace helper; one standard cell, mu-k-document, now MU:Cr2.1.Ka; MU:Cr2.1.Kb); data/standards/ncas-performance-standards.txt (MU:Cr2.1.Kb added, header note); data/standards/ncas-performance-standards-words.txt (music, theater and media arts lines, header note); docs/courses/arts/STANDARD.md 3.1 counts (music K 19, band 59); data/plans/frames.csv, data/plans/calendar.csv and docs/courses/CALENDAR.md through sync. No git run; no file deleted.

Cross-subject choices made inside this pass: theater keeps kamishibai (media arts K to 2 swapped to lianhuanhua); theater 6 to 8 uses Harold Lloyd, not Keaton (Keaton's One Week is media arts 3 to 5); music K to 2 dropped Carnival of the Animals (dance K to 2 keeps it); media arts dropped the Annabelle film (dance K to 2), Shaun Tan and the Lakota winter count (visual arts 3 to 5) and Wangechi Mutu (visual arts 9 to 12). Every new pick was searched in all arts frames, the ELA frames and data/plans/ela-texts.csv before use; no new pick appears in another frame.

## Music
Frames: docs/courses/music-grades-k-to-2, 3-to-5, 6-to-8, 9-to-12 (frame.md each).
Gates at the end: frame.py check, all four bands 0 failures; progression.py check arts 498 rows, 0 failures;
stale.py check 121 files, 0 failures; standards.py check exit 0. No git run, no frame.py sync, no em dashes
in any music frame.

### 1. Findings

E = expert read (frame-music-grades-k-to-12-2026-11-25.md); C-K2, C-35, C-68, C-HS = the Codex reads.

| Read | # | Applied or rejected | What changed, or why not |
|---|---|---|---|
| E | 1 | Applied | Every "see Row changes" now reads "landed in data/progressions/arts.csv 2026-11-25"; the 3-5 ELA row is ela:W.4.1; HS "is being written", the 6-8 stale.py note and the 3-5 "expert read checks" note are gone (0 hits each). |
| E | 2 | Applied | Later band's copy swapped (see part 2); the "no work repeats" lines in all four frames now say "checked 2026-11-26" and list the swaps; maker revisits with a new work (Joplin, Mozart, Beethoven, Dvořák) are named as revisits; 6-8 class pieces that return on purpose are named. |
| E | 3 | Applied | Words line MU:Cr1.1.3b now says "given" tonality or meter; 3-5 unit 2 names the given tonality or meter first. |
| E | 4 | Applied | MU:Cr2.1.Kb added to the id and words files; STANDARD.md counts 1,265 / music 265 / K 19 / band 59; mu-k-document claims it; Cr2.1.Ka narrowed. |
| E | 5 | Applied | 6-8 unit 7: Ives score first published 1949, so described and linked, not public domain; the tune "America" is public domain; recordings carry their own rights. |
| E | 6 | Rejected here, to the lead | docs/ADOPTION-BAR-SUBJECTS.md is a shared file outside the music frames; replacement text is in HS For the lead item 6 and part 4. |
| E | 7 | Applied | HS For the lead item 3: "The full path checks in weeks 16 and 32; week 32 is finals. A daily semester short path ends in its week 16 finals." |
| E | 8 | Applied (resolved, not repointed) | The HS Days Pending is replaced by the NAfME 2020 non-numeric guidance (same schedule as other academic subjects), per C-HS #8; the STANDARD.md 3.4 row goes to the lead. |
| E | 9 | Applied | K-2 unit 4: Ella Jenkins "1924 to 2024", hedge dropped. |
| E | 10 | Applied | "catalog" in the K-2 and HS frames; also fixed "defence" to "defense" in arts.csv rows mu-g10-choose and mu-g10-revise. |
| E | 11 | Applied | mu-g2-choose gained the invented or public option clause. |
| E | 12 | Applied | Carnival of the Animals swapped out of K-2 unit 1 (Haydn "Surprise"); tango (6-8 unit 3) and powwow (6-8 unit 4) named as cross-arts links in the music frame; dance-side lines for the lead in part 4; samba de roda against Cheri Samba is a word match, no change. |
| E | 13 | Applied | 3-5 unit 12: fraction-reading days from week 28; half-beat counting before then. |
| E | 14 | Applied | Order kept; 3-5 unit 3 names the grade 2 staff reading (so-mi-la) it builds on. |
| C-K2 | 1 | Applied | MU:Cr2.1.Kb restored as its own id (see E 4). |
| C-K2 | 2 | Applied | Creating checks now require every dimension the ids name. |
| C-K2 | 3 | Applied | Tonality is not mood: checks ask for the tonality heard; mood labels no longer count as tonality evidence. |
| C-K2 | 4 | Applied | Leave-out entry routes: each dependent unit supplies a prepared starting artifact; left-out ids stay unclaimed. |
| C-K2 | 5 | Applied | The critique model is first used in the earliest unit that needs it. |
| C-K2 | 6 | Applied | A course check right after a unit is that unit's end-of-unit assessment; its last two days are a rehearsal and revision day and a supported practice day; the earlier sample is a growth mark. |
| C-K2 | 7 | Applied | Unit 8's class song has a named maker and place. |
| C-K2 | 8 | Applied | The connecting-row note now says the wording is corrected and landed. |
| C-K2 | 9 | Applied | The after-core calendar note is rewritten; the full clash list is for the lead (part 4). |
| C-35 | 1 | Applied | Cr1.1.3b "given"; grades 4 and 5 paired settings in units 6 and 10; Cr3.2.5a look-fors in unit 11. |
| C-35 | 2 | Applied | Re7.2 three-prompt card (structure, element, context) in units 1, 5 and 9. |
| C-35 | 3 | Applied | Adjacent course checks are the end-of-unit assessment for units 2, 3, 6, 7, 10 and 11, with the last two days as rehearsal and revision plus supported practice. |
| C-35 | 4 | Applied | The warm-up runs on teaching, practice and rehearsal days; the timed check day names it. |
| C-35 | 5 | Applied | Leave-out entry routes, left-out ids unclaimed. |
| C-35 | 6 | Applied | critique-protocol and rhythm-syllables first used in unit 1. |
| C-35 | 7 | Applied | Recordings optional everywhere; the dated live mark is valid evidence. |
| C-35 | 8 | Partly applied | Kidjo "Agolo" (1994), Silkroad Silk Road Journeys: When Strangers Meet (2001), Tate Lowak Shoppala' (2006) and Ginastera "Malambo" named; source links stay for the scope-stage source pass (no web access this pass). |
| C-35 | 9 | Applied | For the lead items 1 and 3 rewritten to the current state. |
| C-68 | 1 | Applied | Cr1.1 aim stated, both AB and ABA in unit 3 (aim in units 7 and 11); Cr3.2 craftsmanship and originality look-fors in units 4, 8, 12; words lines Cr1.1.6a to 8a restored. |
| C-68 | 2 | Applied | Pr4.1 is a performance program: expressive quality, technical challenge and reason; words lines Pr4.1.6a to 8a restored. |
| C-68 | 3 | Applied | Re8 context clue; Cn10 three domains in units 2, 6, 10; Cn11 connection maps in units 1, 5, 9; words lines Re8.1.7a and 8a. |
| C-68 | 4 | Applied | The no-device route keeps audible evidence; ids stay unclaimed if no live equivalent exists. |
| C-68 | 5 | Applied | Ives fixed (E 5); the federal recording shortcut replaced by item-level checks (Marine Band items in units 4 and 9). |
| C-68 | 6 | Partly applied | Named: Huun-Huur-Tu "Kongurei" (1993), N'Dour "Birima" (2000), Wu Man "Ambush from Ten Sides", Astatke "Yèkèrmo Sèw" (1969), SamulNori (1978), Selaocoe Where Is Home (2022). The Chaurasia raga, the second Ma Rainey take, the Davids work, Fairuz, Mariza and the samba de roda group stay unit-plan picks: no web access this pass to confirm a specific recording and its rights, and source URLs belong to the scope-stage source pass. |
| C-68 | 7 | Applied | Mid-year checks are the end-of-unit assessment for units 2, 6, 10: performance marked at the showing (days 34/98/162), written items in the check (37/101/165), last two days rehearsal and revision plus supported practice (35-36, 99-100, 163-164). |
| C-68 | 8 | Applied | Entry routes plus a work-by-work sacred classification (unit 8 samul nori, unit 12 secular samba de roda pick, unit 11 Finlandia). |
| C-68 | 9 | Applied | listening-log first used in unit 1, practice-plan in unit 2. |
| C-68 | 10 | Applied | Two short excerpts in units 6 and 10, one set, at most 4 minutes, inside the performance-day limit. |
| C-68 | 11 | Applied, one part to the lead | For the lead items 2, 3, 4 rewritten; the ADOPTION-BAR line is the lead's (E 6). |
| C-HS | 1 | Applied | Unit 8 drafts in at least two forms (binary and rondo studies); unit 13 in theme and variations and through-composed (sonata optional); function in Pr4.2/Pr4.3.C.IIIa (units 13, 14); form and style in Pr5.1.C.IIIb (unit 15); Re7.2 records the setting plus one later use (units 3, 8, 13); Cn10 includes performing (units 2, 7, 12); Cn11 connection maps (units 5, 10, 15). Rows and words lines match. |
| C-HS | 2 | Applied | Placement is a prerequisite checklist (create, perform, respond, connect; rehearsed performance and feedback-to-revision; the sitting alone never places) in units 6 and 11; Level 4 recovery claims completion only when the record shows it, with an id-by-id Level 3 review at unit 16 entry. |
| C-HS | 3 | Applied | Descriptions never replace musical evidence; every no-device task gets a usable printed exemplar; a protected work is described and linked, with no copied reduction. |
| C-HS | 4 | Applied | Each dependent unit supplies a neutral Curio Class starting artifact (draft packet, extended-idea sketch, sketch, final-version packet); left-out ids unclaimed; a student 18 or older gets the family note and makes their own choices. |
| C-HS | 5 | Applied | Level 4 mid-year check is a whole-class written defense on fresh prompts; portfolio and review set carried unscored; oral conferences optional; showings named for units 16, 17, 18. |
| C-HS | 6 | Applied | practice-plan first used as unit 3's analysis-to-rehearsal card; unit 5 grows it into the full plan. |
| C-HS | 7 | Partly applied | NASM guide titles and URLs linked; gamelan named as Ladrang Pangkur (ensemble and recording at unit plan); raga tied to an identified Ali Akbar Khan Library performance, with section names matching the chosen extract. katajjaq stays a unit-plan pick: it needs a holding archive's page and Inuit community sources, not available without web access this pass. |
| C-HS | 8 | Applied | Days bullet states the NAfME 2020 non-numeric guidance and the course's 225 / 112.5 minutes; STANDARD.md 3.4 row to the lead. |
| C-HS | 9 | Applied | Seams intro names the grade 8 unit numbers (9 to 12); For the lead items 1, 3, 5 rewritten; item 6 (ADOPTION-BAR) kept for the lead with corrected text. |

### 2. Swaps

- K-2 unit 1: Saint-Saëns, Carnival of the Animals -> Haydn, Symphony No. 94 "Surprise", second movement (1791)
- K-2 unit 4: San Jose Taiko revisit -> Raffi, children's concert singer
- 3-5 unit 12: Danzón No. 2 revisit -> Ginastera, Estancia, "Malambo" (1941)
- 9-12 unit 4: Price, Juba Dance -> Margaret Bonds, Montgomery Variations (1964)
- 9-12 unit 4: Tate, Lowak Shoppala' -> Louis W. Ballard, Devil's Promenade (1973)
- 9-12 unit 10: "Shenandoah" -> "Red River Valley"
- 9-12 unit 14: Dvořák, New World Symphony -> Dvořák, String Quartet No. 12 "American" (1893) (Dvořák claims and Burleigh context kept)

All new works grepped against the arts frames, ELA frames, data/plans/ela-texts.csv and the picks registry
before use (no clash; Silkroad appears in 6-8 only in its list of works it dropped) and appended to picks.txt.
No Buster Keaton or Harold Lloyd.

### 3. Files changed

- docs/courses/music-grades-k-to-2/frame.md, 3-to-5/frame.md, 6-to-8/frame.md, 9-to-12/frame.md (HS: 57 exact edits this pass).
- data/progressions/arts.csv, notes only through the locked helper, no id moved or renumbered. 32 rows (7 K-2/3-5, 13 6-8, 12 9-12):
  mu-k-document, mu-g1-invent, mu-g3-invent, mu-g2-choose, mu-g4-invent, mu-g5-invent (K-2 and 3-5);
  mu-g6-invent, mu-g7-invent, mu-g8-invent, mu-g6-choose, mu-g7-choose, mu-g8-choose, mu-g7-express,
  mu-g8-express, mu-g7-revise, mu-g8-revise, mu-g6-respond, mu-g7-respond, mu-g8-respond (6-8);
  mu-g10-document, mu-g11-document, mu-g11-read, mu-g11-express, mu-g11-perform, mu-g9-respond,
  mu-g10-respond, mu-g11-respond, mu-g9-choose, mu-g10-choose, mu-g11-choose, mu-g10-revise (9-12);
  the seventh K-2/3-5 row is in the first-stretch log (not itemized here; check by diff).
- data/standards/ncas-performance-standards-words.txt: Cr2.1.Kb added; Cr1.1.3b, Cr2.1.Ka; Cr1.1.6a/7a/8a,
  Pr4.1.6a/7a/8a, Re8.1.7a/8a; Cr2.1.C.IIb, Cr2.1.C.IIIb, Pr4.2.C.IIIa, Pr4.3.C.IIIa, Pr5.1.C.IIIb; the
  "# words: 2026-11-26" header extended (all lines at most 14 words).
- The id file (MU:Cr2.1.Kb added) and docs/courses/arts/STANDARD.md counts (1,265 / music 265 / K 19 / 59).
- Scratchpad: picks.txt appended; music-findings.md (this file).

### 4. For the lead

- **Dance-side lines** (dance 6-8 frame is not mine to edit):
  - dance 6-8 unit 8: "Cross-arts link: music 6 to 8 unit 3 (grade 6) hears Piazzolla's tango; a student who took it may name the link, and neither unit needs the other."
  - dance 6-8 unit 12: "Cross-arts link: music 6 to 8 unit 4 (grade 6) studies powwow etiquette and the drum by listening and watching; neither unit needs the other."
  - dance K-2 unit 2 keeps Carnival of the Animals; music K-2 no longer uses it, so no link is needed.
- **Calendar clashes** (E, from data/plans/calendar.csv, the stagger keys on `arts`): K week 19 music and theater; grade 1 weeks 17 and 25 dance and music; grade 2 week 17 dance, ELD, music, PE, theater, visual arts, week 25 dance and music; grade 3 week 15 health and music; grade 4 week 15 ELD, music, SEL, week 24 computer science and music; grade 5 week 15 health, music, SEL. 6-8 and 9-12 break no rule. The frames' calendar notes defer to your one calendar pass.
- **Stale shared docs:** docs/ADOPTION-BAR-SUBJECTS.md arts row still lists L83 and the 63 strand ids as owed; replacement: "NCAS id-membership checking and the 63 composition and theory strand ids were completed 2026-11-21." STANDARD.md 3.4: add a "Music, high school" row with the NAfME 2020 guidance (composition and theory gets the same schedule as other academic subjects; no minute figure; nafme.org, NAfME-Opportunity-to-Learn-Standards-2020.pdf, printed page 19).
- **Browser checks** for the scope-stage source pass: Bonds Montgomery Variations and Ballard Devil's Promenade pages (dates, program note), Ladrang Pangkur ensemble and recording, the Ali Akbar Khan Library extract, the NASM guide URLs, and the 6-8 unit-plan picks listed under C-68 #6.
- **Stray file:** an empty C:\Users\Cory\AppData\Local\adj35.py was created by a hung shell command; I did not delete it (never delete files). Safe to remove.

### 5. Questions for Cory

1. **Supply ceilings.** K-2, 3-5 and 6-8 propose a $75 annual class ceiling (frame estimates: K-2 $55/$20/$20; 3-5 $30/$25/$25 plus an optional $20; 6-8 $35/$20/$20); HS proposes a $40 printing ceiling per class per level beside the free plain-paper route. My pick: approve $75 for K-8 and $40 per level for HS; every frame already has a free route, so the ceiling only caps the optional kit.
2. **NAfME high school opportunity-to-learn download.** The frame now uses the non-numeric guidance the Codex read quoted from the 2020 PDF. Should someone open that PDF in Chrome to confirm the page and wording before the course page cites it? My pick: yes, one browser check at the scope-stage source pass, no download kept in the repo.

## Theater
Frames: docs/courses/theater-grades-k-to-2, -3-to-5, -6-to-8, -9-to-12 (frame.md). Reads settled: expert read E
(docs/reviews/frame-theater-grades-k-to-12-2026-11-25.md) and the four second-model reads
(frame-theater-grades-<band>-codex-2026-11-25.md). A second round on 2026-11-26 swapped every within-band repeat of a
studied work (part 2). frame.py sync was run at the end of that round.

### 1. Findings

| Read | # | Applied or rejected | What changed, or why not |
|---|---|---|---|
| E | M1 | Applied | Each work now appears once in theater. 6-8 swaps: kyogen (u1) to Yuyachkani, Appia (u3) to Eiko Ishioka, Earnest (u9) to Sheridan's The Rivals. 3-5 u11: Kamiriithu to Laedza Batanani (Kamiriithu stays in 6-8 u8). The same maker with a new work and a new job stays only as a named revisit, written into the unit: commedia (6-8 u2), Stanislavski and Spolin (6-8 u9), Shakespeare (6-8 u11, 9-12 u12), Arena Stage (9-12 u14). The 6-8 and 9-12 "no repeat" claims are rewritten to name those revisits. Second round: every within-band repeat of the same studied work was swapped in the later unit too (K-2 u4, u9, u10, u11; 3-5 u7, u12; 9-12 u13, u17, u20; see part 2). A form recurs only with a different named work (kamishibai in K-2 u2 and u5 now uses new Curio Class original stories). A maker recurs only with a new work, named as a revisit (Marceau in K-2 u10, Shakespeare in 3-5 u12). Level 4 returns to the student's own earlier work stay (9-12 u18, u19, and the student's own portfolio and designs in u17 and u20). |
| E | M2 | Applied | Chaplin is out of 6-8 u1. Harold Lloyd's Safety Last! (1923, store scenes) is in (it is in the US public domain: published 1923, so public domain since 2019). Chaplin stays only in 3-5 u6. Keaton was not used because One Week is already in media arts 3-5. The cross-subject Chaplin overlap (media arts 6-8, The Kid) is a lead item. |
| E | M3 | Applied | Earnest is out of 6-8 u9. Sheridan's The Rivals (1775, public domain) is in, using the Captain Absolute and Sir Anthony scenes (a refusal, then pretended obedience), with a sensitivity line. The 6-8 lead item now lists the ELA anchor plays and states that none is used. |
| E | M4 | Applied (theater side) | Kamishibai stays in theater K-2 as a form (u1, and u2 and u5 with new Curio Class original stories). Media arts K-2 swapped to lianhuanhua. |
| E | m1 | Applied | The 3-5 u12 title is now "Same story, new eyes", so it no longer repeats "One story, many tellings". |
| E | m2 | Applied | The 3-5 base text now says "one silent film" and adds a rights line. |
| E | m3 | Applied (fell away) | Kamiriithu left 3-5, so grade 5 no longer tells the detention. The 3-5 lead note says "1977 to 1978". 6-8 u8 gives no detention date. |
| E | m4 | Applied | The time-figure text in K-2 and 3-5 now records the source result: the ETA 2016 document addresses grades 6 to 12 and gives no K to 5 figure. The 6-8 text gives the figure with its gaps. The stale "before the 3 to 5 and 6 to 8 frames" ordering note is gone from K-2 lead item 2. |
| E | m5 | Applied | All 98 theater rows in arts.csv had their "Assessed by" sentence rebuilt from their unit's id-by-id evidence line in the frame, by the locked helper. Grade 6 notes now name grade 6 only. |
| E | m6 | Lead item | The ADOPTION-BAR-SUBJECTS.md arts row is a shared file. The exact replacement text is in lead item 4 of 9-12 and below. |
| E | J1 | Applied in part | 6-8 gains a Latin American form (Yuyachkani, Peru, u1) in place of kyogen. Japan is still two in 6-8: kabuki (u7) and Ishioka (u3), which replaced Appia to keep year 6's Asia slot after kyogen left. Question for Cory below. |
| E | J2 | Rejected (kept as named revisit) | Shakespeare appears in 3-5 (u9 Midsummer speech; u12 The Tempest's stage directions in the First Folio, no longer a Midsummer revisit), 6-8 (the Globe) and 9-12 (Macbeth). Each use has a different work and a different job, and each later use names the earlier ones. |
| E | J3 | For Cory | The $150 ceiling for 9-12 is kept as the frame's pick and goes to Cory (questions below). |
| C-K2 | 1 | Applied | Unit 10 now teaches performers' artistic choices: its question changed, the teacher performs the same line two ways, and the TH:Re7.1.2a line, its audience card, the year-end check, the seam row, the model line and the th-g2-notice row text were all aligned. |
| C-K2 | 2 | Applied | Evidence was completed in u6 (Pr4.1.1b silent scene plus spoken line, with trait and feeling; Cr3.1.1b sounds and movements; Re8.1.1c feeling and choice) and u7 (Cr1.1.1b costume piece and prop, with each child's part marked). The u10 cards were reworded. |
| C-K2 | 3 | Applied | Once-a-week path rewritten: study, rehearsal and revision, showing check, a separate teacher's-table check, then respond, so no first-time evidence is collected in a respond session. Units per year: K 9, 9, 5, 5; years 1 and 2 8, 8, 7, 5. Row counts changed: K u3 6 to 5 and u4 4 to 5; year 1 u6 11 to 8, u7 5 to 7, u8 4 to 5; year 2 u11 8 to 7, u12 4 to 5. Checks: K weeks 19 and 26; years 1 and 2 weeks 17 and 26. |
| C-K2 | 4 | Applied | Unit 8's default is now two short stories the teacher makes up with the class and school, each named with its teller and setting. A visitor is optional and private family stories are never required. The Cn11.2.1a lines and the sensitive cell were aligned. |
| C-K2 | 5 | Applied | The "first time" sharing claim in u9 and its why-cell was replaced by "invent and revise the dialogue together, then share". The th-g2-show row text was aligned. |
| C-K2 | 6 | Applied (frame) / lead (shared) | K-2 lead item 2 is rewritten as settled, with the source URL. The STANDARD.md 3.4 line and the ADOPTION-BAR lines go to the lead. |
| C-35 | 1 | Applied | Evidence completed: u3 Cn11.1.3a (three labeled ties) and Re9.1.3b (Holder against the class production, Denslow as background), u10 Re8.1.5c (four fields), u11 Cn10.1.5a and Cn11.1.5a (investigation sheet with look-for), u12 Pr4.1.5a annotation and Cn11.2.5b (term plus convention), u2 retrieval wording. |
| C-35 | 2 | Applied | Once-a-week path rewritten as five-session units. Year 3 8, 8, 7, 5; year 4 8, 8, 7, 5; year 5 8, 9, 6, 5. Checks in weeks 17 and 26, 17 and 26, and 18 and 26. Respond falls one week later. Row counts: u3 8 to 7, u4 4 to 5, u11 7 to 6, u12 4 to 5. |
| C-35 | 3 | Applied | The course-check timetable now includes preparation for the fresh scene (3+3+8+4+18+4 = 40). |
| C-35 | 4 | Applied | U12 shows only the Perrault or the Ye Xian version. The Zuni "Poor Turkey Girl" is used for comparison only, never performed. |
| C-35 | 5 | Applied (frame) / lead | Lead item 3 (OTL) is marked settled and lead item 5 (row notes) is aligned. The STANDARD.md and ADOPTION-BAR lines go to the lead. |
| C-35 | 6 | Applied | The count statements were corrected (seams intro: "seven grade 2 rows through eight handoffs"). |
| C-68 | 1 | Applied | U10 now compares two named productions of Brecht's The Caucasian Chalk Circle (Complicité at the National Theatre, 1997, and the Unicorn Theatre, 2015). Cn11.2.8a gets a research sheet and a transfer item. The showing slot is defined. |
| C-68 | 2 | Applied | Evidence completed: u1 (Pr4.1.6b rehearsal record plus look-for, Pr5.1.6a two fields, Cr3.1.6b one physical and one vocal trait, Re8.1.6c preference plus belief), u3 (Re9.1.6b judgment), u5 (Re8.1.7c belief), u9 (Pr4.1.8b two objectives tested, Cr3.1.8b before-and-after record, Re8.1.8c), u7 and u10 slots defined. |
| C-68 | 3 | Applied | Once-a-week path rewritten: separate showing check, written check and respond session. Study and rehearsal split 2/2/1/1 and 4/2/2/2, then 1+1+1. |
| C-68 | 4 | Applied | Added a student-by-id observation roster and rotation rounds, and made recording optional (a student who declines is observed live). Devices: recording only by choice. Course checks give every student an observable acting turn. |
| C-68 | 5 | Applied | The recurring studies are named as deliberate revisits (commedia, Stanislavski and Spolin, Shakespeare). The ELA anchor check was added as lead item 5 (Earnest is gone). |
| C-68 | 6 | Applied | Lead items updated: OTL figure (2), stagger already keyed on course (3; the day 83 clashes remain), row notes aligned (4). |
| C-HS | 1 | Applied | "Sustainable" now means sustained through the performance. U7 stages one Hagoromo excerpt two contrasting ways, with an annotated observation record for Pr4.1.IIa. Changed to match: the title, the words list, the showing, the seam row and the th-g10-story text. Three lines in the words file (TH:Pr4.1.IIa, Pr5.1.IIa, Pr5.1.IIIa) were changed by a locked exact replace, and u8's "lasting performance" line was fixed. |
| C-HS | 2 | Applied | Evidence completed: u4 Re9.1.Ia (art, history, culture, another discipline), u8 Cr3.1.IIb (body, voice, bodily response, from both research and script), u10 Cr3.1.IIa (two log entries, concept and design), u13 Cr1.1.IIIc (historical and cultural plus experience) and Re8.1.IIIa (plus interpreting a classmate's work), u15 Cr3.1.IIIa (conventions plus a before-and-after note) and Pr6.1.IIIa (all four perspectives). |
| C-HS | 3 | Applied | Units 6 and 11 now add a four-part practical placement component (scene with character explanation, cued design solution, rehearsal record, source note), recorded by thread, with a short-path version. Both year-end rows now say "written component of placement". |
| C-HS | 4 | Applied | Added a student-by-id observation roster, shorter excerpts for u3 pairs and the u5 individual speech, and final live observation rounds counted on both paths. The forced-recording sentence was replaced with "Recording is optional...". The leave-out bullet and the u18 candidate were aligned. U5 Pr6.1.Ia now names an individually observed scripted contribution. |
| C-HS | 5 | Applied | The senior path is now ten days (Level 1 u5 32 not 42; Level 2 u10 and Level 3 u15 35 not 45; Level 4 u20 23 not 33). The final unit ends on day 148, the check falls on day 149 and respond on day 150. It is labeled as a planning judgment. |
| C-HS | 6 | Applied in part | Exact links were added for the three safety guides and the Abbey history page, and the safety-source note now says what the read opened. The source appendix for every fixed work is left to the scope and sequence or unit plans (no web fetch in this job). |
| C-HS | 7 | Applied (frame) / lead | The no-repeat claim was replaced with the named Shakespeare and Arena revisits, and units 12 and 14 now name the earlier units. The ADOPTION-BAR replacement text is in lead item 4. |

### 2. Swaps

- 6-8 unit 1: Chaplin, The Pawnshop -> Harold Lloyd, Safety Last! (1923, store scenes)
- 6-8 unit 1: kyogen (Nomura Mansai) -> Yuyachkani (Lima, Peru, founded 1971) and Andean festival forms
- 6-8 unit 3: Adolphe Appia -> Eiko Ishioka (M. Butterfly, 1988; in copyright, described and linked)
- 6-8 unit 9: Wilde, The Importance of Being Earnest -> Sheridan, The Rivals (1775)
- 6-8 unit 10: adaptation comparison -> two productions of Brecht's The Caucasian Chalk Circle (Complicité, NT 1997; Unicorn 2015)
- 3-5 unit 11: Kamiriithu -> Laedza Batanani (Botswana, from 1974)
- K-2 unit 8: Curio Class "stories told in one town" fallback -> two teacher-made school-community stories (visitor optional)
- K-2 unit 10: a scene "with three decision moments" -> a Curio Class scene performed twice, the same line two ways
- 9-12 unit 7: Hagoromo "lasting" task -> the same excerpt in two contrasting stagings (same work, new task)

Second round (within-band repeats of a studied work):

- K-2 unit 2: kamishibai form revisit -> a second Curio Class original kamishibai story (form kept, new work)
- K-2 unit 5: kamishibai form revisit -> a third Curio Class original kamishibai story (form kept, new work)
- K-2 unit 4: Billy Goats Gruff revisit -> How the Mouse-Deer Crossed the River, a Malay Kancil tale (public domain telling, such as Skeat, 1901)
- K-2 unit 9: Anansi tale revisit -> José Rizal, The Monkey and the Turtle (Philippines, 1889, public domain); Rizal's Noli Me Tángere is in ELA 10, a different work
- K-2 unit 10: Marceau's Bip revisit -> Marceau's The Mask Maker (a maker revisit with a new work)
- K-2 unit 11: Chinese shadow puppetry revisit -> Karagöz, the shadow theater of Türkiye (UNESCO 2009), studied from UNESCO's page only
- 3-5 unit 7: wayang lamp revisit -> tholu bommalata, the leather shadow puppetry of Andhra Pradesh, India (by looking only)
- 3-5 unit 12: First Folio "revisiting A Midsummer Night's Dream" -> the First Folio's stage directions in The Tempest (a Shakespeare maker revisit)
- 9-12 unit 13: Michael Chekhov's gesture revisit -> Uta Hagen, Respect for Acting (1973), object exercises, in Curio Class's own summary
- 9-12 unit 17: Ninagawa and Mnouchkine revisit -> Ivo van Hove's A View from the Bridge (Young Vic, 2014), beside the student's own unit 12 portfolio
- 9-12 unit 20: Ming Cho Lee and Clint Ramos revisit -> Mimi Lien's set for Natasha, Pierre and the Great Comet of 1812 (Broadway, 2016), beside the student's own designs
- 9-12 units 18 and 19: reworded as the student's own technique log and the student's own unit 14 critique (own work, kept)

All new picks were grepped against the arts frames, the ELA frames, data/plans/ela-texts.csv and picks.txt (no clash), then appended to picks.txt (15 theater lines).

### 3. Files changed

- docs/courses/theater-grades-k-to-2/frame.md: 22 exact replacements plus 7 once-a-week row counts, then 7 in the second round (CRLF kept)
- docs/courses/theater-grades-3-to-5/frame.md: 26 exact replacements, then 2 in the second round (LF)
- docs/courses/theater-grades-6-to-8/frame.md: 41 exact replacements, plus "catalogue id" -> "catalog id" (CRLF restored after a sed pass had stripped it)
- docs/courses/theater-grades-9-to-12/frame.md: 29 exact replacements, then 5 in the second round (CRLF kept)
- data/progressions/arts.csv, notes cell only, by the locked helper. All 98 th- rows got their "Assessed by" sentence rebuilt from the frames: th-k-* (7), th-g1-* (7), th-g2-* (7), th-g3/g4/g5-* (24), th-g6/g7/g8-* (24), th-g9 to th-g12 (29). Three of those rows also had their description text changed: th-g2-notice (artistic choices), th-g2-show (no "first time"), th-g10-story (sustained). After the second round the same rebuild was run again, so the notes match the swapped evidence lines (for example, the K u4 Cn11.2.Ka item now names the mouse-deer tale). No ids were moved and no other cells were touched.
- data/standards/ncas-performance-standards-words.txt: 3 lines (TH:Pr4.1.IIa, TH:Pr5.1.IIa, TH:Pr5.1.IIIa), "lasting" -> sustained wording, by a locked exact replace
- Scratchpad: picks.txt (15 theater lines appended)

Gates after the second round: frame.py sync (frames.csv 117 courses, calendar.csv 2119 rows); frame.py check, all four theater frames, 0 failures; progression.py check arts, 498 rows, 0 failures; stale.py check, 121 files, 0 failures. No em dashes in any of the four frames or in arts.csv.

### 4. Lead items

1. **Calendar clashes (not moved).** K-2: grade K week 19 (music) and week 27 (computer science, health, library, media arts); grade 1 week 27 (computer science, health, media arts); grade 2 week 17 (dance, ELD, music, physical education, visual arts) and week 27 (ELD, health, library, media arts, physical education). The once-a-week grade 2 mid-year respond session is in week 18, which is a grade 2 math check week. 3-5: the respond weeks are now 27, and the grade 4 social studies overlap is noted in the frame. 6-8: the day 83 clashes remain (stagger is already keyed on course). 9-12: week 32 is the finals week and has no core clash.
2. **OTL figure.** STANDARD.md 3.4 theater row: "No K to 5 weekly-time recommendation verified; the 2016 opportunity-to-learn document addresses grades 6 to 12." 6-8: at least 45 minutes in the school day for at least one semester each year (page 10), not stated as daily; the course gives 42h40 a year (21h20 on the short path).
3. **ADOPTION-BAR-SUBJECTS.md.** In the arts row, replace both owed clauses with "NCAS membership checking and the 63 high school music strand ids were completed 2026-11-21". Replace the intro line with "Layer 3 requires a subject approach before its scope and sequence; current states are recorded below."
4. **Media arts K-2 kamishibai.** Settled: media arts K-2 swapped to lianhuanhua, and theater keeps kamishibai.
5. **Cross-subject repeats (proposed handling):**
   - Chaplin: theater 3-5 u6 and media arts 6-8 u7 (The Kid). The works and jobs differ. Proposed: keep both, and the media arts unit names the theater study as a cross-subject revisit (or media arts swaps to Lloyd's or another 1920s public domain feature, not Safety Last!).
   - Satyajit Ray: theater 9-12 u5 (Ganashatru) and media arts 6-8 u7. The works and jobs differ. Proposed: keep, named as a cross-subject revisit in the 9-12 unit at the next touch.
   - Kabuki: dance 3-5 (kabuki dance) and theater 6-8 u7 (kabuki staging, hanamichi, onnagata), and Kabuki borrowing in 9-12 u12. Proposed: keep theater 6-8 u7 as the kabuki study and have dance 3-5 swap to another Asian dance form, or have both name the other as a deliberate revisit.
   - Keaton, One Week, is in media arts 3-5, so theater uses Lloyd. No action needed.
6. **Source appendix (C-HS 6).** The 9-12 fixed works still need exact primary-source links (page, claim, access date) before they become writing inputs. That belongs in the scope and sequence or unit plan step, under the browser-check rule.
7. **Within-band revisits (done in the second round).** Every repeat of a studied work inside a band was swapped in the later unit (part 2). What still recurs follows the rule: a form with a new named work (kamishibai), a maker with a new work named as a revisit (Marceau, Shakespeare), and Level 4 returns to the student's own work (9-12 u17 to u20). Browser checks for the scope stage: the Skeat mouse-deer telling, Rizal's 1889 text, a public archive page for Marceau's The Mask Maker, the UNESCO Karagöz page, a tholu bommalata museum page, and pages for the van Hove and Mimi Lien productions.

### 5. Questions for Cory (recommended pick first)

1. **Supply ceilings.** K-2 $40, 3-5 $40, 6-8 $45, 9-12 $150 a class a level, every unit with a free path. Pick: approve as written. The 9-12 figure is three to four times the lower bands, but it covers lighting gels, LED units and set stock for four levels of 30 students.
2. **ETA opportunity-to-learn PDF.** Pick: no download. The second-model read already checked it at source, and the frames cite the URL and pages.
3. **Two 9-12 safety PDFs (Montgomery County handbook, Play It Safe manual).** Pick: the fresh safety agent opens them at the first unit's read under Desk q-fix-downloads-1. No download in the frame pass.
4. **Japan weighting in 6-8 (J1).** Japan is still two (kabuki u7, Ishioka u3). Pick: keep, since Ishioka is a designer, not a form, and Latin America is now in. The alternative is a South Asian or Korean designer for u3.

## Media arts
Frames: docs/courses/media-arts-grades-k-to-2, -3-to-5, -6-to-8, -9-to-12 (frame.md). Reads settled: the expert read
(E, docs/reviews/frame-media-arts-grades-k-to-12-2026-11-25.md) and the four second-model reads (C-K2, C-35, C-68,
C-HS, docs/reviews/frame-media-arts-grades-<band>-codex-2026-11-25.md).

Gates at the end: `frame.py check` on all four media arts frames, 0 failures each; `progression.py check arts`, 498
rows, 0 failures; `stale.py check`, 121 files, 0 failures. No em dashes in any changed file. No git run, no
`frame.py sync`, no calendar weeks moved.

### 1. Findings

| Read | # | Applied or rejected | What changed, or why not |
|---|---|---|---|
| E | S1 | Applied | K to 2: at most one talk item a child a day; every safe-use and table item (MA:Cn11.1.Kb, 1b, 2b; MA:Pr5.1.1c, 2a, 2c) moved to a rotating look-for on the unit's last three making days, ten children a day, about 1.5 minutes, on a class list; second talk items heard in that rotation. Talk check day written out: set-up 5, self-check 5, six groups x 3.5 min (21), clean-up 4, 5 slack, 35 planned of 40. Waiting children have a quiet drawing card; the teacher table faces the room and a second adult, where there is one, watches it. Slack and rotation also applied to 3 to 5 (35 planned of 40). ma-k/g1/g2-society notes changed to match. |
| E | M1 | Applied | Every work repeated across media arts bands swapped in the later band; each work studied once K to 12; a maker who returns with a different work is named as a revisit with a harder question. 6 to 8 no-repeat claim now true; a true claim added to 3 to 5, 9 to 12 and K to 2's base text. See Swaps. |
| E | M2 | Applied | Same-band cross-arts repeats swapped in media arts: kamishibai (K to 2 unit 3 and unit 8, theater keeps), Annabelle Serpentine Dance (K to 2 unit 4, dance keeps), Shaun Tan (3 to 5 unit 1), Lakota winter count (3 to 5 unit 12), Wangechi Mutu (9 to 12 unit 10). Cross-band ties named as links in the frames: Hine (6 to 8 unit 4; visual arts and music 3 to 5), Wendy Red Star (K to 2 unit 9; visual arts 9 to 12, left with reason: different band and question), Chaplin (6 to 8 unit 7, The Kid; theater 3 to 5 has The Gold Rush, a different film), Ray (6 to 8 unit 7; theater 9 to 12). No Keaton or Lloyd added. |
| E | M3 | Applied | 6 to 8 MA:Pr5.1.6b/6c, 7b/7c, 8b/8c now scored from each student's kept trials (production look-fors over the last three production sessions, ten a session) with a production-log line; written "would do" items kept only as respond-day practice. Scored evidence bullet states the rule; ma-g6/7/8-craft notes match. |
| E | M4 | Applied | 9 to 12 Seams note rewritten: 6 to 8 hands on reading and society from unit 9, ideas and craft from unit 10, making and judging from unit 11, presenting and sources from unit 12; unit 1 reteaches. |
| E | m1 | Applied in part | 9 to 12 For the lead item 8 added (Cn10/Cn11 swap settled, as K to 2 and 6 to 8). The words-file header line and the DESK-ANSWERS entry are lead items (shared files), listed below. |
| E | m2 | Applied | K to 2 unit 9 MA:Cn11.1.2a evidence adds one way a studied work belongs to its time, place or people; ma-g2-society note matches. |
| E | m3 | Applied | 6 to 8 screening self-check moved from "that evening" to the first five minutes of the second check day. |
| E | m4 | Applied | 3 to 5 Seams cell for ma-g2-sources now gives "K to 2 unit 12, days 183 to 192" (applied in the earlier part of this pass). |
| E | m5 | Applied | K to 2, 3 to 5 and 6 to 8 Days bullets: Pending replaced with the bounded result (no separate media arts weekly minimum in the association's checklists or general standards, read at source by the second-model reads; 80 / 40 minutes; no comparison claimed). Recording it in STANDARD.md 3.4 is a lead item. |
| E | J1 | Applied, stricter | The read's pick allowed one named revisit a work; the directive's rule (each work once, a maker may return with a different work, named) is used instead. |
| E | J2 | Kept, question for Cory | Paper path for recording ids kept; a device is welcome, never required. Question 2 below. |
| E | J3 | Agreed, lead item | The frame-write line for bridge and review units is a shared-doc change for the lead. |
| E | process (stagger) | Resolved | frame.py stagger_key already counts each after-core course separately (lead, 2026-11-25); K to 2 For the lead item 4 now says so. |
| C-K2 | 1 | Applied | As E S1: one talk item a child, rotation of table items, minutes with 5 min slack, watching named. |
| C-K2 | 2 | Applied | Once-a-week path rewritten: units of 8, 9, 5, 6 sessions plus check and respond (32), weeks named; no assessment in a respond session; per-unit session counts corrected. |
| C-K2 | 3 | Applied | Unit evidence completed: u2 Pr5.1.Ka/Kb pointing to the skill card, u6 Pr5.1.1b dictated technique line, u9 Cn11.1.2a culture, u10 Pr5.1.2a role seen done, u12 Cn10.1.2b meant and for; ma-g2-craft note. |
| C-K2 | 4 | Applied | Critique card now "I notice ___. Why did you choose ___? You could try ___ because ___.", modeled in units 1 and 2. |
| C-K2 | 5 | Applied | Year-end checks sample earlier units, never the unit just before (K: Cr2.1.K + Re7.1.Kb; year 1: Cr1.1.1 + Cn11.1.1a; year 2: Cr1.1.2, Cr2.1.2 + Re7.1.2b); mid-year table items became paper sorts. |
| C-K2 | 6 | Applied in part | Flash criterion now a direct link (w3.org/WAI/WCAG21/Understanding/three-flashes-or-below-threshold.html); McLaren's Pas de deux linked (nfb.ca/film/pas_de_deux/). Other work links are left to each unit plan's holder-page read (no web fetch in this job), listed for the lead. |
| C-K2 | 7 | Applied | For the lead item 2 (bounded time result) and item 4 (stagger_key done) rewritten; item 3 adds library and research skills grade 2. |
| C-35 | 1 | Applied | u1 Cn11.1.3a adds cultural life; u1/5/9 Cn11 b ids now rotating look-fors of observed use plus a kept case card; u2 Pr5.1.3a two different roles each with a skill seen; u2 Pr5.1.3c and u6 Pr5.1.4c to rotation; u9 Cn11.1.5a investigation card (question, evidence from two work cards, conclusion); u3, u7, u11 Re9 with context and a finished piece plus a production step. Words lines MA:Cn11.1.3a, Re9.1.4, Re9.1.5 corrected; ma-g3/4/5-society, -craft, -judge notes match. |
| C-35 | 2 | Applied | Talk check day: set-up 4, written 10, six groups x 3 min (18) one talk item each, others self-check then quiet card, clean-up 3, 5 slack (35 planned); table items to rotation; course-check table items to paper sorts. |
| C-35 | 3 | Applied | Once-a-week path: no assessment in respond; year 3 units 7, 9, 6, 6 with unit 4 paused around the year-end check (weeks named); screening unit sequence of six named sessions; unit 11's one check session stated; unit counts (u3 6, u4 6) corrected. |
| C-35 | 4 | Applied | Unit 1 opens the critique: teacher models describe, ask, suggest on a Curio Class example before the first critique; Models carried row updated. |
| C-35 | 5 | Applied | Year-end checks now sample Re7 from earlier units (year 3 unit 1, year 4 unit 5, year 5 unit 9) with the Cn11 a talk items; check-day minutes given with about 10 min slack; marks in before respond. |
| C-35 | 6 | Applied in part | de Chomón country now "France, 1908, by the Spanish filmmaker" per the French national library's record. Other direct links left to unit plans (no fetch), lead list. |
| C-35 | 7 | Applied | Days bullet states the bounded result; For the lead item 3 rewritten. |
| C-35 | 8 | Lead item | ADOPTION-BAR-SUBJECTS.md is a shared doc; listed below. |
| C-68 | 1 | Applied | As E M3. |
| C-68 | 2 | Applied | u2 Pr5.1.6a two assigned roles in rotation with four skill areas; u3/u7 Re9 with a context card and production steps; u11 Re9.1.8 adds one production decision from the revision log; u4/8/12 Cn10 b ids add the cultural experience (teaching and evidence); u12 Pr6.1.8b trial showing with audience feedback, then a counted revision session before the screening, review covers growth and audience effect. Words lines Re9.1.6, Re9.1.7 add context; ma-g6-craft, ma-g6/7/8-judge, -sources, ma-g8-present notes match. |
| C-68 | 3 | Applied | Short path: six-session screening unit sequence written out; no assessment in respond. |
| C-68 | 4 | Applied | Course checks cut to two tasks: mid-year one structured analysis (two scored parts) plus the ethics task; year-end fresh plan plus unseen interpretation, the third item (angle, shot list, polish) dropped, keeping its unit evidence; 12 + 13 minutes, 2 min slack. |
| C-68 | 5 | Applied in part | Electric Hotel left the band (swap), so its country is moot here; 3 to 5 now says France per the library. Jáaji Approx. (MoMA record) and Falling Leaves (Library of Congress list) marked verified with links in For the lead item 6, which now lists item statuses. Flash criterion linked. Other links left to unit plans. |
| C-68 | 6 | Applied, differently | The read would keep repeats with a stated harder question; the directive's rule (swap every repeated work, keep only maker revisits with a different work) is used, which makes the no-repeat claim true. |
| C-68 | 7 | Applied in part | Days bullet and For the lead item 2 now state the bounded result. STANDARD.md 3.4, ADOPTION-BAR-SUBJECTS.md rows are lead items. The 9 to 12 seam note is fixed (E M4). |
| C-HS | 1 | Applied | u13 Cr2.1.III proposal + prototype + test + revised framework; u8 Cr2.1.II presentation context and tested, revised strategy; u3 Pr5.1.Ia growth in all four skill areas from trials to finished piece; u8 Pr5.1.IIa four areas scored separately from observed production; u4 and u14 Re9 judge work and process (u14 self-selected criteria, competing goals, strategically sought feedback); u15 Cn10.1.IIIb "and", three scored fields; u15 Pr6.1.IIIa curated for two distinct contexts; u2 Re7.1.Ib adds intention. Words lines Cr2.1.II, Cr2.1.III, Re9.1.I, Re9.1.III corrected; ma-g9/10/11-craft, ma-g10/11-ideas, ma-g9/11-judge, ma-g11-sources, ma-g11-present notes match. |
| C-HS | 2 | Applied | Tool-use ids (Pr5.1.Ic, IIc, IIIc) observed over the last three production sessions, ten a session, about 90 s; unit 17 defended talks over four sessions in groups of 8, 8, 8, 6, four minutes each, others on a named task; Level 4 mid-year a fresh framework-and-prototype task, unit 16 records unscored; Level 4 year-end day 638 two fresh written questions, talk records unscored; marks in before respond. |
| C-HS | 3 | Applied | Kicking the Clouds now described as the read gives (Ho-Chunk Nation and Pechanga Band of Luiseño Indians; grandmother learning Pechanga), maker's page linked; leave-out bullet and sensitivity list match; sensitivity read names Pechanga and Ho-Chunk sources. |
| C-HS | 4 | Applied in part | Flash criterion linked; Kicking the Clouds linked; For the lead item 6 gives verified and unresolved statuses. Begone Dull Care left the band. Other links left to unit plans. |
| C-HS | 5 | Applied | Consent rule (under 18 with family consent where required; 18 or over gets the family note and decides; school rules apply) in the leave-out and recording bullets and in 15 ma-g9 to ma-g12 rows' teacher notes (the unqualified "family's yes" replaced). |
| C-HS | 6 | Applied | Unit 16's proposal carries the year's source-selection checklist (living maker, two regions, two periods, one Native maker; maker, place, date, purpose, source); unit 17 fills gaps. |
| C-HS | 7 | Applied in part | Seams note rewritten (E M4); Level 2 day sequence stated plainly with the 237 to 238 check and respond. ADOPTION-BAR rows are lead items. |

### 2. Swaps

- K to 2 unit 3: kamishibai -> lianhuanhua, Chinese picture-story books (theater K to 2 keeps kamishibai, named as a link)
- K to 2 unit 4: Annabelle Serpentine Dance -> Walter Ruttmann, Lichtspiel Opus 1 (Germany, 1921, public domain in the US)
- K to 2 unit 4: Begone Dull Care revisit -> Norman McLaren, Pas de deux (1968), named same-maker revisit
- K to 2 unit 6: Prince Achmed revisit -> John Barnes Linnett, kineograph (England, 1868 patent)
- K to 2 unit 7: Horse in Motion revisit -> Bernd and Hilla Becher, water towers
- K to 2 unit 8: kamishibai revisit -> Duncan Tonatiuh, Dear Primo: A Letter to My Cousin (2010)
- K to 2 unit 11: Printed Rainbow revisit -> Leo Villareal, The Bay Lights (2013, still photograph only)
- K to 2 unit 12: Pauvre Pierrot revisit -> a Bengal patachitra scroll by a living painter of Naya (no deity scroll)
- 3 to 5 unit 1: Shaun Tan, The Lost Thing -> Gabriel Osorio, Bear Story (Chile, 2014)
- 3 to 5 unit 12: Lakota winter count -> a Dianshizhai Pictorial page (Shanghai, 1884 to 1898, public domain)
- 6 to 8 unit 1: de Chomón, The Electric Hotel -> Ladislas Starevich, The Grasshopper and the Ant (Russia, 1913, public domain in the US); Lumière brothers kept as a named maker revisit (Workers Leaving the Factory; grade 1 had Baby's Meal)
- 6 to 8 unit 2: Gertie the Dinosaur -> the Frenkel brothers, Mafish Fayda (Egypt, about 1936)
- 6 to 8 unit 2: Begone Dull Care -> Len Lye, A Colour Box (United Kingdom, 1935)
- 6 to 8 unit 8: Muybridge, The Horse in Motion -> Harold Edgerton, Milk Drop Coronet (1957)
- 9 to 12 unit 1: Méliès, A Trip to the Moon kept, named as a maker revisit (3 to 5 had Cendrillon)
- 9 to 12 unit 3: Trip to the Moon revisit -> Ishu Patel, Bead Game (Canada, 1977)
- 9 to 12 unit 3: Begone Dull Care -> Stan Brakhage, Mothlight (1963)
- 9 to 12 unit 4: Ozu, Tokyo Story -> Lucrecia Martel, La Ciénaga (2001), opening scene only (6 to 8 unit 3 keeps Tokyo Story)
- 9 to 12 unit 4: Kahiu, Pumzi -> Safi Faye, Kaddu Beykat (Senegal, 1975) (6 to 8 unit 10 keeps Pumzi)
- 9 to 12 unit 5: Pumzi revisit -> FESPACO (Ouagadougou, since 1969)
- 9 to 12 unit 8: Te Wei, Where Is Mama -> Te Wei, Feelings of Mountains and Waters (1988), named same-maker revisit (3 to 5 unit 10 keeps Where Is Mama)
- 9 to 12 unit 10: Wangechi Mutu, The End of eating Everything -> Lucy Walker with Vik Muniz, Waste Land (2010), one scene
- 9 to 12 unit 12: Kicking the Clouds revisit -> Merata Mita, Mana Waka (1990)
- 9 to 12 unit 15: Du Bois revisit -> Mona Chalabi, data illustrations (Du Bois stays in unit 12); Isuma named as Kunuk's company (6 to 8 unit 1)
- Named maker revisits kept: Skawennati (3 to 5 CyberPowWow, 9 to 12 TimeTraveller), Hopinka (6 to 8 Jáaji Approx., 9 to 12 Kicking the Clouds), McLaren (K to 2 units 2 and 4), Lumière, Méliès, Te Wei.

All new works were checked against every arts frame, the ELA frames, data/plans/ela-texts.csv and the picks registry
before use and appended to the registry (scratchpad picks.txt, 23 media-arts lines plus one note on Keaton).

### 3. Files changed

- docs/courses/media-arts-grades-k-to-2/frame.md: 64 exact replacements.
- docs/courses/media-arts-grades-3-to-5/frame.md: 43 exact replacements.
- docs/courses/media-arts-grades-6-to-8/frame.md: 43 exact replacements.
- docs/courses/media-arts-grades-9-to-12/frame.md: 57 exact replacements.
- data/progressions/arts.csv, notes cells only, through the locked helper, 42 rows: ma-k-society, ma-g1-society,
  ma-g2-society, ma-g2-craft; ma-g3-society, ma-g4-society, ma-g5-society, ma-g3-craft, ma-g4-craft, ma-g3-judge,
  ma-g4-judge, ma-g5-judge; ma-g6-craft, ma-g7-craft, ma-g8-craft, ma-g6-judge, ma-g7-judge, ma-g8-judge,
  ma-g6-sources, ma-g7-sources, ma-g8-sources, ma-g8-present; ma-g9-make, ma-g9-craft, ma-g9-present, ma-g9-society,
  ma-g9-judge, ma-g10-make, ma-g10-craft, ma-g10-present, ma-g10-society, ma-g10-ideas, ma-g11-make, ma-g11-craft,
  ma-g11-present, ma-g11-society, ma-g11-ideas, ma-g11-judge, ma-g11-sources, ma-g12-studio, ma-g12-exhibit,
  ma-g12-purpose. No id moved or renumbered.
- data/standards/ncas-performance-standards-words.txt: 9 lines (MA:Cn11.1.3a, Re9.1.4, Re9.1.5, Re9.1.6, Re9.1.7,
  Cr2.1.II, Cr2.1.III, Re9.1.I, Re9.1.III), each where a read showed the line dropped part of the standard; all at
  most 14 words.
- Scratchpad only: picks.txt (registry lines), ma/*.py specs and rep.py.

### 4. Lead items

1. **Calendar clashes (weeks not moved; frame.py calendar):** grade K week 27 (computer science K, health K to 2,
   library K, media arts K to 2, theater K to 2); grade 1 week 27 (computer science 1, health, media arts, theater);
   grade 2 week 27 (ELD K to 2, health, library 2, media arts, PE K to 2, theater); grade 3 week 17 (dance, media arts,
   theater 3 to 5) and week 26 (computer science 3, dance, media arts, PE, SEL, visual arts); grade 4 week 17 (dance,
   media arts, theater, visual arts) and week 25 (media arts, visual arts); grade 5 week 18 (computer science 5, dance,
   ELD, media arts, PE, theater, visual arts) and week 25 (computer science 5, media arts); grades 6, 7 and 8 school
   day 83 (dance, media arts, PE, theater, visual arts). 9 to 12: all arts likely on weeks 16 and 32.
2. **Words-file header line** recording the Cn10/Cn11 swap (E m1), and **one DESK-ANSWERS entry** for it.
3. **Frame-write process line** for bridge and review units with an empty Skills cell (E J3, 9 to 12 item 1).
4. **OTL time result:** record in STANDARD.md 3.4 that the association's elementary and middle school checklists and
   general PreK to 12 standards give no media arts weekly minimum (read at source by the second-model reads,
   2026-11-25); the frames now say so. No download needed for K to 8 unless Cory wants it confirmed first.
5. **ADOPTION-BAR-SUBJECTS.md** arts row and intro line (C-35 8, C-68 7, C-HS 7): replace the owed-work text with the
   reads' completed-2026-11-21 line and the approach-pages line.
6. **Cross-subject lines:** Hine's child-labor photographs (media arts 6 to 8 unit 4; visual arts 3 to 5 and music
   3 to 5), named as a link; Wendy Red Star (media arts K to 2 unit 9; visual arts 9 to 12), left, different band and
   question; Chaplin (media arts 6 to 8 The Kid; theater 3 to 5 The Gold Rush), different films; Ray (media arts 6 to
   8 Two; theater 9 to 12), named; Keaton and Cline One Week is media arts 3 to 5 unit 11's own first use (theater 6 to
   8 swapped to Lloyd, so no clash). No visual arts or dance swap is proposed; if the lead wants the Hine tie gone,
   the proposed swap is in media arts 6 to 8 unit 4: a non-US archive set on child labor or a historical event (the
   unit's own Candidate), keeping Bey.
7. **Direct work links (C-K2 6, C-35 6, C-68 5, C-HS 4):** only links known reliably were added (flash criterion,
   Pas de deux, Kicking the Clouds, Jáaji Approx., Falling Leaves, the French library record). Every other pick's
   holder page stays for its unit plan's read; the 6 to 8 and 9 to 12 For the lead item 6 lists give statuses.
8. **Facts to confirm at the unit plan** for this pass's new picks: Mafish Fayda's year (about 1936), Starevich's
   1913 Grasshopper and the Ant copy, A Colour Box's rights in the US, Linnett's 1868 patent, Mana Waka's archive page,
   Merata Mita's iwi as written, Martel's opening-scene content.

### 5. Questions for Cory

1. **Supplies ceilings.** K to 2: costs $35, $30, $40 a class a year, pick a $75 ceiling. 3 to 5: costs $45, $50,
   $50, pick $50 (same as the frame's pick). 6 to 8: costs $40, $40, $45, pick $75. 9 to 12: costs $90, $80, $80, $60
   a class a level, pick $100 a class a level. Every unit keeps its free path. Recommended: accept all four picks.
2. **Recording ids: paper only, or one shared device?** Recommended: keep the paper path as the standard (anything that
   frames, captures, orders, plays or shows counts as a media tool); a device is welcome, never required. The other
   option is one shared device per team of five or six, which is a cost question.
3. **The OTL checklists download.** Recommended: no download; the lead records the second-model reads' bounded
   result (no media arts weekly minimum) in STANDARD.md 3.4. Download only if Cory wants it confirmed at source by
   this side.

