# Teaching lens: half-life-dice

I read spec.md, src.html, notes.md, voice/lines.json, codex-report.md and handoff.md cold, treating the builder's
claims as claims. I worked on the existing bundle, tools/half-life-dice/half-life-dice.html. Frames and scripts are in
S:/CurioClass-codex-scratch/half-life-dice/lens-teaching/ (f1/ and f2/ frames, the nums.py recompute, shots1.json,
shots2.json). I read and cite the shared audit (audit-r1) but did not re-run it. The 5,730 vs 5,700 question belongs
to the owner and is not reported here.

Counts: blockers 1, should fix 6, polish 4, nit 3.

## Blockers

1. **Roll, Mark a half-life (src.html:116 markMove, :117 snap):** the card tells a student to move a line that already
   sits at half the crowd. Acceptance compares the crossing on the student's own noisy tray with the exact half-life
   (within 0.5 rolls), so when the tray runs slow or fast, a correctly placed line is refused.
   - Default seed, d12: a line at 498 nuclei gets "Move to half the crowd. Your tray: 8.5 rolls. Exact for a d12:
     7.966." The only line accepted is at 544 nuclei ("Accepted. Your tray: 8.0 rolls").
   - Seen in f1/t02-d12-line498.png against f1/t03-d12-line544.png, and recomputed in nums.py. My mulberry32 copy
     reproduces the tool's tray points exactly.
   - The same tray noise affects d8 and d10: their accepted lines are at 513 and 504, and the snapped line just below
     500 is refused.

   The feedback is wrong about what the student did. It teaches that their reading is the mistake, when the real
   lesson is that one tray scatters around the exact value. Better: accept the line by where it sits (500, or the
   step nearest 500), then report "Your tray crossed at 8.7 rolls; exact 7.97; one tray scatters, try Average 20 runs".
   The spec's own rule (accept within 0.5 rolls of exact) fails for a single tray, and the integrator should record
   that against the spec. Tag: general (an estimate that misleads when its assumption does not hold).

## Should fix

2. **Roll, Mark a half-life handle (src.html:117 snap):** the hint says "Drag the graph handle to 500 nuclei", but the
   handle snaps to the expected curve's value at each half roll, so for most dice it cannot sit at 500. On a d6 it
   jumps between 528 and 482 (its aria valuetext reads "528 nuclei; move to half the starting crowd"). The student is
   asked for something the control will not do. And because the line follows the expected curve, the tool picks the
   reading. Seen in f1/t04-d6-marked.png and the valuetext in the shots1 output. Better: snap y to 500 (or to steps of
   25) and let the card read the crossing on the tray. Tag: general.

3. **Roll, d20 (src.html:109, roll capped at 10):** the tray stops at roll 10, but a d20's half-life is 13.5 rolls. A
   d20 student never sees their own tray reach half, and the card falls back to "Expected crossing", even though the
   graph is drawn out to roll 16. The spec does not set this cap: "Roll to 10" is a button, not a limit. The
   comparison "bigger die, longer half-life" loses its slowest case. Seen in f1/t05-d20-marked.png (Roll once is
   disabled after roll 10). Better: let Roll once continue to the graph's end (16 for d20), or say on the card that a
   d20 needs more than 10 rolls. Tag: general.

4. **Roll, tray (src.html:109 roll, :112 drawTray):** the student never sees a 1 cause a decay. A die that rolls 1 turns
   gray in the same frame its face would appear, so no 1 is ever drawn. At 1366x768 the faces are also about 5 px and
   can't be read (f1/zoom-tray.png, cropped from t02). The rule card says "Every 1 has decayed", but nothing on screen
   shows it. Better: hold the new faces for a beat with the 1s outlined in the accent, then gray them, and draw faces
   at a readable size wherever the tray has room. Tag: general.

5. **Nucleus, drawing (src.html:126 drawNuclei):** the drawing gives two wrong pictures of a nucleus.
   - (a) The legend is split across the two halves: "Before: protons p+ (solid)" sits over the left nucleus and
     "Products: neutrons n (outlined)" over the right. It reads as "before is protons, products are neutrons", and
     neither color is visibly solid or outlined.
   - (b) Protons fill the center and neutrons form an outer shell, because the spiral layout colors the first Z dots
     as protons. That is a specific wrong structure. Small nuclei also show as scattered dots, where the spec asks for
     "packed".

   Seen in f1/t08-nucleus-default.png, f1/t11-f1-right.png and the audit's state-right-680x425.png. Better: one legend
   line with colored swatches ("● proton ● neutron"), protons and neutrons mixed through the cluster, and the dots
   packed. Tag: general.

6. **Nucleus, energy ladder (src.html:127 drawLadder):** the bars start from methane's value on a log scale with no
   tick marks. Methane looks like zero, and carbon-14 decay looks like more than half of fission, though it is about
   1/1,300 of it. The ratio line says "Log scale", but nothing on the bars shows the powers of ten. At 680x425 each bar
   is also drawn through the next rung's label ("D-T fusion" is struck through in the audit's
   state-right-680x425.png).
   This ladder is the energy half of HS-PS1-8 (the scale of nuclear energy against chemical energy), and the student
   only reads it. Better: ticks at each power of ten (1 eV, 1 keV, 1 MeV, 1 GeV), points or bars from a stated origin,
   and labels clear of the bars. Also give the student one action, such as placing the rung for the card they just
   balanced before it is revealed, so the energy comparison is something they do, not only something they are shown
   (BASELINE rule 2: taught well, not thinly). Tag: general.

7. **Dating lab, ruler (src.html:135 drawRuler, :132 "Close" test):** the ruler cannot be read closely enough for the
   10 percent "Close" check. It labels only whole halvings (13.6, 6.8, 3.4 and so on), so the two real samples fall
   between ticks with nothing to show the log spacing.
   - Reading 10.8 straight across from 13.6 to 6.8 gives 2,359 years against 1,906 (24 percent off).
   - Reading 9.07 the same way gives 3,817 years against 3,349 (14 percent off).
   - Both get "Compare with the halving ticks."
   - Every practice sample sits exactly on a labeled tick.

   So the Estimate step is either trivial (the practice samples) or a sweep: drag, press Estimate, repeat until
   "Close", free and unlimited. Recomputed in Python; seen in f1/t13-scrolls-calc.png and f1/t14-cave-noise.png.
   Better: minor activity marks between the ticks at their log positions (12, 11, 10, 9, 8, 7 dpm/g), and one Estimate
   per sample before Calculate. Tag: general.

## Polish

8. **Roll, tracked die and the "no memory" idea (src.html:106 updateRoll):** "Chance it decays next roll: 1 in 6" is a
   fixed string, so Done when 3 passes because the screen says so. Better: a line per roll from the crowd ("This roll:
   98 of 591 decayed, 17%"), so the student sees the same fraction at every age in their own data. Tag: general.

9. **Nucleus, N4 gamma:** gamma is one of the three decays HS-PS1-8 is limited to, but it appears only in words after
   Check. Better: show ⁰₀γ in the N4 equation once it is balanced. Tag: general.

10. **Dating lab, wDating welcome (spec line):** "Drag on the ruler to estimate, then press Calculate" skips the
    Estimate button, and Calculate needs Estimate first. The hint (hint12) has the steps in the right order. Better:
    "Pick a sample. Drag the ruler pin, press Estimate, then press Calculate." This is the spec's line, so the
    integrator decides. Tag: general.

11. **Sources line (tool.draft.json and notes.md "Good to know"):** 17.6 MeV and "about 200 MeV" are credited to
    OpenStax 21.4, but that page gives neither number. I fetched it on 2026-10-29. It gives the Ba-141 + Kr-92 + 3 n
    equation, fission at 1.8 × 10¹⁰ kJ/mol (186.6 MeV per event), and D-T fusion at 1.69 × 10⁹ kJ/mol with a mass
    loss of 0.0188 amu (17.5 MeV). The spec asked the builder to confirm these values against the page, and
    codex-report says the pages were not fetched. The values themselves are physically right (the D-T Q-value is
    17.59 MeV). Better: cite NNDC or another named source for the two MeV values, or mark them as derived.
    Tag: general.

## Nits

12. **Nucleus, positron (src.html:120 iso):** N5 shows ⁰₁e where the spec writes ⁰₊₁e. The plus sign helps students
    read it as a positron. Tag: general.
13. **Roll, Mark before any roll:** with no rolls yet, the card accepts a line read from the expected curve alone
    ("Expected crossing"). It does no harm, but the student's tray is skipped (f1/t06-premark-norolls.png).
    Tag: general.
14. **Rule 8, notes.md:** N3 to N5 name thyroid treatment, radiation therapy and PET scans. A teacher-note line saying
    these touch on cancer care (a student may have someone in treatment) would fit rule 8. Tag: general.

## Sensitivity referral (rule 5)

Low risk, for the integrator to route. The Dead Sea Scrolls (religious texts) and seeds from Tutankhamun's tomb (a
burial) are named samples. Both are OpenStax examples and are used factually. I did not judge them.

## Standards (rule 2)

HS-PS1-8 is the only code on the module.
- Changes in the nucleus: taught by balancing seven products. This is a real student action and it works.
- Decay over time: taught by rolling and marking. It works, with findings 1 to 4.
- Energy released in fission, fusion and decay compared with other changes: shown, not done (finding 6).

The code can stay once finding 6 gives the student an action. N5's positron decay goes past the standard's limit to
alpha, beta and gamma. That extension is fine and is not a finding.

## Done when

1. PASS. The d6 expected count at roll 10 is 161.5, and the mean of 20 runs stays within 5.59 of the expected curve at
   every roll (default seed, recomputed with my mulberry32 copy, which matches the tool's tray). The worst over 7 more
   seeds was 6.29.
2. PARTIAL. All seven exact half-lives match Content (1.000, 2.409, 3.802, 5.191, 6.579, 7.966, 13.513 rolls). But
   accepting a marked half-life within 0.5 rolls fails as a teaching check: correct lines are refused (finding 1), and
   a d20 is never read from the tray (finding 3).
3. PASS as written: the same "1 in 6" at ages 0 to 6 (f1/t07-track.png). See polish 8.
4. PASS. Check compares the mass and charge sums. They are linear, so exactly one (A, Z) passes per card. Seen right
   on N2 and F1 and wrong on N5 ("Charges: 9 ≠ 11"). The other products are fixed, so nothing beyond the sums the spec
   asks for gives the answer away.
5. PASS on content: four rungs and the 22 million ratio (200 MeV ÷ 9.2304 eV = 2.17 × 10⁷). How it reads is
   misleading (finding 6).
6. PASS. Ages are 1,906, 3,349, 22,920 and 53,916 years, with "Too old to date well" on the last. The noise run gave
   337 counts ± 18 and a range of 11,095 to 11,996 years (recomputed). At 340 counts: ±18.4, a range of 11,023 to
   11,921, matching the spec's rounded 11,020 to 11,920. The mammoth bone at 22,920 years correctly gets no flag.
7. PASS. Reset repeats the same tray (t24-seed returned true). Progress survived a fresh tab (3/7 cards, 4/7 samples),
   and Clear set it to 0/7, which stayed after a reload. For Motion off I cite the audit's clean row.
8. Cited from the audit: every size clean, the Enter-twice keyboard check ok, no console errors (also none in my 21
   driven shots). This lens did not re-shoot it.

Other numbers recomputed:
- Methane: 890.6 kJ/mol ÷ NA = 9.2304 eV per molecule.
- Per nucleon: fusion 3.52 MeV, fission 0.847 MeV.
- Ruler labels: 13.6/2^k, all correct (0.2125 shows as 0.212, which is fine).
- OpenStax 21.3 confirms the 5,730-year half-life, the 13.6 activity, the Scrolls at about 1,900 years, the
  Tutankhamun seeds at 9.07 and about 3,350 years, and the 30,000 and 50,000 year limits.

## Giveaways checked

- Nucleus: no hidden answer. The steppers start at 10 and 3, the element name follows the student's own Z, and Check
  gives only the sums the spec asks for.
- Dating: no age shows before Calculate, but "Close" can be found by sweeping (finding 7).
- Roll: the exact half-life prints on the card from the first drag. The spec wants that, but because of finding 1,
  "Accepted" can also be found by sweeping: drag until it appears.

## Language and guardrails

The language is plain and right for grade 10. The ln(ratio) steps are shown, never asked of the student. There is no
hard history and there are no points or timers. The health topics (thyroid treatment, radiation therapy, PET) are
neutral (nit 14).

## Cross-lens notes (not counted)

Sound starts off: the last lines of src.html call $('sound').click() at load. The spec asks only for the Geiger
clicks to start off, but as built no welcome is heard until the student turns Sound on. This is for Play and Craft to
settle under rule 4.

## Audit pilot

- **Leads confirmed:** at 680x425 the Dating handle's hit area overlaps "13.6" and "6.8", but only the invisible hit
  area does. The visible text is clear on the frames, so it is not a teaching issue. "Welcome not heard" after every
  first tap is real, and the cause is that Sound starts off (cross-lens note).
- **Leads that were wrong or empty:** in the marked state, "expected path drawn across Half-life line" is the curve
  meeting the line, not a defect. Clear "nothing changed" only because there was no saved progress yet; my t22 shows
  Clear takes 3/7 back to 0/7.
- **Missed:** the ladder bars drawn through their labels at 680x425 show in the audit's own frame
  (state-right-680x425.png), but its "lines drawn across labels" check did not flag them. It also missed the issues
  in this file, which are teaching, giveaway or meaning problems the audit does not claim to see:
  - the wrong acceptance feedback on a correct half-life line (1);
  - the handle that cannot reach 500 (2);
  - the d20 roll cap (3);
  - no 1 ever shown, and 5 px faces (4);
  - the split, mislabeled nucleon legend and the proton-core drawing (5);
  - the log ladder with no ticks (6);
  - the ruler that can't be read (7);
  - the source attribution (11).
