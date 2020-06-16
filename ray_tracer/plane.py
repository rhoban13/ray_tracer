from ray_tracer.intersections import EPSILON, Intersections, Intersection
from ray_tracer.rays import Ray
from ray_tracer.shape import ShapeWithMaterial
from ray_tracer.tuples import Vector


class Plane(ShapeWithMaterial):
    __slots__ = ()

    def intersect(self, ray: Ray):
        if abs(ray.direction.y) < EPSILON:  # parallel to the plane
            return Intersections()

        t = -ray.origin.y / ray.direction.y
        return Intersections(Intersection(t, self))

    def normal_at(self, world_point):
        return Vector(0, 1, 0)
