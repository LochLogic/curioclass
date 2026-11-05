# Monologue Rehearsal build handoff

Build only. No commits, branch changes or polish round. The final report records the checks and open leads.

## Structure

- src.html starts from the kit starter and uses curio.css, theme-912 and Curio.voice. Its layout is real pixels,
  rather than scaling a fixed scene. The top section is responsive CSS; the script contains content adapters,
  Choose, Prepare, Rehearse, Perform and Compare renderers, followed by wiring and the test hook.
- content.json is loaded through `"json:content"`. It contains the four speeches, source IDs, circumstances and
  six wants per speech. Art tokens remain in src.html because art expansion precedes JSON expansion.
- `saved` owns serializable work under `curio-monologue-rehearsal`; `state` owns temporary mode and interaction state.
  Circumstances belong to a monologue. Each of its three versions has independent marks, stress, pauses, beats and
  closest want. Beat settings are keyed by the index of the beat's first token; removing a mark removes that row.
- Every performance snapshots the chosen version and the actor's own want before handoff. Later edits cannot rewrite
  an earlier take. All performances, including different monologues, remain selectable in Compare.
- `match(marks, flags)` uses token indices with the inclusive window [mark - 2, mark + 6]. Each flag chooses its nearest
  mark; ties choose the earlier mark. Several flags may refer to one mark; the headline counts unique matched marks.
- Source verse line endings are retained in the reader, rehearsal and overlay. Score and listener word targets wrap
  within those lines. Score's 44-pixel space-dot targets are deliberately generous, so this view is more spread out.
- The actor's score is removed from active DOM markup in partner view. Read uses only the instruction hint; it never
  narrates the speech or exposes the actor's plan. No microphone, camera or recording API is present.
- Keyboard word navigation uses one roving Tab stop. Arrows move through words and spaces; Enter activates them.
  Native button focus is preserved when marks change. Version switches restore focus with preventScroll.
- At 375 pixels Score has a bottom sheet. Long scripts, circumstances, beat lists and reflection records scroll.
  The short landscape layout uses A/B/C labels and a compact response form with Save visible.
- V welcomes are valid only while their instructions fit. The two event IDs are landed and wantRead. A sequence may
  drop an unstarted result after the student leaves Compare, as required by scope and stale-line behavior.
- The elapsed rehearsal timer stays active with Motion off. Only the quiet rehearsal indicator animates; its CSS loop
  is explicitly disabled in calm mode. Resize repositions the current beat or recomputes overlay brackets.

## Source and number notes

- Direct Gutenberg text downloads and extraction are in Scratch. Word counts excluding the two cut markers are
  207, 179, 208 and 161. Mrs Hale has 163 space tokens including the two `[...]` markers, which still take indices.
- At 150 words per minute the displayed durations are 1:23, 1:12, 1:23 and 1:04. The spec's rounded card durations
  were 1:25, 1:10, 1:25 and 1:05; this build displays the recomputed estimates and names the assumption in the reader.
- Viola has 25 source lines, rather than the spec's 24. The other Shakespeare passages have 24 and 26. No text or line
  was removed to force the count. The Glaspell cut follows the supplied wording and cut markers exactly.
- The Helena fact panel follows the supplied Content wording, "Athens, by the Duke's palace." The eBook stage heading
  is a room in the palace. The outdoor garden painting is the spec's requested evocative setting, not documentary proof.
- Computed contrast: teal on panel 8.96:1, teal on section 8.49:1, dark ink on teal 9.56:1, script on black 16.32:1,
  gold flags on black 13.49:1. The sample matching rule produces one of four matches and an unmatched flag at 147.

## Open questions resolved

The spec has no explicit open-question section. Choices follow its stated leaning: three versions, real partner
evidence, a nearest-mark matching window, shuffled listener wants, local saving and no recording. The tie-break for
equally near marks uses the earlier mark; the spec leaves that tie unspecified. No extra topic or game mode was added.

## Art

All nine assets were made with the built-in image tool during this build, using the house style in art/prompts.json.
Raw PNGs are in art/raw and final 1200-pixel WebP assets are in art. The Roman street was redrawn once to replace
figurative arch carvings with geometric and leaf ornament. The original is archived in Scratch. All active final
images were inspected at final size for people and lettering. There are no deferred people assets.

The spec's FLUX production note was superseded by the user's explicit request to use the image tool. All sources
credit OpenAI gpt-image. No images were downloaded and no paid art.py generation form was used, only --rekey.

## Engine changes wanted

None. No shared kit, source docs, scripts or other tool files were changed.

## Verification and remaining limits

Scratch contains bounded command helpers, source downloads, arithmetic, the full interaction results, the narration
log, standard-size frames, phone frames through host port 8795, the bar comparison and the final audit output.
Chrome debugging was restricted to ports 9990 and 9991. Test Chrome and host processes are closed by their helpers.

No voice recordings were made, following the build-only instruction. The ten-line soft-breath / Enceladus manifest
is ready; current speech is the kit's browser fallback and cannot reproduce that bank voice exactly.

The tenth instruction is a one-beat welcome derived from the existing rehearsal instructions. It avoids naming Next
when no change is planned. Active mode taps leave current speech intact. Editable fields have explicit accessible
names in addition to their enclosing labels. The phone footer keeps the local-device privacy statement visible.

At the smallest landscape size, the long circumstances, score settings, performance list and Connect prompts require
panel scrolling. Some dense Choose-card captions also scroll within their cards; the four card choices stay in view.
No human classroom pair supplied listening evidence during this build. Automated held-click flows exercised the
actor and listener roles, and the frames were visually inspected. Live delivery and listening quality need classroom use.

The user's instruction to stop as soon as codex-report.md is written takes precedence over the brief's request for
an early report file. Interim evidence was kept in Scratch; the report is written as the final build action.

## Audit closure

The single full audit completed in 586 seconds with 27 leads and 73 frames, all inspected. Default sizes, targets,
motion-off behavior, resize recovery, runtime checks and five-click repetition were clean. Ten naming leads were
addressed with explicit aria-labels, and the active-mode welcome interruption was fixed. Twelve scroll-panel leads
refer to the intentionally long circumstances and comparison forms. Four skipped first-card welcomes follow the
spec's explicit stale-on-card-tap rule.

Targeted checks after the audit passed for active-mode speech, one-beat instructions and breath, clearing transient
word/timer state on a new monologue, explicit field names, and the phone privacy footer. Only affected frames were
re-shot; the full audit was not repeated. The ten-line manifest includes one conditional one-beat how-to to avoid
directing a student to a disabled Next control. All test Chrome and host processes were closed; host.html was removed.
