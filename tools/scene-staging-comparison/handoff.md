# Scene Staging Comparison: build handoff

## Structure
One offline src.html with kit:curio. Responsive CSS creates the dark theater-program desk.
The script contains the ten captions, timing and staging tables, code silhouettes, Web Audio cues,
two-viewer persistence, live reaction stamps, set-difference ranking, comparison grid and six layer views.
The opinion builder accepts only the selected viewer's actual stamp on the selected production and moment.
window.__tool exposes the state, content tables, timeline and focused verification hooks.
DOM order puts the panel's primary controls ahead of the longer comparison grid.

## Tricky parts
- The playback clock uses performance.now and requestAnimationFrame. Each moment is its specified pause,
  whitespace caption words / 2.5, and one extra second. Motion changes do not reset that clock.
- Previous and Next preserve playback; switching Viewer changes subsequent stamp ownership at once.
  Mode switches stop. Read stops playback before the kit reads the current hint.
- Scene dialogue stays silent. The clock, rain, accordion sting / slide and door slam are local synthesis.
  Sound off and Stop cancel every active sound node and silence the gain bus.
  Rain nodes are separately stopped at moment 9. The door slam follows the exit movement, rather than preceding it.
- No narration overlaps playback. bothDone events triggered while playing are deferred to Stop or completion
  and dropped if their viewer is no longer current. Event instances have unique queue keys.
  Play from another mode enters Watch quietly before starting. A stopped first reaction is allowed to speak the welcome.
- Reaction lists keep three entries including duplicates; set differences collapse duplicates.
  Ranking counts the symmetric difference and breaks ties by earlier moment, even when a difference is zero.
- Chips are per viewer and moment. Stamps are per viewer, production and moment. Six opinions are shared
  across the pair, with viewer identity retained. All saves use localStorage in try/catch.
- A native confirmation dialog resets both viewers. Cancel keeps the complete record.
- Layers have frozen representations; the arrows represent position changes since the preceding moment.
  Character initials inside the dots link to a separate name legend so close blocking cannot overlap labels.

## Spec choices and open questions
- No explicit Open questions section was present. The following contradictions / gaps were resolved locally.
- Timing: supplied word counts reproduce 70.1 and 55.8 seconds. Complete final captions count
  18, 15, 12, 12, 10, 9, 17, 14, 6, 15 words, giving 77.7 and 63.4 seconds.
  This follows the spec's instruction to recompute with final caption text. Role and action labels count.
- Production 1 is fictional: the 1890 label deliberately borrows the realistic style described as a decade later.
  Its time explicitly says so rather than presenting it as a real historical reconstruction.
- The viewer-to-viewer aggregation is unspecified when each viewer has two production sets. This build
  unions each viewer's two sets at each moment, then applies the same 0 to 5 symmetric difference rule.
  A swap of reactions between productions can therefore disappear from the viewer comparison, while
  remaining visible in the four rows and in the production comparison. Review this interpretation.
- Missing data from either viewer produces no viewer split, rather than treating absence as a feeling.
  Production ranking still compares a watched production with an unstamped one as the set rule specifies.
- With all scores tied at zero, Show splits highlights moments 1, 2 and 3, following the earlier-tie rule.
- stampHow at eight seconds is a visible hint only: the no-narration-during-play rule takes priority.
- An extra emptyCompare line avoids telling a student to tap a disabled Show splits control.
- At widths under 900 the frames stack in tall windows. Short landscape previews keep them side by side,
  preserving caption legibility and the primary controls under STANDARDS. At 375 one frame is selected by P1 / P2.
- The phone's comparison table scrolls horizontally, and its opinion builder and Layers details scroll vertically.
  All reaction choices, playback controls and mode tabs stay visible in Watch.
- Physical acting uses faceless code silhouettes, poses and transitions. The dog mime has drawn leash traces.
  Gestures are stylized, especially embraces and kisses, rather than a detailed animated performance.
- The smooth-narrator / Algieba bank selection is in voice/lines.json. No recordings were made as required;
  kit browser speech remains the fallback and its exact voice depends on the browser.

## Art
All four requested paintings were generated with the image tool and copied into art/raw.
art.py --rekey made the final WebP assets, inspected individually and in the tool.
The people-free wardrobe uses headless garment forms and hanging clothing. There are no painted characters.
Prompts, house style and drawn_by are retained in art/prompts.json.

## Engine changes wanted
None. No kit, docs, scripts or other tool files were edited.

## Verification pointers
Evidence lives only in _scratch/scene-staging-comparison.
numbers.json recomputes timing and contrast; functional.json checks live held input, separation, split math,
six layers, chip saves, evidence gating, reload, Read and Reset. voice-check.json checks five repeated
held taps at two-second pace. full-play.json records actual complete timings and moment boundaries.
The final frames cover all STANDARDS sizes, grayscale, keyboard and Motion off.
The report will record the single audit's outcome and any remaining leads.
This is Build only. No commit or polish round was started.

## Final audit and targeted repairs
The single audit finished within its 40-minute limit, with 27 leads. It found no exceptions,
stuck controls, resize failures or infinite motion. The five-repeat and rapid-tap voice checks were clean.
Every lead has an individual disposition in _scratch/scene-staging-comparison/audit-dispositions.md.
The confirmed repairs are an explicit evidence-field name, zero horizontal table overflow at 680 pixels,
enabled-control-only playback hints, a correct first-reaction welcome, and a dialog-only keep fixture.
Additional frame-led repairs contain Layers columns, keep all seven reason chips together, enlarge diagram labels,
keep the entire pratfall visible, add latest-reaction words to the miniature strip, and preserve inactive caption contrast.
The phone still scrolls its wide comparison table; a swipe instruction makes that explicit.
Reset remains below the compact panel's initial fold at 680x425. It is a secondary confirmation control,
and all primary Play, stepping and reaction controls remain visible. This lead is retained deliberately.
Modal coverage of the background hint is expected; its keep fixture no longer demands an uncovered background.
Targeted evidence includes compact-repair.json, cue-contract.json, sound-tail-stop.json, motion-final.json,
phone-held-input.json, phone-layout-repair.json, reaction-welcome.json, reset-welcome.json and delivery.json.
The final delivery HTML is checked byte for byte against the tested Scratch candidate.
The full size sweep and audit were not repeated after repairs. No shared files were changed.
