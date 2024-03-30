import pygame
import math
from poi_simulator.poi import Poi
from poi_simulator.utils import Colors, TimingDirection, Coordinate
from poi_simulator.radio_button import RadioButtonGroup
from poi_simulator.text_input import TextInput
import functools
from typing import List
from poi_simulator.object import Object
from poi_simulator.tickbox import TickBox
from poi_simulator.textbox import TextBox



def set_prop_timing(timing_dir: TimingDirection, r_poi: Poi, l_poi: Poi):

    r_poi.reset()
    l_poi.reset()

    if timing_dir == TimingDirection.TogetherSame:
        r_poi.prop.speed_factor = 3
        l_poi.prop.speed_factor = 3
        r_poi.prop.angle_offset_factor = 0
        l_poi.prop.angle_offset_factor = 0
    elif timing_dir == TimingDirection.TogetherOpposite:
        r_poi.prop.speed_factor = -3
        l_poi.prop.speed_factor = 3
        r_poi.prop.angle_offset_factor = 0
        l_poi.prop.angle_offset_factor = math.pi
    elif timing_dir == TimingDirection.SplitSame:
        r_poi.prop.speed_factor = 3
        l_poi.prop.speed_factor = 3
        r_poi.prop.angle_offset_factor = 0
        l_poi.prop.angle_offset_factor = math.pi
    elif timing_dir == TimingDirection.SplitOpposite:
        r_poi.prop.speed_factor = -3
        l_poi.prop.speed_factor = 3
        r_poi.prop.angle_offset_factor = 0
        l_poi.prop.angle_offset_factor = 0


def set_arm_timing(timing_dir: TimingDirection, r_poi, l_poi):
    l_poi.reset()
    r_poi.reset()

    if timing_dir == TimingDirection.TogetherSame:
        r_poi.arm.speed_factor = 1
        l_poi.arm.speed_factor = 1
        r_poi.arm.angle_offset_factor = 0
        l_poi.arm.angle_offset_factor = 0
    elif timing_dir == TimingDirection.TogetherOpposite:
        r_poi.arm.speed_factor = -1
        l_poi.arm.speed_factor = 1
        r_poi.arm.angle_offset_factor = 0
        l_poi.arm.angle_offset_factor = math.pi
    elif timing_dir == TimingDirection.SplitSame:
        r_poi.arm.speed_factor = 1
        l_poi.arm.speed_factor = 1
        r_poi.arm.angle_offset_factor = 0
        l_poi.arm.angle_offset_factor = math.pi
    elif timing_dir == TimingDirection.SplitOpposite:
        r_poi.arm.speed_factor = -1
        l_poi.arm.speed_factor = 1
        r_poi.arm.angle_offset_factor = 0
        l_poi.arm.angle_offset_factor = 0


def get_timing_dir(l_poi, r_poi):
    prop: TimingDirection = None
    arm: TimingDirection = None

    if (
        l_poi.prop.speed_factor == r_poi.prop.speed_factor
        and l_poi.prop.angle_offset_factor == r_poi.prop.angle_offset_factor
    ):
        prop = TimingDirection.TogetherSame
    elif (
        l_poi.prop.speed_factor == -r_poi.prop.speed_factor
        and l_poi.prop.angle_offset_factor != r_poi.prop.angle_offset_factor
    ):
        prop = TimingDirection.TogetherOpposite
    elif (
        l_poi.prop.speed_factor == r_poi.prop.speed_factor
        and l_poi.prop.angle_offset_factor != r_poi.prop.angle_offset_factor
    ):
        prop = TimingDirection.SplitSame
    elif (
        l_poi.prop.speed_factor == -r_poi.prop.speed_factor
        and l_poi.prop.angle_offset_factor == r_poi.prop.angle_offset_factor
    ):
        prop = TimingDirection.SplitOpposite

    if (
        l_poi.arm.speed_factor == r_poi.arm.speed_factor
        and l_poi.arm.angle_offset_factor == r_poi.arm.angle_offset_factor
    ):
        arm = TimingDirection.TogetherSame
    elif (
        l_poi.arm.speed_factor == -r_poi.arm.speed_factor
        and l_poi.arm.angle_offset_factor != r_poi.arm.angle_offset_factor
    ):
        arm = TimingDirection.TogetherOpposite
    elif (
        l_poi.arm.speed_factor == r_poi.arm.speed_factor
        and l_poi.arm.angle_offset_factor != r_poi.arm.angle_offset_factor
    ):
        arm = TimingDirection.SplitSame
    elif (
        l_poi.arm.speed_factor == -r_poi.arm.speed_factor
        and l_poi.arm.angle_offset_factor == r_poi.arm.angle_offset_factor
    ):
        arm = TimingDirection.SplitOpposite

    return prop, arm



class PoiSimulator:
    def __init__(self):
        
        tick = 250

        # Initialize Pygame
        pygame.init()

        # Set up the screen
        screen_width = 1600
        screen_height = 900
        screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Poi Simulator")

        # Colors
        clock = pygame.time.Clock()

        # Instances
        r_poi = Poi(Colors.BLUE, Coordinate(screen_width // 2, screen_height // 2), tick)
        l_poi = Poi(Colors.RED, Coordinate(screen_width // 2 + 20, screen_height // 2), tick)

        # # Create radio buttons
        # prop_btn_group = radio_button.RadioButtonGroup(
        #     Coordinate(100, 100), screen, title="Prop Timing/Direction"
        # )
        # for tim_dir in TimingDirection:
        #     prop_btn_group.add_radio_button(
        #         tim_dir.name, functools.partial(set_prop_timing, tim_dir, r_poi, l_poi)
        #     )
        # prop_btn_group.set_selected(TimingDirection.TogetherSame.name)

        # arm_btn_group = radio_button.RadioButtonGroup(
        #     Coordinate(100, 500), screen, title="Arms Timing/Direction"
        # )
        # for tim_dir in TimingDirection:
        #     arm_btn_group.add_radio_button(
        #         tim_dir.name, functools.partial(set_arm_timing, tim_dir, r_poi, l_poi)
        #     )
        # arm_btn_group.set_selected(TimingDirection.TogetherSame.name)

        l_prop_speed_text_input = TextInput(
            Coordinate(200, 100),
            40,
            32,
            title="Prop Speed",
            initial_text=str(l_poi.prop.speed_factor),
            input_type=int,
            max_length=2,
            callbacks_pre=[l_poi.reset, r_poi.reset],
            callbacks_text=[l_poi.prop.set_speed_factor],
        )

        l_prop_offset_text_input = TextInput(
            Coordinate(200, 150),
            40,
            32,
            title="Prop Offset",
            initial_text=str(l_poi.prop.angle_offset_factor),
            input_type=float,
            max_length=4,
            callbacks_pre=[l_poi.reset, r_poi.reset],
            callbacks_text=[l_poi.prop.set_angle_offset],
        )

        l_arm_speed_text_input = TextInput(
            Coordinate(200, 200),
            40,
            32,
            title="Arm Speed",
            initial_text=str(l_poi.arm.speed_factor),
            input_type=int,
            max_length=2,
            callbacks_pre=[l_poi.reset, r_poi.reset],
            callbacks_text=[l_poi.arm.set_speed_factor],
        )

        l_arm_offset_text_input = TextInput(
            Coordinate(200, 250),
            40,
            32,
            title="Arm Offset",
            initial_text=str(l_poi.arm.angle_offset_factor),
            input_type=float,
            max_length=4,
            callbacks_pre=[l_poi.reset, r_poi.reset],
            callbacks_text=[l_poi.arm.set_angle_offset],
        )


        r_prop_speed_text_input = TextInput(
            Coordinate(screen_width - 200, 100),
            40,
            32,
            title="Prop Speed",
            initial_text=str(l_poi.prop.speed_factor),
            input_type=int,
            max_length=2,
            callbacks_pre=[l_poi.reset, r_poi.reset],
            callbacks_text=[r_poi.prop.set_speed_factor],
        )

        r_prop_offset_text_input = TextInput(
            Coordinate(screen_width - 200, 150),
            40,
            32,
            title="Prop Offset",
            initial_text=str(r_poi.prop.angle_offset_factor),
            input_type=float,
            max_length=4,
            callbacks_pre=[l_poi.reset, r_poi.reset],
            callbacks_text=[r_poi.prop.set_angle_offset],
        )

        r_arm_speed_text_input = TextInput(
            Coordinate(screen_width - 200, 200),
            40,
            32,
            title="Arm Speed",
            initial_text=str(r_poi.arm.speed_factor),
            input_type=int,
            max_length=2,
            callbacks_pre=[l_poi.reset, r_poi.reset],
            callbacks_text=[r_poi.arm.set_speed_factor],
        )

        r_arm_offset_text_input = TextInput(
            Coordinate(screen_width - 200, 250),
            40,
            32,
            title="Arm Offset",
            initial_text=str(r_poi.arm.angle_offset_factor),
            input_type=float,
            max_length=4,
            callbacks_pre=[l_poi.reset, r_poi.reset],
            callbacks_text=[r_poi.prop.set_angle_offset],
        )

        prop_timdir_textbox = TextBox(
            Coordinate(100, 800),
            100,
            32,
            text_static="Prop: ",
        )

        arm_timdir_textbox = TextBox(
            Coordinate(100, 850),
            100,
            32,
            text_static="Arm: ",
        )


        objects: List[Object] = [
            l_poi,
            r_poi,
            # Text Inputs
            r_prop_speed_text_input,
            r_prop_offset_text_input,
            r_arm_speed_text_input,
            r_arm_offset_text_input,
            l_prop_speed_text_input,
            l_prop_offset_text_input,
            l_arm_speed_text_input,
            l_arm_offset_text_input,
            # Tickboxes
            TickBox(
                Coordinate(200, 300),
                title="Trail",
                callbacks_value=[l_poi.set_trail],
            ),
            TickBox(
                Coordinate(200, 350),
                title="Enabled",
                initial_state=True,
                callbacks_value=[l_poi.set_enabled],
            ),
            TickBox(
                Coordinate(screen_width - 200, 300),
                title="Trail",
                callbacks_value=[r_poi.set_trail],
            ),
            TickBox(
                Coordinate(screen_width - 200, 350),
                title="Enabled",
                initial_state=True,
                callbacks_value=[r_poi.set_enabled],
            ),
            # Textboxes
            #  Timing Direction Props
            prop_timdir_textbox,
            arm_timdir_textbox,
            TextBox(Coordinate(105, 50), 100, 32, text_static="Left Poi", color=Colors.BLUE),
            TextBox(Coordinate(1290, 50), 100, 32, text_static="Right Poi", color=Colors.RED),
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
                Coordinate(1445, 150),
                100,
                32,
                text_static="\u03C0",
            ),
            TextBox(
                Coordinate(1445, 250),
                100,
                32,
                text_static="\u03C0",
            ),
        ]


        # Main loop
        running = True
        while running:
            screen.fill(Colors.WHITE)

            r_poi.perform_movement()
            l_poi.perform_movement()

            for obj in objects:
                obj.draw(screen)

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                for obj in objects:
                    obj.handle_event(event)
            timdir_prop, timdir_arm = get_timing_dir(l_poi, r_poi)
            prop_timdir_textbox.set_text_dynamic(
                f"{timdir_prop.name}" if timdir_prop is not None else ""
            )
            arm_timdir_textbox.set_text_dynamic(
                f"{timdir_arm.name}" if timdir_arm is not None else ""
            )
            pygame.display.flip()
            clock.tick(tick)

        pygame.quit()
        
        
def main():
    poi_simulator = PoiSimulator()
    
if __name__ == "__main__":
    main()