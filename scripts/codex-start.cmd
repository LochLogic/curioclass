@echo off
rem Start a Codex build-only run for one tool: makes its worktree from the latest main if needed, then opens Codex there.
rem   S:\CurioClass-media\scripts\codex-start.cmd ^<tool-id^>     prompts: docs\agents\codex-prompts-40.txt
if "%~1"=="" (echo Usage: codex-start ^<tool-id^> ^& exit /b 1)
set "id=%~1"
set "wt=S:\CurioClass-codex-%id%"
set "scr=S:\CurioClass-codex-scratch\%id%"
if not exist "%wt%" (
  git -C S:\CurioClass-media fetch -q origin
  git -C S:\CurioClass-media worktree add -q "%wt%" -b "codex/%id%" origin/main || exit /b 1
)
if not exist "%scr%" mkdir "%scr%"
call codex -C "%wt%" -s workspace-write -a never --add-dir "%scr%"
