import pygame
from poi_simulator.utils import Coordinate, Colors
from typing import List


class DropDownList:
    def __init__(
        self,
        pos: Coordinate,
        width: int,
        options: List[str],
        initial_selection: int = 0,
        visible_options: int = 20,
        callbacks_pre: List[callable] = None,
        callbacks_index: List[callable] = None,
        callbacks_post: List[callable] = None,
    ):
        self.rect = pygame.Rect(pos.x, pos.y, width, 30)
        self.font = pygame.font.Font(None, 32)
        self.options = options
        self.selection = initial_selection
        self.active = False
        self.callbacks_pre = callbacks_pre if callbacks_pre is not None else []
        self.callbacks_index = callbacks_index if callbacks_index is not None else []
        self.callbacks_post = callbacks_post if callbacks_post is not None else []
        self.visible_options = visible_options
        self.scroll_index = 0

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.rect.collidepoint(event.pos):
                    self.active = not self.active
                elif self.active:
                    for i in range(self.visible_options):
                        option_rect = pygame.Rect(
                            self.rect.x,
                            self.rect.y + (i + 1) * self.rect.height,
                            self.rect.width,
                            self.rect.height,
                        )
                        if option_rect.collidepoint(event.pos):
                            self.selection = i + self.scroll_index
                            self.execute_callbacks(self.selection)
                            break

                    self.active = False
        elif event.type == pygame.MOUSEWHEEL:
            if self.active:
                if event.y > 0:  # scroll up
                    self.scroll_index = max(0, self.scroll_index - 1)
                else:  # scroll down
                    self.scroll_index = min(
                        len(self.options) - self.visible_options - 1,
                        self.scroll_index + 1,
                    )

    def draw(self, screen):
        pygame.draw.rect(screen, Colors.WHITE, self.rect)
        pygame.draw.rect(screen, Colors.BLACK, self.rect, 2)

        selected_option = self.options[self.selection]
        selected_surface = self.font.render(selected_option, True, Colors.BLACK)
        selected_rect = selected_surface.get_rect()
        selected_rect.topleft = (self.rect.x + 5, self.rect.y + 5)
        screen.blit(selected_surface, selected_rect)

        if self.active:

            # Draw the options
            for i, option in enumerate(
                self.options[
                    self.scroll_index : self.scroll_index + self.visible_options
                ]
            ):
                option_rect = pygame.Rect(
                    self.rect.x,
                    self.rect.y + (i + 1) * self.rect.height,
                    self.rect.width,
                    self.rect.height,
                )
                if self.scroll_index + i == self.selection:
                    color = Colors.LIGHT_BLUE
                else:
                    color = Colors.WHITE

                pygame.draw.rect(screen, color, option_rect)
                pygame.draw.rect(screen, Colors.BLACK, option_rect, 1)

                option_surface = self.font.render(option, True, Colors.BLACK)
                option_rect = option_surface.get_rect()
                option_rect.topleft = (
                    self.rect.x + 5,
                    self.rect.y + (i + 1) * self.rect.height + 5,
                )
                screen.blit(option_surface, option_rect)

            # Draw the scroll indicator
            total_height = self.rect.height * self.visible_options
            indicator_height = max(
                20, self.rect.height * self.visible_options**2 / len(self.options)
            )  
            max_scroll_index = len(self.options) - self.visible_options
            indicator_y = (
                3
                + self.rect.height
                + self.rect.y
                + (self.scroll_index / max(1, max_scroll_index))
                * (total_height - indicator_height)
            )

            indicator_rect = pygame.Rect(
                self.rect.right + 17,  # 7 pixels from the right edge
                indicator_y,
                10,  # width of the scroll indicator
                indicator_height,
            )
            pygame.draw.rect(screen, Colors.BLACK, indicator_rect)

            # Draw the indicator frame
            frame_rect = pygame.Rect(
                self.rect.right + 13,
                self.rect.y
                + self.rect.height,  # same y-coordinate as the top of the dropdown list
                18,
                total_height,  # total height of the visible options
            )
            pygame.draw.rect(
                screen, Colors.BLACK, frame_rect, 1
            )  # draw with a line width of 1 to make it an outline

    def execute_callbacks(self, index: int):
        for cb in self.callbacks_pre:
            cb()
        for cb in self.callbacks_index:
            cb(index)
        for cb in self.callbacks_post:
            cb()
