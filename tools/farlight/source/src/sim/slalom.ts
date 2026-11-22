import type { StarSystem } from './galaxy.ts';
import type { Vec3 } from './math.ts';
import { v3Len, v3Sub } from './math.ts';

export interface SlalomRing {
  index: number;
  position: Vec3;
  yaw: number;
  passed: boolean;
}

export interface OrbitalActivityState {
  stationPos: Vec3;
  stationName: string;
  rings: SlalomRing[];
  passedCount: number;
  completed: boolean;
  dockedNotified: boolean;
}

/** Places a cozy Discovery Station and a 6-ring slalom course right in front of the player's arrival point */
export function createOrbitalActivity(system: StarSystem): OrbitalActivityState {
  // Position station gracefully ahead-right of initial arrival (0, 65, 680) so kids spot it immediately!
  const stationPos: Vec3 = { x: 115, y: 78, z: 470 };
  const rings: SlalomRing[] = [];
  for (let i = 0; i < 6; i++) {
    const t = i / 5;
    const angle = t * Math.PI * 0.85;
    rings.push({
      index: i,
      position: {
        x: -75 + Math.sin(angle) * 145,
        y: 66 + Math.sin(t * Math.PI * 2) * 26,
        z: 560 - i * 58,
      },
      yaw: Math.cos(angle) * 0.45,
      passed: false,
    });
  }

  return {
    stationPos,
    stationName: `${system.name} Discovery Outpost`,
    rings,
    passedCount: 0,
    completed: false,
    dockedNotified: false,
  };
}

export interface OrbitalStepResult {
  passedRingIndex: number | null;
  slalomCompletedNow: boolean;
  nearStation: boolean;
  rechargedAtStation: boolean;
}

export function stepOrbitalActivity(
  act: OrbitalActivityState,
  shipPos: Vec3,
): OrbitalStepResult {
  let passedRingIndex: number | null = null;
  let slalomCompletedNow = false;

  for (const ring of act.rings) {
    if (ring.passed) continue;
    const d = v3Len(v3Sub(ring.position, shipPos));
    if (d < 24) {
      ring.passed = true;
      act.passedCount += 1;
      passedRingIndex = ring.index;
      if (act.passedCount === act.rings.length && !act.completed) {
        act.completed = true;
        slalomCompletedNow = true;
      }
      break;
    }
  }

  const distStation = v3Len(v3Sub(act.stationPos, shipPos));
  const nearStation = distStation < 58;
  let rechargedAtStation = false;
  if (nearStation && !act.dockedNotified) {
    act.dockedNotified = true;
    rechargedAtStation = true;
  } else if (!nearStation) {
    act.dockedNotified = false;
  }

  return { passedRingIndex, slalomCompletedNow, nearStation, rechargedAtStation };
}
