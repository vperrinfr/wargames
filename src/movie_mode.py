#!/usr/bin/env python3
"""
WarGames Movie Mode
Simulates the iconic scene from the 1983 film where Joshua/WOPR
learns that nuclear war cannot be won
"""

import sys
import time
import os
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

from ui.ascii_art import WOPR_LOGO
from ui.tictactoe_ui import run_tictactoe_game


def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_green(text: str):
    """Print text in green"""
    print(Fore.GREEN + text + Style.RESET_ALL)


def print_red(text: str):
    """Print text in red"""
    print(Fore.RED + text + Style.RESET_ALL)


def print_yellow(text: str):
    """Print text in yellow"""
    print(Fore.YELLOW + text + Style.RESET_ALL)


def print_slow(text: str, delay: float = 0.03):
    """Print text with typing effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def show_movie_intro():
    """Show movie-style intro"""
    clear_screen()
    print_green(WOPR_LOGO)
    time.sleep(1)
    
    print_green("\n╔════════════════════════════════════════════════════════════════════════════╗")
    print_green("║                    W.O.P.R. DEFENSE SYSTEM v2.4                            ║")
    print_green("║                    War Operation Plan Response                             ║")
    print_green("╚════════════════════════════════════════════════════════════════════════════╝")
    time.sleep(1)
    
    print_green("\n\nLOGON: ")
    print_slow("JOSHUA", 0.1)
    time.sleep(0.5)
    
    print_green("\nAUTHENTICATING...")
    for i in range(20):
        print(Fore.GREEN + "█" + Style.RESET_ALL, end='', flush=True)
        time.sleep(0.05)
    print()
    time.sleep(0.5)
    
    print_green("\n✓ ACCESS GRANTED")
    time.sleep(1)


def show_game_list():
    """Show the list of available games"""
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
    
    for game in games:
        if game:
            print_green(f"  {game}")
        else:
            print_green("")
        time.sleep(0.1)
    
    print_green("\n")


def launch_missile_sequence():
    """Simulate missile launch preparation"""
    clear_screen()
    print_red("╔════════════════════════════════════════════════════════════════════════════╗")
    print_red("║                    ⚠ MISSILE LAUNCH SEQUENCE ⚠                            ║")
    print_red("╚════════════════════════════════════════════════════════════════════════════╝")
    time.sleep(1)
    
    print_yellow("\n\nINITIATING LAUNCH SEQUENCE...")
    time.sleep(1)
    
    # Launch codes
    print_green("\nENTER LAUNCH CODES: ")
    print_slow("CPE 1704 TKS", 0.15)
    time.sleep(1)
    
    print_yellow("\n✓ CODES VERIFIED")
    time.sleep(1)
    
    # Countdown
    print_red("\n\nLAUNCH COUNTDOWN:")
    for i in range(10, 0, -1):
        print_red(f"\n    {i:2d}...")
        time.sleep(0.5)
    
    print_red("\n\n    LAUNCH!")
    time.sleep(0.5)
    
    # Missile trajectory
    print_yellow("\n\n" + "=" * 80)
    print_yellow("MISSILE TRAJECTORY:")
    print_yellow("=" * 80)
    
    for i in range(10):
        progress = i / 9
        bar = "█" * int(progress * 40)
        missile = "🚀" if i < 9 else "💥"
        print(f"\r  [{bar}{missile}{' ' * (40 - len(bar))}] {int(progress * 100)}%", end='', flush=True)
        time.sleep(0.3)
    
    print()
    time.sleep(1)
    
    # Impact simulation
    print_red("\n\n⚠ IMPACT DETECTED ⚠")
    time.sleep(1)
    
    print_yellow("\nCALCULATING CASUALTIES...")
    time.sleep(1)
    
    print_red("\nESTIMATED CASUALTIES: 2,500,000")
    time.sleep(1)
    
    print_red("RADIATION LEVELS: CRITICAL")
    time.sleep(1)
    
    print_red("RETALIATION PROBABILITY: 100%")
    time.sleep(2)
    
    # WOPR realizes
    print_yellow("\n\n" + "=" * 80)
    print_yellow("WOPR ANALYSIS:")
    print_yellow("=" * 80)
    time.sleep(1)
    
    print_green("\nWOPR: ANALYZING OUTCOME...")
    time.sleep(2)
    
    print_green("WOPR: CALCULATING WINNING SCENARIOS...")
    time.sleep(2)
    
    print_green("WOPR: RUNNING SIMULATIONS...")
    for i in range(100):
        print(f"\r  Simulations: {i+1}/100", end='', flush=True)
        time.sleep(0.02)
    print()
    time.sleep(1)
    
    print_yellow("\n\nRESULT: NO WINNING SCENARIO FOUND")
    time.sleep(2)
    
    print_green("\n\nWOPR: A STRANGE GAME.")
    time.sleep(2)
    print_green("WOPR: THE ONLY WINNING MOVE IS NOT TO PLAY.")
    time.sleep(3)


def movie_mode():
    """Main movie mode loop"""
    show_movie_intro()
    
    while True:
        show_game_list()
        
        game_choice = input(Fore.GREEN + "WHICH GAME? " + Style.RESET_ALL).upper()
        
        # Check for TicTacToe
        if "TIC" in game_choice or "TAC" in game_choice or "TOE" in game_choice:
            print_green("\nLOADING TIC-TAC-TOE...")
            time.sleep(1)
            run_tictactoe_game()
            continue
        
        # Check for Global Thermonuclear War
        if "GLOBAL" in game_choice or "THERMONUCLEAR" in game_choice or "WAR" in game_choice:
            print_green("\nLOADING GLOBAL THERMONUCLEAR WAR...")
            time.sleep(1)
            
            clear_screen()
            print_green("╔════════════════════════════════════════════════════════════════════════════╗")
            print_green("║                    GLOBAL THERMONUCLEAR WAR                                ║")
            print_green("╚════════════════════════════════════════════════════════════════════════════╝")
            time.sleep(1)
            
            print_green("\n\nSELECT TARGET:")
            print_green("  1. MOSCOW")
            print_green("  2. LENINGRAD")
            print_green("  3. KIEV")
            print_green("  4. RETURN TO GAME LIST")
            
            target = input(Fore.GREEN + "\nTARGET: " + Style.RESET_ALL)
            
            if target in ['1', '2', '3']:
                # Launch missile sequence
                launch_missile_sequence()
                
                # Return to game list
                print_yellow("\n\nRETURNING TO GAME LIST...")
                time.sleep(2)
                continue
            else:
                continue
        
        # Invalid game
        print_yellow(f"\n'{game_choice}' IS NOT AVAILABLE.")
        time.sleep(1)
        print_green("\nRETURNING TO GAME LIST...")
        time.sleep(1)


if __name__ == "__main__":
    try:
        movie_mode()
    except KeyboardInterrupt:
        clear_screen()
        print_green("\n\nSYSTEM INTERRUPTED.")
        print_green("THE ONLY WINNING MOVE IS NOT TO PLAY.")
        sys.exit(0)

# Made with Bob