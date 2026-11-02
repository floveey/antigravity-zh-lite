#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Antigravity zh-CN Lite - restore the official installation.

Removes the extracted resources/app directory and restores app.asar from
app.asar.disabled. Use this to return Antigravity to its official state.

Usage:
    python restore_official.py
    python restore_official.py --dist "D:\\path\\to\\resources\\app\\dist"
    python restore_official.py --dry-run
"""
import argparse
import os
import shutil
import subprocess
import sys


def default_dist():
    local = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~")
    return os.path.join(local, "Programs", "antigravity", "resources", "app", "dist")


def is_app_running():
    if os.name != "nt":
        return False
    try:
        out = subprocess.run(
            ["tasklist", "/FI", "IMAGENAME eq Antigravity.exe"],
            capture_output=True, text=True, timeout=10,
        ).stdout
        return "Antigravity.exe" in out
    except Exception:
        return False


def main():
    parser = argparse.ArgumentParser(description="Restore official Antigravity files")
    parser.add_argument("--dist", default=default_dist(), help="path to resources/app/dist")
    parser.add_argument("--dry-run", action="store_true", help="show actions without changing files")
    args = parser.parse_args()

    app_dir = os.path.dirname(args.dist)
    resources = os.path.dirname(app_dir)
    asar = os.path.join(resources, "app.asar")
    disabled = asar + ".disabled"
    old = app_dir + ".old"

    if not os.path.isdir(resources):
        print(f"[error] resources directory not found: {resources}")
        return 2

    if not args.dry_run and is_app_running():
        print("[error] Antigravity is running. Quit it completely (including tray), then retry.")
        return 1

    if not os.path.exists(disabled) and not os.path.exists(asar):
        print("[error] neither app.asar nor app.asar.disabled found; refusing to delete the app directory.")
        print("        Reinstall Antigravity to repair the installation.")
        return 1

    try:
        if os.path.exists(disabled):
            if os.path.exists(asar):
                print("[remove] old app.asar")
                if not args.dry_run:
                    os.remove(asar)
            print("[restore] app.asar.disabled -> app.asar")
            if not args.dry_run:
                os.rename(disabled, asar)
        else:
            print("[ok] app.asar is already present")

        if os.path.isdir(old):
            print(f"[remove] {old}")
            if not args.dry_run:
                shutil.rmtree(old, ignore_errors=True)

        if os.path.isdir(app_dir):
            print(f"[remove] {app_dir}")
            if not args.dry_run:
                shutil.rmtree(app_dir, ignore_errors=True)
        else:
            print("[ok] extracted app directory is not present")
    except Exception as e:
        print(f"[error] restore failed: {e}")
        return 1

    if args.dry_run:
        print("Dry run: no files changed.")
    else:
        print("Done. Antigravity is back to the official version.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
