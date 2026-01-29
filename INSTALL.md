# Installation and Setup Guide

## System Requirements

- **Python**: 3.8 or higher
- **Operating System**: macOS, Linux, or Windows
- **Terminal**: Any terminal with ANSI color support
- **Dependencies**: Listed in `requirements.txt`

## Installation Steps

### 1. Navigate to Game Directory

```bash
cd /Users/vperrin/Documents/work/wargame
```

### 2. Install Python Dependencies

```bash
pip3 install -r requirements.txt
```

This will install:
- `colorama` - Cross-platform colored terminal text
- `python-dateutil` - Date utilities

### 3. Verify Installation

Run the test script to ensure everything is working:

```bash
python3 test_game.py
```

You should see:
```
✅ All tests passed! Game is ready to play.
```

## Running the Game

### Method 1: Launch Script (Recommended)

```bash
./play.sh
```

The launch script will:
- Check for Python 3
- Set up the terminal environment
- Install dependencies if needed
- Launch the game

### Method 2: Direct Python Execution

```bash
python3 src/main.py
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'colorama'"

**Solution:** Install dependencies
```bash
pip3 install -r requirements.txt
```

### "Permission denied: ./play.sh"

**Solution:** Make the script executable
```bash
chmod +x play.sh
```

### "TERM environment variable not set"

**Solution:** Set the TERM variable
```bash
export TERM=xterm-256color
python3 src/main.py
```

Or use the launch script which sets this automatically:
```bash
./play.sh
```

### Colors not displaying correctly

**Solution:** Ensure your terminal supports ANSI colors. Most modern terminals do. Try:
- Terminal.app (macOS)
- iTerm2 (macOS)
- GNOME Terminal (Linux)
- Windows Terminal (Windows)

### Import errors

**Solution:** The game uses absolute imports from the `src` package. The main.py file automatically adds the parent directory to Python's path. If you still have issues, run from the project root:

```bash
cd /Users/vperrin/Documents/work/wargame
python3 src/main.py
```

## Uninstallation

To remove the game:

```bash
cd /Users/vperrin/Documents/work
rm -rf wargame
```

To remove Python dependencies (if not used by other projects):

```bash
pip3 uninstall colorama python-dateutil
```

## Development Setup

If you want to modify the game:

1. **Install in development mode:**
   ```bash
   pip3 install -e .
   ```

2. **Run tests:**
   ```bash
   python3 test_game.py
   ```

3. **Check syntax:**
   ```bash
   python3 -m py_compile src/**/*.py
   ```

## File Structure

```
wargame/
├── play.sh              # Launch script
├── test_game.py         # Test script
├── requirements.txt     # Python dependencies
├── README.md           # Project overview
├── QUICKSTART.md       # Quick start guide
├── INSTALL.md          # This file
├── docs/
│   ├── GAMEPLAY.md     # Gameplay guide
│   └── DESIGN.md       # Technical documentation
└── src/
    ├── main.py         # Entry point
    ├── game_engine.py  # Game engine
    ├── ai/             # AI components
    ├── game_logic/     # Game logic
    ├── ui/             # User interface
    └── utils/          # Utilities
```

## Getting Help

- **Quick Start:** See `QUICKSTART.md`
- **Gameplay Help:** See `docs/GAMEPLAY.md`
- **Technical Details:** See `docs/DESIGN.md`
- **Project Overview:** See `README.md`

## Next Steps

Once installed, see `QUICKSTART.md` for how to play the game.

---

*"Shall we play a game?"* - WOPR