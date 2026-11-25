# Time Tides data pipeline

The scripts that made source/chronia-atlas.html, rescued 2026-11-24 (consolidation step 1) from the Antigravity
working folder C:\Users\Cory\.gemini\antigravity\brain\6fbd6632-042c-48d5-b34e-bfe1abcf53d4\ (its `scratch/` and the
plan file). Every file here is an untouched, hash-checked copy; the originals go to the archive in step 3.

- build_data.py: era borders from the raw GeoJSON into atlas_data.b64.
- build_bios.py: short bios, using wiki_bios_cache.json, into bios_data.b64.
- stories_data.py: the era stories and arcs.
- assemble_atlas.py: puts it all into one HTML file.
- era_summary.txt, chronia_atlas_reimagination_plan.md: notes from the build.
- raw/ (git-ignored, like art/raw): raw_geojson/ (57 files, historical-basemaps GPL-3.0 and Natural Earth), the
  Cliopatria GeoJSON zip, and the two generated .b64 data files. Backed up to X: with the rest of S:.

As built, the scripts read from and write to the old paths (`SCRATCH` and `OUT_HTML` near the top of each). To run
them again, point `SCRATCH` at a folder holding both this folder's files and raw/'s, and `OUT_HTML` at a scratch
copy, never at source/ (source/chronia-atlas.html stays the untouched original; src.html is the game with our changes).
