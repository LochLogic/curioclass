struct PlanetUniform {
  posRadius : vec4<f32>,    // xyz = camera-relative pos, w = radius
  colorA    : vec4<f32>,    // rgb, w = isGiant (0 or 1)
  colorB    : vec4<f32>,    // rgb, w = hasRings (0 or 1)
  atmoRing  : vec4<f32>,    // rgb = atmosphereColor, w = ringTilt
  ringData  : vec4<f32>,    // x = ringInner, y = ringOuter, z = seed, w = unused
  ringColor : vec4<f32>,    // rgb = ringColor, w = unused
};

struct SpaceUniforms {
  camRight   : vec4<f32>,   // xyz, w = aspect
  camUp      : vec4<f32>,   // xyz, w = tanHalfFov
  camForward : vec4<f32>,   // xyz, w = time
  starPosRad : vec4<f32>,   // xyz = camera-relative star pos, w = starRadius
  starColor  : vec4<f32>,   // rgb, w = starKind (0..4)
  nebulaA    : vec4<f32>,   // rgb, w = quality (0=Perf, 1=High, 2=Ultra)
  nebulaB    : vec4<f32>,   // rgb, w = planetCount
  jumpParams : vec4<f32>,   // x = jumpProgress (0..1), y = scanPulse (0..1), zw = unused
  planets    : array<PlanetUniform, 6>,
};

@group(0) @binding(0) var<uniform> u : SpaceUniforms;

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
  out.uv = xy;
  return out;
}

fn hash31(p : vec3<f32>) -> f32 {
  var q = fract(p * 0.1031);
  q += dot(q, q.yzx + 33.33);
  return fract((q.x + q.y) * q.z);
}

fn noise3(p : vec3<f32>) -> f32 {
  let i = floor(p);
  let f = fract(p);
  let u3 = f * f * (3.0 - 2.0 * f);

  let n000 = hash31(i + vec3<f32>(0.0, 0.0, 0.0));
  let n100 = hash31(i + vec3<f32>(1.0, 0.0, 0.0));
  let n010 = hash31(i + vec3<f32>(0.0, 1.0, 0.0));
  let n110 = hash31(i + vec3<f32>(1.0, 1.0, 0.0));
  let n001 = hash31(i + vec3<f32>(0.0, 0.0, 1.0));
  let n101 = hash31(i + vec3<f32>(1.0, 0.0, 1.0));
  let n011 = hash31(i + vec3<f32>(0.0, 1.0, 1.0));
  let n111 = hash31(i + vec3<f32>(1.0, 1.0, 1.0));

  let nx00 = mix(n000, n100, u3.x);
  let nx10 = mix(n010, n110, u3.x);
  let nx01 = mix(n001, n101, u3.x);
  let nx11 = mix(n011, n111, u3.x);
  let nxy0 = mix(nx00, nx10, u3.y);
  let nxy1 = mix(nx01, nx11, u3.y);
  return mix(nxy0, nxy1, u3.z);
}

fn fbm(p : vec3<f32>, octaves : i32) -> f32 {
  var v = 0.0;
  var amp = 0.5;
  var q = p;
  for (var i = 0; i < octaves; i = i + 1) {
    v += amp * noise3(q);
    q = q * 2.04 + vec3<f32>(13.7, 7.3, 5.1);
    amp *= 0.5;
  }
  return v;
}

fn starBlackbody(t : f32) -> vec3<f32> {
  let warm = vec3<f32>(1.0, 0.72, 0.48);
  let mid  = vec3<f32>(1.0, 0.96, 0.90);
  let cool = vec3<f32>(0.68, 0.85, 1.0);
  return select(mix(mid, cool, (t - 0.5) * 2.0), mix(warm, mid, t * 2.0), t < 0.5);
}

fn sampleBackground(dir : vec3<f32>, time : f32, octaves : i32) -> vec3<f32> {
  // Deep indigo-navy cosmic canvas (warmer & friendlier than pure pitch black)
  var col = vec3<f32>(0.012, 0.018, 0.038);

  // Milky Way band & domain-warped volumetric nebula
  let band = exp(-abs(dir.y * 2.4 + sin(dir.x * 2.0) * 0.35) * 2.6);
  let warp = fbm(dir * 2.3 + vec3<f32>(0.0, time * 0.005, 0.0), octaves);
  let neb1 = fbm(dir * 3.1 + vec3<f32>(warp * 1.4), octaves);
  let neb2 = fbm(dir * 5.2 - vec3<f32>(warp * 1.1), max(2, octaves - 1));

  let cloudA = pow(max(0.0, neb1 - 0.36), 2.1) * (0.45 + 1.15 * band);
  let cloudB = pow(max(0.0, neb2 - 0.42), 2.3) * (0.35 + 0.85 * band);
  col += u.nebulaA.rgb * cloudA * 0.85;
  col += u.nebulaB.rgb * cloudB * 0.65;

  // Two layers of crisp procedural stars
  for (var layer = 0; layer < 2; layer = layer + 1) {
    let scale = select(170.0, 95.0, layer == 0);
    let cell = floor(dir * scale);
    let f = fract(dir * scale) - 0.5;
    let rnd = hash31(cell + vec3<f32>(f32(layer) * 41.0));
    if (rnd > 0.968) {
      let jitter = vec3<f32>(
        hash31(cell + vec3<f32>(1.7, 3.1, 5.3)),
        hash31(cell + vec3<f32>(7.1, 2.3, 9.7)),
        hash31(cell + vec3<f32>(4.3, 8.9, 1.1))
      ) - 0.5;
      let d = length(f - jitter * 0.55);
      let twinkle = 0.78 + 0.22 * sin(time * (1.8 + rnd * 4.0) + rnd * 40.0);
      let size = select(0.11, 0.16, layer == 0);
      let star = exp(-d * d / (size * size * 0.18)) * twinkle;
      let bright = select(1.4, 2.8, layer == 0) * (0.5 + 0.5 * fract(rnd * 137.0));
      col += starBlackbody(fract(rnd * 53.7)) * star * bright;
    }
  }
  return col;
}

fn intersectSphere(ro : vec3<f32>, rd : vec3<f32>, center : vec3<f32>, radius : f32) -> vec2<f32> {
  let oc = ro - center;
  let b = dot(oc, rd);
  let c = dot(oc, oc) - radius * radius;
  let h = b * b - c;
  if (h < 0.0) { return vec2<f32>(-1.0, -1.0); }
  let s = sqrt(h);
  return vec2<f32>(-b - s, -b + s);
}

@fragment
fn fsMain(in : VsOut) -> @location(0) vec4<f32> {
  let aspect = u.camRight.w;
  let tanHalfFov = u.camUp.w;
  let time = u.camForward.w;
  let quality = i32(u.nebulaA.w + 0.5);
  let octaves = select(4, 3, quality == 0);

  let rd = normalize(
    u.camForward.xyz +
    u.camRight.xyz * (in.uv.x * aspect * tanHalfFov) +
    u.camUp.xyz * (in.uv.y * tanHalfFov)
  );

  // --- Hyperspace Warp Tunnel (when jumping between star systems) ---
  let jp = u.jumpParams.x;
  if (jp > 0.001) {
    let p = vec2<f32>(in.uv.x * aspect, in.uv.y);
    let r = max(0.02, length(p));
    let ang = atan2(p.y, p.x);
    let tunnelDepth = 1.6 / r - time * 11.0 - jp * 18.0;
    let swirl = fbm(vec3<f32>(cos(ang * 3.0) * 1.4, sin(ang * 3.0) * 1.4, tunnelDepth * 0.45), 3);
    let ribbons = pow(max(0.0, sin(ang * 10.0 + tunnelDepth * 1.2 + swirl * 4.0) * 0.5 + 0.5), 3.0);
    let rings = pow(max(0.0, sin(tunnelDepth * 2.2) * 0.5 + 0.5), 4.0);

    let colA = vec3<f32>(0.18, 0.85, 0.98);
    let colB = vec3<f32>(1.0, 0.62, 0.36);
    let colC = vec3<f32>(0.68, 0.42, 1.0);
    let palette = mix(mix(colA, colC, swirl), colB, ribbons * 0.7);

    let edgeBoost = smoothstep(0.05, 0.95, r);
    let coreGlow = exp(-r * 3.8) * vec3<f32>(1.0, 0.96, 0.88) * 2.8;
    let flash = smoothstep(0.82, 1.0, jp) * 3.2 + smoothstep(0.18, 0.0, jp) * 1.2;
    let tunnelCol = palette * (0.35 + ribbons * 1.65 + rings * 0.85) * edgeBoost + coreGlow + vec3<f32>(flash);
    let fade = smoothstep(0.0, 0.12, jp) * (1.0 - smoothstep(0.92, 1.0, jp) * 0.15);
    return vec4<f32>(tunnelCol * fade, 1.0);
  }

  let starPos = u.starPosRad.xyz;
  let starRad = u.starPosRad.w;
  let starKind = i32(u.starColor.w + 0.5);

  // Gravitational lensing deflection for Black Hole systems (starKind == 4)
  var bgDir = rd;
  let toStar = starPos;
  let starDist = length(toStar);
  let starDir = toStar / max(starDist, 0.001);
  let closestT = max(0.0, dot(toStar, rd));
  let closestPt = rd * closestT - toStar;
  let impact = length(closestPt);

  if (starKind == 4 && impact > starRad * 0.55) {
    let bend = clamp((starRad * starRad * 1.45) / (impact * impact + 1.0), 0.0, 0.95);
    bgDir = normalize(rd - normalize(closestPt) * bend * 0.62);
  }

  var color = sampleBackground(bgDir, time, octaves);
  var bestT = 1e9;

  // --- Primary Star / Pulsar / Black Hole ---
  let starHit = intersectSphere(vec3<f32>(0.0), rd, starPos, starRad);

  if (starKind == 4) {
    // Geodesic Black Hole: event horizon + photon ring + Doppler accretion disk
    let horizonRad = starRad * 0.72;
    let hHit = intersectSphere(vec3<f32>(0.0), rd, starPos, horizonRad);

    // Accretion disk plane tilted slightly
    let diskNormal = normalize(vec3<f32>(0.18, 0.94, 0.28));
    let denom = dot(rd, diskNormal);
    var diskGlow = vec3<f32>(0.0);
    if (abs(denom) > 0.0005) {
      let tDisk = dot(starPos, diskNormal) / denom;
      if (tDisk > 0.0 && (hHit.x < 0.0 || tDisk < hHit.x)) {
        let hitP = rd * tDisk - starPos;
        let r = length(hitP);
        if (r > horizonRad * 1.22 && r < starRad * 3.8) {
          let uRad = (r - horizonRad * 1.22) / (starRad * 2.58);
          let angle = atan2(hitP.z, hitP.x);
          let swirl = fbm(vec3<f32>(cos(angle * 2.0 + time * 0.8) * 2.0, r * 0.045, sin(angle * 2.0 + time * 0.8) * 2.0), 3);
          // Relativistic Doppler beaming (brighter on approaching side)
          let tangent = normalize(cross(diskNormal, hitP));
          let doppler = clamp(0.65 + 0.55 * dot(tangent, -rd), 0.25, 1.45);
          let fade = smoothstep(0.0, 0.14, uRad) * (1.0 - smoothstep(0.45, 1.0, uRad));
          let hot = mix(vec3<f32>(1.0, 0.42, 0.18), vec3<f32>(1.0, 0.92, 0.72), doppler * 0.72);
          diskGlow = hot * fade * (0.65 + 1.15 * swirl) * doppler * 2.4;
        }
      }
    }

    // Lensed upper/lower halo around the event horizon
    let ringDist = abs(impact - horizonRad * 1.12) / (starRad * 0.16);
    let photonRing = exp(-ringDist * ringDist) * 2.6;
    let halo = exp(-max(0.0, impact - horizonRad) / (starRad * 0.55)) * 0.85;

    if (hHit.x > 0.0) {
      color = vec3<f32>(0.002, 0.003, 0.008);
      bestT = hHit.x;
    }
    color += vec3<f32>(1.0, 0.82, 0.55) * photonRing + u.starColor.rgb * halo + diskGlow;
  } else {
    // Glowing volumetric star corona + warm anamorphic lens flare streak
    let coronaD = max(0.0, impact - starRad) / (starRad * 1.5);
    let corona = exp(-coronaD * 2.4) * 1.45 + exp(-coronaD * 7.5) * 2.1;
    let starAlign = max(0.0, dot(rd, starDir));
    let flareX = exp(-abs(dot(rd - starDir, u.camUp.xyz)) * 42.0) * pow(starAlign, 18.0) * 0.75;
    color += u.starColor.rgb * (corona + flareX);

    // Pulsar helical twin synchrotron jets (starKind == 3)
    if (starKind == 3) {
      let spinA = time * 1.25;
      let jetAxis = normalize(vec3<f32>(sin(spinA) * 0.35, 0.92, cos(spinA) * 0.35));
      let proj = dot(closestPt, jetAxis);
      let perp = length(closestPt - jetAxis * proj);
      let jetWidth = starRad * (0.14 + abs(proj) * 0.0012);
      let jetCore = exp(-(perp * perp) / max(1.0, jetWidth * jetWidth));
      let jetFade = exp(-abs(proj) / (starRad * 9.5));
      let pulse = 0.75 + 0.25 * sin(abs(proj) * 0.05 - time * 7.0);
      color += vec3<f32>(0.42, 0.92, 1.0) * jetCore * jetFade * pulse * 2.8;
    }

    if (starHit.x > 0.0) {
      let hp = rd * starHit.x;
      let n = normalize(hp - starPos);
      let gran = fbm(n * 6.5 + vec3<f32>(time * 0.08), 3);
      let limb = pow(max(0.0, dot(n, -rd)), 0.45);
      let surf = mix(u.starColor.rgb * 0.85, vec3<f32>(1.0, 0.98, 0.92), 0.35 + 0.65 * gran);
      color = surf * (1.35 + 1.45 * limb);
      bestT = starHit.x;
    }
  }

  // --- Planets & Dual-Shadowed Rings ---
  let pCount = min(6, i32(u.nebulaB.w + 0.5));
  for (var i = 0; i < pCount; i = i + 1) {
    let pl = u.planets[i];
    let pCenter = pl.posRadius.xyz;
    let pRad = pl.posRadius.w;
    let toLight = normalize(starPos - pCenter);

    // Subtle atmospheric limb glow around planet
    let pClosestT = max(0.0, dot(pCenter, rd));
    let pImpact = length(rd * pClosestT - pCenter);
    if (pClosestT < bestT && pImpact > pRad * 0.95 && pImpact < pRad * 1.24) {
      let rimT = (pImpact - pRad) / (pRad * 0.24);
      let rimDir = normalize(rd * pClosestT - pCenter);
      let sunSide = smoothstep(-0.25, 0.75, dot(rimDir, toLight));
      let glow = exp(-max(0.0, rimT) * 5.2) * (0.25 + 0.85 * sunSide);
      color += pl.atmoRing.rgb * glow * 0.85;
    }

    // Ring intersection (rendered back-to-front relative to planet surface)
    let hasRings = pl.colorB.w > 0.5;
    let tilt = pl.atmoRing.w;
    let ringNormal = normalize(vec3<f32>(sin(tilt) * 0.4, cos(tilt), sin(tilt) * 0.9));

    var ringT = -1.0;
    var ringCol = vec3<f32>(0.0);
    var ringAlpha = 0.0;

    if (hasRings) {
      let denom = dot(rd, ringNormal);
      if (abs(denom) > 0.0005) {
        let t = dot(pCenter, ringNormal) / denom;
        if (t > 0.0 && t < bestT) {
          let rp = rd * t - pCenter;
          let r = length(rp);
          if (r > pl.ringData.x && r < pl.ringData.y) {
            let uR = (r - pl.ringData.x) / max(0.001, pl.ringData.y - pl.ringData.x);
            let bands = 0.55 + 0.45 * sin(uR * 42.0 + sin(uR * 11.0) * 2.5);
            let gap = smoothstep(0.02, 0.06, abs(uR - 0.62));
            let edge = smoothstep(0.0, 0.08, uR) * (1.0 - smoothstep(0.9, 1.0, uR));
            // Planet shadow cast onto rings
            let shadowHit = intersectSphere(rp, toLight, vec3<f32>(0.0), pRad * 0.99);
            let lit = select(1.0, 0.12, shadowHit.x > 0.0);
            ringAlpha = clamp(bands * gap * edge * 0.78, 0.0, 0.88);
            ringCol = pl.ringColor.rgb * (0.75 + 0.35 * bands) * lit * u.starColor.rgb;
            ringT = t;
          }
        }
      }
    }

    // Planet sphere intersection
    let pHit = intersectSphere(vec3<f32>(0.0), rd, pCenter, pRad);

    // If ring is behind planet, composite ring first
    if (ringAlpha > 0.01 && (pHit.x < 0.0 || ringT > pHit.x)) {
      color = mix(color, ringCol, ringAlpha);
    }

    if (pHit.x > 0.0 && pHit.x < bestT) {
      let hp = rd * pHit.x;
      let n = normalize(hp - pCenter);
      let ndl = dot(n, toLight);
      let diffuse = smoothstep(-0.12, 0.92, ndl);

      // Ring shadow cast onto planet surface
      var ringShadow = 1.0;
      if (hasRings) {
        let sDenom = dot(toLight, ringNormal);
        if (abs(sDenom) > 0.001) {
          let st = dot(-n * pRad, ringNormal) / sDenom;
          if (st > 0.0) {
            let sr = length(n * pRad + toLight * st);
            if (sr > pl.ringData.x && sr < pl.ringData.y) {
              let su = (sr - pl.ringData.x) / max(0.001, pl.ringData.y - pl.ringData.x);
              ringShadow = 0.42 + 0.35 * sin(su * 36.0);
            }
          }
        }
      }

      let isGiant = pl.colorA.w > 0.5;
      var albedo = pl.colorA.rgb;
      var spec = 0.0;

      if (isGiant) {
        // Swirling gas giant storm bands
        let swirl = fbm(n * 4.2 + vec3<f32>(time * 0.02, 0.0, 0.0), 3);
        let lat = n.y * 9.0 + swirl * 2.6;
        let bandMix = 0.5 + 0.5 * sin(lat);
        albedo = mix(pl.colorA.rgb, pl.colorB.rgb, bandMix);
      } else {
        // Continents, oceans & drifting cloud wisps
        let elev = fbm(n * 3.2 + vec3<f32>(pl.ringData.z * 7.1), 4);
        let landMask = smoothstep(0.47, 0.54, elev);
        albedo = mix(pl.colorB.rgb, pl.colorA.rgb, landMask);

        // Specular highlight on oceans
        let halfV = normalize(toLight - rd);
        spec = pow(max(0.0, dot(n, halfV)), 28.0) * (1.0 - landMask) * 0.45 * diffuse;

        // Soft drifting cloud layer
        let clouds = fbm(n * 5.4 + vec3<f32>(time * 0.015, 0.0, -time * 0.01), 3);
        let cloudMask = smoothstep(0.56, 0.72, clouds) * 0.65;
        albedo = mix(albedo, vec3<f32>(0.97, 0.98, 1.0), cloudMask);
      }

      // Fresnel atmospheric scattering on limb
      let fresnel = pow(1.0 - max(0.0, dot(n, -rd)), 3.2);
      let ambient = u.nebulaA.rgb * 0.09 + vec3<f32>(0.02, 0.03, 0.05);
      var pCol = albedo * (ambient + u.starColor.rgb * diffuse * ringShadow * 1.25) + vec3<f32>(spec);
      pCol += pl.atmoRing.rgb * fresnel * (0.18 + 0.95 * diffuse);

      color = pCol;
      bestT = pHit.x;
    }

    // If ring is in front of planet, composite ring on top
    if (ringAlpha > 0.01 && ringT < bestT) {
      color = mix(color, ringCol, ringAlpha);
    }
  }

  return vec4<f32>(color, 1.0);
}
