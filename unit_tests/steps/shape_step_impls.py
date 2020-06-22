from behave import given

from ray_tracer.intersections import Intersections, Intersection
from ray_tracer.shape import Shape, TransformedShape
from ray_tracer.transformations import Identity
from ray_tracer.tuples import Vector


class ConcreteTestShape(Shape):
    __slots__ = ("saved_ray")

    def __init__(self):
        super().__init__()
        self.saved_ray = None

    def intersect(self, ray):
        self.saved_ray = ray
        # This magical TestShape always has one intersection at t=5
        # I added this to check a mistake I made.  This'll help ensure that the intersection.object is correct
        return Intersections(Intersection(5, self))

    def normal_at(self, point):
        return Vector(point.x, point.y, point.z)


def TestShape():
    return TransformedShape(ConcreteTestShape(), Identity())

def test_shape():
    return TestShape()


@given(u'{s} = test_shape()')
def step_impl(context, s):
    _s = test_shape()
    setattr(context, s, _s)
