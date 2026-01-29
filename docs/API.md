# API Documentation

## Overview

This document provides detailed API documentation for the Global Thermonuclear War game components.

## Table of Contents

1. [Game Engine](#game-engine)
2. [Target System](#target-system)
3. [Missile System](#missile-system)
4. [AI System](#ai-system)
5. [UI Components](#ui-components)
6. [Utilities](#utilities)

---

## Game Engine

### `GameEngine`

Main game controller that manages game state and coordinates all subsystems.

#### Constructor

```python
GameEngine()
```

Creates a new game engine instance.

#### Properties

- `state: GameState` - Current game state (MENU, INTRO, PLAYING, PAUSED, GAME_OVER, PEACE)
- `mode: GameMode` - Current game mode (CAMPAIGN, SIMULATION, TUTORIAL)
- `running: bool` - Whether the game is running
- `player: Player` - Human player instance
- `ai_opponent: WOPRArtificialIntelligence` - AI opponent instance
- `target_manager: TargetManager` - Manages all targets
- `missile_manager: MissileManager` - Manages all missiles
- `turn_count: int` - Current turn number
- `game_result: str` - Final game result

#### Methods

##### `initialize_game(mode: GameMode, difficulty: str) -> None`

Initialize a new game with specified mode and difficulty.

**Parameters:**
- `mode` - Game mode (CAMPAIGN, SIMULATION, TUTORIAL)
- `difficulty` - Difficulty level ('easy', 'normal', 'hard', 'wopr')

**Example:**
```python
engine = GameEngine()
engine.initialize_game(GameMode.CAMPAIGN, 'normal')
```

##### `update(delta_time: float) -> None`

Update game state for one frame.

**Parameters:**
- `delta_time` - Time elapsed since last update (seconds)

##### `player_launch_missile(missile_type: str, target: Target) -> bool`

Launch a missile from the player.

**Parameters:**
- `missile_type` - Type of missile ('ICBM', 'SLBM', 'CRUISE')
- `target` - Target object to attack

**Returns:**
- `bool` - True if launch successful, False otherwise

**Example:**
```python
target = engine.target_manager.get_intact_targets('USSR')[0]
success = engine.player_launch_missile('ICBM', target)
```

##### `ai_take_turn() -> dict`

Execute AI opponent's turn.

**Returns:**
- `dict` - Turn result containing:
  - `action` - Action taken ('attack', 'defend', 'wait', 'peace')
  - `message` - WOPR message
  - `targets` - List of targeted objects (if attacking)
  - `launch_count` - Number of missiles launched

##### `get_game_statistics() -> dict`

Get comprehensive game statistics.

**Returns:**
- `dict` - Statistics including:
  - `turn_count` - Number of turns played
  - `total_casualties` - Total casualties on both sides
  - `total_missiles_launched` - Total missiles launched
  - `player_stats` - Player-specific statistics
  - `ai_stats` - AI-specific statistics

##### `quit_game() -> None`

Quit the current game.

---

## Target System

### `Target`

Represents a strategic target location.

#### Constructor

```python
Target(name: str, target_type: str, x: int, y: int, 
       population: int, strategic_value: int, defense_level: float)
```

**Parameters:**
- `name` - Target name
- `target_type` - Type ('CITY', 'MILITARY_BASE', 'MISSILE_SILO', 'COMMAND_CENTER')
- `x, y` - Map coordinates
- `population` - Civilian population
- `strategic_value` - Strategic point value
- `defense_level` - Defense capability (0.0-1.0)

#### Properties

- `name: str` - Target identifier
- `target_type: str` - Target type
- `x: int, y: int` - Coordinates
- `population: int` - Population count
- `strategic_value: int` - Point value
- `defense_level: float` - Defense capability
- `damage_level: float` - Current damage (0.0-1.0)
- `casualties: int` - Total casualties
- `destroyed: bool` - Whether target is destroyed

#### Methods

##### `take_damage(warheads: int, accuracy: float) -> dict`

Apply damage from incoming missile.

**Parameters:**
- `warheads` - Number of warheads
- `accuracy` - Hit probability (0.0-1.0)

**Returns:**
- `dict` - Damage result containing:
  - `intercepted` - Number of warheads intercepted
  - `hits` - Number of successful hits
  - `damage` - Total damage dealt
  - `casualties` - Casualties inflicted
  - `destroyed` - Whether target was destroyed

##### `get_status() -> str`

Get current target status string.

**Returns:**
- `str` - Status description

##### `get_symbol() -> str`

Get map display symbol for target type.

**Returns:**
- `str` - Symbol character (◉, ▣, ◈, ◆)

##### `distance_to(other: Target) -> float`

Calculate distance to another target.

**Parameters:**
- `other` - Target to measure distance to

**Returns:**
- `float` - Distance in kilometers

### `TargetManager`

Manages all targets in the game.

#### Constructor

```python
TargetManager()
```

#### Methods

##### `add_target(country: str, target: Target) -> None`

Add a target to the manager.

**Parameters:**
- `country` - Country code ('USA', 'USSR')
- `target` - Target object to add

##### `get_targets_by_country(country: str) -> List[Target]`

Get all targets for a country.

**Parameters:**
- `country` - Country code

**Returns:**
- `List[Target]` - List of targets

##### `get_intact_targets(country: str) -> List[Target]`

Get non-destroyed targets for a country.

**Parameters:**
- `country` - Country code

**Returns:**
- `List[Target]` - List of intact targets

##### `get_high_value_targets(country: str, min_value: int) -> List[Target]`

Get high-value targets above threshold.

**Parameters:**
- `country` - Country code
- `min_value` - Minimum strategic value

**Returns:**
- `List[Target]` - List of high-value targets

##### `get_total_casualties(country: str) -> int`

Get total casualties for a country.

**Parameters:**
- `country` - Country code

**Returns:**
- `int` - Total casualties

##### `get_destruction_percentage(country: str) -> float`

Get percentage of targets destroyed.

**Parameters:**
- `country` - Country code

**Returns:**
- `float` - Destruction percentage (0.0-1.0)

---

## Missile System

### `MissileType`

Configuration dataclass for missile types.

#### Properties

- `name: str` - Display name
- `range: int` - Maximum range (km)
- `speed: float` - Flight speed (km/s)
- `warheads: int` - Number of warheads
- `accuracy: float` - Hit probability (0.0-1.0)
- `cost: int` - Resource cost

### `Missile`

Represents a missile in flight.

#### Constructor

```python
Missile(missile_type: MissileType, origin: Tuple[int, int], 
        target: Tuple[int, int], owner: str)
```

**Parameters:**
- `missile_type` - MissileType configuration
- `origin` - Launch coordinates (x, y)
- `target` - Target coordinates (x, y)
- `owner` - Owner name

#### Properties

- `missile_type: MissileType` - Type configuration
- `origin: Tuple[int, int]` - Launch position
- `target: Tuple[int, int]` - Target position
- `owner: str` - Owner identifier
- `current_pos: Tuple[float, float]` - Current position
- `trajectory: List[Tuple[float, float]]` - Flight path
- `launched: bool` - Whether launched
- `detonated: bool` - Whether detonated
- `intercepted: bool` - Whether intercepted

#### Methods

##### `launch() -> None`

Launch the missile.

##### `update(delta_time: float) -> None`

Update missile position.

**Parameters:**
- `delta_time` - Time elapsed (seconds)

##### `detonate() -> None`

Detonate the missile at target.

##### `intercept() -> None`

Intercept the missile.

##### `get_position() -> Tuple[float, float]`

Get current position.

**Returns:**
- `Tuple[float, float]` - Current (x, y) coordinates

##### `get_progress() -> float`

Get flight progress.

**Returns:**
- `float` - Progress (0.0-1.0)

### `MissileManager`

Manages all missiles in the game.

#### Constructor

```python
MissileManager()
```

#### Methods

##### `create_missile(missile_type: str, origin: Tuple[int, int], target: Tuple[int, int], owner: str) -> Missile`

Create a new missile.

**Parameters:**
- `missile_type` - Type name ('ICBM', 'SLBM', 'CRUISE')
- `origin` - Launch coordinates
- `target` - Target coordinates
- `owner` - Owner name

**Returns:**
- `Missile` - Created missile object

##### `launch_missile(missile: Missile) -> None`

Launch a missile.

**Parameters:**
- `missile` - Missile to launch

##### `update_missiles(delta_time: float) -> None`

Update all active missiles.

**Parameters:**
- `delta_time` - Time elapsed (seconds)

##### `get_active_missiles() -> List[Missile]`

Get all active (in-flight) missiles.

**Returns:**
- `List[Missile]` - List of active missiles

---

## AI System

### `WOPRArtificialIntelligence`

Strategic AI opponent.

#### Constructor

```python
WOPRArtificialIntelligence(name: str, difficulty: str)
```

**Parameters:**
- `name` - AI name
- `difficulty` - Difficulty level ('easy', 'normal', 'hard', 'wopr')

#### Properties

- `name: str` - AI identifier
- `difficulty: str` - Difficulty level
- `missiles_remaining: int` - Available missiles
- `aggression_level: float` - Current aggression (0.0-1.0)
- `learning_enabled: bool` - Whether AI learns
- `targets_hit: List[str]` - Successful hits
- `targets_missed: List[str]` - Missed targets

#### Methods

##### `analyze_situation(target_manager: TargetManager, missile_manager: MissileManager, player_stats: dict) -> dict`

Analyze current game situation.

**Parameters:**
- `target_manager` - Target manager instance
- `missile_manager` - Missile manager instance
- `player_stats` - Player statistics

**Returns:**
- `dict` - Situation analysis containing:
  - `threat_level` - Threat assessment (0.0-1.0)
  - `advantage` - Strategic advantage (-1.0 to 1.0)
  - `player_aggression` - Player aggression level
  - `recommended_action` - Suggested action

##### `select_targets(target_manager: TargetManager, num_targets: int) -> List[Target]`

Select targets for attack.

**Parameters:**
- `target_manager` - Target manager instance
- `num_targets` - Number of targets to select

**Returns:**
- `List[Target]` - Selected targets

##### `decide_action(situation: dict) -> str`

Decide what action to take.

**Parameters:**
- `situation` - Situation analysis from `analyze_situation()`

**Returns:**
- `str` - Action ('attack', 'defend', 'wait', 'peace')

##### `adjust_strategy(situation: dict) -> None`

Adjust AI strategy based on situation.

**Parameters:**
- `situation` - Current situation analysis

---

## UI Components

### ASCII Art Functions

#### `create_box(title: str, content: str, width: int) -> str`

Create a bordered text box.

**Parameters:**
- `title` - Box title
- `content` - Box content
- `width` - Box width in characters

**Returns:**
- `str` - Formatted box string

#### `create_menu(title: str, items: List[str], selected: int) -> str`

Create a menu display.

**Parameters:**
- `title` - Menu title
- `items` - Menu items
- `selected` - Selected item index

**Returns:**
- `str` - Formatted menu string

#### `create_stats_display(stats: dict) -> str`

Create statistics display.

**Parameters:**
- `stats` - Statistics dictionary

**Returns:**
- `str` - Formatted statistics string

### Animation Classes

#### `Animation` (Base Class)

Base class for all animations.

##### Methods

- `update(delta_time: float) -> Any` - Update animation state
- `is_finished() -> bool` - Check if animation is complete
- `reset() -> None` - Reset animation to start

#### `MissileAnimation`

Missile flight animation.

#### `ExplosionAnimation`

Explosion effect animation.

#### `TypingAnimation`

Character-by-character text reveal.

#### `LoadingBarAnimation`

Progress bar animation.

---

## Utilities

### Configuration (`src/utils/config.py`)

#### Constants

- `MISSILE_TYPES` - Dictionary of missile type configurations
- `TARGET_TYPES` - Dictionary of target type configurations
- `WORLD_TARGETS` - Predefined target locations
- `MESSAGES` - Game messages and quotes
- `WOPR_QUOTES` - WOPR AI quotes

#### Functions

##### `get_missile_type(name: str) -> MissileType`

Get missile type configuration.

**Parameters:**
- `name` - Missile type name

**Returns:**
- `MissileType` - Missile configuration

##### `get_target_type(name: str) -> dict`

Get target type configuration.

**Parameters:**
- `name` - Target type name

**Returns:**
- `dict` - Target configuration

---

## Error Handling

All API methods may raise the following exceptions:

- `ValueError` - Invalid parameter values
- `KeyError` - Invalid configuration keys
- `RuntimeError` - Game state errors

Example error handling:

```python
try:
    engine.player_launch_missile('INVALID', target)
except ValueError as e:
    print(f"Invalid missile type: {e}")
except RuntimeError as e:
    print(f"Cannot launch: {e}")
```

---

## Usage Examples

### Basic Game Setup

```python
from src.game_engine import GameEngine, GameMode

# Create engine
engine = GameEngine()

# Initialize game
engine.initialize_game(GameMode.CAMPAIGN, 'normal')

# Game loop
while engine.running:
    engine.update(0.016)  # ~60 FPS
```

### Launching Missiles

```python
# Get available targets
targets = engine.target_manager.get_intact_targets('USSR')

# Select target
target = targets[0]

# Launch missile
if engine.player_launch_missile('ICBM', target):
    print(f"Missile launched at {target.name}")
```

### AI Turn

```python
# Execute AI turn
result = engine.ai_take_turn()

print(f"WOPR: {result['message']}")
print(f"Action: {result['action']}")

if result['action'] == 'attack':
    print(f"Targets: {[t.name for t in result['targets']]}")
```

### Statistics

```python
# Get game statistics
stats = engine.get_game_statistics()

print(f"Turn: {stats['turn_count']}")
print(f"Casualties: {stats['total_casualties']:,}")
print(f"Player Score: {stats['player_stats']['score']}")
```

---

## Version History

- **v1.0.0** - Initial release
  - Core game engine
  - Target and missile systems
  - WOPR AI
  - Terminal UI

---

*"A strange game. The only winning move is not to play."* - WOPR