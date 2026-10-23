#!/usr/bin/env python3
"""Lake linter: lake.yaml identity, required frontmatter, unique ids, dead wikilinks.

Usage: python3 tools/check.py [lake_root]   (exit 1 on any error)
"""
import re
import sys
from pathlib import Path

REQUIRED = ("id", "tags", "status", "created", "updated")
STATUSES = {"draft", "experimental", "active", "deprecated", "open", "investigating", "resolved", "closed"}
SKIP_DIRS = {".git", ".github", ".obsidian", ".trash", ".ai", ".claude", "private"}
SKIP_FILES = {"README.md", "LICENSE", "CLAUDE.md", "AGENTS.md", "GEMINI.md"}

FM_RE = re.compile(r"\A---\n(.*?)\n---", re.S)
KEY_RE = re.compile(r"^([\w-]+):[ \t]*(.*(?:\n[ \t]+-.*)*)", re.M)  # value or block list
CODE_RE = re.compile(r"```.*?```|`[^`\n]*`|<!--.*?-->", re.S)  # code and placeholder comments
LAKE_KEY_RE = re.compile(r"^(\w+):[ \t]*([^#\n]*)", re.M)
LINK_RE = re.compile(r"\[\[([^\]|#\\]+)")


def check_lake_yaml(root: Path) -> list[str]:
    path = root / "lake.yaml"
    if not path.is_file():
        return ["lake.yaml: missing"]
    meta = {k: v.strip() for k, v in LAKE_KEY_RE.findall(path.read_text(encoding="utf-8"))}
    errors = [f"lake.yaml: missing '{k}'" for k in ("id", "role") if not meta.get(k)]
    if meta.get("role") and meta["role"] not in ("main", "member"):
        errors.append(f"lake.yaml: unknown role '{meta['role']}'")
    if meta.get("role") == "member" and not meta.get("extends"):
        errors.append("lake.yaml: member lake needs 'extends'")
    return errors


def check(root: Path) -> list[str]:
    errors = check_lake_yaml(root)
    files =[p for p in root.rglob("*") if p.is_file() and not SKIP_DIRS & set(p.relative_to(root).parts)]
    targets = {p.stem for p in files if p.suffix == ".md"} | {p.name for p in files}
    ids = {}

    for p in sorted(f for f in files if f.suffix == ".md" and f.name not in SKIP_FILES):
        rel = p.relative_to(root)
        text = p.read_text(encoding="utf-8")
        is_template = rel.parts[0] == "99_Templates" and rel.name.startswith("_tpl_")

        fm = FM_RE.match(text)
        if not fm:
            errors.append(f"{rel}: no frontmatter")
            continue
        if not is_template:
            meta = dict(KEY_RE.findall(fm.group(1)))
            errors += [f"{rel}: missing '{k}'" for k in REQUIRED if not meta.get(k)]
            if meta.get("status") and meta["status"] not in STATUSES:
                errors.append(f"{rel}: unknown status '{meta['status']}'")
            if meta.get("id"):
                ids.setdefault(meta["id"], []).append(str(rel))

        # Templates link to placeholders like [[RULE-XXX]]; skip them.
        if not is_template:
            for link in LINK_RE.findall(CODE_RE.sub("", text)):
                if link.strip().split("/")[-1] not in targets:
                    errors.append(f"{rel}: dead link [[{link}]]")

    errors += [f"duplicate id '{i}': {', '.join(ps)}" for i, ps in ids.items() if len(ps) > 1]
    return errors


if __name__ == "__main__":
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    errors = check(root)
    print("\n".join(errors) or f"ok: {root.name}")
    sys.exit(1 if errors else 0)
