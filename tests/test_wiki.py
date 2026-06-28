from __future__ import annotations

import json
import re
from pathlib import Path


def test_generated_wiki_covers_catalog_and_has_valid_relative_links() -> None:
    root = Path(__file__).resolve().parents[1]
    wiki = root / "docs" / "wiki"
    manifest = json.loads((wiki / "manifest.json").read_text(encoding="utf-8"))
    catalog = json.loads((root / "catalog" / "resources.json").read_text(encoding="utf-8"))

    assert manifest["resources"] == catalog["resource_count"] == 100
    assert manifest["resource_pages"] == 100
    assert manifest["topics"] == 16

    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    broken: list[str] = []
    for page in wiki.rglob("*.md"):
        for href in link_pattern.findall(page.read_text(encoding="utf-8")):
            if "://" in href or href.startswith("#"):
                continue
            target = (page.parent / href.split("#", 1)[0]).resolve()
            if not target.exists():
                broken.append(f"{page.relative_to(wiki)} -> {href}")
    assert not broken
