# Codex build brief, a Curiosity (Curio Class)

You are building ONE **Curiosity** for Curio Class (curioclass.org). This brief replaces `docs/agents/CODEX-BUILD.md`
for this tool. A Curiosity is not a lesson tool, and the most likely way to fail is to build one anyway: a header with
pills, a hook, numbered steps, a check, a score, a finish screen. None of that belongs here.

Read first, in this order:

1. `docs/VISION.md`, the section "Curiosities: the second shape": the five qualities and the short test.
2. `docs/CURIOSITIES.md`: this tool's concept entry and "The look". They are owner decisions (Cory, 2026-11-04).
3. `tools/<id>/spec.md`, every line. It is written in the Curiosity shape (below). Where an older line in it still
   talks about goals, levels, stickers, a score or a finish, the concept entry and this brief win.
4. `docs/agents/decisions/BASELINE.md` and `docs/agents/STANDARDS.md` for the rules every tool keeps (sizes,
   contrast, keyboard, reduced motion, voice, one offline file). They still bind. Their lesson flow does not.

## What a Curiosity is

A real instrument a scientist, engineer, musician or writer would use, made approachable, with the standard learned as
a side effect of using it. The student drives. There is no correct path, no score, no level, no finish line and no
quiz. The tool answers by showing.

The short test, which your build must pass:

- Would a kid open it when no teacher assigned it?
- Would an adult play with it for fun?
- Is the real thing (sound, light, data, motion) the interface itself?
- Does it work with no score and no finish line?

## The models

Open and use these before you design anything:

- `tools/beat-lab/` and `tools/elements-inspector/` (an older tool: its whole source is `elements-inspector.html`): the owner's two favorite tools and the reason Curiosities exist.
  Beat Lab is a real studio; Elements Inspector is a real atom with real spectra. Match their confidence and density.
- `tools/span-and-spire/` (No. 01) and `tools/pocket-universe/` (No. 02): the first two Curiosities, pivoted from
  lesson-shaped tools. Take the **family marks** from them: the engraved maker's plate and the `Manual` drawer in the
  lower-left corner, Motion, Sound and Read on the tool's own power panel. Do not take their palette, layout or scene.

Do not open the other tools in `tools/` and do not run `scripts/neighbors.py`. Do not start from `kit/starter/src.html`:
its frame is the lesson frame.

## The look (owner's decision)

- **It looks like the real instrument it is.** Not a photo of one, but its visual grammar: an oscilloscope's
  phosphor trace, a planetarium's dark dome, a lab bench's matte surface, a drafting table's paper and pencil.
- **The object fills the screen.** No page around it, no card, no header bar, no right-hand pill panel.
- **Real controls:** knobs, faders, toggle switches, lit pads, dials, needle gauges, sliders with detents. They work
  with the keyboard and announce their value.
- **Readouts, not prose.** Live numbers with units in a monospace face. Between two actions the student reads almost
  nothing; explanations live in the Manual.
- **The Manual** is a drawer in the lower-left corner: how to use it, what the readouts mean, the honesty notes and
  sources, and "Things people have found" (short entries a student reads after finding them, never targets).
- **The maker's plate**, engraved, beside the Manual: `Curio Class Curiosities · No. NN · <Name>`. Your number is in the
  spec. Use the middle dot character, never an em dash.
- **The palette comes from the real material**, not the site's lesson palette.

## What to build, and what not to

Build: the real thing, working on real rules and real data, at 60 frames a second on a school Chromebook. A first two
minutes that gives a reaction with nothing read. Depth a month of use still finds. Presets or a setups book where the
spec lists them. Save and load where the spec lists them.

Do not build, even if a habit says to: a welcome screen to dismiss, a hook, numbered steps or rounds, a progress bar,
points, stars, stickers, badges, a goal list, a timer, a quiz, a reflection gate, a "you did it" screen, confetti, a
teacher-led stepper, or a kit header with mode pills. If the spec asks for one of these, it is an old line: leave it
out and say so in the report.

A first-run hint is allowed: one quiet line on the instrument itself ("Say ahhh", "Drag to spin"), gone after the first
action. Voice speaks that hint once and then only when Read is pressed.

## Kit

You may use `kit/curio.js` for the voice (`Curio.voice`), tones, saving to the device and the Motion and Sound
settings, because BASELINE needs them to behave the same everywhere. Do not use the kit's header, layout, cards or
buttons from `kit/curio.css`: draw your own controls in the instrument's style.

## Machinery (from the regular brief)

From `docs/agents/CODEX-BUILD.md`, read and follow only these sections: **Ground rules**, **Images**, **Do not hang**,
**Files to make** and **Check your work**. They are about files, ports, art and time limits, not about how a tool is
shaped. Skip "Make it look good and play well", "Super tools", "Read, in this order" and its report template: this brief
replaces them. From `docs/agents/BUILD.md` take only the file formats (`tool.draft.json`, `voice/lines.json`,
`audit-states.json`, `notes.md` headings); its wave lessons about lesson flow do not apply. In `tool.draft.json` add
`"curiosity": true` and `"plate": NN`.

Images: a Curiosity draws its working surface in code (SVG, canvas or WebGL) because the real material has to be
exact. Use painted images only where a real object or place adds something (a microscope's body, a desk, a sky
horizon). Never paint data.

Sources: every dataset and fact gets a named source and licence in the Manual and in `tool.draft.json` `sources`.
Bundle the data into the one file; the tool makes no network requests. If a dataset in the spec is too large, sample it
honestly and say so in the Manual ("every quake of magnitude 6 or more since 1970").

## Gathering data (owner's decision, 2026-11-05)

A Curiosity build may go online to gather its real material. This overrides "Do not download anything" in the regular
brief's Ground rules, for Curiosities only. The finished tool still makes no network requests: everything it uses is
bundled into the one file.

- Gather only what the spec names, from the sources it names (or its listed fallback). Read the licence at the
  source before you use anything: public domain, CC0 or CC BY are fine; anything else, use the spec's fallback or
  leave that piece out and say so.
- Where a spec says "staged locally", "prep pass", "builds have no internet" or "fetch", do that step yourself at the
  start of the session.
- Save raw downloads in `_scratch/<id>/data/`, and write the script that packs them in Scratch too, so the next person
  can re-run it. Only the packed result goes into `tools/<id>/`.
- Record each source in the report's "The real material": URL, licence as stated at the source, date fetched, and how
  it was sampled.
- Check facts and quoted texts against two independent sources. Drop any piece you cannot confirm rather than guess.
- Give gathering at most 45 minutes of the session in total, and put a time limit on every download. If a source is
  down or a step needs software you cannot install (for example pygplates), use the fallback or leave that feature out
  and list it under Left open. The instrument itself matters more than any one dataset.
- Never download or run executables, and never install system software. A `pip install` of a pure-Python package
  into a virtual environment in Scratch is fine.

## Check your work

As the regular brief's "Check your work", with these changes:

- Instead of "Break it" for scores (there are none), try to **break the instrument**: extreme values, every control at
  both ends, rapid input, an empty or silent input, resize while running. Nothing may freeze, go blank or lie.
- Instead of the Feel check, do the **short test**: play it for ten minutes as a student of the anchor grade and as an
  adult, then answer the four questions honestly in the report, with one frame of yours beside one of Beat Lab or
  Elements Inspector.
- **Lesson creep check:** search your `src.html` and voice lines for score, points, level, goal, sticker, badge,
  correct, wrong, try again, complete and well done. Each hit is either removed or explained in the report.

## Report: `tools/<id>/codex-report.md`

```
# Codex report: <id> (Curiosity No. NN)
## Built
## The real material   (each dataset and fact the student sees, with source and licence)
## Break the instrument
## Voice walk
## Short test           (the four questions, honestly, with the frame comparison)
## Lesson creep check
## Done when            (each spec item: PASS or FAIL, with evidence)
## Audit leads
## Frames looked at
## Art made
## Engine changes wanted
## Left open
```

When the report is written, say "Build done" and stop.

## For the reviewer

A cold review of a Curiosity follows `docs/agents/CODEX-REVIEW.md` for its process, fixes and report file, but judges
the tool against this brief, not the lesson norms. The reviewer never adds a goal, score, level, quiz, finish screen or
kit header, and removes any goal ladder, grade or forced finish that slipped in; a light game touch that adds fun
and keeps play open may stay (BASELINE rule 19, 2026-11-06). Its own question is the short test: if the tool fails one of the four
questions, that is a blocker, and the fix is to make the real material more central, not to add a game.
