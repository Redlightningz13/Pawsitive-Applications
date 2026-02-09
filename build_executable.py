"""Build a standalone executable for the Rent Value app.

This script uses PyInstaller to bundle app.py into a single executable file.
The produced executable runs without Python installed on machines that match
this build platform (same OS family and architecture).
"""

from pathlib import Path
import shutil
import subprocess
import sys


def run(cmd):
    subprocess.run(cmd, check=True)


def main():
    project_root = Path(__file__).resolve().parent
    app_file = project_root / "app.py"

    if not app_file.exists():
        raise FileNotFoundError("app.py was not found in the project root.")

    # Clean previous build artifacts for a reproducible output.
    for path_name in ["build", "dist", "app.spec"]:
        target = project_root / path_name
        if target.is_dir():
            shutil.rmtree(target)
        elif target.exists():
            target.unlink()

    run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
    run([sys.executable, "-m", "pip", "install", "pyinstaller"])

    run(
        [
            sys.executable,
            "-m",
            "PyInstaller",
            "--onefile",
            "--windowed",
            "--name",
            "PawsitiveRentCalculator",
            str(app_file),
        ]
    )

    exe_dir = project_root / "dist"
    print("\nBuild complete.")
    print(f"Executable output folder: {exe_dir}")
    print("Distribute the generated executable for this same operating system.")


if __name__ == "__main__":
    main()
