# Global Thermonuclear War - Quick Start Guide

## Installation

1. **Navigate to the game directory:**
   ```bash
   cd /Users/vperrin/Documents/work/wargame
   ```

2. **Install dependencies:**
   ```bash
   pip3 install -r requirements.txt
   ```

## Running the Game

### Option 1: Using the launch script (Recommended)
```bash
./play.sh
```

### Option 2: Direct Python execution
```bash
python3 src/main.py
```

## First Time Playing

1. **Watch the intro sequence** - The WOPR system will initialize
2. **Login as JOSHUA** - The authentication is automatic
3. **Choose a game mode:**
   - Press `1` for Campaign Mode (recommended for first-time players)
   - Press `3` for Tutorial to learn the mechanics

4. **Select difficulty:**
   - Press `1` for Easy (good for learning)
   - Press `2` for Normal (balanced challenge)

## Basic Controls

During gameplay:
- **L** - Launch a missile
- **S** - Show statistics
- **P** - Propose peace
- **Q** - Quit game

## Quick Tips

1. **Don't launch all missiles at once** - You'll need reserves
2. **Target high-value assets first** - Command Centers and Missile Silos
3. **Watch for WOPR's retaliation** - The AI will respond to your attacks
4. **Consider peace** - Sometimes not playing is the best move
5. **Read the messages** - WOPR's quotes provide strategic hints

## Troubleshooting

### "ModuleNotFoundError: No module named 'colorama'"
Run: `pip3 install -r requirements.txt`

### "TERM environment variable not set"
This is just a warning. The game will still work. Or run: `export TERM=xterm-256color`

### Game doesn't display colors
Make sure you're using a terminal that supports ANSI colors (most modern terminals do).

## Game Objective

Remember WOPR's wisdom:
> *"A strange game. The only winning move is not to play."*

The goal is to understand the futility of nuclear warfare. Try to achieve peace rather than total destruction.

## Need More Help?

- **Detailed Gameplay Guide:** See `docs/GAMEPLAY.md`
- **Technical Documentation:** See `docs/DESIGN.md`
- **Full README:** See `README.md`

## Have Fun!

Enjoy playing Global Thermonuclear War, and remember - the best victory is peace! 🕊️

---

*"Shall we play a game?"* - WOPR