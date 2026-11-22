import type { BiomeKind, PlanetData } from './galaxy.ts';
import { clamp } from './math.ts';

export interface PlanetFlightState {
  planet: PlanetData;
  seed: number;
  x: number;
  y: number; // altitude above sea level (sea level = 0)
  z: number;
  vx: number;
  vy: number;
  vz: number;
  yaw: number;   // radians
  pitch: number; // radians
  speed: number;
  altitudeAGL: number;
  seaLevel: number;
  surfaceGravityG: number; // Planet's surface gravity in Earth Gs (0.22G moon .. 1.35G super-earth)
  landed: boolean;
  onFoot: boolean;
  inRover: boolean;
  shipParkedX: number;
  shipParkedY: number;
  shipParkedZ: number;
  shipParkedYaw: number;
  jetpackFuel: number; // 0..100 bouncy jetpack charge
  walkBob: number;
  reentryHeat: number; // 0..1 glowing plasma during high-altitude entry
  sunAngle: number;    // 0..2PI (0.28 = golden sunrise, 1.3 = noon, 2.85 = sunset)
  timeOfDaySpeed: number;
}

export interface PlanetFlightInput {
  forward: number;
  strafe: number;
  vertical: number;
  yawDelta: number;
  pitchDelta: number;
  boost: boolean;
  brake: boolean;
  cruise: boolean;
}

export const ORBIT_EXIT_ALTITUDE = 520;

export const BIOME_INDEX: Record<BiomeKind, number> = {
  'meadow-world': 0,
  'coral-ocean': 1,
  'golden-dunes': 2,
  'aurora-ice': 3,
  'crystal-garden': 4,
  'cloud-giant': 5,
  'amber-canyons': 6,
  'volcanic-ember': 7,
  'mist-forest': 8,
  'crater-moon': 9,
};

export function hasBiomeOcean(biome: BiomeKind): boolean {
  return (
    biome === 'meadow-world' ||
    biome === 'coral-ocean' ||
    biome === 'mist-forest' ||
    biome === 'aurora-ice' ||
    biome === 'volcanic-ember'
  );
}

// Fast deterministic 2D value noise matching planet.wgsl closely for accurate ground clearance
function fract(v: number): number {
  return v - Math.floor(v);
}

function hash21(px: number, pz: number): number {
  let x = fract(px * 0.1031);
  let y = fract(pz * 0.1030);
  let z = fract(px * 0.0973);
  const d = x * (y + 33.33) + y * (z + 33.33) + z * (x + 33.33);
  x += d;
  y += d;
  z += d;
  return fract((x + y) * z);
}

function noise2(x: number, z: number): number {
  const ix = Math.floor(x);
  const iz = Math.floor(z);
  const fx = x - ix;
  const fz = z - iz;
  const ux = fx * fx * (3 - 2 * fx);
  const uz = fz * fz * (3 - 2 * fz);

  const a = hash21(ix, iz);
  const b = hash21(ix + 1, iz);
  const c = hash21(ix, iz + 1);
  const d = hash21(ix + 1, iz + 1);
  return a + (b - a) * ux + (c - a) * uz + (a - b - c + d) * ux * uz;
}

/** Deterministic terrain height (meters above sea level) matching planet.wgsl */
export function sampleTerrainHeight(x: number, z: number, seed: number, biome: BiomeKind): number {
  const ox = (seed % 97) * 13.7;
  const oz = ((seed >> 4) % 89) * 17.3;
  const sx = (x + ox) * 0.0042;
  const sz = (z + oz) * 0.0042;

  let h = 0;
  let amp = 0.52;
  let freq = 1.0;
  for (let i = 0; i < 4; i++) {
    const n = noise2(sx * freq, sz * freq);
    if (biome === 'amber-canyons' || biome === 'crystal-garden') {
      // Ridged / terraced plateaus
      const r = 1.0 - Math.abs(n * 2.0 - 1.0);
      h += r * r * amp;
    } else {
      h += n * amp;
    }
    freq *= 2.07;
    amp *= 0.48;
  }

  let height = (h - 0.44) * 128;
  if (biome === 'coral-ocean') height -= 14;
  if (biome === 'golden-dunes') height = (h - 0.36) * 72 + Math.sin(sx * 9.0 + sz * 3.0) * 4.5;
  if (biome === 'amber-canyons') {
    const step = Math.floor(height / 18) * 18;
    height = step + (height - step) * 0.35 + 16;
  }
  if (biome === 'crater-moon') {
    height = (h - 0.42) * 85 + 12;
  }
  return height;
}

export function computePlanetGravityG(planet: PlanetData): number {
  if (planet.biome === 'crater-moon') return 0.24;
  if (planet.biome === 'crystal-garden') return 0.62;
  if (planet.biome === 'aurora-ice') return 0.78;
  // Scale gently with planet radius (~32 = 1.00 G Earth-like)
  return Number(clamp(planet.radius / 32, 0.45, 1.38).toFixed(2));
}

export function createPlanetFlightState(planet: PlanetData, systemSeed: number): PlanetFlightState {
  const seed = (systemSeed ^ ((planet.id + 1) * 2654435761)) >>> 0;
  // Start gracefully descending through upper atmosphere at golden hour!
  const startY = 310;
  const ground = Math.max(0, sampleTerrainHeight(0, 0, seed, planet.biome));
  return {
    planet,
    seed,
    x: 0,
    y: startY,
    z: 0,
    vx: 0,
    vy: -22,
    vz: -55,
    yaw: 0,
    pitch: -0.22,
    speed: 59,
    altitudeAGL: startY - ground,
    seaLevel: hasBiomeOcean(planet.biome) ? 0 : -999,
    surfaceGravityG: computePlanetGravityG(planet),
    landed: false,
    onFoot: false,
    inRover: false,
    shipParkedX: 0,
    shipParkedY: 0,
    shipParkedZ: 0,
    shipParkedYaw: 0,
    jetpackFuel: 100,
    walkBob: 0,
    reentryHeat: 0.72,
    sunAngle: 0.36, // Warm golden-hour sunrise/sunset angle
    timeOfDaySpeed: 0.012,
  };
}

export function toggleOnFoot(state: PlanetFlightState): { ok: boolean; message: string } {
  if (state.onFoot || state.inRover) {
    // Board parked Starhopper
    state.onFoot = false;
    state.inRover = false;
    state.landed = true;
    state.x = state.shipParkedX;
    state.y = state.shipParkedY + 1.2;
    state.z = state.shipParkedZ;
    state.yaw = state.shipParkedYaw;
    state.pitch = 0;
    state.vx = 0;
    state.vy = 0;
    state.vz = 0;
    return { ok: true, message: 'Back inside your Starhopper! Press G to lift off.' };
  }
  if (!state.landed) {
    return { ok: false, message: 'Touch down on dry land (G) first before stepping outside!' };
  }
  state.onFoot = true;
  state.inRover = false;
  state.shipParkedX = state.x;
  state.shipParkedY = sampleTerrainHeight(state.x, state.z, state.seed, state.planet.biome) + 0.9;
  state.shipParkedZ = state.z;
  state.shipParkedYaw = state.yaw;
  state.x += Math.cos(state.yaw) * 6.5;
  state.z += Math.sin(state.yaw) * 6.5;
  const gH = Math.max(state.seaLevel + 0.5, sampleTerrainHeight(state.x, state.z, state.seed, state.planet.biome));
  state.y = gH + 2.2;
  state.jetpackFuel = 100;
  return { ok: true, message: `Stepped out onto ${state.planet.name}! Hold Space for jetpack, K for Rover, F to scan!` };
}

export function toggleRover(state: PlanetFlightState): { ok: boolean; message: string } {
  if (state.inRover) {
    state.inRover = false;
    state.onFoot = true;
    return { ok: true, message: 'Hopped out of the Explorer Rover! Press E to board ship.' };
  }
  if (!state.landed && !state.onFoot) {
    return { ok: false, message: 'Touch down on dry land (G) first to deploy your Explorer Rover!' };
  }
  if (!state.onFoot) {
    // Deploy straight from landed ship!
    state.shipParkedX = state.x;
    state.shipParkedY = sampleTerrainHeight(state.x, state.z, state.seed, state.planet.biome) + 0.9;
    state.shipParkedZ = state.z;
    state.shipParkedYaw = state.yaw;
    state.x += Math.cos(state.yaw) * 8.0;
    state.z += Math.sin(state.yaw) * 8.0;
  }
  state.onFoot = false;
  state.inRover = true;
  const gH = Math.max(state.seaLevel + 0.5, sampleTerrainHeight(state.x, state.z, state.seed, state.planet.biome));
  state.y = gH + 2.4;
  state.jetpackFuel = 100;
  return { ok: true, message: `🚙 Deployed 6-Wheel Explorer Rover! W/A/S/D to drive, Space for hill-jump boost, K to exit.` };
}

export function toggleLanded(state: PlanetFlightState): { ok: boolean; message: string } {
  if (state.onFoot || state.inRover) {
    return { ok: false, message: 'Board your ship (E) before lifting off!' };
  }
  if (state.landed) {
    state.landed = false;
    state.vy = 26;
    state.y += 4;
    return { ok: true, message: 'Thrusters engaged, lifting off!' };
  }
  const terrainH = sampleTerrainHeight(state.x, state.z, state.seed, state.planet.biome);
  if (terrainH < state.seaLevel + 1.5) {
    return { ok: false, message: 'Fly over dry land to touch down!' };
  }
  if (state.altitudeAGL > 42) {
    return { ok: false, message: `Descend lower to land (${Math.round(state.altitudeAGL)}m; get under 42m).` };
  }
  state.landed = true;
  state.y = terrainH + 2.8;
  state.vx = 0;
  state.vy = 0;
  state.vz = 0;
  state.pitch = 0;
  state.speed = 0;
  return { ok: true, message: `Touched down on ${state.planet.name}! Press G to lift off.` };
}

/** Steps planetary flight; returns `exitToOrbit: true` when player climbs above atmosphere */
export function stepPlanetFlight(
  state: PlanetFlightState,
  input: PlanetFlightInput,
  dt: number,
): { exitToOrbit: boolean } {
  const safeDt = clamp(dt, 0.0001, 0.05);
  state.sunAngle = (state.sunAngle + state.timeOfDaySpeed * safeDt) % (Math.PI * 2);

  state.yaw += input.yawDelta;
  state.pitch = clamp(state.pitch - input.pitchDelta, -1.15, 1.15);

  if (state.onFoot || state.inRover) {
    const cosY = Math.cos(state.yaw);
    const sinY = Math.sin(state.yaw);
    const moveSpeed = state.inRover
      ? (input.boost ? 56 : 36)
      : (input.boost ? 22 : 12.5);
    const fx = sinY;
    const fz = -cosY;
    const rx = cosY;
    const rz = sinY;

    // Rover steers smoothly with A/D as well as mouse drag
    if (state.inRover && Math.abs(input.strafe) > 0.01) {
      state.yaw += input.strafe * 1.95 * safeDt;
    }

    const lateralCmd = state.inRover ? 0 : input.strafe;
    const targetVx = (fx * input.forward + rx * lateralCmd) * moveSpeed;
    const targetVz = (fz * input.forward + rz * lateralCmd) * moveSpeed;
    const accelLerp = state.inRover ? 4.8 : 10.0;
    state.vx += (targetVx - state.vx) * Math.min(1, safeDt * accelLerp);
    state.vz += (targetVz - state.vz) * Math.min(1, safeDt * accelLerp);

    const gravity = -24.0 * state.surfaceGravityG;
    const terrainH = sampleTerrainHeight(state.x, state.z, state.seed, state.planet.biome);
    const eyeHeight = state.inRover ? 3.2 : 2.1;
    const floorY = Math.max(state.seaLevel + 1.2, terrainH + eyeHeight);
    const grounded = state.y <= floorY + 0.35;

    // Bouncy jetpack / Rover hydraulic jump booster!
    const jetting = (input.brake || input.vertical > 0.5) && state.jetpackFuel > 2;
    if (jetting) {
      const lift = (state.inRover ? 42 : 36) + 18 * state.surfaceGravityG;
      state.vy = Math.min(28, state.vy + (lift + gravity) * safeDt);
      state.jetpackFuel = clamp(state.jetpackFuel - 32 * safeDt, 0, 100);
    } else {
      state.vy += gravity * safeDt;
      if (grounded) {
        state.jetpackFuel = clamp(state.jetpackFuel + 52 * safeDt, 0, 100);
      }
    }

    state.x += state.vx * safeDt;
    state.y += state.vy * safeDt;
    state.z += state.vz * safeDt;

    const nextTerrain = sampleTerrainHeight(state.x, state.z, state.seed, state.planet.biome);
    const nextFloor = Math.max(state.seaLevel + 1.2, nextTerrain + eyeHeight);
    if (state.y < nextFloor) {
      state.y = nextFloor;
      state.vy = 0;
    }

    const horizSpd = Math.hypot(state.vx, state.vz);
    state.speed = horizSpd;
    state.altitudeAGL = Math.max(0, state.y - Math.max(state.seaLevel, nextTerrain));
    state.reentryHeat = 0;
    if (grounded && horizSpd > 0.8) {
      state.walkBob += safeDt * horizSpd * (state.inRover ? 0.35 : 0.65);
    }
    return { exitToOrbit: false };
  }

  if (state.landed) {
    // Allow gentle look-around while parked, lift off automatically if pressing Space/R/Boost
    if (input.vertical > 0.5 || input.boost) {
      state.landed = false;
      state.vy = 26;
    } else {
      const groundH = Math.max(state.seaLevel, sampleTerrainHeight(state.x, state.z, state.seed, state.planet.biome));
      state.y = groundH + 2.8;
      state.altitudeAGL = 2.8;
      state.reentryHeat = Math.max(0, state.reentryHeat - safeDt * 1.2);
      return { exitToOrbit: false };
    }
  }

  const cosY = Math.cos(state.yaw);
  const sinY = Math.sin(state.yaw);
  const cosP = Math.cos(state.pitch);
  const sinP = Math.sin(state.pitch);

  // Forward (-Z when yaw=0), Right (+X when yaw=0)
  const fx = sinY * cosP;
  const fy = sinP;
  const fz = -cosY * cosP;
  const rx = cosY;
  const rz = sinY;

  const mult = (input.boost ? 2.1 : 1.0) * (input.cruise ? 1.8 : 1.0);
  const fwdCmd = input.cruise ? Math.max(0.85, input.forward) : input.forward;
  const accel = 85 * mult;

  state.vx += (fx * fwdCmd * accel + rx * input.strafe * 55) * safeDt;
  // Gentle atmospheric gravity pull when gliding (countered smoothly by hover thrusters when braking)
  const airGrav = input.brake ? 0 : -6.5 * state.surfaceGravityG;
  state.vy += (fy * fwdCmd * accel + input.vertical * 58 + airGrav) * safeDt;
  state.vz += (fz * fwdCmd * accel + rz * input.strafe * 55) * safeDt;

  // Smooth aerodynamic drag
  const drag = input.brake ? Math.exp(-5.0 * safeDt) : Math.exp(-1.55 * safeDt);
  state.vx *= drag;
  state.vy *= drag;
  state.vz *= drag;

  const maxSpd = 125 * mult;
  const spd = Math.hypot(state.vx, state.vy, state.vz);
  if (spd > maxSpd) {
    const s = maxSpd / spd;
    state.vx *= s;
    state.vy *= s;
    state.vz *= s;
    state.speed = maxSpd;
  } else {
    state.speed = spd;
  }

  state.x += state.vx * safeDt;
  state.y += state.vy * safeDt;
  state.z += state.vz * safeDt;

  // Gentle auto-hover ground/ocean cushion (kids never crash!)
  const terrainH = sampleTerrainHeight(state.x, state.z, state.seed, state.planet.biome);
  const floorH = Math.max(state.seaLevel + 2.5, terrainH + 4.5);
  if (state.y < floorH) {
    state.y = floorH;
    if (state.vy < 0) state.vy = Math.max(0, -state.vy * 0.2);
  }
  state.altitudeAGL = Math.max(0, state.y - Math.max(state.seaLevel, terrainH));

  // Reentry plasma glows when diving fast through upper atmosphere (> 190m)
  const targetHeat =
    state.y > 185 && state.vy < -6
      ? clamp(((state.y - 185) / 140) * clamp(-state.vy / 38, 0, 1), 0, 1)
      : 0;
  state.reentryHeat += (targetHeat - state.reentryHeat) * Math.min(1, safeDt * 3.5);

  return { exitToOrbit: state.y >= ORBIT_EXIT_ALTITUDE };
}
