from datetime import datetime, timezone
from bs4 import BeautifulSoup
import feedparser

def clean_html(raw_html):
    soup = BeautifulSoup(raw_html, "html.parser")
    return soup.get_text()

def fetch_feed_items(feed_url, max_items=5):
    feed = feedparser.parse(feed_url)
    items = []
    for entry in feed.entries[:max_items]:
        title = clean_html(entry.title)
        link = entry.link
        published = entry.get("published", "No date")
        items.append(f"<li><a href='{link}' target='_blank'>{title}</a> <small>({published})</small></li>")
    return items

timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

feeds = {
    "news_psl_only.html": [
        "https://www.espncricinfo.com/rss/content/story/feeds/0.xml",
        "https://www.thenews.com.pk/rss/1/1",
    ],
    "news_top5_sports_text.html": [
        "https://www.skysports.com/rss/12040",
        "https://www.espn.com/espn/rss/news",
    ],
    "news_weekly_sports_text.html": [
        "https://www.espncricinfo.com/rss/content/story/feeds/0.xml",
        "https://www.skysports.com/rss/12040",
        "https://www.tennis.com/feed/rss/",
    ]
}

for filename, urls in feeds.items():
    all_items = []
    for url in urls:
        try:
            all_items.extend(fetch_feed_items(url, max_items=3))
        except Exception as e:
            print(f"Error fetching {url}: {e}")

    html = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>SPNN Targeted News</title></head>
<body>
<h2>📰 Targeted News</h2>
<p><em>Last updated: {timestamp}</em></p>
<ul>
{''.join(all_items)}
</ul>
</body>
</html>
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

print("✅ Topic-specific news files created.")
