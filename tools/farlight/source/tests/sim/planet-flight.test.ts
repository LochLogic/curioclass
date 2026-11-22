import { describe, expect, it } from 'vitest';
import { generateStarSystemFromRef, SOL_STAR_REF } from '../../src/sim/galaxy.ts';
import {
  createPlanetFlightState,
  ORBIT_EXIT_ALTITUDE,
  sampleTerrainHeight,
  stepPlanetFlight,
  toggleLanded,
  type PlanetFlightInput,
} from '../../src/sim/planet-flight.ts';

const IDLE: PlanetFlightInput = {
  forward: 0,
  strafe: 0,
  vertical: 0,
  yawDelta: 0,
  pitchDelta: 0,
  boost: false,
  brake: false,
  cruise: false,
};

describe('Phase 3: Seamless Planetary Flight, Terrain & Landing', () => {
  const sol = generateStarSystemFromRef(202604, SOL_STAR_REF);
  const earth = sol.planets.find((p) => p.name === 'Earth')!;

  it('samples deterministic terrain heights consistently', () => {
    const h1 = sampleTerrainHeight(125.5, -84.2, 4242, 'meadow-world');
    const h2 = sampleTerrainHeight(125.5, -84.2, 4242, 'meadow-world');
    expect(h1).toBe(h2);
  });

  it('prevents the ship from clipping below terrain or ocean (kid-friendly hover cushion)', () => {
    const pf = createPlanetFlightState(earth, sol.seed);
    pf.y = 30;
    pf.vy = -80;
    for (let i = 0; i < 60; i++) {
      stepPlanetFlight(pf, { ...IDLE, vertical: -1 }, 1 / 60);
    }
    const ground = Math.max(pf.seaLevel, sampleTerrainHeight(pf.x, pf.z, pf.seed, pf.planet.biome));
    expect(pf.y).toBeGreaterThanOrEqual(ground + 2.4);
  });

  it('touches down cleanly over dry land and lifts back off', () => {
    const pf = createPlanetFlightState(earth, sol.seed);
    // Find a dry land spot
    let lx = 0;
    let lz = 0;
    for (let x = 0; x < 2000; x += 40) {
      if (sampleTerrainHeight(x, 0, pf.seed, pf.planet.biome) > 8) {
        lx = x;
        break;
      }
    }
    const ground = sampleTerrainHeight(lx, lz, pf.seed, pf.planet.biome);
    pf.x = lx;
    pf.z = lz;
    pf.y = ground + 15;
    pf.altitudeAGL = 15;

    const landRes = toggleLanded(pf);
    expect(landRes.ok).toBe(true);
    expect(pf.landed).toBe(true);

    const liftRes = toggleLanded(pf);
    expect(liftRes.ok).toBe(true);
    expect(pf.landed).toBe(false);
    expect(pf.vy).toBeGreaterThan(0);
  });

  it('triggers seamless return to orbit when climbing above atmosphere', () => {
    const pf = createPlanetFlightState(earth, sol.seed);
    pf.y = ORBIT_EXIT_ALTITUDE - 15;
    pf.vy = 90;
    let exited = false;
    for (let i = 0; i < 30; i++) {
      const res = stepPlanetFlight(pf, { ...IDLE, vertical: 1, boost: true }, 1 / 60);
      if (res.exitToOrbit) {
        exited = true;
        break;
      }
    }
    expect(exited).toBe(true);
  });
});
