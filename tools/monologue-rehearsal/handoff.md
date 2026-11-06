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
- Cold review corrected Helena's context to tomorrow night and a room in Theseus' palace, following Gutenberg 1514,
  Act I scene I. These correct the supplied Content wording. The requested outdoor garden painting stays atmospheric,
  not documentary proof. The spec remains unchanged; its source heading supports the corrected fact panel.
- Computed contrast: teal on panel 8.96:1, teal on section 8.49:1, dark ink on teal 9.56:1, script on black 16.32:1,
  gold flags on black 13.49:1. The sample matching rule produces one of four matches and an unmatched flag at 147.

## Open questions resolved

The spec has no explicit open-question section. Choices follow its stated leaning: three versions, real partner
evidence, a nearest-mark matching window, shuffled listener wants, local saving and no recording. The tie-break for
equally near marks uses the earlier mark; the spec leaves that tie unspecified. No extra topic or game mode was added.

## Art

All nine assets were made with the built-in image tool during this build, using the house style in art/prompts.json.
Raw PNGs are in art/raw and final 1200-pixel WebP assets are in art. The Roman street was redrawn once to replace
figurative arch carvings with geometric and leaf ornament. The original is archived in Scratch. Cold review replaced
the weakest audience image, mr-class, with attentive classmates in the same room and painted style. It is marked
people: true, with its full prompt and asset-specific house style in prompts.json. Other settings remain empty.

The spec's FLUX production note was superseded by the user's explicit request to use the image tool. All sources
credit OpenAI gpt-image. No images were downloaded and no paid art.py generation form was used, only --rekey.

## Engine changes wanted

None. No shared kit, source docs, scripts or other tool files were changed.

## Verification and remaining limits

Scratch contains bounded command helpers, source downloads, arithmetic, the full interaction results, the narration
log, standard-size frames, phone frames through host port 8795, the bar comparison and the final audit output.
Chrome debugging was restricted to ports 9990 and 9991. Test Chrome and host processes are closed by their helpers.

No voice recordings were made, following the build-only instruction. The twelve-line soft-breath / Enceladus manifest
is ready; current speech is the kit's browser fallback and cannot reproduce that bank voice exactly.

The conditional one-beat welcome is derived from the existing rehearsal instructions. It avoids naming Next
when no change is planned. Active mode taps leave current speech intact. Editable fields have explicit accessible
names in addition to their enclosing labels. The phone footer keeps the local-device privacy statement visible.

At the smallest landscape size, the long circumstances, score settings, performance list and Connect prompts require
panel scrolling. Some dense Choose-card captions also scroll within their cards; the four card choices stay in view.
No human classroom pair supplied listening evidence during this build. Automated held-click flows exercised the
actor and listener roles, and the frames were visually inspected. Live delivery and listening quality need classroom use.

The user's instruction to stop as soon as codex-report.md is written takes precedence over the brief's request for
an early report file. Interim evidence was kept in Scratch; the report is written as the final build action.

## Cold review changes

Partner and response phases disable the actor's modes and guard setMode until a response is saved. Save requires both
a want and a nonblank feeling word. The native Space action on buttons works; only non-control Space is a rehearsal
shortcut. Compare now describes nearby flags and closest-want agreement, without claiming proof of understanding.
Its evidence note stays beside the count; Plan a change / Revise a choice in Score returns to that take's work.
The broadFlags guard replaces the ratio and suppresses landed when 12 or more flags cover at least 75 percent of
possible boundaries through the matching window. It leaves raw flags and brackets visible and preserves the record.
Compare and response have how-to narration; the audience reflection allows an unchanged performance.
The input is still a human listener's report. The tool cannot authenticate live acting or distinguish fabricated taps
from real reactions without recording, which the spec forbids. It has no grade, mastery gate, best score or pass badge.

## Sensitivity

Review the Shakespeare characters' gender generalizations, romantic rejection and public shaming as character views,
not universal truths. Trifles includes gendered isolation and a death investigation; the selected cut contains no
graphic violence. No student needs to disclose personal experiences. Any student may play any character, and physical
tactics can be adapted. A cultural reviewer should check this framing and the ancient Greek/Roman atmospheric settings.
The new classroom image has varied skin tones and one wheelchair user participating in the same group. Review its
natural representation and the final card crop; prompts.json identifies it as a people asset.

## Cold review verification

The single cold-review audit completed: _scratch/monologue-rehearsal/review-audit/audit.md, 76 frames, all inspected.
Its 17 leads are thirteen intentional long-form scrolling reports and four first-card welcomes made stale by the
reader opening, as the spec requires. No additional blocker or should-fix was confirmed. Standard sizes, targets,
clipping, runtime, Motion off, resize recovery and the audit's held/quick input checks are clean.
The manual five-mode voice walk gives each main-path how-to once and both result events five times across five takes.
The side path covers the one-beat instruction and Read with Sound off. Keyboard-only completion and confirmed Clear all
pass. Snapshot integrity, reload persistence, option cycling, the 30-flag cap, matching boundaries and wide flag sweeps
were rechecked. Evidence is in review-*-results.json, the targeted frame folders and the review-audit frame manifest.
Final bundle: 1,663,484 bytes. Assigned Chrome/host ports are closed; host.html is absent. No commits or shared edits.

## Audit closure

The single full audit completed in 586 seconds with 27 leads and 73 frames, all inspected. Default sizes, targets,
motion-off behavior, resize recovery, runtime checks and five-click repetition were clean. Ten naming leads were
addressed with explicit aria-labels, and the active-mode welcome interruption was fixed. Twelve scroll-panel leads
refer to the intentionally long circumstances and comparison forms. Four skipped first-card welcomes follow the
spec's explicit stale-on-card-tap rule.

Targeted checks after the audit passed for active-mode speech, one-beat instructions and breath, clearing transient
word/timer state on a new monologue, explicit field names, and the phone privacy footer. Only affected frames were
re-shot; the full build audit was not repeated. The manifest includes one conditional one-beat how-to to avoid
directing a student to a disabled Next control. All test Chrome and host processes were closed; host.html was removed.
