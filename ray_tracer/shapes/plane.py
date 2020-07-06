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
