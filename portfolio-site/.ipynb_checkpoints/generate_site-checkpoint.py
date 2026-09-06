#!/usr/bin/env python3
"""
Generates index.html from templates/index.html.j2 using the content
defined in content.py. Run this any time you edit content.py:

    python generate_site.py

GitHub Pages serves plain HTML/CSS/JS, so this script's only job is to
turn your Python content into a static index.html file that Pages can host.
"""

from jinja2 import Environment, FileSystemLoader
import content

def short_about(text, max_chars=170):
    """Trim the full About paragraph down to a one-line hero intro."""
    if len(text) <= max_chars:
        return text
    cut = text[:max_chars].rsplit(" ", 1)[0]
    return cut.rstrip(",.") + "\u2026"

def main():
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("index.html.j2")

    html = template.render(
        name=content.NAME,
        tagline=content.TAGLINE,
        contact=content.CONTACT,
        about=content.ABOUT,
        about_short=short_about(content.ABOUT),
        experience=content.EXPERIENCE,
        project=content.PROJECT,
        skills=content.SKILLS,
        footer_note=content.FOOTER_NOTE,
    )

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("Built index.html")

if __name__ == "__main__":
    main()
