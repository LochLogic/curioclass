import fs from 'node:fs/promises';
import path from 'node:path';
import zlib from 'node:zlib';
import esbuild from 'esbuild';
import { minifyWgsl } from './wgsl-minify.mjs';

const ROOT = path.resolve(import.meta.dirname, '..');
const DIST_DIR = path.join(ROOT, 'dist');
const OUT_HTML = path.join(DIST_DIR, 'index.html');
const SIZE_LIMIT_BYTES = 2 * 1024 * 1024; // 2,097,152 bytes (strict 2 MiB; we also warn > 2,000,000)
const STRICT_LIMIT_BYTES = 2_000_000;

const isWatch = process.argv.includes('--watch');

const wgslPlugin = {
  name: 'wgsl-loader',
  setup(build) {
    build.onLoad({ filter: /\.wgsl$/ }, async (args) => {
      const raw = await fs.readFile(args.path, 'utf8');
      const code = minifyWgsl(raw);
      return {
        contents: `export default ${JSON.stringify(code)};`,
        loader: 'js',
      };
    });
  },
};

function formatKB(bytes) {
  return `${(bytes / 1024).toFixed(1)} kB`;
}

async function emitHtml(jsCode, cssCode) {
  const placeholderSize = '000.0 kB';
  const buildHtml = (sizeLabel) => `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Farlight</title>
<meta name="description" content="Farlight: fly a small ship home to Earth across a glowing galaxy, scanning planets, landing on living worlds and building camps. A free Recess game on Curio Class.">
<style>${cssCode}</style>
</head>
<body>
<canvas id="gpu-canvas"></canvas>
<div id="ui-root" data-bundle-size="${sizeLabel}"></div>
<script type="module">${jsCode}</script>
</body>
</html>`;

  // Measure actual final file size accurately
  const draft = buildHtml(placeholderSize);
  const finalSize = formatKB(Buffer.byteLength(draft, 'utf8'));
  const html = buildHtml(finalSize);
  await fs.mkdir(DIST_DIR, { recursive: true });
  await fs.writeFile(OUT_HTML, html, 'utf8');

  const rawBytes = Buffer.byteLength(html, 'utf8');
  const gzBytes = zlib.gzipSync(Buffer.from(html, 'utf8'), { level: 9 }).length;
  const pct = ((rawBytes / STRICT_LIMIT_BYTES) * 100).toFixed(2);

  console.log(`\n[FARLIGHT BUILD] ${OUT_HTML}`);
  console.log(`  Uncompressed : ${rawBytes.toLocaleString()} bytes (${formatKB(rawBytes)}), ${pct}% of 2.0 MB cap`);
  console.log(`  Gzip (lvl 9) : ${gzBytes.toLocaleString()} bytes (${formatKB(gzBytes)})`);

  if (rawBytes > STRICT_LIMIT_BYTES) {
    console.error(`\n[SIZE GATE FAILED] Bundle exceeded 2,000,000 bytes! (${rawBytes} bytes)`);
    process.exitCode = 1;
  } else {
    console.log(`  Size Gate    : PASS (${formatKB(STRICT_LIMIT_BYTES - rawBytes)} headroom remaining)\n`);
  }
}

async function runBuild() {
  const cssRaw = await fs.readFile(path.join(ROOT, 'src', 'ui', 'styles.css'), 'utf8');
  const cssMin = cssRaw
    .replace(/\/\*[\s\S]*?\*\//g, '')
    .replace(/\s+/g, ' ')
    .replace(/\s*([{:;,}])\s*/g, '$1')
    .trim();

  const ctx = await esbuild.context({
    entryPoints: [path.join(ROOT, 'src', 'main.ts')],
    bundle: true,
    format: 'esm',
    target: 'es2022',
    minify: !isWatch,
    write: false,
    metafile: true,
    plugins: [wgslPlugin],
  });

  const buildOnce = async () => {
    const result = await ctx.rebuild();
    const jsOut = result.outputFiles[0].text;
    await emitHtml(jsOut, cssMin);
  };

  await buildOnce();

  if (isWatch) {
    console.log('Watching for changes... (Ctrl+C to stop)');
    await ctx.watch();
  } else {
    await ctx.dispose();
  }
}

runBuild().catch((err) => {
  console.error(err);
  process.exit(1);
});
