# SYNTHRA

Landing page for Drop 001 — Mirror Market Engine.

Expected live URL after Pages is approved:
https://jamiejet28-create.github.io/synthra-landing/
Waitlist: https://jamiejet28-create.github.io/synthra-landing/waitlist.html

## Status (rechecked 2026-09-27)
- `index.html` + `waitlist.html` + `.nojekyll` in repo root.
- Pages deploy workflow is on `main` (`.github/workflows/pages.yml`).
- Live URL still **404**. Pages source is not enabled.
- Formspree endpoint still `REPLACE_ME` on waitlist.html.

## Enable Pages (one-time — you must click)
Preferred (usually live in ~1 min, no workflow approval):
1. https://github.com/jamiejet28-create/synthra-landing/settings/pages
2. Source → **Deploy from a branch**
3. Branch = `main`, folder = `/ (root)` → Save

Alt: Source = **GitHub Actions**, then Approve the first workflow run if GitHub asks.

After the site loads, swap Formspree `REPLACE_ME` on `waitlist.html`.
