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

## Optional logo

To show your brand logo in the app header, place one of these files in the project root:
- `pawsitive_logo.png` (preferred)
- `logo.png`
- `pawsitive.png`
