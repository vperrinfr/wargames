"""
Global Thermal Nuclear War - Animations
Terminal animations for missiles, explosions, and effects
"""

import time
import sys
from typing import Tuple, List


class Animation:
    """Base animation class"""
    
    def __init__(self, frames: List[str], duration: float = 1.0):
        self.frames = frames
        self.duration = duration
        self.frame_duration = duration / len(frames) if frames else 0
        self.current_frame = 0
        self.elapsed_time = 0.0
        self.finished = False
        
    def update(self, delta_time: float) -> str:
        """Update animation and return current frame"""
        if self.finished:
            return self.frames[-1] if self.frames else ""
        
        self.elapsed_time += delta_time
        
        if self.elapsed_time >= self.duration:
            self.finished = True
            return self.frames[-1] if self.frames else ""
        
        # Calculate current frame
        self.current_frame = int(self.elapsed_time / self.frame_duration)
        self.current_frame = min(self.current_frame, len(self.frames) - 1)
        
        return self.frames[self.current_frame]
    
    def reset(self):
        """Reset animation to beginning"""
        self.current_frame = 0
        self.elapsed_time = 0.0
        self.finished = False


class MissileAnimation(Animation):
    """Animation for missile launch and flight"""
    
    def __init__(self, start_pos: Tuple[int, int], end_pos: Tuple[int, int], 
                 duration: float = 2.0):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.current_pos = start_pos
        
        # Create trajectory frames
        frames = self._create_trajectory_frames()
        super().__init__(frames, duration)
        
    def _create_trajectory_frames(self) -> List[str]:
        """Create frames showing missile trajectory"""
        frames = [
            "    |    ",
            "   /|\\   ",
            "  / | \\  ",
            " /  |  \\ ",
            "/   |   \\",
            "    *    ",
        ]
        return frames
    
    def get_position(self, progress: float) -> Tuple[int, int]:
        """Get missile position at given progress (0.0 to 1.0)"""
        x = int(self.start_pos[0] + (self.end_pos[0] - self.start_pos[0]) * progress)
        y = int(self.start_pos[1] + (self.end_pos[1] - self.start_pos[1]) * progress)
        return (x, y)


class ExplosionAnimation(Animation):
    """Animation for explosions"""
    
    def __init__(self, position: Tuple[int, int], size: str = 'normal'):
        self.position = position
        
        if size == 'small':
            frames = ["*", "☼", "·"]
            duration = 0.5
        elif size == 'large':
            frames = [
                "    *    ",
                "   ***   ",
                "  *****  ",
                " ******* ",
                "*********",
                " ☼☼☼☼☼☼☼ ",
                "  ☼☼☼☼☼  ",
                "   ☼☼☼   ",
                "    ☼    ",
                "    ·    ",
            ]
            duration = 2.0
        else:  # normal
            frames = [
                "  *  ",
                " *** ",
                "*****",
                " ☼☼☼ ",
                "  ☼  ",
                "  ·  ",
            ]
            duration = 1.0
        
        super().__init__(frames, duration)


class RadarAnimation(Animation):
    """Rotating radar sweep animation"""
    
    def __init__(self):
        frames = [
            "◜", "◝", "◞", "◟"
        ]
        super().__init__(frames, 1.0)
        self.loop = True
    
    def update(self, delta_time: float) -> str:
        """Update with looping"""
        result = super().update(delta_time)
        if self.finished and self.loop:
            self.reset()
        return result


class TypingAnimation:
    """Simulates typing text character by character"""
    
    def __init__(self, text: str, chars_per_second: float = 20.0):
        self.text = text
        self.chars_per_second = chars_per_second
        self.current_index = 0
        self.elapsed_time = 0.0
        self.finished = False
        
    def update(self, delta_time: float) -> str:
        """Update and return current text"""
        if self.finished:
            return self.text
        
        self.elapsed_time += delta_time
        chars_to_show = int(self.elapsed_time * self.chars_per_second)
        
        if chars_to_show >= len(self.text):
            self.finished = True
            return self.text
        
        return self.text[:chars_to_show]
    
    def reset(self):
        """Reset animation"""
        self.current_index = 0
        self.elapsed_time = 0.0
        self.finished = False


class LoadingBarAnimation:
    """Animated loading bar"""
    
    def __init__(self, width: int = 40, duration: float = 3.0):
        self.width = width
        self.duration = duration
        self.elapsed_time = 0.0
        self.finished = False
        
    def update(self, delta_time: float) -> str:
        """Update and return loading bar"""
        if self.finished:
            return self._create_bar(100)
        
        self.elapsed_time += delta_time
        
        if self.elapsed_time >= self.duration:
            self.finished = True
            return self._create_bar(100)
        
        progress = int((self.elapsed_time / self.duration) * 100)
        return self._create_bar(progress)
    
    def _create_bar(self, progress: int) -> str:
        """Create loading bar string"""
        filled = int(self.width * progress / 100)
        bar = '█' * filled + '░' * (self.width - filled)
        return f"[{bar}] {progress}%"
    
    def reset(self):
        """Reset animation"""
        self.elapsed_time = 0.0
        self.finished = False


class CountdownAnimation:
    """Countdown timer animation"""
    
    def __init__(self, start_value: int):
        self.start_value = start_value
        self.current_value = start_value
        self.elapsed_time = 0.0
        self.finished = False
        
    def update(self, delta_time: float) -> str:
        """Update and return countdown"""
        if self.finished:
            return "0"
        
        self.elapsed_time += delta_time
        self.current_value = max(0, self.start_value - int(self.elapsed_time))
        
        if self.current_value <= 0:
            self.finished = True
            return "0"
        
        return str(self.current_value)
    
    def reset(self):
        """Reset countdown"""
        self.current_value = self.start_value
        self.elapsed_time = 0.0
        self.finished = False


class BlinkingText:
    """Text that blinks on and off"""
    
    def __init__(self, text: str, blink_rate: float = 0.5):
        self.text = text
        self.blink_rate = blink_rate
        self.elapsed_time = 0.0
        self.visible = True
        
    def update(self, delta_time: float) -> str:
        """Update and return text (or empty if blinking off)"""
        self.elapsed_time += delta_time
        
        # Toggle visibility at blink rate
        blinks = int(self.elapsed_time / self.blink_rate)
        self.visible = (blinks % 2) == 0
        
        return self.text if self.visible else " " * len(self.text)


class AnimationManager:
    """Manages multiple animations"""
    
    def __init__(self):
        self.animations = {}
        
    def add_animation(self, name: str, animation):
        """Add an animation"""
        self.animations[name] = animation
        
    def remove_animation(self, name: str):
        """Remove an animation"""
        if name in self.animations:
            del self.animations[name]
            
    def update_all(self, delta_time: float) -> dict:
        """Update all animations and return results"""
        results = {}
        finished = []
        
        for name, animation in self.animations.items():
            results[name] = animation.update(delta_time)
            if hasattr(animation, 'finished') and animation.finished:
                finished.append(name)
        
        # Remove finished animations
        for name in finished:
            if not hasattr(self.animations[name], 'loop') or not self.animations[name].loop:
                del self.animations[name]
        
        return results
    
    def clear(self):
        """Clear all animations"""
        self.animations.clear()


if __name__ == "__main__":
    # Test animations
    print("Testing animations...")
    
    # Test typing animation
    typing = TypingAnimation("GREETINGS PROFESSOR FALKEN.", 30)
    for i in range(50):
        text = typing.update(0.05)
        print(f"\r{text}", end='', flush=True)
        time.sleep(0.05)
    
    print("\n\nTesting explosion animation...")
    explosion = ExplosionAnimation((10, 10), 'normal')
    for i in range(20):
        frame = explosion.update(0.1)
        print(f"\r{frame}", end='', flush=True)
        time.sleep(0.1)
    
    print("\n\nAnimations test complete!")

# Made with Bob
