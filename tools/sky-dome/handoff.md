# Sky Dome build handoff

`src.html` holds the observatory CSS, accessible controls, Manual and independent astronomy/rendering code. `sky-data.json` holds a compact binary catalogue, spectra, flags, names, figures, cities and markers; bundle_tool inlines it and kit/curio.js. Edit source, then rebundle with CURIO_DRAFT=1.

## Data and calculations

Second-build raw sources and manifests are in `_scratch/sky-dome/data/second/`. `gather2.py`, `gather_checks2.py`, `distance_sources2.py` and `retry_wiki2.py` preserve bounded downloads. `place_check2.py` verifies city centres. For repacking after this review, run `_scratch/sky-dome/review_pack.py`, then bundle. It wraps `pack2.py` with the verified Maradi name correction before sorting cities and computing zone indexes. Do not run pack2.py alone: it restores the Natural Earth error that misnames Maradi as Niamey and selects the wrong home city for Africa/Niamey. Fourteen non-stellar HR rows are excluded. Every retained B-V and other required star field agrees across HEASARC and CDS/CfA. Thirteen unverified or conflicting city entries are omitted, leaving 1,238. The source's timezone fields provide 302 home-zone names/aliases, with direct city-name matching too. IANA was investigated but is not bundled; Natural Earth supplied the needed zone identifiers.

The star record is 18 bytes, little-endian: uint16 HR, uint32 RA times 100000, int32 DEC times 100000, int16 magnitude times 100, int16 pmRA and pmDEC times 1000, int16 B-V times 100. B-V -32768 means missing. Spectra and uncertainty/variable flags stay alongside. Keep missing measurements missing.

All 88 figures use the explicit d3-celestial BSD fallback, converted to HR paths; all 893 endpoint occurrences match Yale within 0.003 degrees. The licence text is embedded in the Manual. The IAU list validates identities; its archive was unavailable. Do not claim a new hand tracing or a separate observational validation of this conventional connectivity. The 20 lowest-magnitude HEASARC Messier rows have separate SEDS checks; magnitude differences appear as ranges. M41 centre disagreement is documented.

Fourteen distances use the specification's NASA fact-page fallback, with second-source checks in `distance-checks.json`. ESA's public catalogue page now specifies CC BY-NC 3.0 IGO; do not redistribute it under this brief. All astronomy code remains independently written; no astronomy library is bundled.

## Tricky parts

Sky coordinates have epoch-of-date precession and proper motion. Planet coordinates begin in J2000 ecliptic coordinates; they must be precessed before the horizontal transform. The Moon has topocentric parallax. Its previous conjunction is solved numerically even across a cycle boundary, rather than subtracting a mean month; the display explicitly rounds the uncertain conjunction boundary to approximately zero. Raw age remains available for numerical checks. Home clock and away solar clock use different midnight calculations. Year zero means 1 BC.

The ordinary Tab path skips the long sky-object list. Dome deliberately focuses the canvas; Tab then visits its bright objects, and J visits Messier markers. Preserve the readout-card clearance below the top telemetry and above the bottom rim at desktop, short-preview and phone breakpoints. Tall cards scroll. Catalogue variability IDs can include suspected entries, so the UI says "variability listed" rather than asserting confirmed variation. Planet magnitudes remain unmodelled and explicitly unavailable; their navigation entries precede catalogue-ranked stars.

## Engine changes wanted

None. The shared kit is unchanged. The local power labels remove decorative kit emoji after shared setting handlers run.

## Cold review changes

The first instrument gesture now queues the single hint through Curio.voice; it is no longer restricted to opening Manual. Read pauses transport and uses spoken month/time units. Keep automatic narration to that one hint. Dynamic sky readings remain browser speech, with the fixed line listed in voice/lines.json.

Numeric change handlers immediately reconcile committed values, including blank input, with the model. Year changes preserve the local civil clock and clamp leap-day dates. Home/End is specific to each wheel, with a leap-year date range. On pinch release, the remaining pointer's drag origin is rebased. The rim chooses the closest named star to the appropriate pole from the date-precessed catalogue.

Horizon events scan from one local midnight to the next, including 23/25-hour daylight-saving dates at home. Keep that interval separate from a fixed 24-hour astronomical day. The phone transport keeps Reverse visible; its primary Play/Now/Place controls remain 60 px and Reverse meets the secondary 44 px width.

Time clamps use local calendar years, including after place changes near the year endpoints. The renderer caches observer/precession bases and date-updated stellar unit vectors, and projects those vectors directly with the same refraction. The original star disks/glows and all colours remain; a slower sprite-atlas experiment was removed. The Milky Way geometry is date-cached like the stars. Equatorial grid coordinates are already in the current-date frame and must not be precessed again. Preserve the reference horizontal/project helpers and _scratch/sky-dome/review-render-parity.json when changing this fast path.

Phone dial captions reserve their own row; short-preview captions do not wrap. Deep-sky labels share collision reservations with star labels and telemetry, while every marker remains selectable. The Moon's shadow uses the local sky background and its glow scales with illuminated fraction. Duplicate city-and-country names receive coordinate suffixes without changing the source data or zone indexes.

Independent review evidence is under _scratch/sky-dome/review-*. Fresh USNO solstice and November 2026 phase responses are in data/review/. Current IAU licensing is linked in the Manual. The review report supersedes old open-verification claims only where it supplies fresh evidence. Maradi's corrected name is corroborated by Natural Earth's NAMEASCII and Wikidata Q664550; the separate Niamey record Q3674 supplies the correct home-zone city.

## Sensitivity

No cultural narratives, etymologies or illustrations of people are included. Constellation figures are explicitly a modern convention rather than universal sky boundaries. IAU proper names remain credited identifiers. A later addition of cultural stories needs its own fresh sensitivity review.

## Follow-up material

The final audit's only five mechanical leads were the required hidden first-run hint. Its frames exposed canvas-name clipping, repaired by testing each label's corners against the oval and trying the left side for stars near its edge. Focused re-shoots and glyph-corner checks cover every standard viewport. Read's singular hour/minute wording was re-walked, including Sound off. The southern audit fixture now changes the real city control so its city field and coordinates agree.

Keep `codex-report-1.md` as historical evidence. This is a second Build, with no commits, shared changes, deployment or polish round. Recorded narration and actual Chromebook performance remain separate verification needs. Cultural sky stories stay omitted as the spec advises. The fresh report names any reference services that remained unreachable.

## Refine round 1

The current merged list is refine.md and the item-by-item outcome is polish.md. No shared engine files or review
files were edited. The scientific position, phase, rise/set, precession and orbital functions are unchanged:
_scratch/sky-dome/fix-math-preserved.json records the comparison. Projection and its inverse now use one radius.

The star renderer batches display colours/opacity, caches overlay geometry and fonts, and uses sampled refraction
only in rendering. Exact horizontal() still owns all object readouts. The renderer lookup's high-altitude and
minus-one-degree discontinuities are handled exactly. Keep fix-numbers.json's angular/pixel parity checks when
changing this path. Sprite atlas, reusable transformed paths and SVG string paths were slower and were removed.
The 4x CPU target is still an explicit open gate unless polish.md supplies a passing final measurement.

Constellation areas and labels are from the specified d3-celestial BSD fallback, with the complete existing notice
retained in the Manual. Spherical polygon orientation uses signed triangle area, including concave Draco and polar
areas; the inverse precession basis puts the readout direction back in the source's J2000 frame. Raw downloads and
licence checks are in _scratch/sky-dome/data/fix/. Repack with fix_pack_data.py in Scratch. Added checked distance
facts are Rigel and Antares only; Canopus and Deneb were omitted under the item's explicit skip allowance.

The hint uses Curio.voice's wait promise: no time-control first hint, and a non-time first hint stays visible until
the line resolves or time changes. There is one fixed voice line; Read remains dynamic and works with Sound off.
The visual rate knob is a keyboard slider. Sydney's duplicate matches are ordinary keyboard buttons.

No welcome, task list, score, quiz, levels, finish or kit header was added. Source URLs, dates, licences, sampling and
limitations are recorded in the Manual, tool.draft.json and polish.md. The unresolved spec questions stay untouched.

## Refine round 2

The remaining list item is Should fix 2, night-time performance. The new star surface uses one WebGL point buffer,
with the date-precessed catalogue vectors uploaded only when their date changes. Its vertex shader applies the
existing observer rotation, average refraction and equal-angle projection. The browser composites the surface
between the drawn background and the labels, lines, bodies, ground and ring, avoiding a synchronous canvas copy.
Colours and opacity retain the existing display bins; catalogue values, sources and licences are unchanged.

The CPU still projects bright stars and every constellation endpoint each frame. A sky tap projects the full
catalogue before hit testing, so faint stars remain selectable. `draw(true)` explicitly requests those full projected
nodes for diagnostics. If WebGL is absent or its context is lost, the existing canvas batches render the full sky.
All decorative canvases are hidden from accessibility APIs and pointer input; the original sky canvas owns input.

This improves rendering but does not establish 60 fps at 4x CPU throttle. See the round 2 polish report and
`_scratch/sky-dome/r2-*-perf.json` for draw times and actual frame intervals. Keep Done when 7 open unless a final
measurement there explicitly passes it. The CPU pixel-tile experiment was slower and was removed.
