from enum import Enum
from dataclasses import dataclass

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

# Color tuples for the most common colors
class Colors:
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)