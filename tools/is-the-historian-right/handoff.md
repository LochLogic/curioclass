# Is the Historian Right? handoff

## Cold review changes, 2026-11-07

The reviewer played the complete Titanic path and language mode before reading this handoff or the builder report. Evidence lives in `_scratch/is-the-historian-right/review-*`, `probe-before` and `probe-after`.

Step buttons now compute unlocks on every click instead of capturing stale values. Writing separates the original claim from the student's revision. Clue changes clear their reasons and update the preview afterward. Help changes invalidate filed seals. The language-part check rejects one-letter reasons, a bare vocabulary list, repeated filler and a contradictory Lots of help overall chip; it remains a transparent structural aid, not semantic grading.

Language drawers now show all word titles in a physical card index beside the selected large card. The Hear it control reads only that selected card. The extra pair, Chicago stamp and photograph how-to lines use Curio.voice and are listed in voice/lines.json. The primary photograph remains unchanged and can be inspected at readable width. Stamp handles have wood grain and join their bases; filed seals identify this student's clue references and verdict. No shared engine, topic, score or network request was added.

The source check independently confirmed the Senate arithmetic, Turner quotes and report pages, Indian Removal Act title/date, Homestead terms, Mississippi barriers, Jamestown date, Chicago human cost and resolution year, and AIC attribution/date/public-domain status. Current evidence is in `facts-live.md` and `museum-source.json` in Scratch.

## Review verification and remaining tooling gap

The cold review completed one full audit, `review-audit/audit.md`, with 36 mechanical leads, then only targeted rechecks. Confirmed faults were compact clue/title overlap, hidden writing inputs, unnamed reason fields, the clipped Frontier effect, hidden comparison actions and a moving Sound header. Layout repairs keep all guided frames visible at seven STANDARDS sizes and in a real 375-pixel iframe. The fixed Sound width no longer shifts adjacent controls. The filed badge is contained in its action button and was checked after its animation settled.

Rotated folder bounding boxes and native modal background occlusion were false positives, confirmed on frames. The full audit could not attach to the 375 iframe context; it did not pass that size. Separate hosted drive checks accessed the actual child document, exercised real taps and captured its claim, evidence, four-frame writing and filed screens. A shared audit_tool.py context fallback may be useful later; it was not changed here. Motion off, repeat clicks and resize stress completed without runtime faults.

All 4,096 possible scales matched an independent rules calculation. Cheap one-letter, word-soup, punctuated-soup, contradictory-chip, stale-reason and seal-reuse attempts were rerun after their repairs. Pair positions now vary; each pair retains its first response across drawer re-entry, preventing wrong-then-right praise farming. Guided annotation retries and reasoning chips remain specified scaffolding, not independent mastery evidence.

The final default Some help, Sound-on main path used held clicks at two-second gaps and filed. Short once-only effect, tray, wording and Write it cues preserve the next action when longer how-to lines are interrupted by fast progress. The final runtime fixed-line inventory exactly matches all 95 manifest lines. Browser speech remains the fallback; no recordings were made or listening-reviewed. All started browser/server processes were closed. Evidence and source checks remain in Scratch.

## Sensitivity

Unresolved specification faults: Chicago's “did not start” and “not true,” with a keyed Convincing verdict, are stronger than the museum's uncertain finding. F4's “before any state did” overlooks property-qualified women voters in New Jersey before 1807. CODEX-REVIEW.md directs the reviewer to leave faulty specification changes open. These need specification resolution before release; the review does not declare historical accuracy passed. No outside contact or approval was requested during this unattended session.

A cultural reviewer should examine Turner's “free land” framing, continuing Native sovereignty, whose voting rights count as democracy, colonial exclusions, and anti-Irish/anti-Catholic scapegoating in the cow legend. No people illustrations were introduced; the survey-object cover avoids depicting Native homelands as empty.

## Builder record, superseded by the cold review above

Build only. No commits or polish round. Read spec.md and codex-report.md before changing this tool.

## Structure

src.html starts from the kit starter. It uses the kit frame, tone, Motion, Sound, Read and Curio.voice. Responsive CSS redraws the archive layout at real viewport size, with no fixed-scene scaling. The lower panel precedes the work area in DOM order. case-data.json is loaded by a json token and holds all eighteen clues, keys and reasons. Art uses only art tokens. The four new paintings were made separately with built-in imagegen, copied to art/raw and processed only with art.py --rekey.

Each case owns its scale, identified spans, stamp, wording, frame fields, free paragraph and filed state. Local storage is wrapped in try/catch. Changes to evidence invalidate an incompatible stamp or wording and remove the filed seal. Check my scale never changes evidence placements. allowed() is the source of stamp rules; canWord() uses those rules for causal strength. Controls remain live during speech and the short stamp animation.

The four steps are opened in order through real UI gates. __tool exposes the state, data and pure validation functions for reviewers. Tests may prepare states directly, but audit-states.json reaches its states through clicks. Compact previews offer complete selected-clue text in a detail strip; phones use the specified sideways clue strip and four tray buttons. Long writing and key explanations scroll inside their sheets.

## Open questions and specification tensions

- The only listed open question refers to the group's home-language question in then-what-happened. That question asks about sourced, reviewed glossaries and says these need translators or reviewed bilingual dictionaries. No glossary is specified here, and no unreviewed translations were added. All three help levels use English frames.
- Kept the Chicago claim and keyed Convincing result exactly as specified. The cited museum source says a cow origin is possible and definitive knowledge is unlikely. “Did not start” and “not true” therefore overstate what those sources establish. The fresh cold review should settle this before release.
- Chicago's specified cause and effect concern the spread of the cow story, while the first sentence denies the cow as the fire's cause. Cause taps accept “a newspaper” and effect taps accept “cow story”; the connection explicitly names people believing the story. This mismatch is inherent in the spec's combined claim.
- “Because of” and “as a result” express causal relations but do not have a fixed strength relative to each other. They occupy the middle of the requested strip; the weakest and strongest ends are explicit.
- A scale may have no supporting or complicating clues, or all six supporting clues. Conditional writing frames follow the student's actual trays. If no undeciding clue exists, the counter-point asks for a limitation of a second clue without silently moving that clue.
- The exact Indian Removal Act title and Turner's 1893 page range were not independently confirmed from the original printed scans. Turner's democracy sentence was confirmed in a transcription linked to printed page images. The Tribune clearing article was unavailable; the Census account corroborates 1997.
- T6 is the specification's summary wording, not a verbatim Senate quotation. Its meaning was confirmed in the report's Recommendations, AmInqRep10.php, which calls for capacity for every passenger and crew member.
- BASELINE rule 5 requires a fresh accuracy and sensitivity review of the Native and hard-history content before release. This build did not run that later cold review.

## Engine changes wanted

None. No kit, scripts, docs, other tool sources or git state were changed. Reference tools were bundled into Scratch copies to honor the write boundary.

## Follow-up

Browser speech is the fallback; no narration was recorded, as required for this build. The intended smooth-narrator / Algieba timbre needs later recordings. Fixed prompts, dynamic reads and all known case lines are listed in voice/lines.json. No people remain to paint.

The one full audit stopped after 42 frames, at the filed-state test, because the builder manifest used Home, which audit_tool.py does not support. No audit.md was produced, and calm/walk/resize-stress portions were not reached. The manifest now uses supported Arrow keys. Final targeted checks cover the repaired compact stamps, key explanations, paragraph validation, keyboard path and real phone taps; no second full audit was run.

The corrected filed-state sequence was then checked alone at 1366x768 using real clicks and supported Arrow keys. It filed a complete Lots of help paragraph with zero mechanical leads. This is a targeted check, not a completed full audit. The 680x425 writing action buttons were separately repaired and re-shot so File verdict remains visible. The word drawer remains a scrollable reference list on compact screens; writing fields scroll inside their sheet.
