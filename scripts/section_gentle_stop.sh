#!/bin/bash
# Gentle stop for one section lane (Cory 2026-11-27), documented in docs/pipeline/SECTION-RUN.md.
# Usage: bash scripts/section_gentle_stop.sh <math|ela>
# Waits for the lane's next "done ..." or "unit ... green/codex-done" log line (a stage just committed), then writes
# STOP at once: the next stage meets the STOP check after its baseline gate run and before any model call.
# A Codex limit line also stops it. Then it waits for the lane to exit; the lead restarts it.
set -u
S=$1
R=/s/CurioClass
D=$R/build/sections/$S
LOG=$D/run.log
start=$(wc -l < "$LOG")
echo "$(date '+%F %T') watching $S from line $start"
while true; do
  n=$(wc -l < "$LOG")
  if [ "$n" -gt "$start" ]; then
    hit=$(tail -n +"$((start + 1))" "$LOG" | grep -E " done [^ ]+ |^[0-9: -]+ unit .* (green|codex-done)|Codex retry at" | grep -vE " (prep|texts)(,|$)" | head -1)
    # prep and texts can end in the background beside a Claude pass, so they are never taken as a boundary
    if [ -n "$hit" ]; then
      touch "$D/STOP"
      echo "$(date '+%F %T') boundary seen: $hit"
      echo "$(date '+%F %T') STOP written"
      break
    fi
    if [ -f "$D/STOPPED" ]; then echo "lane stopped on its own:"; cat "$D/STOPPED"; exit 0; fi
  fi
  sleep 2
done
while [ -f "$D/RUNNING" ]; do sleep 5; done
echo "$(date '+%F %T') lane exited"
tail -3 "$LOG"
