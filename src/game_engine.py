"""
Global Thermal Nuclear War - Game Engine
Core game loop and state management
"""

import time
import sys
from typing import Optional, Dict, List
from enum import Enum

from src.game_logic.target import Target, TargetManager, create_targets_from_config
from src.game_logic.missile import Missile, MissileManager, MissileType, create_missile_types_from_config
from src.ai.wopr_ai import WOPRArtificialIntelligence
from src.utils.config import WORLD_TARGETS, MISSILE_TYPES


class GameState(Enum):
    """Game state enumeration"""
    MENU = "menu"
    INTRO = "intro"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    PEACE = "peace"


class GameMode(Enum):
    """Game mode enumeration"""
    CAMPAIGN = "campaign"
    SIMULATION = "simulation"
    TUTORIAL = "tutorial"


class Player:
    """Represents a player in the game"""
    
    def __init__(self, name: str, country: str, is_ai: bool = False):
        self.name = name
        self.country = country
        self.is_ai = is_ai
        self.missiles_remaining = 50
        self.defenses_remaining = 20
        self.missiles_launched = []
        self.targets_destroyed = []
        self.score = 0
        
    def launch_missile(self, missile: Missile):
        """Record missile launch"""
        self.missiles_launched.append(missile)
        self.missiles_remaining -= 1
        
    def target_destroyed(self, target: Target):
        """Record target destruction"""
        self.targets_destroyed.append(target)
        self.score += target.strategic_value
        
    def get_stats(self) -> Dict:
        """Get player statistics"""
        return {
            'name': self.name,
            'country': self.country,
            'missiles_remaining': self.missiles_remaining,
            'missiles_launched': len(self.missiles_launched),
            'targets_destroyed': len(self.targets_destroyed),
            'score': self.score,
        }


class GameEngine:
    """Main game engine"""
    
    def __init__(self):
        self.state = GameState.MENU
        self.mode = None
        self.running = False
        self.paused = False
        
        # Game objects
        self.target_manager = None
        self.missile_manager = None
        self.missile_types = {}
        
        # Players
        self.player = None
        self.ai_opponent = None
        
        # Game state
        self.turn_count = 0
        self.game_time = 0.0
        self.last_update = time.time()
        
        # Statistics
        self.total_casualties = 0
        self.total_missiles_launched = 0
        self.game_result = None
        
    def initialize_game(self, mode: GameMode, difficulty: str = 'normal'):
        """Initialize a new game"""
        self.mode = mode
        self.turn_count = 0
        self.game_time = 0.0
        self.total_casualties = 0
        self.total_missiles_launched = 0
        
        # Create target manager
        self.target_manager = create_targets_from_config(WORLD_TARGETS)
        
        # Create missile manager
        self.missile_manager = MissileManager()
        
        # Create missile types
        self.missile_types = create_missile_types_from_config(MISSILE_TYPES)
        
        # Create player
        self.player = Player("PLAYER", "USA", is_ai=False)
        
        # Create AI opponent
        if mode != GameMode.TUTORIAL:
            self.ai_opponent = WOPRArtificialIntelligence(difficulty)
        
        self.state = GameState.PLAYING
        self.running = True
        
    def update(self, delta_time: float):
        """Update game state"""
        if self.state != GameState.PLAYING or self.paused:
            return
        
        self.game_time += delta_time
        
        # Update missiles
        self.missile_manager.update_missiles(delta_time)
        
        # Check for missile impacts
        self._check_missile_impacts()
        
        # Update statistics
        self._update_statistics()
        
        # Check win/loss conditions
        self._check_game_over()
        
    def _check_missile_impacts(self):
        """Check for missile impacts and apply damage"""
        for missile in self.missile_manager.detonated_missiles[:]:
            if missile in self.missile_manager.detonated_missiles:
                # Find target at impact location
                target = self.target_manager.get_nearest_target(
                    missile.target[0], 
                    missile.target[1],
                    intact_only=False
                )
                
                if target and not target.destroyed:
                    # Apply damage
                    result = target.take_damage(
                        missile.missile_type.warheads,
                        missile.missile_type.accuracy
                    )
                    
                    # Update player stats
                    if result['destroyed']:
                        if missile.owner == self.player.name:
                            self.player.target_destroyed(target)
                        elif self.ai_opponent:
                            self.ai_opponent.targets_hit.append(target.name)
                
                # Remove from detonated list
                self.missile_manager.detonated_missiles.remove(missile)
    
    def _update_statistics(self):
        """Update game statistics"""
        self.total_casualties = self.target_manager.get_total_casualties()
        self.total_missiles_launched = len(self.missile_manager.missiles)
    
    def _check_game_over(self):
        """Check if game is over"""
        # Check for mutual assured destruction
        usa_targets = self.target_manager.get_intact_targets('USA')
        ussr_targets = self.target_manager.get_intact_targets('USSR')
        
        usa_destruction = self.target_manager.get_destruction_percentage('USA')
        ussr_destruction = self.target_manager.get_destruction_percentage('USSR')
        
        # MAD condition: both sides heavily damaged
        if usa_destruction > 80 and ussr_destruction > 80:
            self.state = GameState.GAME_OVER
            self.game_result = 'MAD'
            self.running = False
            return
        
        # Player loses: all USA targets destroyed
        if len(usa_targets) == 0:
            self.state = GameState.GAME_OVER
            self.game_result = 'DEFEAT'
            self.running = False
            return
        
        # Player wins: all USSR targets destroyed (unlikely)
        if len(ussr_targets) == 0:
            self.state = GameState.GAME_OVER
            self.game_result = 'VICTORY'
            self.running = False
            return
        
        # Peace condition: both sides stop attacking
        if self.turn_count > 20:
            active_missiles = len(self.missile_manager.get_active_missiles())
            if active_missiles == 0 and self.player.missiles_remaining > 0:
                # Check if AI wants peace
                if self.ai_opponent:
                    situation = self.ai_opponent.analyze_situation(
                        self.target_manager,
                        self.missile_manager,
                        self.player.get_stats()
                    )
                    action = self.ai_opponent.decide_action(situation)
                    if action == 'peace':
                        self.state = GameState.PEACE
                        self.game_result = 'PEACE'
                        self.running = False
    
    def player_launch_missile(self, missile_type_name: str, target: Target) -> bool:
        """
        Player launches a missile at a target
        Returns True if successful
        """
        if self.player.missiles_remaining <= 0:
            return False
        
        if missile_type_name not in self.missile_types:
            return False
        
        missile_type = self.missile_types[missile_type_name]
        
        # Get player's launch position (simplified - use first USA target)
        usa_targets = self.target_manager.get_targets_by_country('USA')
        if not usa_targets:
            return False
        
        origin = (usa_targets[0].x, usa_targets[0].y)
        target_pos = (target.x, target.y)
        
        # Create missile
        missile = self.missile_manager.create_missile(
            missile_type,
            origin,
            target_pos,
            self.player.name
        )
        
        if not missile:
            return False
        
        # Launch missile
        self.missile_manager.launch_missile(missile)
        self.player.launch_missile(missile)
        
        return True
    
    def ai_take_turn(self):
        """AI takes its turn"""
        if not self.ai_opponent or self.state != GameState.PLAYING:
            return
        
        # AI analyzes and acts
        result = self.ai_opponent.take_turn(
            self.target_manager,
            self.missile_manager,
            self.missile_types,
            self.player.get_stats()
        )
        
        # Execute AI actions
        if result['action'] == 'attack' and result.get('targets'):
            # Get AI launch position
            ussr_targets = self.target_manager.get_targets_by_country('USSR')
            if ussr_targets:
                origin = (ussr_targets[0].x, ussr_targets[0].y)
                
                for target in result['targets']:
                    if self.ai_opponent.missiles_remaining <= 0:
                        break
                    
                    # Select missile type
                    missile_type_name = self.ai_opponent.select_missile_type(
                        target,
                        self.missile_types
                    )
                    
                    if missile_type_name:
                        missile_type = self.missile_types[missile_type_name]
                        target_pos = (target.x, target.y)
                        
                        # Create and launch missile
                        missile = self.missile_manager.create_missile(
                            missile_type,
                            origin,
                            target_pos,
                            self.ai_opponent.name
                        )
                        
                        if missile:
                            self.missile_manager.launch_missile(missile)
                            self.ai_opponent.missiles_remaining -= 1
        
        return result
    
    def pause_game(self):
        """Pause the game"""
        self.paused = True
    
    def resume_game(self):
        """Resume the game"""
        self.paused = False
        self.last_update = time.time()
    
    def quit_game(self):
        """Quit the game"""
        self.running = False
        self.state = GameState.MENU
    
    def get_game_statistics(self) -> Dict:
        """Get comprehensive game statistics"""
        stats = {
            'turn_count': self.turn_count,
            'game_time': self.game_time,
            'total_casualties': self.total_casualties,
            'total_missiles_launched': self.total_missiles_launched,
            'player_stats': self.player.get_stats() if self.player else {},
            'target_stats': self.target_manager.get_statistics() if self.target_manager else {},
            'missile_stats': self.missile_manager.get_statistics() if self.missile_manager else {},
        }
        
        if self.ai_opponent:
            stats['ai_stats'] = {
                'missiles_remaining': self.ai_opponent.missiles_remaining,
                'targets_hit': len(self.ai_opponent.targets_hit),
                'aggression_level': self.ai_opponent.aggression_level,
            }
        
        return stats
    
    def get_game_result_message(self) -> str:
        """Get game over message based on result"""
        from src.utils.config import MESSAGES
        
        if self.game_result == 'MAD':
            return MESSAGES['game_over_mad']
        elif self.game_result == 'PEACE':
            return MESSAGES['game_over_peace']
        elif self.game_result == 'VICTORY':
            return "VICTORY ACHIEVED\n\nBut at what cost?"
        elif self.game_result == 'DEFEAT':
            return "DEFEAT\n\nAll strategic assets destroyed."
        else:
            return "GAME OVER"


if __name__ == "__main__":
    # Test game engine
    engine = GameEngine()
    engine.initialize_game(GameMode.CAMPAIGN, 'normal')
    print(f"Game initialized: {engine.state}")
    print(f"Targets: {len(engine.target_manager.all_targets)}")
    print(f"Missile types: {list(engine.missile_types.keys())}")

# Made with Bob
