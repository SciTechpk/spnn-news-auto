from datetime import datetime

pages = [
    ("news_psl_live.html", "news_psl_live.html", "news_psl_only.html"),
    ("news_top5_sports.html", "news_top5_sports.html", "news_top5_sports_text.html"),
    ("news_sports_weekly.html", "news_sports_weekly.html", "news_weekly_sports_text.html"),
]

for output_file, video_file, news_file in pages:
    try:
        with open(video_file, "r", encoding="utf-8") as vf:
            video_content = vf.read()
    except FileNotFoundError:
        video_content = "<!-- Video not available -->"

    try:
        with open(news_file, "r", encoding="utf-8") as nf:
            news_content = nf.read()
    except FileNotFoundError:
        news_content = "<!-- News not available -->"

    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    html = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>SPNN Page</title></head>
<body>
<h2>📺 Video Highlights</h2>
<p><em>Last updated: {timestamp}</em></p>
{video_content}
<hr>
<h2>📰 Related News</h2>
{news_content}
</body>
</html>
"""
    with open(output_file, "w", encoding="utf-8") as out:
        out.write(html)

print("✅ All pages merged with topic-specific news.")
