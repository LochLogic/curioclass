@group(0) @binding(0) var hdrTex : texture_2d<f32>;
@group(0) @binding(1) var hdrSamp : sampler;

struct VsOut {
  @builtin(position) pos : vec4<f32>,
  @location(0) uv : vec2<f32>,
};

@vertex
fn vsMain(@builtin(vertex_index) vid : u32) -> VsOut {
  var p = array<vec2<f32>, 3>(
    vec2<f32>(-1.0, -1.0),
    vec2<f32>( 3.0, -1.0),
    vec2<f32>(-1.0,  3.0)
  );
  var out : VsOut;
  let xy = p[vid];
  out.pos = vec4<f32>(xy, 0.0, 1.0);
  out.uv = vec2<f32>(xy.x * 0.5 + 0.5, 0.5 - xy.y * 0.5);
  return out;
}

// AgX Filmic Tone Mapping (prevents harsh neon clipping, preserves warm highlights)
fn agxDefaultContrastApprox(x : vec3<f32>) -> vec3<f32> {
  let x2 = x * x;
  let x4 = x2 * x2;
  return 15.5 * x4 * x2
    - 40.14 * x4 * x
    + 31.96 * x4
    - 6.868 * x2 * x
    + 0.4298 * x2
    + 0.1191 * x
    - 0.00232;
}

fn agxToneMap(val : vec3<f32>) -> vec3<f32> {
  let mIn = mat3x3<f32>(
    vec3<f32>(0.842479062253094, 0.0423282422610123, 0.0423756549057051),
    vec3<f32>(0.0784335999999992, 0.878468636469772, 0.0784336),
    vec3<f32>(0.0792237451477643, 0.0791661274605434, 0.879142973793104)
  );
  let mOut = mat3x3<f32>(
    vec3<f32>(1.19687900512017, -0.0528968517574562, -0.0529716355144438),
    vec3<f32>(-0.0980208811401368, 1.15190312990417, -0.0980434501171241),
    vec3<f32>(-0.0990297440797205, -0.0989611768448433, 1.15107367264116)
  );
  var v = max(val, vec3<f32>(1e-5));
  v = mIn * v;
  let minEv = -12.47393;
  let maxEv = 4.026069;
  v = clamp(log2(v), vec3<f32>(minEv), vec3<f32>(maxEv));
  v = (v - minEv) / (maxEv - minEv);
  v = agxDefaultContrastApprox(v);
  v = mOut * v;
  return clamp(v, vec3<f32>(0.0), vec3<f32>(1.0));
}

// Smooth 16-tap golden-angle HDR bokeh bloom with Karis luminance weighting (zero blocky halos)
fn sampleBloom(uv : vec2<f32>, texel : vec2<f32>) -> vec3<f32> {
  var acc = vec3<f32>(0.0);
  var wSum = 0.0;
  let goldenAngle = 2.39996323;
  for (var i = 0; i < 16; i = i + 1) {
    let fi = f32(i) + 0.5;
    let r = sqrt(fi / 16.0) * 12.5;
    let a = fi * goldenAngle;
    let off = vec2<f32>(cos(a), sin(a)) * r * texel;
    let s = textureSample(hdrTex, hdrSamp, uv + off).rgb;
    let lum = dot(s, vec3<f32>(0.2126, 0.7152, 0.0722));
    let bright = max(0.0, lum - 0.78) / max(lum, 0.001);
    let karis = 1.0 / (1.0 + lum * 0.35);
    let w = (1.15 - r / 14.0) * karis;
    acc += s * bright * w;
    wSum += w;
  }
  return acc / max(0.001, wSum);
}

@fragment
fn fsMain(in : VsOut) -> @location(0) vec4<f32> {
  let dims = vec2<f32>(textureDimensions(hdrTex));
  let texel = 1.0 / max(dims, vec2<f32>(1.0));

  let base = textureSample(hdrTex, hdrSamp, in.uv).rgb;
  let bloom = sampleBloom(in.uv, texel);

  var col = base + bloom * 0.42;
  col = agxToneMap(col * 1.08);

  // Subtle cozy edge vignette
  let d = length((in.uv - 0.5) * vec2<f32>(1.3, 1.0));
  col *= 1.0 - smoothstep(0.55, 1.18, d) * 0.22;

  return vec4<f32>(col, 1.0);
}
