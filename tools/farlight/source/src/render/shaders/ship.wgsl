struct ShipUniforms {
  mvp         : mat4x4<f32>,
  modelRot    : mat4x4<f32>,
  lightDir    : vec4<f32>, // xyz, w = boostAmount
  starColor   : vec4<f32>, // rgb, w = time
  nebulaFill  : vec4<f32>, // rgb, w = unused
};

@group(0) @binding(0) var<uniform> u : ShipUniforms;

struct VsIn {
  @location(0) pos      : vec3<f32>,
  @location(1) normal   : vec3<f32>,
  @location(2) color    : vec3<f32>,
  @location(3) material : vec2<f32>, // x = roughness, y = emissive
};

struct VsOut {
  @builtin(position) pos   : vec4<f32>,
  @location(0) worldNorm   : vec3<f32>,
  @location(1) localPos    : vec3<f32>,
  @location(2) color       : vec3<f32>,
  @location(3) material    : vec2<f32>,
};

@vertex
fn vsMain(in : VsIn) -> VsOut {
  var p = in.pos;
  // Stretch glowing thruster exhaust plumes dynamically with boost & gentle flicker!
  if (in.material.y > 1.3 && p.z > 1.0) {
    let time = u.starColor.w;
    let boost = u.lightDir.w;
    let flicker = 0.92 + 0.12 * sin(time * 34.0 + p.x * 9.0);
    p.z = 1.0 + (p.z - 1.0) * (0.65 + boost * 1.45) * flicker;
  }

  var out : VsOut;
  out.pos = u.mvp * vec4<f32>(p, 1.0);
  out.worldNorm = normalize((u.modelRot * vec4<f32>(in.normal, 0.0)).xyz);
  out.localPos = in.pos;
  out.color = in.color;
  out.material = in.material;
  return out;
}

@fragment
fn fsMain(in : VsOut) -> @location(0) vec4<f32> {
  let n = normalize(in.worldNorm);
  let l = normalize(u.lightDir.xyz);
  let v = normalize(vec3<f32>(0.0, 0.18, 1.0));
  let h = normalize(l + v);

  let ndl = max(0.0, dot(n, l));
  let hemi = 0.5 + 0.5 * n.y;
  let skyRefl = mix(u.nebulaFill.rgb * 0.35, vec3<f32>(0.36, 0.48, 0.72), hemi);

  // Subtle aerospace hull panel seams on painted surfaces
  let seamZ = smoothstep(0.025, 0.0, abs(fract(in.localPos.z * 1.45) - 0.5));
  let seamX = smoothstep(0.02, 0.0, abs(fract(in.localPos.x * 1.8) - 0.5));
  let panelMask = select(1.0 - max(seamZ, seamX) * 0.14, 1.0, in.material.x < 0.15 || in.material.y > 0.5);

  let rough = clamp(in.material.x, 0.05, 0.95);
  let shininess = mix(140.0, 10.0, rough);
  let spec = pow(max(0.0, dot(n, h)), shininess) * mix(1.05, 0.10, rough);

  // Crisp clearcoat / glass canopy Fresnel sky reflection
  let fresnel = pow(1.0 - max(0.0, dot(n, v)), 3.2);
  let rim = fresnel * (1.0 - rough) * 0.65;

  let baseCol = in.color * panelMask;
  let lit = baseCol * (skyRefl * 0.68 + u.starColor.rgb * ndl * 1.2) + u.starColor.rgb * spec + skyRefl * rim;

  // Dynamic glowing engines & nav beacons
  let boost = u.lightDir.w;
  let glow = in.color * in.material.y * (1.25 + boost * 2.1);

  return vec4<f32>(lit + glow, 1.0);
}
