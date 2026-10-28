# Unified Training website

Research blog for **Training Foundation Models with a Single Algorithm**.

Live site: https://yudasong.github.io/unified-training-website/

## Edit and preview

The site is a static research article in HTML and CSS. Edit `index.html` for
the article and `style.css` for presentation.
All figures are vector SVGs in `assets/`; the paper is `assets/paper.pdf`.

Preview locally with:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765. No installation or build step is needed.

GitHub Pages publishes the repository root on `main`. Push changes to update
the website. `.nojekyll` keeps the site as static files.

## Figure fidelity

The article reuses the paper's original figures. PDFs in `assets/` are exact
copies from the clean manuscript; SVGs are direct conversions for browser
viewing. No curves, colors, panels, or values are redrawn. The conceptual panel
is a vector crop of Figure 1 from `assets/paper.pdf`.

`assets/figure-sources.json` records source paths, conversion details, and hashes.
Wide figures preserve their full panel arrangement; narrow screens can scroll
horizontally or open the SVG/PDF at full size.
