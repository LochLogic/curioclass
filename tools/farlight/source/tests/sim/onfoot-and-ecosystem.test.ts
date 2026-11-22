import { describe, expect, it } from 'vitest';
import { generateStarSystemFromRef, SOL_STAR_REF } from '../../src/sim/galaxy.ts';
import {
  createPlanetFlightState,
  sampleTerrainHeight,
  stepPlanetFlight,
  toggleLanded,
  toggleOnFoot,
  type PlanetFlightInput,
} from '../../src/sim/planet-flight.ts';
import { buildFlierMesh, getPlanetSpecies, spawnSurfaceInstances } from '../../src/proc/world-gen.ts';

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

describe('Phase 4: On-Foot Exploration, Jetpack & Procedural Ecosystem', () => {
  const sol = generateStarSystemFromRef(202604, SOL_STAR_REF);
  const earth = sol.planets.find((p) => p.name === 'Earth')!;

  it('spawns deterministic 3D flora and friendly critters on dry land', () => {
    const pf = createPlanetFlightState(earth, sol.seed);
    const instA = spawnSurfaceInstances(0, 0, pf.seed, earth.biome, pf.seaLevel);
    const instB = spawnSurfaceInstances(0, 0, pf.seed, earth.biome, pf.seaLevel);
    expect(instA.treeCount).toBe(instB.treeCount);
    expect(instA.treeCount + instA.lanternCount + instA.spireCount).toBeGreaterThan(10);
    expect(instA.critterCount).toBeGreaterThan(0);
    expect(instA.flierCount).toBeGreaterThan(0);
    expect(buildFlierMesh().indices.length).toBeGreaterThan(0);

    const species = getPlanetSpecies(earth.biome);
    expect(species.floraName.length).toBeGreaterThan(3);
    expect(species.critterName.length).toBeGreaterThan(3);
    expect(species.flierName.length).toBeGreaterThan(3);
  });

  it('allows stepping out after landing, walking, using the bouncy jetpack, and boarding back in', () => {
    const pf = createPlanetFlightState(earth, sol.seed);

    // Cannot step out while flying
    expect(toggleOnFoot(pf).ok).toBe(false);

    // Find dry land & touch down
    let lx = 0;
    for (let x = 0; x < 2000; x += 40) {
      if (sampleTerrainHeight(x, 0, pf.seed, earth.biome) > 8) {
        lx = x;
        break;
      }
    }
    const ground = sampleTerrainHeight(lx, 0, pf.seed, earth.biome);
    pf.x = lx;
    pf.z = 0;
    pf.y = ground + 10;
    pf.altitudeAGL = 10;
    expect(toggleLanded(pf).ok).toBe(true);

    // Step out onto surface
    const out = toggleOnFoot(pf);
    expect(out.ok).toBe(true);
    expect(pf.onFoot).toBe(true);

    const startY = pf.y;
    // Engage bouncy jetpack (Space = brake input)
    for (let i = 0; i < 20; i++) {
      stepPlanetFlight(pf, { ...IDLE, forward: 1, brake: true }, 1 / 60);
    }
    expect(pf.y).toBeGreaterThan(startY + 1);
    expect(pf.jetpackFuel).toBeLessThan(100);

    // Board back into parked Starhopper
    const back = toggleOnFoot(pf);
    expect(back.ok).toBe(true);
    expect(pf.onFoot).toBe(false);
    expect(pf.landed).toBe(true);
  });
});
