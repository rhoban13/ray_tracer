from ray_tracer.intersections import Intersection, Intersections
from ray_tracer.shape import Shape


class ClippedShape(Shape):
    __slots__ = ("clipping_value", "inner")

    '''A decorator applying a clip to a shape'''
    def __init__(self, shape):

        self.clipping_value = 2
        self.inner = shape

    def __str__(self):
        return f"ClippedShape(inner={self.inner})"

    def __eq__(self, other):
        return self.inner.__eq__(other.inner)

    def intersect(self, ray):
        inner_intersections = self.inner.intersect(ray)
        output = None
        for xs in inner_intersections:
            if self._in_bounding_box(ray.position(xs.t)):
                output.append(Intersection(xs.t, self))
        return Intersections(*output)

    def _in_bounding_box(self, point):
        return all(abs(coord) < self.clipping_value for coord in (point.x, point.y, point.z))

    def normal_at(self, world_point):
        return self.inner.normal_at(world_point)
