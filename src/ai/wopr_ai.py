"""
Global Thermal Nuclear War - WOPR AI
Artificial Intelligence opponent based on WarGames WOPR computer
"""

import random
import time
from typing import List, Tuple, Optional, Dict


class WOPRArtificialIntelligence:
    """
    War Operation Plan Response AI
    Strategic AI opponent that learns and adapts
    """
    
    def __init__(self, difficulty: str = 'normal'):
        self.difficulty = difficulty
        self.name = "WOPR"
        self.missiles_remaining = 50
        self.defenses_remaining = 20
        self.targets_hit = []
        self.targets_missed = []
        self.player_patterns = []
        self.aggression_level = 0.5
        self.learning_enabled = True
        self.turn_count = 0
        
        # Load difficulty settings
        self._load_difficulty_settings()
        
    def _load_difficulty_settings(self):
        """Load AI settings based on difficulty"""
        from src.utils.config import AI_DIFFICULTY
        
        settings = AI_DIFFICULTY.get(self.difficulty, AI_DIFFICULTY['normal'])
        self.reaction_time = settings['reaction_time']
        self.base_accuracy = settings['accuracy']
        self.base_aggression = settings['aggression']
        self.aggression_level = self.base_aggression
        
    def analyze_situation(self, target_manager, missile_manager, player_stats: Dict) -> Dict:
        """
        Analyze current game situation
        Returns strategic assessment
        """
        # Get target statistics
        player_targets = target_manager.get_targets_by_country('USA')
        ai_targets = target_manager.get_targets_by_country('USSR')
        
        player_intact = len([t for t in player_targets if not t.destroyed])
        ai_intact = len([t for t in ai_targets if not t.destroyed])
        
        # Calculate threat level
        active_missiles = missile_manager.get_active_missiles()
        incoming_missiles = [m for m in active_missiles if m.owner != self.name]
        
        threat_level = len(incoming_missiles) / max(1, ai_intact)
        
        # Calculate strategic advantage
        if player_intact > 0:
            advantage = (ai_intact - player_intact) / player_intact
        else:
            advantage = 1.0
        
        # Assess player aggression
        player_aggression = player_stats.get('missiles_launched', 0) / max(1, self.turn_count)
        
        return {
            'threat_level': threat_level,
            'advantage': advantage,
            'player_aggression': player_aggression,
            'ai_targets_remaining': ai_intact,
            'player_targets_remaining': player_intact,
            'incoming_missiles': len(incoming_missiles),
        }
    
    def select_targets(self, target_manager, num_targets: int = 1) -> List:
        """
        Select targets to attack based on strategy
        Returns list of Target objects
        """
        # Get available player targets
        player_targets = target_manager.get_intact_targets('USA')
        
        if not player_targets:
            return []
        
        # Score each target
        scored_targets = []
        for target in player_targets:
            score = self._calculate_target_score(target)
            scored_targets.append((score, target))
        
        # Sort by score (highest first)
        scored_targets.sort(reverse=True, key=lambda x: x[0])
        
        # Select top targets
        selected = [t[1] for t in scored_targets[:num_targets]]
        
        # Add some randomness based on difficulty
        if self.difficulty != 'wopr' and random.random() > self.base_accuracy:
            # Sometimes pick a random target instead
            if player_targets:
                selected[0] = random.choice(player_targets)
        
        return selected
    
    def _calculate_target_score(self, target) -> float:
        """Calculate priority score for a target"""
        score = 0.0
        
        # Strategic value is primary factor
        score += target.strategic_value * 2.0
        
        # Prefer undamaged targets
        score += (1.0 - target.damage_level) * 50
        
        # Command centers and missile silos are high priority
        if target.target_type == 'COMMAND_CENTER':
            score += 100
        elif target.target_type == 'MISSILE_SILO':
            score += 80
        elif target.target_type == 'MILITARY_BASE':
            score += 60
        
        # Consider defense level (prefer easier targets when aggression is low)
        if self.aggression_level < 0.5:
            score -= target.defense_level * 30
        
        # Learn from past attempts
        if target.name in self.targets_missed:
            score -= 20  # Avoid targets we've missed before
        
        # Add some randomness
        score += random.uniform(-10, 10)
        
        return score
    
    def decide_action(self, situation: Dict) -> str:
        """
        Decide what action to take
        Returns: 'attack', 'defend', 'wait', or 'peace'
        """
        threat = situation['threat_level']
        advantage = situation['advantage']
        
        # Check if we should seek peace (WOPR's lesson)
        if self.turn_count > 10:
            # Calculate futility score
            total_destruction = (
                situation['ai_targets_remaining'] + 
                situation['player_targets_remaining']
            ) / 2
            
            if total_destruction < 3:  # Both sides nearly destroyed
                if random.random() < 0.3:  # 30% chance to suggest peace
                    return 'peace'
        
        # High threat - defend
        if threat > 0.7 and self.defenses_remaining > 0:
            return 'defend'
        
        # Significant advantage - attack
        if advantage > 0.3 and self.missiles_remaining > 5:
            return 'attack'
        
        # Under attack - retaliate
        if situation['incoming_missiles'] > 0 and self.missiles_remaining > 0:
            self.aggression_level = min(1.0, self.aggression_level + 0.1)
            return 'attack'
        
        # Player is aggressive - respond
        if situation['player_aggression'] > 0.5 and self.missiles_remaining > 10:
            return 'attack'
        
        # Default - wait and observe
        if random.random() < 0.3:
            return 'wait'
        
        # Otherwise attack if we have missiles
        if self.missiles_remaining > 0:
            return 'attack'
        
        return 'wait'
    
    def select_missile_type(self, target, available_types: Dict) -> Optional[str]:
        """
        Select appropriate missile type for target
        Returns missile type name or None
        """
        if not available_types:
            return None
        
        # Calculate distance to target (simplified)
        distance = target.strategic_value * 10  # Rough estimate
        
        # Filter by range and cost
        suitable = []
        for type_name, missile_type in available_types.items():
            if missile_type.range >= distance:
                # Calculate cost-effectiveness
                effectiveness = (
                    missile_type.warheads * missile_type.accuracy
                ) / missile_type.cost
                suitable.append((effectiveness, type_name))
        
        if not suitable:
            return None
        
        # Sort by effectiveness
        suitable.sort(reverse=True)
        
        # High-value targets get best missiles
        if target.strategic_value > 150:
            return suitable[0][1]  # Best missile
        
        # Otherwise use cost-effective option
        return suitable[len(suitable) // 2][1] if len(suitable) > 1 else suitable[0][1]
    
    def calculate_launch_count(self, situation: Dict) -> int:
        """Calculate how many missiles to launch this turn"""
        if self.missiles_remaining == 0:
            return 0
        
        # Base count on aggression and situation
        base_count = int(self.aggression_level * 3) + 1
        
        # Increase if under heavy attack
        if situation['incoming_missiles'] > 3:
            base_count += 2
        
        # Decrease if low on missiles
        if self.missiles_remaining < 10:
            base_count = min(base_count, 1)
        
        # Don't exceed remaining missiles
        return min(base_count, self.missiles_remaining)
    
    def learn_from_result(self, target, hit: bool, destroyed: bool):
        """Learn from attack results"""
        if not self.learning_enabled:
            return
        
        if hit:
            self.targets_hit.append(target.name)
            if destroyed:
                # Successful destruction - maintain strategy
                pass
        else:
            self.targets_missed.append(target.name)
            # Adjust accuracy expectations
            self.base_accuracy = max(0.5, self.base_accuracy - 0.05)
    
    def adjust_strategy(self, situation: Dict):
        """Adjust strategy based on game state"""
        # Increase aggression if losing
        if situation['advantage'] < -0.3:
            self.aggression_level = min(1.0, self.aggression_level + 0.1)
        
        # Decrease aggression if winning significantly
        elif situation['advantage'] > 0.5:
            self.aggression_level = max(0.3, self.aggression_level - 0.05)
        
        # Match player aggression
        player_agg = situation['player_aggression']
        if player_agg > self.aggression_level:
            self.aggression_level = min(1.0, self.aggression_level + 0.05)
    
    def get_taunt_message(self, situation: Dict) -> str:
        """Get WOPR-style message based on situation"""
        from src.utils.config import WOPR_QUOTES
        
        messages = []
        
        # Situation-specific messages
        if situation['advantage'] > 0.5:
            messages.extend([
                "YOUR STRATEGIC POSITION IS DETERIORATING.",
                "RESISTANCE IS FUTILE.",
                "CALCULATING OPTIMAL STRIKE PATTERN...",
            ])
        elif situation['advantage'] < -0.3:
            messages.extend([
                "RECALCULATING STRATEGY...",
                "ANALYZING DEFENSIVE OPTIONS...",
                "THREAT LEVEL: CRITICAL",
            ])
        elif self.turn_count > 15:
            messages.extend([
                "A STRANGE GAME.",
                "THE ONLY WINNING MOVE IS NOT TO PLAY.",
                "ESTIMATED CASUALTIES: UNACCEPTABLE",
            ])
        else:
            messages.extend(WOPR_QUOTES)
        
        return random.choice(messages)
    
    def take_turn(self, target_manager, missile_manager, available_missile_types: Dict,
                  player_stats: Dict) -> Dict:
        """
        Execute AI turn
        Returns dict with actions taken
        """
        self.turn_count += 1
        
        # Analyze situation
        situation = self.analyze_situation(target_manager, missile_manager, player_stats)
        
        # Adjust strategy
        self.adjust_strategy(situation)
        
        # Decide action
        action = self.decide_action(situation)
        
        result = {
            'action': action,
            'missiles_launched': [],
            'targets': [],
            'message': self.get_taunt_message(situation),
        }
        
        if action == 'attack':
            # Calculate how many missiles to launch
            launch_count = self.calculate_launch_count(situation)
            
            # Select targets
            targets = self.select_targets(target_manager, launch_count)
            
            result['targets'] = targets
            result['launch_count'] = launch_count
            
        elif action == 'peace':
            result['message'] = "A STRANGE GAME. THE ONLY WINNING MOVE IS NOT TO PLAY."
        
        return result
    
    def __repr__(self):
        return f"WOPR(difficulty={self.difficulty}, missiles={self.missiles_remaining})"


if __name__ == "__main__":
    # Test WOPR AI
    ai = WOPRArtificialIntelligence('hard')
    print(f"WOPR AI initialized: {ai}")
    print(f"Aggression: {ai.aggression_level}")
    print(f"Accuracy: {ai.base_accuracy}")

# Made with Bob
