from ray_tracer.intersections import Intersection, Intersections

from .shape import Shape


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
        output = []
        for xs in inner_intersections:
            if self._in_bounding_box(ray.position(xs.t)):
                output.append(Intersection(xs.t, self))
        return Intersections(*output)

    def _in_bounding_box(self, point):
        return all(abs(coord) < self.clipping_value for coord in (point.x, point.y, point.z))

    def normal_at(self, world_point):
        return self.inner.normal_at(world_point)

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
