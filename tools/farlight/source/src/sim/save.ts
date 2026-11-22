import { computeJumpRange, createInitialJourney, type JourneyState } from './journey.ts';
import type { ShipHullId } from './narrative.ts';

const SAVE_KEY = 'farlight_save_v1';

interface SerializedSave {
  version: 1;
  galaxySeed: number;
  currentStar: JourneyState['currentStar'];
  jumpRangeLY: number;
  totalJumps: number;
  yearsPassed: number;
  discoveryStars: number;
  visitedStarIds: string[];
  visitedExotic?: boolean;
  scannedPlanets: JourneyState['scannedPlanets'];
  camps?: JourneyState['camps'];
  activeShip?: ShipHullId;
  unlockedShips?: ShipHullId[];
  reachedHome: boolean;
}

export function serializeJourney(journey: JourneyState): string {
  const payload: SerializedSave = {
    version: 1,
    galaxySeed: journey.galaxySeed,
    currentStar: journey.currentStar,
    jumpRangeLY: journey.jumpRangeLY,
    totalJumps: journey.totalJumps,
    yearsPassed: journey.yearsPassed,
    discoveryStars: journey.discoveryStars,
    visitedStarIds: journey.visitedStarIds,
    visitedExotic: journey.visitedExotic,
    scannedPlanets: journey.scannedPlanets,
    camps: journey.camps,
    activeShip: journey.activeShip,
    unlockedShips: journey.unlockedShips,
    reachedHome: journey.reachedHome,
  };
  return JSON.stringify(payload);
}

export function deserializeJourney(raw: string): JourneyState | null {
  try {
    const data = JSON.parse(raw) as Partial<SerializedSave>;
    if (data.version !== 1 || !data.currentStar || typeof data.galaxySeed !== 'number') {
      return null;
    }
    const base = createInitialJourney(data.galaxySeed);
    const restored: JourneyState = {
      ...base,
      currentStar: data.currentStar,
      totalJumps: typeof data.totalJumps === 'number' ? data.totalJumps : 0,
      yearsPassed: typeof data.yearsPassed === 'number' ? data.yearsPassed : 0,
      discoveryStars: typeof data.discoveryStars === 'number' ? data.discoveryStars : 1,
      visitedStarIds: Array.isArray(data.visitedStarIds) ? data.visitedStarIds : [data.currentStar.id],
      visitedExotic: Boolean(data.visitedExotic),
      scannedPlanets: Array.isArray(data.scannedPlanets) ? data.scannedPlanets : [],
      camps: Array.isArray(data.camps) ? data.camps : [],
      activeShip: data.activeShip ?? 'starhopper',
      unlockedShips: Array.isArray(data.unlockedShips) && data.unlockedShips.length > 0 ? data.unlockedShips : ['starhopper'],
      reachedHome: Boolean(data.reachedHome),
    };
    restored.jumpRangeLY = computeJumpRange(restored);
    return restored;
  } catch {
    return null;
  }
}

export function saveJourneyLocal(journey: JourneyState): void {
  try {
    window.localStorage.setItem(SAVE_KEY, serializeJourney(journey));
  } catch {
    // Ignore restricted storage environments in locked-down browsers
  }
}

export function loadJourneyLocal(): JourneyState | null {
  try {
    const raw = window.localStorage.getItem(SAVE_KEY);
    if (!raw) return null;
    return deserializeJourney(raw);
  } catch {
    return null;
  }
}

export function clearJourneyLocal(): void {
  try {
    window.localStorage.removeItem(SAVE_KEY);
  } catch {
    // Ignore
  }
}
