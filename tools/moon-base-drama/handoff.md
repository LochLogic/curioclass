# Moon Base Drama build handoff

## Structure
`src.html` starts from the kit starter. Its permanent DOM contains the painted stage, six crew badges,
Mission Control radio, Ada's separate card, three meters, eight-node map, two choices and native rewind dialog.
Responsive CSS lays out actual pixels rather than scaling the whole board. Compact landscape keeps the
teacher's card beside the choices; phone controls use two rows. Art tokens appear once in the ART table.

JOBS, BEATS and L hold content. Ada's lines live only in BEATS and the card renderer. They never enter L,
`allLines()` or `voice/lines.json`. The voice manifest requests firm-captain / Alnilam. No speech was recorded,
as required for this Build; the kit currently uses available browser speech. The requested bank timbre awaits recordings.

`state.choices` contains active branch choices. `meterValues()` folds the three changes from the initial
1, 1, 1, so tapping again never stacks resources. Back or Rewind invalidates choices at and after its target;
`oldChoices` preserves their faded map icons. New mission resets story state and retains assigned jobs.
Mode changes retain the story. No story state is stored.

Each operative tap hushes narration on pointerdown, then acts on click. A revision guards queued event lines.
The tool uses `Curio.voice` with mode plus beat scope, `V.heard` for how-to lines, and the kit audio context
for 200 ms filtered radio noise. The radio caption follows active narration; Read never speaks Ada's card.
The glow follows browser speech playback, appropriate to the current unrecorded build.

## Art
Fourteen generated paintings are in `art/*.webp`, with originals in `art/raw/` and full prompts in
`art/prompts.json`. The built-in image tool made them during this build. All were inspected after the
required free `art.py --rekey <name>` processing. The six job props, rover, ice and five settings match the
spec; an additional painted greenhouse planter gives the code-controlled droop a painted leaf layer.
SVG clips split its leaves from its tray. Meter transitions, rover arrival, ice floating, charging and
warmth effects stop with Motion off. The idle beacon stops too. Empty suits are equipment, with no people.

## Spec decisions and ambiguities
- No explicit open questions appear in the spec.
- The explicit user instruction to stop when codex-report.md is written takes precedence over the build
  brief's early-report advice. The report is written last; evidence accumulated in Scratch meanwhile.
- The user requested the image tool, which takes precedence over the spec's local FLUX pipeline choice.
- Read on Mission and Radio again replay the current radio message, including a selected choice's result.
  Read on Crew speaks the current action hint. Neither speaks Ada's script.
- A direct Mission mode tap can enter the story without a job. Start mission itself requires a checked job,
  as specified. Back at beat 1 returns to Crew; Next at beat 8 becomes New mission, keeping navigation usable.
- A newly picked branch leaves later old icons faded until those beats are reached again. The new current
  choice replaces its old icon immediately, and active resources include only the new branch.
- The story map is a compact, noninteractive strip. Rewind opens the large three-choice map; unavailable
  future choices are disabled. Before any choice is visited it explains how to return instead of naming a disabled choice.
- The shared kit stores only its Motion preference. The spec's literal "nothing is saved" cannot be fully
  satisfied without a kit change. Notes disclose this; no classroom or story information is saved.
- The Sources temperature conversion is wrong: minus 130 Celsius is minus 202 Fahrenheit, not minus 208.
  The radio has no exact temperature, so no script correction was needed. The spec itself is unchanged.
- "Colder than any freezer on Earth" is an overbroad supplied line if laboratory cryogenic equipment is
  included. The exact supplied dialogue is preserved; teacher notes explain the home-freezer comparison.
- This is a teacher-led role play, not a scored quiz. The supplied choice order and truthful teaching
  feedback remain. The meters show story resources, not physical engineering quantities.

## Engine changes wanted
- `kit/curio.js`, `init` Motion handler: add an opt-out for persisted Motion preferences, so tools requesting
  no storage can keep that setting in memory. No shared files were changed.
- `kit/curio.js`, `voice` / `speakOne`: expose actual playback start/end callbacks for both recorded clips and
  browser speech. This would let radio tools attach crackle and glow to actual playback with one interface.
  The current build has browser playback only; adding recordings will need that glow hook or a tool adaptation.

## Verification and next workflow
Scratch contains numerical recomputation, all eight real-click path results, all required viewport frames,
phone host checks, keyboard and narration logs, Motion off and grayscale frames, and the final audit output.
The full audit finished in 1,384 seconds with 22 leads. Compact hints and Back focus were repaired and
checked separately afterward. The map state's keep region now checks its dialog rather than the inert
background controls. Missing Crew welcomes after a job or Mission tap are intentional: the spec makes
them stale. Quick repeated Crew or Motion taps deliberately cut speech, and the kit marks a welcome
heard when it starts. The full welcome remains in the Crew radio caption; no stale welcome is replayed.
The audit was not rerun after these targeted repairs. `audited-bundle.html` in Scratch preserves its input.
`codex-report.md` records the audit disposition and any remaining limitations. A cold review is next.
Build only: no commits, branch operations or polish round. Only this tool and its Scratch folder were written.
