#!/usr/bin/env python3
"""Validate Windows theme assets and documentation links.

Checks JSON and YAML syntax and verifies that relative Markdown links resolve.
PowerShell syntax is validated separately in CI with the PowerShell parser.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

try:
    import yaml
except ImportError:  # pragma: no cover - local convenience
    yaml = None

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "__pycache__"}
LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(([^)]+)\)")
HREF_RE = re.compile(r'href=["\']([^"\']+)["\']')


def iter_files(suffix: str) -> list[Path]:
    files = []
    for path in ROOT.rglob(f"*{suffix}"):
        if path.is_file() and not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            files.append(path)
    return sorted(files)


def check_json(path: Path) -> str | None:
    try:
        with path.open(encoding="utf-8") as f:
            json.load(f)
    except (OSError, json.JSONDecodeError) as exc:
        return f"{path.relative_to(ROOT)}: {exc}"
    return None


def check_yaml(path: Path) -> str | None:
    if yaml is None:
        return None
    try:
        with path.open(encoding="utf-8") as f:
            yaml.safe_load(f)
    except (OSError, yaml.YAMLError) as exc:
        return f"{path.relative_to(ROOT)}: {exc}"
    return None


def check_links(path: Path) -> list[str]:
    issues = []
    text = path.read_text(encoding="utf-8", errors="replace")
    for raw in LINK_RE.findall(text) + HREF_RE.findall(text):
        target = unquote(raw.strip().split(" ", 1)[0])
        parsed = urlparse(target)
        if parsed.scheme or target.startswith(("#", "//", "/")):
            continue
        clean = target.split("#", 1)[0].split("?", 1)[0]
        if not clean:
            continue
        destination = (path.parent / clean).resolve()
        try:
            destination.relative_to(ROOT.resolve())
        except ValueError:
            continue
        if not destination.exists():
            issues.append(f"{path.relative_to(ROOT)}: broken link {target!r}")
    return issues


def main() -> int:
    errors: list[str] = []
    checked = 0

    for path in iter_files(".json"):
        checked += 1
        error = check_json(path)
        if error:
            errors.append(error)
    for path in iter_files(".yaml") + iter_files(".yml"):
        checked += 1
        error = check_yaml(path)
        if error:
            errors.append(error)
    for path in iter_files(".md"):
        checked += 1
        errors.extend(check_links(path))

    print(f"Validated {checked} files.")
    if errors:
        print("\nValidation failed:", file=sys.stderr)
        for error in errors:
            print(f"  {error}", file=sys.stderr)
        return 1

    print("All checked files are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
