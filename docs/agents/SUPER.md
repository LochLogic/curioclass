# Super tools (Cory, 2026-10-29)

A few deep, shiny tools that people open for fun and learn from without noticing. Beat Lab is the model: it is an
instrument first, the teaching is how the instrument works, and the depth comes from combining things, not from more
levels. Coverage is already good; these are extra. Each takes over the idea card it overlaps (same module).

| Tool | Module (anchor) | Grades | Took over |
|---|---|---|---|
| pocket-universe | science-6-gravity-and-the-solar-system | 6-12 | Planet Builder |
| living-pond | science-5-food-webs-and-matter-cycles | 3-8 | Food Web Wobble |
| molecule-forge | science-7-atoms-and-molecules | 6-10 | Molecule Builder |
| span-and-spire | science-8-engineering-design | 6-12 | Span the Gap |
| cipher-vault | computer-science-6-8-cyber-attacks-and-defense | 5-12 | (new, a second card) |

## The three tests (every super spec must pass all three)

1. **A toy with no instructions.** In the first 10 seconds something delightful happens from one tap or drag. No
   reading wall, no tutorial gate. A kid who never reads a word still has fun.
2. **Something to show someone.** The student makes a thing they would turn the screen around for (a stable
   two-sun system, a pond that survived ten winters, a bridge that held the big truck, a molecule nobody else found,
   a message their partner cannot crack). It can be saved on this device and replayed.
3. **The concept is the mechanic.** The lesson is how the toy works, never a quiz on top. Remove the science and the
   toy stops working.

## What a super spec adds to docs/agents/SPEC.md

Follow SPEC.md and STANDARDS.md in full (all five rules from Cory's reviews), plus:

- **Up to about 450 lines.** Depth needs room; no padding.
- **First minute.** A section "First minute" right after One idea: second by second, what the student sees and does
  and what delights them, with no instructions read.
- **Goal ladder.** A section "Goals" after Screens and modes: 12 to 25 optional challenges from easy to hard, each with
  a one-line target, the check that decides it (exact numbers), and what it secretly teaches. A collection or
  sticker book shows found ones. Goals never block free play.
- **Depth from combining.** Name the 3 to 6 parts that combine and at least 5 surprising combinations a student can
  discover (emergent, not scripted). Run each in Python on the real model and show they happen.
- **Honest model.** The simulation runs on the real rule (Newtonian gravity, Lotka-Volterra with seasons, valence
  and bond rules, truss statics with buckling, real cipher math), simplified only where the spec says how and why.
  Sources list the model and the checks run on it, including the worst cases (a crash, a collapse, an extinction,
  an unbreakable message).
- **Shine.** Motion and sound are part of the fun: say what glows, trails, wobbles, buckles or clicks, and the sound
  of each event (Web Audio in code). Keep it smooth at 60 frames a second on a school Chromebook: name the budget
  (bodies, members, creatures, atoms) and what happens at the limit.
- **Art budget.** Up to about 40 painted images (local FLUX). No people unless the person is the point; these five
  tools should need none.
- **Ten-minute check.** In Done when, add: "a fresh player with no instructions is still choosing to play after 10
  minutes, and can name one thing they figured out."
- **Teacher layer, light.** One short Teacher note: three ways to use it in a period (free play, a goal set, a
  challenge for the room) and the standards it reaches. No worksheets.

## Per-tool notes

- **pocket-universe.** Fling bodies by drag (direction and speed from the drag). Time scrubber (rewind, pause, speed
  up), glowing trails, collisions merge bodies. Real solar system to scale as a load. Goals such as a stable moon, a
  figure-eight, a slingshot, an escape, a two-sun system. Orbit Lab (grade 9 spec) and Moon Phase Model are neighbors:
  say how this differs.
- **living-pond.** Painted creatures as cutouts that swim, hunt and die back; seasons change the light and ice. Keep
  Food Web Wobble's standard content: matter loops through decomposers, sunlight energy flows one way. Population
  graph under the pond. A slow drift of one trait (minnow color against a heron) shows selection over generations.
  Predator Prey Island (real Isle Royale data) is a neighbor: this one is the toy, that one is the data.
- **molecule-forge.** Atoms snap only where real bonding allows; a discovery book fills as students find molecules
  (water up to caffeine), each with one real fact. Shape follows the real geometry. Repeat a pattern to grow salt,
  diamond and copper. Bond Battle and Equation Balancer are neighbors.
- **span-and-spire.** Bridge mode: build a truss over a creek on a budget; trucks of increasing weight roll across;
  every member colors by force (tension and compression shown differently) and the weakest buckles in slow motion.
  Tower mode: build up against wind and a shake table. Keep Span the Gap's engineering design steps (criteria from the
  people who use it, compare designs, combine the best parts). Our own design: it must not copy any bridge game.
- **cipher-vault.** A chain of locked rooms, each sealed by a real historical cipher (Caesar, pigpen, Vigenere, a
  simple Enigma); tools, not answers (frequency counter, draggable cipher wheel). Make your own message to stump a
  partner on this device. Capture the Flag and Phishing Spotter are neighbors: this one is about how ciphers work
  and break, not attacks.

## Build note (later)

Super tools are built one at a time, never in a wave, with a third Refine round allowed and the ten-minute check
played by a fresh agent. Expect each to cost about three normal tools.
