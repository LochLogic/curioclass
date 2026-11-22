struct PlanetSurfaceUniforms {
  camPos     : vec4<f32>, // xyz = world pos, w = time
  camRight   : vec4<f32>, // xyz, w = aspect
  camUp      : vec4<f32>, // xyz, w = tanHalfFov
  camForward : vec4<f32>, // xyz, w = reentryHeat (0..1)
  sunDir     : vec4<f32>, // xyz = normalized sun dir, w = seaLevel
  atmoColor  : vec4<f32>, // rgb = atmosphere scatter tint, w = biomeIndex
  colorA     : vec4<f32>, // rgb = primary land albedo, w = seedOffsetX
  colorB     : vec4<f32>, // rgb = secondary / rock albedo, w = seedOffsetZ
  starColor  : vec4<f32>, // rgb = sun light color, w = quality (0..2)
};

@group(0) @binding(0) var<uniform> u : PlanetSurfaceUniforms;

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

fn hash21(p : vec2<f32>) -> f32 {
  var q = fract(vec3<f32>(p.x * 0.1031, p.y * 0.1030, p.x * 0.0973));
  q += dot(q, q.yzx + 33.33);
  return fract((q.x + q.y) * q.z);
}

fn noise2(p : vec2<f32>) -> f32 {
  let i = floor(p);
  let f = fract(p);
  let u2 = f * f * (3.0 - 2.0 * f);
  let a = hash21(i);
  let b = hash21(i + vec2<f32>(1.0, 0.0));
  let c = hash21(i + vec2<f32>(0.0, 1.0));
  let d = hash21(i + vec2<f32>(1.0, 1.0));
  return mix(mix(a, b, u2.x), mix(c, d, u2.x), u2.y);
}

// Matches CPU sampleTerrainHeight() for millimeter-accurate flight & landing
fn terrainHeight(xz : vec2<f32>, octaves : i32) -> f32 {
  let biome = i32(u.atmoColor.w + 0.5);
  let s = (xz + vec2<f32>(u.colorA.w, u.colorB.w)) * 0.0042;

  var h = 0.0;
  var amp = 0.52;
  var freq = 1.0;
  for (var i = 0; i < octaves; i = i + 1) {
    let n = noise2(s * freq);
    if (biome == 6 || biome == 4) {
      let r = 1.0 - abs(n * 2.0 - 1.0);
      h += r * r * amp;
    } else {
      h += n * amp;
    }
    freq *= 2.07;
    amp *= 0.48;
  }

  var height = (h - 0.44) * 128.0;
  if (biome == 1) { height -= 14.0; }
  if (biome == 2) { height = (h - 0.36) * 72.0 + sin(s.x * 9.0 + s.y * 3.0) * 4.5; }
  if (biome == 6) {
    let st = floor(height / 18.0) * 18.0;
    height = st + (height - st) * 0.35 + 16.0;
  }
  if (biome == 9) { height = (h - 0.42) * 85.0 + 12.0; }
  return height;
}

fn terrainNormal(xz : vec2<f32>, eps : f32, octaves : i32) -> vec3<f32> {
  let hL = terrainHeight(xz - vec2<f32>(eps, 0.0), octaves);
  let hR = terrainHeight(xz + vec2<f32>(eps, 0.0), octaves);
  let hD = terrainHeight(xz - vec2<f32>(0.0, eps), octaves);
  let hU = terrainHeight(xz + vec2<f32>(0.0, eps), octaves);
  return normalize(vec3<f32>(hL - hR, 2.0 * eps, hD - hU));
}

// Physically-inspired Rayleigh + Mie atmospheric scattering (no inverted-V banding)
fn computeSky(rd : vec3<f32>, sunDir : vec3<f32>, time : f32) -> vec3<f32> {
  let biome = i32(u.atmoColor.w + 0.5);
  let sunElev = sunDir.y;
  let dayFactor = smoothstep(-0.18, 0.25, sunElev);
  let sunsetFactor = exp(-pow((sunElev - 0.06) * 4.5, 2.0));

  let up = max(0.001, rd.y);
  let opticalDepth = exp(-up * 3.2);

  let zenithDay = mix(vec3<f32>(0.09, 0.28, 0.68), u.atmoColor.rgb * 0.55, 0.45);
  let horizonDay = mix(u.atmoColor.rgb * 0.95, vec3<f32>(0.92, 0.95, 1.0), 0.35);
  let horizonSunset = vec3<f32>(1.0, 0.52, 0.26);
  let zenithNight = vec3<f32>(0.015, 0.025, 0.06);

  var sky = mix(zenithDay, horizonDay, opticalDepth);
  sky = mix(sky, mix(zenithDay * 0.65, horizonSunset, pow(opticalDepth, 0.65)), sunsetFactor * 0.85);
  sky = mix(zenithNight, sky, dayFactor);

  // Airless crater moon has darker space sky with faint horizon haze
  if (biome == 9) {
    sky = mix(vec3<f32>(0.01, 0.014, 0.03), u.atmoColor.rgb * 0.14, opticalDepth * dayFactor);
  }

  // Smooth Henyey-Greenstein Mie forward scattering around the sun
  let cosTheta = dot(rd, sunDir);
  let g = 0.78;
  let mie = (1.0 - g * g) / (4.0 * 3.14159 * pow(max(0.05, 1.0 + g * g - 2.0 * g * cosTheta), 1.5));
  let sunTint = mix(vec3<f32>(1.0, 0.55, 0.24), u.starColor.rgb, smoothstep(-0.02, 0.38, sunElev));
  sky += sunTint * mie * (0.28 + 0.45 * sunsetFactor) * smoothstep(-0.14, 0.08, sunElev);

  // Crisp solar disc
  let sunDisc = smoothstep(0.9982, 0.9994, cosTheta) * smoothstep(-0.05, 0.04, sunElev);
  sky += sunTint * sunDisc * 9.0;

  // Twinkling stars at night or high altitude
  let altFade = smoothstep(140.0, 440.0, u.camPos.y);
  let starVis = clamp((1.0 - dayFactor) * 0.9 + altFade * 0.85 + select(0.0, 0.8, biome == 9), 0.0, 1.0);
  if (starVis > 0.05 && rd.y > 0.0) {
    let sc = floor(rd * 140.0);
    let rnd = hash21(sc.xz + sc.y * 19.3);
    if (rnd > 0.982) {
      sky += vec3<f32>(0.9, 0.95, 1.0) * starVis * (0.6 + 0.4 * sin(time * 2.5 + rnd * 50.0)) * 1.4;
    }
  }

  // Dancing Auroras on Aurora-Ice worlds (biome == 3) or at twilight
  if ((biome == 3 || dayFactor < 0.45) && rd.y > 0.06) {
    let ap = rd.xz / (rd.y + 0.22);
    let wave = sin(ap.x * 2.4 + time * 0.45 + noise2(ap * 1.5) * 3.0);
    let curtain = exp(-abs(wave) * 4.5) * smoothstep(0.06, 0.32, rd.y) * smoothstep(0.85, 0.25, rd.y);
    let aurCol = mix(vec3<f32>(0.18, 0.96, 0.68), vec3<f32>(0.55, 0.35, 1.0), 0.5 + 0.5 * sin(ap.y * 2.0 + time * 0.3));
    let strength = select(0.28 * (1.0 - dayFactor), 0.68, biome == 3);
    sky += aurCol * curtain * strength;
  }

  return sky;
}

// True 3D Volumetric Raymarched Clouds (fly beneath, through, and above sculpted 3D puffs!)
fn sampleClouds(ro : vec3<f32>, rd : vec3<f32>, sunDir : vec3<f32>, time : f32) -> vec4<f32> {
  let biome = i32(u.atmoColor.w + 0.5);
  if (biome == 9) { return vec4<f32>(0.0); }

  let cBot = 215.0;
  let cTop = 315.0;
  if (abs(rd.y) < 0.008 && (ro.y < cBot || ro.y > cTop)) { return vec4<f32>(0.0); }

  var tStart = 0.0;
  var tEnd = 0.0;
  if (abs(rd.y) >= 0.008) {
    let t0 = (cBot - ro.y) / rd.y;
    let t1 = (cTop - ro.y) / rd.y;
    tStart = max(0.0, min(t0, t1));
    tEnd = min(5600.0, max(t0, t1));
  } else {
    tStart = 10.0;
    tEnd = 1600.0;
  }
  if (tEnd <= tStart) { return vec4<f32>(0.0); }

  let dayF = smoothstep(-0.12, 0.25, sunDir.y);
  let sunsetF = exp(-pow((sunDir.y - 0.06) * 4.5, 2.0));
  let silver = pow(max(0.0, dot(rd, sunDir)), 7.0) * 1.1;

  let steps = select(6, 4, i32(u.starColor.w + 0.5) == 0);
  let stepLen = (tEnd - tStart) / f32(steps);
  var trans = 1.0;
  var accum = vec3<f32>(0.0);

  let shadowTint = mix(vec3<f32>(0.14, 0.18, 0.30), vec3<f32>(0.46, 0.55, 0.72), dayF);
  let brightTint = mix(vec3<f32>(0.24, 0.28, 0.42), vec3<f32>(0.99, 0.99, 1.0), dayF);

  for (var i = 0; i < steps; i = i + 1) {
    let t = tStart + (f32(i) + 0.5) * stepLen;
    let p = ro + rd * t;
    let hFrac = clamp((p.y - cBot) / (cTop - cBot), 0.0, 1.0);
    // Vertical rounded cumulus profile (flat base, billowy rounded top)
    let hShape = smoothstep(0.0, 0.22, hFrac) * smoothstep(1.0, 0.35, hFrac);

    let uv = p.xz * 0.00145 + vec2<f32>(time * 0.012, time * 0.006);
    let n1 = noise2(uv + vec2<f32>(hFrac * 0.35, -hFrac * 0.25));
    let n2 = noise2(uv * 2.4 + vec2<f32>(4.1, 2.7));
    let n3 = noise2(uv * 5.3 - vec2<f32>(1.9, 6.3));
    let rawD = (n1 * 0.54 + n2 * 0.30 + n3 * 0.16) * hShape;
    let dens = smoothstep(0.26, 0.62, rawD);

    if (dens > 0.01) {
      // Sunward self-shadowing sample for volumetric 3D shading
      let sunUv = uv + sunDir.xz * 0.16;
      let nSun = noise2(sunUv) * 0.6 + noise2(sunUv * 2.4 + vec2<f32>(4.1, 2.7)) * 0.4;
      let light = clamp(1.05 - (nSun - 0.36) * 1.45 + hFrac * 0.28, 0.22, 1.0);
      let powder = 1.0 - exp(-dens * 3.2);
      var col = mix(shadowTint, brightTint, light * (0.55 + 0.45 * powder));
      col = mix(col, vec3<f32>(1.0, 0.60, 0.34), sunsetF * 0.78);
      col += u.starColor.rgb * silver * dayF * (0.45 + 0.55 * powder);

      let distFade = exp(-t * 0.00024);
      let alpha = clamp(dens * distFade * 0.55, 0.0, 0.92);
      accum += trans * col * alpha;
      trans *= (1.0 - alpha);
      if (trans < 0.04) { break; }
    }
  }

  return vec4<f32>(accum / max(0.001, 1.0 - trans), 1.0 - trans);
}

// Soft terrain shadow march
fn softShadow(ro : vec3<f32>, sunDir : vec3<f32>) -> f32 {
  if (sunDir.y < 0.02) { return 0.15; }
  var res = 1.0;
  var t = 4.0;
  for (var i = 0; i < 10; i = i + 1) {
    let p = ro + sunDir * t;
    let h = terrainHeight(p.xz, 4);
    let diff = p.y - h;
    if (diff < 0.0) { return 0.22; }
    res = min(res, 6.0 * diff / t);
    t += clamp(diff * 0.65, 6.0, 48.0);
  }
  return clamp(res, 0.22, 1.0);
}

struct FragOut {
  @location(0) color : vec4<f32>,
  @builtin(frag_depth) depth : f32,
};

@fragment
fn fsMain(in : VsOut) -> FragOut {
  let aspect = u.camRight.w;
  let tanHalfFov = u.camUp.w;
  let time = u.camPos.w;
  let reentry = u.camForward.w;
  let seaLevel = u.sunDir.w;
  let biome = i32(u.atmoColor.w + 0.5);
  let quality = i32(u.starColor.w + 0.5);
  let maxSteps = select(select(96, 68, quality == 0), 120, quality == 2);
  let octaves = select(5, 4, quality == 0);

  let ro = u.camPos.xyz;
  let rd = normalize(
    u.camForward.xyz +
    u.camRight.xyz * (in.uv.x * aspect * tanHalfFov) +
    u.camUp.xyz * (in.uv.y * tanHalfFov)
  );
  let sunDir = normalize(u.sunDir.xyz);
  let dayFactor = smoothstep(-0.16, 0.22, sunDir.y);

  var skyCol = computeSky(rd, sunDir, time);
  // Soft sunlit Rainbow arc opposite the sun on lush/ocean worlds!
  if ((biome == 0 || biome == 1 || biome == 8) && dayFactor > 0.35 && rd.y > 0.02) {
    let antiSun = dot(rd, -sunDir);
    let bowDist = abs(antiSun - 0.743); // ~42 degrees optical rainbow angle!
    if (bowDist < 0.045) {
      let tBow = clamp((antiSun - 0.705) / 0.075, 0.0, 1.0);
      let bowCol = vec3<f32>(
        smoothstep(0.55, 0.15, tBow),
        sin(tBow * 3.14159),
        smoothstep(0.35, 0.88, tBow)
      );
      let bowMask = (1.0 - bowDist / 0.045) * smoothstep(0.02, 0.18, rd.y) * 0.24 * dayFactor;
      skyCol += bowCol * bowMask;
    }
  }

  // Shooting stars / meteors streaking across twilight & night skies!
  if (dayFactor < 0.45 && rd.y > 0.1) {
    let mPeriod = floor(time * 0.28);
    let mFrac = fract(time * 0.28);
    if (mFrac < 0.22) {
      let mSeed = hash21(vec2<f32>(mPeriod, 13.7));
      let mStart = vec2<f32>(mSeed * 1.4 - 0.7, 0.42 + fract(mSeed * 7.3) * 0.35);
      let mHead = mStart + vec2<f32>(0.55, -0.28) * (mFrac / 0.22);
      let sp = vec2<f32>(in.uv.x * aspect, in.uv.y);
      let dLine = length(sp - mHead);
      let streak = exp(-dLine * 42.0) * (1.0 - mFrac / 0.22) * (1.0 - dayFactor);
      skyCol += vec3<f32>(0.9, 0.96, 1.0) * streak * 2.4;
    }
  }

  let clouds = sampleClouds(ro, rd, sunDir, time);
  skyCol = mix(skyCol, clouds.rgb, clouds.a);

  // Raymarch terrain
  var t = 1.0;
  var hit = false;
  let maxDist = 2600.0;
  for (var i = 0; i < maxSteps; i = i + 1) {
    let p = ro + rd * t;
    let h = terrainHeight(p.xz, 4);
    let d = p.y - h;
    if (d < 0.004 * t) {
      hit = true;
      break;
    }
    t += max(0.75, d * 0.52);
    if (t > maxDist || (p.y > 220.0 && rd.y > 0.05)) { break; }
  }

  // Analytical ocean plane intersection
  var waterT = 1e9;
  if (seaLevel > -500.0 && rd.y < -0.0005 && ro.y > seaLevel) {
    let wt = (seaLevel - ro.y) / rd.y;
    if (wt > 0.0 && wt < maxDist) {
      waterT = wt;
    }
  }

  var color = skyCol;
  var hitDist = maxDist;

  if (waterT < t || (!hit && waterT < maxDist)) {
    // --- Spectral Ocean Shader ---
    hitDist = waterT;
    let wp = ro + rd * waterT;
    let bedH = terrainHeight(wp.xz, 4);
    let depth = max(0.0, seaLevel - bedH);

    // Multi-directional animated Gerstner-inspired wave ripples
    let w1 = noise2(wp.xz * 0.14 + vec2<f32>(time * 0.65, time * 0.35));
    let w2 = noise2(wp.xz * 0.31 - vec2<f32>(time * 0.45, -time * 0.55));
    let w3 = noise2(wp.xz * 0.72 + vec2<f32>(-time * 0.9, time * 0.4));
    let eps = 0.6;
    let wx = noise2((wp.xz + vec2<f32>(eps, 0.0)) * 0.14 + vec2<f32>(time * 0.65, time * 0.35)) - w1;
    let wz = noise2((wp.xz + vec2<f32>(0.0, eps)) * 0.14 + vec2<f32>(time * 0.65, time * 0.35)) - w1;
    let waveN = normalize(vec3<f32>(wx * 0.65 + (w2 - 0.5) * 0.16, 1.0, wz * 0.65 + (w3 - 0.5) * 0.16));

    let reflDir = reflect(rd, waveN);
    let skyRefl = computeSky(vec3<f32>(reflDir.x, max(0.01, reflDir.y), reflDir.z), sunDir, time);
    let fresnel = 0.04 + 0.96 * pow(1.0 - max(0.0, dot(waveN, -rd)), 4.2);

    // Beer-Lambert depth absorption (turquoise shallows -> deep ocean) + sunlit shallow caustics!
    let shallow = select(vec3<f32>(0.12, 0.72, 0.78), vec3<f32>(0.98, 0.36, 0.10), biome == 7);
    let deep = select(vec3<f32>(0.02, 0.12, 0.28), vec3<f32>(0.24, 0.05, 0.04), biome == 7);
    let caustic = pow(max(0.0, sin(wp.x * 0.7 + time * 1.6 + w2 * 5.0) * sin(wp.z * 0.7 - time * 1.3 + w3 * 5.0)), 3.0);
    let shallowMask = exp(-depth * 0.16) * select(1.0, 0.0, biome == 7);
    let waterBody = (mix(shallow, deep, 1.0 - exp(-depth * 0.095)) + vec3<f32>(0.28, 0.55, 0.58) * caustic * shallowMask * 0.65) * (0.28 + 0.92 * dayFactor);

    // Sparkling sun specular path
    let halfV = normalize(sunDir - rd);
    let spec = pow(max(0.0, dot(waveN, halfV)), 140.0) * 3.8 * dayFactor;
    let broadSpec = pow(max(0.0, dot(waveN, halfV)), 22.0) * 0.45 * dayFactor;

    // Animated shoreline foam
    let foamWave = sin(depth * 2.2 - time * 2.6 + w2 * 4.0) * 0.5 + 0.5;
    let foam = smoothstep(3.2, 0.2, depth) * (0.55 + 0.45 * foamWave) * select(0.85, 0.3, biome == 7);

    var wCol = mix(waterBody, skyRefl, clamp(fresnel * 0.88, 0.0, 0.92));
    wCol += u.starColor.rgb * (spec + broadSpec);
    wCol = mix(wCol, vec3<f32>(0.94, 0.97, 1.0) * (0.35 + 0.75 * dayFactor), foam);

    // Glowing magma ocean on volcanic worlds
    if (biome == 7) {
      wCol += vec3<f32>(1.0, 0.38, 0.08) * (0.65 + 0.5 * w1);
    }
    color = wCol;
  } else if (hit) {
    // --- Triplanar PBR Eroded Terrain Shader ---
    hitDist = t;
    let p = ro + rd * t;
    let baseN = terrainNormal(p.xz, clamp(t * 0.0028, 0.35, 3.2), octaves);
    // Crisp high-frequency micro-normal perturbation so ground looks rich & tactile up close!
    let mA = noise2(p.xz * 0.95);
    let mB = noise2(p.xz * 0.95 + vec2<f32>(0.4, 0.0));
    let mC = noise2(p.xz * 0.95 + vec2<f32>(0.0, 0.4));
    let detailFade = exp(-t * 0.0045);
    let n = normalize(baseN + vec3<f32>((mA - mB) * 0.45, 0.0, (mA - mC) * 0.45) * detailFade);
    let slope = 1.0 - baseN.y;
    let micro = noise2(p.xz * 0.35) * 0.55 + mA * 0.30 + noise2(p.xz * 2.8) * 0.15;

    // Layered rock strata on cliffs
    let strata = 0.82 + 0.18 * sin(p.y * 0.55 + micro * 3.0);
    let rockCol = mix(u.colorB.rgb * 0.65, vec3<f32>(0.42, 0.39, 0.37), 0.45) * strata;
    let sandCol = vec3<f32>(0.88, 0.79, 0.60);
    let snowCol = vec3<f32>(0.94, 0.97, 1.0);

    var albedo = mix(u.colorA.rgb, u.colorA.rgb * 0.78 + u.colorB.rgb * 0.22, micro);

    // Sandy shorelines near sea level
    if (seaLevel > -500.0 && biome != 7 && biome != 3) {
      let beach = smoothstep(7.5, 0.8, p.y - seaLevel) * smoothstep(0.45, 0.1, slope);
      albedo = mix(albedo, sandCol, beach * 0.85);
    }

    // Cliff rock strata on steep slopes
    let cliffMask = smoothstep(0.24, 0.52, slope);
    albedo = mix(albedo, rockCol, cliffMask);

    // High-altitude snowcaps
    if (biome != 2 && biome != 7 && biome != 9) {
      let snowMask = smoothstep(46.0, 68.0, p.y) * smoothstep(0.55, 0.2, slope);
      albedo = mix(albedo, snowCol, snowMask * 0.88);
    }

    // Lighting: directional sun + soft terrain shadows + hemisphere sky fill
    let ndl = max(0.0, dot(n, sunDir));
    let shadow = select(1.0, softShadow(p + n * 0.8, sunDir), quality > 0 && dayFactor > 0.05);

    // Drifting cloud shadow projected on ground
    let cShadowN = noise2(p.xz * 0.0014 + vec2<f32>(time * 0.012, time * 0.006));
    let cloudShadow = mix(1.0, 0.68, smoothstep(0.52, 0.74, cShadowN) * select(1.0, 0.0, biome == 9));

    let sunTint = mix(vec3<f32>(1.0, 0.56, 0.28), u.starColor.rgb, smoothstep(-0.02, 0.35, sunDir.y));
    let skyAmbient = mix(vec3<f32>(0.05, 0.07, 0.14), u.atmoColor.rgb * 0.36 + vec3<f32>(0.12, 0.14, 0.18), dayFactor);
    let bounce = u.colorA.rgb * 0.08 * dayFactor;

    var lit = albedo * (skyAmbient * (0.55 + 0.45 * n.y) + bounce + sunTint * ndl * shadow * cloudShadow * 1.45 * dayFactor);

    // Bioluminescent crystal veins / magma cracks at night!
    if (biome == 4 && micro > 0.72) {
      lit += vec3<f32>(0.45, 0.88, 1.0) * (micro - 0.72) * 3.2;
    }
    if (biome == 7 && micro < 0.26 && p.y < 14.0) {
      lit += vec3<f32>(1.0, 0.38, 0.08) * (0.26 - micro) * 5.0;
    }
    color = lit;
  }

  // Aerial perspective + subtle golden-hour crepuscular sunbeams!
  if (hitDist < maxDist) {
    let fogDensity = select(0.00052, 0.00014, biome == 9);
    let fog = 1.0 - exp(-hitDist * fogDensity);
    let hazeCol = computeSky(normalize(vec3<f32>(rd.x, max(0.02, rd.y + 0.06), rd.z)), sunDir, time);
    color = mix(color, hazeCol, clamp(fog * 0.92, 0.0, 0.94));
  }

  // Subtle volumetric sunbeam glow when looking near the sun over mountains
  let sunAlign = pow(max(0.0, dot(rd, sunDir)), 10.0);
  if (sunAlign > 0.02 && sunDir.y > -0.05 && biome != 9) {
    let shaftNoise = 0.65 + 0.35 * sin(atan2(rd.y - sunDir.y, rd.x - sunDir.x) * 9.0 + time * 0.25);
    let beamStrength = sunAlign * shaftNoise * (0.22 + 0.35 * exp(-pow((sunDir.y - 0.12) * 3.5, 2.0)));
    color += mix(vec3<f32>(1.0, 0.72, 0.42), u.starColor.rgb, 0.45) * beamStrength * select(0.35, 0.85, hitDist > 120.0);
  }

  // Dynamic atmospheric weather: rain streaks on mist-forest, snowfall on aurora-ice, fireflies on warm worlds!
  if (ro.y < 140.0 && biome != 9) {
    if (biome == 8) {
      // Gentle shimmering rain streaks
      let rUv = vec2<f32>(in.uv.x * aspect * 28.0 + in.uv.y * 4.0, in.uv.y * 6.0 + time * 5.2);
      let rCell = floor(rUv);
      let rf = fract(rUv);
      let rr = hash21(rCell);
      if (rr > 0.84) {
        let drop = smoothstep(0.08, 0.0, abs(rf.x - 0.5)) * smoothstep(0.0, 0.4, rf.y) * smoothstep(1.0, 0.5, rf.y);
        color += vec3<f32>(0.72, 0.86, 0.98) * drop * 0.28;
      }
    } else if (biome == 3) {
      // Soft falling snowflakes
      let sUv = in.uv * vec2<f32>(aspect, 1.0) * 14.0 + vec2<f32>(sin(time * 0.7) * 0.8, time * 1.45);
      let sCell = floor(sUv);
      let sf = fract(sUv) - 0.5;
      if (hash21(sCell) > 0.82) {
        let flake = exp(-dot(sf, sf) * 65.0);
        color += vec3<f32>(0.92, 0.97, 1.0) * flake * 0.55;
      }
    } else if (ro.y < 85.0) {
      // Drifting glowing fireflies / sunlit pollen motes
      let moteUv = in.uv * vec2<f32>(aspect, 1.0) * 7.5 + vec2<f32>(time * 0.22, -time * 0.14);
      let cell = floor(moteUv);
      let f = fract(moteUv) - 0.5;
      let rnd = hash21(cell);
      if (rnd > 0.88) {
        let drift = vec2<f32>(sin(time * 1.4 + rnd * 20.0), cos(time * 1.1 + rnd * 30.0)) * 0.25;
        let md = length(f - drift);
        let glow = exp(-md * md * 95.0) * (0.55 + 0.45 * sin(time * 3.2 + rnd * 40.0));
        color += vec3<f32>(1.0, 0.92, 0.55) * glow * (1.0 - smoothstep(45.0, 85.0, ro.y)) * mix(1.4, 0.45, dayFactor);
      }
    }
  }

  // Warm atmospheric reentry plasma glow around screen edges during descent
  if (reentry > 0.01) {
    let edge = smoothstep(0.35, 1.15, length(in.uv));
    let flicker = 0.78 + 0.22 * noise2(in.uv * 6.0 + vec2<f32>(0.0, time * 14.0));
    let plasma = mix(vec3<f32>(1.0, 0.42, 0.12), vec3<f32>(1.0, 0.82, 0.42), flicker);
    color += plasma * edge * reentry * 1.15;
  }

  // Write exact WebGPU [0, 1] perspective depth (near=0.5, far=2600.0) so 3D flora/critters occlude behind hills
  var outDepth = 0.99999;
  if (hitDist < maxDist) {
    let viewZ = max(0.51, dot(rd, u.camForward.xyz) * hitDist);
    let nearP = 0.5;
    let farP = 2600.0;
    outDepth = clamp((farP / (farP - nearP)) * (1.0 - nearP / viewZ), 0.0, 0.99998);
  }

  var fout : FragOut;
  fout.color = vec4<f32>(color, 1.0);
  fout.depth = outDepth;
  return fout;
}
