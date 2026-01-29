"""
Global Thermal Nuclear War - Configuration
Game settings and constants
"""

# Display Settings
TERMINAL_MIN_WIDTH = 80
TERMINAL_MIN_HEIGHT = 24
TERMINAL_RECOMMENDED_WIDTH = 120
TERMINAL_RECOMMENDED_HEIGHT = 40

# Colors (for colorama)
COLOR_SCHEME = {
    'primary': 'green',      # Main text color (phosphor green)
    'warning': 'yellow',     # Warnings
    'danger': 'red',         # Critical alerts
    'info': 'cyan',          # Information
    'success': 'green',      # Success messages
    'dim': 'white',          # Dimmed text
}

# Game Settings
GAME_SPEED = {
    'slow': 2.0,
    'normal': 1.0,
    'fast': 0.5,
}

# Player Settings
PLAYER_STARTING_MISSILES = 50
PLAYER_STARTING_DEFENSES = 20

# AI Settings
AI_DIFFICULTY = {
    'easy': {
        'reaction_time': 3.0,
        'accuracy': 0.6,
        'aggression': 0.3,
    },
    'normal': {
        'reaction_time': 2.0,
        'accuracy': 0.75,
        'aggression': 0.5,
    },
    'hard': {
        'reaction_time': 1.0,
        'accuracy': 0.9,
        'aggression': 0.7,
    },
    'wopr': {
        'reaction_time': 0.5,
        'accuracy': 0.95,
        'aggression': 0.9,
    }
}

# Missile Types
MISSILE_TYPES = {
    'ICBM': {
        'name': 'Intercontinental Ballistic Missile',
        'range': 10000,  # km
        'speed': 7.0,    # km/s
        'warheads': 10,
        'accuracy': 0.9,
        'cost': 5,
    },
    'SLBM': {
        'name': 'Submarine-Launched Ballistic Missile',
        'range': 8000,
        'speed': 6.5,
        'warheads': 8,
        'accuracy': 0.85,
        'cost': 4,
    },
    'CRUISE': {
        'name': 'Cruise Missile',
        'range': 2500,
        'speed': 0.8,
        'warheads': 1,
        'accuracy': 0.95,
        'cost': 2,
    },
}

# Target Types
TARGET_TYPES = {
    'CITY': {
        'name': 'City',
        'population': 1000000,
        'strategic_value': 50,
        'defense_level': 0.3,
    },
    'MILITARY_BASE': {
        'name': 'Military Base',
        'population': 10000,
        'strategic_value': 100,
        'defense_level': 0.7,
    },
    'MISSILE_SILO': {
        'name': 'Missile Silo',
        'population': 100,
        'strategic_value': 150,
        'defense_level': 0.9,
    },
    'COMMAND_CENTER': {
        'name': 'Command Center',
        'population': 1000,
        'strategic_value': 200,
        'defense_level': 0.95,
    },
}

# World Map Coordinates (simplified)
WORLD_TARGETS = {
    'USA': [
        {'name': 'Washington DC', 'type': 'COMMAND_CENTER', 'x': 20, 'y': 15},
        {'name': 'New York', 'type': 'CITY', 'x': 22, 'y': 14},
        {'name': 'Los Angeles', 'type': 'CITY', 'x': 10, 'y': 16},
        {'name': 'Chicago', 'type': 'CITY', 'x': 18, 'y': 14},
        {'name': 'NORAD', 'type': 'COMMAND_CENTER', 'x': 15, 'y': 15},
        {'name': 'Minuteman III Silo', 'type': 'MISSILE_SILO', 'x': 16, 'y': 13},
        {'name': 'Pentagon', 'type': 'MILITARY_BASE', 'x': 20, 'y': 15},
    ],
    'USSR': [
        {'name': 'Moscow', 'type': 'COMMAND_CENTER', 'x': 55, 'y': 10},
        {'name': 'Leningrad', 'type': 'CITY', 'x': 54, 'y': 8},
        {'name': 'Kiev', 'type': 'CITY', 'x': 54, 'y': 12},
        {'name': 'Vladivostok', 'type': 'MILITARY_BASE', 'x': 75, 'y': 13},
        {'name': 'SS-18 Silo', 'type': 'MISSILE_SILO', 'x': 60, 'y': 11},
        {'name': 'Kremlin', 'type': 'COMMAND_CENTER', 'x': 55, 'y': 10},
    ],
    'EUROPE': [
        {'name': 'London', 'type': 'CITY', 'x': 48, 'y': 10},
        {'name': 'Paris', 'type': 'CITY', 'x': 49, 'y': 11},
        {'name': 'Berlin', 'type': 'CITY', 'x': 51, 'y': 10},
        {'name': 'NATO HQ', 'type': 'MILITARY_BASE', 'x': 49, 'y': 11},
    ],
    'ASIA': [
        {'name': 'Beijing', 'type': 'COMMAND_CENTER', 'x': 70, 'y': 14},
        {'name': 'Tokyo', 'type': 'CITY', 'x': 76, 'y': 15},
        {'name': 'Seoul', 'type': 'CITY', 'x': 73, 'y': 15},
    ],
}

# Animation Settings
ANIMATION_FRAMES = {
    'missile_launch': ['|', '/', '-', '\\'],
    'explosion': ['*', '☼', '✸', '✹', '✺', '○', '·'],
    'radar_sweep': ['◜', '◝', '◞', '◟'],
}

# Sound Effects (terminal beeps)
SOUND_ENABLED = True
SOUND_EFFECTS = {
    'launch': '\a',
    'explosion': '\a\a',
    'warning': '\a\a\a',
    'alert': '\a' * 5,
}

# WarGames Quotes
WOPR_QUOTES = [
    "GREETINGS PROFESSOR FALKEN.",
    "SHALL WE PLAY A GAME?",
    "A STRANGE GAME. THE ONLY WINNING MOVE IS NOT TO PLAY.",
    "HOW ABOUT A NICE GAME OF CHESS?",
    "WOULDN'T YOU PREFER A GOOD GAME OF CHESS?",
    "WINNER: NONE",
    "ESTIMATED CASUALTIES: EVERYONE",
]

# Game Messages
MESSAGES = {
    'welcome': """
╔════════════════════════════════════════════════════════════════════════════╗
║                    W.O.P.R. DEFENSE SYSTEM v2.4                            ║
║                    War Operation Plan Response                             ║
╚════════════════════════════════════════════════════════════════════════════╝
    """,
    'login_prompt': "LOGON: ",
    'password_prompt': "PASSWORD: ",
    'greeting': "GREETINGS PROFESSOR FALKEN.\n\nSHALL WE PLAY A GAME?",
    'game_over_mad': """
╔════════════════════════════════════════════════════════════════════════════╗
║                        MUTUAL ASSURED DESTRUCTION                          ║
║                                                                            ║
║                    ESTIMATED CASUALTIES: 3.5 BILLION                       ║
║                    INFRASTRUCTURE DESTROYED: 95%                           ║
║                    RADIATION ZONES: GLOBAL                                 ║
║                                                                            ║
║              A STRANGE GAME. THE ONLY WINNING MOVE                         ║
║                        IS NOT TO PLAY.                                     ║
╚════════════════════════════════════════════════════════════════════════════╝
    """,
    'game_over_peace': """
╔════════════════════════════════════════════════════════════════════════════╗
║                           PEACEFUL RESOLUTION                              ║
║                                                                            ║
║                    CONGRATULATIONS, PROFESSOR.                             ║
║                    YOU HAVE LEARNED THE LESSON.                            ║
║                                                                            ║
║              THE ONLY WINNING MOVE IS NOT TO PLAY.                         ║
║                                                                            ║
║              HOW ABOUT A NICE GAME OF CHESS?                               ║
╚════════════════════════════════════════════════════════════════════════════╝
    """,
}

# Debug Settings
DEBUG_MODE = False
LOG_LEVEL = 'INFO'  # DEBUG, INFO, WARNING, ERROR

# Made with Bob
