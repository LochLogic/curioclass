import { describe, expect, it } from 'vitest';
import { generateStarSystemFromRef, SOL_STAR_REF } from '../../src/sim/galaxy.ts';
import { createInitialShipState, stepFlight, type FlightInput } from '../../src/sim/flight.ts';
import {
  computePlanetGravityG,
  createPlanetFlightState,
  sampleTerrainHeight,
  stepPlanetFlight,
  toggleLanded,
  toggleOnFoot,
  type PlanetFlightInput,
} from '../../src/sim/planet-flight.ts';
import { v3Len, v3Sub } from '../../src/sim/math.ts';

const IDLE_SPACE: FlightInput = {
  forward: 0,
  strafe: 0,
  vertical: 0,
  roll: 0,
  yawDelta: 0,
  pitchDelta: 0,
  boost: false,
  brake: false,
  cruise: false,
};

const IDLE_PLANET: PlanetFlightInput = {
  forward: 0,
  strafe: 0,
  vertical: 0,
  yawDelta: 0,
  pitchDelta: 0,
  boost: false,
  brake: false,
  cruise: false,
};

describe('Phase 7: Orbital & Planetary Gravity Effects', () => {
  const sol = generateStarSystemFromRef(202604, SOL_STAR_REF);
  const jupiter = sol.planets.find((p) => p.name === 'Jupiter')!;
  const mercury = sol.planets.find((p) => p.name === 'Mercury')!;
  const earth = sol.planets.find((p) => p.name === 'Earth')!;

  it('pulls the ship gently toward nearby massive planets in orbit', () => {
    const ship = createInitialShipState();
    ship.position = {
      x: jupiter.position.x + jupiter.radius * 3.0,
      y: jupiter.position.y,
      z: jupiter.position.z,
    };
    const startDist = v3Len(v3Sub(jupiter.position, ship.position));
    for (let i = 0; i < 60; i++) {
      stepFlight(ship, IDLE_SPACE, 1 / 60, sol.starRadius, sol.planets);
    }
    const endDist = v3Len(v3Sub(jupiter.position, ship.position));
    expect(ship.localGravityG).toBeGreaterThan(0.05);
    expect(endDist).toBeLessThan(startDist);
  });

  it('gives low-gravity moons significantly floatier gravity than Earth-sized worlds', () => {
    expect(computePlanetGravityG(mercury)).toBeLessThan(computePlanetGravityG(earth));

    const pfMoon = createPlanetFlightState(mercury, sol.seed);
    const pfEarth = createPlanetFlightState(earth, sol.seed);

    const setupOnFoot = (pf: ReturnType<typeof createPlanetFlightState>) => {
      let lx = 0;
      for (let x = 0; x < 2000; x += 40) {
        if (sampleTerrainHeight(x, 0, pf.seed, pf.planet.biome) > 8) {
          lx = x;
          break;
        }
      }
      const g = sampleTerrainHeight(lx, 0, pf.seed, pf.planet.biome);
      pf.x = lx;
      pf.z = 0;
      pf.y = g + 10;
      pf.altitudeAGL = 10;
      toggleLanded(pf);
      toggleOnFoot(pf);
      pf.vy = 18; // Identical upward hop impulse
    };

    setupOnFoot(pfMoon);
    setupOnFoot(pfEarth);

    // Let gravity pull both down for 0.6s
    for (let i = 0; i < 36; i++) {
      stepPlanetFlight(pfMoon, IDLE_PLANET, 1 / 60);
      stepPlanetFlight(pfEarth, IDLE_PLANET, 1 / 60);
    }
    expect(pfMoon.altitudeAGL).toBeGreaterThan(pfEarth.altitudeAGL);
  });
});
