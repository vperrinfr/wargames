# Global Thermonuclear War - Technical Design Document

## Architecture Overview

This document describes the technical architecture and implementation details of the Global Thermonuclear War game.

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         Main Entry                          │
│                      (src/main.py)                          │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                      Game Engine                            │
│                  (src/game_engine.py)                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ Game State   │  │   Players    │  │  Statistics  │     │
│  │  Management  │  │  Management  │  │   Tracking   │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
└────────────┬────────────────┬────────────────┬─────────────┘
             │                │                │
    ┌────────▼────────┐  ┌───▼────────┐  ┌───▼──────────┐
    │  Game Logic     │  │     AI     │  │      UI      │
    │                 │  │            │  │              │
    │ ┌─────────────┐ │  │ ┌────────┐ │  │ ┌──────────┐ │
    │ │   Target    │ │  │ │ WOPR   │ │  │ │ Terminal │ │
    │ │  Manager    │ │  │ │   AI   │ │  │ │    UI    │ │
    │ └─────────────┘ │  │ └────────┘ │  │ └──────────┘ │
    │ ┌─────────────┐ │  │ ┌────────┐ │  │ ┌──────────┐ │
    │ │   Missile   │ │  │ │Strategy│ │  │ │ASCII Art │ │
    │ │  Manager    │ │  │ │        │ │  │ │          │ │
    │ └─────────────┘ │  │ └────────┘ │  │ └──────────┘ │
    │ ┌─────────────┐ │  │            │  │ ┌──────────┐ │
    │ │   Combat    │ │  │            │  │ │Animation │ │
    │ │  Resolution │ │  │            │  │ │          │ │
    │ └─────────────┘ │  │            │  │ └──────────┘ │
    └─────────────────┘  └────────────┘  └──────────────┘
             │                │                │
             └────────────────┴────────────────┘
                              │
                    ┌─────────▼──────────┐
                    │   Configuration    │
                    │  (src/utils/       │
                    │    config.py)      │
                    └────────────────────┘
```

## Core Components

### 1. Game Engine (`src/game_engine.py`)

**Purpose**: Central game controller managing game state, turn flow, and coordination between components.

**Key Classes**:

#### `GameEngine`
- Manages overall game state
- Coordinates between subsystems
- Handles game loop
- Processes win/loss conditions

**Responsibilities**:
- Initialize game components
- Update game state each frame
- Process player and AI actions
- Check victory/defeat conditions
- Manage game statistics

**Key Methods**:
```python
initialize_game(mode, difficulty)  # Set up new game
update(delta_time)                 # Update game state
player_launch_missile(type, target) # Handle player action
ai_take_turn()                     # Execute AI turn
check_game_over()                  # Evaluate end conditions
```

#### `GameState` (Enum)
- MENU: Main menu
- INTRO: Introduction sequence
- PLAYING: Active gameplay
- PAUSED: Game paused
- GAME_OVER: Game ended
- PEACE: Peaceful resolution

#### `GameMode` (Enum)
- CAMPAIGN: Player vs AI
- SIMULATION: AI vs AI
- TUTORIAL: Learning mode

#### `Player`
- Represents a player (human or AI)
- Tracks resources and statistics
- Records actions and results

### 2. Target System (`src/game_logic/target.py`)

**Purpose**: Manages all targets in the game world.

**Key Classes**:

#### `Target`
Represents a single target location.

**Properties**:
- `name`: Target identifier
- `target_type`: CITY, MILITARY_BASE, MISSILE_SILO, COMMAND_CENTER
- `x, y`: Map coordinates
- `population`: Civilian population
- `strategic_value`: Points value
- `defense_level`: Interception capability (0.0-1.0)
- `damage_level`: Current damage (0.0-1.0)
- `destroyed`: Boolean flag

**Methods**:
```python
take_damage(warheads, accuracy)  # Apply missile damage
get_status()                     # Return current status
get_symbol()                     # Get map display symbol
distance_to(other_target)        # Calculate distance
```

#### `TargetManager`
Manages all targets in the game.

**Responsibilities**:
- Store and organize targets by country
- Query targets by various criteria
- Calculate statistics
- Find nearest targets

**Methods**:
```python
add_target(country, target)
get_targets_by_country(country)
get_intact_targets(country)
get_high_value_targets(country, min_value)
get_total_casualties(country)
get_destruction_percentage(country)
```

### 3. Missile System (`src/game_logic/missile.py`)

**Purpose**: Handles missile creation, flight, and impact.

**Key Classes**:

#### `MissileType` (Dataclass)
Configuration for missile types.

**Properties**:
- `name`: Display name
- `range`: Maximum range (km)
- `speed`: Flight speed (km/s)
- `warheads`: Number of warheads
- `accuracy`: Hit probability (0.0-1.0)
- `cost`: Resource cost

#### `Missile`
Represents a missile in flight.

**Properties**:
- `missile_type`: MissileType configuration
- `origin`: Launch coordinates
- `target`: Target coordinates
- `owner`: Player name
- `current_pos`: Current position
- `trajectory`: List of trajectory points
- `launched`: Boolean flag
- `detonated`: Boolean flag
- `intercepted`: Boolean flag

**Methods**:
```python
launch()                    # Launch the missile
update(delta_time)          # Update position
detonate()                  # Detonate at target
intercept()                 # Intercept missile
get_position()              # Get current position
get_progress()              # Get flight progress (0-1)
```

**Trajectory Calculation**:
- Uses parabolic arc for realistic ballistic path
- Arc height = 20% of distance
- Interpolates between origin and target
- Generates multiple waypoints for smooth animation

#### `MissileManager`
Manages all missiles in the game.

**Responsibilities**:
- Create and track missiles
- Update missile positions
- Handle detonations and interceptions
- Provide missile queries

**Methods**:
```python
create_missile(type, origin, target, owner)
launch_missile(missile)
update_missiles(delta_time)
intercept_missile(missile)
get_active_missiles()
get_missiles_near_position(pos, radius)
```

### 4. AI System (`src/ai/wopr_ai.py`)

**Purpose**: Implements the WOPR artificial intelligence opponent.

**Key Classes**:

#### `WOPRArtificialIntelligence`
Strategic AI that adapts to player behavior.

**Properties**:
- `difficulty`: AI difficulty level
- `missiles_remaining`: Available missiles
- `aggression_level`: Current aggression (0.0-1.0)
- `learning_enabled`: Whether AI learns from results
- `targets_hit`: List of successful hits
- `targets_missed`: List of missed targets

**AI Decision Making**:

1. **Situation Analysis**
   ```python
   analyze_situation(target_manager, missile_manager, player_stats)
   ```
   - Evaluates threat level
   - Calculates strategic advantage
   - Assesses player aggression
   - Returns comprehensive situation report

2. **Target Selection**
   ```python
   select_targets(target_manager, num_targets)
   ```
   - Scores all available targets
   - Prioritizes by strategic value
   - Considers defense levels
   - Learns from past attempts
   - Returns sorted target list

3. **Action Decision**
   ```python
   decide_action(situation)
   ```
   - Returns: 'attack', 'defend', 'wait', or 'peace'
   - Based on threat level and advantage
   - Considers turn count and destruction
   - May propose peace if futility is evident

4. **Strategy Adjustment**
   ```python
   adjust_strategy(situation)
   ```
   - Increases aggression if losing
   - Decreases aggression if winning
   - Matches player aggression level
   - Adapts to game state

**Difficulty Levels**:

| Level | Reaction Time | Accuracy | Aggression |
|-------|--------------|----------|------------|
| Easy | 3.0s | 60% | 30% |
| Normal | 2.0s | 75% | 50% |
| Hard | 1.0s | 90% | 70% |
| WOPR | 0.5s | 95% | 90% |

**Learning System**:
- Records successful and failed attacks
- Adjusts target priorities based on results
- Avoids previously missed targets
- Adapts accuracy expectations

### 5. UI System (`src/ui/`)

**Purpose**: Handles all visual output and user interaction.

#### `ascii_art.py`
Contains ASCII art assets and rendering functions.

**Assets**:
- Title screen
- WOPR logo
- World map
- Target symbols
- Status indicators
- Explosion frames

**Functions**:
```python
create_box(title, content, width)
create_menu(title, items, selected)
create_loading_bar(progress, width)
create_alert(message, alert_type)
create_stats_display(stats)
```

#### `animations.py`
Implements various animations.

**Animation Classes**:

1. **Animation** (Base class)
   - Frame-based animation system
   - Time-based progression
   - Automatic completion detection

2. **MissileAnimation**
   - Missile launch and flight
   - Trajectory visualization
   - Position interpolation

3. **ExplosionAnimation**
   - Multi-frame explosion
   - Size variants (small, normal, large)
   - Fade-out effect

4. **TypingAnimation**
   - Character-by-character text reveal
   - Configurable speed
   - WarGames-style typing

5. **LoadingBarAnimation**
   - Progress bar with percentage
   - Smooth progression
   - Completion detection

6. **RadarAnimation**
   - Rotating radar sweep
   - Looping animation
   - 4-frame cycle

7. **BlinkingText**
   - Text that blinks on/off
   - Configurable blink rate
   - Attention-grabbing

8. **AnimationManager**
   - Manages multiple animations
   - Updates all animations
   - Removes finished animations

### 6. Configuration (`src/utils/config.py`)

**Purpose**: Centralized game configuration and constants.

**Configuration Categories**:

1. **Display Settings**
   - Terminal size requirements
   - Color scheme
   - Visual preferences

2. **Game Settings**
   - Game speed options
   - Starting resources
   - Difficulty configurations

3. **Missile Types**
   - ICBM, SLBM, CRUISE configurations
   - Range, speed, warheads, accuracy, cost

4. **Target Types**
   - CITY, MILITARY_BASE, MISSILE_SILO, COMMAND_CENTER
   - Population, strategic value, defense level

5. **World Targets**
   - Predefined target locations
   - Organized by country
   - Coordinates and types

6. **Animation Settings**
   - Frame definitions
   - Animation speeds
   - Visual effects

7. **Messages**
   - Welcome messages
   - Game over messages
   - WOPR quotes

## Data Flow

### Game Initialization
```
main.py
  └─> show_intro_sequence()
  └─> GameEngine.initialize_game(mode, difficulty)
      ├─> create_targets_from_config()
      ├─> create_missile_types_from_config()
      ├─> Create Player
      └─> Create WOPRArtificialIntelligence
```

### Player Turn
```
Player Input
  └─> main.py: play_game()
      └─> GameEngine.player_launch_missile(type, target)
          ├─> MissileManager.create_missile()
          ├─> MissileManager.launch_missile()
          └─> Player.launch_missile()
```

### AI Turn
```
GameEngine.ai_take_turn()
  └─> WOPR.take_turn()
      ├─> analyze_situation()
      ├─> adjust_strategy()
      ├─> decide_action()
      ├─> select_targets()
      └─> select_missile_type()
  └─> MissileManager.create_missile()
  └─> MissileManager.launch_missile()
```

### Game Update
```
GameEngine.update(delta_time)
  ├─> MissileManager.update_missiles(delta_time)
  │   └─> Missile.update(delta_time)
  │       └─> Update position along trajectory
  ├─> check_missile_impacts()
  │   └─> Target.take_damage(warheads, accuracy)
  │       ├─> Defense check
  │       ├─> Accuracy check
  │       ├─> Damage calculation
  │       └─> Casualty calculation
  ├─> update_statistics()
  └─> check_game_over()
      ├─> Check MAD condition
      ├─> Check defeat condition
      ├─> Check victory condition
      └─> Check peace condition
```

## Combat Resolution Algorithm

```python
def resolve_combat(missile, target):
    # 1. Defense Check
    if random() < target.defense_level:
        intercepted = random(1, missile.warheads)
        warheads -= intercepted
        if warheads <= 0:
            return INTERCEPTED
    
    # 2. Accuracy Check
    hits = 0
    for warhead in range(warheads):
        if random() < missile.accuracy:
            hits += 1
    
    if hits == 0:
        return MISS
    
    # 3. Damage Calculation
    damage_per_hit = 0.3
    total_damage = min(1.0, hits * damage_per_hit)
    target.damage_level += total_damage
    
    # 4. Casualty Calculation
    casualty_rate = total_damage * 0.8
    casualties = population * casualty_rate
    target.casualties += casualties
    
    # 5. Destruction Check
    if target.damage_level >= 0.9:
        target.destroyed = True
        return DESTROYED
    
    return HIT
```

## AI Decision Tree

```
Analyze Situation
  ├─> Calculate threat_level
  ├─> Calculate advantage
  └─> Assess player_aggression

Decide Action
  ├─> If turn > 10 AND total_destruction < 3
  │   └─> 30% chance: return PEACE
  ├─> If threat > 0.7 AND defenses > 0
  │   └─> return DEFEND
  ├─> If advantage > 0.3 AND missiles > 5
  │   └─> return ATTACK
  ├─> If incoming_missiles > 0 AND missiles > 0
  │   ├─> Increase aggression
  │   └─> return ATTACK
  ├─> If player_aggression > 0.5 AND missiles > 10
  │   └─> return ATTACK
  └─> Else
      └─> return WAIT or ATTACK
```

## Performance Considerations

### Optimization Strategies

1. **Missile Updates**
   - Only update active missiles
   - Remove finished missiles from active list
   - Use trajectory pre-calculation

2. **Target Queries**
   - Cache frequently accessed target lists
   - Use spatial indexing for nearest-target queries
   - Lazy evaluation of statistics

3. **Animation**
   - Frame-based rather than pixel-based
   - Remove finished animations
   - Batch terminal updates

4. **Memory Management**
   - Reuse animation objects
   - Clear finished missiles
   - Limit history tracking

### Scalability

The current architecture supports:
- Up to 100 targets per side
- Up to 50 simultaneous missiles
- 60 FPS update rate
- Minimal memory footprint

## Testing Strategy

### Unit Tests
- Target damage calculation
- Missile trajectory calculation
- AI decision making
- Combat resolution

### Integration Tests
- Game engine initialization
- Turn flow
- Win/loss conditions
- Statistics tracking

### Playtesting
- Balance testing across difficulties
- UI/UX feedback
- Performance testing
- Edge case discovery

## Future Enhancements

### Potential Features
1. Multiplayer support (2 human players)
2. Save/load game state
3. Replay system
4. Advanced graphics mode
5. Sound effects
6. More detailed world map
7. Economic simulation
8. Diplomatic options
9. Technology research
10. Historical scenarios

### Technical Improvements
1. Curses-based full-screen UI
2. Mouse support
3. Configuration file support
4. Mod support
5. Network play
6. Database for high scores
7. Telemetry and analytics
8. Automated testing suite

## Conclusion

The Global Thermonuclear War game demonstrates:
- Clean separation of concerns
- Modular architecture
- Extensible design
- Educational value
- Entertainment value

The architecture supports the game's core message: "The only winning move is not to play."

---

*"Shall we play a game?"* - WOPR