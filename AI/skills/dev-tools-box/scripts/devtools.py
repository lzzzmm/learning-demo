#!/usr/bin/env python3
"""Developer Toolbox - deterministic CLI tools, result-only output."""

import sys
import json
import base64
import urllib.parse
import hashlib
from datetime import datetime, timezone


def cmd_time(args):
    """Convert between unix timestamp and human-readable time."""
    if not args:
        print("Error: missing input", file=sys.stderr)
        sys.exit(1)
    inp = " ".join(args)

    try:
        ts = int(inp)
        # Timestamp -> various formats
        dt_utc = datetime.fromtimestamp(ts, tz=timezone.utc)
        dt_local = datetime.fromtimestamp(ts)
        iso = dt_utc.strftime("%Y-%m-%dT%H:%M:%SZ")
        print(f"UTC:     {dt_utc.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Local:   {dt_local.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"ISO8601: {iso}")
    except ValueError:
        try:
            # Date string -> timestamp + ISO
            dt = datetime.strptime(inp, "%Y-%m-%d %H:%M:%S")
            ts = int(dt.timestamp())
            iso = dt.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            dt_utc = dt.replace(tzinfo=timezone.utc)
            print(f"UTC:     {dt_utc.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Timestamp: {ts}")
            print(f"ISO8601: {iso}")
        except ValueError:
            print(f"Error: cannot parse '{inp}' as timestamp or date", file=sys.stderr)
            sys.exit(1)


def cmd_base64(args):
    """Auto-detect and decode/encode base64."""
    if not args:
        print("Error: missing input", file=sys.stderr)
        sys.exit(1)
    inp = " ".join(args)

    try:
        decoded = base64.b64decode(inp, validate=True)
        # Try decoding as text first
        try:
            text = decoded.decode("utf-8")
            print(f"Decoded (UTF-8):\n{text}")
        except UnicodeDecodeError:
            print(f"Decoded (hex): {decoded.hex()}")
    except Exception:
        # Try encoding
        encoded = base64.b64encode(inp.encode("utf-8")).decode("utf-8")
        print(f"Encoded: {encoded}")


def cmd_json(args):
    """Format minified JSON."""
    if not args:
        print("Error: missing input", file=sys.stderr)
        sys.exit(1)
    inp = " ".join(args)

    try:
        parsed = json.loads(inp)
        print(json.dumps(parsed, indent=2, ensure_ascii=False))
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON — {e}", file=sys.stderr)
        sys.exit(1)


def cmd_url(args):
    """Auto-detect and URL encode/decode."""
    if not args:
        print("Error: missing input", file=sys.stderr)
        sys.exit(1)
    inp = " ".join(args)

    try:
        decoded = urllib.parse.unquote(inp)
        # If decoded is different, it was encoded
        if decoded != inp:
            print(f"Decoded: {decoded}")
        else:
            # Try encoding
            encoded = urllib.parse.quote(inp, safe="")
            print(f"Encoded: {encoded}")
    except Exception:
        print(f"Error: cannot process '{inp}'", file=sys.stderr)
        sys.exit(1)


def cmd_hash(args):
    """Compute MD5 or SHA256 hash."""
    if not args:
        print("Error: missing input", file=sys.stderr)
        sys.exit(1)
    inp = " ".join(args)

    md5 = hashlib.md5(inp.encode("utf-8")).hexdigest()
    sha256 = hashlib.sha256(inp.encode("utf-8")).hexdigest()
    print(f"MD5:     {md5}")
    print(f"SHA256:  {sha256}")


def cmd_cron(args):
    """Parse cron expression and show next 8 run times (UTC)."""

    from datetime import datetime, timezone
    import sys

    try:
        from croniter import croniter
    except ImportError:
        print("Error: croniter not installed. Install with: pip install croniter", file=sys.stderr)
        sys.exit(1)

    if not args:
        print("Error: missing cron expression", file=sys.stderr)
        sys.exit(1)

    raw_expr = " ".join(args).strip()

    # =========================
    # 1. 解析 cron 字段
    # =========================
    parts = raw_expr.split()

    seconds_mode = False
    seconds = None

    if len(parts) == 6:
        seconds_mode = True
        seconds = parts[0]
        expr = " ".join(parts[1:])
    else:
        expr = raw_expr

    # =========================
    # 2. 执行 croniter（只支持 5-field）
    # =========================
    try:
        base = datetime.now(timezone.utc)
        it = croniter(expr, base)

        # =========================
        # 3. 输出（稳定结构）
        # =========================
        print(f"Cron: {raw_expr}")
        print(f"Parsed: {expr}")

        if seconds_mode:
            print(f"(6-field detected, seconds={seconds} ignored)")

        print("Next 8 runs (UTC):")

        for _ in range(8):
            next_time = it.get_next(datetime)
            print(f"{next_time.strftime('%Y-%m-%d %H:%M:%S')}")

    except Exception as e:
        print(f"Error: invalid cron expression — {e}", file=sys.stderr)
        sys.exit(1)


def main():
    commands = {
        "time": cmd_time,
        "base64": cmd_base64,
        "json": cmd_json,
        "url": cmd_url,
        "hash": cmd_hash,
        "cron": cmd_cron,
    }

    if len(sys.argv) < 2 or sys.argv[1] not in commands:
        print("Usage: devtools.py <command> <input>", file=sys.stderr)
        print(f"Commands: {', '.join(commands.keys())}", file=sys.stderr)
        sys.exit(1)

    cmd_name = sys.argv[1]
    commands[cmd_name](sys.argv[2:])


if __name__ == "__main__":
    main()
