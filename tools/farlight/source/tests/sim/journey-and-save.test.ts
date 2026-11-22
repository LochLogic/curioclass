import { describe, expect, it } from 'vitest';
import {
  generateStarSystemFromRef,
  getNearbyStars,
  SOL_STAR_REF,
  starDistanceLY,
} from '../../src/sim/galaxy.ts';
import { createInitialShipState, orientShipToward } from '../../src/sim/flight.ts';
import {
  checkJump,
  createInitialJourney,
  distanceToHomeLY,
  scanNearestPlanet,
  startJump,
  stepJump,
} from '../../src/sim/journey.ts';
import { deserializeJourney, serializeJourney } from '../../src/sim/save.ts';
import { quatRotateVec, v3Dot, v3Norm, v3Sub, vec3 } from '../../src/sim/math.ts';

describe('Phase 2: Galaxy Navigation, Hyperspace Jump, Scanning & Save', () => {
  it('generates Sol with Mercury through ringed Saturn', () => {
    const sol = generateStarSystemFromRef(202604, SOL_STAR_REF);
    expect(sol.name).toBe('Sol (Home)');
    expect(sol.planets.map((p) => p.name)).toEqual([
      'Mercury',
      'Venus',
      'Earth',
      'Mars',
      'Jupiter',
      'Saturn',
    ]);
    expect(sol.planets[5]?.hasRings).toBe(true);
  });

  it('validates jump range and solar charge before engaging hyperspace', () => {
    const journey = createInitialJourney(202604);
    const ship = createInitialShipState();

    // Sol is ~600 LY away initially -> out of range
    const farCheck = checkJump(journey, ship, SOL_STAR_REF);
    expect(farCheck.ok).toBe(false);

    // Find a reachable nearby star
    const nearby = getNearbyStars(journey.galaxySeed, journey.currentStar, journey.jumpRangeLY);
    const dest = nearby.find((s) => s.id !== journey.currentStar.id);
    expect(dest).toBeDefined();

    // Low solar charge blocks jump
    ship.solarCharge = 2;
    expect(checkJump(journey, ship, dest!).ok).toBe(false);

    // Full solar charge allows jump & completes tunnel
    ship.solarCharge = 100;
    const started = startJump(journey, ship, dest!);
    expect(started.ok).toBe(true);
    expect(journey.jumpPhase).toBe('tunnel');

    let arrived = null;
    for (let i = 0; i < 150; i++) {
      const step = stepJump(journey, 0.02);
      if (step.arrivedSystem) {
        arrived = step.arrivedSystem;
        break;
      }
    }
    expect(arrived?.ref.id).toBe(dest!.id);
    expect(journey.totalJumps).toBe(1);
    expect(journey.visitedStarIds).toContain(dest!.id);
  });

  it('scans nearby planets once and awards Discovery Stars', () => {
    const journey = createInitialJourney(202604);
    const sys = generateStarSystemFromRef(journey.galaxySeed, journey.currentStar);
    const ship = createInitialShipState();
    const targetPlanet = sys.planets[0]!;

    // Move ship right beside the planet
    ship.position = {
      x: targetPlanet.position.x + targetPlanet.radius + 40,
      y: targetPlanet.position.y,
      z: targetPlanet.position.z,
    };

    const starsBefore = journey.discoveryStars;
    const first = scanNearestPlanet(journey, sys, ship);
    expect(first.scanned).toBe(true);
    expect(journey.discoveryStars).toBe(starsBefore + 2);

    const second = scanNearestPlanet(journey, sys, ship);
    expect(second.scanned).toBe(false);
    expect(second.alreadyScanned).toBe(true);
  });

  it('round-trips journey state cleanly through save serialization', () => {
    const journey = createInitialJourney(999111);
    journey.totalJumps = 4;
    journey.discoveryStars = 11;
    journey.yearsPassed = 38;
    const raw = serializeJourney(journey);
    const restored = deserializeJourney(raw);
    expect(restored).not.toBeNull();
    expect(restored?.totalJumps).toBe(4);
    expect(restored?.discoveryStars).toBe(11);
    expect(restored?.currentStar).toEqual(journey.currentStar);
  });

  it('orients ship nose directly toward a chosen planet', () => {
    const ship = createInitialShipState();
    const target = vec3(320, -45, -210);
    orientShipToward(ship, target);
    const nose = quatRotateVec(ship.orientation, vec3(0, 0, -1));
    const expected = v3Norm(v3Sub(target, ship.position));
    expect(v3Dot(nose, expected)).toBeGreaterThan(0.999);
  });

  it('can navigate all the way from the starting star back home to Sol in headless simulation', () => {
    const journey = createInitialJourney(202604);
    const ship = createInitialShipState();

    for (let hop = 0; hop < 25 && !journey.reachedHome; hop++) {
      ship.solarCharge = 100; // Assume player scooped solar energy at star
      const candidates = getNearbyStars(journey.galaxySeed, journey.currentStar, journey.jumpRangeLY);
      if (distanceToHomeLY(journey) <= journey.jumpRangeLY && !candidates.some((s) => s.id === SOL_STAR_REF.id)) {
        candidates.push(SOL_STAR_REF);
      }
      // Greedy step closest to Sol
      const best = candidates
        .filter((s) => s.id !== journey.currentStar.id)
        .sort((a, b) => starDistanceLY(a, SOL_STAR_REF) - starDistanceLY(b, SOL_STAR_REF))[0];

      expect(best).toBeDefined();
      const res = startJump(journey, ship, best!);
      expect(res.ok).toBe(true);
      stepJump(journey, 3.0);
    }

    expect(journey.reachedHome).toBe(true);
    expect(journey.currentStar.id).toBe(SOL_STAR_REF.id);
  });
});
