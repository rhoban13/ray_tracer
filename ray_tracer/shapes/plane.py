from ray_tracer.intersections import EPSILON, Intersections, Intersection
from ray_tracer.rays import Ray
from ray_tracer.transformations import Identity
from ray_tracer.tuples import Vector

from .shape import Shape
from .transformed_shape import TransformedShape


class XZPlane(Shape):
    __slots__ = ()

    def intersect(self, ray: Ray):
        if abs(ray.direction.y) < EPSILON:  # parallel to the plane
            return Intersections()

        t = -ray.origin.y / ray.direction.y
        return Intersections(Intersection(t, self))

    def normal_at(self, world_point):
        return Vector(0, 1, 0)


def Plane():
    return TransformedShape(XZPlane(), Identity())
