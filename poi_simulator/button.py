import pygame
from poi_simulator.utils import Coordinate, Colors
from typing import List
from poi_simulator.object import Object

class Button(Object):
    def __init__(
        self,
        pos: Coordinate,
        height: int = 40,
        width: int = 100,
        text="",
        callbacks: List[callable] = None,
    ):
        self.rect = pygame.Rect(pos.x, pos.y, 100, 40)
        self.font = pygame.font.Font(None, 32)
        self.active = False
        self.callbacks = callbacks if callbacks is not None else []
        self.set_text(text)

    def set_text(self, text):
        self.text = text
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                if self.callbacks is not None:
                    for cb in self.callbacks:
                        cb()
            else:
                self.active = False

    def draw(self, screen):
        pygame.draw.rect(screen, Colors.WHITE, self.rect)
        pygame.draw.rect(screen, Colors.BLACK, self.rect, 2)

        text_surface = self.font.render(self.text, True, Colors.BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        screen.blit(text_surface, text_rect)
