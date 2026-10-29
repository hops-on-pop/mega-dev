#!/bin/bash
# usage: post.sh <endpoint> <body.json>  -- logs masked body and reply to log.md
set -e
cd "$(dirname "$0")/.."
T=$(tr -d '\n' < scripts/ticket.txt)
resp=$(curl -sS -X POST -H 'Content-Type: application/json' --data-binary @"$2" -w '\nHTTP %{http_code}' "$1")
{ echo "## $(date -u +%FT%TZ) POST $1"; echo '```json'; sed "s/$T/v1.***masked***/g" "$2"; echo; echo '```'; echo 'Reply:'; echo '```'; echo "$resp" | sed "s/$T/v1.***masked***/g"; echo '```'; echo; } >> log.md
echo "$resp"
