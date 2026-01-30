"""
Global Thermal Nuclear War - TicTacToe Easter Egg
A hidden game that demonstrates "the only winning move is not to play"
Inspired by the WarGames movie scene where WOPR learns this lesson
"""

import random
import time
from typing import List, Tuple, Optional
from enum import Enum


class TicTacToePlayer(Enum):
    """Player types"""
    X = "X"
    O = "O"
    EMPTY = " "


class TicTacToeAI:
    """
    AI player for TicTacToe using minimax algorithm
    Plays perfectly - will never lose
    """
    
    def __init__(self, symbol: TicTacToePlayer, difficulty: str = 'perfect'):
        self.symbol = symbol
        self.opponent_symbol = TicTacToePlayer.O if symbol == TicTacToePlayer.X else TicTacToePlayer.X
        self.difficulty = difficulty
        self.games_played = 0
        self.learning_mode = False
        
    def get_best_move(self, board: List[List[str]]) -> Optional[Tuple[int, int]]:
        """Get the best move using minimax algorithm"""
        if self.difficulty == 'random':
            return self._get_random_move(board)
        elif self.difficulty == 'easy':
            # 50% random, 50% optimal
            if random.random() < 0.5:
                return self._get_random_move(board)
        
        # Perfect play using minimax
        best_score = float('-inf')
        best_move = None
        
        for i in range(3):
            for j in range(3):
                if board[i][j] == TicTacToePlayer.EMPTY.value:
                    # Try this move
                    board[i][j] = self.symbol.value
                    score = self._minimax(board, 0, False)
                    board[i][j] = TicTacToePlayer.EMPTY.value
                    
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        return best_move
    
    def _get_random_move(self, board: List[List[str]]) -> Optional[Tuple[int, int]]:
        """Get a random valid move"""
        empty_cells = []
        for i in range(3):
            for j in range(3):
                if board[i][j] == TicTacToePlayer.EMPTY.value:
                    empty_cells.append((i, j))
        
        return random.choice(empty_cells) if empty_cells else None
    
    def _minimax(self, board: List[List[str]], depth: int, is_maximizing: bool) -> int:
        """
        Minimax algorithm for perfect play
        Returns the best score for the current position
        """
        # Check terminal states
        winner = self._check_winner(board)
        if winner == self.symbol.value:
            return 10 - depth
        elif winner == self.opponent_symbol.value:
            return depth - 10
        elif self._is_board_full(board):
            return 0
        
        if is_maximizing:
            best_score = -999
            for i in range(3):
                for j in range(3):
                    if board[i][j] == TicTacToePlayer.EMPTY.value:
                        board[i][j] = self.symbol.value
                        score = self._minimax(board, depth + 1, False)
                        board[i][j] = TicTacToePlayer.EMPTY.value
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = 999
            for i in range(3):
                for j in range(3):
                    if board[i][j] == TicTacToePlayer.EMPTY.value:
                        board[i][j] = self.opponent_symbol.value
                        score = self._minimax(board, depth + 1, True)
                        board[i][j] = TicTacToePlayer.EMPTY.value
                        best_score = min(score, best_score)
            return best_score
    
    def _check_winner(self, board: List[List[str]]) -> Optional[str]:
        """Check if there's a winner"""
        # Check rows
        for row in board:
            if row[0] == row[1] == row[2] != TicTacToePlayer.EMPTY.value:
                return row[0]
        
        # Check columns
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] != TicTacToePlayer.EMPTY.value:
                return board[0][col]
        
        # Check diagonals
        if board[0][0] == board[1][1] == board[2][2] != TicTacToePlayer.EMPTY.value:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != TicTacToePlayer.EMPTY.value:
            return board[0][2]
        
        return None
    
    def _is_board_full(self, board: List[List[str]]) -> bool:
        """Check if board is full"""
        for row in board:
            if TicTacToePlayer.EMPTY.value in row:
                return False
        return True


class TicTacToeGame:
    """
    TicTacToe game implementation
    Supports Human vs AI and AI vs AI modes
    """
    
    def __init__(self):
        self.board = [[TicTacToePlayer.EMPTY.value for _ in range(3)] for _ in range(3)]
        self.current_player = TicTacToePlayer.X
        self.game_over = False
        self.winner = None
        self.move_count = 0
        self.ai_players = {}
        self.game_mode = None
        
    def reset(self):
        """Reset the game"""
        self.board = [[TicTacToePlayer.EMPTY.value for _ in range(3)] for _ in range(3)]
        self.current_player = TicTacToePlayer.X
        self.game_over = False
        self.winner = None
        self.move_count = 0
    
    def set_mode(self, mode: str, difficulty: str = 'perfect'):
        """
        Set game mode
        mode: 'human_vs_ai', 'ai_vs_ai'
        """
        self.game_mode = mode
        self.ai_players = {}
        
        if mode == 'human_vs_ai':
            # Human is X, AI is O
            self.ai_players[TicTacToePlayer.O] = TicTacToeAI(TicTacToePlayer.O, difficulty)
        elif mode == 'ai_vs_ai':
            # Both are AI
            self.ai_players[TicTacToePlayer.X] = TicTacToeAI(TicTacToePlayer.X, 'perfect')
            self.ai_players[TicTacToePlayer.O] = TicTacToeAI(TicTacToePlayer.O, 'perfect')
    
    def make_move(self, row: int, col: int) -> bool:
        """
        Make a move at the specified position
        Returns True if move was valid
        """
        if self.game_over:
            return False
        
        if not (0 <= row < 3 and 0 <= col < 3):
            return False
        
        if self.board[row][col] != TicTacToePlayer.EMPTY.value:
            return False
        
        # Make the move
        self.board[row][col] = self.current_player.value
        self.move_count += 1
        
        # Check for winner
        self._check_game_over()
        
        # Switch player
        if not self.game_over:
            self.current_player = TicTacToePlayer.O if self.current_player == TicTacToePlayer.X else TicTacToePlayer.X
        
        return True
    
    def get_ai_move(self) -> Optional[Tuple[int, int]]:
        """Get AI move for current player"""
        if self.current_player in self.ai_players:
            return self.ai_players[self.current_player].get_best_move(self.board)
        return None
    
    def _check_game_over(self):
        """Check if game is over"""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != TicTacToePlayer.EMPTY.value:
                self.game_over = True
                self.winner = row[0]
                return
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != TicTacToePlayer.EMPTY.value:
                self.game_over = True
                self.winner = self.board[0][col]
                return
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != TicTacToePlayer.EMPTY.value:
            self.game_over = True
            self.winner = self.board[0][0]
            return
        
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != TicTacToePlayer.EMPTY.value:
            self.game_over = True
            self.winner = self.board[0][2]
            return
        
        # Check for draw
        if self.move_count >= 9:
            self.game_over = True
            self.winner = None  # Draw
    
    def get_board_string(self) -> str:
        """Get string representation of the board"""
        lines = []
        lines.append("     1   2   3")
        lines.append("   ╔═══╦═══╦═══╗")
        
        for i, row in enumerate(self.board):
            row_str = f" {i+1} ║ {row[0]} ║ {row[1]} ║ {row[2]} ║"
            lines.append(row_str)
            if i < 2:
                lines.append("   ╠═══╬═══╬═══╣")
        
        lines.append("   ╚═══╩═══╩═══╝")
        return '\n'.join(lines)
    
    def is_current_player_ai(self) -> bool:
        """Check if current player is AI"""
        return self.current_player in self.ai_players
    
    def get_game_result(self) -> str:
        """Get game result message"""
        if not self.game_over:
            return "Game in progress"
        
        if self.winner is None:
            return "DRAW - A STRANGE GAME"
        else:
            return f"Winner: {self.winner}"


if __name__ == "__main__":
    # Test the game
    game = TicTacToeGame()
    game.set_mode('ai_vs_ai')
    
    print("Testing AI vs AI mode...")
    while not game.game_over:
        print(game.get_board_string())
        print(f"\nCurrent player: {game.current_player.value}")
        
        move = game.get_ai_move()
        if move:
            game.make_move(move[0], move[1])
            time.sleep(0.5)
    
    print(game.get_board_string())
    print(f"\n{game.get_game_result()}")

# Made with Bob