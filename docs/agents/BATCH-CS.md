# Batch note: Computer Science, first five (2026-10-26)

Cory asked for five computer science tools, with "good quality in the first draft". In build order:

| Order | Id | Name | Grade | Format | Module | Voice |
|---|---|---|---|---|---|---|
| 1 | robot-dance | Robot Dance | K | showdown | Step-by-Step | lively-host |
| 2 | computer-builder | Computer Builder | 1 | builder | Parts of a Computer | bright-teacher |
| 3 | score-keeper | Score Keeper | 3 | lab | Variables in Programs | friendly-dad |
| 4 | code-tracer | Code Tracer | 4 | puzzle | Trace the Code | clear-teacher |
| 5 | game-remix | Game Remix | 5 | studio | Remix a Program | big-sister |

Cory named two of them by module ("Variables in Programs" is score-keeper, "Remix a Program" is game-remix). Each is
the first tool in its module, so it should be the one a teacher would open for that lesson.

## Rules for this batch (on top of your brief and STANDARDS.md)

- **First draft is the real draft.** Before a builder reports done, it runs its own checks the way VERIFY.md will: every
  size in STANDARDS.md, held clicks with the voice log, keyboard only, console clean. Fix what it finds, then report.
  Polish counts: motion that shows cause and effect (a step runs, the robot moves, the variable box changes), not
  just a text result.
- **One idea each, no overlap.** loop-garden (grade 2, live) already does repeat blocks with a robot gardener;
  bee-bot-garden (grade 1, concept) will do arrow paths on a grid. robot-dance is about order of steps and finding
  the wrong step (debugging) as a class, not grid paths or loops. code-tracer predicts values line by line;
  score-keeper watches variables change while a game runs; game-remix changes a working program. Keep them apart.
- **Code the kids see.** Grades 3-5 code is a small, readable language of our own (blocks or short text lines like
  `score = score + 1`), run by a tiny interpreter written in the tool. Never `eval` or `new Function` on anything a
  student typed or arranged. Every line that runs is highlighted as it runs, at a speed the student can follow, with
  step and pause controls.
- **K-1 reads nothing.** robot-dance and computer-builder work for children who can't read: icons and pictures on
  every control, a narrator voicing every fixed line (K-2 band rules), 60 px targets, teacher on a projector.
- **No network, no accounts.** game-remix "shares" through a short remix code the student can copy or a printed card;
  no uploads, no links that leave the page. Nothing a student makes is stored unless they press Save
  (localStorage, with a Clear button).
- **Art.** Robots and computer parts may be drawn in code (SVG or canvas) or made with Codex (`scripts/gptart.py`:
  base first, then siblings with `"ref"` + `"ref_mode": "style"`); scenes and props with Cloudflare FLUX.2
  (`scripts/cfart.py`). No people from a local model. Two tools in this batch may not ask for the same image.
- **Bands.** K-2 and 3-5 set their own `:root` colors (no band theme file for them; do not write one). Each tool its
  own accent, different from its neighbors' and from loop-garden's, WCAG AA ratios stated in the spec.
- **Facts and standards.** Name the CSTA K-12 Computer Science Standards (2017) codes the module lists, and check each
  claim on screen (what a variable is, what a CPU does, what RAM holds) against a named source in the spec
  (CSTA, Code.org CS Fundamentals glossary, a textbook). Computer parts for grade 1 are the everyday ones (screen,
  keyboard, mouse, speakers, microphone, camera, the computer box or tablet); "the brain of the computer" is fine
  for the processor at grade 1 if the spec says so.
