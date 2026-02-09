# Rent Value Desktop App

This repository includes a desktop calculator that helps you enter:
- average monthly rent per unit,
- weekly total property cost / price being charged,
- number of units,

and computes:
- weekly cost per unit,
- cost as a percentage of monthly rent,
- a full sales paragraph with calculated values substituted in.

## Run from source

```bash
python3 app.py
```

The app uses Python's built-in `tkinter`, so no third-party dependencies are required to run from source.

## Build a standalone executable (no Python required on the target machine)

Run:

```bash
python3 build_executable.py
```

This creates a bundled executable in `dist/` named `PawsitiveRentCalculator` (or `PawsitiveRentCalculator.exe` on Windows).

> Important: executables are platform-specific.  
> To run on Windows, build on Windows.  
> To run on macOS, build on macOS.  
> To run on Linux, build on Linux.

## Build a Windows `.exe`

### Option 1 (recommended): GitHub Actions (no local Windows setup needed)

1. Push this repo to GitHub.
2. Open the **Actions** tab.
3. Run **Build Windows EXE** workflow.
4. Download the artifact named **PawsitiveRentCalculator-windows**.

### Option 2: Build locally on Windows

On a Windows PC, double-click or run:

```bat
build_windows_exe.bat
```

This creates:

- `dist\PawsitiveRentCalculator.exe`

## Optional logo

To show your brand logo in the app header, place one of these files in the project root:
- `pawsitive_logo.png` (preferred)
- `logo.png`
- `pawsitive.png`


## Android app

An Android version is included under `android-app/` (Kotlin + Jetpack Compose).

- Open `android-app/` in Android Studio.
- Let Gradle sync.
- Run on an emulator or Android device.

### Android logo
The Android launcher icon uses `app/src/main/res/drawable/ic_logo_foreground.xml`.
If you want to use your exact provided image, replace that vector with PNG assets generated via Android Studio:
`New > Image Asset` and select your dog logo image.
