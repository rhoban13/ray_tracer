from behave import given

from ray_tracer.intersections import Intersections, Intersection
from ray_tracer.shapes import Shape, TransformedShape
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

# Copyright 2020 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
