import pygame
from poi_simulator.utils import Coordinate, Colors
from typing import List


class Slider:
    def __init__(
        self,
        pos: Coordinate,
        min_value: float,
        max_value: float,
        initial_value: float = None,
        format_string: str = "{value:.2f}",
        callbacks_pre: List[callable] = None,
        callbacks_value: List[callable] = None,
        callbacks_post: List[callable] = None,
    ):
        self.rect = pygame.Rect(pos.x, pos.y, 200, 20)
        self.font = pygame.font.Font(None, 32)
        self.min_value = min_value
        self.max_value = max_value
        self.value = initial_value
        if self.value < self.min_value or self.value > self.max_value:
            raise ValueError("Initial value is not within the specified range")
        
        self.format_string = format_string#.replace("value", "self.value")

        self.slider_rect_y_offset = -5
        self.slider_rect = pygame.Rect(0, self.slider_rect_y_offset, 15, 30)
        
        self.callbacks_pre = callbacks_pre if callbacks_pre is not None else []
        self.callbacks_value = callbacks_value if callbacks_value is not None else []
        self.callbacks_post = callbacks_post if callbacks_post is not None else []
        self.dragging = False
        self.active = False
        
        self.set_slider() 
                
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.dragging = True
                self.move_slider(event)
                self.active = True
            else:
                self.active = False
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging:
                self.move_slider(event)
        elif event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_LEFT:
                    self.value -= (self.max_value - self.min_value) / 200
                    self.value = max(self.min_value, self.value)
                    self.update_slider((self.value - self.min_value) / (self.max_value - self.min_value))
                elif event.key == pygame.K_RIGHT:
                    self.value += (self.max_value - self.min_value) / 200
                    self.value = min(self.max_value, self.value)
                    self.update_slider((self.value - self.min_value) / (self.max_value - self.min_value))
                
    def move_slider(self, event):
        mouse_x = event.pos[0]
        normalized_x = (mouse_x - self.rect.x) / self.rect.width
        # Clamp the value of normalized_x between 0 and 1
        normalized_x = max(0, min(1, normalized_x))
        self.value = self.min_value + normalized_x * (self.max_value - self.min_value)
        self.update_slider(normalized_x)

    
    def set_slider(self):
        normalized_x = self.value / (self.max_value - self.min_value)
        self.update_slider(normalized_x)
        
    def update_slider(self, normalized_x: float):
        self.slider_rect.x = self.rect.x + normalized_x * self.rect.width - self.slider_rect.width / 2
        self.slider_rect.y = self.rect.y + self.slider_rect_y_offset
        self.execute_callbacks(self.value)

    
    def execute_callbacks(self, value):
        if self.callbacks_pre is not None:
            for cb in self.callbacks_pre:
                cb()
        if self.callbacks_value is not None:
            for cb in self.callbacks_value:
                cb(value)
        if self.callbacks_post is not None:
            for cb in self.callbacks_post:
                cb()

    def draw(self, screen):
        pygame.draw.rect(screen, Colors.WHITE, self.rect)
        pygame.draw.rect(screen, Colors.BLACK, self.rect, 2)
        slider_width = int(
            (self.value - self.min_value)
            / (self.max_value - self.min_value)
            * self.rect.width
        )
        slider_rect = pygame.Rect(
            self.rect.x, self.rect.y, slider_width, self.rect.height
        )
        pygame.draw.rect(screen, Colors.LIGHT_BLUE, slider_rect)
        pygame.draw.rect(screen, Colors.BLACK, self.slider_rect)
        
        value_text = self.format_string.format(value=self.value)
        value_surface = self.font.render(value_text, True, Colors.BLACK)
        value_rect = value_surface.get_rect()
        value_rect.center = (self.rect.center[0], self.rect.center[1] - 40)
        screen.blit(value_surface, value_rect)
