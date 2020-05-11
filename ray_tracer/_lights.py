from dataclasses import dataclass

from . import Point, Color


@dataclass
class Light:
    position: Point
    intensity: Color


def point_light(position, intensity):
    return Light(position, intensity)