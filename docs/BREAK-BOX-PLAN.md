# Break Box: school-break activities (plan)

Status: DRAFT content, added 2026-10-31 (Cory). Track 2, Supply Closet, in docs/ROADMAP.md. Not on the site yet.
"Break Box" is a working name.

## Why

When school lets out for a week, two weeks or the summer, many parents still work. Kids end up at home, bored, and
on screens. The Break Box is a shelf of one-page activity sheets a family can print or hand over. Each sheet is
something a child can do in **one to two hours**, built on **fun and imagination**, with things already in the house.

It is the home cousin of Sub Day. A Sub Day packet lets a substitute run a lesson with no prep. A Break Box sheet lets
a kid (or, in K-2, the grown-up at home with them) start a real project with no prep.

## What it holds

- **30 ideas per grade, K through 12: 390 sheets.** The drafts are in `docs/break-box/`, one file per grade
  (`grade-k.md`, `grade-1.md` ... `grade-12.md`). Each file opens with an index of its 30 ideas.
- No idea repeats across grades. A theme can come back later only as a clearly older project (a K box rocket, a
  grade 7 trebuchet).
- `python scripts/check_breaks.py` checks every sheet against this plan (below).

## Who reads the sheet

| Grades | Written to | Reading level |
|---|---|---|
| K-2 | The grown-up or older sibling at home, who reads it and runs it. A short **Read aloud** part speaks to the child. | Plain adult prose. Read-aloud lines are short, simple sentences. |
| 3 | The child | Short sentences (about 10 words), everyday words, one action per step. |
| 4-5 | The child | Sentences under about 15 words. A new word gets a quick meaning in the same sentence. |
| 6-8 | The child | Natural middle-school voice. Clear, a little playful, never babyish. |
| 9-12 | The teen | Talks to them like a capable near-adult. Real techniques and real vocabulary. |

Every sheet ends with a **For the grown-up** part written to the parent, at any grade.

## The sheet

Every sheet has the same parts, in this order. This is the framework the site page will be built from later.

```
## 7. Ice Rescue

| Kind | Time | Where | Mess | Grown-up | Players |
|---|---|---|---|---|---|
| Science | 60-90 min | Indoors | Medium | With you | 1+ |

**Materials:** small plastic toys, a muffin tin or plastic containers, water, a freezer, salt, a squeeze bottle or cup, warm water, a towel

**Nice to have:** food coloring, a turkey baster, a magnifying glass

**Get ready the night before:** ...        (only when needed)

### The big idea
### Goals
### Objectives
### Get ready
### Steps
### Make it yours
### Stuck?
### Show it off
### Clean up
### For the grown-up
```

### The info row

| Column | Values |
|---|---|
| Kind | Build, Story, Art, Pretend, Science, Game, Puzzle, Music, Move, Outside, Kitchen, Kindness |
| Time | A range inside 45 to 120 minutes, written `60-90 min`. The center of the range is 60 to 120. |
| Where | Indoors, Outdoors, Either |
| Mess | Low, Medium, High |
| Grown-up | **With you** (a grown-up does it alongside), **Nearby** (a grown-up is home and checks in), **On your own** (fine alone; tell someone what you are doing) |
| Players | `1`, `1+` (works alone, better with others), `2+` (needs a partner) |

### The parts

1. **The big idea.** The hook, 2 to 4 sentences, written to the child at every grade (in K-2 it is labeled
   "Read aloud:"). It should make a kid want to start.
2. **Goals.** 2 or 3 bullets: what the child will have made or done by the end. The fun outcome.
3. **Objectives.** 3 bullets that start "I can" (grades 3-12) or "Your child can" (K-2): the skills the project
   builds, each one something you could see.
4. **Get ready.** Setup, about 5 to 10 minutes: clear a space, gather materials, anything to do first.
5. **Steps.** 5 to 9 numbered steps, with rough times in parentheses on the longer ones. The middle steps leave room
   for the child's own choices; they never turn into "copy this".
6. **Make it yours.** 3 imagination twists that change the project, not just decorate it.
7. **Stuck?** 2 or 3 fixes for the most likely problems ("The tower falls over: ...").
8. **Show it off.** How it gets shared: a show for the family when they get home, a photo, a tour, a performance.
   Never online.
9. **Clean up.** One or two lines. Cleanup is part of the project.
10. **For the grown-up.** Written to the parent: what this builds (school subjects and skills, in a sentence or two),
    any safety notes, and one **Ask at dinner** question that gets the child talking about it.

## Rules for every sheet

1. **Fun first.** Imagination, play and making things lead. Learning rides along; the sheet never feels like
   homework. No worksheets, quizzes or drills.
2. **Stuff from home.** Materials a typical house has: paper, tape, scissors, cardboard and recycling, kitchen
   staples, old clothes, outdoor things. Nothing to buy. Anything less common goes under **Nice to have**, and the
   project still works without it.
3. **Screen-free.** No device needed. A phone may appear only as a nice-to-have (a timer, a photo for the family),
   never as the core of the project.
4. **Works alone.** At least 20 of each grade's 30 are `1` or `1+`. A `2+` sheet names who the partner can be
   (sibling, grown-up after work, a friend over).
5. **Safe for the age.**
   - K-2: a grown-up is present for every sheet (they cannot be home alone). Grown-up does any cutting with sharp
     tools, any heat, and anything with small parts for kindergarten. No balloons under 8 (choking risk).
   - 3-5: "Nearby" at most for anything with scissors, glue guns (grown-up only), the oven or stove (grown-up with
     you), or going outside past the yard.
   - 6-8: stove, oven and kitchen knives with permission and a grown-up checking in. Leaving the yard only with
     permission.
   - 9-12: tools and cooking on their own with permission; tell someone before going out.
   - Never: fire, matches or candles, button or coin batteries, chemicals beyond normal kitchen and laundry items
     (no mixing cleaners), climbing on roofs, or meeting strangers. Kitchen sheets remind the grown-up to check
     allergies. Nothing with peanuts by default.
6. **Variety.** Each grade's 30 cover at least 3 Build, 3 Story, 3 Art, 3 Science, 3 Pretend (or drama), 3 Game or
   Puzzle, 3 Move or Outside, 2 Music, 1 Kitchen and 1 Kindness. At least 6 can be done outdoors (Outdoors or
   Either). At least 18 are Low or Medium mess.
7. **Inclusive.** Any child, any family: no assumptions about a yard, siblings, two parents, money, holidays or
   religion. An outdoor sheet gives an indoor or balcony version where it can.
8. **Original.** No brand names, characters, shows or games owned by someone else ("building bricks", not a brand).
9. **House words rules** (docs/agents/STANDARDS.md, LESSON-PLANS.md rule 7): no em dashes, "Curio Class" never
   "Curio" alone, grade-level language in anything a child reads.
10. **Specific.** Real numbers, real examples and real tips ("fold the wing tips up a pencil's width"), never
    "decorate it however you like" as a whole step.

## Later, to put it on the site

Not part of this draft; for when Cory says go.

- **Site:** `/closet/break-box/` (shelf by grade), `/closet/break-box/<grade>/<id>/` (one sheet, prints on one or two
  Letter pages like Game Night). Gated with the closet flag until ready.
- **Data:** split each grade file into `data/closet/breaks/<id>.md`, one sheet each, with the info row moved to
  `key: value` header lines like `data/closet/games/`. `check_breaks.py` moves to that format and the build runs it.
- **Extras worth building:** a "pick for me" filter on the shelf (time, mess, alone or with others, indoors or out),
  a printable "Break week" pack (five sheets for a week, mixed kinds), and a blank "My own idea" sheet in the same
  layout.
- **Spanish:** written alongside when the sheets move to data (closet rule 6), then the native-speaker review.
- **Review:** Cory reads all K-2 sheets and any with heat, tools or going out; spot-checks one in four of the rest.
