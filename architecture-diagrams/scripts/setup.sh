#!/usr/bin/env bash
# Architecture Diagrams - Setup Script
# Creates Python venv and installs all dependencies

set -euo pipefail

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${SKILL_DIR}/.venv"

echo "=== Architecture Diagrams Setup ==="
echo "Skill directory: ${SKILL_DIR}"

# --- Check system dependency: graphviz binary ---
if ! command -v dot &>/dev/null; then
    echo ""
    echo "ERROR: Graphviz is not installed (the 'dot' command is missing)."
    echo ""
    echo "Install it with:"
    echo "  Ubuntu/Debian:  sudo apt install graphviz"
    echo "  macOS:          brew install graphviz"
    echo "  RHEL/Fedora:    sudo dnf install graphviz"
    echo ""
    exit 1
fi
echo "✓ Graphviz found: $(dot -V 2>&1)"

# --- Check Python ---
PYTHON=""
for candidate in python3 python; do
    if command -v "$candidate" &>/dev/null; then
        PYTHON="$candidate"
        break
    fi
done

if [ -z "$PYTHON" ]; then
    echo "ERROR: Python 3.7+ is required but not found."
    exit 1
fi
echo "✓ Python found: $(${PYTHON} --version)"

# --- Create virtual environment ---
if [ ! -d "${VENV_DIR}" ]; then
    echo "Creating virtual environment..."
    ${PYTHON} -m venv "${VENV_DIR}"
    echo "✓ Virtual environment created at ${VENV_DIR}"
else
    echo "✓ Virtual environment already exists"
fi

# --- Activate and install ---
source "${VENV_DIR}/bin/activate"
echo "Installing Python dependencies..."
pip install --quiet --upgrade pip
pip install --quiet -r "${SKILL_DIR}/requirements.txt"

echo ""
echo "✓ All dependencies installed"
echo ""

# --- Verify installation ---
python -c "import diagrams; print(f'✓ diagrams {diagrams.__version__} ready')" 2>/dev/null || \
    python -c "import diagrams; print('✓ diagrams package ready')"
python -c "import graphviz; print(f'✓ graphviz Python binding ready')"

echo ""
echo "=== Setup Complete ==="
echo ""
echo "Usage:"
echo "  source ${VENV_DIR}/bin/activate"
echo "  python scripts/generate.py src/examples/cisco-network.py"
echo "  # Output: output/png/cisco-network.png"
