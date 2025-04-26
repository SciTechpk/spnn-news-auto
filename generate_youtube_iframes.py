from datetime import datetime, timezone
from googleapiclient.discovery import build

# ✅ Your API key
api_key = "AIzaSyADRyWjUl0xfBVCkW8r-3YoM_72e5Qso2c"

# ✅ Playlists
playlists = {
    "news_psl_live.html": "PLr6o7VvlqFOUo3uuf6sMLA3SwpVXsfF0g",  # PSL Live Highlight
    "news_top5_sports.html": "PLrr-WIVYH-XhKGfRbjeddC8S9QwkVazMH",  # Top 5 Moments
    "news_sports_weekly.html": {
        "Cricket": "PLH06VbPakyYUnpMhUFZLp6pbGfYTDf3-S",
        "Football": "PLzn2Kbs0lFDsKiN04bQ2AsobsvV2U7S36",
        "Tennis": "PLQHHr8gPOsH6KEvZs8n8-l4UXJuLz9GJn"
    }
}

youtube = build("youtube", "v3", developerKey=api_key)

def fetch_latest_video(playlist_id):
    request = youtube.playlistItems().list(
        part="snippet",
        maxResults=1,
        playlistId=playlist_id
    )
    response = request.execute()
    items = response.get("items", [])
    if items:
        video_id = items[0]["snippet"]["resourceId"]["videoId"]
        return video_id
    return None

timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

# Process simple playlists
for filename, playlist_id in playlists.items():
    if isinstance(playlist_id, str):
        video_id = fetch_latest_video(playlist_id)
        if video_id:
            html = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>SPNN Video</title></head>
<body>
<h2>▶️ Latest Video</h2>
<p><em>Last updated: {timestamp}</em></p>
<iframe width="100%" height="400" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>
</body>
</html>
"""
            with open(filename, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"✅ Created {filename}")
    elif isinstance(playlist_id, dict):
        # Weekly Sports Special case
        merged_html = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>SPNN Weekly Sports Recap</title></head>
<body>
<h2>🏆 Weekly Sports Recap</h2>
<p><em>Last updated: {timestamp}</em></p>
"""
        for sport_name, sport_playlist_id in playlist_id.items():
            video_id = fetch_latest_video(sport_playlist_id)
            if video_id:
                merged_html += f"""
<h3>{sport_name}</h3>
<iframe width="100%" height="400" src="https://www.youtube.com/embed/{video_id}" frameborder="0" allowfullscreen></iframe>
<br><br>
"""
        merged_html += """
</body>
</html>
"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(merged_html)
        print(f"✅ Created {filename}")

print("🎯 All YouTube video iframe pages generated.")
