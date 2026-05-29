#!/usr/bin/env python3
from __future__ import annotations

import os
from pathlib import Path
import re
import sys
import time
from urllib import error, parse, request

ROOT = Path(__file__).resolve().parent.parent
URL_RE = re.compile(r"\[[^\]]+\]\((https?://[^)\s]+)\)")

TARGET_GLOBS = [
    "README.md",
    "docs/*.md",
    "governance/*.md",
    "projects/*.md",
]

PROBE_HTTP = os.environ.get("EXTERNAL_LINK_HTTP_PROBE", "0") == "1"
REQUEST_TIMEOUT_SECONDS = 8
MAX_RETRIES = 3
RETRY_DELAY_BASE_SECONDS = 0.3


def find_targets() -> list[Path]:
    files: set[Path] = set()
    for pattern in TARGET_GLOBS:
        files.update(ROOT.glob(pattern))
    return sorted(files)


def probe_url(url: str) -> tuple[bool, str | None]:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            req = request.Request(url, method="HEAD")
            with request.urlopen(req, timeout=REQUEST_TIMEOUT_SECONDS) as response:
                status = getattr(response, "status", 200)
                if 200 <= status < 400:
                    return True, None
                return False, f"unexpected status {status}"
        except error.HTTPError as exc:
            if exc.code in {405, 501}:
                try:
                    req = request.Request(url, method="GET")
                    with request.urlopen(req, timeout=REQUEST_TIMEOUT_SECONDS) as response:
                        status = getattr(response, "status", 200)
                        if 200 <= status < 400:
                            return True, None
                        return False, f"unexpected status {status}"
                except (error.URLError, TimeoutError, OSError) as get_exc:
                    if attempt == MAX_RETRIES:
                        return False, f"{type(get_exc).__name__}: {get_exc}"
            elif attempt == MAX_RETRIES:
                return False, f"HTTPError {exc.code}"
        except (error.URLError, TimeoutError, OSError) as exc:
            if attempt == MAX_RETRIES:
                return False, f"{type(exc).__name__}: {exc}"
        time.sleep(RETRY_DELAY_BASE_SECONDS * attempt)
    return False, "exhausted retries"


errors: list[str] = []
checked_links = 0

for path in find_targets():
    text = path.read_text(encoding="utf-8")
    for url in URL_RE.findall(text):
        checked_links += 1
        parsed = parse.urlparse(url)

        if parsed.scheme != "https":
            errors.append(f"{path.relative_to(ROOT)}: non-https URL not allowed: {url}")
            continue

        if not parsed.netloc:
            errors.append(f"{path.relative_to(ROOT)}: malformed URL: {url}")
            continue

        query_keys = {k.lower() for k, _ in parse.parse_qsl(parsed.query)}
        if any(key.startswith("utm_") for key in query_keys):
            errors.append(f"{path.relative_to(ROOT)}: tracking query parameters are not allowed: {url}")

        if PROBE_HTTP:
            ok, detail = probe_url(url)
            if not ok:
                errors.append(
                    f"{path.relative_to(ROOT)}: URL failed policy probe "
                    f"(timeout={REQUEST_TIMEOUT_SECONDS}s retries={MAX_RETRIES}): {url} ({detail})"
                )

if errors:
    print("external link policy check failed:")
    for error_msg in errors:
        print(f"- {error_msg}")
    sys.exit(1)

probe_state = "enabled" if PROBE_HTTP else "disabled"
print(
    "external link policy check passed "
    f"({checked_links} links checked, timeout={REQUEST_TIMEOUT_SECONDS}s, retries={MAX_RETRIES}, probe={probe_state})"
)
