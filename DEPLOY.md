# SYNTHRA Landing — Deploy Checklist

Live still 404 until transferred to Netlify/Vercel (preferred) or Pages enabled. Formspree still REPLACE_ME in waitlist.html.
Rechecked 2026-11-28 ~9:16 AM EST: https://jamiejet28-create.github.io/synthra-landing/ remains 404.

## Preferred: Transfer to Netlify or Vercel (no GitHub Pages needed, gets to 100%)
### Netlify Drop (fastest, no build needed):
1. Download repo as ZIP from https://github.com/jamiejet28-create/synthra-landing/archive/refs/heads/main.zip
2. Unzip, then go to https://app.netlify.com/drop (login or claim after)
3. Drag the unzipped folder (with index.html at root) to the Drop zone → instant .netlify.app URL
4. Once live, replace REPLACE_ME in waitlist.html form action with real Formspree ID, commit/push.
5. Update Notion with live URL → mark Done.

### Or Netlify from Git:
1. New site from Git → GitHub → select synthra-landing → main branch, publish dir = / (root), no build command.
2. Deploy.

### Vercel:
1. Go to https://vercel.com/new or https://vercel.com/drop
2. Import GitHub repo or drag ZIP/folder → Deploy (static detected).
3. Get .vercel.app URL.

Once live URL exists, Formspree fix + Notion update = Done. Transfer preferred over Pages.

## Alternative: GitHub Pages (user-only)
1. Go to https://github.com/jamiejet28-create/synthra-landing/settings/pages
2. Source: Deploy from a branch → main / root → Save
3. Wait ~1 min, confirm https://jamiejet28-create.github.io/synthra-landing/ loads
4. Create Formspree form → copy ID → replace REPLACE_ME in waitlist.html form action
5. Commit + push the Formspree ID change

No other blockers. Repo is clean. Transfer gets you to 100% faster.
