# Usage Panel handoff

Build only. No commits or polish round. Read spec.md and codex-report.md before changes.

## Structure
src.html starts from the kit starter and includes the dark 9-12 theme. A single CASES array is inside the clearly marked case-data and timeline block. SOURCES names each evidence source. Hearing nodes stay in place during votes and speaker changes. Ruling controls rebuild only on entry or case change; individual radio and checkbox events update the note without replacing their controls.

asOf handles dated stance lookup. playRecord uses one cancellable animation-frame clock: eight seconds of moving time plus 1.5 seconds for every marker, including same-year markers separately. Motion off changes year movement only. Stop, slider pointerdown/input, markers, cases and modes invalidate the clock immediately. Record labels fan into a grid with leaders to the true linear dates so the 2015-2019 cluster remains selectable.

fitHearing measures the sentence card and panelist rows after content or size changes, keeping the marks inside the short preview. All 16 sentences were checked at 680x425 after voting. Long compact cards use tighter sentence spacing; larger screens retain the generous painted emblems.

buildNote is a pure function. Partial rulings omit undecided settings and empty choice groups. Every case owns votes, private marks, reasons, choices and edited text. Storage is validated on load and every access is caught. Copy has a clipboard fallback. Confirmation uses a keyboard-accessible dialog and returns focus with preventScroll. __tool exposes state, cases, saved work, note builder, stance lookup and the kit voice log.

## Open questions and specification tensions
- The only listed open question asks about AHD evidence for personal they. Keep the Jordan sentence note-only, with no acceptability vote or borrowed statistic. The AHD entry has a 2015 survey about a different sentence; that figure is not transferred here.
- The brief requests built-in image generation and overrides the spec's local FLUX provider. All six assets were generated with built-in imagegen, copied to art/raw and processed only with art.py --rekey. No people appear.
- The exact original edition sources for several historical markers are not all accessible from the supplied links. Keep those provenance gaps visible in the report, especially Chicago 1993 and the split-infinitive guide dates. The sources are named, not invented.
- The spec supplies uncertain date ranges but requires an integer slider. Labels retain the uncertainty; numeric placements are explained in notes.md.
- Markers that share recent years cannot have both readable 44 px labels and literal coincident horizontal positions. The axis keeps true positions, while labels stack and fan with thin leader lines.
- The spec's note ending says earlier authorities ruled differently even when Literally's only authority marker is the current entry at 2026. That case uses a factual current-entry ending rather than pretending the inclusion year is known.
- The prescribed 1.5-second marker pause is short for some source cards. It is retained; Stop and all controls remain live so students can inspect a card.
- The spec's Indiana University APA link is dated 2016. The same guidance is checked against APA's own singular-they page, with the edition date retained from the spec.
- Compact Ruling keeps the grid central and the note below it as specified. Reference content can scroll. See report for measured layout limits.
- At short preview heights, Record's stance board sits beside the fanned marker labels under a full-width axis, with the source card below. Year and playback controls remain sticky while reading it. This fits readable 44 px marker targets and the board together.
- The under-760 hearing card grid conflicts with fitting a 680x425 preview. STANDARDS wins: short landscape previews keep the five emblems in one row; tall phones use the requested two rows.
- Some supplied panelist statements exceed the brief's two-short-sentence reading guideline. Their specified wording is retained, with Read and a scrollable statement region.
- The They usage note explicitly says generic singular they, so a contextual Avoid choice cannot be read as a ruling on a known person's pronouns.

## Sensitivity
Singular they includes personal pronouns and nonbinary identity. The known-person example never asks whether that person's pronoun is acceptable. Review the respectful distinction between personal pronouns and the generic-usage disagreement. No portraits, bodies, religion, Indigenous topics or hard-history scenes are depicted. Do not equate home-language conventions or dialects with intelligence.

## Engine changes wanted
None. Kit, scripts, docs and other tool sources remain untouched. Reference tool copies were bundled only inside Scratch.

## Voice and art
The chair premise remains in the Hearing hint and Read even when the first action skips welcome. Explicit emblem requests replay their argument as events; automatic how-to instructions remain once per load. Evidence is a nonmodal drawer fitted inside the work stage, so docket tabs and the hint remain visible and usable. Case and mode changes close it; Escape and Close also dismiss it.

voice/lines.json lists the specified firm-captain voice and all fixed spoken lines. No recordings were made, as required by the Build brief. Browser fallback does not reproduce the bank voice's timbre. art/prompts.json is the complete saved prompt set; all six assets have people false and drawn_by codex. No paintings are missing.

## Cold review changes
Read in the evidence drawer selects one visible card instead of speaking all off-screen cards. Opening and closing that drawer updates the hint synchronously; closing also stops its reading. Private marks on the personal-pronoun example never suggest a hidden vote control. Adding or selecting Your panel hushes earlier instructions. Carried-forward panel percentages include their original survey year. Successful storage writes restore the saved status after an earlier error.

The teacher paper stack was redrawn through built-in imagegen on magenta, with the complete prompt saved in art/prompts.json. All five cutouts were reprocessed with art.py --rekey using despill and hole handling. Their warm painted style, room, plates and materials remain. The personal ruling card has a restrained diamond seal and separate setting lines; live note changes have a brief ink-settle treatment that stops with Motion off. No new topic, assessment or mode was added.

Post-audit fixes: private marker labels show all four short setting choices, with compact layouts reserving two columns for that label. Page Up/Down visits both markers when years repeat, and can reach the personal marker. Paper metadata, placeholder and status ink now use #6a4c2d, at least 5.63:1 on the darkest paper. No welcome may start over an open drawer or confirmation; opening confirmation hushes speech, and the dialog describes its question to assistive technology.

Selecting the private marker directly also refreshes the hint. This covers interrupting an active sweep after the marker was already added; the old playing hint must not survive that stop.
