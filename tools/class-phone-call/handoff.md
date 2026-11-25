# Handoff: class-phone-call

## Status
- Built, self-checked, and bundled at `tools/class-phone-call/index.html` (`675 KB`).
- Source: `tools/class-phone-call/src.html`
- Audit states: `tools/class-phone-call/audit-states.json`
- Voice lines manifest: `tools/class-phone-call/voice/lines.json` (135 lines exported; ready for `python scripts/voice.py class-phone-call` TTS generation when `GEMINI_API_KEY` is configured).
- Art prompts manifest: `tools/class-phone-call/art/prompts.json` (25 Gemini WebP assets in `art/*.webp`, including all 6 `"people": true` illustrations and all 4 table medallions; 26 non-people card illustrations currently use rich inline SVG fallbacks until Gemini image quota resets).

## Next steps for production release
1. Run `python scripts/voice.py class-phone-call` with `GEMINI_API_KEY` to record the MP3 voice clips in `tools/class-phone-call/voice/`.
2. Optional: once Gemini image quota resets, paint the remaining 26 non-people card illustrations in `art/prompts.json` and run `python scripts/art.py class-phone-call --rekey <name>`.
3. Re-bundle without `CURIO_DRAFT=1`: `python scripts/bundle_tool.py class-phone-call`.
