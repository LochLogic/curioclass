@echo off
rem Codex draft run (scripts/codex_draft.py): four subject lanes, runs in S:\CurioClass-draft. Stop gently: create _draft\STOP.
cd /d S:\CurioClass-draft
title Curio Class Codex draft run
"C:\Users\Cory\AppData\Local\Programs\Python\Python313\python.exe" -X utf8 scripts\codex_draft.py run
echo.
echo The draft run ended. See S:\CurioClass-draft\_draft\run.log
pause
