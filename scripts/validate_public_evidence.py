#!/usr/bin/env python3
"""Fail closed on stale, broken, or obviously unsafe public evidence."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_FILES = sorted(ROOT.glob("*.md")) + sorted((ROOT / "evidence").glob("*.md"))
REQUIRED = {
    "README.md",
    "evidence/assurance-boundary.md",
    "evidence/nist-csf-2-current-profile.md",
    "evidence/secure-development.md",
    "evidence/risk-register.md",
    "evidence/internal-review-2026-08-18.md",
    "evidence/restricted-evidence-register.md",
}
FORBIDDEN = {
    "private_key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "github_token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "jwt": re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b"),
    "home_path": re.compile(r"/(?:Users|home)/[^/\s]+/"),
    "service_role_value": re.compile(r"(?i)service[_-]?role\s*[=:]\s*['\"]?[A-Za-z0-9._-]{12,}"),
}


def fail(message: str) -> None:
    raise SystemExit(message)


missing = sorted(path for path in REQUIRED if not (ROOT / path).is_file())
if missing:
    fail(f"missing required evidence: {', '.join(missing)}")

for path in TEXT_FILES:
    text = path.read_text(encoding="utf-8")
    if not re.search(r"^(?:Reviewed|Review date|Register date): 20\d{2}-\d{2}-\d{2}$", text, re.MULTILINE) and path.name != "README.md":
        fail(f"missing review date: {path.relative_to(ROOT)}")
    for label, pattern in FORBIDDEN.items():
        if pattern.search(text):
            fail(f"forbidden {label} pattern: {path.relative_to(ROOT)}")
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        if "://" in target or target.startswith("#"):
            continue
        resolved = (path.parent / target.split("#", 1)[0]).resolve()
        if not resolved.is_file() or ROOT not in resolved.parents:
            fail(f"broken or escaping link in {path.relative_to(ROOT)}: {target}")

matrix = (ROOT / "evidence/nist-csf-2-current-profile.md").read_text(encoding="utf-8")
category_rows = re.findall(r"^\| (?:GV|ID|PR|DE|RS|RC)\.[A-Z]{2} ", matrix, flags=re.MULTILINE)
if len(category_rows) != 23:
    fail(f"expected 23 NIST CSF 2.0 category rows, found {len(category_rows)}")

print(f"validated {len(TEXT_FILES)} public evidence documents and {len(category_rows)} CSF categories")
