import math

from ray_tracer.intersections import Intersections, Intersection
from ray_tracer.transformations import Identity
from ray_tracer.tuples import Point, dot

from .shape import Shape
from .transformed_shape import TransformedShape


class UnitSphere(Shape):
    __slots__ = ()

    def __eq__(self, other):
        return isinstance(other, self.__class__)

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


def Sphere():
    return TransformedShape(UnitSphere(), Identity())

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
