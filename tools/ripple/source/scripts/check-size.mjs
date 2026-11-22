import fs from 'node:fs';
import path from 'node:path';

const LIMIT = 2 * 1024 * 1024; // 2 MB
const target = path.resolve('dist/index.html');

if (!fs.existsSync(target)) {
  console.error('Missing dist/index.html');
  process.exit(1);
}

const bytes = fs.statSync(target).size;
const kb = (bytes / 1024).toFixed(1);
const pct = ((bytes / LIMIT) * 100).toFixed(1);
console.log(`\nStandalone bundle: dist/index.html -> ${kb} KB (${bytes.toLocaleString()} bytes, ${pct}% of 2 MB limit)`);

if (bytes >= LIMIT) {
  console.error(`ERROR: Bundle exceeds 2 MB limit by ${((bytes - LIMIT) / 1024).toFixed(1)} KB!`);
  process.exit(1);
}
console.log('Size check PASSED (< 2 MB).\n');
