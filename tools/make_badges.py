"""Generate the README badges as local SVG files in badges/.

The badges used to be hot-linked from img.shields.io, which GitHub fetches
through its camo image proxy. Those requests time out often enough that the
badges showed up as broken images with only their alt text. Serving the SVGs
from this repo removes that dependency.

Usage:
    python tools/make_badges.py              # all badges, followers from the API
    python tools/make_badges.py --followers  # only refresh badges/followers.svg

Icons are from Simple Icons (CC0): https://simpleicons.org
Set GITHUB_TOKEN to avoid the unauthenticated API rate limit.
"""

import json
import os
import sys
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "badges"
USER = "Zeyadmosalem"
FONT = 'font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision"'

ICONS = {
    "gmail": "M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z",
    "linkedin": "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z",
    "github": "M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12",
}

# Verdana 11px advance widths, enough for the strings these badges use.
WIDTHS = {
    " ": 3.87, "0": 6.99, "1": 6.99, "2": 6.99, "3": 6.99, "4": 6.99, "5": 6.99,
    "6": 6.99, "7": 6.99, "8": 6.99, "9": 6.99, ".": 3.5,
    "a": 6.68, "b": 6.86, "d": 6.86, "e": 6.6, "f": 3.87, "i": 3.0, "k": 6.5,
    "l": 3.0, "m": 10.7, "n": 6.98, "o": 6.68, "r": 4.69, "s": 5.73, "t": 4.33,
    "w": 9.0, "E": 6.83, "I": 4.62, "L": 6.1, "P": 6.64,
}


def text_width(s):
    return round(sum(WIDTHS.get(c, 7.0) for c in s))


# Line globe for the portfolio badge (the GitHub Pages logo is a wordmark,
# unreadable at 14px).
GLOBE = ('<g fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10"/>'
         '<ellipse cx="12" cy="12" rx="4.5" ry="10"/><path d="M2 12h20M4 6.5h16M4 17.5h16"/></g>')


def icon(name, x, y):
    # Simple Icons are 24x24; badges draw them at 14x14.
    body = GLOBE if name == "globe" else f'<path fill="#fff" d="{ICONS[name]}"/>'
    return f'<svg x="{x}" y="{y}" width="14" height="14" viewBox="0 0 24 24">{body}</svg>'



def flat(message, color, logo, label=None, label_color=None):
    """flat-square badge: optional label (with the logo) + message."""
    tw = text_width(message)
    if label is None:
        width = 5 + 14 + 4 + tw + 5
        cx = (23 + tw / 2) * 10
        rects = f'<rect width="{width}" height="20" fill="#{color}"/>'
        texts = f'<text x="{cx:g}" y="140" textLength="{tw * 10}" transform="scale(.1)">{message}</text>'
        title = message
    else:
        lw = text_width(label)
        left = 5 + 14 + 4 + lw + 5
        right = 5 + tw + 5
        width = left + right
        rects = (f'<rect width="{left}" height="20" fill="#{label_color}"/>'
                 f'<rect x="{left}" width="{right}" height="20" fill="#{color}"/>')
        texts = (f'<text x="{(23 + lw / 2) * 10:g}" y="140" textLength="{lw * 10}" transform="scale(.1)">{label}</text>'
                 f'<text x="{(left + right / 2) * 10:g}" y="140" textLength="{tw * 10}" transform="scale(.1)">{message}</text>')
        title = f"{label}: {message}"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="20" role="img" aria-label="{title}">'
            f'<title>{title}</title><g shape-rendering="crispEdges">{rects}</g>'
            f'{icon(logo, 5, 3)}'
            f'<g fill="#fff" text-anchor="middle" {FONT} font-size="110">{texts}</g></svg>\n')


def cta():
    """The for-the-badge call to action at the bottom of the README (same geometry as shields.io)."""
    t = "OPEN TO REMOTE WORK: GET IN TOUCH"
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="309.75" height="28" role="img" aria-label="{t}">'
            f'<title>{t}</title><g shape-rendering="crispEdges">'
            '<rect width="189.75" height="28" fill="#555"/><rect x="189.75" width="120" height="28" fill="#d12a3c"/></g>'
            f'{icon("gmail", 9, 7)}'
            f'<g fill="#fff" text-anchor="middle" {FONT} font-size="100">'
            '<text transform="scale(.1)" x="1033.75" y="175" textLength="1487.5">OPEN TO REMOTE WORK</text>'
            '<text transform="scale(.1)" x="2497.5" y="175" textLength="960" font-weight="bold">GET IN TOUCH</text>'
            '</g></svg>\n')


def followers():
    n = os.environ.get("FOLLOWERS")  # lets you pass the count in by hand
    if n is not None:
        return followers_badge(int(n))
    req = urllib.request.Request(f"https://api.github.com/users/{USER}",
                                 headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=20) as r:
        return followers_badge(json.load(r)["followers"])


def followers_badge(n):
    count = f"{n / 1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)
    return flat(count, "D12A3C", "github", label="followers", label_color="0A0407")


def write(name, svg):
    OUT.mkdir(exist_ok=True)
    (OUT / name).write_text(svg, encoding="utf-8")
    print("wrote", OUT / name)


if __name__ == "__main__":
    if "--followers" not in sys.argv:
        write("linkedin.svg", flat("LinkedIn", "D12A3C", "linkedin"))
        write("email.svg", flat("Email", "961A2A", "gmail"))
        write("portfolio.svg", flat("Portfolio", "EF4E5C", "globe"))
        write("open-to-work.svg", cta())
    write("followers.svg", followers())
