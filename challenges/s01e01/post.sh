#!/bin/sh
# usage: post.sh <body.json> — POSTs the body and appends body + reply to log.md exactly
URL=https://hq.mega.dev/challenges/where-the-story-begins/api
LOG="$(dirname "$0")/log.md"
{
  printf '\n## POST %s — %s\n\n### Body sent (%s)\n\n```json\n' "$URL" "$(date -u +%FT%TZ)" "$1"
  cat "$1"; printf '\n```\n\n### Reply\n\n```\n'
  curl -sS -i -X POST -H 'Content-Type: application/json' --data-binary @"$1" "$URL"
  printf '\n```\n'
} >> "$LOG"
tail -n 60 "$LOG"
