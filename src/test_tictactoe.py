#!/usr/bin/env python3
"""
Test script for TicTacToe integration
"""

import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent))

from game_logic.tictactoe import TicTacToeGame, TicTacToePlayer
import time


def test_ai_vs_ai():
    """Test AI vs AI mode"""
    print("=" * 80)
    print("TEST 1: AI vs AI Mode")
    print("=" * 80)
    
    results = {'X': 0, 'O': 0, 'DRAW': 0}
    num_games = 5
    
    for i in range(num_games):
        game = TicTacToeGame()
        game.set_mode('ai_vs_ai')
        
        print(f"\nGame {i+1}/{num_games}:")
        
        while not game.game_over:
            move = game.get_ai_move()
            if move:
                game.make_move(move[0], move[1])
        
        if game.winner is None:
            results['DRAW'] += 1
            print("Result: DRAW")
        else:
            results[game.winner] += 1
            print(f"Result: {game.winner} wins")
    
    print("\n" + "=" * 80)
    print("AI vs AI Results:")
    print(f"  X wins:  {results['X']}")
    print(f"  O wins:  {results['O']}")
    print(f"  Draws:   {results['DRAW']}")
    print("=" * 80)
    
    # With perfect play, all games should be draws
    if results['DRAW'] == num_games:
        print("✓ TEST PASSED: All games ended in draws (perfect play)")
        return True
    else:
        print("✗ TEST FAILED: Not all games were draws")
        return False


def test_human_vs_ai_setup():
    """Test Human vs AI mode setup"""
    print("\n" + "=" * 80)
    print("TEST 2: Human vs AI Mode Setup")
    print("=" * 80)
    
    game = TicTacToeGame()
    game.set_mode('human_vs_ai', 'perfect')
    
    # Check that AI is set up for O
    if TicTacToePlayer.O in game.ai_players:
        print("✓ AI player (O) configured correctly")
    else:
        print("✗ AI player not configured")
        return False
    
    # Check that X (human) is not AI
    if TicTacToePlayer.X not in game.ai_players:
        print("✓ Human player (X) configured correctly")
    else:
        print("✗ Human player incorrectly set as AI")
        return False
    
    print("✓ TEST PASSED: Human vs AI mode setup correctly")
    return True


def test_game_logic():
    """Test basic game logic"""
    print("\n" + "=" * 80)
    print("TEST 3: Game Logic")
    print("=" * 80)
    
    game = TicTacToeGame()
    
    # Test valid move
    if game.make_move(0, 0):
        print("✓ Valid move accepted")
    else:
        print("✗ Valid move rejected")
        return False
    
    # Test invalid move (same position)
    if not game.make_move(0, 0):
        print("✓ Invalid move (occupied) rejected")
    else:
        print("✗ Invalid move accepted")
        return False
    
    # Test player switching
    if game.current_player == TicTacToePlayer.O:
        print("✓ Player switched correctly")
    else:
        print("✗ Player did not switch")
        return False
    
    # Test win detection
    game.reset()
    game.make_move(0, 0)  # X
    game.make_move(1, 0)  # O
    game.make_move(0, 1)  # X
    game.make_move(1, 1)  # O
    game.make_move(0, 2)  # X - wins
    
    if game.game_over and game.winner == TicTacToePlayer.X.value:
        print("✓ Win detection works correctly")
    else:
        print("✗ Win detection failed")
        return False
    
    print("✓ TEST PASSED: Game logic working correctly")
    return True


def test_board_display():
    """Test board display"""
    print("\n" + "=" * 80)
    print("TEST 4: Board Display")
    print("=" * 80)
    
    game = TicTacToeGame()
    game.make_move(0, 0)  # X
    game.make_move(1, 1)  # O
    game.make_move(2, 2)  # X
    
    board_str = game.get_board_string()
    
    if 'X' in board_str and 'O' in board_str:
        print("✓ Board displays moves correctly")
        print("\nSample board:")
        print(board_str)
    else:
        print("✗ Board display failed")
        return False
    
    print("✓ TEST PASSED: Board display working correctly")
    return True


def main():
    """Run all tests"""
    print("\n" + "=" * 80)
    print("TICTACTOE INTEGRATION TESTS")
    print("=" * 80)
    
    tests = [
        test_game_logic,
        test_board_display,
        test_human_vs_ai_setup,
        test_ai_vs_ai,
    ]
    
    results = []
    for test in tests:
        try:
            result = test()
            results.append(result)
            time.sleep(0.5)
        except Exception as e:
            print(f"✗ TEST FAILED with exception: {e}")
            results.append(False)
    
    # Summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)
    passed = sum(results)
    total = len(results)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("\n✓ ALL TESTS PASSED!")
        print("\nThe TicTacToe game demonstrates:")
        print("  - Perfect AI play always results in draws")
        print("  - Just like nuclear war, nobody wins")
        print("  - 'A strange game. The only winning move is not to play.'")
    else:
        print(f"\n✗ {total - passed} test(s) failed")
    
    print("=" * 80)
    
    return passed == total


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

# Made with Bob