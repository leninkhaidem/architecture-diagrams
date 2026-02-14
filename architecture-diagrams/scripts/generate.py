#!/usr/bin/env python3
"""
Architecture Diagrams - Generator Script

Executes a Python diagram script and moves the output PNG to output/png/.

Usage:
    python scripts/generate.py src/examples/cisco-network.py
    python scripts/generate.py src/examples/cisco-network.py --outformat svg
    python scripts/generate.py src/examples/cisco-network.py --name custom-name
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Generate architecture diagram from Python script")
    parser.add_argument("script", help="Path to the Python diagram script")
    parser.add_argument("--outformat", default="png", choices=["png", "jpg", "svg", "pdf", "dot"],
                        help="Output format (default: png)")
    parser.add_argument("--name", help="Custom output filename (without extension)")
    parser.add_argument("--output-dir", help="Custom output directory (default: output/png/)")
    args = parser.parse_args()

    script_path = Path(args.script).resolve()
    if not script_path.exists():
        print(f"ERROR: Script not found: {script_path}")
        sys.exit(1)

    # Determine skill root directory
    skill_dir = Path(__file__).resolve().parent.parent
    output_dir = Path(args.output_dir) if args.output_dir else skill_dir / "output" / "png"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Run the diagram script from the output directory so diagrams lib writes there
    env = os.environ.copy()
    env["DIAGRAM_OUTPUT_DIR"] = str(output_dir)
    env["DIAGRAM_OUTFORMAT"] = args.outformat

    # If custom name provided, pass it via env
    if args.name:
        env["DIAGRAM_NAME"] = args.name

    print(f"Generating diagram from: {script_path.name}")
    print(f"Output directory: {output_dir}")

    # Execute the script with cwd set to output dir
    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(output_dir),
        env=env,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        print(f"ERROR: Script failed with exit code {result.returncode}")
        if result.stderr:
            print(f"STDERR:\n{result.stderr}")
        if result.stdout:
            print(f"STDOUT:\n{result.stdout}")
        sys.exit(1)

    if result.stdout:
        print(result.stdout.rstrip())

    # Find generated files
    extensions = {args.outformat}
    generated = []
    for ext in extensions:
        for f in output_dir.glob(f"*.{ext}"):
            # Only include recently created files (within last 30 seconds)
            import time
            if f.stat().st_mtime > time.time() - 30:
                generated.append(f)

    if generated:
        print(f"\n✓ Generated {len(generated)} file(s):")
        for f in sorted(generated):
            size_kb = f.stat().st_size / 1024
            print(f"  {f.name} ({size_kb:.1f} KB)")
    else:
        print("\nWARNING: No output files detected. The diagram script may need adjustment.")
        print("Check that the Diagram context manager is used correctly.")


if __name__ == "__main__":
    main()
