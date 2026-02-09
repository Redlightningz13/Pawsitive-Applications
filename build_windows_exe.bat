@echo off
setlocal

where python >nul 2>nul
if %errorlevel% neq 0 (
  echo Python is required to build the EXE. Install Python 3.11+ and try again.
  exit /b 1
)

python -m pip install --upgrade pip
if %errorlevel% neq 0 exit /b 1

python -m pip install pyinstaller
if %errorlevel% neq 0 exit /b 1

if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist app.spec del /q app.spec

python -m PyInstaller --onefile --windowed --name PawsitiveRentCalculator app.py
if %errorlevel% neq 0 exit /b 1

echo.
echo Build complete. Your Windows executable is in dist\PawsitiveRentCalculator.exe
endlocal
