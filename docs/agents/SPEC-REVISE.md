# Spec revision brief (2026-10-29)

You revise existing, unbuilt Curio Class specs so they meet the current `docs/agents/SPEC.md`. Most were written
2026-10-27, before Cory's first two review rounds taught us five things (SPEC.md Rules: Art, Voice, Check your own
numbers, Name the focus, Fit the kit and the scope). You do not write code and you do not start over.

## Read first

1. `docs/agents/STANDARDS.md` (it wins over this brief), then `docs/agents/SPEC.md` in full.
2. Your batch line in `docs/agents/spec-revise/BATCHES.md`: the specs you own, all one subject, in grade order.
3. For each spec: the spec itself, then `python scripts/neighbors.py <tool-id>` for its neighbors and family.

## What to change, in this order

1. **Art.** The biggest one. For every scene, place, character, animal, creature, object or prop the student looks at,
   replace the code drawing with painted images in the template form (name: positive prompt; aspect; cutout; people;
   how it is used). Keep code for diagrams, charts, graphs, data maps, grids, controls, labels and shapes that must
   bend. Plan cutouts for anything that moves or changes pose. Mark people `people: true`. Text on signs stays in
   code over a blank painted surface. "none: drawn in code" stays only with a one-line reason the tool is all
   diagram or chart. Update "Look" and "Screens and modes" where they described the old drawings.
2. **Voice.** Tag every fixed line `how` or `event`, with when it plays and when it goes stale. Rewrite any waiting
   line that does not name the action and the control, or that names a control disabled at that moment. Keep the
   voice id unless it clashes with a neighbor or another spec in your batch.
3. **Focus.** Give each mode its focus. Move the layout if the focus is not the biggest, central thing. Anything that
   plays on its own keeps controls live and responds at once.
4. **Numbers.** Run every rule, score table, tolerance and worked answer in Python on real values, including the
   worst cases. Fix what fails. Add the checks you ran and their results to Sources.
5. **Kit and scope.** Remove features that move work between devices by hand (codes, print cards). Sound starts on.
   Shorten auto-plays over about 30 s or give the reason.
6. **Done when.** Add a check for the focus and one for a tap while anything plays, if missing.

## What not to change

- The One idea, the Not like list, the standards, grade and the content facts. If a fix seems to need one of these
  changed, leave it and raise it as an open question.
- Sensitive collections (hard history, Spanish, growing-up and body questions): change only Art, Voice tags and
  Done when, keep every content line, and mark any new image with people for Cory's review.
- Do not touch any other file. Write only `tools/<id>/spec.md` for the specs in your batch.

## Batch check (after all your specs)

Read your revised specs side by side: no two ask for the same image, scene or palette; no two share a voice and
accent; no two have the same mechanic. Fix the spec files directly.

## Report (short)

One line per spec: how many images it now asks for (and how many with people), what else changed, and any open
question only Cory can decide. Then the batch check result. Plain words, no em dashes, "Curio Class" never alone.
Do not commit.
