import feedparser

# CNN RSS feed
feed_url = "http://rss.cnn.com/rss/edition.rss"
feed = feedparser.parse(feed_url)

# Extract top 5 headlines
items = feed.entries[:5]
ticker_items = [f"{entry.title}" for entry in items]

# HTML output (marquee style)
html_content = f'''
<div style="background-color:#cc0000;color:white;padding:10px;font-weight:bold;font-size:18px;">
    <marquee behavior="scroll" direction="left" scrollamount="5">
        {"  ⚡  ".join(ticker_items)}
    </marquee>
</div>
'''

# Save to file
with open("cnn_ticker.html", "w", encoding="utf-8") as f:
    f.write(html_content)
