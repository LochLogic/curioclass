# Sequence read: social-and-emotional-learning-grades-9-to-12 (2026-11-26)

Expert read of the scope and sequence for SEL 9 to 12, by a fresh Claude agent that did not write it. I read it as a high school SEL teacher, using docs/pipeline/briefs/sequence-read.md and build/scope-writes/AFTERCORE-READ.md. This report is the only file I edited.

## What I read

- build/scope-writes/AFTERCORE-READ.md and AFTERCORE-BRIEF.md (the writer's notes: no grading or credit claimed in 9 to 12, partners never play an unkind part, settled cases not repeated within the band, shared cards quoted word for word from STANDARD section 7, no source-map, the For the lead route).
- docs/pipeline/briefs/sequence-read.md, sequence-write.md (rules 1 to 11), docs/agents/EXPERT.md, docs/agents/lenses/sel.md.
- docs/courses/social-and-emotional-learning-grades-9-to-12/scope-and-sequence.md, all of it.
- data/plans/social-and-emotional-learning-grades-9-to-12/days.csv, all 256 rows. I read every Check, Respond and grade 9 and grade 12 note in full, and sampled the grade 10 and 11 two-group units.
- From frame.md: the course in brief, the Units table (lines 141 to 168), Course-level checks (170 to 183) and the Base text list. I did not read Seams, Cross-subject or the frame's For the lead in full.
- data/progressions/sel.csv (the g12 rows and their notes) and data/standards/casel-5.txt (our-words text of all 40 codes).
- docs/courses/CALENDAR.md and data/plans/calendar.csv, for SEL 9 to 12 and for the cross-subject weeks the notes lean on: ELA 9 to 10, Health 9, PE 9 to 12, US History I and II, Economics, Geometry, Computer science 11.
- To check the "deliberate return" on day 85, the SEL 3 to 5 and 6 to 8 frames, only as far as which settled cases they name.
- Gates:
  - scripts/sequence.py check: 0 failures. It notes "standard None is on no day" for units 1 to 18, which is harmless and is already the writer's For the lead 5.
  - frame.py check: 0 failures (24 units, 256 days).
  - frame.py calendar: no break. The course checks sit in weeks 15 and 32.
  - plan.py check: failures in other courses only (algebra-ii), none here.
  - stale.py check: 121 files, 0 failures.

## Verdict

The scope is sound in its structure, calendar, cross-subject leans and guards, and it passes every gate. Its most serious gap: three owned grade 12 codes each have one half that is never assessed, and the first of those halves is never taught either. They are RS8 (offer help), SO6 (different unwritten rules in different places) and RD3 (problems in your own life). The ten-day shorter path also folds away the only rehearsal of several sub-skills, among them the owned SM6 and SO7, and each one goes the day before an assessed Application. The fixes are small and sit inside the units, so this is a revise, not a rewrite.

## Findings, most serious first

1. **RS8's "offer help" half is neither taught nor assessed in the owner year.**
   - What is wrong: casel-5 RS8 reads "Ask for help when you need it, and offer help when others do". The frame's unit 24 row and the g12-rel-ask-offer-help progression row both include planning an offer of help to a new coworker or roommate. In the scope, day 246 (Understanding) teaches only the ask, day 247 rehearses only the ask, day 248 judges SM4 and RS2, and the day 255 page is "support map and one-year goal". No item asks a student to plan or make an offer.
   - Why it matters: an owned id is claimed while only half of it is taught, and that breaks "each part of each code is asked".
   - Fix: on day 246, change the goal to "ask for help, and plan an offer of help to a new coworker or roommate". On day 247, add one offer round to the rehearsal, with the partner as the newcomer who accepts. On day 255, add one prompt: "Write the offer you would make to a new roommate who seems stuck, and when you would make it."
   - LAYER sequence. REPEAT yes (unasked part of a claimed id). Confidence high.

2. **SO6's "different places, different unwritten rules" half is taught once and never rehearsed or assessed.**
   - What is wrong: SO6 reads "Notice that places and groups have different unwritten rules, and that some of those rules were not fair". Day 224 teaches the two-settings comparison. Day 225 rehearses only fairness and the invented bus-stop rule, and day 226 judges SO8. The items on days 233 and 255 ask only whether a rule is fair, who it touches and what route would change it.
   - Why it matters: the owned id is assessed on its second clause only.
   - Fix: on day 225, add one round where students compare the unwritten rules of two invented settings (a workplace break room and a dorm floor, say) before the fairness round. On day 233, add one prompt asking the student to name one unwritten rule that differs between the two settings and say how a newcomer would learn it.
   - LAYER sequence. REPEAT yes. Confidence high.

3. **RD3's "own life" half is not in the evidence.**
   - What is wrong: RD3 says "in your own life and in your community". Day 243 judges only the class community fix, which is a group product, and day 244 adds nothing personal. The day 242 rehearsal on the bus-route problem is never assessed.
   - Why it matters: an owned id is judged on a group product alone, with no per-student evidence on the personal half.
   - Fix: on day 243, give each student a fresh invented own-life problem (for example, a part-time job schedule that clashes with a family duty), solved on the same steps and marked per student, while the community fix stays as the group part. Or put that item on the day 244 page.
   - LAYER sequence. REPEAT yes. Confidence high.

4. **The shorter path's fold-ins cut sub-skills' only rehearsal.**
   - What is wrong: the scope says each folded second Fluency's "rows are already taught and rehearsed on the Fluency day before it". For many of them that is not true. In two-group units the second Fluency often holds a sub-skill's only rehearsal:
     - day 3: SA7, and the SM3 rewrite
     - day 7: saying the RS8 ask aloud
     - day 28: RS3, including the custom the unit cites
     - day 71: SO8
     - day 77: the RS8 offer, in grade 10
     - day 81: SM7
     - day 152: RD4
     - day 156: SA6
     - day 216: SM6, owned
     - day 220: SO7, owned

     The fold moves that rehearsal into the first ten minutes of the Application. Often that is an assess=end day, so practice gets cut down right before the assessment.
   - Why it matters: AFTERCORE-READ requires the shorter paths to hold with no assessed or owned part cut. Here an owned skill's practice is cut before it is judged.
   - Fix: in each two-group unit, make the first Fluency rehearse every sub-skill in the group, and make the second Fluency a changed case for all of them. That makes the fold safe and the claim true. If the expert prefers otherwise, pick fold-ins that are not the last rehearsal before an end day. Either way, rewrite the shorter path claim so it is true as written.
   - LAYER sequence. REPEAT yes (fold-in safety). Confidence high on the facts, medium on which fix is best.

5. **Retrieval often comes after the new form is taught.**
   - What is wrong: there is one retrieval item per opening, and a group's assumed rows are spread across its Understanding, Fluency and Application. So two of every three rows are retrieved after the grade's new depth has already been modeled, and often on an assessed Application day. Examples: days 3, 34, 45, 48, 56, 59, 226, 229, 240, 248 and 251.
   - Why it matters: retrieval is there to warm up the earlier form before it is built on. Retrieving it afterwards turns it into a review, and on end days it eats the calm start.
   - Fix: let the group's Understanding opening hold one retrieval item with a short prompt for each assumed row (about 5 minutes). Or place those retrievals in the openings before the group (the prior Application or Respond). Keep the calm start on assessed days.
   - LAYER sequence. REPEAT yes. Confidence medium.

6. **Two Checks claim codes their items do not ask.**
   - What is wrong: day 9 claims SM5, but its page is a support map and a focus plan only. Day 137 claims SA1, but both its page and the day before's rehearsal are about SA4.
   - Why it matters: "Checks claim only what they sample."
   - Fix: on day 9, add one prompt on a planning system (for example, "Show where this week's three deadlines go in your planner and when you check it"). On day 137, add an identity-under-pull prompt ("Name one part of who you are that a group pushed you to hide, and what you did"), using the invented-case option for disclosure. Otherwise drop SM5 and SA1 from those rows.
   - LAYER sequence. REPEAT yes. Confidence high.

7. **The widened course checks are overloaded.**
   - What is wrong: on days 30/31 and 63/64 of each year, the unit page plus two sampled multi-part items must fit into the same 20 minutes a normal Check gives one page. Day 255 is the extreme. It holds RS8 and SM4, SO6 and SM7, RD2 and RD5, plus the rehearsal.
   - Why it matters: a rushed final check yields thin evidence on the owned codes it is the only home for.
   - Fix: set the time split in each course check note: the unit page in about 12 minutes, then two short sampled items in about 4 minutes each, one prompt per part. Also say in the 30-minute path how the widened checks fit.
   - LAYER sequence. REPEAT yes. Confidence medium.

8. **The leave-out bridge for unit 1 omits the support map.**
   - What is wrong: day 11's bridge for schools that skip unit 1 does not give the support map. Unit 2 uses it on days 17 to 19 and unit 4 on day 39, and the frame names the support map as a unit 1 bridge.
   - Fix: add the support map's one-step form to the day 11 bridge, and to day 32, where units 1 and 2 are both left out.
   - LAYER sequence. REPEAT yes. Confidence high.

9. **Minor items.**
   - Unit 23's "evidence points" line lists RD1 twice and leaves RD2 off the Applications. Correct the list.
   - Days 217 and 243 "carry out" a service project or a fix inside one session. Say it runs between sessions, as unit 2 does.
   - SM7 "together": the grade 12 owner year has only an individual plan. The "together" part was met in the grade 9 and grade 11 proposals. This is a judgment call (see the table).
   - Day 85 calls Brown a "deliberate return" to the SEL 3 to 5 grade 5 case. That is a repeat across bands, not within this band, so it does not break the brief. It is fine if the expert keeps it.

   LAYER sequence. REPEAT new. Confidence high on the first two, medium on the rest.

## Right, do not touch

- school_day, from the formula 160*(grade-9) + 5*(week-1) + 2 or 4. It puts every unit and both course checks of each year in the weeks the frame and CALENDAR.md give (weeks 15/16 and 32, finals).
- The cross-subject leans. All match calendar.csv. Examples:
  - The ELA 9 argument evaluation comes before SEL unit 5.
  - US History I unit 6 comes before Morgan.
  - US History II unit 7 runs in the same weeks as Heart of Atlanta, with a two-sentence facts bridge where it comes later.
- Ownership. Every grade 12 owned code (all 40 CASEL codes plus AASL V.D.1, V.D.2 and III.D.2) has an end Application or Check day, apart from the halves in findings 1 to 3. No owned id is claimed outside the frame's owned rows.
- The 31 owned codes that are on no course check have a valid named reason (the frame's two-item cap) and owner-unit evidence.
- Settled cases: one a year, none repeated within the band, each with the affected community named and a sensitivity read first. History is left to social studies, and current political disputes are kept out.
- The guards. Role plays never cast a student as victim or perpetrator, and partners never play an unkind part. Disclosure prompts always offer an invented option. Customs come from invented partners, never a whole culture. There are no clinical words, no product names, no exit that asks for a feeling, and growth mindset is "never belief alone".
- The shared cards are quoted word for word: the I-statement "I feel ___ when ___ because ___. I need ___. Does that work for you?" and the refusal second push "say it again, move away, tell".
- No grading or credit is claimed in 9 to 12.

## Could not judge

- I did not open the source pages, so each is marked browser check:
  - uscourts.gov (Mendez)
  - archives.gov and brownvboard.org (Brown)
  - lva.virginia.gov changemakers (Morgan)
  - loc.gov Civil Rights Act exhibition (Heart of Atlanta)
  - Oyez 328us373 and 1964/515, which the frame already marks browser check
  - the DHCC communication tips page
  - the Colorado CDE field trip checklist

  The case facts as the notes state them (dates, the 1954 ruling told apart from its slow, resisted rollout, interstate passengers, the 1964 Act) match what I know. Their currency on the pages themselves is not checked.
- The frame's Seams and Cross-subject sections, read only as far as the notes cite them.
- Whether a teacher can actually fit the widened course checks into the period without rehearsal (finding 7).

## Settled by the expert

| Question | Pick | Why |
|---|---|---|
| Fold-in fix (finding 4) | First Fluency rehearses every sub-skill; second Fluency is a changed case for all | Makes any fold safe without re-choosing days |
| Retrieval placement (finding 5) | One opening item with a prompt per assumed row, on the group's Understanding day | Warms all rows before new depth; keeps calm starts on end days |
| Course check time split (finding 7) | Page about 12 minutes, two sampled items about 4 minutes each | Fits 20 minutes and keeps per-part evidence |
| SM7 "together" in the owner year | Accept the grade 9 and 11 group proposals as evidence; no change | The part was taught and assessed; the grade 12 plan deepens the individual part |
| SO6 settled-case part | Not assessed separately; fine | The case is context for the rule, not an item |
| Day 85 cross-band return to Brown | Keep | The brief bars repeats within the band only, and the new depth is named |
| AASL begun-id and progression-cell question | Leave with the lead (writer's For the lead 4) | It is a frame and progression call, not a sequence call |

## For Cory

- None. Every finding is a fix inside a unit, with no scope, money, people or audience call.

## Lens checklist

- Self-management and relationship skills practiced, not only discussed: met.
- A skill's name and steps kept the same across units: met.
- Health topics left to health: met.
- No clinical words: met.
- Disclosure prompts offer an invented option: met.
- No role play casts a student as victim or perpetrator: met.
- No exit asks for a feeling: met.
- No product names: met.
- Growth mindset not taught as belief: met.
- Each part of each code is asked: missed (findings 1, 2, 3).
- Checks claim only what they sample: missed (finding 6).
- Every owned id is on a day, and none is claimed outside the owned rows: met.
- school_day in the frame and calendar weeks: met.
- The shorter paths hold with no assessed or owned part cut: missed (finding 4).
- Course checks never repeat a task form from the last two weeks: met.
- Rule 3 (every owned code is on a course check or has a named reason): met.
- Sensitive topics, cultural practices, safety and the shared cards follow the frame's guards: met.
- Named cases, facts and sources accurate and current: not fully judged (browser check).

## Stale notes

scripts/stale.py check: 121 files, 0 failures. Nothing stale touches this course.

## Sources

- data/standards/casel-5.txt (CASEL 5 in our words), docs/courses/sel/STANDARD.md section 7 (shared cards) and the frame's Base text list. No outside page was opened in this read.

## For the source list

- None new. The frame's URLs stand, with the browser check marks listed above.
