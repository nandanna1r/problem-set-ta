#!/usr/bin/env python3
"""Validate and package Problem-Set TA without third-party dependencies."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
NAME = "problem-set-ta"
SKILL_DIR = ROOT / "skills" / NAME
SKILL_FILE = SKILL_DIR / "SKILL.md"
MANIFEST_FILE = ROOT / ".codex-plugin" / "plugin.json"
DIST = ROOT / "dist"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)


def fail(message: str) -> None:
    raise SystemExit(f"error: {message}")


def validate() -> None:
    if not SKILL_FILE.is_file():
        fail(f"missing {SKILL_FILE.relative_to(ROOT)}")

    text = SKILL_FILE.read_text(encoding="utf-8")
    frontmatter = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not frontmatter:
        fail("SKILL.md must start with YAML frontmatter")
    header = frontmatter.group(1)
    if not re.search(rf"^name:\s*['\"]?{re.escape(NAME)}['\"]?\s*$", header, re.MULTILINE):
        fail(f"SKILL.md name must be {NAME!r}")
    if not re.search(r"^description:\s*\S", header, re.MULTILINE):
        fail("SKILL.md must have a non-empty description")

    try:
        manifest = json.loads(MANIFEST_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"invalid plugin manifest: {exc}")
    if manifest.get("name") != NAME:
        fail(f"plugin name must be {NAME!r}")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
        fail("plugin version must use strict semantic versioning")
    if manifest.get("skills") != "./skills/":
        fail("plugin manifest must point skills to './skills/'")
    interface = manifest.get("interface", {})
    for key in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        if not interface.get(key):
            fail(f"plugin interface.{key} is required")


def add_file(archive: ZipFile, source: Path, destination: Path) -> None:
    info = ZipInfo(destination.as_posix(), FIXED_TIME)
    info.compress_type = ZIP_DEFLATED
    info.external_attr = 0o100644 << 16
    archive.writestr(info, source.read_bytes())


def build_skill_bundle(target: Path) -> None:
    with ZipFile(target, "w") as archive:
        for source in sorted(path for path in SKILL_DIR.rglob("*") if path.is_file()):
            add_file(archive, source, Path(NAME) / source.relative_to(SKILL_DIR))


def build_plugin_bundle(target: Path) -> None:
    included = [MANIFEST_FILE, ROOT / "README.md", ROOT / "LICENSE"]
    included.extend(path for path in SKILL_DIR.rglob("*") if path.is_file())
    with ZipFile(target, "w") as archive:
        for source in sorted(included):
            add_file(archive, source, source.relative_to(ROOT))


def main() -> None:
    validate()
    DIST.mkdir(exist_ok=True)
    skill_bundle = DIST / f"{NAME}.skill"
    zip_bundle = DIST / f"{NAME}.zip"
    plugin_bundle = DIST / f"{NAME}-plugin.zip"
    build_skill_bundle(skill_bundle)
    shutil.copyfile(skill_bundle, zip_bundle)
    build_plugin_bundle(plugin_bundle)
    for artifact in (skill_bundle, zip_bundle, plugin_bundle):
        print(artifact.relative_to(ROOT))


if __name__ == "__main__":
    main()
