# Unified Training website

Research blog for **Training Foundation Models with a Single Algorithm**.

Live site: https://yudasong.github.io/unified-training/

## Edit and preview

The site is a static research article in HTML, CSS, and vanilla JavaScript. Edit `index.html` for
the article and `style.css` for presentation.
All figures are vector SVGs in `assets/`. Paper links point to
https://arxiv.org/abs/2610.40564; `assets/paper.pdf` retains the local copy.
`assets/citation.bib` is the official export retrieved from
https://arxiv.org/bibtex/2610.40564, displayed verbatim in the bottom BibTeX section.

### Finding and editing the text in VS Code

Open this `website` folder in VS Code and edit **`index.html`**. It contains the
full article; there is no template engine or build step. Each paragraph has its
own block, with sentences on separate lines. Line breaks in the source do not
create line breaks on the page.

The file is divided into named `<!-- #region ... -->` blocks. Use the folding
arrows in the gutter to collapse the animation or sections you are not editing.
VS Code's **Fold All** and **Unfold All** commands are also useful. Search for a
section title or its stable HTML ID:

| What to edit | Find in `index.html` |
| --- | --- |
| Title, authors, affiliations, and project links | `paper-header` |
| Left navigation links | `article-contents` |
| Opening animation and its caption | `training-animation` |
| Introductory paragraphs | `class="opening"` |
| A unified likelihood formulation | `id="one-rule"` |
| Midtraining across the full training pipeline | `id="same-data"` |
| Accuracy and coverage under a total compute budget | `id="compute"` |
| Retention of pretrained capabilities | `id="retention"` |
| Heterogeneous midtraining data | `id="mixtures"` |
| Scheduling midtraining data during RL | `id="schedules"` |
| Continual learning after mathematical RL | `id="next-task"` |
| Future directions | `id="looking-ahead"` |
| BibTeX citation | `id="bibtex"` |

Within each section, edit the `<p>` paragraphs, `<li>` list items,
`<figcaption>` captions, or `<aside class="takeaway">` summary. Keep the existing
IDs and classes unless you also intend to change navigation or styling.
The folder's `.vscode/settings.json` enables soft wrapping and two-space
indentation for HTML when this folder is opened directly; it does not change
your global VS Code settings or the manuscript's LaTeX configuration.

Preview locally with:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765. No installation or build step is needed.

### Paragraph typesetting

Article paragraphs, list items, figure captions, and takeaway boxes use
**tex-linebreak 0.9.0** on desktop and mobile to choose line breaks across each text block.
Titles, author information, navigation, and animation labels keep their original
layout. The typesetter tries whole words first, then permits
hyphenation if needed to meet its spacing constraint. Only lowercase words of at
least nine letters are eligible, with at least three letters on either side of
a break; abbreviations and existing compounds stay intact. If needed, a second
pass limits hyphenation to words of at least twelve letters before falling back
to whole words. It avoids too many hyphens (two per paragraph, increasing to
roughly one per five lines for longer blocks). Consecutive hyphenated lines are
avoided, with at most two allowed in narrow columns.
The text
remains in `index.html`; no compilation is needed after editing. The bundled
library is in `assets/vendor/tex-linebreak/`, and `typography.js` applies it after
fonts load and recalculates when the column width changes, including phone
rotation. Print uses normal browser wrapping.

Compare the introduction at `index.html#opening` with
`index.html?typesetting=browser#opening` (ordinary browser justification), or
`index.html?typesetting=nohyphens#opening` (TeX layout without hyphens).
Both URLs also work with the local HTTP preview. To disable TeX typesetting, remove
the three typesetting script tags near the bottom of `index.html`.

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
reconstruct or interpolate the plotted results. Both panels advance using one
cumulative compute budget. The end of staged midtraining aligns with the first
staged pre-RL evaluation in the plot (the one-epoch configuration), and unified
RL starts at its earlier pre-RL evaluation. The curves are envelopes across
multiple configurations; the left panel is not one run underlying every point.
Data proportions and the equal-width staged phases remain illustrative.
Animation time is compressed during pretraining, and the two RL onsets are
shown close together (23% and 28% of playback) to avoid exaggerating their
small difference in cumulative compute. Their schematic positions are 235/400
and 266.667/400. Both panels still reach the same compute value at each instant;
the remaining time follows the plotted RL compute range.

The module uses `teaser-animation.css`; its HTML is embedded in `index.html`
and retained in `teaser-animation.html` for editing. Keep both copies in sync.
`assets/teaser-animation-data.json` records the original plot and compute bounds.
The animation includes pause, replay, and scrubbing controls, honors reduced
motion, pauses out of view, and shows the complete original figure without JS.
