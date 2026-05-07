#!/usr/bin/env python3
"""
Validate every SKILL.md in the Glare marketplace.

Usage (run from marketplace root):
    python3 scripts/validate-skills.py

Checks each SKILL.md for:
  - Opening and closing --- frontmatter delimiters
  - Valid YAML inside the frontmatter
  - Required fields: name, description
  - name field matches the folder name
  - description length within Anthropic's 1024-char limit
  - No bare "Word:" substrings inside the description value (would break YAML)
  - No duplicate names across the marketplace

Exits 0 if all skills pass, 1 if any fail.
"""

import os
import re
import sys
from collections import Counter

# Try pyyaml for richer parsing; fall back to manual extraction if unavailable.
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


def parse_frontmatter(fm_text):
    """Parse YAML frontmatter. Uses pyyaml if available, otherwise regex fallback."""
    if HAS_YAML:
        return yaml.safe_load(fm_text)
    # Fallback: extract name and description with regex (good enough for our 2 required fields)
    result = {}
    name_m = re.search(r"^name:\s*(.+)$", fm_text, re.MULTILINE)
    if name_m:
        result["name"] = name_m.group(1).strip()
    # description spans until the next top-level key or end of frontmatter
    desc_m = re.search(r"^description:\s*(.+?)(?=\n[a-z_]+:|\Z)", fm_text, re.MULTILINE | re.DOTALL)
    if desc_m:
        result["description"] = desc_m.group(1).strip()
    # version, source_doc_version, last_rebuilt
    for key in ("version", "source_doc_version", "last_rebuilt"):
        m = re.search(rf"^{key}:\s*(.+)$", fm_text, re.MULTILINE)
        if m:
            result[key] = m.group(1).strip()
    return result

SKILLS_DIR = "glare/skills"
MAX_DESCRIPTION_LENGTH = 1024

GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
DIM = "\033[2m"
RESET = "\033[0m"


def validate_skill(folder_name, skill_path):
    """Return list of issues for a single skill (empty list = clean)."""
    issues = []

    if not os.path.exists(skill_path):
        return [f"missing SKILL.md"]

    with open(skill_path, "rb") as f:
        raw = f.read()

    if raw.startswith(b"\xef\xbb\xbf"):
        issues.append("file starts with BOM (remove)")

    text = raw.decode("utf-8", errors="replace")
    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        issues.append(f"first line not '---' (got {lines[0][:50]!r})")
        return issues

    closing_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            closing_idx = i
            break

    if closing_idx is None:
        issues.append("no closing '---'")
        return issues

    fm_text = "\n".join(lines[1:closing_idx])

    try:
        parsed = parse_frontmatter(fm_text)
    except Exception as e:
        issues.append(f"YAML parse error: {str(e)[:120]}")
        return issues

    if not isinstance(parsed, dict):
        issues.append(f"frontmatter must be a YAML dict, got {type(parsed).__name__}")
        return issues

    name = parsed.get("name")
    desc = parsed.get("description")

    if not name:
        issues.append("missing 'name' field")
    elif name != folder_name:
        issues.append(f"name {name!r} != folder {folder_name!r}")

    if not desc:
        issues.append("missing 'description' field")
    elif not isinstance(desc, str):
        issues.append(f"description must be a string, got {type(desc).__name__}")
    else:
        if len(desc) > MAX_DESCRIPTION_LENGTH:
            issues.append(f"description {len(desc)} chars > {MAX_DESCRIPTION_LENGTH} max")
        if len(desc) < 50:
            issues.append(f"description {len(desc)} chars — too short to disambiguate")
        # Bare Word: substring breaks YAML if not quoted (re-parses as new key)
        bare_keys = re.findall(r"\s([A-Za-z][A-Za-z0-9_]*?):\s", desc)
        if bare_keys:
            issues.append(f"description contains bare 'Word:' substring(s): {bare_keys[:3]} (use em-dash or comma instead)")

    return issues


def main():
    if not os.path.isdir(SKILLS_DIR):
        print(f"{RED}ERROR{RESET}: {SKILLS_DIR}/ not found. Run from marketplace root.")
        sys.exit(2)

    folders = sorted(d for d in os.listdir(SKILLS_DIR) if os.path.isdir(os.path.join(SKILLS_DIR, d)))
    if not folders:
        print(f"{RED}ERROR{RESET}: no skill folders found in {SKILLS_DIR}/")
        sys.exit(2)

    results = []
    names_seen = []

    for folder in folders:
        skill_path = os.path.join(SKILLS_DIR, folder, "SKILL.md")
        issues = validate_skill(folder, skill_path)
        results.append((folder, issues))

        # Capture name for duplicate check
        if not issues or all("YAML parse error" not in i and "no closing" not in i and "first line" not in i for i in issues):
            try:
                with open(skill_path) as f:
                    m = re.match(r"^---\n(.*?)\n---\n", f.read(), re.DOTALL)
                if m:
                    parsed = parse_frontmatter(m.group(1))
                    if isinstance(parsed, dict) and parsed.get("name"):
                        names_seen.append(parsed["name"])
            except Exception:
                pass

    # Duplicate name check across marketplace
    name_counts = Counter(names_seen)
    duplicates = {n: c for n, c in name_counts.items() if c > 1}

    # Print report
    failed = [r for r in results if r[1]]
    passed = [r for r in results if not r[1]]

    for folder, issues in results:
        if not issues:
            print(f"  {GREEN}OK{RESET}   {folder}")
        else:
            print(f"  {RED}FAIL{RESET} {folder}")
            for issue in issues:
                print(f"         {DIM}-{RESET} {issue}")

    print()
    print(f"{DIM}─────────────────────────────────────{RESET}")
    print(f"  Total:   {len(results)}")
    print(f"  {GREEN}Passed:  {len(passed)}{RESET}")
    if failed:
        print(f"  {RED}Failed:  {len(failed)}{RESET}")
    if duplicates:
        print(f"  {YELLOW}Duplicate names: {duplicates}{RESET}")

    sys.exit(0 if not failed and not duplicates else 1)


if __name__ == "__main__":
    main()
