from . import Point, Vector

class Ray:
    def __init__(self, origin: Point, direction: Vector):
        self.origin = origin
        self.direction = direction


def position(ray, t):
    return ray.origin + ray.direction * t


def transform(ray, matrix):
    return Ray(matrix * ray.origin, matrix * ray.direction)