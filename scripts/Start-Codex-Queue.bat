@echo off
title Codex Queue (Curio Class)
echo Codex Queue: runs the build and review prompts from _queue.txt, each in its own fresh Codex session.
echo To stop gently: create S:\CurioClass-codex\_runner\STOP (running sessions finish). Closing this window stops all.
echo Log: S:\CurioClass-codex\_runner\summary.txt
echo.
cd /d S:\CurioClass
python scripts\codex_runner.py %*
echo.
echo Runner finished. See S:\CurioClass-codex\_runner\summary.txt
pause
