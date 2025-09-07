#!/usr/bin/env python3
"""
Create a Python starter file for a LeetCode problem and open it in VS Code.

Usage:
  # optional: auto-cookie method (recommended)
  pip install requests browser-cookie3

  # OR env cookies method:
  export LEETCODE_SESSION="..."
  export LEETCODE_CSRF="..."

  python make_leetcode_py.py "https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/?envType=daily-question&envId=2025-09-07"
"""
import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from html import unescape
from pathlib import Path

import requests

GRAPHQL_URL = "https://leetcode.com/graphql"


def slug_from_url(url: str) -> str:
    u = url.split("?")[0]
    if not u.endswith("/"):
        u += "/"
    m = re.search(r"/problems/([^/]+)/", u)
    if not m:
        raise ValueError("Could not parse titleSlug from URL; expected /problems/<slug>/")
    return m.group(1)


def get_cookies():
    """
    Prefer pulling fresh cookies from your logged-in browser (browser-cookie3).
    Fallback to env vars LEETCODE_SESSION + LEETCODE_CSRF.
    Returns dict of cookies (at least LEETCODE_SESSION, csrftoken).
    """
    # Try browser-cookie3 (Chrome/Edge/Brave/Firefox etc.)
    try:
        import browser_cookie3  # type: ignore

        # Try Chrome-like first; cj is a CookieJar
        for getter in (
            lambda: browser_cookie3.chrome(domain_name="leetcode.com"),
            lambda: browser_cookie3.edge(domain_name="leetcode.com"),
            lambda: browser_cookie3.brave(domain_name="leetcode.com"),
            lambda: browser_cookie3.firefox(domain_name="leetcode.com"),
        ):
            try:
                cj = getter()
                jar = {c.name: c.value for c in cj}
                if "LEETCODE_SESSION" in jar and "csrftoken" in jar:
                    return {"LEETCODE_SESSION": jar["LEETCODE_SESSION"], "csrftoken": jar["csrftoken"]}
            except Exception:
                pass
    except Exception:
        pass

    # Fallback to env vars
    sess = os.getenv("LEETCODE_SESSION")
    csrf = os.getenv("LEETCODE_CSRF") or os.getenv("csrftoken")
    if not (sess and csrf):
        sys.exit(
            "Couldn't auto-read cookies.\n"
            "Either install browser-cookie3 (pip install browser-cookie3) while logged into LeetCode\n"
            "OR export env vars LEETCODE_SESSION and LEETCODE_CSRF (csrftoken)."
        )
    return {"LEETCODE_SESSION": sess, "csrftoken": csrf}


def fetch_problem(slug: str, cookies: dict) -> dict:
    query = """
    query getQuestionDetail($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId
        title
        titleSlug
        difficulty
        isPaidOnly
        likes
        dislikes
        content
        sampleTestCase
        codeSnippets { lang langSlug code }
      }
    }
    """
    payload = {
        "operationName": "getQuestionDetail",
        "variables": {"titleSlug": slug},
        "query": query,
    }
    headers = {
        "Content-Type": "application/json",
        "x-csrftoken": cookies["csrftoken"],
        "Referer": f"https://leetcode.com/problems/{slug}/",
        "Origin": "https://leetcode.com",
        "User-Agent": "leetcode-starter-script",
    }
    r = requests.post(GRAPHQL_URL, headers=headers, cookies=cookies, json=payload, timeout=25)
    r.raise_for_status()
    data = r.json()
    if data.get("errors"):
        raise RuntimeError(f"GraphQL error: {data['errors']}")
    q = data.get("data", {}).get("question")
    if not q:
        raise RuntimeError("No question returned (cookies expired or insufficient permissions?).")
    return q


def pick_python_snippet(code_snippets):
    """
    Choose Python3 starter code if available; else a minimal fallback.
    """
    if code_snippets:
        # Prefer Python3, then Python
        for target in ("python3", "python"):
            for snip in code_snippets:
                if (snip.get("langSlug") or "").lower() == target:
                    return snip.get("code") or ""
            for snip in code_snippets:
                if (snip.get("lang") or "").lower() == "python3":
                    return snip.get("code") or ""
                if (snip.get("lang") or "").lower().startswith("python"):
                    return snip.get("code") or ""
    # Fallback template
    return (
        "from typing import *\n\n"
        "class Solution:\n"
        "    def TODO_replace_with_function(self, *args, **kwargs):\n"
        "        pass\n\n"
        "if __name__ == \"__main__\":\n"
        "    # TODO: instantiate Solution() and call method with sample inputs\n"
        "    pass\n"
    )


def sanitize_title(title: str) -> str:
    s = title.strip().lower()
    s = re.sub(r"['’]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "problem"


def build_header_comment(q: dict, url: str) -> str:
    date_str = datetime.now().strftime("%Y-%m-%d")
    header = f"""# {q['title']} — LeetCode #{q['questionId']} ({q['difficulty']})
# URL: {url}
# Slug: {q['titleSlug']}
# Difficulty: {q['difficulty']}
# Paid only: {bool(q.get('isPaidOnly'))}
# Fetched: {date_str}

"""
    return header


def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)


def write_file(path: Path, header: str, code: str, sample: str | None):
    # If snippet doesn't include a main block, add a tiny harness stub
    needs_stub = "if __name__" not in code
    sample_section = ""
    if sample and sample.strip():
        sample_section = (
            f"\n# Sample Test Case (from LeetCode)\n# {unescape(sample.strip())}\n"
        )

    content = header + code.rstrip() + sample_section + "\n"
    path.write_text(content, encoding="utf-8")


def open_in_vscode(path: Path):
    try:
        subprocess.run(["code", "-r", str(path)], check=False)
    except FileNotFoundError:
        print(
            "VS Code CLI 'code' not found on PATH. Open manually, or enable it via:\n"
            "VS Code → Command Palette → 'Shell Command: Install 'code' command in PATH'"
        )


def main():
    ap = argparse.ArgumentParser(description="Create ./leetcode/{id}-{title}.py starter file for a LeetCode problem and open it in VS Code.")
    ap.add_argument("url", help="LeetCode problem URL")
    ap.add_argument("--force", "-f", action="store_true", help="Overwrite file if it exists")
    ap.add_argument("--dir", default="leetcode", help="Target directory (default: ./leetcode)")
    args = ap.parse_args()

    slug = slug_from_url(args.url)
    cookies = get_cookies()
    q = fetch_problem(slug, cookies)

    title = q["title"]
    qid = q["questionId"]
    safe_title = sanitize_title(title)
    target_dir = Path(args.dir)
    ensure_dir(target_dir)
    out_path = target_dir / f"{qid}-{safe_title}.py"

    if out_path.exists() and not args.force:
        print(f"File already exists: {out_path}\nUse --force to overwrite.")
        open_in_vscode(out_path)
        return

    code = pick_python_snippet(q.get("codeSnippets") or [])
    header = build_header_comment(q, f"https://leetcode.com/problems/{slug}/")
    write_file(out_path, header, code, q.get("sampleTestCase"))

    print(f"Created → {out_path}")
    open_in_vscode(out_path)


if __name__ == "__main__":
    main()