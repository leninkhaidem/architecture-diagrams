#!/usr/bin/env python3
"""
Architecture Diagrams - Generator Script

Executes a Python diagram script and outputs to the current working directory.

Output goes to ./output/png/ relative to where this script is invoked (not the
skill directory), so diagrams appear in your project folder. Use --output-dir
to customize.

Usage:
    python scripts/generate.py src/examples/cisco-network.py
    python scripts/generate.py src/examples/cisco-network.py --outformat svg
    python scripts/generate.py src/examples/cisco-network.py --name custom-name
    python scripts/generate.py src/examples/cisco-network.py --output-dir /tmp/diagrams/

Examples (from a project directory):
    cd ~/projects/my-project
    python ~/.claude-wa/.claude/skills/architecture-diagrams/scripts/generate.py diagram.py
    # Output: ~/projects/my-project/output/png/diagram.png
"""

import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

# Skill directory (where this script lives)
SKILL_DIR = Path(__file__).resolve().parent.parent

def get_venv_python():
    """Return the Python executable from the skill's .venv, activating it if needed."""
    venv_python = SKILL_DIR / ".venv" / "bin" / "python"
    if venv_python.exists():
        return str(venv_python)
    # Fallback: try to set up the venv
    setup_sh = SKILL_DIR / "scripts" / "setup.sh"
    if setup_sh.exists():
        print(f"⚙️  .venv not found. Running setup.sh...")
        subprocess.run(["bash", str(setup_sh)], check=True, cwd=str(SKILL_DIR))
    if venv_python.exists():
        return str(venv_python)
    # Last resort: use current Python
    print("WARNING: .venv not found. Using system Python (diagrams may not be installed).")
    return sys.executable


def main():
    parser = argparse.ArgumentParser(
        description="Generate architecture diagram from Python script",
        epilog="Output defaults to ./output/png/ relative to the current working directory."
    )
    parser.add_argument("script", help="Path to the Python diagram script")
    parser.add_argument("--outformat", default="png", choices=["png", "jpg", "svg", "pdf", "dot"],
                        help="Output format (default: png)")
    parser.add_argument("--name", help="Custom output filename (without extension)")
    parser.add_argument("--output-dir",
                        help="Custom output directory (default: ./output/png/ relative to cwd)")
    args = parser.parse_args()

    script_path = Path(args.script).resolve()
    if not script_path.exists():
        print(f"ERROR: Script not found: {script_path}")
        sys.exit(1)

    # Output directory: custom > ./output/png/ relative to current working directory
    if args.output_dir:
        output_dir = Path(args.output_dir).resolve()
    else:
        output_dir = Path.cwd() / "output" / "png"

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

    # Use venv Python to ensure diagrams library is available
    python_exec = get_venv_python()
    print(f"Using Python: {python_exec}")

    # Execute the script with cwd set to output dir
    result = subprocess.run(
        [python_exec, str(script_path)],
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
            if f.stat().st_mtime > time.time() - 30:
                generated.append(f)

    if generated:
        print(f"\n✓ Generated {len(generated)} file(s):")
        for f in sorted(generated):
            size_kb = f.stat().st_size / 1024
            print(f"  {f} ({size_kb:.1f} KB)")
    else:
        print("\nWARNING: No output files detected. The diagram script may need adjustment.")
        print("Check that the Diagram context manager is used correctly.")


if __name__ == "__main__":
    main()
