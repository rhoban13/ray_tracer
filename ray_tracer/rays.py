from dataclasses import dataclass
from ray_tracer.tuples import Point, Vector

@dataclass
class Ray:
    origin: Point
    direction: Vector

    def position(self, t):
        return self.origin + t * self.direction


def position(ray, t):
    return ray.position(t)


def transform(ray, matrix):
    return Ray(matrix * ray.origin, matrix * ray.direction)
