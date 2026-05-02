#!/usr/bin/env python3
"""Validate that every model card has the frontmatter the Jekyll site needs.

A card is any `<provider>/<model>.md` under a known provider directory. Each
must carry both the model-card schema (model_name, provider, model_version,
last_researched, card_version, researcher, sources) AND the Jekyll-nav key
(title) so just-the-docs renders a side-nav entry.

Run locally: `python3 scripts/validate_cards.py`
Run in CI:   .github/workflows/validate-cards.yml
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

PROVIDER_DIRS = {
    "alibaba", "anthropic", "cohere", "google", "meta",
    "mistral", "openai", "xai",
}

REQUIRED_MODEL_CARD_KEYS = {
    "model_name", "provider", "model_version", "last_researched",
    "card_version", "researcher", "sources",
}

REQUIRED_JEKYLL_KEYS = {"title", "parent"}

# Map of provider directory name → expected `parent:` value.
# A card under openai/ must declare `parent: OpenAI` so just-the-docs nests it
# under the OpenAI provider page in the side nav.
EXPECTED_PARENT_BY_DIR = {
    "alibaba": "Alibaba", "anthropic": "Anthropic", "cohere": "Cohere",
    "google": "Google", "meta": "Meta", "mistral": "Mistral",
    "openai": "OpenAI", "xai": "xAI",
}


def find_cards(root: Path) -> list[Path]:
    return sorted(
        p for p in root.glob("*/*.md")
        if p.parent.name in PROVIDER_DIRS and p.name != "index.md"
    )


def parse_frontmatter(card: Path) -> dict:
    text = card.read_text()
    if not text.startswith("---\n"):
        raise ValueError("missing opening --- on first line")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("missing closing --- (no body separator)")
    return yaml.safe_load(parts[1]) or {}


def validate_card(card: Path) -> list[str]:
    errors: list[str] = []
    try:
        fm = parse_frontmatter(card)
    except Exception as exc:
        return [f"frontmatter parse error: {exc}"]

    missing_model = REQUIRED_MODEL_CARD_KEYS - set(fm)
    if missing_model:
        errors.append(f"missing model-card keys: {sorted(missing_model)}")

    missing_jekyll = REQUIRED_JEKYLL_KEYS - set(fm)
    if missing_jekyll:
        errors.append(
            f"missing Jekyll-nav keys: {sorted(missing_jekyll)} "
            "(needed for just-the-docs side-nav rendering — "
            "add `title: <model-name>` to frontmatter)"
        )

    title = fm.get("title")
    if title and not isinstance(title, str):
        errors.append(f"title must be a string, got {type(title).__name__}")

    expected_parent = EXPECTED_PARENT_BY_DIR.get(card.parent.name)
    if expected_parent and fm.get("parent") and fm["parent"] != expected_parent:
        errors.append(
            f"parent must be '{expected_parent}' for cards under {card.parent.name}/, "
            f"got '{fm['parent']}'"
        )

    return errors


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    cards = find_cards(root)
    if not cards:
        print(f"No cards found under {root}/<provider>/*.md", file=sys.stderr)
        return 1

    failures: dict[Path, list[str]] = {}
    for card in cards:
        errors = validate_card(card)
        if errors:
            failures[card] = errors

    if failures:
        print(f"✗ {len(failures)} of {len(cards)} cards failed validation:\n")
        for card, errors in failures.items():
            rel = card.relative_to(root)
            print(f"  {rel}")
            for err in errors:
                print(f"    - {err}")
        return 1

    print(f"✓ All {len(cards)} cards have required frontmatter (model-card schema + Jekyll nav).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
