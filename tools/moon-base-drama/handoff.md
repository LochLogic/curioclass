# Moon Base Drama build handoff

## Codex fix, round 1, 2026-11-06
This section supersedes the older review notes below. The current path frontier drops whenever Back or Rewind
invalidates choices. Rewind requires a node behind the current beat or a current choice; its handler guards this
as well as disabling the button. Old icons are independently faded, including an unanswered current node.

Choice content uses six shared inline SVG drawings on buttons, map diamonds and rewind cards. The map is an accessible
list with decorative dots. Options are voiced in the actual shuffled order after the fact, including Read and rewind.
The role premise can recover through Sound on or Crew entry and is carried into Start mission if still unheard.
The three endings speak the outcome before their first reflection instruction. Ada has six unspoken result reactions
and an unspoken invitation to revise dialogue in the child's own words after Back or Rewind.

Night rendering separately controls background light, desaturation, yellow hanging leaves, and cold-blue frost.
The painted backgrounds, healthy planter and all existing props remain. A ResizeObserver reserves the actual radio
height below choices at all sizes and card heights on phones. Compact choice captions keep the full fact and both options; their how-to and
rewind invitation are already in the visible hint and card. Large Crew badges have more subtitle and prop-label space.

Radio glow follows V.playing for events. Read uses a small adapter around Curio.say(text,true), whose actual promise
completion clears activeRead for both Audio clips and speech synthesis. Every operative action clears activeRead and
hushes the kit. No queue or audio engine is copied. Header Read and modal Read map use the same adapter. Read events
are retained in V.log. This is needed because the current kit does not expose native Read's completion or playing text.
All fixed Read forms and both option orders belong to L and voice/lines.json (93 matching lines). No narration was recorded in this fix.

The single final audit completed with exit 0 and 19 leads. All 68 frames were inspected. Its real new lead was a long
rewind caption overlapping choices at 1366x768; measured radio height now reserves that space at every choice size.
Targeted follow-up frames show 14 px separation at 1366x768 and 9 px at 680x425, with both button centers unobstructed.
The same follow-up verifies accurate visited/current/old/future accessible path labels, including ordinary nonchoice
beats. The audit snapshot predates these two small follow-ups; the audit was not repeated. Detailed evidence and
dispositions belong to polish.md.

The prescribed options still admit an always-longest-text route to full resources in all eight shuffle configurations.
No new assessment or content rewrite was authorized by this Refine. The report conservatively leaves its stronger
no-skill-pass condition open; full resources must not be represented as proof of Moon science understanding.

Current evidence and the final audit are under `_scratch/moon-base-drama/fix-*`. Read polish.md for verified outcomes.

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
The round 1 fix section above describes the current glow and Read behavior.

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
- Both Mission entry and Start mission require a checked job. A premature Mission tap names the job action
  and focuses its first badge. Back at beat 1 returns to Crew; Next at beat 8 becomes New mission.
- A newly picked branch leaves later old icons faded until a new choice is picked at those beats. The new current
  choice replaces its old icon immediately, and active resources include only the new branch.
- The story map is a compact, noninteractive strip. Rewind opens the large three-choice map; unavailable
  future choices are disabled. Before any choice is visited it explains how to return instead of naming a disabled choice.
- The shared kit stores only its Motion preference. The spec's literal "nothing is saved" cannot be fully
  satisfied without a kit change. Notes disclose this; no classroom or story information is saved.
- The Sources temperature conversion is wrong: minus 130 Celsius is minus 202 Fahrenheit, not minus 208.
  The radio has no exact temperature, so no script correction was needed. The spec itself is unchanged.
- Cold review corrected the overbroad freezer dialogue to a home-freezer comparison, clarified daylight
  versus the full lunar day, and distinguished no breathable air from literally no atmosphere.
- This is a teacher-led role play, not a scored quiz. The supplied choice order and truthful teaching
  feedback remain. The meters show story resources, not physical engineering quantities.

## Engine changes wanted
- `kit/curio.js`, `init` Motion handler: add an opt-out for persisted Motion preferences, so tools requesting
  no storage can keep that setting in memory. No shared files were changed.
- `kit/curio.js`, `voice` / `speakOne`: expose actual playback start/end callbacks for both recorded clips and
  browser speech, including Read, and expose Read's current text/completion. This would let radio tools attach
  crackle and glow to one playback interface and remove this tool's small Read adapter. The tool now supports
  recorded playback through that adapter and V.playing; the shared change is optional for this fix.

## Verification and next workflow
Cold review changes: the first how-to is a prefix in its event transmission, chosen using V.heard across
the finite guided keys. This keeps the instruction and fact in one real utterance at a two-second tap
pace. The transmission is an event, so later job/beat/result taps still speak, without repeating its how-to.
The voice manifest includes these fixed combined transmissions as well as their individual lines.

Choice positions are sampled once per mission and retained across rewinds. State stores semantic choices,
not button positions. A committed choice can only change after Back or Rewind. Opposite taps leave every
meter unchanged and name Rewind. These are story outcomes, not an assessment of a child's knowledge.
The rover now brings a visible ice load after a water choice, with a smaller load for finding it late.
Compact screens retain battery and warmth effects. New mission from the map restores focus to Next.
On phones, response art sits to the right of the beat label and the ending planter sits above Ada's card,
so the changing plants and tray remain visible instead of disappearing behind the script.
The longest first-beat caption also has a clear gap below Ada's card. This phone-only spacing repair was
made after the review audit's failed iframe-context probe and rechecked in a real 375 px host.
Read map is available inside the native modal and speaks its own instruction, never a covered story beat.

## Sensitivity
Fictional crew roles and Moon science, with no cultural, religious, Indigenous or hard-history representation.
The class supplies the people in this teacher-led drama; the paintings deliberately show empty equipment.

## Original build verification
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

## Cold review verification, 2026-11-05
The review audit ran once with the 2,400-second cap and completed with exit 0. Its 18 leads are two
iframe-context probe consequences, seven intentional first-tap welcome skips, and nine intentional
quick-tap interruptions. Five-click repeats, layout/target checks, Motion off and resize stress were clean.
Its automatic Mission walk stays on Crew because a job is required. Separate real-input Mission walks
cover all eight outcomes, every resource sweep, all rewinds, replay, Sound-off Read and keyboard controls.
The 59-line manifest matches runtime allLines exactly. No story state is persisted.

The failed iframe probe was covered with real held input at 375 px via host port 8755. That follow-up
found a small first-beat card/radio collision. Only the phone spacing changed after the audit, with Crew,
night and the longest first-beat message re-shot. The minimum measured gap is 3.625 px; phone job badges
remain 172.5 px high. The audit input is preserved in `_scratch/moon-base-drama/review-audit/host/tool.html`.
All 64 audit frames were inspected. Other current evidence and the final validation manifest are in Scratch.

Audit reader improvement wanted, outside this tool's write scope: `scripts/audit_tool.py`, `Audit.size`,
needs a fallback when child-frame execution-context discovery returns none. A same-origin iframe-window
probe worked in the separate drive.py host tests. No audit, kit or other shared source was changed.
