# 07_eval_blog_checker.py
import re, json, os, sys, pathlib
from collections import Counter
from pathlib import Path

# Directory where this script lives: .../DataCamp/claude_agent_SDK
ROOT = Path(__file__).resolve().parent
# Project root: .../DataCamp
PROJECT_ROOT = ROOT.parent
# Default report path: .../DataCamp/reports/datacamp_blog_latest.md
REPORT = PROJECT_ROOT / "reports" / "datacamp_blog_latest.md"
# LOG
LOG   = ROOT / "claude" / "logs" / "sdk-stream.jsonl"

def check_report():
    ok_path = REPORT.exists()
    text = REPORT.read_text(encoding="utf-8") if ok_path else ""

    # Match headings like: "### 1. Title here"
    items = re.findall(r"^###\s+\d+\.\s+(.+)$", text, flags=re.M)

    ok_count = len(items) >= 5
    return ok_path, ok_count, items[:5]


def count_tools():
    c = Counter()
    if LOG.exists():
        for line in LOG.read_text(encoding="utf-8").splitlines():
            try:
                rec = json.loads(line)
                if rec.get("kind") == "tool_use_request":
                    c[ rec.get("name","<unknown>") ] += 1
            except: pass
    return c

if __name__ == "__main__":
    ok_path, ok_count, sample = check_report()
    print("REPORT PATH: ", REPORT)
    tools = count_tools()
    print("Report file exists:", ok_path)
    print("Has >=5 items:", ok_count)
    print("Sample items:", sample)
    print("Tool usage:", tools)
