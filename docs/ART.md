# Art

Tools mix two kinds of art:
- **Illustrations** (characters, backgrounds, textures) are made with Gemini image generation, cut out, and bundled into the tool as small WebP images.
- **Vector** is kept for anything that moves in pieces or responds to the lesson: legs that step, particles, thermometers, charts, highlights.

## House style

Warm storybook illustration: soft gouache and colored-pencil texture, clean shapes, gentle shading, friendly proportions, rich but not neon colors. No text in images. Each tool can add its own flavor (fairy tale, marching band...) in its `prompts.json`. Characters across a tool use `"ref"` so they stay consistent.

## Pipeline

```
tools/<id>/art/prompts.json   what to draw (committed)
python scripts/art.py <id>    draws it: raw PNG to art/raw/ (not committed), finished art/<name>.webp (committed)
python scripts/art.py <id> --rekey   redoes only the cutout and sizing from art/raw/ (no new drawing, free)
tools/<id>/src.html           the tool source, referencing images as art:<name>
python scripts/bundle_tool.py inlines them -> tools/<id>/<id>.html (one offline file, as the contract requires)
```

`build_site.py` and `check_tools.py` bundle automatically.

Full-length characters: set `"aspect": "9:16"` so Gemini draws a portrait frame (its default landscape frame cuts figures off), and ask for a clear gap between the legs. A tool can then split the painting at the crotch with clip paths and step each painted leg on its own (see Marching Band).

Other options (see the top of `scripts/art.py`): `"key": "magenta"` for green subjects like lettuce, `"trim": 0.03` for backgrounds that come back with a painted frame. Small square scenes (like the evidence photos in Resource Detective) need no cutout at all.

Older grades: set `"house_style"` at the top of `prompts.json` to replace the storybook style (Moon Phase Model uses a planetarium look, Concert Ticket Market an editorial magazine look).

Scenes with a changing sky: ask for the sky as flat pure green and set `"cutout": "keyed"`. The sky becomes transparent (including gaps in leaves) and the tool paints its own sky behind it (Moon Phase Model's backyard). Keep the sky open: tall trees or walls hide anything the tool draws behind them.

Budget: about 30-80 KB per character and 100-150 KB per background as WebP, which keeps a tool well under the 2 MB limit.

## Gemini key

Store the key as a Windows user setting, never in the repo or in chat. In PowerShell:

```
[Environment]::SetEnvironmentVariable('GEMINI_API_KEY', (Read-Host 'Gemini API key'), 'User')
```

`scripts/art.py` reads it from there. Model: `gemini-3.1-flash-image` by default (override with `CURIO_IMAGE_MODEL`). Image generation is billed per image, at a few cents each.

## Provenance

Generated art is credited in each tool's `tool.json` sources as "Illustrations generated with Google Gemini, edited for Curio Class." Review every image before it ships: no text artifacts, no odd hands, and every child-facing character friendly and inclusive.

## Data files and recorded speech

- `"json:<name>"` in src.html is replaced by `tools/<id>/<name>.json` at bundle time (map paths, state shapes). `scripts/na_map.py` builds the North America map used by Nations of North America and Me on the Map.
- `"voice:*"` is replaced by the tool's recorded lines from `scripts/voice.py` (see POLISH.md, Sound and voice). Raw speech is kept in `voice/raw/` (not committed), so `--reencode` is free.

## Local art (no API)

When Gemini is unavailable (no credits) or for large batches, `scripts/localart.py` draws on this PC with FLUX.1-schnell (Apache 2.0) in KoboldCpp. Start `S:\AI\Start-FluxModel.bat` first (port 5002, about 7 s an image on the RTX 5080; `--sdoffloadcpu` swaps the text encoder and the image model in and out of the 16 GB card for every image).

- **Batches: `scripts/fluxbatch.py`** draws from the same model files in Python (diffusers), without KoboldCpp, in two phases: it encodes every prompt with T5-XXL and CLIP-L, frees them, then keeps the FLUX transformer and VAE on the card and draws the lot back to back. About 37 s to set up, then 3.6 s an image at 768 px (20 Word Wall cards: 108 s against 144 s; a few hundred: about half the time). Peak 14.6 GB of 16 GB, so stop KoboldCpp first and keep one image per call (four at once spill into shared memory and slow to 9 s each). `txt2img_many([(prompt, w, h, seed, out_path), ...])`; `scripts/wordart.py` uses it for draw runs and `--redo` when it is available (`--kobold` falls back to the server). Same never-people rule.

- `python scripts/localart.py <tool-id> [names] [--n 3]` draws candidates to `art/raw/<name>.c<k>.png` plus a contact sheet `_sheet-<name>.jpg`. Look at every candidate.
- `python scripts/localart.py <tool-id> --pick name:2 ...` keys the backdrop flat (FLUX paints shaded backdrops and cast shadows), then runs `art.py --rekey` for the cutout and sizing.
- Same prompts.json. `"sd"` replaces an asset's prompt for this model only. Leave hex codes out: FLUX paints "#00FF00" as text. Green or yellow-green subjects need `"key": "magenta"`.
- Space and glowing objects work best painted "on a pure black background" without a cutout and shown with `mix-blend-mode: screen`; the pick step crushes near-black to true black.
- **Never draw people with a local model.** An earlier Pony SDXL model drew a 13-year-old in underwear despite every safety setting; it is not used for Curio Class at all. People come from Gemini with review, or are plain silhouettes.
- Credit it in the tool's comment and tool.json sources: "Illustrations drawn with FLUX.1-schnell (Apache 2.0) on a local computer, edited for Curio Class".
- Classroom and home scenes can bring in people even when the prompt says "No people" (a calm-corner candidate drew two children). Look at every candidate; delete any with people. Wall posters come back with fake text.
- A cast shadow on a yellow-green key survives as a green blob (apple). Use the magenta key for red, orange and yellow subjects too, or `"shadow": "dark"`.

## ChatGPT art (gpt-image-2 through Codex)

`scripts/gptart.py` draws with gpt-image-2 through the Codex CLI on the ChatGPT subscription, with no API key (`npm i -g @openai/codex`, then `codex login` with the ChatGPT account). It is the best of the models at hands and tricky objects, and draws clean flat keys.

- `python scripts/gptart.py <tool-id> [names] [--n 1] [--ref name]` writes `art/raw/<name>.c20.png` (k from 20) and `_sheet-<name>-gpt.jpg`; pick with `localart.py --pick name:20` as usual. The pick records source "gpt-image-2 (Codex)".
- Same prompt as art.py, hex codes included (gpt-image keeps them out of the picture). People are allowed here, with a review of every image.
- Image turns use the plan's Codex allowance 3-5x faster than plain turns, so keep it for the hard cases; the script stops cleanly at the usage limit.
- Credit: "Illustrations generated with OpenAI gpt-image, edited for Curio Class".
- Word Wall cards that need a person doing the action (hop, skip, stretch) have a picture starting `people:` and are drawn by `scripts/wordpeople.py` the same way (candidates in closet/words/art/_raw/people/, `--pick key:k` keeps one). Give each card its own child so the set is varied.

## Daily art rhythm

1. **Cloudflare FLUX.2 klein** (`cfart.py`) for the bulk: objects, animals, places, about 95 free images a day (resets 00:00 UTC). Never people.
2. **Local FLUX** (`localart.py`) for higher-grade realistic subjects (diagrams, lab gear, landscapes) when Cloudflare is spent. Never people.
3. **Codex gpt-image-2** (`gptart.py`) for hands, objects the FLUX models keep getting wrong, and redraws flagged in review.
4. **Gemini** (`art.py`) to finish: people, character sets that need a reference, and anything still not right.

Every candidate is looked at before it is picked, and `artstatus.py` tracks needed / drawn / placed / ok.
