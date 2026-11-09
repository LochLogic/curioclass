@echo off
rem Sara's Curio Class spec session: her own Claude login (separate config folder), her own worktree.
rem First run asks her to sign in with her Claude account. Never sign in with Cory's here.
title Curio Class specs (Sara)
set "CLAUDE_CONFIG_DIR=%USERPROFILE%\.claude-sara"
set "CLAUDE_EXE="
where claude >nul 2>nul && set "CLAUDE_EXE=claude"
if not defined CLAUDE_EXE for /f "delims=" %%i in ('powershell -NoProfile -Command "(Get-ChildItem \"$env:LOCALAPPDATA\Claude-Data\" -Recurse -Depth 4 -Filter claude.exe -ErrorAction SilentlyContinue ^| Sort-Object LastWriteTime -Descending ^| Select-Object -First 1).FullName"') do set "CLAUDE_EXE=%%i"
if not defined CLAUDE_EXE (
  echo Could not find Claude Code. Ask Cory.
  pause
  exit /b 1
)
cd /d S:\CurioClass-spec2
"%CLAUDE_EXE%" "Read docs/agents/GUEST-SPEC.md and follow it: sync, then start the next batch of five."
pause
