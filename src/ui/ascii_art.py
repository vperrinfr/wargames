"""
Global Thermal Nuclear War - ASCII Art
Visual elements and world map rendering
"""

# ASCII World Map (simplified for terminal display)
WORLD_MAP = """
                                    ARCTIC OCEAN
    
         NORTH                                              ASIA
        AMERICA          ATLANTIC                                    PACIFIC
                          OCEAN                                       OCEAN
    
                                    EUROPE
    
                                              MIDDLE
                                               EAST
                  AFRICA
    
                                                        AUSTRALIA
    
         SOUTH
        AMERICA
                                    ANTARCTICA
"""

# Detailed ASCII World Map with coordinates
DETAILED_MAP = [
    "                                                                                                    ",
    "                    ╔═══════════════════════════════════════════════════════════════════════════╗",
    "                    ║                    GLOBAL THERMONUCLEAR WAR                               ║",
    "                    ╚═══════════════════════════════════════════════════════════════════════════╝",
    "                                                                                                    ",
    "        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░",
    "      ░░                                                                                      ░░  ",
    "    ░░    ▓▓▓▓                                                                                ░░  ",
    "   ░░   ▓▓▓▓▓▓▓▓                    ▒▒▒▒▒▒                                                    ░░ ",
    "  ░░   ▓▓▓▓▓▓▓▓▓                  ▒▒▒▒▒▒▒▒▒▒                                                  ░░ ",
    "  ░░    ▓▓▓▓▓▓▓                  ▒▒▒▒▒▒▒▒▒▒▒▒▒                                                ░░ ",
    "  ░░     ▓▓▓▓▓                   ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ░░ ",
    "  ░░      ▓▓▓                    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ░░ ",
    "  ░░       ▓                      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ░░ ",
    "  ░░                              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒   ░░ ",
    "  ░░                               ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒     ░░ ",
    "  ░░                                 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒       ░░ ",
    "  ░░          ███                      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒         ░░ ",
    "  ░░         █████                       ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒           ░░ ",
    "  ░░        ███████                                                                          ░░ ",
    "  ░░        ███████                                                                          ░░ ",
    "  ░░         █████                                                                           ░░ ",
    "   ░░         ███                                                                           ░░  ",
    "    ░░         █                                                                           ░░   ",
    "     ░░                                                                                    ░░    ",
    "       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░      ",
    "                                                                                                 ",
]

# WOPR Logo
WOPR_LOGO = """
██╗    ██╗   ██╗ ██████╗    ██████╗    ██████╗ 
██║    ██║   ██║██╔═══██╗   ██╔══██╗   ██╔══██╗
██║ █╗ ██║   ██║██║   ██║   ██████╔╝   ██████╔╝
██║███╗██║   ██║██║   ██║   ██╔═══╝    ██╔══██╗
╚███╔███╔╝██╗╚██████╔╝██╗██║  ██╗██╗██║  ██║
 ╚══╝╚══╝ ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
"""

# Title Screen
TITLE_SCREEN = """
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║   ██████╗ ██╗      ██████╗ ██████╗  █████╗ ██╗                            ║
║  ██╔════╝ ██║     ██╔═══██╗██╔══██╗██╔══██╗██║                            ║
║  ██║  ███╗██║     ██║   ██║██████╔╝███████║██║                            ║
║  ██║   ██║██║     ██║   ██║██╔══██╗██╔══██║██║                            ║
║  ╚██████╔╝███████╗╚██████╔╝██████╔╝██║  ██║███████╗                       ║
║   ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝                       ║
║                                                                            ║
║  ████████╗██╗  ██╗███████╗██████╗ ███╗   ███╗ █████╗ ██╗                 ║
║  ╚══██╔══╝██║  ██║██╔════╝██╔══██╗████╗ ████║██╔══██╗██║                 ║
║     ██║   ███████║█████╗  ██████╔╝██╔████╔██║███████║██║                 ║
║     ██║   ██╔══██║██╔══╝  ██╔══██╗██║╚██╔╝██║██╔══██║██║                 ║
║     ██║   ██║  ██║███████╗██║  ██║██║ ╚═╝ ██║██║  ██║███████╗            ║
║     ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝            ║
║                                                                            ║
║  ███╗   ██╗██╗   ██╗ ██████╗██╗     ███████╗ █████╗ ██████╗              ║
║  ████╗  ██║██║   ██║██╔════╝██║     ██╔════╝██╔══██╗██╔══██╗             ║
║  ██╔██╗ ██║██║   ██║██║     ██║     █████╗  ███████║██████╔╝             ║
║  ██║╚██╗██║██║   ██║██║     ██║     ██╔══╝  ██╔══██║██╔══██╗             ║
║  ██║ ╚████║╚██████╔╝╚██████╗███████╗███████╗██║  ██║██║  ██║             ║
║  ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝             ║
║                                                                            ║
║  ██╗    ██╗ █████╗ ██████╗                                                ║
║  ██║    ██║██╔══██╗██╔══██╗                                               ║
║  ██║ █╗ ██║███████║██████╔╝                                               ║
║  ██║███╗██║██╔══██║██╔══██╗                                               ║
║  ╚███╔███╔╝██║  ██║██║  ██║                                               ║
║   ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝                                               ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
"""

# Missile ASCII Art
MISSILE_FRAMES = [
    "    |    ",
    "   /|\\   ",
    "  / | \\  ",
    " /  |  \\ ",
    "/   |   \\",
]

MISSILE_TRAIL = ["·", ":", "∴", "∷", "░", "▒", "▓"]

# Explosion Animation Frames
EXPLOSION_FRAMES = [
    "    *    ",
    "   ***   ",
    "  *****  ",
    " ******* ",
    "*********",
    " ☼☼☼☼☼☼☼ ",
    "  ☼☼☼☼☼  ",
    "   ☼☼☼   ",
    "    ☼    ",
    "    ·    ",
]

# Target Symbols
TARGET_SYMBOLS = {
    'CITY': '◉',
    'MILITARY_BASE': '▣',
    'MISSILE_SILO': '◈',
    'COMMAND_CENTER': '◆',
    'DESTROYED': '✕',
}

# Status Indicators
STATUS_INDICATORS = {
    'active': '●',
    'warning': '◐',
    'critical': '◯',
    'destroyed': '✕',
}

# Radar Display
RADAR_FRAMES = [
    """
        ╱─────╲
       ╱       ╲
      │    ◜    │
       ╲       ╱
        ╲─────╱
    """,
    """
        ╱─────╲
       ╱       ╲
      │    ◝    │
       ╲       ╱
        ╲─────╱
    """,
    """
        ╱─────╲
       ╱       ╲
      │    ◞    │
       ╲       ╱
        ╲─────╱
    """,
    """
        ╱─────╲
       ╱       ╲
      │    ◟    │
       ╲       ╱
        ╲─────╱
    """,
]

# Loading Bar
def create_loading_bar(progress, width=40):
    """Create a loading bar with given progress (0-100)"""
    filled = int(width * progress / 100)
    bar = '█' * filled + '░' * (width - filled)
    return f"[{bar}] {progress}%"

# Box Drawing
def create_box(title, content, width=80):
    """Create a box with title and content"""
    top = f"╔{'═' * (width - 2)}╗"
    title_line = f"║ {title.center(width - 4)} ║"
    separator = f"╠{'═' * (width - 2)}╣"
    bottom = f"╚{'═' * (width - 2)}╝"
    
    lines = [top, title_line, separator]
    for line in content.split('\n'):
        lines.append(f"║ {line.ljust(width - 4)} ║")
    lines.append(bottom)
    
    return '\n'.join(lines)

# Menu Items
def create_menu(title, items, selected=0):
    """Create a menu with selectable items"""
    menu_lines = [f"\n{title}\n", "=" * len(title), ""]
    for i, item in enumerate(items):
        prefix = "► " if i == selected else "  "
        menu_lines.append(f"{prefix}{item}")
    return '\n'.join(menu_lines)

# Statistics Display
def create_stats_display(stats):
    """Create a statistics display"""
    lines = [
        "╔════════════════════════════════════════╗",
        "║          MISSION STATISTICS            ║",
        "╠════════════════════════════════════════╣",
    ]
    
    for key, value in stats.items():
        line = f"║ {key.ljust(25)}: {str(value).rjust(10)} ║"
        lines.append(line)
    
    lines.append("╚════════════════════════════════════════╝")
    return '\n'.join(lines)

# Countdown Display
def create_countdown(seconds):
    """Create a countdown display"""
    return f"""
    ╔═══════════════╗
    ║   LAUNCH IN   ║
    ║               ║
    ║      {str(seconds).center(2)}       ║
    ║               ║
    ╚═══════════════╝
    """

# Alert Banner
def create_alert(message, alert_type='warning'):
    """Create an alert banner"""
    symbols = {
        'warning': '⚠',
        'danger': '☢',
        'info': 'ℹ',
        'success': '✓',
    }
    symbol = symbols.get(alert_type, '!')
    
    width = len(message) + 10
    return f"""
╔{'═' * width}╗
║ {symbol} {message.center(width - 4)} {symbol} ║
╚{'═' * width}╝
    """

# Typing Effect Text
def get_typing_text(text, position):
    """Get text for typing effect animation"""
    return text[:position]

if __name__ == "__main__":
    # Test ASCII art
    print(TITLE_SCREEN)
    print("\n" + WOPR_LOGO)
    print("\n" + create_box("TEST", "This is a test box\nWith multiple lines"))
    print("\n" + create_menu("MAIN MENU", ["Start Game", "Options", "Exit"], 0))
    print("\n" + create_loading_bar(75))
    print("\n" + create_alert("MISSILE LAUNCH DETECTED", 'danger'))

# Made with Bob
