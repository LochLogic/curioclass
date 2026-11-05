# Codex review: biome-atlas

## Played

Cold Grade 12 solo play before builder notes: Read, wrong and correct Key paths, Reveal, Clearing, Play, rewind and a rain shift. Then read through projected examples, including Dodge City's miss. The large climograph and painted reveals are strong; recovery originally felt softer and flatter.

## Findings fixed

- Blocker, general, Key: Real biomes disclosed untried answers. Each real pin now stays unknown until that station's Reveal.
- Should fix, general, Key: the dry-month chart outlined the answer months. It now outlines the whole year for that question.
- Should fix, general, Key: incorrect Dodge City comparisons could blame the model. Wrong paths now get a numerical-check explanation and their own spoken event.
- Should fix, general, Craft: comparison feedback shrank into a clipped strip. Fixed flex sizing, compact Key station details and short-screen spacing. Open phone feedback now fits in view.
- Should fix, general, Craft: answer buttons and map pins rebuilt after actions. Reuse answer buttons; preserve pin elements when map dimensions stay unchanged. Focus remains usable.
- Should fix, general, Voice: old station speech and stale welcomes could outlive their state. Station changes hush; welcome eligibility and fallback validity now match the current state.
- Should fix, general, Voice: quick repeated mode or pristine Reset taps cut welcomes. Redundant taps now leave the current line playing.
- Should fix, general, Craft: checked feedback followed mode switches. It now belongs to Key only.
- Should fix, general, Craft: all-station chart labels overlapped, and shifted labels/accessibility values used base climate. Labels now avoid collisions and follow the current dot.
- Should fix, general, Graphics: 480 px cutouts blurred across the landscape. Re-exported all twenty at 1400 px, quality 72; redrew the sparse tropical canopy as a closed, layered forest.
- Polish, general, Play: recovery lacked an earned visible result. Added the next approximate milestone, a progress edge and a specific same-climate completion, retaining the required eight-second run.
- Polish, general, Craft: captions covered low plants and early year labels collided. Reserve a measured caption band and space tick labels in pixels.
- Polish, general, Voice: first Place could speak an obsolete welcome. It now gives its own next-action instruction; Check and layer changes also give sound feedback.

## Findings left

- Should fix, spec/source: the WWF point query puts Niamey in West Sudanian savanna, rather than the named ecoregion in the spec. Kredarica's regional forest polygon does not verify local alpine vegetation. Retained the supplied categories because changing the spec is forbidden; notes disclose the limits.
- Polish, general: Clear my progress remains in the scrollable footer at some sizes. The equivalent Reset stays visible; this is not a hidden answer choice.
- Polish, general: narration uses browser speech. Recording audio is outside this brief.

## Flattest moment left

Thirteen key traversals can still become routine. Kept the specified branching structure and Dodge City's deliberate surprise; no extra challenge or topic was added.

## Graphics

Checked all thirty paintings in contact sheets and mode/stage frames. One canopy redraw; twenty sharper exports. No people, missing assets or placeholders.
Built-in imagegen prompt and selected raw: art/prompts.json and art/raw/ba-k-tropical-canopy.png. Finished asset: art/ba-k-tropical-canopy.webp.
Final art: 5,758,650 bytes. Bundle: 7,848,991 bytes, about 7,849 decimal KB (7,665 KiB). The required Size line explains the full-screen art in notes.md.
Opened the existing Beat Lab and Snowy Mail Route bundles as finish references; preserved the atlas's richer landscape cards and instrument layout.

## Audit

Ran audit_tool.py once, last, on Chrome 9941 and host 8745, with a 2400-second process-tree limit. It finished: 57 leads, 89 PNGs inspected. Motion off, repeat clicks, console checks and resize stress had no errors or stuck controls.
Confirmed and fixed: 9 chart-label rows, 1 phone-feedback row and 4 quick-tap speech rows. Also repaired the walk's rebuilt pin elements and a manually confirmed stale Key welcome.
Answered the other groups: 14 footer/short-choice rows concern the secondary reset duplicate; 15 SVG/path rows concern circular bounding-box corners; 14 missing welcomes correctly yield to the first action's own instruction.
Focused rechecks only: zero label overlaps at 680, 800, 1000, 1280 and 1366; all thirteen pin centers hittable and elements stable at 1000, 1280 and 1366; phone feedback ends at 779.7 of 812 px; all four quick-tap cases preserve speech. Completed-Key re-entry speaks Reveal. No console errors.
The audit misses panel modes in automatic mode discovery. Explicit states covered Key and Change; separate held-input checks covered their controls and narration. No second full audit was run.
Evidence and grouped responses: _scratch/biome-atlas/audit-responses.md, review-audit/, post-audit-frames/ and post-*.json.

| Voice check | Kind | Expected | Spoken |
| --- | --- | --- | --- |
| placeIt, five station actions | how | 1 | 1 |
| first Place instruction | how | 1 | 1 |
| match | event | 5 | 5 |
| miss | event | 5 | 5 |
| shifted, nine boundary changes | event | 9 | 9 |

Full voice-line parity passed. Keyboard-only play reached Reveal with tally 1 of 1; grayscale inspected. Calm recovery measured 7.90 seconds. Real Years input pauses Play; climate input leaves Play running.

## Left open

Independent Python matched every monthly spec input, all thirteen base outcomes, all eleven what-if checks and Dodge City's 546.0 mm dry line. The 12-of-13 tally is verified against the supplied assignments, not thirteen independently observed local vegetation records.
Regional source evidence: _scratch/biome-atlas/review-ecoregions.json, queried from [UNEP-WCMC's WWF layer](https://data-gis.unep-wcmc.org/server/rest/services/Hosted/Terrestrial_Ecoregions_of_the_World/FeatureServer/0). The spec/source discrepancies above need a spec decision.
The spec's 200 divisions put the approximate 0.3-year milestone between 0.28 and 0.32; Play crosses it. Kept that rule.
Writes stayed in tools/biome-atlas/ and its Scratch folder. No commits, shared engine edits or new review round. Owned Chrome processes and servers are closed; host.html is absent.
