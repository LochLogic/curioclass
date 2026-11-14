# Frame read: world-history-ii (World History II, about 1800 to today, grade 10), 2026-11-13

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/social-studies.md, docs/courses/social-studies/STANDARD.md (sections 1 to
  4), docs/sources/BASE-TEXTS.md (the ETSU partial base).
- The frame docs/courses/world-history-ii/frame.md and its row in data/plans/frames.csv (`world-history-ii,11,160`).
  No source map: no base text, only a partial base not mapped lesson by lesson, as allowed.
- All 43 wh2-* rows of data/progressions/social-studies.csv.
- The anchor: every MA.WHII line of data/standards/ma-hss-2018.txt, lettered parts included.
- Frames before and after: docs/courses/world-history-i/frame.md (grade 9), docs/courses/civics-government-and-civic-life/frame.md
  (grade 8, the civic action hand-on), docs/courses/us-history-i/frame.md (grade 11), docs/courses/us-history-ii/frame.md,
  docs/courses/us-government-and-politics/frame.md and docs/courses/economics/frame.md (their "Picked up" tables).
- The cross-subject rows named (e9/e10-*, m6/m7/m8, s7, bio, chem): each exists in data/progressions. No ELA 10 or
  chemistry frame exists yet.
- Earlier reads: docs/reviews/progression-social-studies-2026-11-13.md (and its Codex read and fixes), the other
  social studies frame reads of today, and DESK-ANSWERS 2026-11-13 on the genocide anchor as the frame cites it.
- Gates: `python -X utf8 scripts/plan.py check` (frame world-history-ii: 0 failures; 11 units, 160 days, 150 in
  units, 10 checks and respond days). `python -X utf8 scripts/stale.py check`: 19 files, 0 failures.

## Verdict

The frame is sound in content and order: every WHII code sits in a unit, the units run from 1800 to today with a
reason for the one thematic unit, every World History I hand-on is picked up and every hand-on to US History I, US
History II, Government and Economics lands where those frames say, and the hard-history units are guarded with care.
The biggest risk is time: unit 10 (Rwanda in depth, Srebrenica, a case survey, the Convention's definition and
terrorism) has 9 days and unit 8 (decolonization in depth, apartheid, eight parts of Israel and Palestine with more
than one account each, and social movements) has 13. The one change that matters most is to move about three days
into those two units from units whose rows repeat World History I or are lighter.

## Findings, most serious first

### 1. Units 10 and 8 are under their share of days (moderate; judgment call)

**What is wrong.** Unit 10 holds wh2-genocide-atrocity (the 1948 definition, Rwanda in depth with the tribunal,
Srebrenica with the ICJ and ICTY findings, a brief survey of the other cases with warning signs) and wh2-terrorism
(al-Qaeda, the Taliban, ISIS, and "one government response evaluated from evidence, including the debate over civil
liberties"), plus its end-of-unit task, in 9 days. A plain count: definition 1, Rwanda 4, Srebrenica 1 to 2, survey 1,
terrorism 2 to 3, assessment 1 gives 10 to 12. Unit 8 holds four rows and five codes in 13 days, one movement in
depth, and MA.WHII.T5.7 with eight lettered parts, each contested event "in more than one account"; Israel and
Palestine alone needs about 4 to 5 days to do that honestly. The frame's own pick (For the lead 2) keeps 9 days on the
ground that earlier units taught the definition's history; that covers the definition day, not terrorism or the depth
case. Its fallback (move wh2-terrorism to unit 9) would put a sixth row into unit 9's 12 days.
**Why it matters.** These are the units where a rushed day does the most harm: survivors' testimony, the court
record and the multi-account rule all need time, and a writer short of days cuts the second account first.
**Fix (frame, Units and Course-level checks week ranges).** Unit 10 from 9 to 11 days and unit 8 from 13 to 14,
taken from unit 1 (16 to 15: MA.WHII.T1.1b and c become recall, finding 3), unit 2 (12 to 11: three rows) and unit 3
(14 to 13: wh2-colonial-culture is the lightest row). Recompute the week ranges. If Cory prefers, the frame's own
alternative of a 165-day year does the same. LAYER frame. REPEAT yes (the grade 5 frame read, finding 3: one unit short
for what it holds, another with days to spare).

### 2. "Check set adds" lists four items the course already owns (minor; firm)

**What is wrong.** Candidates the unit plan may drop include owned content: unit 5's "Japan's militarism and the
Manchurian Incident" is MA.WHII.T4.10c (wh2-road-to-war teaches it); unit 6's "The bombing of cities on both sides" is
T4.15a (wh2-wwii-consequences); unit 10's "Cambodia under the Khmer Rouge" and "Darfur" are options T7.1c and T7.1e
of the owned survey.
**Why it matters.** A busy unit writer who drops a candidate drops owned content with it.
**Fix (frame units 5, 6 and 10).** Strike the four items from "Check set adds", or relabel each "owned (code), named
here for depth only". If unit 5 needs an addition, the college-level framework's three roads to war can stay as the
framing, with T4.10c named as owned. LAYER frame. REPEAT yes (the grade 5 frame read, finding 1).

### 3. Unit 1 reteaches World History I's absolutism without saying so (minor; firm)

**What is wrong.** wh2-states-and-absolutism marks MA.WHII.T1.2 (England as the exception) as recall of
MA.WHI.T6.3, but MA.WHII.T1.1b (Louis XIV and Versailles) and T1.1c (Peter the Great) repeat MA.WHI.T6.2b and c,
which wh1-philosophies-of-government taught in grade 9 unit 10. Only Westphalia (T1.1a), serfdom's spread and the
rise of Prussia, Poland and Sweden are new.
**Why it matters.** Louis XIV and Peter get taught twice at the same depth in consecutive years; the new parts get
squeezed in a row the frame calls light.
**Fix (row notes and frame unit 1).** Add to the row: "T1.1b and c are recall of wh1-philosophies-of-government
(T6.2b and c), opened with a retrieval task; new here are the Thirty Years War and Westphalia, serfdom's spread, and
Prussia, Poland and Sweden." Unit 1's "What students learn" says the same. This frees the day finding 1 uses. LAYER
progression and frame. REPEAT new.

### 4. The wh1-black-death hand-on is labelled as content, not as the skill it carries (minor; firm)

**What is wrong.** The "Picked up" table calls wh1-black-death to wh2-wwi-causes "next grade, direct". The link is a
skill link (weighing several causes, the multi-cause chain), which the row's own notes say; World History I's frame
says the same. US History I labels its matching link "skill link, opens with a worked example".
**Why it matters.** A writer reading "direct" plans a Black Death retrieval opener for the First World War unit.
**Fix (frame "Picked up" table).** Kind: "skill link (multi-cause chain), opens with a worked example". LAYER frame.
REPEAT new.

### 5. Stale note: the frame is written, but flow-status says "Writing" (minor; firm)

**What is wrong.** data/plans/flow-status.csv reads `frame:world-history-ii,active,...,"Writing: ..."`.
**Fix.** Note: "Written; expert read 2026-11-13 (docs/reviews/frame-world-history-ii-2026-11-13.md)". LAYER process.
REPEAT yes (stale notes in earlier reads).

## Checked and found right (do not undo)

- **Owned skills.** All 43 rows sit once; review uses are named as review. The C3 indicators split cleanly with World
  History I (D1.2 and D1.3 here, D1.1, D1.4 and D1.5 there; D2.His.10, 13, 17 and D3.2 here, D2.His.9 and 12 there).
- **Standards in full.** Every MA.WHII code and lettered part I traced is in its row: T1.1a to c, T2.3 (Owen, Marx),
  T3.2a and b (slavery's capital, with the historians' debate on its size), T3.4a to f, T4.2a to c, T4.3a to i, T4.7a
  to d, T4.10a to d, T4.13 (Roma and LGBT people), T4.14 (the effect on Soviet relations), T4.15a to f, T5.3a to h,
  T5.7a to h, T5.9 (oligarchic power), T5.11 options, T6.5a and b, T7.1 options.
- **Order.** Revolutions before industry (the Atlantic thread closes first), industry before empire, nationalism before
  the war it helps cause, the Russian revolutions inside the war, the Depression before the dictators, the Holocaust
  after the war's course and before the human rights answer to it, Israel and Palestine after the Holocaust it needs
  (T5.7b), the Middle East since 1980 after units 7 and 8.
- **Days, apart from finding 1.** 3.5 days a row; the heavy rows are weighed one by one in the frame; the week
  ranges add up to 32 weeks.
- **Seams.** Every World History I hand-on (16, plus ss8-civic-action) is in the "Picked up" table, and every hand-on
  from here appears in the US History I, US History II, Government and Economics frames in the unit named.
- **Values and hard history.** Court findings decide where courts ruled (Rwanda, Srebrenica, Nuremberg); the Armenian
  genocide as the scholars' finding, denial studied as denial; Haiti as self-liberation; Israel and Palestine with
  1948 named both ways, Jewish refugees from Arab countries named, both peoples present tense; climate change as the
  science shows; no simulations, no "what would you do"; a student with family ties to a case gets a choice.

## Cross-subject

Same-year leans on ELA 10 (RL.9-10.6, RI.9-10.8, W.9-10.1, W.9-10.7, SL.9-10.4) and chemistry 10 (HS-PS3-3,
HS-PS1-8, HS-ESS3-5), each with a pick or a local bridge (the fission paragraph is the right size); earlier-year
leans on math 6 to 8, science 7 and biology 9 need only retrieval. Every row named exists. No ELA 10 or chemistry
frame exists, so "taught first" cannot be checked; the shared research brief (weeks 29 to 32) and the hard-week list
give those frames what they need. If finding 1 is applied, the hard-week list moves: unit 10 becomes about weeks 28 to
30.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| An anchor standard in the course's Massachusetts topic range has no unit | Met (WHII.T1 to T7 all placed) |
| The replaced grade 3 year, or "your state" in grade 8, keeps Massachusetts-only content | Not applicable |
| No unit lists what the check set adds, or an addition has no recorded source | Met: every unit lists additions with their member (finding 2 is four owned items among them) |

## What I could not judge

- The ELA 10 and chemistry frames (not written).
- Accuracy of the genocide, Holocaust, Israel and Palestine and colonial content (sensitivity read and a qualified
  reader, as the frame flags).
- Whether the ETSU chapters cover events after 2022 well enough; the frame already says current events come from
  other dated sources.

## Settled by the expert

None. Finding 1 moves days between units, which changes what several units can hold; the caller or Cory decides it.

## For Cory

- **Days (finding 1).** Either move about three days into units 8 and 10 from units 1 to 3 (my pick), or take the
  frame's 165-day alternative. Both keep every standard where it is.
- **People.** Units 3, 4, 6, 8 and 10 need a qualified person's read before any unit ships (FOUNDATION 7.3).

Not logged in the defect ledger (`plan.py defect`): the brief allows edits to this report only. The caller may log
findings 1 to 5 with found_by `expert`.

## Sources

No outside source was fetched for this read; it rests on the repository files above and memory.
- Massachusetts 2018 as coded in data/standards/ma-hss-2018.txt (WHII.T1 to T7, lettered parts).
- Day estimates for unit 10 and Israel and Palestine: my own reckoning as a teacher of the grade (judgment call).

## For the source list

Nothing new.
