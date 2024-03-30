import pygame
from poi_simulator.utils import Coordinate

class Object:
    def __init__(self, pos: Coordinate):
        self.pos = pos
        
    def draw(self, screen):
        pass
    
    def handle_event(self, event):
        pass