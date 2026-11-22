struct WorldPropsUniforms {
  viewProj   : mat4x4<f32>,
  camPos     : vec4<f32>, // xyz, w = time
  sunDir     : vec4<f32>, // xyz, w = fogDensity
  starColor  : vec4<f32>, // rgb, w = dayFactor
  atmoColor  : vec4<f32>, // rgb, w = unused
  biomeTintA : vec4<f32>, // rgb, w = unused
  biomeTintB : vec4<f32>, // rgb, w = unused
};

@group(0) @binding(0) var<uniform> u : WorldPropsUniforms;

struct VsIn {
  // Per-vertex
  @location(0) pos      : vec3<f32>,
  @location(1) normal   : vec3<f32>,
  @location(2) color    : vec3<f32>,
  @location(3) material : vec2<f32>, // x = roughness, y = emissive
  // Per-instance
  @location(4) instPosScale : vec4<f32>, // xyz = world pos, w = scale
  @location(5) instMeta     : vec4<f32>, // x = rotY, y = kind (0=tree,1=lantern,2=spire,3=critter,4=ship), z = phase, w = tintMix
};

struct VsOut {
  @builtin(position) clipPos : vec4<f32>,
  @location(0) worldPos  : vec3<f32>,
  @location(1) worldNorm : vec3<f32>,
  @location(2) color     : vec3<f32>,
  @location(3) material  : vec2<f32>,
};

@vertex
fn vsMain(in : VsIn) -> VsOut {
  let time = u.camPos.w;
  let rotY = in.instMeta.x;
  let kind = i32(in.instMeta.y + 0.5);
  let phase = in.instMeta.z;
  let tintMix = in.instMeta.w;
  let scale = in.instPosScale.w;

  var localPos = in.pos * scale;

  // Gentle wind sway on trees & lantern-fungi
  if (kind == 0 || kind == 1) {
    let sway = sin(time * 1.6 + phase) * 0.08 * max(0.0, localPos.y);
    localPos.x += sway;
    localPos.z += cos(time * 1.3 + phase) * 0.05 * max(0.0, localPos.y);
  }

  // Cheerful hopping animation on friendly ground critters!
  var hopY = 0.0;
  var wanderOff = vec2<f32>(0.0);
  var effRotY = rotY;
  if (kind == 3) {
    let hop = abs(sin(time * 3.8 + phase));
    hopY = pow(hop, 1.6) * 0.75 * scale;
    wanderOff = vec2<f32>(cos(time * 0.45 + phase), sin(time * 0.45 + phase)) * 2.4;
  }

  // Graceful soaring circles & flapping wings on Sky-Gliders (kind == 5)!
  if (kind == 5) {
    let flap = sin(time * 4.4 + phase) * 0.42 * abs(localPos.x);
    localPos.y += flap;
    let orbitA = time * 0.38 + phase;
    let orbitR = 14.0 + tintMix * 16.0;
    wanderOff = vec2<f32>(cos(orbitA) * orbitR, sin(orbitA) * orbitR);
    hopY = sin(time * 1.1 + phase) * 3.2;
    effRotY = -orbitA;
  }

  // Swimming shallow-ocean rays/fish (kind == 6)
  if (kind == 6) {
    let swimA = time * 0.65 + phase;
    wanderOff = vec2<f32>(cos(swimA) * 7.5, sin(swimA) * 7.5);
    localPos.x += sin(time * 6.0 + localPos.z * 3.0 + phase) * 0.14;
    effRotY = -swimA;
  }

  // Wind-swaying grass & wildflowers (kind == 7)
  if (kind == 7) {
    let breeze = sin(time * 2.4 + phase) * 0.22 * max(0.0, localPos.y);
    localPos.x += breeze;
  }

  // Slowly spinning Discovery Space Station (kind == 8)
  if (kind == 8) {
    effRotY = rotY + time * 0.18;
  }

  let c = cos(effRotY);
  let s = sin(effRotY);
  let rx = localPos.x * c - localPos.z * s;
  let rz = localPos.x * s + localPos.z * c;
  let rnx = in.normal.x * c - in.normal.z * s;
  let rnz = in.normal.x * s + in.normal.z * c;

  let worldPos = in.instPosScale.xyz + vec3<f32>(rx + wanderOff.x, localPos.y + hopY, rz + wanderOff.y);
  let relPos = worldPos - u.camPos.xyz;

  // Subtle biome color harmony for flora (leave parked ship & critters crisp)
  var col = in.color;
  if (kind == 0 && in.pos.y > 3.0) {
    col = mix(col, mix(u.biomeTintA.rgb, u.biomeTintB.rgb, tintMix), 0.55);
  } else if (kind == 2) {
    col = mix(col, u.biomeTintB.rgb, tintMix * 0.45);
  }

  var out : VsOut;
  out.clipPos = u.viewProj * vec4<f32>(relPos, 1.0);
  out.worldPos = relPos;
  out.worldNorm = normalize(vec3<f32>(rnx, in.normal.y, rnz));
  out.color = col;
  out.material = in.material;
  return out;
}

@fragment
fn fsMain(in : VsOut) -> @location(0) vec4<f32> {
  let n = normalize(in.worldNorm);
  let sunDir = normalize(u.sunDir.xyz);
  let viewDir = normalize(-in.worldPos);
  let dayFactor = u.starColor.w;

  let ndl = max(0.0, dot(n, sunDir));
  let halfV = normalize(sunDir + viewDir);
  let rough = clamp(in.material.x, 0.1, 0.95);
  let spec = pow(max(0.0, dot(n, halfV)), mix(64.0, 6.0, rough)) * mix(0.65, 0.06, rough) * dayFactor;

  // Backlit subsurface scattering glow on foliage & lantern caps
  let sss = pow(max(0.0, dot(-viewDir, sunDir)), 3.0) * 0.28 * dayFactor;

  let skyAmbient = mix(vec3<f32>(0.06, 0.08, 0.16), u.atmoColor.rgb * 0.35 + vec3<f32>(0.14, 0.16, 0.2), dayFactor);
  let sunTint = mix(vec3<f32>(1.0, 0.58, 0.30), u.starColor.rgb, smoothstep(0.0, 0.35, sunDir.y));

  var col = in.color * (skyAmbient * (0.55 + 0.45 * n.y) + sunTint * (ndl * 1.35 + sss) * dayFactor) + sunTint * spec;

  // Bioluminescence shines brighter at dusk & night!
  let nightBoost = mix(2.2, 0.95, dayFactor);
  col += in.color * in.material.y * nightBoost;

  // Aerial perspective fog matching planet.wgsl
  let dist = length(in.worldPos);
  let fog = 1.0 - exp(-dist * u.sunDir.w);
  let haze = mix(vec3<f32>(0.04, 0.06, 0.12), u.atmoColor.rgb * 0.82 + vec3<f32>(0.12), dayFactor);
  col = mix(col, haze, clamp(fog * 0.88, 0.0, 0.92));

  return vec4<f32>(col, 1.0);
}
