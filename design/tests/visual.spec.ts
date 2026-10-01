// Visual acceptance: every route at 1440 (1x) and 390 (2x) against the canvas references.
// npm i -D @playwright/test pixelmatch pngjs sharp && BASE_URL=http://localhost:3000 npx playwright test
import { test, expect } from '@playwright/test';
import fs from 'node:fs';
import path from 'node:path';
import sharp from 'sharp';
import pixelmatch from 'pixelmatch';

const ROOT = path.resolve(__dirname, '..');
const spec = JSON.parse(fs.readFileSync(path.join(ROOT, 'spec/routes.json'), 'utf8'));
const BASE = process.env.BASE_URL ?? 'http://localhost:3000';
const FREEZE = '*,*::before,*::after{animation-play-state:paused!important;animation-delay:-3.5s!important;transition:none!important;caret-color:transparent!important}';

const url = (route: string) => (route.startsWith('app:') ? BASE + route.slice(4) : BASE + route);

for (const r of spec.routes) {
  if (r.route.endsWith('.pdf')) continue;                     // the price sheet is checked as a PDF, by eye
  for (const side of ['desktop', 'phone'] as const) {
    const s = r[side];
    if (!s) continue;
    test(`${r.route} · ${side}`, async ({ browser }) => {
      const scale = s.reference_scale ?? 1;
      const page = await browser.newPage({ viewport: { width: s.width, height: 900 }, deviceScaleFactor: scale });
      await page.goto(url(r.route), { waitUntil: 'networkidle' });
      await page.addStyleTag({ content: FREEZE });
      await page.evaluate(() => document.fonts.ready);
      const shot = await page.screenshot({ fullPage: true });
      await page.close();

      const ref = sharp(path.join(ROOT, s.reference)).ensureAlpha();
      const { width: rw, height: rh } = await ref.metadata() as { width: number; height: number };
      const got = sharp(shot).ensureAlpha();
      const { width: gw, height: gh } = await got.metadata() as { width: number; height: number };
      expect(gw, 'width').toBe(rw);
      expect(Math.abs(gh - rh) / scale, 'page height within 4px of the reference').toBeLessThanOrEqual(4);

      const h = Math.min(gh, rh);
      const a = await ref.extract({ left: 0, top: 0, width: rw, height: h }).raw().toBuffer();
      const b = await got.extract({ left: 0, top: 0, width: rw, height: h }).raw().toBuffer();
      const diff = Buffer.alloc(rw * h * 4);
      const bad = pixelmatch(a, b, diff, rw, h, { threshold: 0.1 });
      const share = bad / (rw * h);
      if (share > 0.005) {
        const out = path.join(ROOT, 'tests/diff');
        fs.mkdirSync(out, { recursive: true });
        await sharp(diff, { raw: { width: rw, height: h, channels: 4 } }).png().toFile(path.join(out, `${r.slug}-${side}.png`));
      }
      expect(share, `${(share * 100).toFixed(2)}% of pixels differ (diff in tests/diff)`).toBeLessThanOrEqual(0.005);
    });
  }
}
