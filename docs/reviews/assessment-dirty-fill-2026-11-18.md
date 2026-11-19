# Assessment: a dirty fill of every core course, then two refines (2026-11-18)

Cory's question (2026-11-18, after the confirm probe): fill every section plan and day from beginning to end, so each
one is written with the earlier ones in hand and can look back; accept that this first pass is dirty; then refine the
whole course from beginning to end, then refine it again.

Numbers are tagged:
- MEASURED: taken from the probe token files and reads.
- DERIVED: calculated from the measured numbers.
- ASSUMED: a guess, to be tested.

## Scope

- 52 core courses have unit plans (399 units). Their days.csv files hold **7,544 planned days** (MEASURED, grade 4
  math and grade 6 ELA left out). The split is ELA 2,080, social studies 2,016, math 1,920 and science 1,528.
- About 50 days are written so far, and 21 section plans exist.
- The other 53 active courses have no scope and sequence yet, so they cannot be filled. This plan covers the core.

## Cost

Per day, from the confirm probe (MEASURED, docs/reviews/probe-confirm-tokens-2026-11-18.csv):

| Stage | ELA grade 11 | Science grade 7 |
|---|---|---|
| Fill: section plan + plan data + day writing | 18k + 24k + 43k = **85k** | 15k + 19k + 15k = **49k** |
| Refine: answer-key read + expert read + fix | 35k + 16k + 41k = **92k** | 29k + 38k + 43k = **110k** |

Whole core, DERIVED:

| Pass | Tokens |
|---|---|
| Dirty fill | 380M to 640M |
| Refine 1 | 690M to 830M |
| Refine 2 (ASSUMED: about half the fixes of refine 1) | 550M to 700M |
| **Total** | **about 1.6B to 2.2B** |

- **Per course,** at 145 days on average: about 10M for the fill and 13M to 16M for each refine, so roughly 35M to 45M a
  course.
- **Against option (b) on the Desk** (scale with reads on every section): (b) is about 1.3B to 1.5B (174k to 195k a finished
  day, MEASURED, times 7,544). The plan here is (b) plus one more whole-course refine, at about a quarter to a half
  more cost.
- **Refines are the expense.** The fill is the cheap part: 25 to 30% of the total.

## What it gains

1. **Look-back is real, and it targets the faults that are left.** The probes kept finding faults at section and day
   edges:
   - notation tested before the day that teaches it;
   - hand-backs sent into the next section with no slot;
   - terms that drift on a reused passage;
   - retrieval of something never taught.

   A writer holding the actual earlier days, not only the plan, avoids most of these by construction. Parallel waves
   cannot.
2. **The refine sees the whole course.** A front-to-back read can check what a section read cannot: the arc, repeated
   cases, whether every end item was taught, pace across units, and the same skill taught twice.
3. **The data supports more than one read.** In the confirm probe, the answer-key read fixed 13 faults in each course.
   On the same days, the expert read then found 13 (ELA) and 22 (science) more (MEASURED). One pass leaves a lot, so a
   second pass is not waste. Whether refine 2 still finds enough to pay for itself is unmeasured.
4. **It ends the probe loop.** Plan share has been Off in five probes for different reasons each time. The refines fix
   plan faults and day faults in the same pass, so the gate stops blocking the work. The plan-share line was a guard
   against scaling bad plans. Here the guard becomes two refines, and the cost of that is paid in tokens.

## What it risks

1. **Errors spread forward.** This is the main risk, and look-back makes it worse. In the probes the leading fault was
   wrong item keys at plan data, such as the solid escaping where the particles do. In a dirty fill:
   - the day copies the key;
   - later days retrieve from that day;
   - the course final leans on it.

   One fault becomes several places to fix.
2. **Fixes cascade into stale days.** Every refine fix to an earlier day can make later days stale (stale.py flags
   them). Refine 1 then has to choose: fix forward in the same pass (slower, and context grows), or leave a stale list
   for refine 2. Refine 2 then becomes partly a repair of refine 1.
3. **Context grows along the course.** Day 150 cannot hold days 1 to 149. Look-back needs a running course ledger
   (terms, notation, cases used, items, what was taught on which day) that each writer reads and appends to. That
   ledger is new work and is not built yet. Without it, "look back" means the previous section only.
4. **It is serial within a course.** Each course is one lane, written front to back, so the only parallel work is
   across courses. A slow or stuck course holds its own lane only.
5. **A read of a dirty draft anchors on it.** A reader fixes what is there; it rarely rebuilds a weak day from
   scratch. A day that is wrong in shape (wrong activity, wrong pace) can pass two refines with polished prose. The
   probes saw no such day, but they ran on cleaner input (ASSUMED risk).

## What I would change

These are small changes, and they keep the plan as Cory described it:

- **Pilot one whole course first.** Science grade 7 or ELA grade 11, 160 days each, about 40M tokens. Unit 1 is
  already started in both. The pilot measures what this plan rests on, and none of these has a number yet:
  - how much look-back cuts the edge faults;
  - how many fixes cascade into stale days;
  - what refine 2 finds after refine 1.

  This is the skeleton note's own lesson 7: pilot one course, then run the rest.
- **Keep the cheap answer-key check inside the fill,** at plan data, before any day is written. Keys are the biggest
  fault that spreads, and catching one before days lean on it is much cheaper than fixing it in five places later.
  This raises the fill by about 30k a day (about 230M across the core), but it should shrink refine 1. A pure dirty
  fill without it is the alternative.
- **Build the course ledger before the fill.** One file per course. Each section writer reads it and appends to it.
  plan.py checks that every term and notation a day uses is in the ledger at or before that day.
- **Set the stop line for refines in advance.** For example, refine 2 runs on a course only if refine 1 found more
  than one firm fault a day. A course is done when an expert read of 10 sampled days finds no firm fault. The pilot
  sets the numbers.
- **Mark every dirty day as a draft.** The site is not public, so nothing leaks, but a teacher-facing build should
  never show a day that has not been through refine 1.

## Recommendation

Do it this way: pilot one course end to end (fill, refine, refine), then fill and refine the core in lanes, one lane
per course. Build the ledger and keep the answer-key check in the fill.

This replaces the probe gate: q-probe-confirm-1 is answered by the pilot, not by another probe. If the pilot's refine 2
finds little, drop refine 2 for the rest and save about 600M tokens.

Not settled here, and Cory's call: the total spend (1.6B to 2.2B tokens over the core), and which pilot course.
