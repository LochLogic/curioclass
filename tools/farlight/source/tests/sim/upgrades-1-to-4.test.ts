import { describe, expect, it } from 'vitest';
import { generateStarSystemFromRef, SOL_STAR_REF } from '../../src/sim/galaxy.ts';
import { createOrbitalActivity, stepOrbitalActivity } from '../../src/sim/slalom.ts';
import { buildSlalomRingMesh, buildStationMesh } from '../../src/proc/station-gen.ts';
import {
  createPlanetFlightState,
  sampleTerrainHeight,
  stepPlanetFlight,
  toggleLanded,
  toggleRover,
  type PlanetFlightInput,
} from '../../src/sim/planet-flight.ts';
import {
  buildCityTowerMesh,
  buildFishMesh,
  buildGrassMesh,
  buildRoverMesh,
  buildRuinMesh,
  spawnSurfaceInstances,
} from '../../src/proc/world-gen.ts';

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

describe('Upgrades 1–4: Space Station, Slalom Rings, Rover, Ruins, Grass, Fish & Earth Cities', () => {
  const sol = generateStarSystemFromRef(202604, SOL_STAR_REF);
  const earth = sol.planets.find((p) => p.name === 'Earth')!;

  it('builds 3D Space Station & Slalom Ring meshes and tracks ring-course completion', () => {
    expect(buildStationMesh().indices.length).toBeGreaterThan(0);
    expect(buildSlalomRingMesh().indices.length).toBeGreaterThan(0);

    const orb = createOrbitalActivity(sol);
    expect(orb.rings).toHaveLength(6);

    for (let i = 0; i < orb.rings.length; i++) {
      const res = stepOrbitalActivity(orb, orb.rings[i]!.position);
      expect(res.passedRingIndex).toBe(i);
      if (i === orb.rings.length - 1) {
        expect(res.slalomCompletedNow).toBe(true);
      }
    }
    expect(orb.completed).toBe(true);

    const dockRes = stepOrbitalActivity(orb, orb.stationPos);
    expect(dockRes.nearStation).toBe(true);
    expect(dockRes.rechargedAtStation).toBe(true);
  });

  it('deploys the 6-wheel Explorer Rover from a landed ship and drives + jumps cleanly', () => {
    expect(buildRoverMesh().indices.length).toBeGreaterThan(0);

    const pf = createPlanetFlightState(earth, sol.seed);
    let lx = 0;
    for (let x = 0; x < 2000; x += 40) {
      if (sampleTerrainHeight(x, 0, pf.seed, earth.biome) > 8) {
        lx = x;
        break;
      }
    }
    const g = sampleTerrainHeight(lx, 0, pf.seed, earth.biome);
    pf.x = lx;
    pf.z = 0;
    pf.y = g + 8;
    pf.altitudeAGL = 8;
    expect(toggleLanded(pf).ok).toBe(true);

    const roverRes = toggleRover(pf);
    expect(roverRes.ok).toBe(true);
    expect(pf.inRover).toBe(true);

    for (let i = 0; i < 20; i++) {
      stepPlanetFlight(pf, { ...IDLE, forward: 1, brake: true }, 1 / 60);
    }
    expect(pf.speed).toBeGreaterThan(15);
  });

  it('spawns lush grass, swimming fish, ancient ruins, and coastal cities on Earth', () => {
    expect(buildGrassMesh().indices.length).toBeGreaterThan(0);
    expect(buildFishMesh().indices.length).toBeGreaterThan(0);
    expect(buildRuinMesh().indices.length).toBeGreaterThan(0);
    expect(buildCityTowerMesh().indices.length).toBeGreaterThan(0);

    const pf = createPlanetFlightState(earth, sol.seed);
    const inst = spawnSurfaceInstances(0, 0, pf.seed, earth.biome, pf.seaLevel, true);
    expect(inst.grassCount).toBeGreaterThan(10);
    expect(inst.fishCount).toBeGreaterThan(0);
    expect(inst.cityCount).toBeGreaterThan(0);
  });
});
