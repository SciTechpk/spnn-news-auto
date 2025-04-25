@echo off
cd /d %~dp0

echo Renaming merged files to replace original news-only HTML files...

if exist news_psl_live.html del news_psl_live.html
rename sports_psl.html news_psl_live.html

if exist news_top5_sports.html del news_top5_sports.html
rename sports_top5.html news_top5_sports.html

if exist news_sports_weekly.html del news_sports_weekly.html
rename sports_weekly.html news_sports_weekly.html

echo ✅ Files renamed successfully. Ready for GitHub push.
pause
