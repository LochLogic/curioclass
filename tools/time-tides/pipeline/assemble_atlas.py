import json, gzip, base64
from pathlib import Path
import sys

SCRATCH = Path(r"C:\Users\Cory\.gemini\antigravity\brain\6fbd6632-042c-48d5-b34e-bfe1abcf53d4\scratch")
OUT_HTML = Path(r"s:\CurioClass-agy\chronia-atlas.html")

sys.path.insert(0, str(SCRATCH))
import stories_data

def assemble():
    map_b64 = (SCRATCH / "atlas_data.b64").read_text(encoding="utf-8").strip()
    bios_b64 = (SCRATCH / "bios_data.b64").read_text(encoding="utf-8").strip()
    stories_payload = {
        "eraStories": stories_data.ERA_STORIES,
        "storyArcs": stories_data.STORY_ARCS,
        "empireBios": stories_data.EMPIRE_BIOS
    }
    stories_json = json.dumps(stories_payload, separators=(",", ":"), ensure_ascii=False)

    html = (
        HTML_TEMPLATE
        .replace("__MAP_DATA_B64__", map_b64)
        .replace("__BIOS_DATA_B64__", bios_b64)
        .replace("__STORIES_JSON__", stories_json)
    )
    OUT_HTML.write_text(html, encoding="utf-8")
    size_bytes = OUT_HTML.stat().st_size
    print(f"Wrote {OUT_HTML}")
    print(f"Total single-file size: {size_bytes:,} bytes ({size_bytes/1024:.1f} KB / {size_bytes/(1024*1024):.2f} MB)")
    assert size_bytes < 2 * 1024 * 1024, f"Exceeded 2 MB budget: {size_bytes}"

HTML_TEMPLATE = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>Chronia — Flat Historical Atlas & Stories</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Inter:wght@400;500;600&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap" rel="stylesheet">
<style>
:root {
  --paper: #F2ECE0;
  --paper-deep: #E8DFCE;
  --ocean: #D9E2DD;
  --ink: #2C231B;
  --ink-soft: #5C4E40;
  --ink-muted: #847565;
  --accent: #9E472A;
  --accent-soft: rgba(158, 71, 42, 0.12);
  --vellum: rgba(251, 248, 241, 0.80);
  --vellum-strong: rgba(251, 248, 241, 0.92);
  --vellum-border: rgba(84, 68, 50, 0.17);
  --vellum-shadow: 0 8px 30px rgba(44, 35, 27, 0.08), 0 1px 3px rgba(44, 35, 27, 0.05);
  --radius: 14px;
  --radius-sm: 9px;
  --font-display: 'Cormorant Garamond', Georgia, 'Times New Roman', serif;
  --font-body: 'Newsreader', Georgia, serif;
  --font-ui: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

* { box-sizing: border-box; margin: 0; padding: 0; -webkit-tap-highlight-color: transparent; }
html, body {
  width: 100%; height: 100%; overflow: hidden;
  background: var(--paper);
  color: var(--ink);
  font-family: var(--font-ui);
  font-size: 13px;
  -webkit-font-smoothing: antialiased;
}

/* Subtle procedural rag-paper grain overlay */
body::after {
  content: "";
  position: fixed; inset: 0;
  pointer-events: none;
  z-index: 90;
  opacity: 0.04;
  mix-blend-mode: multiply;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}

#map-canvas {
  position: fixed; inset: 0;
  width: 100%; height: 100%;
  display: block;
  cursor: grab;
  touch-action: none;
}
#map-canvas:active { cursor: grabbing; }

/* Frosted-vellum utility surface */
.vellum {
  background: var(--vellum);
  backdrop-filter: blur(16px) saturate(1.12);
  -webkit-backdrop-filter: blur(16px) saturate(1.12);
  border: 1px solid var(--vellum-border);
  box-shadow: var(--vellum-shadow);
}

/* Top Floating Bar */
.top-bar {
  position: fixed; top: 14px; left: 16px; right: 16px;
  display: flex; align-items: center; justify-content: space-between;
  gap: 10px;
  pointer-events: none;
  z-index: 30;
}
.top-bar > * { pointer-events: auto; }

.brand-pill {
  display: flex; align-items: center; gap: 10px;
  padding: 7px 14px;
  border-radius: 999px;
}
.brand-title {
  font-family: var(--font-display);
  font-size: 19px; font-weight: 700; letter-spacing: 0.12em;
  color: var(--ink);
  line-height: 1;
}
.brand-sep { width: 1px; height: 14px; background: var(--vellum-border); }
.brand-era {
  font-family: var(--font-body); font-style: italic;
  font-size: 13px; color: var(--ink-soft);
  max-width: 210px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}

.date-pill {
  display: flex; align-items: center; gap: 2px;
  padding: 4px;
  border-radius: 999px;
}
.icon-btn {
  appearance: none; border: none; background: transparent;
  color: var(--ink-soft); cursor: pointer;
  width: 30px; height: 30px; border-radius: 999px;
  display: inline-flex; align-items: center; justify-content: center;
  transition: background 0.16s, color 0.16s, transform 0.12s;
}
.icon-btn:hover { background: rgba(44, 35, 27, 0.07); color: var(--ink); }
.icon-btn:active { transform: scale(0.94); }
.icon-btn:disabled { opacity: 0.35; cursor: default; }
.icon-btn.active { background: var(--accent-soft); color: var(--accent); }

.date-display {
  font-family: var(--font-display);
  font-size: 18px; font-weight: 700;
  color: var(--ink);
  padding: 0 12px;
  min-width: 98px; text-align: center;
  font-variant-numeric: tabular-nums;
  cursor: pointer; border-radius: 999px;
  line-height: 30px;
  transition: background 0.15s;
}
.date-display:hover { background: rgba(44, 35, 27, 0.05); }

.tools-pill {
  display: flex; align-items: center; gap: 4px;
  padding: 4px 6px;
  border-radius: 999px;
}
.pill-btn {
  appearance: none; border: none; background: transparent;
  color: var(--ink-soft); cursor: pointer;
  height: 30px; padding: 0 10px; border-radius: 999px;
  display: inline-flex; align-items: center; gap: 6px;
  font-family: var(--font-ui); font-size: 12px; font-weight: 500;
  transition: background 0.16s, color 0.16s;
}
.pill-btn:hover { background: rgba(44, 35, 27, 0.07); color: var(--ink); }
.pill-btn.active { background: var(--accent-soft); color: var(--accent); }
.kbd {
  font-size: 10px; font-weight: 600; color: var(--ink-muted);
  border: 1px solid var(--vellum-border); border-radius: 4px;
  padding: 1px 4px; background: rgba(255,255,255,0.45);
}

/* Right Docked Frosted-Vellum Inspector Drawer */
.inspector {
  position: fixed;
  top: 64px; right: 16px; bottom: 92px;
  width: 348px;
  border-radius: var(--radius);
  display: flex; flex-direction: column;
  z-index: 25;
  overflow: hidden;
  transition: transform 0.28s cubic-bezier(0.22, 1, 0.36, 1), opacity 0.22s ease;
}
.inspector.collapsed {
  transform: translateX(calc(100% + 28px));
  opacity: 0;
  pointer-events: none;
}
.inspector-tabs {
  display: flex; align-items: center; gap: 4px;
  padding: 8px 10px;
  border-bottom: 1px solid var(--vellum-border);
  background: rgba(251, 248, 241, 0.55);
  flex-shrink: 0;
}
.tab-btn {
  flex: 1; appearance: none; border: none; background: transparent;
  padding: 6px 8px; border-radius: 8px;
  font-family: var(--font-ui); font-size: 12px; font-weight: 500;
  color: var(--ink-soft); cursor: pointer;
  transition: background 0.15s, color 0.15s;
}
.tab-btn:hover { color: var(--ink); background: rgba(44,35,27,0.05); }
.tab-btn.active {
  background: rgba(255, 253, 249, 0.85);
  color: var(--ink);
  box-shadow: 0 1px 3px rgba(44,35,27,0.08);
}
.inspector-close {
  width: 28px; height: 28px; flex: 0 0 28px;
}

.inspector-body {
  flex: 1; overflow-y: auto; padding: 14px 16px 18px;
  scrollbar-width: thin;
  scrollbar-color: rgba(92,78,64,0.25) transparent;
}
.inspector-body::-webkit-scrollbar { width: 5px; }
.inspector-body::-webkit-scrollbar-thumb { background: rgba(92,78,64,0.25); border-radius: 99px; }

.section-eyebrow {
  font-size: 10px; font-weight: 600; letter-spacing: 0.1em;
  text-transform: uppercase; color: var(--ink-muted);
  margin-bottom: 6px;
}
.era-heading {
  font-family: var(--font-display); font-size: 25px; font-weight: 700;
  line-height: 1.1; color: var(--ink); margin-bottom: 8px;
}
.editorial-lead {
  font-family: var(--font-body); font-size: 14.5px; line-height: 1.55;
  color: var(--ink-soft); margin-bottom: 16px;
}

.shift-card {
  padding: 10px 12px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--vellum-border);
  background: rgba(255, 253, 248, 0.55);
  margin-bottom: 8px;
  cursor: pointer;
  transition: transform 0.14s, background 0.14s, border-color 0.14s;
}
.shift-card:hover {
  background: rgba(255, 253, 248, 0.92);
  border-color: rgba(158, 71, 42, 0.35);
  transform: translateY(-1px);
}
.shift-title {
  display: flex; align-items: flex-start; justify-content: space-between; gap: 8px;
  font-weight: 600; font-size: 12.5px; color: var(--ink); margin-bottom: 3px;
}
.shift-loc { font-size: 11px; color: var(--accent); font-weight: 500; flex-shrink: 0; white-space: nowrap; }
.shift-text {
  font-family: var(--font-body); font-size: 13px; line-height: 1.45;
  color: var(--ink-soft);
}

.powers-grid {
  display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px;
}
.power-chip {
  display: inline-flex; align-items: center; gap: 6px;
  padding: 5px 9px; border-radius: 999px;
  border: 1px solid var(--vellum-border);
  background: rgba(255,253,248,0.6);
  font-size: 11.5px; color: var(--ink); cursor: pointer;
  transition: background 0.14s, border-color 0.14s;
}
.power-chip:hover { background: #fffdf8; border-color: rgba(158,71,42,0.4); }
.swatch { width: 9px; height: 9px; border-radius: 50%; flex-shrink: 0; border: 1px solid rgba(44,35,27,0.22); }

/* Story Arc Cards & Active Reader */
.arc-card {
  padding: 12px 13px;
  border-radius: var(--radius-sm);
  border: 1px solid var(--vellum-border);
  background: rgba(255, 253, 248, 0.58);
  margin-bottom: 10px;
  cursor: pointer;
  transition: background 0.15s, border-color 0.15s, transform 0.14s;
}
.arc-card:hover {
  background: rgba(255,253,248,0.95);
  border-color: rgba(158,71,42,0.4);
  transform: translateY(-1px);
}
.arc-tag {
  display: inline-block; font-size: 10px; font-weight: 600;
  text-transform: uppercase; letter-spacing: 0.08em;
  color: var(--accent); background: var(--accent-soft);
  padding: 2px 7px; border-radius: 999px; margin-bottom: 6px;
}
.arc-title {
  font-family: var(--font-display); font-size: 19px; font-weight: 700;
  color: var(--ink); line-height: 1.15; margin-bottom: 3px;
}
.arc-sub { font-size: 11.5px; color: var(--ink-muted); }

.chapter-box {
  padding: 14px;
  border-radius: var(--radius-sm);
  border: 1px solid rgba(158,71,42,0.28);
  background: rgba(255,253,248,0.85);
}
.chapter-dots { display: flex; gap: 5px; margin: 10px 0 12px; }
.chapter-dot {
  flex: 1; height: 4px; border-radius: 99px;
  background: rgba(44,35,27,0.12); cursor: pointer;
  transition: background 0.2s;
}
.chapter-dot.done { background: rgba(158,71,42,0.45); }
.chapter-dot.active { background: var(--accent); }
.chapter-nav {
  display: flex; gap: 8px; margin-top: 14px;
}
.primary-btn {
  flex: 1; appearance: none; border: none;
  background: var(--ink); color: #FAF6EE;
  padding: 8px 12px; border-radius: 9px;
  font-family: var(--font-ui); font-size: 12px; font-weight: 500;
  cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 6px;
  transition: background 0.15s, transform 0.12s;
}
.primary-btn:hover { background: #413428; }
.primary-btn:active { transform: scale(0.98); }
.primary-btn.accent { background: var(--accent); }
.primary-btn.accent:hover { background: #853A21; }
.secondary-btn {
  appearance: none; border: 1px solid var(--vellum-border);
  background: rgba(255,253,248,0.7); color: var(--ink);
  padding: 8px 12px; border-radius: 9px;
  font-family: var(--font-ui); font-size: 12px; font-weight: 500;
  cursor: pointer; display: inline-flex; align-items: center; justify-content: center; gap: 6px;
  transition: background 0.15s;
}
.secondary-btn:hover { background: #fffdf8; }
.secondary-btn:disabled { opacity: 0.4; cursor: default; }

/* Empire Detail */
.emp-meta {
  display: grid; grid-template-columns: 1fr 1fr; gap: 8px;
  margin: 10px 0 14px;
}
.meta-box {
  padding: 8px 10px; border-radius: 8px;
  background: rgba(255,253,248,0.6);
  border: 1px solid var(--vellum-border);
}
.meta-label { font-size: 10px; text-transform: uppercase; letter-spacing: 0.08em; color: var(--ink-muted); }
.meta-val { font-size: 12.5px; font-weight: 600; color: var(--ink); margin-top: 2px; }
.spark-wrap {
  padding: 10px 12px; border-radius: 9px;
  background: rgba(255,253,248,0.6);
  border: 1px solid var(--vellum-border);
  margin-bottom: 14px;
}

/* Collapsed Legend Pill (Bottom-Left) */
.legend-wrap {
  position: fixed; left: 16px; bottom: 92px;
  z-index: 24;
  display: flex; flex-direction: column; align-items: flex-start; gap: 8px;
}
.legend-panel {
  width: 224px; padding: 12px 14px; border-radius: var(--radius);
  display: none;
}
.legend-panel.open { display: block; animation: fadeUp 0.18s ease; }
.legend-row {
  display: flex; align-items: center; gap: 9px;
  font-size: 12px; color: var(--ink-soft); margin-bottom: 7px;
}
.legend-row:last-child { margin-bottom: 0; }
.leg-line { width: 22px; height: 2px; background: #3D3226; flex-shrink: 0; }
.leg-line.dashed { background: repeating-linear-gradient(90deg, #5C4E40 0 4px, transparent 4px 7px); }
.leg-swatch { width: 16px; height: 11px; border-radius: 3px; border: 1px solid rgba(44,35,27,0.3); flex-shrink: 0; }
.leg-star { width: 14px; height: 14px; border-radius: 50%; border: 2px solid var(--accent); background: rgba(158,71,42,0.18); flex-shrink: 0; }

/* Layers Popover */
.layers-popover {
  position: fixed; top: 58px; right: 16px;
  width: 248px; padding: 12px 14px; border-radius: var(--radius);
  z-index: 40; display: none;
}
.layers-popover.open { display: block; animation: fadeDown 0.16s ease; }
.toggle-row {
  display: flex; align-items: center; justify-content: space-between;
  padding: 6px 0; font-size: 12.5px; color: var(--ink);
  cursor: pointer;
}
.toggle-row input { accent-color: var(--accent); width: 15px; height: 15px; cursor: pointer; }

/* Floating Follow Pill */
.follow-pill {
  position: fixed; left: 50%; bottom: 96px; transform: translateX(-50%);
  padding: 6px 8px 6px 14px; border-radius: 999px;
  display: none; align-items: center; gap: 10px;
  z-index: 28;
}
.follow-pill.active { display: flex; animation: fadeUp 0.2s ease; }
.follow-dot { width: 8px; height: 8px; border-radius: 50%; background: var(--accent); animation: pulse 1.4s infinite; }

/* Bottom Floating Timeline Dock */
.timeline-dock {
  position: fixed; left: 16px; right: 16px; bottom: 14px;
  height: 66px; padding: 8px 14px;
  border-radius: var(--radius);
  display: flex; align-items: center; gap: 14px;
  z-index: 30;
}
.play-controls { display: flex; align-items: center; gap: 4px; flex-shrink: 0; }
.play-btn {
  width: 36px; height: 36px; border-radius: 999px;
  border: none; background: var(--ink); color: #FAF6EE;
  display: inline-flex; align-items: center; justify-content: center;
  cursor: pointer; transition: background 0.15s, transform 0.12s;
}
.play-btn:hover { background: var(--accent); }
.play-btn:active { transform: scale(0.94); }
.speed-btn {
  appearance: none; border: 1px solid var(--vellum-border);
  background: rgba(255,253,248,0.65); color: var(--ink-soft);
  border-radius: 999px; padding: 4px 8px; font-size: 11px; font-weight: 600;
  cursor: pointer; font-variant-numeric: tabular-nums;
}
.speed-btn:hover { color: var(--ink); background: #fffdf8; }

.scrubber-wrap {
  flex: 1; position: relative; height: 48px;
  display: flex; flex-direction: column; justify-content: center;
  user-select: none; cursor: pointer;
}
.scrubber-ticks {
  display: flex; justify-content: space-between;
  font-size: 10px; color: var(--ink-muted); font-variant-numeric: tabular-nums;
  margin-top: 6px; padding: 0 2px;
}
.scrubber-track {
  position: relative; height: 18px;
  display: flex; align-items: center;
}
.scrubber-rail {
  width: 100%; height: 4px; border-radius: 99px;
  background: rgba(44, 35, 27, 0.12);
  position: relative;
}
.scrubber-fill {
  position: absolute; left: 0; top: 0; bottom: 0;
  background: linear-gradient(90deg, rgba(158,71,42,0.45), var(--accent));
  border-radius: 99px;
}
.scrubber-dots {
  position: absolute; inset: 0; pointer-events: none;
}
.scrubber-dot {
  position: absolute; top: 50%; width: 4px; height: 4px;
  border-radius: 50%; background: rgba(44,35,27,0.28);
  transform: translate(-50%, -50%);
}
.scrubber-thumb {
  position: absolute; top: 50%;
  width: 15px; height: 15px; border-radius: 50%;
  background: var(--accent);
  border: 2.5px solid #FAF6EE;
  box-shadow: 0 2px 6px rgba(44,35,27,0.28);
  transform: translate(-50%, -50%);
  pointer-events: none;
  transition: transform 0.1s;
}
.scrubber-wrap:hover .scrubber-thumb { transform: translate(-50%, -50%) scale(1.16); }
.scrubber-hover-tip {
  position: absolute; bottom: 44px;
  padding: 4px 9px; border-radius: 8px;
  font-size: 11px; font-weight: 500; white-space: nowrap;
  pointer-events: none; opacity: 0; transform: translate(-50%, 4px);
  transition: opacity 0.12s, transform 0.12s;
  background: var(--ink); color: #FAF6EE;
}
.scrubber-hover-tip.show { opacity: 1; transform: translate(-50%, 0); }

/* Map Hover Tooltip */
.map-tooltip {
  position: fixed; pointer-events: none; z-index: 50;
  padding: 5px 10px; border-radius: 9px;
  font-size: 12px; font-weight: 500; color: var(--ink);
  opacity: 0; transform: translateY(4px);
  transition: opacity 0.12s, transform 0.12s;
  white-space: nowrap;
}
.map-tooltip.show { opacity: 1; transform: translateY(0); }

/* Omnisearch Modal */
.modal-backdrop {
  position: fixed; inset: 0; z-index: 80;
  background: rgba(34, 26, 19, 0.32);
  backdrop-filter: blur(4px);
  display: none; align-items: flex-start; justify-content: center;
  padding-top: 11vh;
}
.modal-backdrop.open { display: flex; animation: fadeIn 0.15s ease; }
.search-modal {
  width: min(540px, calc(100vw - 32px));
  border-radius: 16px;
  overflow: hidden;
  background: var(--vellum-strong);
  backdrop-filter: blur(20px);
  border: 1px solid var(--vellum-border);
  box-shadow: 0 24px 64px rgba(34,26,19,0.22);
}
.search-input-row {
  display: flex; align-items: center; gap: 10px;
  padding: 12px 16px; border-bottom: 1px solid var(--vellum-border);
}
.search-input {
  flex: 1; border: none; background: transparent; outline: none;
  font-family: var(--font-ui); font-size: 14px; color: var(--ink);
}
.search-results {
  max-height: 380px; overflow-y: auto; padding: 8px;
}
.search-group-label {
  font-size: 10px; font-weight: 600; letter-spacing: 0.1em;
  text-transform: uppercase; color: var(--ink-muted);
  padding: 8px 10px 4px;
}
.search-item {
  display: flex; align-items: center; justify-content: space-between;
  padding: 8px 10px; border-radius: 9px; cursor: pointer;
  transition: background 0.12s;
}
.search-item:hover { background: rgba(158,71,42,0.09); }
.search-item-title { font-weight: 500; font-size: 13px; color: var(--ink); }
.search-item-sub { font-size: 11px; color: var(--ink-muted); }
.search-empty {
  padding: 28px 16px; text-align: center;
  color: var(--ink-muted); font-size: 13px;
}

/* Re-open Inspector Tab Button */
.drawer-reopen {
  position: fixed; top: 68px; right: 16px; z-index: 24;
  padding: 7px 12px; border-radius: 999px;
  display: none; align-items: center; gap: 6px;
  cursor: pointer; font-size: 12px; font-weight: 500; color: var(--ink);
}
.drawer-reopen.show { display: inline-flex; }

/* Loading Overlay */
#loading-veil {
  position: fixed; inset: 0; z-index: 100;
  background: var(--paper);
  display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px;
  transition: opacity 0.35s ease;
}
#loading-veil.hidden { opacity: 0; pointer-events: none; }
.load-title { font-family: var(--font-display); font-size: 28px; font-weight: 700; letter-spacing: 0.15em; }
.load-sub { font-family: var(--font-body); font-style: italic; color: var(--ink-soft); font-size: 14px; }

@keyframes fadeUp { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
@keyframes fadeDown { from { opacity: 0; transform: translateY(-6px); } to { opacity: 1; transform: translateY(0); } }
@keyframes fadeIn { from { opacity: 0; } to { opacity: 1; } }
@keyframes pulse { 0%, 100% { opacity: 1; transform: scale(1); } 50% { opacity: 0.45; transform: scale(1.35); } }

/* Mobile Responsive Bottom Sheet */
@media (max-width: 780px) {
  .brand-era, .brand-sep, .kbd, .hide-sm { display: none; }
  .top-bar { top: 10px; left: 8px; right: 8px; gap: 6px; }
  .brand-pill { padding: 6px 10px; }
  .brand-title { font-size: 14px; letter-spacing: 0.09em; }
  .date-pill { padding: 3px; }
  .date-display { font-size: 14px; min-width: 68px; padding: 0 4px; }
  .tools-pill { padding: 3px 4px; gap: 1px; }
  .pill-btn { padding: 0 7px; }
  .icon-btn { width: 28px; height: 28px; }
  #btn-reset-view { display: none; }
  .inspector {
    top: auto; left: 10px; right: 10px; bottom: 82px;
    width: auto; height: 40vh;
  }
  .inspector.collapsed { transform: translateY(calc(100% + 100px)); }
  .legend-wrap { left: 10px; bottom: 84px; transition: opacity 0.2s; }
  body:not(.drawer-closed) .legend-wrap { opacity: 0; pointer-events: none; }
  .timeline-dock { left: 10px; right: 10px; bottom: 10px; height: 64px; padding: 8px 10px; gap: 8px; }
  .drawer-reopen { top: auto; bottom: 84px; right: 10px; }
}
</style>
</head>
<body>

<div id="loading-veil">
  <div class="load-title">CHRONIA</div>
  <div class="load-sub">Unfurling 12,000 years of borders &amp; stories…</div>
</div>

<canvas id="map-canvas" aria-label="Interactive flat historical world map"></canvas>

<!-- Top Floating Bar -->
<header class="top-bar">
  <div class="brand-pill vellum">
    <span class="brand-title">CHRONIA</span>
    <span class="brand-sep"></span>
    <span class="brand-era" id="brand-era-sub">Congress of Vienna</span>
  </div>

  <div class="date-pill vellum" role="group" aria-label="Era navigation">
    <button class="icon-btn" id="btn-prev-era" title="Previous milestone (←)" aria-label="Previous milestone">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M15 18l-6-6 6-6"/></svg>
    </button>
    <div class="date-display" id="date-display" title="Click to search or jump to any era">1815 AD</div>
    <button class="icon-btn" id="btn-next-era" title="Next milestone (→)" aria-label="Next milestone">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M9 18l6-6-6-6"/></svg>
    </button>
  </div>

  <div class="tools-pill vellum">
    <button class="pill-btn" id="btn-search" title="Search empires, eras & stories (⌘K or /)">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.35-4.35"/></svg>
      <span class="hide-sm">Search</span>
      <span class="kbd">⌘K</span>
    </button>
    <button class="pill-btn" id="btn-stories-shortcut" title="Open Guided Story Arcs">
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
      <span class="hide-sm">Stories</span>
    </button>
    <button class="icon-btn" id="btn-layers" title="Map layers & palette" aria-label="Map layers">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
    </button>
    <button class="icon-btn" id="btn-reset-view" title="Reset map view (R)" aria-label="Reset map view">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/></svg>
    </button>
    <button class="icon-btn hide-sm" id="btn-export-png" title="Save map image (PNG)" aria-label="Save map PNG">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
    </button>
  </div>
</header>

<!-- Layers Popover -->
<div class="layers-popover vellum" id="layers-popover">
  <div class="section-eyebrow">Cartographic Layers</div>
  <label class="toggle-row"><span>Border-shift story pins</span><input type="checkbox" id="opt-pins" checked></label>
  <label class="toggle-row"><span>Highlight border changes</span><input type="checkbox" id="opt-diffs" checked></label>
  <label class="toggle-row"><span>Non-state peoples &amp; cultures</span><input type="checkbox" id="opt-peoples"></label>
  <label class="toggle-row"><span>Major rivers &amp; lakes</span><input type="checkbox" id="opt-water" checked></label>
  <label class="toggle-row"><span>Graticule lines</span><input type="checkbox" id="opt-grat" checked></label>
  <label class="toggle-row"><span>Color-blind safe palette</span><input type="checkbox" id="opt-cb"></label>
</div>

<!-- Re-open Inspector Button -->
<button class="drawer-reopen vellum" id="btn-reopen-drawer">
  <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="15" y1="3" x2="15" y2="21"/></svg>
  <span>Atlas Notes</span>
</button>

<!-- Unified Right Inspector Drawer -->
<aside class="inspector vellum" id="inspector" aria-label="Historical inspector">
  <div class="inspector-tabs">
    <button class="tab-btn active" data-tab="era">Era &amp; Shifts</button>
    <button class="tab-btn" data-tab="stories">Stories</button>
    <button class="tab-btn" data-tab="empire">Empire</button>
    <button class="icon-btn inspector-close" id="btn-close-drawer" title="Collapse panel" aria-label="Collapse panel">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
    </button>
  </div>
  <div class="inspector-body" id="inspector-body"></div>
</aside>

<!-- Bottom-Left Collapsed-by-Default Legend -->
<div class="legend-wrap">
  <div class="legend-panel vellum" id="legend-panel">
    <div class="section-eyebrow">Map Key</div>
    <div class="legend-row"><span class="leg-swatch" style="background:rgba(181,111,88,0.62)"></span><span>Organized empire / state</span></div>
    <div class="legend-row"><span class="leg-line"></span><span>Established border</span></div>
    <div class="legend-row"><span class="leg-line dashed"></span><span>Fluid / approximate frontier</span></div>
    <div class="legend-row"><span class="leg-swatch" style="background:rgba(158,71,42,0.22);border-color:#9E472A"></span><span>Newly shifted territory</span></div>
    <div class="legend-row"><span class="leg-star"></span><span>Border-shift story marker</span></div>
  </div>
  <button class="pill-btn vellum" id="btn-legend" style="height:32px;padding:0 12px;">
    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
    <span>Key</span>
  </button>
</div>

<!-- Follow Through Time Pill -->
<div class="follow-pill vellum" id="follow-pill">
  <span class="follow-dot"></span>
  <span id="follow-label" style="font-size:12.5px;font-weight:600;">Following Empire</span>
  <button class="pill-btn" id="btn-stop-follow" style="height:26px;background:var(--accent-soft);color:var(--accent);">Stop</button>
</div>

<!-- Bottom Timeline Dock -->
<footer class="timeline-dock vellum">
  <div class="play-controls">
    <button class="play-btn" id="btn-play" title="Play through history (Space)" aria-label="Play through history">
      <svg id="play-icon" width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><polygon points="6 4 20 12 6 20 6 4"/></svg>
    </button>
    <button class="speed-btn" id="btn-speed" title="Playback speed">1×</button>
  </div>
  <div class="scrubber-wrap" id="scrubber-wrap">
    <div class="scrubber-hover-tip" id="scrubber-tip">1815 AD</div>
    <div class="scrubber-track">
      <div class="scrubber-rail">
        <div class="scrubber-fill" id="scrubber-fill"></div>
        <div class="scrubber-dots" id="scrubber-dots"></div>
      </div>
      <div class="scrubber-thumb" id="scrubber-thumb"></div>
    </div>
    <div class="scrubber-ticks" id="scrubber-ticks"></div>
  </div>
</footer>

<!-- Floating Map Hover Tooltip -->
<div class="map-tooltip vellum" id="map-tooltip"></div>

<!-- Cross-Era Omnisearch Modal -->
<div class="modal-backdrop" id="search-modal">
  <div class="search-modal" role="dialog" aria-label="Search empires, eras, and stories">
    <div class="search-input-row">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" style="color:var(--ink-muted)"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.35-4.35"/></svg>
      <input class="search-input" id="search-input" type="text" placeholder="Search any empire, era, or story (e.g. Roman, Mongol, 1815, Silk Road)…" autocomplete="off">
      <button class="icon-btn" id="btn-close-search" aria-label="Close search">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
      </button>
    </div>
    <div class="search-results" id="search-results"></div>
  </div>
</div>

<script>
const MAP_DATA_B64 = "__MAP_DATA_B64__";
const BIOS_DATA_B64 = "__BIOS_DATA_B64__";
const STORIES = __STORIES_JSON__;

// Authentic mineral/gouache archival pigments
const ARCHIVAL_PALETTE = [
  "#C47D64", "#8FA68B", "#CFA76E", "#8B9EB0", "#B98B9A",
  "#A99B74", "#7F9B96", "#C89578", "#9B8FA8", "#B5A87A",
  "#849B7C", "#C5897C", "#7E95A6", "#B69472", "#9AA389", "#B4868E"
];
const CB_PALETTE = [
  "#56B4E9", "#E69F00", "#009E73", "#CC79A7", "#D55E00",
  "#0072B2", "#F0E442", "#88CCEE", "#44AA99", "#DDCC77",
  "#AA4499", "#999933", "#882255", "#6699CC"
];

// Natural Earth Projection (exact forward + Newton-Raphson inverse)
const DEG2RAD = Math.PI / 180;
const RAD2DEG = 180 / Math.PI;
const A0 = 0.8707, A1 = -0.131979, A2 = -0.013791, A3 = 0.003971, A4 = -0.001529;
const B0 = 1.007226, B1 = 0.015085, B2 = -0.044475, B3 = 0.028874, B4 = -0.005916;
const NE_MAX_X = 2.73539;
const NE_MAX_Y = 1.42239;

function projectNE(lonDeg, latDeg) {
  const lam = lonDeg * DEG2RAD;
  const phi = Math.max(-85, Math.min(85, latDeg)) * DEG2RAD;
  const phi2 = phi * phi, phi4 = phi2 * phi2;
  const x = lam * (A0 + phi2 * (A1 + phi2 * (A2 + phi4 * (A3 + phi2 * A4))));
  const y = phi * (B0 + phi2 * (B1 + phi4 * (B2 + phi2 * (B3 + phi2 * B4))));
  return [x, -y]; // canvas Y goes down
}

function unprojectNE(x, yCanvas) {
  const y = -yCanvas;
  let phi = y;
  for (let i = 0; i < 6; i++) {
    const p2 = phi * phi, p4 = p2 * p2;
    const f = phi * (B0 + p2 * (B1 + p4 * (B2 + p2 * (B3 + p2 * B4)))) - y;
    const df = B0 + p2 * (3 * B1 + p4 * (7 * B2 + p2 * (9 * B3 + 11 * p2 * B4)));
    phi -= f / df;
  }
  const p2 = phi * phi, p4 = p2 * p2;
  const denom = A0 + p2 * (A1 + p2 * (A2 + p4 * (A3 + p2 * A4)));
  const lam = x / denom;
  return [lam * RAD2DEG, phi * RAD2DEG];
}

// Decompress embedded gzipped Base64 JSON payload
async function decodeGzipB64(b64Str) {
  const binStr = atob(b64Str);
  const bytes = new Uint8Array(binStr.length);
  for (let i = 0; i < binStr.length; i++) bytes[i] = binStr.charCodeAt(i);
  const ds = new DecompressionStream("gzip");
  const stream = new Blob([bytes]).stream().pipeThrough(ds);
  const text = await new Response(stream).text();
  return JSON.parse(text);
}

function regionFromLonLat(lon, lat) {
  if (lon < -30) {
    if (lat > 23) return "North America";
    if (lat > 7) return "Mesoamerica & the Caribbean";
    return "South America";
  }
  if (lon < 45 && lat > 35) return lon < 15 ? "Western Europe" : "Central & Eastern Europe";
  if (lon < 52 && lat <= 35 && lat > -36) return lat > 15 ? "North Africa & the Sahel" : "Sub-Saharan Africa";
  if (lon >= 34 && lon < 62 && lat > 12 && lat <= 42) return "the Middle East & Persia";
  if (lon >= 50 && lon < 92 && lat > 34) return "Central Asia & the Eurasian Steppe";
  if (lon >= 60 && lon < 95 && lat <= 34 && lat > 5) return "South Asia";
  if (lon >= 95 && lat > 20) return "East Asia";
  if (lon >= 92 && lat <= 20 && lat > -12) return "Southeast Asia";
  if (lon >= 110 && lat <= -10) return "Australia & Oceania";
  return "Northern Eurasia";
}

// Decode delta-encoded integer ring into projected Natural Earth coords + bbox
function decodeProjected(flat, scale) {
  const pts = new Float32Array(flat.length);
  let qx = flat[0], qy = flat[1];
  let [px, py] = projectNE(qx / scale, qy / scale);
  pts[0] = px; pts[1] = py;
  let minX = px, maxX = px, minY = py, maxY = py;
  for (let i = 2; i < flat.length; i += 2) {
    qx += flat[i]; qy += flat[i + 1];
    [px, py] = projectNE(qx / scale, qy / scale);
    pts[i] = px; pts[i + 1] = py;
    if (px < minX) minX = px; if (px > maxX) maxX = px;
    if (py < minY) minY = py; if (py > maxY) maxY = py;
  }
  return { pts, minX, maxX, minY, maxY };
}

function pointInRing(x, y, pts) {
  let inside = false;
  for (let i = 0, j = pts.length - 2; i < pts.length; j = i, i += 2) {
    const xi = pts[i], yi = pts[i + 1];
    const xj = pts[j], yj = pts[j + 1];
    const intersect = ((yi > y) !== (yj > y)) && (x < (xj - xi) * (y - yi) / (yj - yi + 1e-12) + xi);
    if (intersect) inside = !inside;
  }
  return inside;
}

// Stable lineage color hash so major empires keep consistent colors across eras
function lineageKey(name) {
  const n = name.toLowerCase();
  if (n.includes("roman") || n.includes("rome") || n.includes("byzant")) return "rome";
  if (n.includes("ottoman") || n.includes("turkey")) return "ottoman";
  if (n.includes("han") || n.includes("tang") || n.includes("song") || n.includes("ming") || n.includes("qing") || n.includes("manchu") || n.includes("china") || n.includes("sui")) return "china";
  if (n.includes("russia") || n.includes("muscov") || n.includes("ussr")) return "russia";
  if (n.includes("persia") || n.includes("achaemenid") || n.includes("sasanian") || n.includes("parthian") || n.includes("safavid") || n.includes("iran")) return "persia";
  if (n.includes("mongol") || n.includes("khanate") || n.includes("golden horde") || n.includes("ilkhanate")) return "mongol";
  if (n.includes("united states")) return "usa";
  if (n.includes("british") || n.includes("united kingdom") || n.includes("england")) return "britain";
  if (n.includes("france") || n.includes("french") || n.includes("frankish")) return "france";
  if (n.includes("spain") || n.includes("spanish") || n.includes("new spain") || n.includes("peru") || n.includes("castile")) return "spain";
  if (n.includes("mughal") || n.includes("maurya") || n.includes("gupta") || n.includes("india")) return "india";
  if (n.includes("umayyad") || n.includes("abbasid") || n.includes("fatimid") || n.includes("arab")) return "caliphate";
  return n.replace(/\b(empire|kingdom|republic|dynasty|sultanate|caliphate|of|the)\b/g, "").trim() || n;
}

function colorForName(name, cbMode) {
  const key = lineageKey(name);
  let h = 2166136261;
  for (let i = 0; i < key.length; i++) {
    h ^= key.charCodeAt(i);
    h = Math.imul(h, 16777619);
  }
  const pal = cbMode ? CB_PALETTE : ARCHIVAL_PALETTE;
  return pal[Math.abs(h) % pal.length];
}

// Application State
const state = {
  data: null,
  bios: {}, // name -> persistent historical overview
  land: [], lakes: [], rivers: [],
  eraCache: new Map(),
  entityIndex: new Map(), // nameId -> [{eraIdx, year, area, cx, cy}]
  eraIdx: 0,
  prevEraIdx: 0,
  playPos: 0, // continuous floating-point timeline position [0 .. eras.length-1]
  trans: { fromIdx: 0, toIdx: 0, start: 0, duration: 620 },
  labelAlpha: new Map(), // nameId -> smoothed screen opacity [0..1]
  labelPos: new Map(),   // nameId -> {x, y} smoothed world label position
  diffHighlightUntil: 0,
  diffNameIds: new Set(),
  lastFrameTime: 0,
  // Camera in Natural Earth projected space
  cam: { x: 0.25, y: -0.25, zoom: 1.15 },
  targetCam: { x: 0.25, y: -0.25, zoom: 1.15 },
  vel: { x: 0, y: 0 },
  dragging: false,
  dragMoved: false,
  lastPtr: { x: 0, y: 0 },
  hoverEnt: null,
  selectedNameId: null,
  activeTab: "era",
  activeArc: null,
  arcChapter: 0,
  pulsePin: null, // {x, y, until}
  playing: false,
  playSpeed: 1,
  playTimer: 0,
  following: null, // {nameId, eraIndices, pos}
  opts: {
    pins: true, diffs: true, peoples: false, water: true, grat: true, cb: false
  }
};

const canvas = document.getElementById("map-canvas");
const ctx = canvas.getContext("2d");
// Offscreen canvases for artifact-free, flicker-free era cross-dissolves
const offA = document.createElement("canvas");
const offActx = offA.getContext("2d");
const offB = document.createElement("canvas");
const offBctx = offB.getContext("2d");
let W = 0, H = 0, DPR = 1, BASE_SCALE = 1;

function resize() {
  DPR = Math.min(window.devicePixelRatio || 1, 2);
  W = window.innerWidth;
  H = window.innerHeight;
  const cw = Math.round(W * DPR), ch = Math.round(H * DPR);
  canvas.width = cw; canvas.height = ch;
  offA.width = cw; offA.height = ch;
  offB.width = cw; offB.height = ch;
  // Fit Natural Earth sheet comfortably inside viewport
  const padX = W > 900 ? 40 : 16;
  const padY = 140;
  BASE_SCALE = Math.min((W - padX * 2) / (NE_MAX_X * 2), (H - padY) / (NE_MAX_Y * 2));
}

function getViewportCenter() {
  const drawerOpen = !document.getElementById("inspector").classList.contains("collapsed");
  const cx = W * 0.5 - (W > 900 && drawerOpen ? 155 : 0);
  const cy = (W <= 780 && drawerOpen) ? H * 0.29 : H * 0.49;
  return [cx, cy];
}

function worldToScreen(wx, wy) {
  const s = BASE_SCALE * state.cam.zoom;
  const [cx, cy] = getViewportCenter();
  return [cx + (wx - state.cam.x) * s, cy + (wy - state.cam.y) * s];
}

function screenToWorld(sx, sy) {
  const s = BASE_SCALE * state.cam.zoom;
  const [cx, cy] = getViewportCenter();
  return [(sx - cx) / s + state.cam.x, (sy - cy) / s + state.cam.y];
}

function getEraDecoded(idx) {
  if (state.eraCache.has(idx)) return state.eraCache.get(idx);
  const rawEra = state.data.eras[idx];
  const scale = state.data.scale;
  const ents = rawEra.e.map(tuple => {
    const [nameId, subjId, isNS, bp, cx10, cy10, area10, ringsRaw] = tuple;
    const rings = [];
    let minX = 1e9, maxX = -1e9, minY = 1e9, maxY = -1e9;
    for (const r of ringsRaw) {
      const dec = decodeProjected(r, scale);
      rings.push(dec);
      if (dec.minX < minX) minX = dec.minX;
      if (dec.maxX > maxX) maxX = dec.maxX;
      if (dec.minY < minY) minY = dec.minY;
      if (dec.maxY > maxY) maxY = dec.maxY;
    }
    const [lx, ly] = projectNE(cx10 / 10, cy10 / 10);
    return {
      nameId, subjId,
      name: state.data.names[nameId],
      subj: subjId >= 0 ? state.data.names[subjId] : "",
      isNS: isNS === 1,
      bp, lx, ly,
      lon: cx10 / 10, lat: cy10 / 10,
      area: area10 / 10,
      rings, minX, maxX, minY, maxY
    };
  });
  const obj = { y: rawEra.y, l: rawEra.l, s: rawEra.s, ents };
  state.eraCache.set(idx, obj);
  return obj;
}

function computeDiffs(oldIdx, newIdx) {
  state.diffNameIds.clear();
  if (oldIdx === newIdx) return;
  const prevEra = getEraDecoded(oldIdx);
  const nextEra = getEraDecoded(newIdx);
  const prevAreas = new Map();
  for (const e of prevEra.ents) if (!e.isNS) prevAreas.set(e.nameId, e.area);
  for (const e of nextEra.ents) {
    if (e.isNS) continue;
    const oldA = prevAreas.get(e.nameId);
    if (oldA === undefined || e.area > oldA * 1.28) {
      state.diffNameIds.add(e.nameId);
    }
  }
  state.diffHighlightUntil = performance.now() + 2000;
}

function formatYear(y) {
  const r = Math.round(y);
  if (r < 0) return `${Math.abs(r)} BC`;
  if (r === 0) return "1 BC";
  return `${r} AD`;
}

function setEra(idx, opts = {}) {
  idx = Math.max(0, Math.min(state.data.eras.length - 1, idx));
  const prev = state.eraIdx;
  if (!opts.keepPlayPos) state.playPos = idx;
  if (prev !== idx && !opts.instant) {
    state.trans = {
      fromIdx: prev,
      toIdx: idx,
      start: performance.now(),
      duration: opts.fast ? 220 : 620
    };
  } else if (opts.instant) {
    state.trans = { fromIdx: idx, toIdx: idx, start: 0, duration: 1 };
  }
  state.prevEraIdx = prev;
  state.eraIdx = idx;
  if (!opts.noDiff && !state.playing) computeDiffs(prev, idx);

  const era = getEraDecoded(idx);
  // Pre-decode adjacent eras asynchronously so playback never stutters on decode
  if (idx + 1 < state.data.eras.length && !state.eraCache.has(idx + 1)) {
    setTimeout(() => getEraDecoded(idx + 1), 16);
  }
  if (!opts.skipDateText) {
    document.getElementById("date-display").textContent = era.l;
  }
  document.getElementById("brand-era-sub").textContent = era.s;
  document.getElementById("btn-prev-era").disabled = idx === 0;
  document.getElementById("btn-next-era").disabled = idx === state.data.eras.length - 1;
  if (!opts.keepPlayPos) updateScrubberUI(idx);
  // Defer DOM inspector rebuild off the animation frame to prevent micro-stutter
  if (opts.deferInspector) {
    setTimeout(renderInspector, 0);
  } else {
    renderInspector();
  }
}

function easeInOutCubic(t) {
  return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
}

function flyTo(lon, lat, zoom) {
  const [wx, wy] = projectNE(lon, lat);
  state.targetCam.x = wx;
  state.targetCam.y = wy;
  if (zoom !== undefined) state.targetCam.zoom = Math.max(0.85, Math.min(11, zoom));
  state.vel.x = 0; state.vel.y = 0;
}

function pulseAt(lon, lat) {
  const [wx, wy] = projectNE(lon, lat);
  state.pulsePin = { x: wx, y: wy, until: performance.now() + 2600 };
}

// Build Natural Earth outer boundary path for ocean clipping & engraved frame
let neBoundaryPts = null;
function buildNEBoundary() {
  const pts = [];
  for (let lat = -85; lat <= 85; lat += 5) pts.push(projectNE(-180, lat));
  for (let lon = -180; lon <= 180; lon += 10) pts.push(projectNE(lon, 85));
  for (let lat = 85; lat >= -85; lat -= 5) pts.push(projectNE(180, lat));
  for (let lon = 180; lon >= -180; lon -= 10) pts.push(projectNE(lon, -85));
  neBoundaryPts = pts;
}

function tracePolyOn(g, pts) {
  g.moveTo(pts[0], pts[1]);
  for (let i = 2; i < pts.length; i += 2) g.lineTo(pts[i], pts[i + 1]);
  g.closePath();
}

// Render one complete era's land + empires + water onto a target 2D context at full crispness
function renderEraToContext(g, targetEra, s, cx, cy, arcFocus, diffAlpha, isPrimary) {
  g.save();
  g.setTransform(DPR, 0, 0, DPR, 0, 0);
  g.clearRect(0, 0, W, H);
  g.translate(cx - state.cam.x * s, cy - state.cam.y * s);
  g.scale(s, s);

  // Ocean sheet clip
  g.beginPath();
  g.moveTo(neBoundaryPts[0][0], neBoundaryPts[0][1]);
  for (let i = 1; i < neBoundaryPts.length; i++) g.lineTo(neBoundaryPts[i][0], neBoundaryPts[i][1]);
  g.closePath();
  g.fillStyle = "#D9E2DD";
  g.fill();
  g.clip();

  // Graticule
  if (state.opts.grat) {
    g.beginPath();
    for (let lon = -150; lon <= 150; lon += 30) {
      for (let lat = -85; lat <= 85; lat += 5) {
        const [gx, gy] = projectNE(lon, lat);
        if (lat === -85) g.moveTo(gx, gy); else g.lineTo(gx, gy);
      }
    }
    for (let lat = -60; lat <= 60; lat += 30) {
      for (let lon = -180; lon <= 180; lon += 10) {
        const [gx, gy] = projectNE(lon, lat);
        if (lon === -180) g.moveTo(gx, gy); else g.lineTo(gx, gy);
      }
    }
    g.strokeStyle = "rgba(74, 86, 82, 0.14)";
    g.lineWidth = 0.7 / s;
    g.stroke();
  }

  // Opaque Natural Earth 50m Landmass Base (prevents any bleed/dip during cross-dissolve)
  g.beginPath();
  for (const r of state.land) tracePolyOn(g, r.pts);
  g.fillStyle = "#ECE4D3";
  g.fill();
  g.strokeStyle = "rgba(68, 56, 42, 0.28)";
  g.lineWidth = 0.9 / s;
  g.stroke();

  // Historical Empires & States
  for (const ent of targetEra.ents) {
    if (ent.isNS && !state.opts.peoples) continue;
    const isSelected = state.selectedNameId === ent.nameId;
    const isHovered = isPrimary && state.hoverEnt && state.hoverEnt.nameId === ent.nameId;
    const isArcFocused = arcFocus && arcFocus.has(ent.name.toLowerCase());
    const isDimmed = arcFocus && !isArcFocused && !isSelected;

    g.beginPath();
    for (const r of ent.rings) tracePolyOn(g, r.pts);

    if (ent.isNS) {
      g.fillStyle = "rgba(182, 166, 138, 0.16)";
      g.fill();
      g.strokeStyle = "rgba(104, 88, 68, 0.25)";
      g.setLineDash([2.5 / s, 2.5 / s]);
      g.lineWidth = 0.7 / s;
      g.stroke();
      g.setLineDash([]);
    } else {
      const baseHex = colorForName(ent.name, state.opts.cb);
      g.globalAlpha = isDimmed ? 0.24 : (isSelected || isHovered || isArcFocused ? 0.84 : 0.60);
      g.fillStyle = baseHex;
      g.fill();
      g.globalAlpha = 1;

      if (isPrimary && diffAlpha > 0 && state.diffNameIds.has(ent.nameId)) {
        g.fillStyle = `rgba(158, 71, 42, ${(diffAlpha * 0.20).toFixed(3)})`;
        g.fill();
      }

      if (ent.bp <= 1) g.setLineDash([3 / s, 2.5 / s]);
      const isChangedEdge = isPrimary && diffAlpha > 0 && state.diffNameIds.has(ent.nameId);
      g.strokeStyle = isSelected || isArcFocused
        ? "#9E472A"
        : (isChangedEdge ? `rgba(158, 71, 42, ${(0.55 + diffAlpha * 0.35).toFixed(3)})`
        : (isHovered ? "#2C231B" : "rgba(58, 46, 34, 0.56)"));
      g.lineWidth = (isSelected || isArcFocused ? 2.0 : isHovered ? 1.5 : (isChangedEdge ? 1.2 : 0.85)) / s;
      g.stroke();
      g.setLineDash([]);
    }
  }

  // Rivers & Lakes
  if (state.opts.water) {
    g.beginPath();
    for (const r of state.rivers) {
      g.moveTo(r.pts[0], r.pts[1]);
      for (let i = 2; i < r.pts.length; i += 2) g.lineTo(r.pts[i], r.pts[i + 1]);
    }
    g.strokeStyle = "rgba(116, 146, 148, 0.55)";
    g.lineWidth = 0.9 / s;
    g.stroke();

    g.beginPath();
    for (const r of state.lakes) tracePolyOn(g, r.pts);
    g.fillStyle = "#CFE0DD";
    g.fill();
    g.strokeStyle = "rgba(84, 110, 112, 0.45)";
    g.lineWidth = 0.65 / s;
    g.stroke();
  }

  g.restore();
}

// Main 60fps Canvas Render Loop
function draw(now) {
  requestAnimationFrame(draw);
  if (!state.data) return;

  const dt = state.lastFrameTime ? Math.min(0.05, (now - state.lastFrameTime) / 1000) : 0.016;
  state.lastFrameTime = now;

  // Smooth camera damping + inertia
  if (!state.dragging) {
    state.targetCam.x += state.vel.x;
    state.targetCam.y += state.vel.y;
    state.vel.x *= 0.89;
    state.vel.y *= 0.89;
    state.targetCam.x = Math.max(-NE_MAX_X, Math.min(NE_MAX_X, state.targetCam.x));
    state.targetCam.y = Math.max(-NE_MAX_Y, Math.min(NE_MAX_Y, state.targetCam.y));
  }
  const camLerp = state.dragging ? 0.45 : (1 - Math.exp(-9 * dt));
  state.cam.x += (state.targetCam.x - state.cam.x) * camLerp;
  state.cam.y += (state.targetCam.y - state.cam.y) * camLerp;
  state.cam.zoom += (state.targetCam.zoom - state.cam.zoom) * camLerp;

  // Continuous Playback (zero stop-and-go pauses!)
  let blendFromIdx = state.eraIdx;
  let blendToIdx = state.eraIdx;
  let blendT = 1;

  if (state.playing) {
    if (state.following) {
      const interval = 1650 / state.playSpeed;
      if (now - state.playTimer > interval) {
        state.playTimer = now;
        const f = state.following;
        f.pos++;
        if (f.pos >= f.eraIndices.length) {
          stopPlayback();
        } else {
          const nextIdx = f.eraIndices[f.pos];
          setEra(nextIdx, { deferInspector: true, noDiff: true });
          focusEntityInEra(f.nameId, nextIdx);
        }
      }
      if (state.trans.fromIdx !== state.trans.toIdx) {
        const rawT = Math.max(0, Math.min(1, (now - state.trans.start) / state.trans.duration));
        blendFromIdx = state.trans.fromIdx;
        blendToIdx = state.trans.toIdx;
        blendT = easeInOutCubic(rawT);
      }
    } else {
      // Advance continuous float playhead smoothly every single frame
      const maxIdx = state.data.eras.length - 1;
      state.playPos = Math.min(maxIdx, state.playPos + dt * 0.58 * state.playSpeed);
      const lo = Math.floor(state.playPos);
      const hi = Math.min(maxIdx, lo + 1);
      const frac = state.playPos - lo;
      blendFromIdx = lo;
      blendToIdx = hi;
      // Smoothstep curve for organic flow between milestones
      blendT = frac * frac * (3 - 2 * frac);

      // Update floating date readout & scrubber pixel-smoothly
      const yA = state.data.eras[lo].y;
      const yB = state.data.eras[hi].y;
      document.getElementById("date-display").textContent = formatYear(yA + (yB - yA) * frac);
      updateScrubberUI(state.playPos);

      // Sync active milestone metadata & pre-decode next era cleanly when crossing midpoint
      const nearest = Math.round(state.playPos);
      if (nearest !== state.eraIdx) {
        setEra(nearest, { keepPlayPos: true, noDiff: true, instant: true, skipDateText: true, deferInspector: true });
      }
      if (state.playPos >= maxIdx) {
        state.playPos = maxIdx;
        setEra(maxIdx, { noDiff: true, instant: true });
        stopPlayback();
      }
    }
  } else if (state.trans.fromIdx !== state.trans.toIdx) {
    const rawT = Math.max(0, Math.min(1, (now - state.trans.start) / state.trans.duration));
    blendFromIdx = state.trans.fromIdx;
    blendToIdx = state.trans.toIdx;
    blendT = easeInOutCubic(rawT);
  }

  const isBlending = blendFromIdx !== blendToIdx && blendT > 0.002 && blendT < 0.998;
  const eraA = getEraDecoded(blendFromIdx);
  const eraB = getEraDecoded(blendToIdx);
  const activeEra = blendT >= 0.5 ? eraB : eraA;

  const s = BASE_SCALE * state.cam.zoom;
  const [cx, cy] = getViewportCenter();
  const arcFocus = state.activeArc ? new Set(state.activeArc.chapters[state.arcChapter].focus.map(x => x.toLowerCase())) : null;
  const diffAlpha = (!state.playing && state.opts.diffs && now < state.diffHighlightUntil)
    ? Math.max(0, (state.diffHighlightUntil - now) / 1800) : 0;

  ctx.save();
  ctx.setTransform(DPR, 0, 0, DPR, 0, 0);

  // 1. Archival Rag-Paper Background
  ctx.fillStyle = "#F2ECE0";
  ctx.fillRect(0, 0, W, H);

  // 2. Artifact-Free Offscreen Cross-Dissolve Compositing
  if (isBlending) {
    renderEraToContext(offActx, eraA, s, cx, cy, arcFocus, 0, false);
    renderEraToContext(offBctx, eraB, s, cx, cy, arcFocus, diffAlpha, true);
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.globalAlpha = 1;
    ctx.drawImage(offA, 0, 0);
    ctx.globalAlpha = blendT;
    ctx.drawImage(offB, 0, 0);
    ctx.globalAlpha = 1;
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  } else {
    const soloEra = blendT >= 0.5 ? eraB : eraA;
    renderEraToContext(offActx, soloEra, s, cx, cy, arcFocus, diffAlpha, true);
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.drawImage(offA, 0, 0);
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  }

  // 3. Engraved Antique Sheet Frame
  ctx.save();
  ctx.translate(cx - state.cam.x * s, cy - state.cam.y * s);
  ctx.scale(s, s);
  ctx.beginPath();
  ctx.moveTo(neBoundaryPts[0][0], neBoundaryPts[0][1]);
  for (let i = 1; i < neBoundaryPts.length; i++) ctx.lineTo(neBoundaryPts[i][0], neBoundaryPts[i][1]);
  ctx.closePath();
  ctx.strokeStyle = "rgba(76, 61, 44, 0.42)";
  ctx.lineWidth = 1.4 / s;
  ctx.stroke();
  ctx.restore();

  // 4. Flicker-Free Labels with Smooth Opacity Hysteresis & Gliding Centroids
  const placedBoxes = [];
  const labelMargin = 6;
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";

  const visibleNow = new Set();
  const labelTargets = new Map();

  for (const ent of activeEra.ents) {
    if (ent.isNS && !state.opts.peoples) continue;
    const minArea = ent.isNS ? 18 / (state.cam.zoom * state.cam.zoom) : 6.5 / (state.cam.zoom * state.cam.zoom);
    const isSel = state.selectedNameId === ent.nameId;
    const isArcF = arcFocus && arcFocus.has(ent.name.toLowerCase());
    if (!isSel && !isArcF && ent.area < minArea) continue;

    // Smoothly glide label world position so centroids never jump
    let pos = state.labelPos.get(ent.nameId);
    if (!pos) {
      pos = { x: ent.lx, y: ent.ly };
      state.labelPos.set(ent.nameId, pos);
    } else {
      const posEase = 1 - Math.exp(-8 * dt);
      pos.x += (ent.lx - pos.x) * posEase;
      pos.y += (ent.ly - pos.y) * posEase;
    }

    const [sx, sy] = worldToScreen(pos.x, pos.y);
    if (sx < -60 || sx > W + 60 || sy < 40 || sy > H - 70) continue;

    const size = ent.isNS
      ? Math.max(9.5, Math.min(12, 9.5 + Math.log10(ent.area + 1) * 1.1))
      : Math.max(10.5, Math.min(16.5, 9.5 + Math.log10(ent.area + 1) * 2.1 + (state.cam.zoom - 1) * 0.6));
    const displayLabel = ent.isNS ? ent.name : (ent.area > 35 ? ent.name.toUpperCase() : ent.name);

    ctx.font = ent.isNS
      ? `italic 500 ${size.toFixed(1)}px 'Cormorant Garamond', Georgia, serif`
      : `600 ${size.toFixed(1)}px 'Cormorant Garamond', Georgia, serif`;

    const tw = ctx.measureText(displayLabel).width;
    const bx1 = sx - tw / 2 - labelMargin, bx2 = sx + tw / 2 + labelMargin;
    const by1 = sy - size / 2 - 3, by2 = sy + size / 2 + 3;

    let collides = false;
    if (!isSel && !isArcF) {
      for (const b of placedBoxes) {
        if (bx1 < b[2] && bx2 > b[0] && by1 < b[3] && by2 > b[1]) { collides = true; break; }
      }
    }
    if (collides) continue;
    placedBoxes.push([bx1, by1, bx2, by2]);
    visibleNow.add(ent.nameId);
    labelTargets.set(ent.nameId, { ent, sx, sy, size, displayLabel, isSel, isArcF });
  }

  // Smoothly ease alpha for all visible & fading-out labels (eliminates pop/twitch!)
  const alphaSpeed = 1 - Math.exp(-7.5 * dt);
  for (const [nid, info] of labelTargets) {
    const cur = state.labelAlpha.get(nid) || 0;
    const next = cur + (1 - cur) * alphaSpeed;
    state.labelAlpha.set(nid, next);
    if (next < 0.02) continue;

    ctx.font = info.ent.isNS
      ? `italic 500 ${info.size.toFixed(1)}px 'Cormorant Garamond', Georgia, serif`
      : `600 ${info.size.toFixed(1)}px 'Cormorant Garamond', Georgia, serif`;
    ctx.globalAlpha = next;
    ctx.lineWidth = 3.2;
    ctx.strokeStyle = "rgba(242, 236, 224, 0.86)";
    ctx.strokeText(info.displayLabel, info.sx, info.sy);
    ctx.fillStyle = info.isSel || info.isArcF ? "#8A361B" : (info.ent.isNS ? "rgba(92, 78, 64, 0.72)" : "#2C231B");
    ctx.fillText(info.displayLabel, info.sx, info.sy);
  }
  // Fade out departed labels smoothly and prune once invisible
  for (const [nid, cur] of state.labelAlpha) {
    if (visibleNow.has(nid)) continue;
    const next = cur * (1 - alphaSpeed);
    if (next < 0.02) {
      state.labelAlpha.delete(nid);
      state.labelPos.delete(nid);
    } else {
      state.labelAlpha.set(nid, next);
      const pos = state.labelPos.get(nid);
      if (pos) {
        const [sx, sy] = worldToScreen(pos.x, pos.y);
        if (sx >= -60 && sx <= W + 60 && sy >= 40 && sy <= H - 70) {
          const nm = state.data.names[nid];
          ctx.font = `600 12.5px 'Cormorant Garamond', Georgia, serif`;
          ctx.globalAlpha = next;
          ctx.lineWidth = 3;
          ctx.strokeStyle = "rgba(242, 236, 224, 0.82)";
          ctx.strokeText(nm, sx, sy);
          ctx.fillStyle = "#2C231B";
          ctx.fillText(nm, sx, sy);
        }
      }
    }
  }
  ctx.globalAlpha = 1;

  // 5. Interactive Border-Shift Story Pins (hidden gently during fast continuous playback to keep map calm)
  if (state.opts.pins && !state.playing) {
    const story = STORIES.eraStories[activeEra.y];
    if (story && story.shifts) {
      for (const sh of story.shifts) {
        const [wx, wy] = projectNE(sh.lon, sh.lat);
        const [sx, sy] = worldToScreen(wx, wy);
        if (sx < 10 || sx > W - 10 || sy < 50 || sy > H - 80) continue;

        ctx.beginPath();
        ctx.arc(sx, sy, 6.5, 0, Math.PI * 2);
        ctx.fillStyle = "rgba(251, 248, 241, 0.9)";
        ctx.fill();
        ctx.lineWidth = 2;
        ctx.strokeStyle = "#9E472A";
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(sx, sy, 2.3, 0, Math.PI * 2);
        ctx.fillStyle = "#9E472A";
        ctx.fill();
      }
    }
  }

  // 6. Animated Pulse Ring (when flying to a border shift)
  if (state.pulsePin && now < state.pulsePin.until) {
    const [sx, sy] = worldToScreen(state.pulsePin.x, state.pulsePin.y);
    const t = 1 - (state.pulsePin.until - now) / 2600;
    const r = 10 + (t * 2.5 % 1) * 34;
    const a = (1 - (t * 2.5 % 1)) * 0.75;
    ctx.beginPath();
    ctx.arc(sx, sy, r, 0, Math.PI * 2);
    ctx.strokeStyle = `rgba(158, 71, 42, ${a.toFixed(3)})`;
    ctx.lineWidth = 2;
    ctx.stroke();
  }

  ctx.restore();
}

// Hit-test world coordinates against active era polygons
function hitTestEntity(sx, sy) {
  if (!state.data) return null;
  const [wx, wy] = screenToWorld(sx, sy);
  const era = getEraDecoded(state.eraIdx);
  // Check smaller organized states first so enclaves/vassals are clickable over giants
  for (let i = era.ents.length - 1; i >= 0; i--) {
    const ent = era.ents[i];
    if (ent.isNS && !state.opts.peoples) continue;
    if (wx < ent.minX || wx > ent.maxX || wy < ent.minY || wy > ent.maxY) continue;
    for (const r of ent.rings) {
      if (wx < r.minX || wx > r.maxX || wy < r.minY || wy > r.maxY) continue;
      if (pointInRing(wx, wy, r.pts)) return ent;
    }
  }
  return null;
}

function hitTestPin(sx, sy) {
  if (!state.opts.pins || !state.data) return null;
  const era = getEraDecoded(state.eraIdx);
  const story = STORIES.eraStories[era.y];
  if (!story || !story.shifts) return null;
  for (const sh of story.shifts) {
    const [wx, wy] = projectNE(sh.lon, sh.lat);
    const [px, py] = worldToScreen(wx, wy);
    if (Math.hypot(sx - px, sy - py) < 13) return sh;
  }
  return null;
}

// Pointer & Wheel Interactions
let pinchDist = 0;
canvas.addEventListener("pointerdown", e => {
  canvas.setPointerCapture(e.pointerId);
  state.dragging = true;
  state.dragMoved = false;
  state.lastPtr = { x: e.clientX, y: e.clientY };
  state.vel.x = 0; state.vel.y = 0;
});

canvas.addEventListener("pointermove", e => {
  const tip = document.getElementById("map-tooltip");
  if (state.dragging) {
    const dx = e.clientX - state.lastPtr.x;
    const dy = e.clientY - state.lastPtr.y;
    if (Math.hypot(dx, dy) > 2) state.dragMoved = true;
    const s = BASE_SCALE * state.cam.zoom;
    state.targetCam.x -= dx / s;
    state.targetCam.y -= dy / s;
    state.vel.x = -dx / s * 0.45;
    state.vel.y = -dy / s * 0.45;
    state.lastPtr = { x: e.clientX, y: e.clientY };
    tip.classList.remove("show");
    return;
  }
  const pin = hitTestPin(e.clientX, e.clientY);
  if (pin) {
    canvas.style.cursor = "pointer";
    tip.textContent = "✦ " + pin.title;
    tip.style.left = (e.clientX + 14) + "px";
    tip.style.top = (e.clientY - 12) + "px";
    tip.classList.add("show");
    state.hoverEnt = null;
    return;
  }
  const ent = hitTestEntity(e.clientX, e.clientY);
  state.hoverEnt = ent;
  if (ent) {
    canvas.style.cursor = "pointer";
    const era = getEraDecoded(state.eraIdx);
    tip.textContent = `${ent.name} · ${era.l}`;
    tip.style.left = (e.clientX + 14) + "px";
    tip.style.top = (e.clientY - 12) + "px";
    tip.classList.add("show");
  } else {
    canvas.style.cursor = "grab";
    tip.classList.remove("show");
  }
});

canvas.addEventListener("pointerup", e => {
  state.dragging = false;
  if (!state.dragMoved) {
    const pin = hitTestPin(e.clientX, e.clientY);
    if (pin) {
      flyTo(pin.lon, pin.lat, Math.max(state.cam.zoom, 2.8));
      pulseAt(pin.lon, pin.lat);
      openInspector("era");
      return;
    }
    const ent = hitTestEntity(e.clientX, e.clientY);
    if (ent) {
      selectEntity(ent.nameId);
    }
  }
});

canvas.addEventListener("wheel", e => {
  e.preventDefault();
  const factor = Math.exp(-e.deltaY * 0.0014);
  const newZoom = Math.max(0.85, Math.min(12, state.targetCam.zoom * factor));
  const [wx, wy] = screenToWorld(e.clientX, e.clientY);
  const ratio = state.targetCam.zoom / newZoom;
  state.targetCam.x = wx + (state.targetCam.x - wx) * ratio;
  state.targetCam.y = wy + (state.targetCam.y - wy) * ratio;
  state.targetCam.zoom = newZoom;
}, { passive: false });

canvas.addEventListener("dblclick", e => {
  const [wx, wy] = screenToWorld(e.clientX, e.clientY);
  const [lon, lat] = unprojectNE(wx, wy);
  flyTo(lon, lat, Math.min(10, state.targetCam.zoom * 1.8));
});

// Inspector Rendering
function openInspector(tab) {
  if (tab) state.activeTab = tab;
  document.getElementById("inspector").classList.remove("collapsed");
  document.body.classList.remove("drawer-closed");
  document.getElementById("btn-reopen-drawer").classList.remove("show");
  document.querySelectorAll(".tab-btn").forEach(b => {
    b.classList.toggle("active", b.dataset.tab === state.activeTab);
  });
  renderInspector();
}

function selectEntity(nameId) {
  state.selectedNameId = nameId;
  state.activeArc = null;
  openInspector("empire");
}

function focusEntityInEra(nameId, eraIdx) {
  const era = getEraDecoded(eraIdx);
  const ent = era.ents.find(e => e.nameId === nameId);
  if (ent) {
    const zoom = ent.area > 200 ? 1.5 : ent.area > 60 ? 2.1 : 3.0;
    flyTo(ent.lon, ent.lat, zoom);
    pulseAt(ent.lon, ent.lat);
  }
}

function buildSparklineSVG(history, currentEraIdx) {
  if (!history || history.length === 0) return "";
  const totalEras = state.data.eras.length;
  const maxArea = Math.max(...history.map(h => h.area), 1);
  const w = 280, h = 44;
  let pts = [];
  for (const item of history) {
    const x = (item.eraIdx / (totalEras - 1)) * (w - 16) + 8;
    const y = h - 8 - (item.area / maxArea) * (h - 16);
    pts.push({ x, y, eraIdx: item.eraIdx });
  }
  const pathD = pts.map((p, i) => `${i === 0 ? "M" : "L"}${p.x.toFixed(1)},${p.y.toFixed(1)}`).join(" ");
  const dots = pts.map(p => {
    const active = p.eraIdx === currentEraIdx;
    return `<circle cx="${p.x.toFixed(1)}" cy="${p.y.toFixed(1)}" r="${active ? 4.2 : 2.3}" fill="${active ? "#9E472A" : "#5C4E40"}" />`;
  }).join("");
  return `<svg width="100%" height="${h}" viewBox="0 0 ${w} ${h}">
    <line x1="8" y1="${h-8}" x2="${w-8}" y2="${h-8}" stroke="rgba(44,35,27,0.14)" stroke-width="1"/>
    <path d="${pathD}" fill="none" stroke="#9E472A" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
    ${dots}
  </svg>`;
}

function renderInspector() {
  const body = document.getElementById("inspector-body");
  const era = getEraDecoded(state.eraIdx);

  if (state.activeTab === "era") {
    const story = STORIES.eraStories[era.y] || { lead: "Explore the shifting borders of major empires and states in this historical era.", shifts: [] };
    const topPowers = era.ents.filter(e => !e.isNS).slice(0, 12);

    const shiftsHtml = (story.shifts || []).map((sh, i) => `
      <div class="shift-card" data-shift="${i}">
        <div class="shift-title">
          <span>✦ ${sh.title}</span>
          <span class="shift-loc">Fly to →</span>
        </div>
        <div class="shift-text">${sh.text}</div>
      </div>
    `).join("");

    const powersHtml = topPowers.map(p => `
      <button class="power-chip" data-ent="${p.nameId}">
        <span class="swatch" style="background:${colorForName(p.name, state.opts.cb)}"></span>
        <span>${p.name}</span>
      </button>
    `).join("");

    body.innerHTML = `
      <div class="section-eyebrow">${era.l} Milestone</div>
      <div class="era-heading">${era.s}</div>
      <div class="editorial-lead">${story.lead}</div>
      ${shiftsHtml ? `<div class="section-eyebrow">Key Border Shifts</div>${shiftsHtml}` : ""}
      <div class="section-eyebrow" style="margin-top:16px;">Major Powers on This Map</div>
      <div class="powers-grid">${powersHtml}</div>
    `;

    body.querySelectorAll(".shift-card").forEach(el => {
      el.addEventListener("click", () => {
        const sh = story.shifts[Number(el.dataset.shift)];
        flyTo(sh.lon, sh.lat, 3.0);
        pulseAt(sh.lon, sh.lat);
      });
    });
    body.querySelectorAll(".power-chip").forEach(el => {
      el.addEventListener("click", () => {
        const nid = Number(el.dataset.ent);
        selectEntity(nid);
        focusEntityInEra(nid, state.eraIdx);
      });
    });
  } else if (state.activeTab === "stories") {
    if (state.activeArc) {
      const arc = state.activeArc;
      const ch = arc.chapters[state.arcChapter];
      const dots = arc.chapters.map((_, i) =>
        `<div class="chapter-dot ${i < state.arcChapter ? "done" : ""} ${i === state.arcChapter ? "active" : ""}" data-ch="${i}"></div>`
      ).join("");
      body.innerHTML = `
        <button class="secondary-btn" id="btn-back-arcs" style="margin-bottom:12px;padding:5px 10px;font-size:11.5px;">← All Story Arcs</button>
        <div class="chapter-box">
          <span class="arc-tag">${arc.tag}</span>
          <div class="arc-title" style="font-size:22px;">${arc.title}</div>
          <div class="chapter-dots">${dots}</div>
          <div style="font-weight:600;font-size:13.5px;margin-bottom:6px;color:var(--ink);">${ch.title}</div>
          <div class="editorial-lead" style="margin-bottom:4px;">${ch.text}</div>
          <div class="chapter-nav">
            <button class="secondary-btn" id="btn-ch-prev" ${state.arcChapter === 0 ? "disabled" : ""}>← Previous</button>
            <button class="primary-btn accent" id="btn-ch-next">${state.arcChapter === arc.chapters.length - 1 ? "Finish Arc" : "Next Chapter →"}</button>
          </div>
        </div>
      `;
      document.getElementById("btn-back-arcs").onclick = () => { state.activeArc = null; renderInspector(); };
      document.getElementById("btn-ch-prev").onclick = () => launchArcChapter(arc, state.arcChapter - 1);
      document.getElementById("btn-ch-next").onclick = () => {
        if (state.arcChapter < arc.chapters.length - 1) launchArcChapter(arc, state.arcChapter + 1);
        else { state.activeArc = null; renderInspector(); }
      };
      body.querySelectorAll(".chapter-dot").forEach(d => {
        d.onclick = () => launchArcChapter(arc, Number(d.dataset.ch));
      });
    } else {
      const arcsHtml = STORIES.storyArcs.map(a => `
        <div class="arc-card" data-arc="${a.id}">
          <span class="arc-tag">${a.tag}</span>
          <div class="arc-title">${a.title}</div>
          <div class="arc-sub">${a.subtitle}</div>
        </div>
      `).join("");
      body.innerHTML = `
        <div class="section-eyebrow">Guided Spatial Narratives</div>
        <div class="editorial-lead" style="margin-bottom:12px;">Step through defining border transformations as the map glides across continents and centuries.</div>
        ${arcsHtml}
      `;
      body.querySelectorAll(".arc-card").forEach(el => {
        el.onclick = () => {
          const arc = STORIES.storyArcs.find(a => a.id === el.dataset.arc);
          if (arc) launchArcChapter(arc, 0);
        };
      });
    }
  } else if (state.activeTab === "empire") {
    if (state.selectedNameId === null) {
      body.innerHTML = `
        <div class="section-eyebrow">Inspect an Empire</div>
        <div class="editorial-lead">Click any empire or state on the map to explore its borders, historical lifespan, and story—or follow it across centuries.</div>
      `;
      return;
    }
    const name = state.data.names[state.selectedNameId];
    const hist = state.entityIndex.get(state.selectedNameId) || [];
    const curEnt = era.ents.find(e => e.nameId === state.selectedNameId);
    const bioObj = STORIES.empireBios[name];
    const firstL = hist.length ? state.data.eras[hist[0].eraIdx].l : era.l;
    const lastL = hist.length ? state.data.eras[hist[hist.length - 1].eraIdx].l : era.l;
    const spanText = firstL === lastL ? firstL : `${firstL} – ${lastL}`;

    // Persistent overview: curated -> 1,630 embedded offline bios -> smart regional/historical summary
    let bioText = state.bios[name] || (bioObj ? bioObj.bio : "");
    if (!bioText) {
      const ref = curEnt || (hist.length ? hist[0] : null);
      const reg = ref ? regionFromLonLat(ref.lon, ref.lat) : "this region";
      const kind = curEnt && curEnt.isNS ? "historical cultural region" : "historical territory";
      bioText = `${name} is a ${kind} in ${reg}, appearing across ${hist.length || 1} milestone${hist.length > 1 ? "s" : ""} in this atlas (${spanText}). Use "Follow Through Time" to trace how its borders shift across eras.`;
    }

    // Find peak era in case the user scrubbed outside this territory's active lifespan
    let peakItem = hist.length ? hist[0] : null;
    for (const h of hist) if (h.area > peakItem.area) peakItem = h;

    const isFollowingThis = state.following && state.following.nameId === state.selectedNameId;

    body.innerHTML = `
      <div style="display:flex;align-items:center;gap:8px;margin-bottom:6px;">
        <span class="swatch" style="width:12px;height:12px;background:${colorForName(name, state.opts.cb)}"></span>
        <span class="section-eyebrow" style="margin:0;">${curEnt ? (curEnt.isNS ? "Peoples & Culture" : "State / Empire") : "Historical Territory"}</span>
      </div>
      <div class="era-heading">${name}</div>
      ${curEnt && curEnt.subj ? `<div style="font-size:12px;color:var(--accent);margin-bottom:8px;">Part of ${curEnt.subj}</div>` : ""}
      ${!curEnt && peakItem ? `<div style="font-size:11.5px;color:var(--ink-muted);margin-bottom:8px;">Not present in ${era.l} · <a href="#" id="btn-jump-peak" style="color:var(--accent);text-decoration:none;font-weight:600;">Jump to ${state.data.eras[peakItem.eraIdx].l} →</a></div>` : ""}
      <div class="emp-meta">
        <div class="meta-box"><div class="meta-label">Atlas Span</div><div class="meta-val">${spanText}</div></div>
        <div class="meta-box"><div class="meta-label">${bioObj ? "Capital" : "Milestones"}</div><div class="meta-val">${bioObj ? bioObj.capital : (hist.length || 1) + " eras"}</div></div>
      </div>
      <div class="spark-wrap">
        <div class="section-eyebrow" style="margin-bottom:2px;">Territorial Footprint Across Time</div>
        ${buildSparklineSVG(hist, state.eraIdx)}
      </div>
      <div class="section-eyebrow" style="margin-bottom:4px;">Overview</div>
      <div class="editorial-lead">${bioText}</div>
      <div style="display:flex;gap:8px;">
        <button class="primary-btn accent" id="btn-follow-emp">
          ${isFollowingThis ? "■ Stop Following" : "▶ Follow Through Time"}
        </button>
        ${curEnt ? `<button class="secondary-btn" id="btn-center-emp">Center</button>` : ""}
      </div>
    `;

    document.getElementById("btn-follow-emp").onclick = () => {
      if (isFollowingThis) { stopPlayback(); return; }
      startFollowing(state.selectedNameId);
    };
    const cBtn = document.getElementById("btn-center-emp");
    if (cBtn) cBtn.onclick = () => focusEntityInEra(state.selectedNameId, state.eraIdx);
    const jBtn = document.getElementById("btn-jump-peak");
    if (jBtn && peakItem) jBtn.onclick = e => {
      e.preventDefault();
      stopPlayback();
      setEra(peakItem.eraIdx);
      focusEntityInEra(state.selectedNameId, peakItem.eraIdx);
    };
  }
}

function launchArcChapter(arc, chIdx) {
  stopPlayback();
  state.activeArc = arc;
  state.arcChapter = chIdx;
  const ch = arc.chapters[chIdx];
  const eIdx = state.data.eras.findIndex(e => e.y === ch.year);
  if (eIdx >= 0) setEra(eIdx);
  flyTo(ch.lon, ch.lat, ch.zoom);
  pulseAt(ch.lon, ch.lat);
  openInspector("stories");
}

function startFollowing(nameId) {
  const hist = state.entityIndex.get(nameId);
  if (!hist || !hist.length) return;
  state.activeArc = null;
  state.following = { nameId, eraIndices: hist.map(h => h.eraIdx), pos: 0 };
  state.playing = true;
  state.playTimer = performance.now();
  setEra(hist[0].eraIdx);
  focusEntityInEra(nameId, hist[0].eraIdx);
  document.getElementById("follow-label").textContent = `Following: ${state.data.names[nameId]}`;
  document.getElementById("follow-pill").classList.add("active");
  updatePlayButton();
}

function stopPlayback() {
  state.playing = false;
  state.following = null;
  if (state.data) {
    state.playPos = state.eraIdx;
    document.getElementById("date-display").textContent = state.data.eras[state.eraIdx].l;
    updateScrubberUI(state.eraIdx);
  }
  document.getElementById("follow-pill").classList.remove("active");
  updatePlayButton();
  renderInspector();
}

function updatePlayButton() {
  const icon = document.getElementById("play-icon");
  icon.innerHTML = state.playing
    ? `<rect x="6" y="4" width="4" height="16"/><rect x="14" y="4" width="4" height="16"/>`
    : `<polygon points="6 4 20 12 6 20 6 4"/>`;
}

// Timeline Scrubber
function initScrubber() {
  const eras = state.data.eras;
  const dots = document.getElementById("scrubber-dots");
  dots.innerHTML = eras.map((e, i) => {
    const pct = (i / (eras.length - 1)) * 100;
    return `<span class="scrubber-dot" style="left:${pct}%"></span>`;
  }).join("");

  const tickYears = [-10000, -3000, -500, 100, 800, 1279, 1500, 1815, 1945, 2010];
  const tickIndices = tickYears.map(y => eras.findIndex(e => e.y === y)).filter(i => i >= 0);
  const ticks = document.getElementById("scrubber-ticks");
  ticks.innerHTML = tickIndices.map(i => `<span>${eras[i].l}</span>`).join("");

  const wrap = document.getElementById("scrubber-wrap");
  const tip = document.getElementById("scrubber-tip");
  let scrubbing = false;

  function idxFromEvent(e) {
    const rect = wrap.getBoundingClientRect();
    const t = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
    return Math.round(t * (eras.length - 1));
  }

  wrap.addEventListener("pointerdown", e => {
    scrubbing = true;
    wrap.setPointerCapture(e.pointerId);
    stopPlayback();
    setEra(idxFromEvent(e), { fast: true });
  });
  wrap.addEventListener("pointermove", e => {
    const idx = idxFromEvent(e);
    const rect = wrap.getBoundingClientRect();
    const x = Math.max(24, Math.min(rect.width - 24, e.clientX - rect.left));
    tip.style.left = x + "px";
    tip.textContent = `${eras[idx].l} — ${eras[idx].s}`;
    tip.classList.add("show");
    if (scrubbing && idx !== state.eraIdx) setEra(idx, { fast: true });
  });
  wrap.addEventListener("pointerup", () => { scrubbing = false; });
  wrap.addEventListener("pointerleave", () => { if (!scrubbing) tip.classList.remove("show"); });
}

function updateScrubberUI(pos = state.eraIdx) {
  const pct = (pos / (state.data.eras.length - 1)) * 100;
  document.getElementById("scrubber-fill").style.width = pct + "%";
  document.getElementById("scrubber-thumb").style.left = pct + "%";
}

// Cross-Era Omnisearch
function openSearch() {
  const modal = document.getElementById("search-modal");
  modal.classList.add("open");
  const inp = document.getElementById("search-input");
  inp.value = "";
  inp.focus();
  renderSearchResults("");
}
function closeSearch() {
  document.getElementById("search-modal").classList.remove("open");
}

function renderSearchResults(q) {
  const box = document.getElementById("search-results");
  const query = q.trim().toLowerCase();
  const era = getEraDecoded(state.eraIdx);
  let html = "";

  // 1. Story Arcs
  const arcs = STORIES.storyArcs.filter(a => !query || a.title.toLowerCase().includes(query) || a.tag.toLowerCase().includes(query));
  if (arcs.length && (!query || arcs.length <= 4)) {
    html += `<div class="search-group-label">Guided Story Arcs</div>`;
    html += arcs.slice(0, 4).map(a => `
      <div class="search-item" data-jump-arc="${a.id}">
        <div><div class="search-item-title">✦ ${a.title}</div><div class="search-item-sub">${a.subtitle}</div></div>
        <span class="shift-loc">Start →</span>
      </div>
    `).join("");
  }

  // 2. Milestones / Years
  const erasMatch = state.data.eras.map((e, i) => ({ e, i }))
    .filter(({ e }) => !query ? false : (e.l.toLowerCase().includes(query) || e.s.toLowerCase().includes(query) || String(Math.abs(e.y)).includes(query)))
    .slice(0, 5);
  if (erasMatch.length) {
    html += `<div class="search-group-label">Historical Milestones</div>`;
    html += erasMatch.map(({ e, i }) => `
      <div class="search-item" data-jump-era="${i}">
        <div><div class="search-item-title">${e.l}</div><div class="search-item-sub">${e.s}</div></div>
        <span class="shift-loc">Jump →</span>
      </div>
    `).join("");
  }

  // 3. Empires (On this map vs Other eras)
  if (query) {
    const onMap = era.ents.filter(e => !e.isNS && e.name.toLowerCase().includes(query)).slice(0, 6);
    if (onMap.length) {
      html += `<div class="search-group-label">On This Map (${era.l})</div>`;
      html += onMap.map(e => `
        <div class="search-item" data-jump-ent="${e.nameId}" data-jump-era="${state.eraIdx}">
          <div style="display:flex;align-items:center;gap:8px;">
            <span class="swatch" style="background:${colorForName(e.name, state.opts.cb)}"></span>
            <div><div class="search-item-title">${e.name}</div><div class="search-item-sub">Active in ${era.l}</div></div>
          </div>
          <span class="shift-loc">Fly to →</span>
        </div>
      `).join("");
    }
    const onMapIds = new Set(onMap.map(e => e.nameId));
    const otherEras = [];
    for (let nid = 0; nid < state.data.names.length; nid++) {
      if (onMapIds.has(nid)) continue;
      const nm = state.data.names[nid];
      if (!nm.toLowerCase().includes(query)) continue;
      const hist = state.entityIndex.get(nid);
      if (!hist || !hist.length) continue;
      // Pick peak area era
      let peak = hist[0];
      for (const h of hist) if (h.area > peak.area) peak = h;
      otherEras.push({ nid, nm, peak, span: `${state.data.eras[hist[0].eraIdx].l} – ${state.data.eras[hist[hist.length - 1].eraIdx].l}` });
      if (otherEras.length >= 8) break;
    }
    if (otherEras.length) {
      html += `<div class="search-group-label">Across Other Eras</div>`;
      html += otherEras.map(o => `
        <div class="search-item" data-jump-ent="${o.nid}" data-jump-era="${o.peak.eraIdx}">
          <div style="display:flex;align-items:center;gap:8px;">
            <span class="swatch" style="background:${colorForName(o.nm, state.opts.cb)}"></span>
            <div><div class="search-item-title">${o.nm}</div><div class="search-item-sub">${o.span} · Peak at ${state.data.eras[o.peak.eraIdx].l}</div></div>
          </div>
          <span class="shift-loc">Jump →</span>
        </div>
      `).join("");
    }
  } else {
    html += `<div class="search-group-label">Popular Eras to Explore</div>`;
    [-500, 100, 1279, 1492, 1815, 1920, 1960, 2010].forEach(yr => {
      const i = state.data.eras.findIndex(x => x.y === yr);
      if (i < 0) return;
      const e = state.data.eras[i];
      html += `
        <div class="search-item" data-jump-era="${i}">
          <div><div class="search-item-title">${e.l}</div><div class="search-item-sub">${e.s}</div></div>
          <span class="shift-loc">Jump →</span>
        </div>
      `;
    });
  }

  if (!html) {
    html = `<div class="search-empty">No empires, eras, or stories matched "<strong>${q.replace(/</g, "&lt;")}</strong>".<br>Try searching <em>Roman</em>, <em>Mongol</em>, <em>Ottoman</em>, <em>1815</em>, or <em>1945</em>.</div>`;
  }
  box.innerHTML = html;

  box.querySelectorAll("[data-jump-arc]").forEach(el => {
    el.onclick = () => {
      const arc = STORIES.storyArcs.find(a => a.id === el.dataset.jumpArc);
      closeSearch();
      if (arc) launchArcChapter(arc, 0);
    };
  });
  box.querySelectorAll("[data-jump-ent]").forEach(el => {
    el.onclick = () => {
      const nid = Number(el.dataset.jumpEnt);
      const eIdx = Number(el.dataset.jumpEra);
      closeSearch();
      stopPlayback();
      setEra(eIdx);
      selectEntity(nid);
      focusEntityInEra(nid, eIdx);
    };
  });
  box.querySelectorAll("[data-jump-era]:not([data-jump-ent])").forEach(el => {
    el.onclick = () => {
      closeSearch();
      stopPlayback();
      setEra(Number(el.dataset.jumpEra));
    };
  });
}

// Wire UI Events
document.getElementById("btn-prev-era").onclick = () => { stopPlayback(); setEra(state.eraIdx - 1); };
document.getElementById("btn-next-era").onclick = () => { stopPlayback(); setEra(state.eraIdx + 1); };
document.getElementById("date-display").onclick = openSearch;
document.getElementById("btn-search").onclick = openSearch;
document.getElementById("btn-close-search").onclick = closeSearch;
document.getElementById("search-modal").onclick = e => { if (e.target.id === "search-modal") closeSearch(); };
document.getElementById("search-input").addEventListener("input", e => renderSearchResults(e.target.value));

document.getElementById("btn-stories-shortcut").onclick = () => openInspector("stories");
document.getElementById("btn-close-drawer").onclick = () => {
  document.getElementById("inspector").classList.add("collapsed");
  document.body.classList.add("drawer-closed");
  document.getElementById("btn-reopen-drawer").classList.add("show");
};
document.getElementById("btn-reopen-drawer").onclick = () => openInspector();
document.querySelectorAll(".tab-btn").forEach(b => {
  b.onclick = () => openInspector(b.dataset.tab);
});

document.getElementById("btn-legend").onclick = () => {
  document.getElementById("legend-panel").classList.toggle("open");
};

const layersPop = document.getElementById("layers-popover");
document.getElementById("btn-layers").onclick = e => {
  e.stopPropagation();
  layersPop.classList.toggle("open");
};
document.addEventListener("click", e => {
  if (!layersPop.contains(e.target) && e.target.id !== "btn-layers") layersPop.classList.remove("open");
});

["pins", "diffs", "peoples", "water", "grat", "cb"].forEach(k => {
  document.getElementById("opt-" + k).addEventListener("change", e => {
    state.opts[k] = e.target.checked;
    if (k === "cb") renderInspector();
  });
});

document.getElementById("btn-reset-view").onclick = () => {
  state.activeArc = null;
  state.targetCam = { x: 0.25, y: -0.25, zoom: 1.15 };
  state.vel = { x: 0, y: 0 };
};

document.getElementById("btn-export-png").onclick = () => {
  const era = getEraDecoded(state.eraIdx);
  const link = document.createElement("a");
  link.download = `chronia-${era.l.toLowerCase().replace(/\s+/g, "-")}.png`;
  link.href = canvas.toDataURL("image/png");
  link.click();
};

document.getElementById("btn-play").onclick = () => {
  if (state.playing) { stopPlayback(); return; }
  if (state.eraIdx >= state.data.eras.length - 1) setEra(0, { noDiff: true, instant: true });
  state.playPos = state.eraIdx;
  state.playing = true;
  state.playTimer = performance.now();
  updatePlayButton();
};
document.getElementById("btn-stop-follow").onclick = stopPlayback;

const SPEEDS = [0.5, 1, 2];
document.getElementById("btn-speed").onclick = e => {
  const next = SPEEDS[(SPEEDS.indexOf(state.playSpeed) + 1) % SPEEDS.length];
  state.playSpeed = next;
  e.target.textContent = next + "×";
};

// Keyboard Shortcuts
window.addEventListener("keydown", e => {
  if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k") { e.preventDefault(); openSearch(); return; }
  if (document.getElementById("search-modal").classList.contains("open")) {
    if (e.key === "Escape") closeSearch();
    return;
  }
  if (e.key === "/") { e.preventDefault(); openSearch(); }
  else if (e.key === "ArrowLeft") { stopPlayback(); setEra(state.eraIdx - 1); }
  else if (e.key === "ArrowRight") { stopPlayback(); setEra(state.eraIdx + 1); }
  else if (e.key === " ") { e.preventDefault(); document.getElementById("btn-play").click(); }
  else if (e.key.toLowerCase() === "r") { document.getElementById("btn-reset-view").click(); }
});

window.addEventListener("resize", resize);

// Boot
(async function init() {
  resize();
  buildNEBoundary();
  const [mapData, biosData] = await Promise.all([
    decodeGzipB64(MAP_DATA_B64),
    decodeGzipB64(BIOS_DATA_B64)
  ]);
  state.data = mapData;
  state.bios = biosData;

  const sc = state.data.scale;
  state.land = state.data.land.map(r => decodeProjected(r, sc));
  state.lakes = state.data.lakes.map(r => decodeProjected(r, sc));
  state.rivers = state.data.rivers.map(r => decodeProjected(r, sc));

  // Build cross-era entity index for instant Omnisearch & lifespan sparklines
  state.data.eras.forEach((era, eIdx) => {
    for (const tuple of era.e) {
      const [nid, , isNS, , cx10, cy10, area10] = tuple;
      if (isNS === 1) continue;
      if (!state.entityIndex.has(nid)) state.entityIndex.set(nid, []);
      state.entityIndex.get(nid).push({ eraIdx: eIdx, year: era.y, area: area10 / 10, lon: cx10 / 10, lat: cy10 / 10 });
    }
  });

  initScrubber();
  const startIdx = Math.max(0, state.data.eras.findIndex(e => e.y === 1815));
  setEra(startIdx, { noDiff: true, instant: true }); // Start at 1815 AD
  document.getElementById("loading-veil").classList.add("hidden");
  requestAnimationFrame(draw);
})();
</script>
</body>
</html>
'''

if __name__ == "__main__":
    assemble()
