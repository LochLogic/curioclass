@echo off
title Codex Scopes (Curio Class)
echo Codex Scopes: writes, reconciles and first-reads every science, ELA and math scope and sequence (37 courses),
echo each job in its own fresh Codex session, 3 at once. Run it again any time: it picks up where it stopped.
echo To stop gently: create S:\CurioClass\_scopes\STOP (running jobs finish). Closing this window stops all.
echo Log: S:\CurioClass\_scopes\summary.txt
echo.
for /d %%D in ("%LOCALAPPDATA%\Packages\Claude_*") do set "PATH=%%D\LocalCache\Roaming\npm;%PATH%"
set "PATH=%APPDATA%\npm;%PATH%"
cd /d S:\CurioClass
python -X utf8 scripts\codex_scopes.py %*
echo.
echo Run finished. See S:\CurioClass\_scopes\summary.txt
pause
