"""Validate the two editorial drafts and their actual Jekyll output.

Run from the repository root: python _review/roomescape-ctf/check_posts.py
Add --rendered after: bundle exec jekyll build --drafts -d _site-review
This checks publication structure only; challenge payloads are never executed.
"""
import argparse
import json
import re
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from PIL import Image


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.links = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "img":
            self.images.append(attrs.get("src", ""))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rendered", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    errors = []
    results = []
    authors = yaml.safe_load((root / "_data/authors.yml").read_text(encoding="utf-8"))
    existing_tags = set()
    for published in (root / "_posts").glob("*.md"):
        try:
            header = published.read_text(encoding="utf-8-sig").split("---", 2)[1]
            tags = yaml.safe_load(header).get("tags", []) or []
            existing_tags.update(tags if isinstance(tags, list) else [tags])
        except (IndexError, AttributeError, yaml.YAMLError):
            # Historical post syntax is outside this two-draft check.
            continue
    for part in (1, 3):
        slug = f"roomescape-ctf-part-{part}"
        path = root / "_drafts" / f"{slug}.md"
        text = path.read_text(encoding="utf-8")
        _, front, body = text.split("---\n", 2)
        meta = yaml.safe_load(front)
        for key in ("title", "description", "author", "categories", "tags", "comments", "math", "mermaid", "pin", "image"):
            if key not in meta:
                errors.append(f"{slug}: missing {key}")
        if meta.get("author") not in authors:
            errors.append(f"{slug}: author missing from authors.yml")
        if "date" in meta:
            errors.append(f"{slug}: publication date must remain undecided")
        tags = meta.get("tags", [])
        if not 3 <= len(tags) <= 5 or any(t != t.lower() or re.search(r"\s", t) for t in tags):
            errors.append(f"{slug}: invalid tags")
        for tag in tags:
            collisions = [old for old in existing_tags if old.lower() == tag and old != tag]
            if collisions:
                errors.append(f"{slug}: tag case conflicts with existing tags: {collisions}")
        expected_category = ["CTF", "Misc" if part == 1 else "Writeup"]
        if meta.get("categories") != expected_category:
            errors.append(f"{slug}: invalid categories")
        for key in ("comments", "math", "mermaid", "pin", "toc"):
            if type(meta.get(key)) is not bool:
                errors.append(f"{slug}: {key} is not boolean")
        fenced = False
        for number, line in enumerate(body.splitlines(), 1):
            if line.startswith("```"):
                fenced = not fenced
            if not fenced and re.match(r"^(<<<<<<< |=======\s*$|>>>>>>> )", line):
                errors.append(f"{slug}: merge marker at body line {number}")
        if fenced:
            errors.append(f"{slug}: unclosed code fence")
        if re.search(r"^# ", body, re.M):
            errors.append(f"{slug}: duplicate H1 under theme title")
        image_paths = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", body)
        for image in image_paths + ([meta["image"]] if meta["image"] else []):
            if not image.startswith("/assets/img/room-escape-ctf/"):
                errors.append(f"{slug}: image is not a site-root path: {image}")
                continue
            file = root / image.lstrip("/")
            if not file.is_file():
                errors.append(f"{slug}: missing image: {image}")
                continue
            try:
                with Image.open(file) as opened:
                    opened.verify()
            except Exception as exc:
                errors.append(f"{slug}: invalid image {image}: {exc}")
        if args.rendered:
            rendered = root / "_site-review/posts" / slug / "index.html"
            if not rendered.is_file():
                errors.append(f"{slug}: rendered HTML missing")
            else:
                page = Page()
                page.feed(rendered.read_text(encoding="utf-8"))
                for target, count in Counter(page.ids).items():
                    if count > 1:
                        errors.append(f"{slug}: duplicate rendered ID: {target}")
                for href in page.links:
                    parsed = urlsplit(href)
                    if href.startswith("#") and unquote(parsed.fragment) not in page.ids:
                        errors.append(f"{slug}: broken rendered anchor: {href}")
                    if parsed.path.startswith("/posts/roomescape-ctf-part-"):
                        if not (root / "_site-review" / parsed.path.lstrip("/") / "index.html").is_file():
                            errors.append(f"{slug}: broken series link: {href}")
                for image in page.images:
                    image_path = urlsplit(image).path
                    if "/room-escape-ctf/" in image_path and not (root / "_site-review" / image_path.lstrip("/")).is_file():
                        errors.append(f"{slug}: image missing from build: {image}")
        results.append({"part": part, "body_images": len(image_paths), "tags": len(tags), "source_lines": len(text.splitlines()), "rendered_checked": args.rendered})
    result = {"posts": results, "errors": errors, "passed": not errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    (root / "_review/roomescape-ctf/validation.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    raise SystemExit(bool(errors))


if __name__ == "__main__":
    main()
