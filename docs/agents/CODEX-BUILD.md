# Codex build brief, any tool (Curio Class)

You are building ONE tool for Curio Class (curioclass.org), a free, public K-12 site of interactive classroom tools.
Each tool is one self-contained HTML file that a teacher projects or a student opens on a school laptop. Three blind
reviewers will check your work later, so build it as if it ships to real students tomorrow.

A tool that passes every check and is dull has failed. The first two Codex builds had a sound frame, color and layout,
but the owner found the graphics very simple and the play underwhelming. Correct is the floor here. The goal is a tool a
student would open again on their own.

The tool id is in the prompt that sent you here, and `<id>` below means that id. Every Codex chat shares one checkout,
`S:\CurioClass-codex`, and that is the repo root. Run every command from there. Scratch means `_scratch/<id>` in it.
If your working folder is anything else, say so and stop: nothing you make there will reach the tool.

**This run is Build only.** When the report is written, stop and wait. Do not start a polish round, and do not commit.
A cold Codex review comes next (`docs/agents/CODEX-REVIEW.md`), in another chat. The tool holds on this branch until then.

## Ground rules

- Write only inside `tools/<id>/` and Scratch. Other chats are working in this same checkout at the same time, so never
  touch `kit/`, `docs/`, `scripts/` or another tool, and no git commits, branch changes, stash, reset or clean.
- Keep the tool folder tidy. It holds the files listed under Files to make, plus a data file only if `src.html` loads it.
  Plans, evidence, audit notes, previews, contact sheets and anything else you made for yourself go in Scratch.
- If a kit engine needs a change, do not make it. Work around it in the tool and list the change in `handoff.md` under
  `## Engine changes wanted`: the file, the function, the exact change and why.
- If the spec is wrong or impossible, build everything else and say so in `handoff.md` and the report. Do not improvise.
- You make the graphics yourself, during the build. See Images, below. Do not download anything or record audio.
- Write readable code: normal line breaks and one statement per line, about 160 characters a line at most. Never
  compress `src.html`. The next person has to change it.
- Write "Curio Class", never "Curio" alone. Never use an em dash anywhere: code comments, UI text, notes, lines, reports.
- The tool makes no network requests. You need no internet.
- Screenshots, Chrome profiles, shots files, audit output and temporary scripts go in Scratch or %TEMP%, never the repo.
  Your sandbox cannot delete files afterwards, so anything left in the tool folder stays.
- Use only the ports your prompt names (default: Chrome debugging 9990 to 9997, host server 8795), and use those numbers
  wherever the commands below show the defaults. Other builds may be running. Every Chrome uses `--mute-audio` (drive.py does).
  drive.py and audit_tool.py already handle a missing `websockets` and a Chrome that will not start; do not work around them.

## Super tools

If your prompt calls this a super tool, also read `docs/agents/SUPER.md` right after the spec. Its three tests, First
minute, Goals, shine and ten-minute check are the point of the tool. The simulation runs on the real rule and stays
smooth at 60 frames a second within the spec's budget. Expect a longer build, and keep to the same time limits per
command. In the Feel check, say honestly whether you would still be playing after 10 minutes, and why.

## Make it look good and play well

This comes first. Spend your time here before the size and audit checks, not after them.

The spec sets what the tool teaches, its modes, content and facts: add no new features or topics. It does not set the
finish. Rich drawing, motion, sound and feedback inside what the spec describes are the job, not extras, and "drawn in
code" or "Art: none" never means plain.

**Graphics**

- Draw a place, not a diagram. Every scene has a background, a middle and a foreground, with light from one direction.
  Use SVG gradients, soft shadows, highlights and texture so things have weight.
- Each object gets at least three levels: its shape, its shading, and small true details (the screws on a router, the
  chips on a die, the grain on a desk). A plain rounded rectangle with a label is not finished art.
- Small life: something quietly moves while the tool waits, such as a blinking light, a drifting cloud or a ticking
  needle. It stops with Motion off.
- Use every painted image the spec lists, large enough to enjoy. Do not shrink art into a thumbnail. Art and layout are
  built together, so fit the scene to the picture you actually drew.
- Panels and buttons belong to the scene's world (a clipboard, a control desk, a field notebook), not a default web form.

**Gameplay**

- The first tap pays off. Within about 10 seconds, with nothing read, the student has done something and seen a result.
- Every action answers at once: within about 100 ms something moves, something sounds (`Curio.tone`, or Web Audio for
  richer sounds, silent when Sound is off) and the state visibly changes. A number changing alone is not an answer.
- Show the outcome, do not tell it. Let the bridge sag, the ping travel and stop, the dice tumble and land. Play it out
  on screen, then put the words after it.
- Real choices. At each step the student weighs something and can be wrong in an interesting way. A wrong choice shows
  what it caused, so failing teaches something and is worth watching.
- It builds. Later rounds change something: a new twist, a harder case, a combination. The same step repeated is not depth.
- A payoff. The session ends in something earned and specific to what this student did, worth showing someone: their
  record, their design, a recap of their own choices.
- Less reading. Between two actions a student reads about two short sentences at most. Move the rest into the scene,
  the hint or the teacher notes.

The grade band rules still win (docs/agents/STANDARDS.md): 9-12 tools work like the real thing, so their reward is
respect and a sharp result, not confetti. K-2 stays teacher led. Hard history has no points, timers or win states.

**The bar.** Before you start, bundle and open `tools/snowy-mail-route/` (motion and feedback) and `tools/beat-lab/`
(the owner's model of a tool people want to use). Match their finish, not their look.

**Feel check.** Near the end, play the whole tool once as a student of that grade. Then, in the report's Feel check
section, write down the best moment, the two flattest moments and what you changed to fix them, and put one frame of
your tool beside one from a bar tool. If yours looks plainer, keep going.

## Images

You have an image generation tool. Use it as you build, so the art is real from the first playable version. Try hard:
the owner would rather dial back rich art than add it later. Never leave a labeled placeholder for an image you can make.

1. Write `art/prompts.json` first, from the spec's Art section, in the format of `tools/calm-corner/art/prompts.json`. If
   it already exists it may be older than the spec: keep what it has and add what is missing. `docs/ART.md` has the style
   rules and the options. Set a `house_style` that fits the grade. Keep one style across the whole set.
2. Make each missing image with the full prompt: house style, then the asset's prompt. Pictures have no text, letters,
   numbers or logos. Anything that must cut out from its background is drawn on flat pure green (#00FF00), or magenta for
   green subjects, with `"cutout": true` (and `"key": "magenta"`) in its asset.
3. Copy the image into `tools/<id>/art/raw/<name>.png`. New images land under `~/.codex/generated_images/`. Add
   `"drawn_by": "codex"` to the asset.
4. Run `python scripts/art.py <id> --rekey <name>`. It cuts out, sizes and writes `art/<name>.webp`, free, and it is the
   only art.py form you may run: without `--rekey` it calls a paid service.
5. Look at the finished image at its final size. Redraw it, up to twice, if it is wrong, ugly or untrue to what the tool
   teaches. A real species, tool or place has to look like the real one.

Beyond the spec's list: "Art: none" means no art was planned, not that none is allowed. Where a painted backdrop or
object would make the scene richer, add it to prompts.json and make it. Where exact drawing matters (a graph, a moving
simulation, a precise diagram), draw in SVG or canvas, which stays the better picture. Images already in `art/` stay;
match new ones to them.

**People.** Do not draw people, faces or body parts, even if the spec asks. Those go to another painter with the owner
checking each one. Add the asset with `"people": true`, use its `art:<name>` token, make the scene work with a tasteful
faceless silhouette drawn in code until then, and list it in the report under Art still to paint.

**Size.** The bundle stays under 2 MB, and the art drives that: about 30 to 80 KB for a character or object and 100 to
150 KB for a background. Set `width` in the asset to the largest size it shows at. If you are over, lower `quality` to
about 72, then the width of the backgrounds, before you drop any image.

If image generation fails or hits a usage limit, finish the tool with art drawn in code, list the missing images under
Art still to paint, and carry on.

Credit: when you used any generated image, add this to `sources` in `tool.draft.json`:
`Illustrations generated with OpenAI gpt-image, edited for Curio Class`.

## Do not hang

Past builds lost hours to one stuck command and to re-running every check at the end. So:

The limits below are for commands and checks. They are never a reason to cut the graphics or the play.

1. **Start the report early.** Create `tools/<id>/codex-report.md` as soon as the first version bundles, and fill each
   section as its check finishes. Keep it under 200 lines.
2. **Put a time limit on every command** you run: 2 minutes for a bundle, 5 for a drive.py batch, 40 for the audit.
   A command that hits its limit is stopped and retried once, smaller. If it stops again, write it under Left open and
   move on. Never wait on a command with no limit.
3. **Nothing long-lived in the foreground.** The `--host` server starts in the background and stops right after its
   shots. Keep drive.py batches to about 12 shots.
4. **Shoot once, late.** Work in small checks on the size you are fixing. Do the full run of every size only once, near
   the end. After that, re-shoot only what a fix touched. Do not re-run the whole set after a small fix.
5. **Run the audit once, last.** Answer its leads in the report. If it has not finished in 40 minutes, stop it, say so
   in the report and finish. The reviewer can run it.
6. **Close every Chrome and server you start**, each time, before the next step.
7. **If you are stuck on one problem for more than about 20 minutes,** write it under Left open and go on to the next.

## Read, in this order

1. `docs/agents/STANDARDS.md`. Where anything differs, it wins.
2. `tools/<id>/spec.md`, every line, before you write anything. It is the source of truth. Build what it says, nothing more.
3. `docs/agents/BUILD.md`, all of it, including its wave lessons. Those are the repeat review findings, so each one is a
   check you must do. It lists the files to make.
4. `docs/agents/decisions/BASELINE.md`, `docs/TOOL-CONTRACT.md`, `docs/KIT.md` (above all "Voice: Curio.voice"), `docs/POLISH.md`
   and `docs/ART.md`.
5. `kit/starter/src.html`: start from a copy. Skim `kit/curio.js` and `kit/curio.css`, and use them instead of re-implementing anything.
6. If the spec names a family: `docs/families/<family>.md` and its engine file, in full. Use the engine, do not rewrite it.
7. `python scripts/neighbors.py <id>`: open one built neighbor (`src.html`, `handoff.md`, `refine.md`) to see the level of
   care reviewers expect. Do not copy its look, scene, voice or palette.

Before building, recompute every number in the spec's Sources in a small script in Scratch. If your numbers differ,
trust the computation, say what differs in the report, and leave the spec alone.

## Files to make in `tools/<id>/`

As BUILD.md lists: `src.html`, `tool.draft.json` (`"stage": "built"`), `notes.md`, `voice/lines.json`,
`audit-states.json`, `handoff.md`, `art/prompts.json` and `art/<name>.webp`, plus `codex-report.md`.
`notes.md` opens with `## What it teaches`, `## Key skills` and `## Support at home`, as BUILD.md says. The bundle
`<id>.html` is generated and git-ignored. Delete `host.html` when you finish, or say you could not.

## Check your work (from the repo root)

1. `$env:CURIO_DRAFT=1; python scripts/bundle_tool.py <id>`: bundles cleanly, under 2 MB.
2. `python scripts/drive.py <id> <Scratch>/shots.json <Scratch>/frames --port 9990 --profile <Scratch>/chrome-prof`. The header
   of `scripts/drive.py` gives the shots format. Use held clicks (`"hold": 0.12`) for anything with voice and real drags
   for dragging. There must be no console errors, warnings or exceptions.
3. 375 wide: `python scripts/drive.py <id> --host 8795` in the background, then shots at `http://127.0.0.1:8795/host.html?w=375&h=812`.
4. Cover every STANDARDS size, every mode, each extreme in POLISH.md, Motion off, a grayscale frame and a keyboard-only run.
5. Open and look at every PNG you shot. Fix overlaps, clipping, unreadable text and any "Done when" that fails.
6. Voice: at a 2 s tap pace with held clicks, read `__tool.vlog` and check the STANDARDS voice rules.
7. Last: `python scripts/audit_tool.py <id> <Scratch>/audit --port 9991 --profile <Scratch>/chrome-prof-audit`.

## Report: `tools/<id>/codex-report.md`

```
# Codex report: <id>
## Built
## Numbers check
## Feel check         (best moment, two flattest moments, what you changed, frames compared with a bar tool)
## Done when          (each spec item: PASS or FAIL, with evidence)
## Wave lessons       (each BUILD.md lesson: PASS or FAIL, and how you checked)
## Audit leads        (each lead: fixed, or why not; or "audit not finished")
## Frames looked at
## Art made           (image count, total art KB, bundle KB, what was redrawn)
## Art still to paint (people and anything image generation could not make)
## Engine changes wanted
## Left open
```

Be honest: a FAIL you report is worth more than a PASS you did not check. When the report is written, say "Build done"
and stop.
