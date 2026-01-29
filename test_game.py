#!/usr/bin/env python3
"""Quick test to verify game components work"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

print("Testing game components...")

try:
    # Test imports
    print("1. Testing imports...")
    from src.utils.config import WORLD_TARGETS, MISSILE_TYPES
    from src.game_logic.target import create_targets_from_config
    from src.game_logic.missile import create_missile_types_from_config
    from src.ai.wopr_ai import WOPRArtificialIntelligence
    from src.game_engine import GameEngine, GameMode
    print("   ✓ All imports successful")
    
    # Test target creation
    print("2. Testing target creation...")
    target_manager = create_targets_from_config(WORLD_TARGETS)
    print(f"   ✓ Created {len(target_manager.all_targets)} targets")
    
    # Test missile types
    print("3. Testing missile types...")
    missile_types = create_missile_types_from_config(MISSILE_TYPES)
    print(f"   ✓ Created {len(missile_types)} missile types")
    
    # Test AI creation
    print("4. Testing AI creation...")
    ai = WOPRArtificialIntelligence('normal')
    print(f"   ✓ WOPR AI created with difficulty: {ai.difficulty}")
    
    # Test game engine
    print("5. Testing game engine...")
    engine = GameEngine()
    engine.initialize_game(GameMode.CAMPAIGN, 'easy')
    print(f"   ✓ Game engine initialized")
    print(f"   ✓ Player has {engine.player.missiles_remaining} missiles")
    print(f"   ✓ AI has {engine.ai_opponent.missiles_remaining} missiles")
    
    # Test player stats
    print("6. Testing player stats...")
    stats = engine.player.get_stats()
    print(f"   ✓ Player stats: {stats}")
    
    # Test AI analysis
    print("7. Testing AI situation analysis...")
    situation = engine.ai_opponent.analyze_situation(
        engine.target_manager,
        engine.missile_manager,
        stats
    )
    print(f"   ✓ AI analyzed situation: threat={situation['threat_level']:.2f}")
    
    print("\n✅ All tests passed! Game is ready to play.")
    print("\nRun the game with: python3 src/main.py")
    
except Exception as e:
    print(f"\n❌ Test failed with error:")
    print(f"   {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Made with Bob
