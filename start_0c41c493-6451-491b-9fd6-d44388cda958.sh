#!/bin/sh
set -eu

PYTHON_BIN="${PYTHON_BIN:-/usr/local/bin/python}"

"$PYTHON_BIN" -m uvicorn app.main:app --host 127.0.0.1 --port 8000 &
pid=$!
trap 'kill "$pid" 2>/dev/null || true; wait "$pid" 2>/dev/null || true' EXIT

attempt=0
until curl -fsS http://127.0.0.1:8000/generate-letter; do
    attempt=$((attempt + 1))
    if [ "$attempt" -ge 24 ]; then
        echo "Uvicorn did not serve /generate-letter within 120 seconds." >&2
        exit 1
    fi
    sleep 5
done
