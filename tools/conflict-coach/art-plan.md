# Conflict Coach art plan (characters)

Cory's review: "Great, just needs improved characters." The five kids are drawn in code today (`kidSVG`, `headSVG`,
`hairBack`, `hairTop`, `POSE`, `armPts` in src.html, about lines 430-530). This plan replaces them with painted
gpt-image-2 figures, three body-language states per kid. Prompts are in `art/prompts.json` (names `kid-*`).

## How the five postures map to three paintings

The meter has five stops and the kid has five postures today. Three paintings per kid cover them; the in-between stops
use a small whole-figure transform (lean about the hips) on top of the painting.

| Meter stop | Posture today | Painting | Transform on top |
|---|---|---|---|
| Heated (0) | arms crossed, turned away, leaning back | `kid-<name>-upset` | lean back about 4 deg |
| Tense (1, every scene starts here) | half turned, hands gripped in lap | `kid-<name>-guarded` | none |
| Calm (2) | neutral, hands on knees | `kid-<name>` (base) | upright, none |
| Listening (3) | facing you, head tilt, brows up | `kid-<name>` (base) | lean toward you about 3 deg |
| Working it out (4) | small smile, one hand open | `kid-<name>` (base) | lean toward you about 5 deg |

Line Builder reactions (`setPosture(t === 0 ? 4 : t === 1 ? 1 : 0)`): no traps = base, one trap = guarded, two or
more = upset. Line Builder neutral (posture 2) = base. The picker face chips (`faceIcon`) use the base painting cropped
to the head (no extra image).

Change between paintings: 400 ms crossfade plus the lean easing (the same timing as today); instant when Motion is off.

## Assets

All characters: source gpt-image-2 through Codex (`scripts/gptart.py`), `"people": true`, cutout on green
(Aiyana on magenta: her teal jacket is close to the green key), `despill`, aspect 3:4, `height` 480, quality 72.
Shown at up to about 380 CSS px tall (`k` up to 1.45 on a 262-unit figure), so 480 px is sharp enough without
paying for 2x.

| # | Name | Source | Size budget (WebP) | Replaces (code-drawn) | Where in src.html |
|---|---|---|---|---|---|
| 1 | kid-jordan | Codex | 30-40 KB | Jordan, Calm/Listening/Working it out; face chip | `SC[0].look`; `kidSVG`, `headSVG`, `faceIcon`; `drawStage` `#kidG` |
| 2 | kid-priya | Codex | 30-40 KB | Priya, same | `SC[1].look`; same functions |
| 3 | kid-mateo | Codex | 30-40 KB | Mateo, same | `SC[2].look`; same |
| 4 | kid-aiyana | Codex | 30-40 KB | Aiyana, same | `SC[3].look`; same |
| 5 | kid-sam | Codex | 30-40 KB | Sam, same (also the courtyard kid in Line Builder when The Weekend Plan is chosen) | `SC[4].look`; same |
| 6 | kid-jordan-guarded | Codex, ref kid-jordan | 30-40 KB | Tense posture (`POSE[1]`, arms `lap`) | `POSE`, `armPts('lap')`, `setPosture(1)` |
| 7 | kid-priya-guarded | Codex, ref kid-priya | 30-40 KB | same | same |
| 8 | kid-mateo-guarded | Codex, ref kid-mateo | 30-40 KB | same | same |
| 9 | kid-aiyana-guarded | Codex, ref kid-aiyana | 30-40 KB | same | same |
| 10 | kid-sam-guarded | Codex, ref kid-sam | 30-40 KB | same | same |
| 11 | kid-jordan-upset | Codex, ref kid-jordan | 30-40 KB | Heated posture (`POSE[0]`, arms `crossed`) | `POSE`, `armPts('crossed')`, `setPosture(0)` |
| 12 | kid-priya-upset | Codex, ref kid-priya | 30-40 KB | same | same |
| 13 | kid-mateo-upset | Codex, ref kid-mateo | 30-40 KB | same | same |
| 14 | kid-aiyana-upset | Codex, ref kid-aiyana | 30-40 KB | same | same |
| 15 | kid-sam-upset | Codex, ref kid-sam | 30-40 KB | same | same |

Codex images: 15 first draws (one over the "about 14" guide; see Questions). Allow 2-4 redraws for hands or a
mismatched variant.

Looks follow spec.md (skin and hair as in `SC[].look`, shirts in the scene colors). Jordan and Sam use "they" in the
dialogue, so both are drawn with a relaxed, gender-neutral look. Prompts carry no names (names invite lettering).

## Size

- New characters: 15 x about 32 KB = about 480 KB as files (range 375-600 KB).
- Inlined as base64 that is about 640 KB in the bundle (x 4/3). Bundle today 0.97 MB, so about 1.6 MB after, under the
  2 MB limit, with the vector kid code (about 8 KB) removed.
- If a painting comes back over 40 KB, drop it to quality 66 or height 440 with `art.py --rekey` (free).

## Draw order

1. The five bases: `kid-jordan`, `kid-priya`, `kid-mateo`, `kid-aiyana`, `kid-sam`. Pick each
   (`localart.py --pick kid-x:20`), so `art/raw/kid-x.png` exists for the ref. Look at all five side by side before
   going on: same drawing style, same scale, all facing left, friendly, age 12, no text on clothes.
2. The five `-guarded` variants (`"ref"` is set, so each matches its base).
3. The five `-upset` variants.
4. Review every image (hands, faces, no lettering, sympathetic not scary), set `review` in prompts.json.

Commands (Cory runs them, one at a time):

```
python scripts/gptart.py conflict-coach kid-jordan kid-priya kid-mateo kid-aiyana kid-sam
python scripts/localart.py conflict-coach --pick kid-jordan:20 kid-priya:20 kid-mateo:20 kid-aiyana:20 kid-sam:20
python scripts/gptart.py conflict-coach kid-jordan-guarded kid-priya-guarded kid-mateo-guarded kid-aiyana-guarded kid-sam-guarded
python scripts/gptart.py conflict-coach kid-jordan-upset kid-priya-upset kid-mateo-upset kid-aiyana-upset kid-sam-upset
```

## Wiring notes (phase 2)

- Each painting is placed by an anchor: the hip point on the seat (where `kidSVG` puts (0, 0)) and the head center
  (for the face chip crop and the name label). The cutout trims to the figure, so the hip point differs per painting;
  measure it after each pick and keep a small table in src.html (`ANCHOR['kid-jordan-upset'] = {hx, hy, cx, cy}` as
  fractions of the image).
- `#kidG` holds two `<image>` elements (current and next) for the crossfade; the lean is a rotate about the hip anchor.
- Facing: all paintings face left (toward your seat). If one comes back facing right, flip it with `scale(-1 1)` only if
  nothing in it is one-sided (Priya's braid over one shoulder is fine either way).
- The `heated` lean room stays: `kidX = W - pad - 90 * k`; re-check the verify.md regression 1 (kid past the right edge)
  with the upset painting at every size.
- aria-label text (`POSTURE_WORDS`) should be updated to describe the three paintings plus lean.
- Update spec.md (Faces and Art sections), notes.md (Good to know, sources line), the comment at src.html line 21 and
  tool.json sources: "Illustrations generated with OpenAI gpt-image, edited for Curio Class" next to the FLUX credit.
  Rebuild preview.svg (`scripts/preview.py conflict-coach`), it still shows the vector kid.

## What stays vector

- The bench (seat, backrest, legs): it is laid out per box and the kid sits on it; Partner Cards shows it empty.
- The meter, its marker motion and stop icons; the turn strip; speech bubbles and the faded "Last time" bubble; the
  ending card icons; the name label; Line Builder frame and tiles; Partner Cards.
- The lean and crossfade between paintings (transforms in code, not extra paintings).
- The paper overlay on the backdrop.

Nothing on the kid animates in pieces any more, so no split body parts are needed.

## Backdrops (FLUX, already in the bundle)

Looked at all five at full size. They are clean and warm and sit under a 0.32 paper overlay. Faint scribbles:

| Backdrop | What is there | Redraw? |
|---|---|---|
| bg-classroom | bulletin board at left and two clipboards with scribbled lines; clock face has garbled numerals | Optional, best candidate. Bubbles stack on the left, over that board |
| bg-hallway | papers taped on both doors with scribbled lines (the right door sits behind the kid) | Optional |
| bg-lab | two small wall signs with pseudo-symbols, high on the walls | No, very faint under the overlay |
| bg-courtyard | small notices on the brick and the door | No |
| bg-artroom | clean (blank papers, an easel) | No |

If redrawn (free, Cloudflare `cfart.py` or local FLUX, never people), add to the existing prompt: "No papers, notices
or signs on the walls or doors, no clock." Same name, 16:9, width 1600, quality 72, so the size stays about the same
(45-55 KB each).

## Questions for Cory

1. 15 Codex images (three per kid) is one over the "about 14" guide. OK, or drop to two per kid (base and upset, 10
   images, Tense then reuses upset with less lean)?
2. Calm, Listening and Working it out share the base painting and differ only by lean. verify.md "Done when 7" asks for
   five visibly different postures; the meter word and icon still change. Accept that, or add a fourth `-listening`
   variant per kid (5 more Codex images, 20 total)?
3. Redraw bg-classroom and bg-hallway without the scribbled notices and clock (free Cloudflare), or leave all five?
