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
PUBLIC_CLAIM_FILES = {
    "evidence/internal-review-2026-08-18.md",
    "evidence/nist-csf-2-current-profile.md",
    "evidence/risk-register.md",
    "evidence/secure-development.md",
}
RESTRICTED_IMPLEMENTATION_PATTERNS = {
    "uuid": re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b", re.I),
    "internal_function": re.compile(r"\b(?:get|create|finalize|recover|enqueue|claim|confirm)_vexa_[a-z0-9_]+\b", re.I),
    "internal_role": re.compile(r"\b(?:service_role|security\s+definer|auth\.jwt|row[- ]level security|RLS)\b", re.I),
    "private_storage_uri": re.compile(r"\b(?:r2|s3)://", re.I),
    "private_worker_endpoint": re.compile(r"https?://[^\s)]+\.workers\.dev\b", re.I),
    "secret_identifier": re.compile(r"\b[A-Z][A-Z0-9]*(?:_API)?_(?:KEY|TOKEN|SECRET|PASSWORD)\b"),
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
    relative = str(path.relative_to(ROOT))
    if relative in PUBLIC_CLAIM_FILES:
        for label, pattern in RESTRICTED_IMPLEMENTATION_PATTERNS.items():
            if pattern.search(text):
                fail(f"restricted implementation detail ({label}): {relative}")
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
