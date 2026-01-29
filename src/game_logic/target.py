"""
Global Thermal Nuclear War - Target Management
Handles target locations, status, and damage
"""

from typing import Dict, Tuple
import random


class Target:
    """Represents a target location on the map"""
    
    def __init__(self, name: str, target_type: str, x: int, y: int, 
                 population: int, strategic_value: int, defense_level: float):
        self.name = name
        self.target_type = target_type
        self.x = x
        self.y = y
        self.population = population
        self.strategic_value = strategic_value
        self.defense_level = defense_level
        self.destroyed = False
        self.damage_level = 0.0  # 0.0 to 1.0
        self.casualties = 0
        self.hit_count = 0
        
    def take_damage(self, warheads: int, accuracy: float) -> Dict:
        """
        Apply damage to the target
        Returns dict with damage results
        """
        if self.destroyed:
            return {
                'hit': False,
                'destroyed': False,
                'casualties': 0,
                'message': f"{self.name} is already destroyed"
            }
        
        # Check if defense systems intercept
        if random.random() < self.defense_level:
            intercepted = random.randint(1, warheads)
            warheads -= intercepted
            if warheads <= 0:
                return {
                    'hit': False,
                    'destroyed': False,
                    'casualties': 0,
                    'intercepted': intercepted,
                    'message': f"Defense systems intercepted all warheads targeting {self.name}"
                }
        
        # Calculate hits based on accuracy
        hits = sum(1 for _ in range(warheads) if random.random() < accuracy)
        
        if hits == 0:
            return {
                'hit': False,
                'destroyed': False,
                'casualties': 0,
                'message': f"All warheads missed {self.name}"
            }
        
        # Calculate damage
        damage_per_hit = 0.3  # Each hit does 30% damage
        total_damage = min(1.0, hits * damage_per_hit)
        self.damage_level = min(1.0, self.damage_level + total_damage)
        self.hit_count += hits
        
        # Calculate casualties
        casualty_rate = total_damage * 0.8  # 80% of population affected by damage
        new_casualties = int(self.population * casualty_rate * (1 - self.damage_level + total_damage))
        self.casualties += new_casualties
        
        # Check if destroyed
        if self.damage_level >= 0.9:
            self.destroyed = True
            message = f"{self.name} has been DESTROYED! {self.casualties:,} casualties"
        else:
            message = f"{self.name} hit by {hits} warhead(s). Damage: {int(self.damage_level * 100)}%"
        
        return {
            'hit': True,
            'destroyed': self.destroyed,
            'casualties': new_casualties,
            'total_casualties': self.casualties,
            'damage_level': self.damage_level,
            'hits': hits,
            'message': message
        }
    
    def get_status(self) -> str:
        """Get current status of the target"""
        if self.destroyed:
            return "DESTROYED"
        elif self.damage_level > 0.7:
            return "CRITICAL"
        elif self.damage_level > 0.4:
            return "DAMAGED"
        elif self.damage_level > 0:
            return "HIT"
        else:
            return "INTACT"
    
    def get_symbol(self) -> str:
        """Get map symbol for this target"""
        from src.ui.ascii_art import TARGET_SYMBOLS
        if self.destroyed:
            return TARGET_SYMBOLS['DESTROYED']
        return TARGET_SYMBOLS.get(self.target_type, '○')
    
    def get_info(self) -> str:
        """Get detailed information about the target"""
        status = self.get_status()
        info = [
            f"Target: {self.name}",
            f"Type: {self.target_type}",
            f"Status: {status}",
            f"Population: {self.population:,}",
            f"Casualties: {self.casualties:,}",
            f"Strategic Value: {self.strategic_value}",
            f"Defense Level: {int(self.defense_level * 100)}%",
            f"Damage: {int(self.damage_level * 100)}%",
            f"Hits Taken: {self.hit_count}",
        ]
        return '\n'.join(info)
    
    def distance_to(self, other: 'Target') -> float:
        """Calculate distance to another target"""
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx * dx + dy * dy) ** 0.5
    
    def __repr__(self):
        return f"Target({self.name}, {self.target_type}, status={self.get_status()})"


class TargetManager:
    """Manages all targets in the game"""
    
    def __init__(self):
        self.targets = {}  # Dict[str, List[Target]]
        self.all_targets = []  # List of all targets
        
    def add_target(self, country: str, target: Target):
        """Add a target to the manager"""
        if country not in self.targets:
            self.targets[country] = []
        self.targets[country].append(target)
        self.all_targets.append(target)
    
    def get_targets_by_country(self, country: str) -> list:
        """Get all targets for a country"""
        return self.targets.get(country, [])
    
    def get_target_by_name(self, name: str) -> Target:
        """Find a target by name"""
        for target in self.all_targets:
            if target.name == name:
                return target
        return None
    
    def get_intact_targets(self, country: str = None) -> list:
        """Get all intact (not destroyed) targets"""
        if country:
            targets = self.get_targets_by_country(country)
        else:
            targets = self.all_targets
        return [t for t in targets if not t.destroyed]
    
    def get_destroyed_targets(self, country: str = None) -> list:
        """Get all destroyed targets"""
        if country:
            targets = self.get_targets_by_country(country)
        else:
            targets = self.all_targets
        return [t for t in targets if t.destroyed]
    
    def get_high_value_targets(self, country: str = None, min_value: int = 100) -> list:
        """Get high-value targets that are still intact"""
        intact = self.get_intact_targets(country)
        return [t for t in intact if t.strategic_value >= min_value]
    
    def get_total_casualties(self, country: str = None) -> int:
        """Get total casualties"""
        if country:
            targets = self.get_targets_by_country(country)
        else:
            targets = self.all_targets
        return sum(t.casualties for t in targets)
    
    def get_total_population(self, country: str = None) -> int:
        """Get total population"""
        if country:
            targets = self.get_targets_by_country(country)
        else:
            targets = self.all_targets
        return sum(t.population for t in targets)
    
    def get_destruction_percentage(self, country: str = None) -> float:
        """Get percentage of targets destroyed"""
        if country:
            targets = self.get_targets_by_country(country)
        else:
            targets = self.all_targets
        
        if not targets:
            return 0.0
        
        destroyed = len([t for t in targets if t.destroyed])
        return (destroyed / len(targets)) * 100
    
    def get_statistics(self) -> Dict:
        """Get overall statistics"""
        return {
            'total_targets': len(self.all_targets),
            'destroyed': len(self.get_destroyed_targets()),
            'intact': len(self.get_intact_targets()),
            'total_casualties': self.get_total_casualties(),
            'total_population': self.get_total_population(),
            'destruction_rate': self.get_destruction_percentage(),
        }
    
    def get_nearest_target(self, x: int, y: int, country: str = None, 
                          intact_only: bool = True) -> Target:
        """Find the nearest target to given coordinates"""
        if country:
            targets = self.get_targets_by_country(country)
        else:
            targets = self.all_targets
        
        if intact_only:
            targets = [t for t in targets if not t.destroyed]
        
        if not targets:
            return None
        
        # Calculate distances
        distances = []
        for target in targets:
            dx = target.x - x
            dy = target.y - y
            dist = (dx * dx + dy * dy) ** 0.5
            distances.append((dist, target))
        
        # Return nearest
        distances.sort(key=lambda x: x[0])
        return distances[0][1] if distances else None
    
    def __repr__(self):
        return f"TargetManager(countries={len(self.targets)}, targets={len(self.all_targets)})"


def create_targets_from_config(config_targets: Dict) -> TargetManager:
    """Create TargetManager from configuration"""
    from src.utils.config import TARGET_TYPES
    
    manager = TargetManager()
    
    for country, target_list in config_targets.items():
        for target_data in target_list:
            target_type = target_data['type']
            type_config = TARGET_TYPES[target_type]
            
            target = Target(
                name=target_data['name'],
                target_type=target_type,
                x=target_data['x'],
                y=target_data['y'],
                population=type_config['population'],
                strategic_value=type_config['strategic_value'],
                defense_level=type_config['defense_level']
            )
            
            manager.add_target(country, target)
    
    return manager


if __name__ == "__main__":
    # Test target system
    target = Target("Test City", "CITY", 10, 10, 1000000, 50, 0.3)
    print(target.get_info())
    
    result = target.take_damage(warheads=5, accuracy=0.9)
    print(f"\nAttack result: {result}")
    print(f"\nAfter attack:\n{target.get_info()}")

# Made with Bob
