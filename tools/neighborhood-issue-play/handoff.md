# Neighborhood Issue Play: handoff after cold review

## Scope
One cold review, with repairs and targeted rechecks. No commits. Writes stayed in this tool and its Scratch folder. The builder report remains historical evidence; codex-review.md records the current review.

## Owner decision and sensitivity
Problem C is neighbors who cannot yet talk to one another after a family moves in. The family is never the problem. Fern speaks as a member of the new family, with her own ideas to share. Greetings and pictures work both ways; interpreter help is an option. No language, nationality or accent is assigned, and appearance does not identify language. Do not invite accent imitation or ask students to represent a community.

Six human puppets are painted, people: true, and enabled. The set includes different ages and skin tones, a walking stick, wheelchair and stroller. These are ordinary parts of the cast. The courtyard replaces the empty-lot set selection; old lot art remains preserved. A future fresh cultural lens should check the reciprocal communication, the family viewpoint, and whether the chosen character blocker encourages blame despite the framing.

## Source map
src.html contains the responsive paper scenery, neighbor/problem data, asset tokens, voice table, saved authoring state, plan checks, and a render/bind pair for each step. window.__tool exposes state, run, data, checks, suggestion, lineText, readback, render and the voice log.

state is the saved authored play. run is temporary performance state. Scene lines store a suggestion slot or custom text; suggestions follow changes to wants, blockers and the fix. Custom dialogue stays unchanged. If removing a character leaves a scene short, ensureScenes restores a two-line starter and preserves a setup/proposal line.

## Checks and content
The three checks verify declared plan choices. They do not assess the meaning of custom dialogue or whether a proposed fix actually works. This is stated beside the checks; reasons name the chosen blocker and proposed beneficiaries. Blank or punctuation-only wants/fixes fail. The street counter says Views opened, because opening material does not establish understanding. There is no mastery score or saved best score.

The school issue now asks the town to study crossings, traffic, speeds and pedestrian needs. The removed claims that crossing guards cannot stop cars without paint, or that every town must count cars before painting, are not safe general rules. Notes link FHWA guidance. All park dates, neighbors, reasons and proposed local fixes are fictional.

## Layout and art
The stage remains the focus. Short landscapes keep the workbench alongside it; phones stack it below. Main actions stay visible; long editors scroll. An empty casting stage now shows a painted audition lineup. Costume anchors correspond to the reviewed full cutouts, including their wooden sticks. Ball artwork scales with the theater independently of its 44-pixel tap target. Props stay within normalized floor bounds and support pointer capture and arrow keys.

The original street, proscenium, scenery and paper shelves are retained. Six people and a courtyard were generated with the built-in image tool, inspected, copied to art/raw, and processed with art.py --rekey. Gail's blank paddle was redrawn as an octagon. Several older cutouts were re-keyed to remove magenta fringes. art/prompts.json records prompts, source and anchors. The contact sheet is _scratch/neighborhood-issue-play/art-contact.png.

## Voice and timing
Curio.voice scopes speech to the step. Read speaks the current hint. The neighbors and script are read by the student. Each theater category has an instruction; repeated selection of the current category leaves its speech running. Perform entry no longer starts a flat preview over its welcome. Closing the curtain, changing roles or leaving an own-role line stops stale role narration. All fixed hints are in voice/lines.json and allLines().

No recordings were made. Browser speech is the current fallback, so bank metadata does not guarantee Achird's timbre. Main-path starts, repeats, Read, Sound and stale-line behavior are logged in Scratch. A cut in that log may be a deliberate later action, not a failed clip. The kit watchdog also bounds headless fallback speech.

Flat Preview lasts six seconds. Auto uses 1500 + 60 times the current line's character count milliseconds. Motion off removes movement and retains these times. Curtain focuses Next line, so Space and Enter advance immediately; other buttons retain their native keyboard actions. Next skips an entrance; Curtain closes during it; From the top clears run timers. The closing question is accompanied by the student's selected issue title.

## Verification
See codex-review.md and the Scratch evidence it names. The single final audit completed in under 23 minutes with a 40-minute limit: 50 leads and 76 frames. Phone card spacing, the compact fix/beneficiary group, and the closing hint were repaired afterward and re-shot at the affected sizes. The full audit was not repeated. audit-states.json reaches all five steps with real input and adds a people/costume state for the restored language scenario. An automatic discovery count of zero modes is expected because reached tabs are outside the header.

## Engine changes wanted
None. No kit or shared-script edits were made.
