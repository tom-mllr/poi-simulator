from enum import Enum
from dataclasses import dataclass
from typing import Optional
from typing import Tuple, Optional

@dataclass
class Coordinate:
    x: int
    y: int
    
    def tuple(self):
        return (self.x, self.y)
    
    def int_tuple(self):
        return (self.x, self.y)
    
    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
class TimingDirection(Enum):
    TogetherSame = 0
    TogetherOpposite = 1
    SplitSame = 2
    SplitOpposite = 3
    

class Timing(Enum):
    Together = 0
    Split = 1
    def short_str(self):
        return "Tog" if self == Timing.Together else "Split"
    

class Direction(Enum):
    Same = 0
    Opposite = 1
    def short_str(self):
        return "Same" if self == Direction.Same else "Opp"

@dataclass
class TimDir:
    timing: Timing
    direction: Direction
    def short_str(self):
        return f"{self.timing.short_str()}/{self.direction.short_str()}"

    
t = TimDir(Timing.Together, Direction.Same)
    

# Color tuples for the most common colors
class Colors:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    LIGHT_BLUE = (0, 255, 255)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)
    

def get_orbit_timing_dir(l_orbit: 'Orbit', r_orbit: 'Orbit') -> TimingDirection:
    timdir = None
    if (l_orbit.speed_factor == r_orbit.speed_factor):
        if (l_orbit.angle_offset_factor - r_orbit.angle_offset_factor) % 2 == 0:
            timdir = TimingDirection.TogetherSame
        elif (l_orbit.angle_offset_factor - r_orbit.angle_offset_factor) % 2 == 1:
            timdir = TimingDirection.SplitSame
    elif (l_orbit.speed_factor == -r_orbit.speed_factor):
        if (l_orbit.angle_offset_factor + r_orbit.angle_offset_factor) % 2 == 0:
            timdir = TimingDirection.SplitOpposite
        elif (l_orbit.angle_offset_factor + r_orbit.angle_offset_factor) % 2 == 1:
            timdir = TimingDirection.TogetherOpposite
    return timdir
            
def get_poi_timing_dir(l_poi: 'Poi', r_poi: 'Poi') -> Tuple[TimingDirection, TimingDirection]:
    prop = get_orbit_timing_dir(l_poi.prop, r_poi.prop)
    arm = get_orbit_timing_dir(l_poi.arm, r_poi.arm)
    return prop, arm
