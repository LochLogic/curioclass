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
tools/<id>/src.html           the tool source, referencing images as art:<name>
python scripts/bundle_tool.py inlines them -> tools/<id>/<id>.html (one offline file, as the contract requires)
```

`build_site.py` and `check_tools.py` bundle automatically.

Budget: about 30-80 KB per character and 100-150 KB per background as WebP, which keeps a tool well under the 2 MB limit.

## Gemini key

Store the key as a Windows user setting, never in the repo or in chat. In PowerShell:

```
[Environment]::SetEnvironmentVariable('GEMINI_API_KEY', (Read-Host 'Gemini API key'), 'User')
```

`scripts/art.py` reads it from there. Model: `gemini-3.1-flash-image` by default (override with `CURIO_IMAGE_MODEL`). Image generation is billed per image, at a few cents each.

## Provenance

Generated art is credited in each tool's `tool.json` sources as "Illustrations generated with Google Gemini, edited for Curio Class." Review every image before it ships: no text artifacts, no odd hands, and every child-facing character friendly and inclusive.
