from datetime import datetime, timezone

timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

pages = [
    ("news_psl_only.html", "psl_live.html"),
    ("news_top5_sports_text.html", "top5_moments.html"),
    ("news_weekly_sports_text.html", "weekly_recap.html"),
]

for news_file, video_file in pages:
    try:
        with open(news_file, "r", encoding="utf-8") as nf, open(video_file, "r", encoding="utf-8") as vf:
            news_content = nf.read()
            video_content = vf.read()

        final_html = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>SPNN Full Content</title></head>
<body>
<h1>📢 SPNN News + Video</h1>
<p><em>Last merged: {timestamp}</em></p>
<hr>
{video_content}
<hr>
{news_content}
</body>
</html>
"""
        output_name = f"merged_{news_file.replace('news_', '').replace('_text.html', '').replace('_only.html', '')}.html"
        with open(output_name, "w", encoding="utf-8") as out:
            out.write(final_html)

        print(f"✅ Merged {news_file} + {video_file} → {output_name}")
    except Exception as e:
        print(f"❌ Error merging {news_file} and {video_file}: {e}")
