# Lesson plans

Agreed with Cory 2026-10-25. Every built tool gets a one-page lesson plan for a whole class period: a hook that
opens the standard, questions worth asking, the tool at the point in the lesson where it does the most good, and a
quick check at the end. It sits on the tool page as a **Lesson plan** button between Download and Embed, at
`/tools/<id>/plan/`, and prints on its own.

## Why

A tool alone is a maybe-someday for a busy teacher. A tool with a plan is tomorrow's lesson, a ready sub plan, and
an easy answer when someone asks what standard the class was working on.

## The rules

1. **Specific or nothing.** A generic plan is worse than none: teachers spot boilerplate at once. Every plan names
   the tool's own buttons, items and moments ("when the egg goes in the freezer, ask..."). The checker requires at
   least four bold names that really appear in the tool.
2. **The tool goes where it teaches best.** That depends on the tool, so every plan picks an arc (below). Explore
   tools come early; practice tools come after a short lesson; model tools lead into students making something.
3. **A skeleton, not a script.** Short steps and real questions with the answers we expect, so a teacher can adapt
   it and a substitute who has never seen the tool can still run it.
4. **One period.** 30 to 50 minutes (K-2: 40 at most, no part longer than 15). Every timed part says its minutes,
   and they add up to the total.
5. **One page, roughly.** At most 850 words. If it doesn't fit, it's doing too much.
6. **Teacher notes stay the tool's how-to** (what each button does, good to know). The plan is the period. The plan
   links to the notes instead of repeating them.
7. The usual words rules: no em dashes, "Curio Class" never "Curio" alone, grade-level language in anything said to
   students, and the guardrails in docs/agents/STANDARDS.md (hard history, health) apply to plans too.

## Arcs

| Arc | Use it for | Timed parts, in order |
|---|---|---|
| `explore-first` | explore and sort tools, models, simulations | Hook, Explore (the tool), Make sense, Apply, Exit check |
| `teach-then-practice` | practice, arcade and drill tools | Hook, Teach, Practice (the tool), Apply, Exit check |
| `model-then-make` | builders where students then make their own | Hook, Model (the tool), Make, Share, Exit check |

The checker holds each plan to its arc's parts and order. If a tool truly needs another shape, add an arc here
first, with Cory's OK.

**K-2:** the class is on the carpet and the teacher drives the tool on the big screen (all K-2 tools are teacher
led). Keep parts short, use turn-and-talk and hands-up votes, and make the exit check oral or physical (thumbs,
point, act it out). No worksheets needed unless the plan says what to print.

## The file: `tools/<id>/plan.md`

A header of `key: value` lines, a line with `---`, then the sections.

```
arc: explore-first
minutes: 40
focus: 2-PS1-4
goal: I can tell which changes from heating and cooling can go back, and show my evidence.
materials: The tool on the big screen. Optional: an ice cube on a plate, started at the beginning of class.
grouping: Whole class on the carpet, with turn-and-talk partners.
---
## Before class
## Hook (5 min)
## Explore (15 min)
## Make sense (8 min)
## Apply (7 min)
## Exit check (5 min)
## Support and stretch
## Short on time
```

- `focus` is one or more of the module's standard codes (semicolon separated, as in modules.csv); the page shows their text.
- `goal` is an "I can" sentence a student could say.
- **Before class:** setup in two or three bullets.
- **Timed parts:** numbered steps. Questions in quotes, with expected answers in parentheses.
- **Support and stretch:** two to four bullets for students who need more help or more challenge.
- **Short on time:** a 15 to 20 minute version in two or three bullets.

## Sub Day: `tools/<id>/exit.md`

Every tool with a plan also gets a Sub Day packet at `/tools/<id>/sub/` (docs/SUPPLY-CLOSET-PLAN.md, Phase B): five
printed pages, each starting a new sheet. A cover page the teacher fills in by hand (the tool's link and a QR code,
who drives, how long, and blanks for the day), the plan, the teacher notes, the exit page and a backup sheet for when
the tool will not load. The packet is built from the plan, notes.md, tool.json, the module's Word Wall words and one
small file:

```
kind: ticket
---
1. Show me: Write 90 as a product of primes. | (2 x 3 x 3 x 5)
2. Explain: Find the GCF and LCM of 12 and 18. Which one is bigger, and why? | (GCF 6, LCM 36; ...)
3. Rate it: I can use prime factors to find the GCF and LCM.
```

- `kind` is `checklist` for K-2 and `ticket` for everything else.
- **Tickets:** one to three items labeled `Show me`, `Explain` or `Rate it`, ending with a `Rate it` self-rating
  ("I can ..."). Every other item has the teacher key after a `|`, in parentheses. 45 words at most per item. They
  print four to a page with cut lines, and the key prints upside down at the bottom.
- **Checklists:** one to three short things to watch for (10 words at most each). They print as column heads on a
  class list with got it, almost and not yet boxes.
- The items ask the same thing as the plan's Exit check (the checker wants a shared key word).
- The backup sheet needs nothing extra: K-2 gets a draw-it box, the exit items to read aloud and faces to color;
  3-8 a frame sheet (what I know, two Word Wall words, the exit items); 9-12 the goal to explain, the words and the
  exit items.


Plans are written after a tool passes verify, by a fresh plan agent (`docs/agents/PLAN.md`), because a plan has to
point at the finished tool's real screens. The same agent writes exit.md. `python scripts/check_plans.py` checks
every plan and exit file (also run by the site build). Cory reviews K-2 plans and sensitive ones with the tool; others are spot-checked like the tools. The build
board shows which tools have one.
