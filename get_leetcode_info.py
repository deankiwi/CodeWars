#!/usr/bin/env python3
"""
Create a starter file for a LeetCode problem in Python or Go and open it in VS Code.

Usage:
  # optional: auto-cookie method (recommended)
  pip install requests browser-cookie3

  # OR env cookies method:
  export LEETCODE_SESSION="..."
  export LEETCODE_CSRF="..."

  # Python (default)
  python make_leetcode.py "https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/"

  # Go
  python make_leetcode.py --lang go "https://leetcode.com/problems/two-sum/description/"
"""
import argparse
import os
import re
import subprocess
import sys
from datetime import datetime
from html import unescape
from pathlib import Path
from typing import Optional

import requests

GRAPHQL_URL = "https://leetcode.com/graphql"

# -------- URL / cookies / API --------

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
    try:
        import browser_cookie3  # type: ignore
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

# -------- Language handling --------

LANG_CHOICES = ("python", "go")

EXT_BY_LANG = {
    "python": "py",
    "go": "go",
}

COMMENT_PREFIX = {
    "python": "# ",
    "go": "// ",
}

# LeetCode uses langSlug "python3"/"python" for Python and "golang" for Go
LANGSLUG_PREFERENCE = {
    "python": ("python3", "python"),
    "go": ("golang", "go"),
}

LANGNAME_FALLBACKS = {
    "python": ("python3", "python"),
    "go": ("go",),
}

def normalize_lang(s: str) -> str:
    s = s.strip().lower()
    if s in ("py", "python3"):
        return "python"
    if s in ("go", "golang"):
        return "go"
    if s in LANG_CHOICES:
        return s
    raise SystemExit(f"Unsupported --lang '{s}'. Choose from: {', '.join(LANG_CHOICES)}")

def pick_snippet(code_snippets, lang: str) -> str:
    """
    Pick a code snippet for the requested language, or provide a minimal fallback.
    """
    if code_snippets:
        # Try by langSlug first
        for target in LANGSLUG_PREFERENCE[lang]:
            for snip in code_snippets:
                if (snip.get("langSlug") or "").lower() == target:
                    return snip.get("code") or ""
        # Then by human-readable lang
        for target in LANGNAME_FALLBACKS[lang]:
            for snip in code_snippets:
                if (snip.get("lang") or "").lower() == target:
                    return snip.get("code") or ""

    # Fallbacks
    if lang == "python":
        return (
            "from typing import *\n\n"
            "class Solution:\n"
            "    def TODO_replace_with_function(self, *args, **kwargs):\n"
            "        pass\n\n"
            "if __name__ == \"__main__\":\n"
            "    # TODO: instantiate Solution() and call method with sample inputs\n"
            "    pass\n"
        )
    else:  # go
        return (
            "package main\n\n"
            "import \"fmt\"\n\n"
            "// TODO: implement solution function(s)\n"
            "func TODOReplaceWithFunction() {\n"
            "    // ...\n"
            "}\n\n"
            "func main() {\n"
            "    // TODO: call your function(s) with sample inputs\n"
            "    fmt.Println(\"stub\")\n"
            "}\n"
        )

# -------- File helpers --------

def sanitize_title(title: str) -> str:
    s = title.strip().lower()
    s = re.sub(r"['’]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-{2,}", "-", s).strip("-")
    return s or "problem"

def build_header_comment(q: dict, url: str, lang: str) -> str:
    prefix = COMMENT_PREFIX[lang]
    date_str = datetime.now().strftime("%Y-%m-%d")
    header_lines = [
        f"{prefix}{q['title']} — LeetCode #{q['questionId']} ({q['difficulty']})",
        f"{prefix}URL: {url}",
        f"{prefix}Slug: {q['titleSlug']}",
        f"{prefix}Difficulty: {q['difficulty']}",
        f"{prefix}Paid only: {bool(q.get('isPaidOnly'))}",
        f"{prefix}Fetched: {date_str}",
        "",
    ]
    return "\n".join(header_lines) + "\n"

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def write_file(path: Path, header: str, code: str, sample: Optional[str], lang: str):
    sample_section = ""
    if sample and sample.strip():
        prefix = COMMENT_PREFIX[lang]
        sample_section = f"\n{prefix}Sample Test Case (from LeetCode)\n{prefix}{unescape(sample.strip())}\n"
    content = header + code.rstrip() + sample_section + "\n"
    path.write_text(content, encoding="utf-8")

def open_in_vscode(path: Path):
    try:
        subprocess.run(["code", "-r", str(path)], check=False)
    except FileNotFoundError:
        print(
            "VS Code CLI 'code' not found on PATH. Open manually, or enable it via:\n"
            "VS Code → Command Palette → 'Shell Command: Install 'code' command in PATH'\n"
        )

# -------- CLI --------

def main():
    ap = argparse.ArgumentParser(
        description="Create ./leetcode/{id}-{title}.{py|go} starter file for a LeetCode problem and open it in VS Code."
    )
    ap.add_argument("url", help="LeetCode problem URL")
    ap.add_argument("--lang", default="python", help="Target language: python | go (default: python)")
    ap.add_argument("--force", "-f", action="store_true", help="Overwrite file if it exists")
    ap.add_argument("--dir", default="leetcode", help="Target directory (default: ./leetcode)")
    args = ap.parse_args()

    lang = normalize_lang(args.lang)

    slug = slug_from_url(args.url)
    cookies = get_cookies()
    q = fetch_problem(slug, cookies)

    title = q["title"]
    qid = q["questionId"]
    safe_title = sanitize_title(title)
    ext = EXT_BY_LANG[lang]

    target_dir = Path(args.dir)
    ensure_dir(target_dir)
    out_path = target_dir / f"{qid}-{safe_title}.{ext}"

    if out_path.exists() and not args.force:
        print(f"File already exists: {out_path}\nUse --force to overwrite.")
        open_in_vscode(out_path)
        return

    code = pick_snippet(q.get("codeSnippets") or [], lang)
    header = build_header_comment(q, f"https://leetcode.com/problems/{slug}/", lang)
    write_file(out_path, header, code, q.get("sampleTestCase"), lang)

    print(f"Created → {out_path}")
    open_in_vscode(out_path)

if __name__ == "__main__":
    main()