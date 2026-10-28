# ASL graphics: the design path

Cory's call (2026-10-27, BASELINE.md): ASL tools are graphics only. No video, no photos of people. Do not re-pitch
video. Every ASL spec, build and review agent follows this file. It settles the "needs signing video" question in
IDEA-PASS-LOG.md (lang). The template is locked only after Cory sees the proof (last section).

## What has to come across without video

| Part of a sign | What the picture must show |
|---|---|
| Handshape | The exact finger shape, readable at a glance, with its name (B, bent V, flat O). |
| Location | Where the hand is: chin, forehead, chest, neutral space, the other hand. |
| Movement | Path (straight, arc, circle, zigzag), local movement (wiggle, twist, flick), contact, repeats, size. |
| Palm orientation | Which way the palm faces and the fingers point, at start and at end. |
| Non-manual markers | Brows, eyes, mouth, head nod, shake or tilt: question, negation, topic, intensity. |
| Timing and space | Holds and pauses; referents set at points in space and pointed back to; classifier paths; role shift (body and gaze turn to become a character). |

## The recommendation: a hybrid signer

Generated renders per sign are rich, but image models get fingers wrong, drift between the 2 to 4 frames a sign
needs, cannot be tweened, and each sign needs its own people review: rejected for hands. An all-vector signer is
precise and consistent, but a code-drawn person reads as a placeholder (rule 3). **Chosen: a hybrid.** One
consistent illustrated signer for body and face, with precise vector arms and hands drawn over it.

1. **Body plates (rendered once per character):** head and torso with the arms left out, in the classifier-scenes
   house style (flat shapes, soft texture). Views: front, back (signer's view), torso turned left and right (role
   shift). Drawn with gptart.py or art.py using `ref` for consistency, `"people": true`, people review. Never
   localart.py or cfart.py (they skip people by design).
2. **Face plates (rendered once per character):** about 12 expressions (neutral, yes/no question, wh-question,
   negation, topic, conditional, "mm", "cha", "oo", puffed cheeks, smile, surprise), each reviewed against a written
   description of the marker. Nod, shake and tilt are small transforms of the head plate, so they animate.
3. **Arms and hands (vector, in code):** a parametric hand. Each handshape is a short spec of finger bends and thumb
   position, rendered to flat SVG at any palm orientation, in the character's skin tone and sleeve color. One spec
   gives every view, the back view and the left-handed form, and the fingers are always right. Arms are two
   segments from fixed shoulder points to a named body-map location.

Because the hands are vector, the player tweens real motion between keyframes: movement without video.

### Panel conventions

- **Start, movement, end:** each sign is a strip. The movement panel shows a faint ghost of the start hand, the arrow
  and the solid end hand. A held sign with no path uses one panel.
- **Arrows** follow printed ASL dictionary practice: dominant hand orange, non-dominant blue, drawn start to end in
  the current view. Arcs and circles keep their shape; a double arrowhead or "x2" is a repeat; zigzag ticks at the
  fingertips are a wiggle; a curved arrow around the wrist is a twist; a small star is contact; two bars are a hold.
- **Handshape inset:** a close-up of each handshape in the panel corner, at its true orientation, with its name. A
  handshape change (flat O opening to 5) gets an inset at start and at end.
- **Face inset:** a larger crop of the face plate with a short label (wh-q, y/n-q, neg, topic). In the gloss, the
  marker is a line over the signs it covers, the standard ASL transcription convention.
- **Space map:** a top-down half-circle in front of the signer for referents, classifier paths and role shift.
  Tokens stay where they were set, so a point-back reads clearly.
- **Stepped flipbook player:** Play tweens at Slow or Natural speed; step buttons move one panel at a time; "Panels"
  lays out the whole strip. Calm mode shows steps only.
- **Viewpoint:** default is the viewer's view (facing the signer), as in dictionaries and as students read signs.
  Tools about space (classifiers, referents, story) add **Signer's view**, drawn from behind, so left and right
  match the student's own hands.
- **Left-handed:** mirrors the signer, arrows and space map so a left-dominant student copies their own form. Text
  and letter labels are never mirrored.

## The template: Sign Strip

One engine, `kit/asl-strip.js`, with a family doc `docs/families/asl.md` and one shared lexicon
`kit/asl/signs.json` (each tool lists only the sign ids it uses). It renders an entry as panels, a flipbook or a
static SVG (the same SVG can later feed Word Wall cards and printables). Each sign entry holds:

- `id`, `gloss` (THANK-YOU), `english` (meanings), `variant` (a note where regions differ)
- `hands`: one or two; for two, the non-dominant role (`mirror` or `base`) and its handshape
- `keyframes`: start, optional middles, end; per hand `hs` (handshape id), `loc` (body-map or space point), `palm`
  and `fingers` (up, down, in, out, toward center, away), `contact`
- `move`: `path` (straight, arc, circle, zigzag, none), `local` (wiggle, twist, flick, none), `repeat`, `size`, `speed`
- `face` (plate id, for the sign or for spans of keyframes), `head` (nod, shake, tilt), `gaze`
- `space`: loci the sign sets or points to (referents, agreement verbs, classifiers)
- `sources`: at least two open references, each with its description paraphrased
- `review`: status, the reviewer's blind reading, date

The body map (about 20 points) and the handshape inventory (about 40, starting with the letters, numbers and
classifier shapes already in use) are defined once in the family doc.

## How each ASL tool fits

- **asl-bingo-night:** the caller is the illustrated signer; a miss replays the sign as stepped panels with the
  handshape inset lit; pattern cards are panel pairs (palm turn, wrist point).
- **asl-family-tree:** each sentence is a strip with a space map, so the point-back that replaces a name is visible.
- **asl-hello-booth:** a small cast of illustrated signers (own plates, shared hands); attention norms become short
  comic strips.
- **asl-story-theater:** becomes a storyboard and comic-strip studio: the model story is a comic with role-shift
  body turns, gaze lines and a space map; the student builds a storyboard from the same parts, with optional
  on-device rehearsal recording.
- **deaf-culture-explorer:** host and signed stories become captioned illustrated comics; history rooms use
  illustrations and public-domain photos of places, objects and documents.
- **face-the-grammar:** same hand keyframes, swapped face plates, a large face inset and marker lines over the gloss;
  the splice level picks a face plate per span.
- **sign-parameters-lab:** the best fit: the five dials edit the entry and the panel redraws; curated pairs and "not
  a sign" results come from the same engine.
- **fingerspell-flash (live, later):** swap the public-domain line art for Sign Strip hands (true orientation,
  transitions, left-handed form); keep the current art until the proof passes.
- **classifier-scenes (live, later):** replace the generated hs-*.webp hands with vector handshapes, reuse the signer
  plates for the front and back views, and tween the classifier paths; scene pictures stay.

## Accuracy without video or outside people

Rule 5: a fresh review agent checks, then it ships.

1. The build agent writes each entry from at least two openly available written references (for example ASL-LEX
   phonological coding, Lifeprint and Handspeak descriptions; terms checked at spec; paraphrased, never copied).
2. The engine renders the panels. A **fresh review agent sees only the panels**, writes a blind reading of each
   parameter in plain words, then compares it with the references. A mismatch goes back to the entry.
3. Contact sheets of every sign in all three views (front, signer's view, left-handed) are checked for drift.
4. Regional variants are named in `variant`; the tool says it shows one common form.

On-screen note under every player: "These drawings show one common way to make each sign. Real signing flows and
varies by region and signer. When you can, practice with a fluent Deaf signer or your ASL teacher."
Camera mirror (rule 7): "The mirror uses your camera on this device only. Nothing is recorded or sent."
Recording (asl-story-theater): "Your video stays on this device and never leaves it."

## Proof first: three signs

A throwaway proof page (outside tools/) with three signs that cover every hard part:

1. **THANK-YOU:** flat hand from the chin, out and down; contact, a path, a pleasant face and small nod.
2. **NAME:** two H hands, the dominant taps the base hand twice; two hands, a base role, contact, a repeat.
3. **WHERE:** index finger shaken side to side with the wh-question face; local movement and a face marker.

Steps: write the three entries; build the parametric hand and arms on a plain stand-in torso; on Cory's go, draw one
signer (front, back, three face plates) with gptart.py and a people review; render each sign as panels, flipbook,
signer's view and left-handed; run the blind review. For contrast, render THANK-YOU as fully generated frames too,
so Cory sees the trade-off side by side before the template and family doc are locked.

## Open for Cory

- Do archival photos of people (Deaf President Now, 1988) count as "photos of people" in deaf-culture-explorer?
  Until answered: illustrations instead.
- The student's own camera (mirror, story rehearsal) stays as an optional on-device extra; it is not signer video.
