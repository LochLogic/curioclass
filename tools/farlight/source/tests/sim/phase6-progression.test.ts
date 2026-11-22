import { describe, expect, it } from 'vitest';
import { generateStarSystemFromRef, getNearbyStars, SOL_STAR_REF } from '../../src/sim/galaxy.ts';
import { createInitialShipState } from '../../src/sim/flight.ts';
import {
  buildCampOnPlanet,
  createInitialJourney,
  selectOrUnlockShip,
  startJump,
  stepJump,
} from '../../src/sim/journey.ts';
import { evaluateEnding, SHIP_HULLS } from '../../src/sim/narrative.ts';
import { buildExplorerShipMesh } from '../../src/proc/ship-gen.ts';
import { buildCampMesh } from '../../src/proc/world-gen.ts';

describe('Phase 6: Cozy Camps, Unlockable Ships & Story Endings', () => {
  it('builds a Cozy Research Camp once per planet and earns passive Discovery Stars on jump', () => {
    const journey = createInitialJourney(202604);
    const sys = generateStarSystemFromRef(journey.galaxySeed, journey.currentStar);
    const planet = sys.planets[0]!;
    const starsBefore = journey.discoveryStars;

    const first = buildCampOnPlanet(journey, sys, planet, 12, 5, -18);
    expect(first.ok).toBe(true);
    expect(journey.camps).toHaveLength(1);
    expect(journey.discoveryStars).toBe(starsBefore + 3);

    // Duplicate camp on same planet blocked
    expect(buildCampOnPlanet(journey, sys, planet, 20, 5, -10).ok).toBe(false);

    // Passive science income triggers on jump
    const ship = createInitialShipState();
    const nearby = getNearbyStars(journey.galaxySeed, journey.currentStar, journey.jumpRangeLY);
    const dest = nearby.find((s) => s.id !== journey.currentStar.id)!;
    const starsPreJump = journey.discoveryStars;
    startJump(journey, ship, dest);
    stepJump(journey, 3.0);
    expect(journey.discoveryStars).toBeGreaterThanOrEqual(starsPreJump + 2);
  });

  it('unlocks and equips all 4 procedural 3D explorer ships as Discovery Stars grow', () => {
    const journey = createInitialJourney(202604);
    expect(selectOrUnlockShip(journey, 'sunskipper').ok).toBe(false);

    journey.discoveryStars = 25;
    for (const spec of SHIP_HULLS) {
      const res = selectOrUnlockShip(journey, spec.id);
      expect(res.ok).toBe(true);
      expect(journey.activeShip).toBe(spec.id);
      const mesh = buildExplorerShipMesh(spec.id);
      expect(mesh.vertices.length).toBeGreaterThan(0);
      expect(mesh.indices.length).toBeGreaterThan(0);
    }
    expect(buildCampMesh().indices.length).toBeGreaterThan(0);
  });

  it('evaluates all 4 distinct Homecoming Endings accurately', () => {
    expect(evaluateEnding({ scannedCount: 0, campCount: 0, visitedExotic: false, discoveryStars: 2 }).title).toBe(
      'The Swift Starfarer',
    );
    expect(evaluateEnding({ scannedCount: 5, campCount: 0, visitedExotic: false, discoveryStars: 10 }).title).toBe(
      'The Galactic Naturalist',
    );
    expect(evaluateEnding({ scannedCount: 1, campCount: 2, visitedExotic: false, discoveryStars: 10 }).title).toBe(
      'The Trailblazer’s Network',
    );
    expect(evaluateEnding({ scannedCount: 5, campCount: 2, visitedExotic: true, discoveryStars: 18 }).title).toBe(
      'Grand Explorer of Farlight',
    );
    expect(SOL_STAR_REF.isHome).toBe(true);
  });
});
