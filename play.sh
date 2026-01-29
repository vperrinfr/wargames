#!/bin/bash
# Global Thermonuclear War - Launch Script

echo "╔════════════════════════════════════════════════════════════════════════════╗"
echo "║                    GLOBAL THERMONUCLEAR WAR                                ║"
echo "║                    Initializing WOPR System...                             ║"
echo "╚════════════════════════════════════════════════════════════════════════════╝"
echo ""

# Set TERM if not set
if [ -z "$TERM" ]; then
    export TERM=xterm-256color
fi

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed."
    exit 1
fi

# Check if dependencies are installed
if ! python3 -c "import colorama" 2>/dev/null; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
fi

# Run the game
cd "$(dirname "$0")"
python3 src/main.py

exit 0

# Made with Bob
