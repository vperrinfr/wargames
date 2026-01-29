# Global Thermonuclear War - Gameplay Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Game Modes](#game-modes)
4. [Controls](#controls)
5. [Game Mechanics](#game-mechanics)
6. [Strategy Guide](#strategy-guide)
7. [Tips and Tricks](#tips-and-tricks)

## Introduction

Global Thermonuclear War is a strategic simulation game inspired by the 1983 film "WarGames". You play against WOPR (War Operation Plan Response), an artificial intelligence controlling the Soviet nuclear arsenal during the Cold War era.

The game demonstrates the concept of Mutual Assured Destruction (MAD) and explores the futility of nuclear warfare through strategic gameplay.

> *"A strange game. The only winning move is not to play."* - WOPR

## Getting Started

### Installation

1. Ensure Python 3.8+ is installed
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Game

```bash
python src/main.py
```

### First Launch

When you first launch the game, you'll see:
1. **WOPR Logo** - The iconic War Operation Plan Response system
2. **Login Sequence** - Authenticate as "JOSHUA"
3. **Main Menu** - Choose your game mode

## Game Modes

### 1. Campaign Mode
Play against WOPR AI with four difficulty levels:

- **Easy**: WOPR is learning, slower reactions, lower accuracy
- **Normal**: Standard Cold War scenario, balanced gameplay
- **Hard**: WOPR is experienced, faster reactions, higher accuracy
- **WOPR**: Maximum difficulty, near-perfect strategic decisions

### 2. Simulation Mode
Watch two AI opponents battle each other. This mode demonstrates:
- The escalation of nuclear conflict
- The concept of Mutual Assured Destruction
- Why "the only winning move is not to play"

### 3. Tutorial Mode
Learn the game mechanics step-by-step without AI opposition.

## Controls

### Main Menu
- **1-5**: Select menu option
- **Enter**: Confirm selection

### During Gameplay
- **L**: Launch missile at target
- **S**: Show detailed statistics
- **P**: Propose peace (end game peacefully)
- **Q**: Quit game (with confirmation)

### Target Selection
- **1-10**: Select target by number
- **Enter**: Confirm target

### Missile Selection
- **1**: ICBM (Intercontinental Ballistic Missile)
- **2**: SLBM (Submarine-Launched Ballistic Missile)
- **3**: CRUISE (Cruise Missile)

## Game Mechanics

### Targets

Each side has strategic targets with different characteristics:

#### Target Types

| Symbol | Type | Description | Strategic Value |
|--------|------|-------------|-----------------|
| ◉ | City | Population centers | 50 |
| ▣ | Military Base | Strategic installations | 100 |
| ◈ | Missile Silo | Offensive capability | 150 |
| ◆ | Command Center | Critical infrastructure | 200 |

#### Target Properties

- **Population**: Number of civilians at risk
- **Strategic Value**: Points awarded for destruction
- **Defense Level**: Chance to intercept incoming missiles
- **Damage Level**: Current damage (0-100%)

### Missiles

#### ICBM (Intercontinental Ballistic Missile)
- **Range**: 10,000 km
- **Speed**: 7.0 km/s
- **Warheads**: 10
- **Accuracy**: 90%
- **Cost**: 5 missiles from inventory
- **Best For**: High-value targets at long range

#### SLBM (Submarine-Launched Ballistic Missile)
- **Range**: 8,000 km
- **Speed**: 6.5 km/s
- **Warheads**: 8
- **Accuracy**: 85%
- **Cost**: 4 missiles from inventory
- **Best For**: Medium-range strategic targets

#### CRUISE (Cruise Missile)
- **Range**: 2,500 km
- **Speed**: 0.8 km/s
- **Warheads**: 1
- **Accuracy**: 95%
- **Cost**: 2 missiles from inventory
- **Best For**: Precision strikes on nearby targets

### Combat Resolution

When a missile reaches its target:

1. **Defense Check**: Target's defense systems attempt interception
2. **Accuracy Check**: Each warhead has a chance to hit based on accuracy
3. **Damage Calculation**: Successful hits deal 30% damage per warhead
4. **Casualties**: Population casualties based on damage level
5. **Destruction**: Target destroyed at 90%+ damage

### Turn Structure

1. **Player Phase**
   - View available targets
   - Select action (Launch, Statistics, Peace, Quit)
   - Choose target and missile type
   - Confirm launch

2. **AI Phase**
   - WOPR analyzes situation
   - Displays strategic message
   - Launches retaliatory strikes
   - Updates game state

3. **Resolution Phase**
   - Missiles travel to targets
   - Combat resolution
   - Statistics update
   - Win/loss condition check

### Win/Loss Conditions

#### Mutual Assured Destruction (MAD)
- Both sides suffer 80%+ destruction
- Most common outcome
- Demonstrates futility of nuclear war

#### Defeat
- All your strategic assets destroyed
- WOPR achieves strategic superiority

#### Victory
- All enemy targets destroyed
- Extremely rare and pyrrhic
- Massive casualties on both sides

#### Peace
- Both sides agree to stop fighting
- Best possible outcome
- Requires strategic restraint

## Strategy Guide

### Early Game (Turns 1-5)

**Priorities:**
1. Identify high-value targets (Command Centers, Missile Silos)
2. Conserve missiles - don't launch everything at once
3. Observe WOPR's targeting patterns
4. Consider defensive positioning

**Recommended Actions:**
- Launch 1-2 missiles per turn
- Target Command Centers first (disrupts AI coordination)
- Use ICBMs for maximum impact
- Save some missiles for later turns

### Mid Game (Turns 6-15)

**Priorities:**
1. Maintain missile reserves
2. Target remaining high-value assets
3. Adapt to WOPR's strategy
4. Consider escalation consequences

**Recommended Actions:**
- Balance offense and conservation
- Use SLBMs for cost-effective strikes
- Monitor casualty counts
- Evaluate peace options

### Late Game (Turns 16+)

**Priorities:**
1. Assess total destruction
2. Consider peace proposal
3. Minimize further casualties
4. Remember WOPR's lesson

**Recommended Actions:**
- Propose peace if destruction is high
- Use remaining missiles strategically
- Accept that MAD may be inevitable
- Learn from the experience

## Tips and Tricks

### Offensive Strategy

1. **Target Priority**
   - Command Centers > Missile Silos > Military Bases > Cities
   - Destroy offensive capability first
   - Cities are last resort (high casualties, lower strategic value)

2. **Missile Selection**
   - Use ICBMs for distant, high-value targets
   - Use Cruise missiles for precision strikes
   - Save SLBMs for mid-game flexibility

3. **Timing**
   - Don't exhaust missiles early
   - Space out attacks to observe results
   - Coordinate strikes on related targets

### Defensive Considerations

1. **Defense Systems**
   - High-value targets have better defenses
   - Multiple warheads increase hit probability
   - Some missiles will be intercepted

2. **Retaliation**
   - WOPR will respond to aggression
   - Escalation leads to MAD
   - Restraint may lead to peace

### Advanced Tactics

1. **Psychological Warfare**
   - WOPR adapts to your strategy
   - Unpredictable targeting confuses AI
   - Sudden peace proposals can work

2. **Resource Management**
   - Track missile inventory carefully
   - Don't waste missiles on destroyed targets
   - Save reserves for critical moments

3. **Victory Conditions**
   - True victory is avoiding the game
   - Peace is the best outcome
   - MAD teaches the lesson

### Common Mistakes

❌ **Launching all missiles immediately**
- Leaves you defenseless
- Triggers maximum retaliation
- Guarantees MAD

❌ **Ignoring high-value targets**
- Allows WOPR to maintain capability
- Reduces strategic advantage
- Prolongs conflict

❌ **Targeting only cities**
- High casualties, low strategic value
- Doesn't reduce enemy capability
- Morally questionable

❌ **Never proposing peace**
- Misses the game's message
- Ensures destructive outcome
- Ignores WOPR's wisdom

### Optimal Strategy

✅ **The WOPR Approach:**
1. Analyze the situation carefully
2. Target strategic assets, not populations
3. Maintain missile reserves
4. Recognize when to stop
5. Propose peace before MAD
6. Remember: "The only winning move is not to play"

## Difficulty Progression

### Easy Mode
- Learn game mechanics
- Practice targeting
- Understand AI behavior
- Low pressure environment

### Normal Mode
- Balanced challenge
- Standard Cold War scenario
- Requires strategic thinking
- Good for most players

### Hard Mode
- Fast AI reactions
- High accuracy attacks
- Aggressive retaliation
- Tests your skills

### WOPR Mode
- Maximum difficulty
- Near-perfect AI decisions
- Rapid escalation
- Ultimate challenge
- Demonstrates why nuclear war is unwinnable

## Scoring System

Points are awarded for:
- Target destruction (based on strategic value)
- Minimizing casualties
- Efficient missile use
- Achieving peace

**High Score Tips:**
- Target high-value assets
- Minimize civilian casualties
- Use missiles efficiently
- End game peacefully

## Educational Value

This game teaches:
1. **Mutual Assured Destruction (MAD)**: Why nuclear war has no winners
2. **Strategic Thinking**: Balancing offense, defense, and diplomacy
3. **Consequence Analysis**: Every action has reactions
4. **Historical Context**: Cold War nuclear strategy
5. **Ethical Considerations**: The human cost of warfare

## Final Thoughts

Remember WOPR's conclusion from WarGames:

> *"A strange game. The only winning move is not to play."*

The game is designed to demonstrate that nuclear warfare has no winners. The best outcome is always to find a peaceful resolution before mutual destruction becomes inevitable.

Play strategically, but remember the lesson: sometimes the wisest choice is restraint.

---

*"How about a nice game of chess?"* - WOPR