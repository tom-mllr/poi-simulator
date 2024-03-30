import pygame
from poi_simulator.utils import Coordinate, Colors
from typing import List


class TickBox:
    def __init__(
        self,
        pos: Coordinate,
        title="",
        initial_state=False,
        callbacks_pre: List[callable] = None,
        callbacks_value: List[callable] = None,
        callbacks_post: List[callable] = None,
    ):
        self.rect = pygame.Rect(pos.x, pos.y, 20, 20)
        self.font = pygame.font.Font(None, 32)
        self.title = title
        self.active = False
        self.callbacks_pre = callbacks_pre if callbacks_pre is not None else []
        self.callbacks_value = callbacks_value if callbacks_value is not None else []
        self.callbacks_post = callbacks_post if callbacks_post is not None else []
        self.checked = initial_state

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.checked = not self.checked
                if self.callbacks_pre is not None:
                    for cb in self.callbacks_pre:
                        cb()
                if self.callbacks_value is not None:
                    for cb in self.callbacks_value:
                        cb(self.checked)
                if self.callbacks_post is not None:
                    for cb in self.callbacks_post:
                        cb()
            else:
                self.active = False

    def draw(self, screen):
        pygame.draw.rect(screen, Colors.WHITE, self.rect)
        pygame.draw.rect(screen, Colors.BLACK, self.rect, 2)

        top_left = Coordinate(*self.rect.topleft) 
        top_right = Coordinate(*self.rect.topright) + Coordinate(-2, 0)
        bottom_left = Coordinate(*self.rect.bottomleft) + Coordinate(0, -2)
        bottom_right = Coordinate(*self.rect.bottomright) + Coordinate(-2, -2)
        
        if self.checked:
            pygame.draw.line(
                screen, Colors.BLACK, top_left.int_tuple(), bottom_right.int_tuple(), 2
            )
            pygame.draw.line(
                screen, Colors.BLACK, bottom_left.int_tuple(), top_right.int_tuple(), 2
            )

        title_surface = self.font.render(self.title, True, Colors.BLACK)
        title_rect = title_surface.get_rect()
        title_rect.topright = (self.rect.x - 10, self.rect.y)
        screen.blit(title_surface, title_rect)
