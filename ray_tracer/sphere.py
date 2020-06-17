import math

from ray_tracer.intersections import Intersections, Intersection
from ray_tracer.shape import Shape
from ray_tracer.tuples import Point, dot


class Sphere(Shape):
    __slots__ = ()

    def __eq__(self, other):
        return isinstance(other, Sphere)

    def __str__(self):
        return "Sphere()"

    def intersect(self, ray):
        center = Point(0, 0, 0)
        radius = 1
        sphere_to_ray = ray.origin - center
        a = dot(ray.direction, ray.direction)
        b = 2 * dot(ray.direction, sphere_to_ray)
        c = dot(sphere_to_ray, sphere_to_ray) - radius
        discriminant = b**2 - 4 * a * c

        if discriminant < 0:
            return Intersections()

        t1 = (-b - math.sqrt(discriminant)) / (2 * a)
        t2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return Intersections(Intersection(t1, self), Intersection(t2, self))

    def normal_at(self, point):
        object_normal = point - Point(0, 0, 0)
        return object_normal
