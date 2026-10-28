r"""Draw many pictures fast with local FLUX.1-schnell in two phases, without KoboldCpp.

    from fluxbatch import txt2img_many
    txt2img_many([(prompt, w, h, seed, out_path), ...])          # saves each image (or save(img, out_path))
    python scripts/fluxbatch.py "prompt" [more prompts] [--size 768] [--out dir]   quick test

Phase 1 (encode) loads only the text encoders, T5-XXL (the fp8 file upcast to bf16) and CLIP-L, encodes every
prompt, then frees them. Phase 2 (draw) loads only the FLUX transformer (the same Q6_K GGUF through diffusers) and
the VAE, keeps them on the GPU and draws every image back to back from the cached embeddings. KoboldCpp with
--sdoffloadcpu swaps the encoder and the model for every image instead (7.2 s an image). Same settings as there:
4 steps, no guidance (schnell is distilled). Nothing else may hold the GPU, so stop KoboldCpp first.

Same files as S:\AI\Start-FluxModel.bat (S:\AI\models\flux, CURIO_FLUX_DIR overrides). The BFL repo is gated, so the
small diffusers configs are written to <flux dir>\diffusers\ here, and the tokenizers come from the ungated
openai/clip-vit-large-patch14 and google/t5-v1_1-xxl repos (a few MB, in the Hugging Face cache on S:).
Never draw people with this model (see localart.py).
"""
import gc, json, os, sys, time
from pathlib import Path

FLUX = Path(os.environ.get('CURIO_FLUX_DIR', r'S:\AI\models\flux'))
CFG = FLUX / 'diffusers'
CLIP, T5 = 'openai/clip-vit-large-patch14', 'google/t5-v1_1-xxl'
CONFIGS = {
    'transformer': {'_class_name': 'FluxTransformer2DModel', 'attention_head_dim': 128, 'guidance_embeds': False,
                    'in_channels': 64, 'joint_attention_dim': 4096, 'num_attention_heads': 24, 'num_layers': 19,
                    'num_single_layers': 38, 'patch_size': 1, 'pooled_projection_dim': 768,
                    'axes_dims_rope': [16, 56, 56]},
    'vae': {'_class_name': 'AutoencoderKL', 'act_fn': 'silu', 'block_out_channels': [128, 256, 512, 512],
            'down_block_types': ['DownEncoderBlock2D'] * 4, 'up_block_types': ['UpDecoderBlock2D'] * 4,
            'force_upcast': True, 'in_channels': 3, 'out_channels': 3, 'latent_channels': 16,
            'layers_per_block': 2, 'mid_block_add_attention': True, 'norm_num_groups': 32, 'sample_size': 1024,
            'scaling_factor': 0.3611, 'shift_factor': 0.1159, 'use_post_quant_conv': False, 'use_quant_conv': False},
    'scheduler': {'_class_name': 'FlowMatchEulerDiscreteScheduler', 'base_image_seq_len': 256, 'base_shift': 0.5,
                  'max_image_seq_len': 4096, 'max_shift': 1.15, 'num_train_timesteps': 1000, 'shift': 1.0,
                  'use_dynamic_shifting': False},
}
CHUNK = 400  # prompts per encode/draw round: embeddings are 2 MB each, kept in RAM


def available():
    """True when diffusers, a CUDA GPU and the model files are all here."""
    try:
        import diffusers, gguf, torch  # noqa: F401
        return torch.cuda.is_available() and all((FLUX / f).exists() for f in (
            'flux1-schnell-Q6_K.gguf', 't5xxl_fp8_e4m3fn.safetensors', 'clip_l.safetensors', 'ae.safetensors'))
    except ImportError:
        return False


def _configs():
    for sub, cfg in CONFIGS.items():
        p = CFG / sub / ('scheduler_config.json' if sub == 'scheduler' else 'config.json')
        if not p.exists():
            p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(cfg, indent=1))


def _free():
    import torch
    gc.collect(); torch.cuda.empty_cache()


def _load(cls, config, path, dtype):
    """Build a transformers model on the meta device and fill it from a single safetensors file, cast to dtype."""
    from accelerate import init_empty_weights
    from safetensors.torch import load_file
    with init_empty_weights():
        m = cls(config)
    have = m.state_dict().keys()  # transformers 5 dropped CLIP's "text_model." prefix
    sd = {k if k in have else k.split('.', 1)[1]: v.to(dtype) for k, v in load_file(path).items()}
    m.load_state_dict(sd, strict=True, assign=True)
    del sd
    return m.to('cuda', dtype).eval().requires_grad_(False)


def encode(prompts, batch=16):
    """Phase 1: [(prompt_embeds, pooled_prompt_embeds)] on the CPU, one per prompt; the encoders are freed after."""
    import torch
    from transformers import CLIPTextConfig, CLIPTextModel, CLIPTokenizer, T5Config, T5EncoderModel, T5TokenizerFast
    tok, tok2 = CLIPTokenizer.from_pretrained(CLIP), T5TokenizerFast.from_pretrained(T5)
    clip = _load(CLIPTextModel, CLIPTextConfig.from_pretrained(CLIP), FLUX / 'clip_l.safetensors', torch.bfloat16)
    t5 = _load(T5EncoderModel, T5Config.from_pretrained(T5), FLUX / 't5xxl_fp8_e4m3fn.safetensors', torch.bfloat16)
    out = []
    with torch.inference_mode():
        for i in range(0, len(prompts), batch):
            ps = prompts[i:i + batch]
            ids = tok(ps, padding='max_length', max_length=77, truncation=True, return_tensors='pt').input_ids
            pooled = clip(ids.to('cuda'), output_hidden_states=False).pooler_output
            ids = tok2(ps, padding='max_length', max_length=256, truncation=True, return_tensors='pt').input_ids
            emb = t5(ids.to('cuda'))[0]
            out += [(e[None].cpu(), p[None].cpu()) for e, p in zip(emb, pooled)]
    del clip, t5; _free()
    return out


def pipeline():
    """Phase 2 model: the GGUF transformer and the VAE on the GPU, no text encoders."""
    import torch
    from diffusers import (AutoencoderKL, FlowMatchEulerDiscreteScheduler, FluxPipeline, FluxTransformer2DModel,
                           GGUFQuantizationConfig)
    _configs()
    tr = FluxTransformer2DModel.from_single_file(
        str(FLUX / 'flux1-schnell-Q6_K.gguf'), config=str(CFG), subfolder='transformer', torch_dtype=torch.bfloat16,
        quantization_config=GGUFQuantizationConfig(compute_dtype=torch.bfloat16))
    vae = AutoencoderKL.from_single_file(str(FLUX / 'ae.safetensors'), config=str(CFG), subfolder='vae',
                                         torch_dtype=torch.bfloat16)
    sch = FlowMatchEulerDiscreteScheduler.from_pretrained(str(CFG), subfolder='scheduler')
    pipe = FluxPipeline(scheduler=sch, vae=vae, text_encoder=None, tokenizer=None, text_encoder_2=None,
                        tokenizer_2=None, transformer=tr).to('cuda')
    pipe.set_progress_bar_config(disable=True)
    return pipe


def draw(embeds, width, height, seeds, pipe=None):
    """Phase 2: one PIL image per (embedding, seed). Pass pipe to keep the model loaded across calls."""
    import torch
    own = pipe is None
    pipe = pipe or pipeline()
    ims = []
    for (e, p), seed in zip(embeds, seeds):
        ims += pipe(prompt_embeds=e.to('cuda'), pooled_prompt_embeds=p.to('cuda'), width=width, height=height,
                    num_inference_steps=4, guidance_scale=0.0, max_sequence_length=256,
                    generator=torch.Generator('cuda').manual_seed(seed)).images
    if own:
        del pipe; _free()
    return ims


def txt2img_many(jobs, save=None):
    """Draw [(prompt, w, h, seed, out_path)] in both phases; save(img, out_path) defaults to img.save(out_path).
    Returns timings {'encode': s, 'load': s, 'draw': [s per image]}."""
    t = {'encode': 0., 'load': 0., 'draw': []}
    for i in range(0, len(jobs), CHUNK):
        part = jobs[i:i + CHUNK]
        t0 = time.time()
        embeds = encode([j[0] for j in part])
        t['encode'] += time.time() - t0; t0 = time.time()
        pipe = pipeline()
        t['load'] += time.time() - t0
        print(f'encoded {len(part)} prompts in {t["encode"]:.0f}s, model loaded in {t["load"]:.0f}s', flush=True)
        for k, ((prompt, w, h, seed, out), emb) in enumerate(zip(part, embeds), 1):
            t0 = time.time()
            im = draw([emb], w, h, [seed], pipe)[0]
            Path(out).parent.mkdir(parents=True, exist_ok=True)
            (save or (lambda im, p: im.save(p)))(im, out)
            t['draw'].append(time.time() - t0)
            if k % 25 == 0 or k == len(part):
                print(f'{i + k}/{len(jobs)} drawn, {sum(t["draw"]) / len(t["draw"]):.2f} s each', flush=True)
        del pipe, embeds; _free()
    return t


def main():
    a = sys.argv[1:]
    opt = lambda k, d: a[a.index(k) + 1] if k in a else d
    skip = {opt('--size', None), opt('--out', None)}
    prompts = [p for p in a if not p.startswith('--') and p not in skip]
    n, out = int(opt('--size', 768)), Path(opt('--out', '.'))
    print(txt2img_many([(p, n, n, k, out / f'fluxbatch-{k}.png') for k, p in enumerate(prompts)]))


if __name__ == '__main__':
    main()
