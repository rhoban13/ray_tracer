from ray_tracer.intersections import Intersection, Intersections
from ray_tracer.tuples import Vector

from .shape import Shape
from .transformed_shape import TransformedShape


def minkowski_dot(u, v):
    return u.x * v.x + u.y * v.y - u.z * v.z


def minkowski_norm(v):
    return minkowski_dot(v, v)


class DefaultCrookedPlane(Shape):
    def __init__(self):
        super().__init__()

    def intersect(self, ray):
        stem_intersection = self.intersect_stem(ray)
        wing1_intersection = self.intersect_wing1(ray)
        wing2_intersection = self.intersect_wing2(ray)
        intersections = [stem_intersection, wing1_intersection, wing2_intersection]
        intersections = [x for x in intersections if x is not None]
        return Intersections(*intersections)

    def intersect_stem(self, ray):
        if ray.direction.x == 0:  # parallel to the xz-plane 
            return None

        t = -ray.origin.x / ray.direction.x
        intersection_point = ray.origin + t * ray.direction
        if minkowski_norm(intersection_point) < 0:
            return Intersection(t, self)

    def intersect_wing1(self, ray):
        if ray.direction.y == - ray.direction.z:  # parallel to the wing
            return None

        t = - (ray.origin.y + ray.origin.z)/(ray.direction.y + ray.direction.z)
        intersection_point = ray.origin + t * ray.direction
        if intersection_point.x >= 0:
            return Intersection(t, self)

    def intersect_wing2(self, ray):
        if ray.direction.y == ray.direction.z:  # parallel to the wing
            return None

        t = - (ray.origin.y - ray.origin.z)/(ray.direction.y - ray.direction.z)
        intersection_point = ray.origin + t * ray.direction
        if intersection_point.x <= 0:
            return Intersection(t, self)

    def normal_at(self, world_point):
        if minkowski_norm(world_point) <= 0:
            if world_point.z > 0:
                return Vector(1, 0, 0)
            else:
                return Vector(-1, 0, 0)
        if world_point.x >= 0:
            return Vector(0, 1, 1)
        if world_point.x <= 0:
            return Vector(0, 1, -1)


def CrookedPlane():
    return TransformedShape(DefaultCrookedPlane())

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
