@echo off
title Codex Queue (Curio Class)
echo Codex Queue: runs the build and review prompts from _queue.txt, each in its own fresh Codex session.
echo To stop gently: create S:\CurioClass-codex\_runner\STOP (running sessions finish). Closing this window stops all.
echo Log: S:\CurioClass-codex\_runner\summary.txt
echo.
rem Codex was installed from inside the Claude app, so it lives in that app's private AppData copy,
rem which a scheduled task cannot see under APPDATA. Add both places (2026-11-04).
for /d %%D in ("%LOCALAPPDATA%\Packages\Claude_*") do set "PATH=%%D\LocalCache\Roaming\npm;%PATH%"
set "PATH=%APPDATA%\npm;%PATH%"
cd /d S:\CurioClass
python scripts\codex_runner.py %*
echo.
echo Runner finished. See S:\CurioClass-codex\_runner\summary.txt
pause
