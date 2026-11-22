import {
  generateStarSystemFromRef,
  getStartingStar,
  SOL_STAR_REF,
  starDistanceLY,
  type PlanetData,
  type StarRef,
  type StarSystem,
} from './galaxy.ts';
import { v3Len, v3Sub } from './math.ts';
import type { ShipState } from './flight.ts';
import { getShipHull, type ShipHullId } from './narrative.ts';

export type JumpPhase = 'idle' | 'tunnel';

export interface ScannedRecord {
  key: string;
  planetName: string;
  systemName: string;
  biome: string;
  funFact: string;
}

export interface CampRecord {
  key: string; // `${systemId}#${planetId}`
  planetName: string;
  systemName: string;
  x: number;
  y: number;
  z: number;
}

export interface JourneyState {
  galaxySeed: number;
  currentStar: StarRef;
  targetStar: StarRef | null;
  jumpRangeLY: number;
  totalJumps: number;
  yearsPassed: number;
  discoveryStars: number;
  visitedStarIds: string[];
  visitedExotic: boolean;
  scannedPlanets: ScannedRecord[];
  camps: CampRecord[];
  activeShip: ShipHullId;
  unlockedShips: ShipHullId[];
  reachedHome: boolean;
  jumpPhase: JumpPhase;
  jumpProgress: number; // 0..1 during hyperspace tunnel
}

export function computeJumpRange(journey: JourneyState): number {
  const hull = getShipHull(journey.activeShip);
  const discoveryBonus = Math.min(115, Math.floor(journey.discoveryStars / 3) * 15);
  return 165 + discoveryBonus + hull.bonusRangeLY;
}

export function createInitialJourney(galaxySeed = 202604): JourneyState {
  const start = getStartingStar(galaxySeed);
  return {
    galaxySeed,
    currentStar: start,
    targetStar: null,
    jumpRangeLY: 165,
    totalJumps: 0,
    yearsPassed: 0,
    discoveryStars: 1,
    visitedStarIds: [start.id],
    visitedExotic: false,
    scannedPlanets: [],
    camps: [],
    activeShip: 'starhopper',
    unlockedShips: ['starhopper'],
    reachedHome: false,
    jumpPhase: 'idle',
    jumpProgress: 0,
  };
}

export function jumpSolarCost(distanceLY: number): number {
  return Math.max(8, Math.min(45, Math.round(distanceLY * 0.22)));
}

export interface JumpCheck {
  ok: boolean;
  reason: string;
  distanceLY: number;
  solarCost: number;
}

export function checkJump(
  journey: JourneyState,
  ship: ShipState,
  target: StarRef | null,
): JumpCheck {
  if (!target) {
    return { ok: false, reason: 'Pick a star on the Galaxy Map (M) first!', distanceLY: 0, solarCost: 0 };
  }
  if (target.id === journey.currentStar.id) {
    return { ok: false, reason: 'You are already in this star system.', distanceLY: 0, solarCost: 0 };
  }
  const dist = starDistanceLY(journey.currentStar, target);
  const cost = jumpSolarCost(dist);
  if (dist > journey.jumpRangeLY) {
    return {
      ok: false,
      reason: `Too far (${Math.round(dist)} LY). Max jump range is ${journey.jumpRangeLY} LY.`,
      distanceLY: dist,
      solarCost: cost,
    };
  }
  if (ship.solarCharge < cost) {
    return {
      ok: false,
      reason: `Need ${cost}% Solar Charge (fly closer to the star to recharge!).`,
      distanceLY: dist,
      solarCost: cost,
    };
  }
  return { ok: true, reason: 'Ready to jump!', distanceLY: dist, solarCost: cost };
}

export function startJump(journey: JourneyState, ship: ShipState, target: StarRef): JumpCheck {
  const chk = checkJump(journey, ship, target);
  if (!chk.ok) return chk;
  ship.solarCharge = Math.max(0, ship.solarCharge - chk.solarCost);
  journey.targetStar = target;
  journey.jumpPhase = 'tunnel';
  journey.jumpProgress = 0;
  return chk;
}

/** Advances the hyperspace tunnel animation; returns the newly arrived StarSystem once complete. */
export function stepJump(
  journey: JourneyState,
  dt: number,
): { arrivedSystem: StarSystem | null; newDiscovery: boolean } {
  if (journey.jumpPhase !== 'tunnel' || !journey.targetStar) {
    return { arrivedSystem: null, newDiscovery: false };
  }
  // 2.2-second joyful warp tunnel
  journey.jumpProgress += dt / 2.2;
  if (journey.jumpProgress < 1) {
    return { arrivedSystem: null, newDiscovery: false };
  }

  const dest = journey.targetStar;
  const dist = starDistanceLY(journey.currentStar, dest);
  journey.currentStar = dest;
  journey.targetStar = null;
  journey.jumpPhase = 'idle';
  journey.jumpProgress = 0;
  journey.totalJumps += 1;
  journey.yearsPassed += Math.max(1, Math.round(dist * 0.12));

  let newDiscovery = false;
  if (!journey.visitedStarIds.includes(dest.id)) {
    journey.visitedStarIds.push(dest.id);
    journey.discoveryStars += dest.starKind === 'black-hole' || dest.starKind === 'pulsar' ? 3 : 1;
    newDiscovery = true;
  }
  if (dest.starKind === 'black-hole' || dest.starKind === 'pulsar') {
    journey.visitedExotic = true;
  }
  // Cozy Research Camps beam back passive Discovery Stars on every jump!
  if (journey.camps.length > 0) {
    journey.discoveryStars += journey.camps.length;
  }
  if (dest.isHome || dest.id === SOL_STAR_REF.id) {
    journey.reachedHome = true;
  }
  journey.jumpRangeLY = computeJumpRange(journey);

  return {
    arrivedSystem: generateStarSystemFromRef(journey.galaxySeed, dest),
    newDiscovery,
  };
}

export function buildCampOnPlanet(
  journey: JourneyState,
  system: StarSystem,
  planet: PlanetData,
  x: number,
  y: number,
  z: number,
): { ok: boolean; message: string } {
  const key = planetScanKey(system.ref.id, planet.id);
  if (journey.camps.some((c) => c.key === key)) {
    return { ok: false, message: `You already built a Cozy Research Camp on ${planet.name}!` };
  }
  journey.camps.push({
    key,
    planetName: planet.name,
    systemName: system.name,
    x,
    y,
    z,
  });
  journey.discoveryStars += 3;
  journey.jumpRangeLY = computeJumpRange(journey);
  return {
    ok: true,
    message: `⛺ Built a Cozy Research Camp on ${planet.name}! (+3 Discovery Stars + passive science on every jump!)`,
  };
}

export function selectOrUnlockShip(
  journey: JourneyState,
  hullId: ShipHullId,
): { ok: boolean; message: string } {
  const spec = getShipHull(hullId);
  if (journey.unlockedShips.includes(hullId)) {
    journey.activeShip = hullId;
    journey.jumpRangeLY = computeJumpRange(journey);
    return { ok: true, message: `Switched to ${spec.name}! (Jump Range: ${journey.jumpRangeLY} LY)` };
  }
  if (journey.discoveryStars < spec.costStars) {
    return {
      ok: false,
      message: `Need ★ ${spec.costStars} Discovery Stars to unlock ${spec.name} (you have ★ ${journey.discoveryStars}).`,
    };
  }
  journey.unlockedShips.push(hullId);
  journey.activeShip = hullId;
  journey.jumpRangeLY = computeJumpRange(journey);
  return { ok: true, message: `🚀 Unlocked & boarded ${spec.name}! (+${spec.bonusRangeLY} LY jump range)` };
}

export function distanceToHomeLY(journey: JourneyState): number {
  return starDistanceLY(journey.currentStar, SOL_STAR_REF);
}

export function planetScanKey(systemId: string, planetId: number): string {
  return `${systemId}#${planetId}`;
}

export function scanNearestPlanet(
  journey: JourneyState,
  system: StarSystem,
  ship: ShipState,
): { scanned: boolean; alreadyScanned: boolean; planet: PlanetData | null; message: string } {
  let nearest: PlanetData | null = null;
  let bestDist = Infinity;
  for (const p of system.planets) {
    const d = v3Len(v3Sub(p.position, ship.position)) - p.radius;
    if (d < bestDist) {
      bestDist = d;
      nearest = p;
    }
  }
  if (!nearest) {
    return { scanned: false, alreadyScanned: false, planet: null, message: 'No planets in this system.' };
  }
  const scanRange = Math.max(260, nearest.radius * 6.5);
  if (bestDist > scanRange) {
    return {
      scanned: false,
      alreadyScanned: false,
      planet: nearest,
      message: `Fly closer to ${nearest.name} to scan (${Math.round(bestDist)} km away; get under ${Math.round(scanRange)} km).`,
    };
  }
  const key = planetScanKey(system.ref.id, nearest.id);
  if (journey.scannedPlanets.some((r) => r.key === key)) {
    return {
      scanned: false,
      alreadyScanned: true,
      planet: nearest,
      message: `${nearest.name} is already in your Explorer's Journal!`,
    };
  }
  journey.scannedPlanets.push({
    key,
    planetName: nearest.name,
    systemName: system.name,
    biome: nearest.biome,
    funFact: nearest.funFact,
  });
  journey.discoveryStars += 2;
  journey.jumpRangeLY = computeJumpRange(journey);
  return {
    scanned: true,
    alreadyScanned: false,
    planet: nearest,
    message: `Scanned ${nearest.name}! (+2 Discovery Stars) ${nearest.funFact}`,
  };
}
