@echo off
setlocal
cd /d "%~dp0"
chcp 65001 >nul

set "PY=python"
where python >nul 2>nul
if errorlevel 1 (
  where py >nul 2>nul
  if errorlevel 1 (
    echo Python 3.8+ is required. Install it from https://www.python.org/downloads/
    pause
    exit /b 1
  )
  set "PY=py -3"
)

%PY% antigravity_zh.py --update
pause
