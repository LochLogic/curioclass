PASS
Counts: blockers 0, should fix 0, polish 3, nit 3

# career-cluster-explorer: Final look

Cold check on 2026-10-29 against REFINE.md (Final look), STANDARDS.md and BASELINE.md, after reading refine.md (round 1 PASS)
and handoff.md. Real assets: 9 recorded clips (local Qwen3-TTS clone, upbeat-guide bank, credit in voice/local.json). No art
files: the town is drawn in code and art/prompts.json is empty by design. The sensitivity review is a separate agent's job
and is not repeated here.

Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py career-cluster-explorer`, 330 KB. Driven with scripts/drive.py (held
clicks of 0.12 s, Sound and Motion on unless named) on ports 9201 and 9202, with the 375 host on 8811. Frames and logs are
in S:/CurioClass-codex-scratch/final/career-cluster-explorer/ (f/, v/, v2/). I looked at every frame named here. The audit
(audit_tool.py, audit/audit.md) finished late, with 25 leads; its log has one CDP connection reset, so its rows are leads
only. I confirmed the leads on my frames:
- Marker / Pan right overlaps at 800, 1280, 1366 and 760, and walk rows 39 to 44 "covered or clipped": these are markers
  clipped by the stage edge, which is the known case in handoff.md (Tricky parts). Not a finding.
- "Where?" buttons below the fold at 760x900 and 375, and trail buttons below the fold at 760x900: these are the
  stacked page scroll, with the first rows in view (f/n375-default). Refine passed this. Not a finding.
- Clusters hint out of view at 375: see nit 6.
- Pan left "nothing changed" in Trails: the view is already at its left end. Not a finding.
- Walk, five clicks and quick taps: every welcome was heard, and all rows are clean.

## 1. Frames
Default, card, sheet, trail middle, trail end, Clusters grid and ladder at 680x425, 800x500, 1000x625, 1280x720,
1366x768, 1920x1080 and 760x900 (f/default-*, card-*, sheet-*, trailmid-*, trailend-*, grid-*, ladder-*). At 375 through
the iframe host: default, card, sheet, trail end, grid, two ladders (f/n375-*), no sideways scroll (scrollWidth 375). All
14 lit at 1366 and 680 and in the grid (f/alllit-*). Motion off (f/calm-default-1366x768, f/calm-check: Curio.reduce true,
no running animations with a card open). No placeholders anywhere. No text sits over a picture: card and sheet text is on
solid panels. No clipped words and no overlaps, apart from the carried items below. Lanterns are readable at every size,
and labels are large at 1920.

## 2. Art against the spec
Nothing to check: no `art:` tokens, art/prompts.json has no assets, and the drawn town matches the spec's flat, layered
night look in every frame. There are no people pictures (the careers use emoji).

## 3. Voice with the real clips
Clip text: I ran each mp3 and raw take through Whisper base.en. All 9 say exactly their line in voice/lines.json (only
punctuation and "14" vs "fourteen" differ). In the bundle, every line text maps to its own clip (base64 matched per file).
Lengths are 2.38 to 5.36 s, and no clip is very short.

Timing (I logged each Audio play, end and pause next to `__tool.vlog`):
- v2/v1-marker-job-esc (fresh): welcomeFestival plays 1.36 to 6.08 s in full. A job tapped at about 2.9 s lights the
  lantern, and lanternHow waits for the welcome to finish. After Esc twice, lanternHow plays 8.10 to 12.40 s, then panHow
  12.93 to 17.22 s. Nothing overlaps and nothing is cut.
- v/v2-trails: welcomeTrails plays 1.35 to 5.20 s, and trailEnd4 waits for it, then plays 6.06 to 8.48 s while the end
  card shows "took 4 clusters". The line matches the screen.
- v2/v3-trailend-x5: trailEnd4 spoken 5 of 5, each clip ending in full; welcomeTrails once.
- v2/v5-alllit: 13 lit, then the first tap is the ridge's job: welcome 1.44 to 6.15 s, then allLit 6.32 to 11.75 s, in
  full and after the welcome.
- v/v6-read: Read 1.1 s into welcomeTrails pauses that clip and plays the hint (it is the same line, so its clip plays). Read
  is not cut off.
- v/v7-fast: fast taps (0.25 s) through a trail, then Festival: welcomeTrails is hushed, the queued trailEnd3 is dropped
  (hush), and welcomeFestival starts at once. No stale line plays.
- v/v8-sound-toggle: the Sound tap says nothing. Sound back on brings the skipped welcome once.

| line | kind | expected | spoken |
|---|---|---|---|
| welcomeFestival | how | 1 | 1 |
| lanternHow | how | 1 | 1 |
| panHow | how | 1 | 1 |
| welcomeTrails | how | 1 | 1 |
| trailEnd4 | event | 5 | 5 |
| allLit | event | 1 (once all 14 are lit) | 1 |
| welcomeClusters | how | 1 | 1 |

Liveliness (`scripts/voice_liveliness.py`): only line 4 is flagged: welcomeTrails, "Pick a trail, then tap Next to
follow it across the fair.", with semitone SD 2.98 against the 3.0 threshold and the narrowest range, 9.3. It is a
how-to line heard once, when Trails opens. Its rate (14.8 c/s) and its transcript are normal, and it sits on the
threshold, not clearly flat. Judged: it can stay (RUNBOOK: a flag or two is normal). See polish item 2.

## 4. Full run, solo student and teacher projecting
Solo: the first screen and its spoken welcome say what to do. Every waiting moment names its control (card, sheet,
trail, ladder hints read from the DOM in every shot). The real voice keeps up with a fast student, because lines queue
behind the welcome instead of being lost. Projected at 1920x1080: lanterns, the panel and the trail card read from a
distance. Nothing felt slow, except polish item 1.

## 5. Contract
330 KB with all 9 clips inlined (9 data:audio/mpeg URIs). No fetch or XHR in the bundle and no external src/href
resources. No console errors or exceptions in any shot (0 of about 75). No em dashes in the bundle.

## Findings

1. **polish (general)**, Clusters: welcomeClusters runs on over the opened ladder. A student who taps a cluster 1 s after
   entering still hears "Tap a cluster to see its ways in..." for about 3 s more while the ladder already shows
   (v2/v4-clusters: the clip plays 1.35 to 5.74 s, the ladder opens at about 2.4 s). The real clip (4.36 s) holds it a little
   longer than the browser read. Better: give the welcome a `valid` of `state.cluster === null`, and let openCluster cut
   the welcome if it is still playing (or hush), so the line stops once its step is done.
2. **polish (general)**, voice line 4 (welcomeTrails): it is on the liveliness threshold (2.98). It is optional and
   low priority. If Cory hears it as bored, run `localvoice.py career-cluster-explorer --redo 4 --takes 5`. Otherwise
   keep it.
3. **polish (general)**, carried from refine.md item 26: at 1366x768 the trail stop header still wraps ("BEHIND THE
   KETTLE CORN: / STOP 5 OF 5", f/trailend-1366x768). At 800x500 it is a single "STOP 5 OF 5" (f/trailend-800x500).
4. **nit (general)**: allLit plays while the career sheet still covers the lantern strip (v2/v5-alllit, sheet open at
   11.75 s). The sheet's own "lantern: lit" line is in view and the shimmer waits for the close, so it still reads.
   Same as the exit check's lanternHow nit.
5. **nit (general)**, carried: at 680x425 the Ferris wheel card's fourth job runs to the stage edge (f/card-680x425).

6. **nit (general)**: at 375 in Clusters, the hint sits below the 14-tile grid, out of view until the student scrolls
   (audit lead, f/n375-grid). The welcome speaks it, and the grid's own "Ways in" tile says the same, so it still reads.

No blockers or should-fix items. The real clips broke nothing that Refine passed.
