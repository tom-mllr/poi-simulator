import pygame
import math
from poi_simulator.poi import Poi
from poi_simulator.utils import Colors, TimingDirection, Coordinate, get_poi_timing_dir
from poi_simulator.radio_button import RadioButtonGroup
from poi_simulator.text_input import TextInput
import functools
from typing import List
from poi_simulator.object import Object
from poi_simulator.tickbox import TickBox
from poi_simulator.textbox import TextBox

from poi_simulator.slider import Slider
from poi_simulator.dropdown_list import DropDownList
from poi_simulator.button import Button
from poi_simulator.poi_moves import poi_moves



class PoiSimulator:
    def __init__(self):

        self.tick = 100
        self.paused = False

        # Initialize Pygame
        pygame.init()

        # Set up the self.screen
        self.screen_width = 1920
        self.screen_height = 1000
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Poi Simulator")

        # Colors
        self.clock = pygame.time.Clock()

        # Instances
        self.r_poi = Poi(
            self,
            Colors.BLUE,
            Coordinate(self.screen_width // 2 + 50, self.screen_height // 2),
        )
        self.l_poi = Poi(
            self,
            Colors.RED,
            Coordinate(self.screen_width // 2 - 50, self.screen_height // 2),
        )

        self.l_prop_speed_text_input = TextInput(
            Coordinate(200, 100),
            40,
            32,
            title="Prop Speed",
            initial_text=str(self.l_poi.prop.speed_factor),
            input_type=int,
            max_length=2,
            callbacks_pre=[self.l_poi.reset, self.r_poi.reset],
            callbacks_text=[self.l_poi.prop.set_speed_factor],
        )

        self.l_prop_offset_text_input = TextInput(
            Coordinate(200, 150),
            40,
            32,
            title="Prop Offset",
            initial_text=str(self.l_poi.prop.angle_offset_factor),
            input_type=float,
            max_length=4,
            callbacks_pre=[self.l_poi.reset, self.r_poi.reset],
            callbacks_text=[self.l_poi.prop.set_angle_offset],
        )

        self.l_arm_speed_text_input = TextInput(
            Coordinate(200, 200),
            40,
            32,
            title="Arm Speed",
            initial_text=str(self.l_poi.arm.speed_factor),
            input_type=int,
            max_length=2,
            callbacks_pre=[self.l_poi.reset, self.r_poi.reset],
            callbacks_text=[self.l_poi.arm.set_speed_factor],
        )

        self.l_arm_offset_text_input = TextInput(
            Coordinate(200, 250),
            40,
            32,
            title="Arm Offset",
            initial_text=str(self.l_poi.arm.angle_offset_factor),
            input_type=float,
            max_length=4,
            callbacks_pre=[self.l_poi.reset, self.r_poi.reset],
            callbacks_text=[self.l_poi.arm.set_angle_offset],
        )

        self.r_prop_speed_text_input = TextInput(
            Coordinate(self.screen_width - 125, 100),
            40,
            32,
            title="Prop Speed",
            initial_text=str(self.l_poi.prop.speed_factor),
            input_type=int,
            max_length=2,
            callbacks_pre=[self.l_poi.reset, self.r_poi.reset],
            callbacks_text=[self.r_poi.prop.set_speed_factor],
        )

        self.r_prop_offset_text_input = TextInput(
            Coordinate(self.screen_width - 125, 150),
            40,
            32,
            title="Prop Offset",
            initial_text=str(self.r_poi.prop.angle_offset_factor),
            input_type=float,
            max_length=4,
            callbacks_pre=[self.l_poi.reset, self.r_poi.reset],
            callbacks_text=[self.r_poi.prop.set_angle_offset],
        )

        self.r_arm_speed_text_input = TextInput(
            Coordinate(self.screen_width - 125, 200),
            40,
            32,
            title="Arm Speed",
            initial_text=str(self.r_poi.arm.speed_factor),
            input_type=int,
            max_length=2,
            callbacks_pre=[self.l_poi.reset, self.r_poi.reset],
            callbacks_text=[self.r_poi.arm.set_speed_factor],
        )

        self.r_arm_offset_text_input = TextInput(
            Coordinate(self.screen_width - 125, 250),
            40,
            32,
            title="Arm Offset",
            initial_text=str(self.r_poi.arm.angle_offset_factor),
            input_type=float,
            max_length=4,
            callbacks_pre=[self.l_poi.reset, self.r_poi.reset],
            callbacks_text=[self.r_poi.arm.set_angle_offset],
        )

        self.prop_timdir_textbox = TextBox(
            Coordinate(100, 800),
            100,
            32,
            text_static="Prop: ",
        )

        self.arm_timdir_textbox = TextBox(
            Coordinate(100, 850),
            100,
            32,
            text_static="Arm: ",
        )

        pause_button = Button(
            Coordinate(self.screen_width - 150, self.screen_height - 120), text="Pause"
        )
        pause_button.callbacks.append(lambda: self.set_paused(not self.is_paused()))
        pause_button.callbacks.append(
            lambda: (
                pause_button.set_text("Resume")
                if self.paused
                else pause_button.set_text("Pause")
            )
        )

        self.objects: List[Object] = [
            self.l_poi,
            self.r_poi,
            # Text Inputs
            self.r_prop_speed_text_input,
            self.r_prop_offset_text_input,
            self.r_arm_speed_text_input,
            self.r_arm_offset_text_input,
            self.l_prop_speed_text_input,
            self.l_prop_offset_text_input,
            self.l_arm_speed_text_input,
            self.l_arm_offset_text_input,
            # Tickboxes
            TickBox(
                Coordinate(200, 300),
                title="Trail",
                initial_state=True,
                callbacks_value=[self.l_poi.set_trail],
            ),
            TickBox(
                Coordinate(200, 350),
                title="Enabled",
                initial_state=True,
                callbacks_value=[self.l_poi.set_enabled],
            ),
            TickBox(
                Coordinate(self.screen_width - 125, 300),
                title="Trail",
                initial_state=True,
                callbacks_value=[self.r_poi.set_trail],
            ),
            TickBox(
                Coordinate(self.screen_width - 125, 350),
                title="Enabled",
                initial_state=True,
                callbacks_value=[self.r_poi.set_enabled],
            ),
            # Textboxes
            #  Timing Direction Props
            self.prop_timdir_textbox,
            self.arm_timdir_textbox,
            TextBox(
                Coordinate(105, 50), 100, 32, text_static="Left Poi", color=Colors.RED
            ),
            TextBox(
                Coordinate(self.screen_width-235, 50),
                100,
                32,
                text_static="Right Poi",
                color=Colors.BLUE,
            ),
            TextBox(
                Coordinate(245, 150),
                100,
                32,
                text_static="\u03C0",
            ),
            TextBox(
                Coordinate(245, 250),
                100,
                32,
                text_static="\u03C0",
            ),
            TextBox(
                Coordinate(self.screen_width - 80, 150),
                100,
                32,
                text_static="\u03C0",
            ),
            TextBox(
                Coordinate(self.screen_width - 80, 250),
                100,
                32,
                text_static="\u03C0",
            ),
            Slider(
                Coordinate(self.screen_width - 400, self.screen_height - 100),
                0,
                10,
                1.0,
                format_string="Base speed: {value:.2f} \u03C0/s",
                callbacks_value=[
                    self.l_poi.set_unit_speed_pi_per_sec,
                    self.r_poi.set_unit_speed_pi_per_sec,
                ],
            ),
            DropDownList(
                Coordinate(self.screen_width//2-450, 50),
                890,
                [move.name for move in poi_moves],
                callbacks_pre=[self.r_poi.reset, self.l_poi.reset],
                callbacks_index=[self.set_move],
                visible_options=27
            ),
            pause_button,
            Button(
                Coordinate(150, 700),
                text="Invert",
                callbacks=[self.invert_move],
            )
        ]

        self.run()

    def is_paused(self):
        return self.paused

    def set_paused(self, paused: bool):
        self.paused = paused

    def set_move(self, index):
        move = poi_moves[index]

        self.l_poi.arm.set_speed_factor(move.l_arm_speed_factor)
        self.l_poi.arm.set_angle_offset(move.l_arm_angle_offset)
        self.l_poi.prop.set_speed_factor(move.l_prop_speed_factor)
        self.l_poi.prop.set_angle_offset(move.l_prop_angle_offset)
        self.r_poi.arm.set_speed_factor(move.r_arm_speed_factor)
        self.r_poi.arm.set_angle_offset(move.r_arm_angle_offset)
        self.r_poi.prop.set_speed_factor(move.r_prop_speed_factor)
        self.r_poi.prop.set_angle_offset(move.r_prop_angle_offset)

        self.l_arm_speed_text_input.set_text(str(move.l_arm_speed_factor))
        self.l_arm_offset_text_input.set_text(str(move.l_arm_angle_offset))
        self.l_prop_speed_text_input.set_text(str(move.l_prop_speed_factor))
        self.l_prop_offset_text_input.set_text(str(move.l_prop_angle_offset))
        self.r_arm_speed_text_input.set_text(str(move.r_arm_speed_factor))
        self.r_arm_offset_text_input.set_text(str(move.r_arm_angle_offset))
        self.r_prop_speed_text_input.set_text(str(move.r_prop_speed_factor))
        self.r_prop_offset_text_input.set_text(str(move.r_prop_angle_offset))

    def invert_move(self):
        self.l_arm_speed_text_input.set_text(str(-self.l_poi.arm.speed_factor))
        self.l_prop_speed_text_input.set_text(str(-self.l_poi.prop.speed_factor))
        self.r_arm_speed_text_input.set_text(str(-self.r_poi.arm.speed_factor))
        self.r_prop_speed_text_input.set_text(str(-self.r_poi.prop.speed_factor))
        
    def run(self):
        # Main loop
        running = True
        while running:
            self.screen.fill(Colors.WHITE)

            self.r_poi.perform_movement()
            self.l_poi.perform_movement()

            for obj in self.objects:
                obj.draw(self.screen)

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                for obj in self.objects:
                    obj.handle_event(event)
            timdir_prop, timdir_arm = get_poi_timing_dir(self.l_poi, self.r_poi)
            self.prop_timdir_textbox.set_text_dynamic(
                f"{timdir_prop.name}" if timdir_prop is not None else ""
            )
            self.arm_timdir_textbox.set_text_dynamic(
                f"{timdir_arm.name}" if timdir_arm is not None else ""
            )
            pygame.display.flip()
            self.clock.tick(self.tick)

        pygame.quit()


def main():
    PoiSimulator()


if __name__ == "__main__":
    main()
