#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import html
from urllib.parse import urlparse, parse_qs


def read_scholar_user_id_from_config(config_path: str) -> str:
    user_id = ""
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            for line in f:
                if "googlescholar" in line and ":" in line:
                    # line like: googlescholar    : "https://scholar.google.com/citations?user=IT5sfsYAAAAJ&hl=zh-CN"
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


def sanitize_slug(text: str) -> str:
    text = text.replace("{", "").replace("}", "").replace("\\", "")
    text = re.sub(r"\s+", "-", text.strip())
    text = re.sub(r"[^a-zA-Z0-9_-]", "", text)
    text = re.sub(r"-+", "-", text)
    return text.lower()


def html_escape(text: str) -> str:
    return html.escape(text, quote=True)


def build_citation(authors: str, title: str, venue: str, year: str) -> str:
    citation = ""
    if authors:
        citation += f"{authors}, "
    citation += f'"{title}."'
    if venue:
        citation += f" {venue}"
    if year:
        citation += f", {year}."
    return citation


def write_publication_md(output_dir: str, date_str: str, slug: str, title: str, venue: str, paper_url: str, citation: str) -> None:
    filename = f"{date_str}-{slug}.md"
    path = os.path.join(output_dir, filename)
    lines = []
    lines.append("---")
    lines.append(f"title: \"{html_escape(title)}\"")
    lines.append("collection: publications")
    lines.append(f"permalink: /publication/{date_str}-{slug}")
    lines.append(f"date: {date_str}")
    if venue:
        lines.append(f"venue: '{html_escape(venue)}'")
    if paper_url:
        lines.append(f"paperurl: '{paper_url}'")
    lines.append(f"citation: '{html_escape(citation)}'")
    lines.append("---")
    if paper_url:
        lines.append("")
        lines.append(f"[Access paper here]({paper_url}){{:target=\"_blank\"}}")
    content = "\n".join(lines) + "\n"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main() -> int:
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "_config.yml"))
    publications_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "_publications"))
    os.makedirs(publications_dir, exist_ok=True)

    user_id = read_scholar_user_id_from_config(config_path)
    if not user_id:
        raise SystemExit("Could not determine Google Scholar user id from _config.yml")

    try:
        from scholarly import scholarly
    except Exception as e:
        raise SystemExit("scholarly is not installed. Please install with: pip install scholarly")

    # Fetch author and publications
    author = scholarly.search_author_id(user_id)
    author = scholarly.fill(author, sections=["publications"])  # type: ignore

    # Optional: clear out existing generated publications first
    for name in os.listdir(publications_dir):
        if name.endswith(".md"):
            os.remove(os.path.join(publications_dir, name))

    for pub in author.get("publications", []):
        try:
            pub = scholarly.fill(pub)  # type: ignore
            bib = pub.get("bib", {})
            title = bib.get("title") or pub.get("bib", {}).get("title") or "Untitled"
            year = (str(bib.get("pub_year")) if bib.get("pub_year") else str(pub.get("year", ""))).strip()
            if not year or not year.isdigit():
                year = "1900"
            date_str = f"{year}-01-01"
            venue = bib.get("venue") or bib.get("journal") or bib.get("booktitle") or ""
            authors = bib.get("author") or ""
            # Prefer eprint_url (often PDFs); fallback to pub_url
            paper_url = pub.get("eprint_url") or pub.get("pub_url") or ""

            slug = sanitize_slug(title)
            citation = build_citation(authors, title, venue, year)
            write_publication_md(publications_dir, date_str, slug, title, venue, paper_url, citation)
        except Exception:
            # Skip problematic entries to ensure best-effort generation
            continue

    print("Publications generated from Google Scholar.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

