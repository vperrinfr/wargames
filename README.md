# Global Thermal Nuclear War

A text-based terminal game inspired by the 1983 film "WarGames". Experience the tension of Cold War nuclear strategy in an authentic retro computer interface.

```
 ██████╗ ██╗      ██████╗ ██████╗  █████╗ ██╗         
██╔════╝ ██║     ██╔═══██╗██╔══██╗██╔══██╗██║         
██║  ███╗██║     ██║   ██║██████╔╝███████║██║         
██║   ██║██║     ██║   ██║██╔══██╗██╔══██║██║         
╚██████╔╝███████╗╚██████╔╝██████╔╝██║  ██║███████╗    
 ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    
                                                        
████████╗██╗  ██╗███████╗██████╗ ███╗   ███╗ █████╗ ██╗     
╚══██╔══╝██║  ██║██╔════╝██╔══██╗████╗ ████║██╔══██╗██║     
   ██║   ███████║█████╗  ██████╔╝██╔████╔██║███████║██║     
   ██║   ██╔══██║██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══██║██║     
   ██║   ██║  ██║███████╗██║  ██║██║ ╚═╝ ██║██║  ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝
                                                              
███╗   ██╗██╗   ██╗ ██████╗██╗     ███████╗ █████╗ ██████╗  
████╗  ██║██║   ██║██╔════╝██║     ██╔════╝██╔══██╗██╔══██╗ 
██╔██╗ ██║██║   ██║██║     ██║     █████╗  ███████║██████╔╝ 
██║╚██╗██║██║   ██║██║     ██║     ██╔══╝  ██╔══██║██╔══██╗ 
██║ ╚████║╚██████╔╝╚██████╗███████╗███████╗██║  ██║██║  ██║ 
╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ 
                                                              
██╗    ██╗ █████╗ ██████╗                                    
██║    ██║██╔══██╗██╔══██╗                                   
██║ █╗ ██║███████║██████╔╝                                   
██║███╗██║██╔══██║██╔══██╗                                   
╚███╔███╔╝██║  ██║██║  ██║                                   
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝                                   
```

> *"A strange game. The only winning move is not to play."* - WOPR

## 🎮 Features

- **Authentic 1980s Terminal Interface**: Green phosphor display simulation
- **Strategic Gameplay**: Turn-based nuclear warfare simulation
- **AI Opponent (WOPR)**: Intelligent computer adversary with adaptive strategies
- **ASCII World Map**: Visual representation of global targets
- **Missile Animations**: Watch ICBMs arc across the terminal
- **Multiple Game Modes**: Campaign, Simulation, and Tutorial
- **WarGames References**: Easter eggs and quotes from the classic film

## 📋 Requirements

- Python 3.8 or higher
- Terminal with color support (most modern terminals)
- Minimum terminal size: 80x24 characters (recommended: 120x40)

## 🚀 Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd wargame
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 How to Play

Run the game:
```bash
python src/main.py
```

### Game Modes

1. **Campaign Mode**: Play against the WOPR AI
   - Strategic target selection
   - Resource management
   - Progressive difficulty

2. **Simulation Mode**: Watch AI vs AI
   - Demonstrates the futility of nuclear war
   - Educational experience

3. **Tutorial Mode**: Learn the mechanics
   - Step-by-step guidance
   - Practice without consequences

### Controls

- **Arrow Keys**: Navigate menus and map
- **Enter**: Select/Confirm
- **Space**: Launch missile
- **ESC**: Pause/Menu
- **Q**: Quit (with confirmation)

### Gameplay Tips

- **Target Priority**: Military installations > Cities > Infrastructure
- **Resource Management**: You have limited missiles
- **Defense Systems**: Some targets have anti-missile capabilities
- **Escalation**: The AI will respond to your aggression
- **Victory**: Remember WOPR's lesson - sometimes not playing is winning

## 🏗️ Project Structure

```
wargame/
├── src/
│   ├── main.py              # Entry point
│   ├── game_engine.py       # Core game loop
│   ├── ui/
│   │   ├── terminal_ui.py   # Curses-based UI
│   │   ├── animations.py    # Missile animations
│   │   └── ascii_art.py     # Map and graphics
│   ├── game_logic/
│   │   ├── world_map.py     # Map data and rendering
│   │   ├── missile.py       # Missile mechanics
│   │   ├── target.py        # Target management
│   │   └── combat.py        # Combat resolution
│   ├── ai/
│   │   ├── wopr_ai.py       # AI opponent
│   │   └── strategy.py      # AI decision making
│   └── utils/
│       ├── config.py        # Game configuration
│       └── sound.py         # Terminal sound effects
├── assets/
│   └── maps/
│       └── world_ascii.txt  # ASCII world map
├── docs/
│   ├── GAMEPLAY.md          # Detailed gameplay guide
│   └── DESIGN.md            # Technical design document
├── requirements.txt
├── README.md
└── .gitignore
```

## 🎨 Screenshots

```
╔════════════════════════════════════════════════════════════════════════════╗
║                    W.O.P.R. DEFENSE SYSTEM v2.4                            ║
║                    War Operation Plan Response                             ║
╚════════════════════════════════════════════════════════════════════════════╝

LOGON: [████████████]

PASSWORD: ****************

GREETINGS PROFESSOR FALKEN.

SHALL WE PLAY A GAME?

> GLOBAL THERMONUCLEAR WAR
```

## 🛠️ Development

### Running Tests
```bash
python -m pytest tests/
```

### Code Style
This project follows PEP 8 guidelines. Format code with:
```bash
black src/
```

## 📚 Documentation

- [Gameplay Guide](docs/GAMEPLAY.md) - Detailed instructions and strategies
- [Design Document](docs/DESIGN.md) - Technical architecture and implementation

## 🎬 Inspiration

This game is inspired by the 1983 film "WarGames" directed by John Badham, starring Matthew Broderick. The film explores themes of nuclear war, artificial intelligence, and the importance of human judgment in automated systems.

## ⚠️ Educational Purpose

This game is designed to be educational and thought-provoking. It demonstrates the concept of Mutual Assured Destruction (MAD) and the futility of nuclear warfare. The best outcome is always to find a peaceful resolution.

## 📝 License

This project is created for educational purposes. Feel free to modify and share.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 🙏 Acknowledgments

- The creators of "WarGames" (1983)
- The Python curses library developers
- Cold War historians and nuclear policy experts who have documented this era

---

*"The only winning move is not to play. How about a nice game of chess?"*