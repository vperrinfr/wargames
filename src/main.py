#!/usr/bin/env python3
"""
Global Thermal Nuclear War
A text-based terminal game inspired by WarGames (1983)

"A strange game. The only winning move is not to play."
"""

import sys
import time
import os
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from colorama import init, Fore, Back, Style

# Initialize colorama for cross-platform colored terminal output
init(autoreset=True)

from src.game_engine import GameEngine, GameMode, GameState
from src.ui.ascii_art import (
    TITLE_SCREEN, WOPR_LOGO, create_menu, create_box,
    create_alert, create_stats_display
)
from src.ui.animations import TypingAnimation, LoadingBarAnimation, BlinkingText
from src.utils.config import MESSAGES, WOPR_QUOTES
from src.ui.tictactoe_ui import run_tictactoe_game


def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_slow(text: str, delay: float = 0.03):
    """Print text with typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def print_green(text: str):
    """Print text in green (phosphor terminal style)"""
    print(Fore.GREEN + text + Style.RESET_ALL)


def print_red(text: str):
    """Print text in red (alert style)"""
    print(Fore.RED + text + Style.RESET_ALL)


def print_yellow(text: str):
    """Print text in yellow (warning style)"""
    print(Fore.YELLOW + text + Style.RESET_ALL)


def show_intro_sequence():
    """Show WarGames-style intro sequence"""
    clear_screen()
    
    # Show WOPR logo
    print_green(WOPR_LOGO)
    time.sleep(1)
    
    # Show welcome message
    print_green(MESSAGES['welcome'])
    time.sleep(1)
    
    # Login sequence
    print_green("\n" + MESSAGES['login_prompt'])
    print_slow("JOSHUA", 0.1)
    time.sleep(0.5)
    
    # Loading
    print_green("\nAUTHENTICATING...")
    loading = LoadingBarAnimation(40, 1.5)
    for i in range(30):
        bar = loading.update(0.05)
        print(f"\r{Fore.GREEN}{bar}{Style.RESET_ALL}", end='', flush=True)
        time.sleep(0.05)
    
    print("\n")
    time.sleep(0.5)
    
    # Greeting
    print_green("\n" + MESSAGES['greeting'])
    time.sleep(2)
    
    # Show game list (from WarGames movie)
    clear_screen()
    print_green("╔════════════════════════════════════════════════════════════════════════════╗")
    print_green("║                         AVAILABLE GAMES                                    ║")
    print_green("╚════════════════════════════════════════════════════════════════════════════╝")
    print_green("\n")
    
    games = [
        "FALKEN'S MAZE",
        "BLACK JACK",
        "GIN RUMMY",
        "HEARTS",
        "BRIDGE",
        "CHECKERS",
        "CHESS",
        "POKER",
        "FIGHTER COMBAT",
        "GUERRILLA ENGAGEMENT",
        "DESERT WARFARE",
        "AIR-TO-GROUND ACTIONS",
        "THEATERWIDE TACTICAL WARFARE",
        "THEATERWIDE BIOTOXIC AND CHEMICAL WARFARE",
        "",
        "GLOBAL THERMONUCLEAR WAR",
    ]
    
    for i, game in enumerate(games, 1):
        if game:
            print_green(f"  {game}")
        else:
            print_green("")
        time.sleep(0.1)
    
    print_green("\n")
    game_choice = input(Fore.GREEN + "WHICH GAME? " + Style.RESET_ALL).upper()
    
    # Check for TicTacToe (easter egg from WarGames movie)
    if "TIC" in game_choice or "TAC" in game_choice or "TOE" in game_choice:
        print_green("\nLOADING TIC-TAC-TOE...")
        time.sleep(1)
        run_tictactoe_game()
        # After TicTacToe, continue to main menu
        return
    elif "GLOBAL" in game_choice or "THERMONUCLEAR" in game_choice or "WAR" in game_choice:
        print_green("\nLOADING GLOBAL THERMONUCLEAR WAR...")
        time.sleep(1)
    else:
        print_yellow(f"\n'{game_choice}' IS NOT AVAILABLE.")
        time.sleep(1)
        print_green("\nDEFAULTING TO GLOBAL THERMONUCLEAR WAR...")
        time.sleep(1)


def show_main_menu() -> str:
    """Show main menu and get user choice"""
    clear_screen()
    print_green(TITLE_SCREEN)
    
    menu_items = [
        "1. Campaign Mode - Play against WOPR",
        "2. Simulation Mode - Watch AI vs AI",
        "3. Tutorial - Learn the game",
        "4. About",
        "5. Exit"
    ]
    
    print_green("\n" + "=" * 60)
    for item in menu_items:
        print_green(item)
    print_green("=" * 60)
    
    choice = input(Fore.GREEN + "\nSelect option: " + Style.RESET_ALL)
    return choice


def show_difficulty_menu() -> str:
    """Show difficulty selection menu"""
    clear_screen()
    print_green("╔════════════════════════════════════════╗")
    print_green("║        SELECT DIFFICULTY LEVEL         ║")
    print_green("╠════════════════════════════════════════╣")
    print_green("║  1. Easy    - WOPR is learning         ║")
    print_green("║  2. Normal  - Standard Cold War        ║")
    print_green("║  3. Hard    - WOPR is experienced      ║")
    print_green("║  4. WOPR    - Maximum difficulty       ║")
    print_green("╚════════════════════════════════════════╝")
    
    choice = input(Fore.GREEN + "\nSelect difficulty: " + Style.RESET_ALL)
    
    difficulty_map = {
        '1': 'easy',
        '2': 'normal',
        '3': 'hard',
        '4': 'wopr'
    }
    
    return difficulty_map.get(choice, 'normal')


def show_about():
    """Show about information"""
    clear_screen()
    print_green("╔════════════════════════════════════════════════════════════════════════════╗")
    print_green("║                    GLOBAL THERMONUCLEAR WAR                                ║")
    print_green("╠════════════════════════════════════════════════════════════════════════════╣")
    print_green("║                                                                            ║")
    print_green("║  A text-based strategy game inspired by the 1983 film 'WarGames'          ║")
    print_green("║                                                                            ║")
    print_green("║  In this game, you play against WOPR (War Operation Plan Response),       ║")
    print_green("║  an artificial intelligence that controls the Soviet nuclear arsenal.     ║")
    print_green("║                                                                            ║")
    print_green("║  The game demonstrates the concept of Mutual Assured Destruction (MAD)    ║")
    print_green("║  and the futility of nuclear warfare.                                     ║")
    print_green("║                                                                            ║")
    print_green("║  As WOPR concludes in the film:                                           ║")
    print_green("║  'A strange game. The only winning move is not to play.'                  ║")
    print_green("║                                                                            ║")
    print_green("║  This game is for educational purposes only.                              ║")
    print_green("║                                                                            ║")
    print_green("╚════════════════════════════════════════════════════════════════════════════╝")
    
    input(Fore.GREEN + "\nPress Enter to continue..." + Style.RESET_ALL)


def show_tutorial():
    """Show tutorial"""
    clear_screen()
    print_green("╔════════════════════════════════════════════════════════════════════════════╗")
    print_green("║                              TUTORIAL                                      ║")
    print_green("╠════════════════════════════════════════════════════════════════════════════╣")
    print_green("║                                                                            ║")
    print_green("║  OBJECTIVE:                                                                ║")
    print_green("║  Protect your strategic assets while neutralizing enemy targets.          ║")
    print_green("║                                                                            ║")
    print_green("║  GAMEPLAY:                                                                 ║")
    print_green("║  - Each turn, you can launch missiles at enemy targets                    ║")
    print_green("║  - Different missile types have different ranges and capabilities         ║")
    print_green("║  - Targets have defense systems that may intercept your missiles          ║")
    print_green("║  - WOPR will retaliate against your attacks                               ║")
    print_green("║                                                                            ║")
    print_green("║  TARGET TYPES:                                                             ║")
    print_green("║  ◉ Cities - High population, moderate strategic value                     ║")
    print_green("║  ▣ Military Bases - Strategic importance                                  ║")
    print_green("║  ◈ Missile Silos - Offensive capability                                   ║")
    print_green("║  ◆ Command Centers - Critical infrastructure                              ║")
    print_green("║                                                                            ║")
    print_green("║  MISSILE TYPES:                                                            ║")
    print_green("║  ICBM - Long range, multiple warheads, high accuracy                      ║")
    print_green("║  SLBM - Medium range, submarine-launched                                  ║")
    print_green("║  CRUISE - Short range, very high accuracy                                 ║")
    print_green("║                                                                            ║")
    print_green("║  REMEMBER:                                                                 ║")
    print_green("║  The only winning move is not to play.                                    ║")
    print_green("║                                                                            ║")
    print_green("╚════════════════════════════════════════════════════════════════════════════╝")
    
    input(Fore.GREEN + "\nPress Enter to continue..." + Style.RESET_ALL)


def play_game(engine: GameEngine, mode: GameMode, difficulty: str):
    """Main game loop"""
    clear_screen()
    
    # Initialize game
    engine.initialize_game(mode, difficulty)
    
    print_green("╔════════════════════════════════════════════════════════════════════════════╗")
    print_green("║                         GAME INITIALIZED                                   ║")
    print_green("╚════════════════════════════════════════════════════════════════════════════╝")
    time.sleep(1)
    
    # Show initial status
    print_green(f"\nMode: {mode.value.upper()}")
    print_green(f"Difficulty: {difficulty.upper()}")
    print_green(f"Your missiles: {engine.player.missiles_remaining}")
    print_green(f"Your defenses: {engine.player.defenses_remaining}")
    time.sleep(2)
    
    # Game loop
    turn = 0
    while engine.running and engine.state == GameState.PLAYING:
        turn += 1
        clear_screen()
        
        print_green("╔════════════════════════════════════════════════════════════════════════════╗")
        print_green(f"║                            TURN {turn:3d}                                      ║")
        print_green("╚════════════════════════════════════════════════════════════════════════════╝")
        
        # Show status
        print_green(f"\nYour missiles remaining: {engine.player.missiles_remaining}")
        print_green(f"Enemy missiles remaining: {engine.ai_opponent.missiles_remaining if engine.ai_opponent else 0}")
        print_green(f"Your targets destroyed: {len(engine.player.targets_destroyed)}")
        
        # Show simple map
        print_green("\n" + "=" * 80)
        print_green("TACTICAL MAP:")
        print_green("=" * 80)
        
        usa_targets = engine.target_manager.get_targets_by_country('USA')
        ussr_targets = engine.target_manager.get_targets_by_country('USSR')
        
        print_green(f"\nUSA Assets: {len([t for t in usa_targets if not t.destroyed])}/{len(usa_targets)} intact")
        for target in usa_targets[:5]:
            status = "✕ DESTROYED" if target.destroyed else f"✓ {target.get_status()}"
            print_green(f"  {target.get_symbol()} {target.name:20s} {status}")
        
        print_green(f"\nUSSR Assets: {len([t for t in ussr_targets if not t.destroyed])}/{len(ussr_targets)} intact")
        for target in ussr_targets[:5]:
            status = "✕ DESTROYED" if target.destroyed else f"✓ {target.get_status()}"
            print_green(f"  {target.get_symbol()} {target.name:20s} {status}")
        
        print_green("\n" + "=" * 80)
        
        # Show available targets for attack
        targets = engine.target_manager.get_intact_targets('USSR')
        if targets:
            print_green("\nAvailable enemy targets:")
            for i, target in enumerate(targets[:10], 1):  # Show first 10
                print_green(f"  {i}. {target.name} ({target.target_type}) - Value: {target.strategic_value}")
        
        # Player action
        print_green("\nOptions:")
        print_green("  L - Launch missile")
        print_green("  S - Show statistics")
        print_green("  P - Propose peace")
        print_green("  Q - Quit")
        
        action = input(Fore.GREEN + "\nYour action: " + Style.RESET_ALL).upper()
        
        if action == 'L':
            # Launch missile
            if engine.player.missiles_remaining > 0 and targets:
                try:
                    target_num = int(input(Fore.GREEN + "Select target number: " + Style.RESET_ALL))
                    if 1 <= target_num <= len(targets):
                        target = targets[target_num - 1]
                        
                        # Select missile type
                        print_green("\nMissile types:")
                        print_green("  1. ICBM")
                        print_green("  2. SLBM")
                        print_green("  3. CRUISE")
                        
                        missile_choice = input(Fore.GREEN + "Select missile type: " + Style.RESET_ALL)
                        missile_types = {'1': 'ICBM', '2': 'SLBM', '3': 'CRUISE'}
                        missile_type = missile_types.get(missile_choice, 'ICBM')
                        
                        # Launch
                        if engine.player_launch_missile(missile_type, target):
                            print_green(f"\n✓ {missile_type} launched at {target.name}!")
                            
                            # Show trajectory map
                            print_yellow("\n" + "=" * 80)
                            print_yellow("MISSILE TRAJECTORY:")
                            print_yellow("=" * 80)
                            
                            # Get launch and target locations
                            usa_targets = engine.target_manager.get_targets_by_country('USA')
                            origin = usa_targets[0] if usa_targets else None
                            
                            if origin:
                                print_green(f"\nLaunch: {origin.name} ({origin.x}, {origin.y})")
                                print_red(f"Target: {target.name} ({target.x}, {target.y})")
                                
                                # Simple trajectory visualization
                                print_yellow("\nFlight path:")
                                steps = 5
                                for i in range(steps + 1):
                                    progress = i / steps
                                    x = int(origin.x + (target.x - origin.x) * progress)
                                    y = int(origin.y + (target.y - origin.y) * progress)
                                    
                                    # Create simple visual
                                    bar = "=" * int(progress * 40)
                                    missile_pos = ">" if i < steps else "*"
                                    print(f"  [{bar}{missile_pos}{' ' * (40 - len(bar))}] {int(progress * 100)}%")
                                    time.sleep(0.2)
                            
                            print_yellow("=" * 80)
                            
                            # Process missile impact immediately
                            print_yellow("\nProcessing impact...")
                            
                            # Update missiles to detonate
                            for missile in engine.missile_manager.missiles:
                                if not missile.detonated and not missile.intercepted:
                                    missile.detonate()
                            
                            # Apply damage
                            engine._check_missile_impacts()
                            
                            # Show result
                            if target.destroyed:
                                print_red(f"\n✓ {target.name} DESTROYED!")
                                print_red(f"   Casualties: {target.casualties:,}")
                            elif target.damage_level > 0:
                                print_yellow(f"\n✓ {target.name} HIT!")
                                print_yellow(f"   Damage: {int(target.damage_level * 100)}%")
                                print_yellow(f"   Casualties: {target.casualties:,}")
                            else:
                                print_green(f"\n○ {target.name} - Missile intercepted or missed")
                            
                            time.sleep(2)
                        else:
                            print_red("\n✗ Launch failed!")
                            time.sleep(1)
                except ValueError:
                    print_red("\nInvalid input!")
                    time.sleep(1)
            else:
                print_red("\nNo missiles or targets available!")
                time.sleep(1)
                
        elif action == 'S':
            # Show statistics
            stats = engine.get_game_statistics()
            clear_screen()
            print_green(create_stats_display(stats['player_stats']))
            input(Fore.GREEN + "\nPress Enter to continue..." + Style.RESET_ALL)
            
        elif action == 'P':
            # Propose peace
            print_yellow("\nProposing peace to WOPR...")
            time.sleep(1)
            print_green("\nWOPR: " + WOPR_QUOTES[2])  # "A strange game..."
            time.sleep(2)
            engine.state = GameState.PEACE
            engine.game_result = 'PEACE'
            break
            
        elif action == 'Q':
            confirm = input(Fore.YELLOW + "\nAre you sure you want to quit? (y/n): " + Style.RESET_ALL)
            if confirm.lower() == 'y':
                engine.quit_game()
                return
        
        # AI turn
        if engine.ai_opponent and engine.state == GameState.PLAYING and action == 'L':
            print_green("\n" + "=" * 80)
            print_green("WOPR RESPONSE:")
            print_green("=" * 80)
            print_yellow("\nWOPR is analyzing threat...")
            time.sleep(1)
            
            result = engine.ai_take_turn()
            if result:
                print_green(f"\nWOPR: {result['message']}")
                
                if result['action'] == 'attack' and result.get('targets'):
                    launch_count = result.get('launch_count', 0)
                    print_red(f"\n⚠ WARNING: WOPR detected {launch_count} missile(s)!")
                    
                    # Show targets
                    for i, target in enumerate(result['targets'][:3], 1):
                        print_red(f"  Target {i}: {target.name}")
                        time.sleep(0.5)
                    
                    print_yellow("\nIncoming missiles detected...")
                    time.sleep(1)
                    
                    # Process AI missile impacts
                    print_yellow("Processing impacts...")
                    for missile in engine.missile_manager.missiles:
                        if missile.owner == engine.ai_opponent.name and not missile.detonated:
                            missile.detonate()
                    
                    engine._check_missile_impacts()
                    
                    # Show damage to USA targets
                    usa_targets = engine.target_manager.get_targets_by_country('USA')
                    damaged = [t for t in usa_targets if t.damage_level > 0 and t.damage_level < 1.0]
                    destroyed = [t for t in usa_targets if t.destroyed]
                    
                    if destroyed:
                        for target in destroyed[-launch_count:]:  # Show recently destroyed
                            print_red(f"  ✕ {target.name} DESTROYED!")
                    elif damaged:
                        for target in damaged[-launch_count:]:  # Show recently damaged
                            print_yellow(f"  ⚠ {target.name} damaged ({int(target.damage_level * 100)}%)")
                    
                    time.sleep(1)
                elif result['action'] == 'peace':
                    print_green("\n✓ WOPR proposes peace!")
                    time.sleep(1)
                elif result['action'] == 'wait':
                    print_yellow("\nWOPR is holding position...")
                    time.sleep(1)
                
                time.sleep(1)
        
        # Update game
        engine.update(0.1)
        engine.turn_count = turn
        
        # Check if game over
        if engine.state != GameState.PLAYING:
            break
    
    # Game over
    clear_screen()
    print_green(engine.get_game_result_message())
    
    # Show final statistics
    stats = engine.get_game_statistics()
    print_green(f"\n\nFinal Statistics:")
    print_green(f"Turns played: {stats['turn_count']}")
    print_green(f"Total casualties: {stats['total_casualties']:,}")
    print_green(f"Missiles launched: {stats['total_missiles_launched']}")
    print_green(f"Your score: {stats['player_stats']['score']}")
    
    input(Fore.GREEN + "\n\nPress Enter to return to menu..." + Style.RESET_ALL)


def main():
    """Main entry point"""
    # Show intro
    show_intro_sequence()
    
    # Create game engine
    engine = GameEngine()
    
    # Main menu loop
    while True:
        choice = show_main_menu()
        
        if choice == '1':
            # Campaign mode
            difficulty = show_difficulty_menu()
            play_game(engine, GameMode.CAMPAIGN, difficulty)
            
        elif choice == '2':
            # Simulation mode
            print_yellow("\nSimulation mode coming soon!")
            time.sleep(2)
            
        elif choice == '3':
            # Tutorial
            show_tutorial()
            
        elif choice == '4':
            # About
            show_about()
            
        elif choice == '5':
            # Exit
            clear_screen()
            print_green("\n" + WOPR_QUOTES[2])  # "A strange game..."
            print_green("\nThank you for playing.")
            time.sleep(2)
            break
        
        else:
            print_red("\nInvalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print_green("\n\nGame interrupted.")
        print_green("The only winning move is not to play.")
        sys.exit(0)
    except Exception as e:
        print_red(f"\n\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

# Made with Bob
