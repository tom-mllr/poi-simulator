import pygame

from poi_simulator.utils import Coordinate, Colors
from typing import List
from poi_simulator.object import Object


class TextBox(Object):
    def __init__(
        self,
        pos: Coordinate,
        width,
        height,
        text_static = "",
        color = Colors.BLACK
    ):
        self.rect = pygame.Rect(*pos.int_tuple(), width, height)
        self.font = pygame.font.Font(None, 32)
        self.text_static = text_static
        self.text_dynamic = ""
        self.color = color

    def draw(self, screen):
        text_surface = self.font.render(self.text_static + self.text_dynamic, True, self.color)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        
    def set_text_dynamic(self, text):
        self.text_dynamic = text