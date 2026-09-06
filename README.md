# Portfolio Site

A single-page portfolio, generated from Python and hosted free on GitHub Pages.
No server, no framework, no Python runtime needed once it's live, just a
plain `index.html` + CSS file that GitHub serves as-is.

## How it works

- **`content.py`** — all your text lives here (name, about blurb, experience,
  project, skills, contact links). Edit this file to change what the site says.
- **`templates/index.html.j2`** — the page structure (Jinja2 template). You
  shouldn't need to touch this unless you want to change the layout.
- **`static/css/style.css`** — all the styling.
- **`generate_site.py`** — reads `content.py`, fills in the template, and
  writes out a plain `index.html` in the project root. This is the only
  script you run.

## Adding your contact links

Open `content.py` and find the `CONTACT` dictionary near the top:

```python
CONTACT = {
    "email": None,
    "linkedin": None,
    "github": None,
}
```

Fill in real values, for example:

```python
CONTACT = {
    "email": "mailto:scott.hodgins@example.com",
    "linkedin": "https://linkedin.com/in/scotthodgins",
    "github": "https://github.com/scotthodgins",
}
```

Then rebuild the site (see below). Any value left as `None` will just be
skipped on the live page.

## Rebuilding the site after edits

Every time you change `content.py` (or the template/CSS), run:

```bash
pip install -r requirements.txt   # only needed once
python generate_site.py
```

This overwrites `index.html`. Open it directly in a browser to preview
your changes before pushing.

## Deploying to GitHub Pages

You have two options. Option A gives you a URL like `yourname.github.io`
(the "main" personal site). Option B gives you `yourname.github.io/reponame`
and is useful if you want this alongside other project repos.

### Option A: personal site (`yourname.github.io`)

1. On GitHub, create a **new repository** named exactly `yourusername.github.io`
   (replace `yourusername` with your actual GitHub username).
2. In this project folder, run:
   ```bash
   git init
   git add .
   git commit -m "Initial portfolio site"
   git branch -M main
   git remote add origin https://github.com/yourusername/yourusername.github.io.git
   git push -u origin main
   ```
3. Go to the repo on GitHub → **Settings** → **Pages**.
4. Under "Build and deployment", set **Source** to "Deploy from a branch",
   branch `main`, folder `/ (root)`. Save.
5. Within a minute or two, your site will be live at
   `https://yourusername.github.io`.

### Option B: project site (`yourusername.github.io/reponame`)

Same steps as above, but name the repo anything you like (e.g. `portfolio`).
Your site will be live at `https://yourusername.github.io/portfolio`.

## Updating the live site later

Any time you edit `content.py`:

```bash
python generate_site.py
git add .
git commit -m "Update content"
git push
```

GitHub Pages will redeploy automatically within a minute or so.
