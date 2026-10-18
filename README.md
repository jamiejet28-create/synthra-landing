# SYNTHRA

Landing page and early-access waitlist for Drop 001 — Mirror Market Engine.

- Live URL (once Pages is activated): https://jamiejet28-create.github.io/synthra-landing/
- Waitlist URL: https://jamiejet28-create.github.io/synthra-landing/waitlist.html

## Project Structure

- `index.html`: Main landing page for Drop 001. Built with pure CSS cyber-synth visual styling, zero external image asset dependencies, responsive layout, SEO/Open Graph metadata, and inline SVG favicon.
- `waitlist.html`: Waitlist signup page. Features dual-mode submission: submits to Formspree if configured, or automatically falls back to client-side `localStorage` with JSON export functionality so no leads are lost.
- `.nojekyll`: Instructs GitHub Pages to serve static files directly without Jekyll processing.
- `tests/test_site.py`: Automated validation suite checking HTML structure, anchor IDs, internal links, CSS asset resolution, SEO metadata, and waitlist cleanliness.
- `.github/workflows/ci.yml`: Automated CI workflow executing site validation tests on push and pull requests.
- `.github/workflows/pages.yml`: Deployment workflow targeting GitHub Pages.

## Local Testing

Run the automated validation suite locally:

```bash
python3 -m unittest discover -s tests -v
```

To preview the landing page locally:

```bash
python3 -m http.server 8000
```
Then open `http://localhost:8000` in your browser.

## Known External Bottlenecks (Action Required)

1. **GitHub Pages Source Activation**:
   GitHub Actions tokens cannot self-provision Pages without repository administration rights. The repo owner must manually enable Pages once:
   - Go to [Repository Pages Settings](https://github.com/jamiejet28-create/synthra-landing/settings/pages).
   - Under **Build and deployment > Source**, select **Deploy from a branch** (Branch: `main`, folder: `/ (root)`), or select **GitHub Actions**.
   - Save changes.

2. **Formspree Endpoint Configuration**:
   - `waitlist.html` currently targets `https://formspree.io/f/REPLACE_ME`.
   - Client submissions are safely captured in browser `localStorage` and can be exported as JSON via the **Export saved emails** button.
   - Once a Formspree form is created, replace `REPLACE_ME` in `waitlist.html` with your Formspree form ID to receive emails directly.

