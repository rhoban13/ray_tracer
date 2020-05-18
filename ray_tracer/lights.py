from dataclasses import dataclass

from ray_tracer.colors import Color
from ray_tracer.tuples import Point


@dataclass
class Light:
    position: Point
    intensity: Color

    def __str__(self):
        return f"Light<position={self.position}, intensity={self.intensity}>"

def point_light(position, intensity):
    return Light(position, intensity)