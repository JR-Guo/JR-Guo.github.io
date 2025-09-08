#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import html
from urllib.parse import urlparse, parse_qs, urlencode
from urllib.request import Request, urlopen


def read_scholar_user_id_from_config(config_path: str) -> str:
    user_id = ""
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            for line in f:
                if "googlescholar" in line and ":" in line:
                    parts = line.split(":", 1)
                    if len(parts) == 2:
                        url = parts[1].strip().strip('"').strip()
                        try:
                            parsed = urlparse(url)
                            qs = parse_qs(parsed.query)
                            user_id = qs.get("user", [""])[0]
                            if user_id:
                                return user_id
                        except Exception:
                            continue
    except FileNotFoundError:
        pass
    return user_id


def fetch_scholar_profile_html(user_id: str, hl: str = "en") -> str:
    base = "https://scholar.google.com/citations"
    params = {
        "user": user_id,
        "hl": hl,
        "view_op": "list_works",
        "sortby": "pubdate",
        "cstart": "0",
        "pagesize": "100"
    }
    url = f"{base}?{urlencode(params)}"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9"
    }
    req = Request(url, headers=headers)
    with urlopen(req, timeout=20) as resp:
        content = resp.read().decode("utf-8", errors="ignore")
        return content


def parse_publications(html_text: str):
    # Very lightweight parsing using regex tailored to Scholar's markup
    # Each row is a publication
    rows = re.findall(r"<tr class=\\\"gsc_a_tr\\\">(.*?)</tr>", html_text, flags=re.S)
    publications = []
    for row in rows:
        # Title
        m_title = re.search(r"<a class=\\\"gsc_a_at\\\".*?>(.*?)</a>", row, flags=re.S)
        title = html.unescape(m_title.group(1)).strip() if m_title else "Untitled"

        # Authors and venue line
        m_tu = re.search(r"<div class=\\\"gsc_a_tu\\\">(.*?)</div>", row, flags=re.S)
        tu_text = html.unescape(re.sub(r"<.*?>", " ", m_tu.group(1))).strip() if m_tu else ""

        # Year
        m_year = re.search(r"<span class=\\\"gsc_a_h gsc_a_hc gs_ibl\\\">(\d{4})</span>", row)
        year = m_year.group(1) if m_year else "1900"

        # Link to publication page (if available)
        m_link = re.search(r"<a class=\\\"gsc_a_at\\\" href=\\\"(.*?)\\\"", row)
        pub_rel = html.unescape(m_link.group(1)) if m_link else ""
        pub_url = f"https://scholar.google.com{pub_rel}" if pub_rel else ""

        publications.append({
            "title": re.sub(r"\s+", " ", title),
            "meta": re.sub(r"\s+", " ", tu_text),
            "year": year,
            "url": pub_url
        })
    return publications


def sanitize_slug(text: str) -> str:
    text = text.replace("{", "").replace("}", "").replace("\\", "")
    text = re.sub(r"\s+", "-", text.strip())
    text = re.sub(r"[^a-zA-Z0-9_-]", "", text)
    text = re.sub(r"-+", "-", text)
    return text.lower()


def write_publication_md(output_dir: str, pub: dict):
    title = pub.get("title", "Untitled")
    year = pub.get("year", "1900")
    venue = pub.get("meta", "")
    paper_url = pub.get("url", "")
    slug = sanitize_slug(title)
    date_str = f"{year}-01-01"

    citation = title
    if venue:
        citation = f'"{title}." {venue}, {year}.'
    else:
        citation = f'"{title}." {year}.'

    filename = f"{date_str}-{slug}.md"
    path = os.path.join(output_dir, filename)
    lines = []
    lines.append("---")
    lines.append(f"title: \"{html.escape(title, quote=True)}\"")
    lines.append("collection: publications")
    lines.append(f"permalink: /publication/{date_str}-{slug}")
    lines.append(f"date: {date_str}")
    if venue:
        lines.append(f"venue: '{html.escape(venue, quote=True)}'")
    if paper_url:
        lines.append(f"paperurl: '{paper_url}'")
    lines.append(f"citation: '{html.escape(citation, quote=True)}'")
    lines.append("---")
    if paper_url:
        lines.append("")
        lines.append(f"[Access paper here]({paper_url}){{:target=\"_blank\"}}")
    content = "\n".join(lines) + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main() -> int:
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    config_path = os.path.join(root, "_config.yml")
    publications_dir = os.path.join(root, "_publications")
    os.makedirs(publications_dir, exist_ok=True)

    user_id = read_scholar_user_id_from_config(config_path)
    if not user_id:
        print("Could not determine Google Scholar user id from _config.yml", file=sys.stderr)
        return 2

    try:
        html_text = fetch_scholar_profile_html(user_id)
    except Exception as e:
        print(f"Failed to fetch Google Scholar page: {e}", file=sys.stderr)
        return 3

    pubs = parse_publications(html_text)
    if not pubs:
        print("No publications parsed. Google may have blocked the request.", file=sys.stderr)
        return 4

    # Clear existing files
    for name in os.listdir(publications_dir):
        if name.endswith(".md"):
            try:
                os.remove(os.path.join(publications_dir, name))
            except Exception:
                pass

    for pub in pubs:
        try:
            write_publication_md(publications_dir, pub)
        except Exception:
            continue

    print(f"Generated {len(pubs)} publications from Google Scholar.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

