import { ContinuousEmitter, WaveImpulse, telemetry } from '../audio/telemetry';
import { clamp } from '../core/music';
import { state } from '../core/state';
import { THEMES } from './themes';

const MAX_IMPULSES = 10;

const VERT_SRC = `#version 300 es
precision highp float;
const vec2 POS[3] = vec2[3](vec2(-1.0, -1.0), vec2(3.0, -1.0), vec2(-1.0, 3.0));
out vec2 vUv;
void main() {
  vec2 p = POS[gl_VertexID];
  vUv = p * 0.5 + 0.5;
  gl_Position = vec4(p, 0.0, 1.0);
}
`;

// Ping-pong 2D damped wave equation (Verlet) with line-source & point-source acoustic impulses
const STEP_FRAG_SRC = `#version 300 es
precision highp float;

in vec2 vUv;
out vec4 outWave;

uniform sampler2D uWavePrev;
uniform vec2 uTexel;
uniform float uAspect;
uniform float uDamp;
uniform float uSpeed;
uniform int uImpCount;
// Each impulse: uImpSeg[i] = (x0, y0, x1, y1), uImpMeta[i] = (freqNorm, amp, phase, isPoint)
uniform vec4 uImpSeg[${MAX_IMPULSES}];
uniform vec4 uImpMeta[${MAX_IMPULSES}];
uniform vec3 uImpCol[${MAX_IMPULSES}];
uniform float uTime;

// Distance from p to segment ab (in aspect-corrected space)
vec2 segDist(vec2 p, vec2 a, vec2 b) {
  vec2 pa = p - a;
  vec2 ba = b - a;
  float len2 = max(dot(ba, ba), 1e-6);
  float u = clamp(dot(pa, ba) / len2, 0.0, 1.0);
  vec2 d = pa - ba * u;
  return vec2(length(d), u);
}

void main() {
  vec4 cur = texture(uWavePrev, vUv);
  float h = cur.r;
  float hPrev = cur.g;
  float hueTint = cur.b;
  float energy = cur.a;

  // 9-point isotropic Laplacian for smooth circular wave fronts (no diamond grid artifacts)
  vec2 tx = vec2(uTexel.x, 0.0);
  vec2 ty = vec2(0.0, uTexel.y);
  float nL = texture(uWavePrev, vUv - tx).r;
  float nR = texture(uWavePrev, vUv + tx).r;
  float nD = texture(uWavePrev, vUv - ty).r;
  float nU = texture(uWavePrev, vUv + ty).r;
  float nLD = texture(uWavePrev, vUv - tx - ty).r;
  float nRD = texture(uWavePrev, vUv + tx - ty).r;
  float nLU = texture(uWavePrev, vUv - tx + ty).r;
  float nRU = texture(uWavePrev, vUv + tx + ty).r;

  float lap = (nL + nR + nD + nU) * 0.2 + (nLD + nRD + nLU + nRU) * 0.05 - h;

  // Gentle absorbing sponge near edges so waves fade naturally without harsh box reflections
  vec2 edge = min(vUv, 1.0 - vUv);
  float borderDamp = smoothstep(0.0, 0.06, min(edge.x, edge.y));
  float damp = mix(0.92, uDamp, borderDamp);

  float nextH = (2.0 * h - hPrev + uSpeed * lap) * damp;

  // Propagate & diffuse spectral energy and tint smoothly with the wave
  float avgE = (
    texture(uWavePrev, vUv - tx).a + texture(uWavePrev, vUv + tx).a +
    texture(uWavePrev, vUv - ty).a + texture(uWavePrev, vUv + ty).a + energy * 2.0
  ) / 6.0;
  float avgTint = (
    texture(uWavePrev, vUv - tx).b + texture(uWavePrev, vUv + tx).b +
    texture(uWavePrev, vUv - ty).b + texture(uWavePrev, vUv + ty).b + hueTint * 2.0
  ) / 6.0;
  float nextE = avgE * 0.986;
  float nextTint = avgTint;

  // Inject acoustic impulses along exact string segments or drum points
  vec2 p = vec2(vUv.x * uAspect, vUv.y);
  for (int i = 0; i < ${MAX_IMPULSES}; i++) {
    if (i >= uImpCount) break;
    vec4 seg = uImpSeg[i];
    vec4 meta = uImpMeta[i];
    vec2 a = vec2(seg.x * uAspect, seg.y);
    vec2 b = vec2(seg.z * uAspect, seg.w);
    float freqNorm = meta.x; // 0 (low bass) .. 1 (high bell)
    float amp = meta.y;
    float phase = meta.z;
    float isPoint = meta.w;

    // Width of the wave source narrows with higher frequency
    float radius = mix(0.036, 0.014, freqNorm);
    float d;
    float u = 0.5;
    if (isPoint > 0.5) {
      d = length(p - a);
    } else {
      vec2 sd = segDist(p, a, b);
      d = sd.x;
      u = sd.y;
    }

    if (d < radius * 2.8) {
      float falloff = exp(-(d * d) / (radius * radius));
      // Standing-wave harmonic modulation along the string: higher notes have more spatial nodes
      float lobes = mix(1.0, 5.0, freqNorm);
      float spatial = isPoint > 0.5
        ? cos(d / radius * 1.4)
        : sin(u * 3.14159265 * lobes + phase) * sin(u * 3.14159265);
      float imp = falloff * spatial * amp * 0.42;
      nextH += imp;
      float eAdd = falloff * abs(amp) * 0.65;
      float lumTint = clamp(uImpCol[i].r * 0.35 + uImpCol[i].g * 0.55 + uImpCol[i].b * 0.95, 0.0, 1.0);
      nextTint = mix(nextTint, freqNorm * 0.65 + lumTint * 0.35, clamp(eAdd * 1.4, 0.0, 0.85));
      nextE = clamp(nextE + eAdd, 0.0, 1.5);
    }
  }

  // Soft clamp to prevent runaway oscillation on huge chords
  nextH = clamp(nextH, -2.5, 2.5);
  outWave = vec4(nextH, h, nextTint, nextE);
}
`;

// Subtle, complex acoustic caustic & cymatic wavefield renderer
const RENDER_FRAG_SRC = `#version 300 es
precision highp float;

in vec2 vUv;
out vec4 outColor;

uniform sampler2D uWave;
uniform vec2 uTexel;
uniform float uTime;
uniform float uAspect;
uniform float uIntensity;
uniform vec3 uBands; // sub, mid, air
uniform float uRms;
uniform vec3 uBgTop;
uniform vec3 uBgBot;
uniform vec3 uCausticTint;
uniform vec3 uAccentGlow;
uniform float uContourStr;
uniform float uCausticStr;
uniform float uChromaStr;
uniform vec2 uAirPad; // (echo, dark-thin)

// Smooth cosine palette for subtle iridescent wave interference
vec3 spectralPalette(float t) {
  vec3 a = vec3(0.45, 0.52, 0.65);
  vec3 b = vec3(0.35, 0.32, 0.35);
  vec3 c = vec3(1.0, 1.0, 1.0);
  vec3 d = vec3(0.05, 0.30, 0.58);
  return a + b * cos(6.28318 * (c * t + d));
}

// Subtle ambient slow interference field so silence feels like dark living water
float ambientWave(vec2 p, float t) {
  float w = 0.0;
  w += sin(p.x * 3.1 + t * 0.35 + sin(p.y * 2.2 - t * 0.22) * 0.8) * 0.5;
  w += sin(p.y * 4.3 - t * 0.28 + cos(p.x * 2.9 + t * 0.19) * 0.7) * 0.35;
  w += sin((p.x + p.y) * 5.7 + t * 0.41) * 0.15;
  return w;
}

float hash12(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * 0.1031);
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.x + p3.y) * p3.z);
}

void main() {
  // Base studio gradient (slightly deeper at top)
  vec3 col = mix(uBgBot, uBgTop, smoothstep(0.0, 1.0, vUv.y));

  vec4 wC = texture(uWave, vUv);
  float h = wC.r;
  float tintParam = wC.b;
  float energy = wC.a;

  // Spatial gradient & curvature (caustics)
  vec2 tx = vec2(uTexel.x * 1.5, 0.0);
  vec2 ty = vec2(0.0, uTexel.y * 1.5);
  float hL = texture(uWave, vUv - tx).r;
  float hR = texture(uWave, vUv + tx).r;
  float hD = texture(uWave, vUv - ty).r;
  float hU = texture(uWave, vUv + ty).r;

  vec2 grad = vec2(hR - hL, hU - hD);
  float slope = length(grad);
  float curv = max(0.0, (hL + hR + hD + hU) * 0.25 - h); // positive at caustic valleys/crests

  // Subtle ambient harmonic field coupled to sub/mid/air audio bands
  vec2 p = vec2((vUv.x - 0.5) * uAspect, vUv.y - 0.5);
  float amb = ambientWave(p * 2.4, uTime);
  float amb2 = ambientWave(p * 5.2 + grad * 1.4, -uTime * 0.65);
  float subBreath = (0.012 + uBands.x * 0.028 + uRms * 0.018) * uIntensity;
  col += uCausticTint * (amb * 0.5 + 0.5) * subBreath;

  // Fine acoustic silk filaments distorted by the live wave gradient
  float silk = sin((p.y * 28.0 + amb * 1.6 + h * 9.0) + uTime * 0.45);
  float silkLine = pow(max(0.0, 1.0 - abs(silk)), 6.0);
  col += uCausticTint * silkLine * (0.012 + uBands.y * 0.032 + energy * 0.025) * uIntensity;

  // Physical wave caustic ridges (bright, delicate highlights along wave slopes)
  float caustic = pow(clamp(slope * 3.8 + curv * 6.5, 0.0, 1.0), 1.65);
  vec3 waveHue = mix(uCausticTint, spectralPalette(tintParam + amb2 * 0.08 + uTime * 0.015), uChromaStr * 0.72);
  col += waveHue * caustic * (0.19 * uCausticStr * uIntensity);

  // Subtle translucent energy glow where waves interfere constructively
  float interference = abs(h) * (0.55 + 0.45 * energy);
  col += waveHue * clamp(interference * 0.14, 0.0, 0.16) * uIntensity;

  // Cymatic nodal isolines (subtle topographic rings along wave contours)
  if (uContourStr > 0.01) {
    float phaseContour = abs(fract(h * 11.0 + 0.5) - 0.5) * 2.0;
    float line = smoothstep(0.14, 0.0, phaseContour) * smoothstep(0.025, 0.14, abs(h));
    col += uAccentGlow * line * (0.14 * uContourStr * uIntensity);
  }

  // Subtle air-shimmer highlight on high-frequency energy
  float shimmer = pow(clamp(slope * 5.2, 0.0, 1.0), 3.0) * (0.35 + uBands.z * 0.9);
  col += uAccentGlow * shimmer * 0.08 * uIntensity;

  // Subtle Air Pad modulation tint when active
  if (uAirPad.x > 0.01) {
    col += uAccentGlow * uAirPad.x * 0.025 * (0.5 + 0.5 * sin(length(p) * 18.0 - uTime * 3.0));
  }

  // Soft studio vignette so center stage breathes and edges stay grounded
  float vig = 1.0 - dot(p * vec2(0.55, 0.75), p * vec2(0.55, 0.75)) * 0.42;
  col *= clamp(vig, 0.58, 1.04);

  // Gentle luminance ceiling to preserve "subtle, not noisy" clarity for foreground strings
  col = col / (vec3(1.0) + col * 0.55);

  // Micro-dither to prevent dark gradient banding
  col += (hash12(gl_FragCoord.xy + fract(uTime) * 100.0) - 0.5) / 255.0;

  outColor = vec4(col, 1.0);
}
`;

export class WavefieldRenderer {
  public canvas: HTMLCanvasElement;
  private gl: WebGL2RenderingContext | null = null;
  private ctx2d: CanvasRenderingContext2D | null = null;
  private stepProg: WebGLProgram | null = null;
  private renderProg: WebGLProgram | null = null;
  private fbos: [WebGLFramebuffer, WebGLFramebuffer] | null = null;
  private texs: [WebGLTexture, WebGLTexture] | null = null;
  private vao: WebGLVertexArrayObject | null = null;
  private curIdx = 0;
  private simW = 512;
  private simH = 288;
  private ok = false;

  // Fallback 2D ripples when WebGL2 float FBO is unavailable
  private fallbackRipples: Array<{ x: number; y: number; r: number; maxR: number; amp: number; color: string }> = [];

  constructor(canvas: HTMLCanvasElement) {
    this.canvas = canvas;
    this.initWebGL();
    if (!this.ok) {
      this.ctx2d = canvas.getContext('2d');
    }
  }

  private compileShader(gl: WebGL2RenderingContext, type: number, src: string): WebGLShader | null {
    const sh = gl.createShader(type);
    if (!sh) return null;
    gl.shaderSource(sh, src);
    gl.compileShader(sh);
    if (!gl.getShaderParameter(sh, gl.COMPILE_STATUS)) {
      console.warn('Wavefield shader compile error:', gl.getShaderInfoLog(sh));
      gl.deleteShader(sh);
      return null;
    }
    return sh;
  }

  private linkProgram(gl: WebGL2RenderingContext, vSrc: string, fSrc: string): WebGLProgram | null {
    const vs = this.compileShader(gl, gl.VERTEX_SHADER, vSrc);
    const fs = this.compileShader(gl, gl.FRAGMENT_SHADER, fSrc);
    if (!vs || !fs) return null;
    const prog = gl.createProgram();
    if (!prog) return null;
    gl.attachShader(prog, vs);
    gl.attachShader(prog, fs);
    gl.linkProgram(prog);
    gl.deleteShader(vs);
    gl.deleteShader(fs);
    if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) {
      console.warn('Wavefield program link error:', gl.getProgramInfoLog(prog));
      gl.deleteProgram(prog);
      return null;
    }
    return prog;
  }

  private initWebGL(): void {
    const gl = this.canvas.getContext('webgl2', {
      alpha: false,
      antialias: false,
      depth: false,
      stencil: false,
      preserveDrawingBuffer: true, // Needed for clean composite video recording
      powerPreference: 'high-performance',
    });
    if (!gl) return;

    const extFloat = gl.getExtension('EXT_color_buffer_float');
    const extHalf = gl.getExtension('EXT_color_buffer_half_float');
    if (!extFloat && !extHalf) return;
    gl.getExtension('OES_texture_float_linear');
    gl.getExtension('OES_texture_half_float_linear');

    const stepProg = this.linkProgram(gl, VERT_SRC, STEP_FRAG_SRC);
    const renderProg = this.linkProgram(gl, VERT_SRC, RENDER_FRAG_SRC);
    if (!stepProg || !renderProg) return;

    this.gl = gl;
    this.stepProg = stepProg;
    this.renderProg = renderProg;
    this.vao = gl.createVertexArray();

    if (!this.allocateFbos(this.simW, this.simH)) {
      this.gl = null;
      return;
    }
    this.ok = true;
  }

  private allocateFbos(w: number, h: number): boolean {
    const gl = this.gl;
    if (!gl) return false;

    if (this.fbos) {
      gl.deleteFramebuffer(this.fbos[0]);
      gl.deleteFramebuffer(this.fbos[1]);
    }
    if (this.texs) {
      gl.deleteTexture(this.texs[0]);
      gl.deleteTexture(this.texs[1]);
    }

    const createTarget = () => {
      const tex = gl.createTexture()!;
      gl.bindTexture(gl.TEXTURE_2D, tex);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA16F, w, h, 0, gl.RGBA, gl.HALF_FLOAT, null);

      const fbo = gl.createFramebuffer()!;
      gl.bindFramebuffer(gl.FRAMEBUFFER, fbo);
      gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, tex, 0);
      const status = gl.checkFramebufferStatus(gl.FRAMEBUFFER);
      return { tex, fbo, ok: status === gl.FRAMEBUFFER_COMPLETE };
    };

    const a = createTarget();
    const b = createTarget();
    gl.bindFramebuffer(gl.FRAMEBUFFER, null);
    if (!a.ok || !b.ok) return false;

    // Clear both buffers
    for (const fbo of [a.fbo, b.fbo]) {
      gl.bindFramebuffer(gl.FRAMEBUFFER, fbo);
      gl.viewport(0, 0, w, h);
      gl.clearColor(0, 0, 0, 0);
      gl.clear(gl.COLOR_BUFFER_BIT);
    }
    gl.bindFramebuffer(gl.FRAMEBUFFER, null);

    this.texs = [a.tex, b.tex];
    this.fbos = [a.fbo, b.fbo];
    this.simW = w;
    this.simH = h;
    return true;
  }

  public resize(w: number, h: number): void {
    this.canvas.width = w;
    this.canvas.height = h;
    if (this.ok && this.gl) {
      const targetW = w >= h ? 512 : 288;
      const targetH = w >= h ? 288 : 512;
      if (targetW !== this.simW || targetH !== this.simH) {
        this.allocateFbos(targetW, targetH);
      }
    }
  }

  public render(t: number, dt: number): void {
    const impulses = telemetry.drainImpulses(MAX_IMPULSES);
    const emitters = telemetry.getEmitters();

    if (!this.ok || !this.gl || !this.fbos || !this.texs || !this.stepProg || !this.renderProg) {
      this.renderFallback2D(t, dt, impulses, emitters);
      return;
    }

    const gl = this.gl;
    const aspect = this.canvas.width / Math.max(1, this.canvas.height);

    // Pack impulses + active continuous emitters (up to MAX_IMPULSES)
    const segData = new Float32Array(MAX_IMPULSES * 4);
    const metaData = new Float32Array(MAX_IMPULSES * 4);
    const colData = new Float32Array(MAX_IMPULSES * 3);
    let count = 0;

    const pushItem = (
      x0: number, y0: number, x1: number, y1: number,
      freqHz: number, amp: number, phase: number, isPoint: boolean,
      r: number, g: number, b: number,
    ) => {
      if (count >= MAX_IMPULSES) return;
      const freqNorm = clamp(Math.log2(Math.max(40, freqHz) / 55) / 5.5, 0, 1);
      segData[count * 4 + 0] = x0;
      segData[count * 4 + 1] = 1.0 - y0; // flip Y for WebGL UV
      segData[count * 4 + 2] = x1;
      segData[count * 4 + 3] = 1.0 - y1;
      metaData[count * 4 + 0] = freqNorm;
      metaData[count * 4 + 1] = amp;
      metaData[count * 4 + 2] = phase;
      metaData[count * 4 + 3] = isPoint ? 1.0 : 0.0;
      colData[count * 3 + 0] = r;
      colData[count * 3 + 1] = g;
      colData[count * 3 + 2] = b;
      count++;
    };

    for (const imp of impulses) {
      pushItem(imp.x0, imp.y0, imp.x1, imp.y1, imp.freqHz, imp.amp, t * 2.0, imp.isPoint, imp.r, imp.g, imp.b);
    }
    for (const em of emitters) {
      em.phase += dt * (4.0 + clamp(em.freqHz / 180, 0, 10));
      const osc = Math.sin(em.phase) * 0.28;
      pushItem(em.x0, em.y0, em.x1, em.y1, em.freqHz, em.amp * osc, em.phase, false, em.r, em.g, em.b);
    }

    gl.bindVertexArray(this.vao);

    // 2 wave simulation sub-steps per frame for crisp propagation speed
    gl.useProgram(this.stepProg);
    gl.viewport(0, 0, this.simW, this.simH);
    gl.uniform2f(gl.getUniformLocation(this.stepProg, 'uTexel'), 1 / this.simW, 1 / this.simH);
    gl.uniform1f(gl.getUniformLocation(this.stepProg, 'uAspect'), aspect);
    gl.uniform1f(gl.getUniformLocation(this.stepProg, 'uDamp'), 0.9865);
    gl.uniform1f(gl.getUniformLocation(this.stepProg, 'uSpeed'), 0.24);
    gl.uniform1f(gl.getUniformLocation(this.stepProg, 'uTime'), t);
    gl.uniform4fv(gl.getUniformLocation(this.stepProg, 'uImpSeg'), segData);
    gl.uniform4fv(gl.getUniformLocation(this.stepProg, 'uImpMeta'), metaData);
    gl.uniform3fv(gl.getUniformLocation(this.stepProg, 'uImpCol'), colData);

    for (let s = 0; s < 2; s++) {
      const srcIdx = this.curIdx;
      const dstIdx = 1 - this.curIdx;
      gl.bindFramebuffer(gl.FRAMEBUFFER, this.fbos[dstIdx]);
      gl.activeTexture(gl.TEXTURE0);
      gl.bindTexture(gl.TEXTURE_2D, this.texs[srcIdx]);
      gl.uniform1i(gl.getUniformLocation(this.stepProg, 'uWavePrev'), 0);
      // Only inject impulses on first sub-step
      gl.uniform1i(gl.getUniformLocation(this.stepProg, 'uImpCount'), s === 0 ? count : 0);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
      this.curIdx = dstIdx;
    }

    // Final caustic/cymatic screen pass
    const theme = THEMES[state.settings.theme];
    const bands = telemetry.bands;
    gl.bindFramebuffer(gl.FRAMEBUFFER, null);
    gl.viewport(0, 0, this.canvas.width, this.canvas.height);
    gl.useProgram(this.renderProg);
    gl.activeTexture(gl.TEXTURE0);
    gl.bindTexture(gl.TEXTURE_2D, this.texs[this.curIdx]);
    gl.uniform1i(gl.getUniformLocation(this.renderProg, 'uWave'), 0);
    gl.uniform2f(gl.getUniformLocation(this.renderProg, 'uTexel'), 1 / this.simW, 1 / this.simH);
    gl.uniform1f(gl.getUniformLocation(this.renderProg, 'uTime'), t);
    gl.uniform1f(gl.getUniformLocation(this.renderProg, 'uAspect'), aspect);
    gl.uniform1f(gl.getUniformLocation(this.renderProg, 'uIntensity'), state.settings.waveIntensity);
    gl.uniform3f(gl.getUniformLocation(this.renderProg, 'uBands'), bands.sub, bands.mid, bands.air);
    gl.uniform1f(gl.getUniformLocation(this.renderProg, 'uRms'), bands.rms);
    gl.uniform3fv(gl.getUniformLocation(this.renderProg, 'uBgTop'), theme.bgTop);
    gl.uniform3fv(gl.getUniformLocation(this.renderProg, 'uBgBot'), theme.bgBot);
    gl.uniform3fv(gl.getUniformLocation(this.renderProg, 'uCausticTint'), theme.causticTint);
    gl.uniform3fv(gl.getUniformLocation(this.renderProg, 'uAccentGlow'), theme.accentGlow);
    gl.uniform1f(gl.getUniformLocation(this.renderProg, 'uContourStr'), theme.contourStrength);
    gl.uniform1f(gl.getUniformLocation(this.renderProg, 'uCausticStr'), theme.causticStrength);
    gl.uniform1f(gl.getUniformLocation(this.renderProg, 'uChromaStr'), theme.chromaticStrength);
    gl.uniform2f(
      gl.getUniformLocation(this.renderProg, 'uAirPad'),
      state.fx ? state.fx.echo : 0,
      state.fx ? state.fx.dark - state.fx.thin : 0,
    );
    gl.drawArrays(gl.TRIANGLES, 0, 3);
  }

  private renderFallback2D(
    t: number,
    dt: number,
    impulses: WaveImpulse[],
    emitters: ContinuousEmitter[],
  ): void {
    const g = this.ctx2d;
    if (!g) return;
    const W = this.canvas.width, H = this.canvas.height;
    const theme = THEMES[state.settings.theme];
    const toCss = (c: [number, number, number]) =>
      `rgb(${Math.round(c[0] * 255)},${Math.round(c[1] * 255)},${Math.round(c[2] * 255)})`;

    const gr = g.createLinearGradient(0, 0, 0, H);
    gr.addColorStop(0, toCss(theme.bgTop));
    gr.addColorStop(1, toCss(theme.bgBot));
    g.fillStyle = gr;
    g.fillRect(0, 0, W, H);

    for (const imp of impulses) {
      this.fallbackRipples.push({
        x: ((imp.x0 + imp.x1) * 0.5) * W,
        y: ((imp.y0 + imp.y1) * 0.5) * H,
        r: 12,
        maxR: Math.max(W, H) * 0.65,
        amp: imp.amp,
        color: `rgb(${Math.round(imp.r * 255)},${Math.round(imp.g * 255)},${Math.round(imp.b * 255)})`,
      });
    }
    for (const em of emitters) {
      if (Math.random() < 0.25) {
        this.fallbackRipples.push({
          x: ((em.x0 + em.x1) * 0.5) * W,
          y: ((em.y0 + em.y1) * 0.5) * H,
          r: 16,
          maxR: Math.max(W, H) * 0.45,
          amp: em.amp * 0.5,
          color: `rgb(${Math.round(em.r * 255)},${Math.round(em.g * 255)},${Math.round(em.b * 255)})`,
        });
      }
    }

    // Subtle sine silk waves
    const bands = telemetry.bands;
    g.save();
    g.strokeStyle = `rgba(160,205,255,${(0.03 + bands.rms * 0.05) * state.settings.waveIntensity})`;
    g.lineWidth = 1.2;
    for (let row = 0; row < 9; row++) {
      const baseY = (row + 1) / 10 * H;
      g.beginPath();
      for (let x = 0; x <= W; x += 24) {
        const y = baseY + Math.sin(x * 0.008 + t * 0.8 + row) * (6 + bands.sub * 26);
        if (x === 0) g.moveTo(x, y); else g.lineTo(x, y);
      }
      g.stroke();
    }

    for (let i = this.fallbackRipples.length - 1; i >= 0; i--) {
      const rp = this.fallbackRipples[i];
      rp.r += dt * 210;
      const a = (1 - rp.r / rp.maxR) * 0.16 * rp.amp * state.settings.waveIntensity;
      if (a <= 0.003) {
        this.fallbackRipples.splice(i, 1);
        continue;
      }
      g.strokeStyle = rp.color;
      g.globalAlpha = a;
      g.lineWidth = 2;
      g.beginPath();
      g.arc(rp.x, rp.y, rp.r, 0, Math.PI * 2);
      g.stroke();
    }
    g.restore();
  }
}
