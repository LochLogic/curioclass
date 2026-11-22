import { describe, expect, it } from 'vitest';
import { createRng, hashCoords } from '../../src/sim/prng.ts';
import { generateStarSystem, getShowcaseSystems } from '../../src/sim/galaxy.ts';
import { createInitialShipState, stepFlight, type FlightInput } from '../../src/sim/flight.ts';
import { v3Len } from '../../src/sim/math.ts';

const IDLE_INPUT: FlightInput = {
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

describe('Procedural Galaxy Determinism', () => {
  it('produces identical PRNG sequences for the same seed', () => {
    const a = createRng(424242);
    const b = createRng(424242);
    for (let i = 0; i < 20; i++) {
      expect(a.next()).toBe(b.next());
    }
  });

  it('generates identical star systems from the same sector coordinates', () => {
    const s1 = generateStarSystem(12345, 7, -2, 4);
    const s2 = generateStarSystem(12345, 7, -2, 4);
    expect(s1).toEqual(s2);
    expect(hashCoords(12345, 7, -2, 4)).not.toBe(hashCoords(12345, 7, -2, 5));
  });

  it('provides 5 distinct curated showcase star types', () => {
    const showcase = getShowcaseSystems();
    expect(showcase).toHaveLength(5);
    const kinds = new Set(showcase.map((s) => s.starKind));
    expect(kinds.size).toBe(5);
  });
});

describe('6-DoF Explorer Flight Simulation', () => {
  it('accelerates smoothly when thrusting forward and slows when braking', () => {
    const ship = createInitialShipState();
    for (let i = 0; i < 30; i++) {
      stepFlight(ship, { ...IDLE_INPUT, forward: 1 }, 1 / 60, 180);
    }
    expect(ship.speed).toBeGreaterThan(20);

    const speedBeforeBrake = ship.speed;
    for (let i = 0; i < 30; i++) {
      stepFlight(ship, { ...IDLE_INPUT, brake: true }, 1 / 60, 180);
    }
    expect(ship.speed).toBeLessThan(speedBeforeBrake * 0.25);
  });

  it('gently keeps the explorer ship outside the star safety boundary and recharges solar energy', () => {
    const ship = createInitialShipState();
    ship.position = { x: 0, y: 0, z: 200 };
    ship.solarCharge = 40;
    stepFlight(ship, IDLE_INPUT, 1 / 60, 180);
    expect(v3Len(ship.position)).toBeGreaterThanOrEqual(180 * 1.44);
    expect(ship.solarCharge).toBeGreaterThan(40);
  });
});
