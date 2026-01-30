"""
Global Thermal Nuclear War - TicTacToe UI
User interface for the hidden TicTacToe game
"""

import time
import os
import sys
from pathlib import Path

# Add parent directory to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from colorama import Fore, Style

from game_logic.tictactoe import TicTacToeGame, TicTacToePlayer


def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_green(text: str):
    """Print text in green (phosphor terminal style)"""
    print(Fore.GREEN + text + Style.RESET_ALL)


def print_red(text: str):
    """Print text in red"""
    print(Fore.RED + text + Style.RESET_ALL)


def print_yellow(text: str):
    """Print text in yellow"""
    print(Fore.YELLOW + text + Style.RESET_ALL)


def print_cyan(text: str):
    """Print text in cyan"""
    print(Fore.CYAN + text + Style.RESET_ALL)


def show_tictactoe_intro():
    """Show TicTacToe intro sequence"""
    clear_screen()
    
    intro_art = """
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║  ████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    ████████╗ ██████╗  ║
║  ╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗ ║
║     ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║ ║
║     ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║ ║
║     ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝ ║
║     ╚═╝   ╚═╝ ╚═════╝       ╚═╝   ╚═╝  ╚═╝ ╚═════╝       ╚═╝    ╚═════╝  ║
║                                                                            ║
║                    "SHALL WE PLAY A GAME?"                                 ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
    """
    
    print_green(intro_art)
    time.sleep(1.5)


def show_tictactoe_menu() -> str:
    """Show TicTacToe mode selection menu"""
    clear_screen()
    print_green("╔════════════════════════════════════════╗")
    print_green("║         TIC-TAC-TOE GAME MODE          ║")
    print_green("╠════════════════════════════════════════╣")
    print_green("║  1. Human vs WOPR                      ║")
    print_green("║  2. WOPR vs WOPR (Watch AI learn)      ║")
    print_green("║  3. Return to main menu                ║")
    print_green("╚════════════════════════════════════════╝")
    
    choice = input(Fore.GREEN + "\nSelect mode: " + Style.RESET_ALL)
    return choice


def play_human_vs_ai():
    """Play Human vs AI mode"""
    game = TicTacToeGame()
    game.set_mode('human_vs_ai', 'perfect')
    
    clear_screen()
    print_green("╔════════════════════════════════════════════════════════════════════════════╗")
    print_green("║                         HUMAN vs WOPR                                      ║")
    print_green("║                                                                            ║")
    print_green("║  You are X, WOPR is O                                                     ║")
    print_green("║  Enter your move as: row column (e.g., '1 2' for row 1, column 2)        ║")
    print_green("║                                                                            ║")
    print_green("╚════════════════════════════════════════════════════════════════════════════╝")
    time.sleep(2)
    
    while not game.game_over:
        clear_screen()
        print_green(game.get_board_string())
        print_green(f"\nCurrent player: {game.current_player.value}")
        
        if game.is_current_player_ai():
            print_yellow("\nWOPR is thinking...")
            time.sleep(1)
            
            move = game.get_ai_move()
            if move:
                game.make_move(move[0], move[1])
                print_green(f"WOPR plays: Row {move[0]+1}, Column {move[1]+1}")
                time.sleep(1.5)
        else:
            # Human player
            valid_move = False
            while not valid_move:
                try:
                    move_input = input(Fore.GREEN + "\nYour move (row column): " + Style.RESET_ALL)
                    parts = move_input.strip().split()
                    
                    if len(parts) != 2:
                        print_red("Invalid input! Enter row and column (e.g., '1 2')")
                        continue
                    
                    row = int(parts[0]) - 1
                    col = int(parts[1]) - 1
                    
                    if game.make_move(row, col):
                        valid_move = True
                    else:
                        print_red("Invalid move! Try again.")
                        time.sleep(1)
                except (ValueError, IndexError):
                    print_red("Invalid input! Enter row and column as numbers (1-3)")
                    time.sleep(1)
    
    # Game over
    clear_screen()
    print_green(game.get_board_string())
    print_green("\n" + "=" * 80)
    
    if game.winner is None:
        print_yellow("\n                           DRAW")
        print_yellow("\n              A STRANGE GAME.")
        print_yellow("      THE ONLY WINNING MOVE IS NOT TO PLAY.")
    elif game.winner == TicTacToePlayer.X.value:
        print_green("\n                    YOU WIN!")
        print_yellow("\n              (This should not happen...)")
    else:
        print_red("\n                    WOPR WINS!")
        print_yellow("\n              A STRANGE GAME.")
    
    print_green("\n" + "=" * 80)
    input(Fore.GREEN + "\nPress Enter to continue..." + Style.RESET_ALL)


def play_ai_vs_ai(num_games: int = 5):
    """Play AI vs AI mode - demonstrates futility"""
    clear_screen()
    print_green("╔════════════════════════════════════════════════════════════════════════════╗")
    print_green("║                         WOPR vs WOPR                                       ║")
    print_green("║                                                                            ║")
    print_green("║  Watch as WOPR plays against itself...                                    ║")
    print_green("║  Learning that the only winning move is not to play.                      ║")
    print_green("║                                                                            ║")
    print_green("╚════════════════════════════════════════════════════════════════════════════╝")
    time.sleep(2)
    
    results = {'X': 0, 'O': 0, 'DRAW': 0}
    
    # Display initial empty board once
    clear_screen()
    print_green("╔════════════════════════════════════════════════════════════════════════════╗")
    print_green("║                         WOPR vs WOPR                                       ║")
    print_green("║                    Simulating 5 games...                                   ║")
    print_green("╚════════════════════════════════════════════════════════════════════════════╝\n")
    
    for game_num in range(1, num_games + 1):
        game = TicTacToeGame()
        game.set_mode('ai_vs_ai')
        
        print_yellow(f"\nGAME {game_num}/{num_games}")
        print_yellow('='*80)
        
        # Show the board updating move by move
        while not game.game_over:
            # Clear previous board and redraw with new move
            # Move cursor up to redraw the board in place
            if game.move_count > 0:
                # Move cursor up 8 lines (board height)
                print("\033[8A", end='')
            
            # Display current board state
            print_green(game.get_board_string())
            
            move = game.get_ai_move()
            if move:
                game.make_move(move[0], move[1])
                time.sleep(0.4)
        
        # Record result
        if game.winner is None:
            results['DRAW'] += 1
            print_yellow("\nResult: DRAW")
        else:
            results[game.winner] += 1
            print_green(f"\nResult: {game.winner} wins")
        
        time.sleep(1.5)
    
    # Show final statistics
    clear_screen()
    print_green("╔════════════════════════════════════════════════════════════════════════════╗")
    print_green("║                         SIMULATION COMPLETE                                ║")
    print_green("╠════════════════════════════════════════════════════════════════════════════╣")
    print_green(f"║  Games played: {num_games:3d}                                                      ║")
    print_green(f"║  X wins:       {results['X']:3d}                                                      ║")
    print_green(f"║  O wins:       {results['O']:3d}                                                      ║")
    print_green(f"║  Draws:        {results['DRAW']:3d}                                                      ║")
    print_green("╠════════════════════════════════════════════════════════════════════════════╣")
    print_green("║                                                                            ║")
    print_yellow("║                         A STRANGE GAME.                                    ║")
    print_yellow("║              THE ONLY WINNING MOVE IS NOT TO PLAY.                         ║")
    print_green("║                                                                            ║")
    print_green("║  WOPR has learned that perfect play always results in a draw.             ║")
    print_green("║  Just like nuclear war - nobody wins.                                     ║")
    print_green("║                                                                            ║")
    print_green("╚════════════════════════════════════════════════════════════════════════════╝")
    
    input(Fore.GREEN + "\nPress Enter to continue..." + Style.RESET_ALL)


def run_tictactoe_game():
    """Main TicTacToe game loop"""
    show_tictactoe_intro()
    
    while True:
        choice = show_tictactoe_menu()
        
        if choice == '1':
            play_human_vs_ai()
        elif choice == '2':
            play_ai_vs_ai(5)
        elif choice == '3':
            break
        else:
            print_red("\nInvalid choice!")
            time.sleep(1)


if __name__ == "__main__":
    # Test the UI
    run_tictactoe_game()

# Made with Bob