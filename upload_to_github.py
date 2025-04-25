# ✅ upload_to_github.py — Push all HTML files to GitHub Pages

import os
import subprocess
from datetime import datetime, timezone

# ✅ Ensure script always runs from its own folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

html_files = [
    "news_latest.html",
    "news_24hr.html",
    "news_7day.html",
    "news_psl_live.html",
    "news_psl_only.html",
    "news_top5_sports.html",
    "news_top5_sports_text.html",
    "news_sports_weekly.html",
    "news_weekly_sports_text.html",
    "cnn_ticker.html",
    "market_ticker.html"
]

# ✅ UTC timestamp (future-proof)
timestamp = datetime.now(timezone.utc).strftime("📡 Auto-update: %Y-%m-%d %H:%M UTC")

for file in html_files:
    with open(file, "r+", encoding="utf-8") as f:
        content = f.read()
        f.seek(0)
        f.write(f"<!-- {timestamp} -->\n{content}")
        f.truncate()

# ✅ Add and commit
subprocess.run(["git", "add"] + html_files)
subprocess.run(["git", "commit", "-m", timestamp])
subprocess.run(["git", "push"])
