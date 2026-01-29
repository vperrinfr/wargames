"""
Global Thermal Nuclear War - Missile System
Handles missile launches, trajectories, and combat
"""

import time
import math
from typing import Tuple, Optional, Dict
from dataclasses import dataclass


@dataclass
class MissileType:
    """Missile type configuration"""
    name: str
    range: int
    speed: float
    warheads: int
    accuracy: float
    cost: int


class Missile:
    """Represents a missile in flight"""
    
    def __init__(self, missile_type: MissileType, origin: Tuple[int, int], 
                 target: Tuple[int, int], owner: str):
        self.missile_type = missile_type
        self.origin = origin
        self.target = target
        self.owner = owner
        self.current_pos = list(origin)
        self.launched = False
        self.detonated = False
        self.intercepted = False
        self.flight_time = 0.0
        self.total_flight_time = self._calculate_flight_time()
        self.trajectory = self._calculate_trajectory()
        self.trajectory_index = 0
        
    def _calculate_flight_time(self) -> float:
        """Calculate total flight time based on distance and speed"""
        distance = self._calculate_distance(self.origin, self.target)
        # Flight time in seconds (simplified)
        return distance / self.missile_type.speed
    
    def _calculate_distance(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:
        """Calculate distance between two points"""
        dx = pos2[0] - pos1[0]
        dy = pos2[1] - pos1[1]
        return math.sqrt(dx * dx + dy * dy)
    
    def _calculate_trajectory(self) -> list:
        """Calculate missile trajectory points"""
        x1, y1 = self.origin
        x2, y2 = self.target
        
        # Number of points in trajectory
        distance = self._calculate_distance(self.origin, self.target)
        num_points = max(10, int(distance))
        
        trajectory = []
        for i in range(num_points + 1):
            t = i / num_points
            
            # Linear interpolation for x
            x = x1 + (x2 - x1) * t
            
            # Parabolic arc for y (ballistic trajectory)
            # Arc height is 20% of distance
            arc_height = distance * 0.2
            y = y1 + (y2 - y1) * t - 4 * arc_height * t * (1 - t)
            
            trajectory.append((int(x), int(y)))
        
        return trajectory
    
    def launch(self):
        """Launch the missile"""
        self.launched = True
        self.flight_time = 0.0
    
    def update(self, delta_time: float) -> bool:
        """
        Update missile position
        Returns True if missile is still in flight
        """
        if not self.launched or self.detonated or self.intercepted:
            return False
        
        self.flight_time += delta_time
        
        # Check if reached target
        if self.flight_time >= self.total_flight_time:
            self.detonate()
            return False
        
        # Update position along trajectory
        progress = self.flight_time / self.total_flight_time
        self.trajectory_index = int(progress * len(self.trajectory))
        
        if self.trajectory_index < len(self.trajectory):
            self.current_pos = list(self.trajectory[self.trajectory_index])
        
        return True
    
    def detonate(self):
        """Detonate the missile at target"""
        self.detonated = True
        self.current_pos = list(self.target)
    
    def intercept(self):
        """Intercept the missile"""
        self.intercepted = True
    
    def get_position(self) -> Tuple[int, int]:
        """Get current position"""
        return tuple(self.current_pos)
    
    def get_progress(self) -> float:
        """Get flight progress (0.0 to 1.0)"""
        if self.total_flight_time == 0:
            return 1.0
        return min(1.0, self.flight_time / self.total_flight_time)
    
    def is_in_range(self) -> bool:
        """Check if target is in range"""
        distance = self._calculate_distance(self.origin, self.target)
        return distance <= self.missile_type.range
    
    def get_status(self) -> str:
        """Get missile status"""
        if self.intercepted:
            return "INTERCEPTED"
        elif self.detonated:
            return "DETONATED"
        elif self.launched:
            return f"IN FLIGHT ({int(self.get_progress() * 100)}%)"
        else:
            return "READY"
    
    def get_info(self) -> str:
        """Get detailed missile information"""
        info = [
            f"Type: {self.missile_type.name}",
            f"Owner: {self.owner}",
            f"Origin: {self.origin}",
            f"Target: {self.target}",
            f"Status: {self.get_status()}",
            f"Warheads: {self.missile_type.warheads}",
            f"Accuracy: {int(self.missile_type.accuracy * 100)}%",
        ]
        
        if self.launched and not self.detonated and not self.intercepted:
            info.append(f"Flight Time: {self.flight_time:.1f}s / {self.total_flight_time:.1f}s")
            info.append(f"Progress: {int(self.get_progress() * 100)}%")
        
        return '\n'.join(info)
    
    def __repr__(self):
        return f"Missile({self.missile_type.name}, {self.owner}, {self.get_status()})"


class MissileManager:
    """Manages all missiles in the game"""
    
    def __init__(self):
        self.missiles = []
        self.active_missiles = []
        self.detonated_missiles = []
        self.intercepted_missiles = []
        
    def create_missile(self, missile_type: MissileType, origin: Tuple[int, int],
                      target: Tuple[int, int], owner: str) -> Optional[Missile]:
        """Create a new missile"""
        missile = Missile(missile_type, origin, target, owner)
        
        if not missile.is_in_range():
            return None
        
        self.missiles.append(missile)
        return missile
    
    def launch_missile(self, missile: Missile):
        """Launch a missile"""
        if missile in self.missiles and not missile.launched:
            missile.launch()
            self.active_missiles.append(missile)
    
    def update_missiles(self, delta_time: float):
        """Update all active missiles"""
        still_active = []
        
        for missile in self.active_missiles:
            if missile.update(delta_time):
                still_active.append(missile)
            else:
                if missile.detonated:
                    self.detonated_missiles.append(missile)
                elif missile.intercepted:
                    self.intercepted_missiles.append(missile)
        
        self.active_missiles = still_active
    
    def intercept_missile(self, missile: Missile) -> bool:
        """Attempt to intercept a missile"""
        if missile in self.active_missiles:
            missile.intercept()
            self.active_missiles.remove(missile)
            self.intercepted_missiles.append(missile)
            return True
        return False
    
    def get_missiles_by_owner(self, owner: str) -> list:
        """Get all missiles owned by a player"""
        return [m for m in self.missiles if m.owner == owner]
    
    def get_active_missiles(self) -> list:
        """Get all missiles currently in flight"""
        return self.active_missiles.copy()
    
    def get_missiles_near_position(self, pos: Tuple[int, int], radius: float) -> list:
        """Get missiles near a position"""
        nearby = []
        for missile in self.active_missiles:
            current_pos = missile.get_position()
            dx = current_pos[0] - pos[0]
            dy = current_pos[1] - pos[1]
            distance = math.sqrt(dx * dx + dy * dy)
            if distance <= radius:
                nearby.append(missile)
        return nearby
    
    def get_statistics(self) -> Dict:
        """Get missile statistics"""
        return {
            'total_launched': len(self.missiles),
            'in_flight': len(self.active_missiles),
            'detonated': len(self.detonated_missiles),
            'intercepted': len(self.intercepted_missiles),
        }
    
    def clear(self):
        """Clear all missiles"""
        self.missiles.clear()
        self.active_missiles.clear()
        self.detonated_missiles.clear()
        self.intercepted_missiles.clear()
    
    def __repr__(self):
        return f"MissileManager(total={len(self.missiles)}, active={len(self.active_missiles)})"


def create_missile_types_from_config(config_types: Dict) -> Dict[str, MissileType]:
    """Create missile types from configuration"""
    missile_types = {}
    
    for type_name, config in config_types.items():
        missile_types[type_name] = MissileType(
            name=config['name'],
            range=config['range'],
            speed=config['speed'],
            warheads=config['warheads'],
            accuracy=config['accuracy'],
            cost=config['cost']
        )
    
    return missile_types


if __name__ == "__main__":
    # Test missile system
    icbm_type = MissileType("ICBM", 10000, 7.0, 10, 0.9, 5)
    
    missile = Missile(icbm_type, (10, 10), (50, 30), "USA")
    print(missile.get_info())
    
    missile.launch()
    print(f"\nLaunched! Status: {missile.get_status()}")
    
    # Simulate flight
    for i in range(5):
        missile.update(1.0)
        print(f"Update {i+1}: {missile.get_status()}, Position: {missile.get_position()}")

# Made with Bob
