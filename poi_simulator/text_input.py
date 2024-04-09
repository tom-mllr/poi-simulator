import pygame

from poi_simulator.utils import Coordinate, Colors
from typing import List


class TextInput:
    def __init__(
        self,
        pos: Coordinate,
        width,
        height,
        font_size=32,
        title = "",
        initial_text = "",
        callbacks_pre: List[callable] = None,
        callbacks_text: List[callable] = None,
        callbacks_post: List[callable] = None,
        input_type=None,
        max_length=None,
    ):
        self.rect = pygame.Rect(*pos.int_tuple(), width, height)
        self.font = pygame.font.Font(None, font_size)
        self.title = title
        self.active = False
        self.callbacks_pre = callbacks_pre if callbacks_pre is not None else []
        self.callbacks_text = callbacks_text if callbacks_text is not None else []
        self.callbacks_post = callbacks_post if callbacks_post is not None else []
        self.input_type = input_type
        self.max_length = max_length
        self.initial_text = initial_text
        self.text = self.initial_text
        self.update_text()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = True
            else:
                if self.active:
                    self.update_text()
                self.active = False
                
        elif event.type == pygame.KEYDOWN:
                if self.active:
                    if event.key in [pygame.K_RETURN, 1073741912]: # 1073741912 is the enter key on german keyboard
                        self.update_text()

                    elif event.key == pygame.K_BACKSPACE:
                        self.text = self.text[:-1]
                    else:
                        if self.input_type == int:
                            if event.unicode.isdigit() or (
                                event.unicode == "-" and len(self.text) == 0
                            ):
                                if (
                                    self.max_length is None
                                    or len(self.text.strip("-")) < self.max_length
                                ):
                                    self.text += event.unicode
                        elif self.input_type == float:
                            if event.unicode.isdigit() or event.unicode == ".":
                                if (
                                    self.max_length is None
                                    or len(self.text.strip("-").split(".")[0]) < self.max_length
                                ):
                                    self.text += event.unicode
                        else:
                            if self.max_length is None or len(self.text) < self.max_length:
                                self.text += event.unicode
    def update_text(self):
        if self.text=="":
            self.text = self.initial_text
        arg = None
        if self.input_type is not None:
            arg = self.input_type(self.text)

        for cb in self.callbacks_pre:
            cb()
        if arg is not None:
            for cb in self.callbacks_text:
                cb(arg)
        for cb in self.callbacks_post:
            cb()
            
    def draw(self, screen):
        pygame.draw.rect(screen, Colors.LIGHT_BLUE if self.active else Colors.WHITE, self.rect)
        text_surface = self.font.render(self.text, True, Colors.BLACK)
        screen.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
        
        title_surface = self.font.render(self.title, True, Colors.BLACK)
        title_rect = title_surface.get_rect()
        title_rect.topright = (self.rect.x - 10, self.rect.y + 5)
        screen.blit(title_surface, title_rect)
        
        pygame.draw.rect(screen, Colors.BLACK, self.rect, 2)

    def set_text(self, text):
        self.text = text
        self.update_text()
        