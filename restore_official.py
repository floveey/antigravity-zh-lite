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


def _clean_install_value(value):
    text = str(value).strip()
    if not text:
        return ""
    if "," in text and text.lower().endswith((",0", ",1")):
        text = text.rsplit(",", 1)[0]
    if text.startswith('"'):
        end = text.find('"', 1)
        if end != -1:
            text = text[1:end]
    elif " /" in text:
        text = text.split(" /", 1)[0]
    text = text.strip().strip('"')
    if os.path.isfile(text):
        return os.path.dirname(text)
    if os.path.isdir(text):
        return text
    return ""


def find_install_root():
    local = os.environ.get("LOCALAPPDATA") or ""
    program_files = os.environ.get("ProgramFiles") or ""
    program_files_x86 = os.environ.get("ProgramFiles(x86)") or ""
    candidates = []
    for base in (
        os.path.join(local, "Programs", "antigravity") if local else "",
        os.path.join(program_files, "Antigravity") if program_files else "",
        os.path.join(program_files_x86, "Antigravity") if program_files_x86 else "",
        os.path.join(local, "Programs", "Antigravity") if local else "",
    ):
        if base:
            candidates.append(base)
    if os.name == "nt":
        try:
            import winreg
            keys = [
                (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Uninstall"),
                (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Uninstall"),
                (winreg.HKEY_LOCAL_MACHINE, r"Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall"),
            ]
            for hive, path in keys:
                try:
                    with winreg.OpenKey(hive, path) as root:
                        for i in range(winreg.QueryInfoKey(root)[0]):
                            try:
                                name = winreg.EnumKey(root, i)
                                with winreg.OpenKey(root, name) as sub:
                                    try:
                                        display, _ = winreg.QueryValueEx(sub, "DisplayName")
                                    except OSError:
                                        continue
                                    if "antigravity" not in str(display).lower():
                                        continue
                                    for value in ("InstallLocation", "DisplayIcon", "UninstallString"):
                                        try:
                                            raw, _ = winreg.QueryValueEx(sub, value)
                                        except OSError:
                                            continue
                                        candidate = _clean_install_value(raw)
                                        if candidate:
                                            candidates.append(candidate)
                            except OSError:
                                continue
                except OSError:
                    continue
        except ImportError:
            pass
    for candidate in candidates:
        if candidate and os.path.isdir(os.path.join(candidate, "resources")):
            return candidate
    for candidate in candidates:
        if candidate and os.path.isfile(os.path.join(candidate, "Antigravity.exe")):
            return candidate
    return None


def default_dist():
    root = find_install_root()
    if root:
        return os.path.join(root, "resources", "app", "dist")
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
    parser.add_argument("--print-dist", action="store_true", help="print the detected dist path and exit")
    args = parser.parse_args()

    if args.print_dist:
        print(args.dist)
        return 0

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
