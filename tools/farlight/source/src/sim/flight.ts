import {
  clamp,
  quatFromAxisAngle,
  quatIdentity,
  quatMul,
  quatNorm,
  quatRotateVec,
  v3Add,
  v3Cross,
  v3Dot,
  v3Len,
  v3Norm,
  v3Scale,
  v3Sub,
  vec3,
  type Quat,
  type Vec3,
} from './math.ts';

import type { PlanetData } from './galaxy.ts';

export interface FlightInput {
  forward: number; // -1..1 (S/W)
  strafe: number;  // -1..1 (A/D)
  vertical: number; // -1..1 (Ctrl/Space or Q/E)
  roll: number;    // -1..1 (Q/E)
  yawDelta: number;
  pitchDelta: number;
  boost: boolean;
  brake: boolean;
  cruise: boolean;
}

export interface ShipState {
  position: Vec3;
  velocity: Vec3;
  orientation: Quat;
  speed: number;
  maxSpeed: number;
  solarCharge: number; // 0..100 friendly "fuel" recharged near stars
  hullWarmth: number;  // 0..100 gentle heat gauge near stars
  boostAmount: number; // 0..1 for thruster visuals
  cruiseActive: boolean;
  localGravityG: number; // Live felt gravity in Earth Gs (0.00 in deep space)
}

export function createInitialShipState(): ShipState {
  return {
    position: vec3(0, 65, 680),
    velocity: vec3(0, 0, 0),
    orientation: quatIdentity(),
    speed: 0,
    maxSpeed: 120,
    solarCharge: 100,
    hullWarmth: 12,
    boostAmount: 0,
    cruiseActive: false,
    localGravityG: 0,
  };
}

export function stepFlight(
  ship: ShipState,
  input: FlightInput,
  dt: number,
  starRadius: number,
  planets: readonly PlanetData[] = [],
): void {
  const safeDt = clamp(dt, 0.0001, 0.05);

  // Smooth rotational steering
  if (Math.abs(input.yawDelta) > 1e-6) {
    const qYaw = quatFromAxisAngle(vec3(0, 1, 0), -input.yawDelta);
    ship.orientation = quatNorm(quatMul(ship.orientation, qYaw));
  }
  if (Math.abs(input.pitchDelta) > 1e-6) {
    const qPitch = quatFromAxisAngle(vec3(1, 0, 0), -input.pitchDelta);
    ship.orientation = quatNorm(quatMul(ship.orientation, qPitch));
  }
  if (Math.abs(input.roll) > 1e-4) {
    const qRoll = quatFromAxisAngle(vec3(0, 0, 1), -input.roll * 1.9 * safeDt);
    ship.orientation = quatNorm(quatMul(ship.orientation, qRoll));
  }

  const forwardDir = quatRotateVec(ship.orientation, vec3(0, 0, -1));
  const rightDir = quatRotateVec(ship.orientation, vec3(1, 0, 0));
  const upDir = quatRotateVec(ship.orientation, vec3(0, 1, 0));

  const boosting = input.boost && ship.solarCharge > 2;
  const cruiseMult = input.cruise ? 3.2 : 1.0;
  const boostMult = boosting ? 2.1 : 1.0;
  ship.cruiseActive = input.cruise;
  ship.boostAmount = clamp(
    ship.boostAmount + ((boosting || input.cruise ? 1 : 0) - ship.boostAmount) * 8 * safeDt,
    0,
    1,
  );

  const accel = 95 * boostMult * cruiseMult;
  let thrust = vec3(0, 0, 0);
  const fwdCmd = input.cruise ? Math.max(0.85, input.forward) : input.forward;
  thrust = v3Add(thrust, v3Scale(forwardDir, fwdCmd * accel));
  thrust = v3Add(thrust, v3Scale(rightDir, input.strafe * 65));
  thrust = v3Add(thrust, v3Scale(upDir, input.vertical * 65));

  // Gentle, tactile orbital gravity pull from the star and nearby planets (great for slingshots!)
  let gravAccel = vec3(0, 0, 0);
  const starD = v3Len(ship.position);
  if (starD > starRadius * 1.1 && starD < starRadius * 7.5) {
    const pull = clamp((starRadius * starRadius * 4.5) / (starD * starD + 1), 0, 22);
    gravAccel = v3Add(gravAccel, v3Scale(ship.position, -pull / starD));
  }
  for (const p of planets) {
    const toPlanet = v3Sub(p.position, ship.position);
    const pd = v3Len(toPlanet);
    const wellRadius = p.radius * 9.0;
    if (pd > p.radius * 0.9 && pd < wellRadius) {
      const massFactor = p.biome === 'cloud-giant' ? 38.0 : 22.0;
      const pull = clamp((p.radius * p.radius * massFactor) / (pd * pd + 1), 0, 22);
      gravAccel = v3Add(gravAccel, v3Scale(toPlanet, pull / pd));
    }
  }
  ship.localGravityG = v3Len(gravAccel) / 14.0;

  ship.velocity = v3Add(ship.velocity, v3Scale(v3Add(thrust, gravAccel), safeDt));

  // Friendly space damping so kids can fly effortlessly without spinning out
  const damping = input.brake ? Math.exp(-5.5 * safeDt) : Math.exp(-1.45 * safeDt);
  ship.velocity = v3Scale(ship.velocity, damping);

  const speedCap = ship.maxSpeed * boostMult * cruiseMult;
  const curSpeed = v3Len(ship.velocity);
  if (curSpeed > speedCap) {
    ship.velocity = v3Scale(ship.velocity, speedCap / curSpeed);
    ship.speed = speedCap;
  } else {
    ship.speed = curSpeed;
  }

  ship.position = v3Add(ship.position, v3Scale(ship.velocity, safeDt));

  // Gentle star proximity: solar recharge + friendly heat buffer (softly pushes ship out if too close)
  const distToStar = v3Len(ship.position);
  const safeOrbit = starRadius * 1.45;
  if (distToStar < safeOrbit && distToStar > 1e-4) {
    const pushDir = v3Scale(ship.position, 1 / distToStar);
    ship.position = v3Scale(pushDir, safeOrbit);
    ship.velocity = v3Add(ship.velocity, v3Scale(pushDir, 45 * safeDt));
  }

  const scoopZone = starRadius * 4.2;
  if (distToStar < scoopZone) {
    const closeness = 1 - clamp((distToStar - safeOrbit) / (scoopZone - safeOrbit), 0, 1);
    ship.solarCharge = clamp(ship.solarCharge + (14 + 28 * closeness) * safeDt, 0, 100);
    ship.hullWarmth = clamp(ship.hullWarmth + (closeness * 45 - 8) * safeDt, 10, 95);
  } else {
    const drain = boosting ? 5.5 : input.cruise ? 1.8 : 0.15;
    ship.solarCharge = clamp(ship.solarCharge - drain * safeDt, 0, 100);
    ship.hullWarmth = clamp(ship.hullWarmth - 18 * safeDt, 10, 95);
  }
}

/** Points the ship's nose (-Z local axis) toward a target position in system coordinates */
export function orientShipToward(ship: ShipState, targetPos: Vec3): void {
  const dir = v3Norm(v3Sub(targetPos, ship.position));
  const baseFwd = vec3(0, 0, -1);
  const dot = clamp(v3Dot(baseFwd, dir), -1, 1);
  if (dot > 0.9999) {
    ship.orientation = quatIdentity();
  } else if (dot < -0.9999) {
    ship.orientation = quatFromAxisAngle(vec3(0, 1, 0), Math.PI);
  } else {
    const axis = v3Cross(baseFwd, dir);
    ship.orientation = quatNorm(quatFromAxisAngle(axis, Math.acos(dot)));
  }
}
