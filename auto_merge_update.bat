@echo off
:: ✅ Set working directory explicitly (prevent fallback to System32)
cd /d D:\SPNN-Backup\spnn-news-auto

echo 🔄 Generating tickers...
C:\Windows\py.exe generate_cnn_ticker.py
C:\Windows\py.exe generate_market_ticker.py

echo ▶️ Running YouTube video generator...
C:\Windows\py.exe generate_youtube_iframes.py

echo ▶️ Running topic-specific news generator...
C:\Windows\py.exe generate_latest_html.py

echo 🧩 Merging targeted video and news into HTML pages...
C:\Windows\py.exe merge_content.py

echo 🟢 Adding updated HTML files to Git...
git add -f cnn_ticker.html market_ticker.html
git add -f *.html

echo 💾 Committing and pushing to GitHub...
git commit -m "🔁 Auto-update: tickers + news + videos"
git push origin main

echo ✅ All done: tickers, videos, and news deployed!
pause
