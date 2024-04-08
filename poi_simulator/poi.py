import math
import pygame
from poi_simulator.utils import Coordinate
from poi_simulator.object import Object

def move(coord: Coordinate, radius: float, angle: float):
    coord.x = radius * math.cos(angle)
    coord.y = radius * math.sin(angle)



class Orbit:
    def __init__(self, poi: 'Poi', radius: int):
        self.poi = poi
        self.radius = radius
        self.speed_factor = 1
        self.angle_base = 0
        self.angle_offset_factor = 0
        self.pos = Coordinate(0, 0)
        
        self.trail_enabled = True
        self.trail_positions = []
        self.trail_length = 500
        
    def set_speed_factor(self, speed_factor):
        self.speed_factor = speed_factor
        
    def set_angle_offset(self, angle_offset_factor: float):
        self.angle_offset_factor = angle_offset_factor

            
    def get_angular_speed(self):
        return self.poi.angular_speed_unit * self.speed_factor
    
    def get_angle(self):
        return self.angle_base + self.angle_offset_factor * math.pi
    
    def move(self):
        move(self.pos, self.radius, self.get_angle())
        self.pos.x = self.radius * math.cos(self.get_angle())
        self.pos.y = self.radius * math.sin(self.get_angle())
        
        self.trail_positions.append(self.pos)
        self.trail_positions = self.trail_positions[-self.trail_length:]
        
        self.angle_base += self.get_angular_speed()
        
    def reset(self):
        self.angle_base = 0
        self.pos = Coordinate(0, 0)
        self.trail_positions = []
    
class Poi(Object):
    def __init__(self, sim: 'PoiSimulator', color: tuple, pos_center: Coordinate):
        self.sim = sim
        self.color = color
        self.pos_center = pos_center
        
        self.set_unit_speed_pi_per_sec(2)

        self.prop = Orbit(self, 180)
        self.arm = Orbit(self, 200)
        
        self.trail_length = 500
        self.trail_positions = []
        self.trail_enabled = False
        self.enabled = True
        
        self.reset()
        self.start()
        
    def set_unit_speed_pi_per_sec(self, pi_per_sec: float):
        self.angular_speed_unit = pi_per_sec * math.pi / self.sim.tick
        
    def set_enabled(self, enabled: bool) -> None:
        self.enabled = enabled
        if self.enabled:
            self.clear_trail()
            
        
    def perform_movement(self):

        if not self.sim.paused:
            self.arm.move()
            self.prop.move()        
            self.pos_result = self.pos_center + self.arm.pos + self.prop.pos
            
            self.trail_positions.append(self.pos_result)
            self.trail_positions = self.trail_positions[-self.trail_length:]
        

    def draw(self, screen):
        if not self.enabled:
            return
                # Draw circles
        pygame.draw.circle(screen, self.color, self.pos_result.int_tuple(), 15)
        # pygame.draw.circle(screen, self.color, (self.pos_arm + self.pos_center).int_tuple(), 10)
        # pygame.draw.circle(screen, self.color, (self.pos_prop + self.pos_center).int_tuple(), 10)
        
        # Draw lines
        pygame.draw.line(screen, self.color, self.pos_center.int_tuple(), (self.pos_center + self.arm.pos).int_tuple(), 4)
        pygame.draw.line(screen, self.color, (self.pos_center + self.arm.pos).int_tuple(), self.pos_result.int_tuple(), 4)
        

        # Draw trail
        if self.trail_enabled:
            for i in range(len(self.trail_positions) - 1):
                pygame.draw.line(screen, self.color, self.trail_positions[i].int_tuple(), self.trail_positions[i + 1].int_tuple(), 2)

        
    def set_trail(self, enabled):
        self.trail_enabled = enabled
        self.clear_trail()
                
    def clear_trail(self):
        self.trail_positions = []
        
    def reset(self):
        self.clear_trail()
        self.arm.reset()
        self.prop.reset()

    def start(self):
        self.running = True
        
    def stop(self):
        self.running = False