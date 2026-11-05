# Neighborhood Issue Play: build handoff

## Scope and owner decision
Build only. No git commits and no polish round. Writes limited to this tool and its Scratch folder.

The spec's sole open question is resolved by the owner's explicit decision: restore the idea card's third issue. The UI says a new family moved in and neighbors cannot yet talk to each other. The family is never framed as the problem. Six fictional viewpoints and three fixes were authored for that restored scenario, emphasizing shared understanding, two-way greetings, pictures and language help. No real language or ethnicity is assigned. A cold sensitivity/content review is still useful. This build does not add a family viewpoint outside the specified six-neighbor cast.

The cast is human, retaining the six supplied names and roles without their animal species. All six puppet assets are marked `people: true` for the next painter. `paintedPeople` in src.html remains false. Set it true only after reviewed art is available, then tune head/body anchors. Until then tasteful faceless paper silhouettes work in all steps.

The empty-lot problem is removed. The empty-lot backdrop is retained because the owner replaced the problem and the spec separately lists it as a theater set. It introduces no garden-versus-parking scenario.

## Source map
src.html has responsive paper scenery CSS, then the six neighbors and three issue datasets, asset tokens, fixed voice lines, saved play state, live checks, and one render/bind pair per step. `window.__tool` exposes state, run, data, checks, suggestion, lineText, render and the voice log for review.

`state` is the saved authored play. `run` holds temporary performance state and is not saved. Scene lines store either a suggestion slot or custom text, so suggested dialogue follows changes to wants, blockers and the fix. Custom dialogue stays unchanged. The two initial lines in each scene are clearly labeled starter lines. Students can edit them or add up to six.

The three checks intentionally follow the specified simple rules. They do not validate the causal logic of a student-chosen blocker or the merits of a fix. Students explicitly tick whom a fix helps; the tool does not silently choose for them. Wants have a noun phrase, full first-person sentence and reported form so dialogue and read-backs keep pronouns natural. All four clash template slots are available when a character blocker makes the reply fit.

## Layout and controls
Wide layout uses a paper stage and a fixed action row on the right. The rest of the workbench scrolls. Short landscapes keep the panel beside the stage; phones stack the stage above the workbench. `fitTheater()` measures available real pixels after the speech bubble. Scenes uses one scene at a time at every width, preserving room for readable script lines.

Theater category buttons sit below the painted theater. This keeps all four categories visible while all six props or costumes fit in the compact workbench. Default props use available slots at 26, 50 and 74 percent to avoid accidental overlap. Students can still overlap props deliberately by dragging. Character wants and blockers come first; voice, movement and other character management controls follow in the scrolling editor. Scenes is also a scrolling editor on compact screens. These long forms are not a hidden answer-card set.

Props move with pointer capture or arrow keys, bounded to the stage floor. Resizing does not discard normalized prop positions. Costume pieces use CSS anchor positions corresponding to prompts.json head/body anchors. People assets override the nonpeople house-style prohibition for the next painter, while staying marked people: true and unpainted in this build.

Curtain, Next line, Auto and From the top stay live during entrances. Next line ends the entrance at once. Mode changes, reset and From the top clear all performance and preview timers. Auto uses 1500 + 60 * line length milliseconds. The flat preview uses six seconds even with Motion off.

## Voice
Curio.voice uses scope `state.step`, owns no hint writes, and Read explicitly reads the current hint. Neighbors and student scripts stay silent. Voice bank is friendly-dad / Achird; voice/lines.json contains 21 fixed instruction lines. No recordings were made, per the build instruction. Browser voice is the fallback and cannot guarantee the bank timbre. How lines use V.how; checkFail, flat, checkPass and bow use V.say with validity checks. A problem tap speaks the next listening action. Dialogs hush speech and suppress welcomes. Full scenes name Edit, not the disabled Add line button.

## Art
The spec says 30 images but enumerates 27: 21 nonpeople images and six people puppets. All 21 nonpeople images were generated with the built-in image tool, raw PNGs copied here, and processed only with art.py --rekey. Prompts and source credit are in art/prompts.json and tool.draft.json. Scene, curtain, text, silhouettes, audience and bubbles are code. Some fixed paper wing images include their own framing, appropriate to miniature scenery.

## Engine changes wanted
None. No kit files changed.

## Checks and remaining work
Build verification evidence and mechanical audit disposition are in codex-report.md. The single audit completed with 75 leads and 73 frames. Focus, textarea naming, default prop spacing, the compact theater shelves and the closing answer were repaired afterward and checked with targeted input and frames. The full audit was not repeated. Step tabs are outside the header, so the audit's automatic mode discovery found zero; audit-states.json explicitly reaches every step using real input.

Review should inspect the restored scenario, the compact workbench scrolling, temporary silhouettes and browser narration. Secondary editor fields and New play can require page scrolling on phones. The modal intentionally covers the page. Do not treat these documented choices, or targeted repair checks, as a clean repeated full audit.
