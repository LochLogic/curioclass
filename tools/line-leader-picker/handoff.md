# Handoff: Line Leader Picker

## Structure
src.html has tool-local wooden controls, the classroom chart, two-step rule desk, optional evidence cards, Our chart and the lower-left Manual. kit/curio.js supplies Motion, Sound and Read. There is no kit stylesheet or header. Workstations keep independent state for this page load.

drawDay is the single interpreter. Counts, stickers and evidence use its generated days. A coupled all-present day-2 draw records whether Bee's absence changed her turn. Before is captured only on a genuine edit of a finished month. Re-tapping a selected instruction preserves the month and Before.

The optional comparison inspection judges a changed slot, so either old or new tile identifies it. Any first inspection leaves that state; there is no required correct path. Evidence cards and both fairness opinions are independent controls available after a month appears. A fact mark always describes evidence, never the tapped answer's correctness. recordSummary preserves an old verdict when the current month has no new verdict. Sick and healthy rows use separate keys.

## Voice
Curio.voice owns Read and its log. The first quiet hint may speak once. Later interactions update readParts and the readout, without queuing automatic questions or lessons. Read speaks the parts in order: tile name before Run, Q1 about the rule, Q2's actual zero count before the feelings line. voice/lines.json equals allLines(). Browser narration is the current fallback; recordings remain the owner's later workflow.

Automatic three-answer narration and the unanswered Who quiz from the older review are superseded by the user's Curiosity instruction. polish.md records those departures. No kit engine changes were needed.

## Layout
Original paintings, palette, calendar and all 20 classmates remain. Compact ordinary cells retain large classmates beside 12-pixel sticker rows. Cells with more than six current or Before stickers use the full cell width for short rows. layoutStars recalculates columns on resize. Dashed blue outlines remain distinguishable from gold fills at shared coordinates.

The name slip belongs to the jar scene, never the calendar. Bee's bed mark persists while the sick switch is on. Our chart has a visible Close label at 1366 and above. The lower-left Manual has a sixty-pixel target.

## Sources and metadata
Manual and tool.draft.json name the authored Curio Class model (CC BY 4.0), interpreter (MIT) and existing illustration credit. No outside data or quoted standards wording was imported. Scratch contains independent arithmetic and runtime evidence. The old spec has no Curiosity number or concept entry; plate is null instead of an invented catalogue number.

## Sensitivity
Imaginary animals only. Bee's one-day absence has no medical claim. Waiting poses show an outcome, never a judgement about a child. Both fairness opinions remain available and ungraded.

## Engine changes wanted
Shared kit, docs and audit scripts were untouched. Audit compatibility wanted: scripts/audit_tool.py, MODES_JS, include `nav .workstations button` alongside the current header-only selectors. A Curiosity has no kit header, so the current selector misses its workstations. Explicit audit states cover both other workstations in this fix; the automatic per-mode control walk remains limited to the initial workstation.

## Validation
See polish.md for before/after evidence and the single final audit. Prior build and cold-review reports remain historical. Refine and its lens files were not edited.

## Final geometry and audit disposition
The single full audit completed with 71 frames. The four confirmed geometry causes were repaired and re-shot, with no second full audit. See polish.md and _scratch/line-leader-picker/audit-disposition.md. Source and audit-snapshot hashes differ explicitly in final-validation.json.

Fact marks are part of the diagram row, whose minimum height contains a 24-pixel marker. This avoids dependence on a heading's wrapped height. Short layouts reserve a 264-pixel side panel. Compact transport and chart utilities sit on the wooden rail. In a dense cell under 68 pixels high, four grid positions reserve room for the count and small portrait; twenty 12-pixel stars remain visible.

The Manual reserves a sixty-pixel title row. It makes the workbench inert while open, contains Tab focus, and restores focus on Escape or Close. The projector sick switch separates its On/Off state and caption in a two-row grid. These are tool-local repairs.
