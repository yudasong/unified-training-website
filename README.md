# Unified Training website

Research blog for **Training Foundation Models with a Single Algorithm**.

Live site: https://yudasong.github.io/unified-training/

## Edit and preview

The site is a static research article in HTML, CSS, and vanilla JavaScript. Edit `index.html` for
the article and `style.css` for presentation.
All figures are vector SVGs in `assets/`; the paper is `assets/paper.pdf`.

Preview locally with:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765. No installation or build step is needed.

The editable source remains in this repository. The public site is hosted in the
`unified-training/` folder of `yudasong/yudasong.github.io` on its `master` branch.
After committing and pushing source changes here, publish with:

```bash
python3 publish.py
```

The script copies only the site's static files into that project folder, commits
any changes there, and pushes them. It leaves the rest of the personal site
unchanged. The former `unified-training-website/` address redirects to the new URL,
preserving query parameters and section anchors.

## Writing

The audience is ML and LLM researchers. Retain the paper’s terminology and reuse
its wording where it already works. Shorten derivations and implementation detail
without replacing precise concepts with lay explanations. Results sections should
explain the motivation, comparison, finding, and implication, including material
tradeoffs. Use bullets when they make parallel settings or distinct findings easier
to compare; do not impose a list on every results section or invent a label for
each sentence. Keep closely connected findings, the main argument, and
interpretation in prose. Avoid slogans, a long literature review, and narrating
every plotted value.

## Figure fidelity

The article reuses the paper's original figures. PDFs in `assets/` are exact
copies from the clean manuscript; SVGs are direct conversions for browser
viewing. No curves, colors, panels, or values are redrawn. The conceptual panel
is a vector crop of Figure 1, and the token-weight diagram is a vector crop of
Figure 2, from `assets/paper.pdf`.

`assets/figure-sources.json` records source paths, conversion details, and hashes.
Figures preserve their full panel arrangement and scale within the article column.
The contents navigation stays to the left on desktop and becomes an inline list
on narrow screens.

## Opening animation

`teaser-animation.js` reveals the four original curves in
`assets/teaser_reasoning.svg` as cumulative compute increases. It does not
reconstruct or interpolate the plotted results. The left schedules illustrate
data-source timing; their proportions and phase lengths are schematic.

The module uses `teaser-animation.css`; its HTML is embedded in `index.html`
and retained in `teaser-animation.html` for editing. Keep both copies in sync.
`assets/teaser-animation-data.json` records the original plot and compute bounds.
The animation includes pause, replay, and scrubbing controls, honors reduced
motion, pauses out of view, and shows the complete original figure without JS.
