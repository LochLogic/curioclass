# Is the Historian Right? handoff

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
