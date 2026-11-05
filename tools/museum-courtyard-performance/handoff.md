# Museum Courtyard Performance handoff

## Structure

src.html starts from the kit starter and includes curio, the grade 9-12 theme with the specified light palette, and dance. CSS handles Site, Week, Opening night and dialogs. The script contains the content tables, ray model, production state, canvas plan, perspective seat renderer, one show clock, synthesized score and fountain noise, and local persistence. window.__tool exposes the model, state, actions and voice log for review.

Only this tool and its Scratch folder were written. No commits, branch changes, shared-engine edits or polish round.

## Model and implementation

- Zone sampling uses the specified 9 by 9 grid clipped to the ellipse, including its boundary, giving 49 sample points. Each ground seat casts rays against all columns and, when running, the 1.5 meter spray circle. Row factors are applied per row before averaging. Kneeling uses the stated 75% overall factor. Light, spacing and column-uplight effects follow in order.
- The basin radius is absent from the spec. This build chooses 0.75 meters, explains it on screen, and keeps zone edges at least 0.8 meters from its center. Floor placement keeps clear of seats and basin; marley also keeps 1 meter from the basin edge, since the fountain always runs in rehearsal.
- The installed floor's factor uses the Rise zone center, a simplification of the landing location. Seat views are perspective geometry with painted billboards and engine figures. The model itself uses the exact specified two-dimensional rays. Painted architecture has illustrative proportions, not surveyed elevations.
- All three modes share state. Reservations immediately reduce the displayed available budget and hours; End week applies them. Undo stores one complete pre-week snapshot, including booked cards and zone positions. The next End week replaces that snapshot.
- The warm-up card affects later weeks. A new floor is available in its booking week when End week applies the load. The preview includes the default position of a newly booked floor. Move installed floors in Site; floor factors use the Rise zone center.
- Rehearsal always asks for two sections. In week 6, the first selected gets a dot in the lobby if backup is booked. Lobby load assumes sprung flooring, matching the studio-floor direction in the spec. With no backup there is no site load or dot.
- The 40-second show uses one Dance.clock at 96 BPM over 64 counts. Each section has a Dance.phrase and six Dance.dancer figures, or five in injured Rise. Stop ends clock, music and fountain source synchronously. Skip seeks to the next 16-count boundary. Motion off quantizes pose and position without changing duration.
- Dialogs keep their buttons outside the scrolling body. The phone uses horizontal action cards and a pinned End week footer. Compact Seat view replaces the plan, with a seat menu provided for keyboard access.
- Installed floors can be selected by clicking an exposed part of their square, or through Move installed floor below the primary Site buttons. That secondary selector may need panel scrolling in a short preview; it remains keyboard accessible.
- Native localStorage is wrapped in try/catch. The UI states that saving stays on this device. Sound controls score, fountain and narration. No narration recordings were made; browser speech is the fallback.

## Owner decision: painted dancers

Use painted dancers in the final tool. The current code figure is temporary, as directed. All provisional figures go through makeDancer. PAINTED_POSES holds the art tokens, and art/prompts.json lists six replacement assets with people:true: procession, floor roll, kneeling/sitting, standing Pool, weaving, and Rise landing/jump/lift. The next painter should supply coherent front and rear variants and preserve the renderer's world coordinates and depth sorting. No generated image in this build contains people.

## Open questions and source discrepancies

There is no explicit open-question list in this spec. Choices made in its direction are listed above: 0.75 meter basin, later-week warm-up, 75% kneeling factor, first-selected lobby section, sprung lobby, and center-based landing surface.

The computed Source examples differ at (10,8), which is 97.96% without spray but 83.13% with spray, and at (10,13), which is 33.54% with spray rather than 37%. The stated ray model is implemented and the spec is unchanged. Both arcade examples give 78.50%, and balcony examples give 100%, 59.18% and 26.53%, matching within two points. The extreme of six full site weeks conflicts with week 6 rain, but the two consecutive stone weeks still demonstrate the required injury.

Budget totals, weekly loads, sample production cost/hours and contrast ratios match the spec. Scratch numbers.txt and manual-sample-result.json contain independent recomputation evidence.

## Art and files

Nine non-people assets were generated with the built-in image tool, copied into art/raw, and converted only with art.py --rekey. The still fountain was redrawn once because the first version had a spray. Keyed images received despill and hole cleanup. Full prompts, model credit, pending people assets and provenance are in art/prompts.json. The bundle uses only embedded assets and makes no network requests.

## Engine changes wanted

None. The kit was used without changes. Family documentation does not yet list this tool; add it to the dance figure/pose consumers when the owner authorizes documentation updates.

## Review next

Read codex-report.md for final verification, audit dispositions and remaining limits. Inspect the camera framing, physical meaning of center-based landings and the simplified low-work visibility assumption. A human headphone check and actual browser narration timbre review remain useful because automated Chrome is muted. The requested cold review belongs to the next chat.

The held-click, two-second pace run spoke welcomeWeek once, sore five times and rain once. It dropped the queued injured line when the student opened the next week before the sore line finished. A separate normal-pace test spoke both sore and injured. This follows the requested stale-on-week-change rule, but does not satisfy an unqualified reading of every event being heard at a two-second pace. Review the priority or presentation of simultaneous sore and injury events.

## Final audit and targeted repairs

The single full audit completed in 1,421.91 seconds with 28 leads. Its runtime, Motion off, resize recovery and repeated-tap checks were clean. All 53 frames were reviewed in five contact sheets. Intentional map overlays, the specified sideways phone card list, the locked Opening night tab and the modal covering its background account for the non-actionable groups.

After the audited snapshot, repairs preserve focus through Plan week, End week, Begin and Stop; replace stale end-week instructions with a report-specific how line; move Model into the footer at every size; suppress a warning under the compact seat inset; provide direct and keyboard floor selection; reset show status after plan changes; and show two sequential lifts with camera space for the whole dancer. Targeted follow-up frames and JSON results in Scratch verify those changes. The full audit was not repeated.

At small sizes, close Seat view to edit an installed floor. This removes an irrelevant floor selector while the seat inset replaces the plan and keeps the seat menu in view. Secondary report text or an installed-floor menu may still require panel scrolling in a short preview. All primary actions stay available. The final report records remaining source-number and rapid-event narration limits.

Final bundle: 1,020,229 bytes. Nine WebP images total 324,384 bytes. Source: 1,604 lines, maximum 159 characters. The final phone seat menu fits without horizontal overflow. All started Chrome instances and host servers are closed; host.html is removed. No full audit was repeated after targeted repairs.
