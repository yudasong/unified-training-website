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

The plots summarize the paper's current results. The reasoning bars compare
final accuracy at matched RL horizons; the compute plots compare the best
observed checkpoints within total training budgets. Their selection conventions
are explained in the article and figure captions.
