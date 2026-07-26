import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile, stat } from 'node:fs/promises';
import path from 'node:path';

const root = path.resolve(import.meta.dirname, '../..');
const text = (relative) => readFile(path.join(root, relative), 'utf8');
const exists = (relative) => stat(path.join(root, relative)).then(() => true, () => false);

function normalizedSvg(source) {
  return source.replace(/\s+/g, ' ').trim();
}

test('the hero explains the product before presenting calls to action', async () => {
  const html = await text('website/index.html');
  const styles = await text('website/assets/polish.css');

  assert.match(html, /One local API for all your AI providers\./);
  assert.match(html, /OpenAI, Anthropic, Gemini, Grok/);
  assert.match(html, /routes each request to an eligible account/);
  assert.match(html, /fails over before streaming\s+starts/);
  assert.match(html, /records usage locally/);
  assert.match(html, /class="hero-flow"/);
  assert.match(html, /aria-label="How the local gateway works"/);
  assert.match(styles, /\.hero-actions\s*\{[\s\S]*gap:\s*16px/);
  assert.match(styles, /\.hero-actions \.button[\s\S]*min-inline-size:\s*168px/);
  assert.match(styles, /\.button:focus-visible[\s\S]*outline:\s*3px solid/);
});

test('one balanced calendar-refresh icon is used across website, desktop, and packaging', async () => {
  const websiteIcon = await text('website/assets/icon.svg');
  const desktopIcon = await text('desktop/renderer/assets/icon.svg');
  const buildIcon = await text('build/icon.svg');
  const shell = await text('desktop/renderer/components/Shell.jsx');
  const app = await text('desktop/renderer/App.jsx');
  const pkg = JSON.parse(await text('package.json'));
  const manifest = JSON.parse(await text('website/manifest.webmanifest'));
  const readme = await text('README.md');

  assert.equal(normalizedSvg(websiteIcon), normalizedSvg(desktopIcon));
  assert.equal(normalizedSvg(websiteIcon), normalizedSvg(buildIcon));
  assert.match(websiteIcon, /rx="14"/);
  assert.match(websiteIcon, /id="calendar"/);
  assert.match(websiteIcon, /id="refresh-badge"/);
  assert.match(shell, /ProductIcon/);
  assert.match(app, /ProductIcon/);
  assert.equal(pkg.build.mac.icon, 'build/icon.svg');
  assert.equal(pkg.build.win.icon, 'build/icon.svg');
  assert.equal(pkg.build.linux.icon, 'build/icon.svg');
  assert.equal(manifest.icons.length, 1);
  assert.equal(manifest.icons[0].src, 'assets/icon.svg');
  assert.match(readme, /website\/assets\/icon\.svg/);
  assert.equal(await exists('build/icon.png'), false);
  assert.equal(await exists('website/assets/icon-512.png'), false);
  assert.equal(await exists('website/assets/social-card.png'), false);
});

test('website and desktop motion are purposeful and respect reduced-motion preferences', async () => {
  const websiteHtml = await text('website/index.html');
  const websiteStyles = await text('website/assets/polish.css');
  const websiteScript = await text('website/assets/site.js');
  const desktopStyles = await text('desktop/renderer/polish.css');
  const desktopEntry = await text('desktop/renderer/main.jsx');

  assert.match(websiteHtml, /assets\/polish\.css/);
  assert.match(websiteHtml, /data-reveal/);
  assert.match(websiteScript, /IntersectionObserver/);
  assert.match(websiteScript, /prefers-reduced-motion: reduce/);
  assert.match(websiteScript, /firstLink\?\.focus/);
  assert.match(websiteStyles, /\.reveal\s*\{[\s\S]*opacity:\s*0/);
  assert.match(websiteStyles, /\.reveal\.is-visible\s*\{[\s\S]*opacity:\s*1/);
  assert.match(websiteStyles, /@media \(prefers-reduced-motion: reduce\)/);
  assert.match(desktopEntry, /\.\/polish\.css/);
  assert.match(desktopStyles, /@keyframes page-enter/);
  assert.match(desktopStyles, /@media \(prefers-reduced-motion: reduce\)/);
  assert.match(desktopStyles, /\.reduce-motion/);
});

test('the social preview and documentation contract use the finished icon and motion rules', async () => {
  const html = await text('website/index.html');
  const social = await text('website/assets/social-card.svg');
  const docs = await text('docs/DESIGN_SYSTEM.md');

  assert.match(html, /social-card\.svg/);
  assert.match(social, /id="calendar"/);
  assert.match(social, /id="refresh-badge"/);
  assert.match(docs, /CTA groups use at least 16 px between adjacent actions/);
  assert.match(docs, /Motion is limited to opacity, color, and short spatial transitions/);
  assert.match(docs, /calendar with a refresh badge/);
});
