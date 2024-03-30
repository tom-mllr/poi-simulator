import pygame
from poi_simulator.utils import Colors, Coordinate
import pygame.font
import logging

class RadioButtonGroup:
    element_spacing = 50
    def __init__(self, position: Coordinate, screen, title: str=None) -> None:
        self.offset = 0
        self.position = position
        self.screen = screen
        self.radio_buttons = []
        self.font = pygame.font.Font(None, 36)
        self.title = None
        if title:
            self.set_title(title)

    def set_title(self, title: str):
        if self.title is not None:
            logging.error("Title already set")
            return
        self.title = title
        self.offset += self.element_spacing
        self.title_surface = self.font.render(title, True, Colors.BLACK)
        self.title_rect = self.title_surface.get_rect(bottomleft =(self.position + Coordinate(-10, self.offset)).int_tuple())

        
    def add_radio_button(self, text: str, callback=None):
        self.offset += self.element_spacing        
        self.radio_buttons.append(
            RadioButton(
                self.position + Coordinate(0, self.offset),
                text,
                self.screen,
                callback,
            )
        )

    def draw(self):
        if self.title:
            self.screen.blit(self.title_surface, self.title_rect)
        for radio_button in self.radio_buttons:
            radio_button.draw()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for radio_button in self.radio_buttons:
                radio_button.handle_event()
            self.evaluate_buttons()
        
    
    def evaluate_buttons(self):
        for radio_button in self.radio_buttons:
            if radio_button.selected_new:
                self.unselect_other(radio_button)
                if hasattr(radio_button, "callback"):
                    radio_button.callback()
            radio_button.selected_new = False   
    
    def unselect_other(self, radio_button):
        for other_radio_button in self.radio_buttons:
            if radio_button != other_radio_button:
                other_radio_button.selected = False
    
    def get_button(self, text):
        for radio_button in self.radio_buttons:
            if radio_button.text == text:
                return radio_button
        return None
    
    def set_selected(self, text):
        button = self.get_button(text)
        if button is not None:
            button.select()
            self.evaluate_buttons()
                
# Radio Button class
class RadioButton:
    def __init__(self, position: Coordinate, text, screen, callback=None):
        self.position = position
        self.text = text
        self.selected = False
        self.selected_new = False
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        if callback is not None:
            self.callback = callback

    def draw(self):
        pygame.draw.circle(
            self.screen,
            Colors.BLACK if self.selected else Colors.GRAY,
            self.position.int_tuple(),
            10,
        )
        text_surface = self.font.render(self.text, True, Colors.BLACK)
        self.screen.blit(
            text_surface, (self.position + Coordinate(20, -10)).int_tuple()
        )

    def handle_event(self):
            mouse_pos = pygame.mouse.get_pos()
            if (
                self.position.x - 10 <= mouse_pos[0] <= self.position.x + 10
                and self.position.y - 10 <= mouse_pos[1] <= self.position.y + 10
            ):
                self.select()
                


    def select(self):
        self.selected_new = True if not self.selected else False
        self.selected = True