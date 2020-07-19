from functools import total_ordering
import heapq

from ray_tracer.rays import position
from ray_tracer.tuples import dot, reflect


@total_ordering
class Intersection:
    __slots__ = ("t", "object")

    def __init__(self, t, object_):
        self.t = t
        self.object = object_

    def __lt__(self, other):
        return self.t < other.t

    def __str__(self):
        return f"Intersection(t={self.t}, object={self.object})"


class Intersections:
    def __init__(self, *args):
        self._list_of_t = list(args)
        heapq.heapify(self._list_of_t)

    def __getitem__(self, index):
        return self._list_of_t[index]

    def __str__(self):
        return f"{self._list_of_t}"

    def __bool__(self):
        return self.count > 0

    @property
    def count(self):
        return len(self._list_of_t)

    def extend(self, intersections):
        self._list_of_t = list(heapq.merge(self._list_of_t, intersections._list_of_t))


def hit(intersections: Intersections):
    for intersection in intersections:
        if intersection.t >= 0:
            return intersection


def intersect(shape, ray):
    return shape.intersect(ray)


EPSILON = 1e-5


class Computations:
    def __init__(self, intersection, ray, xs=None):
        self.intersection = intersection
        self.ray = ray

        self.point = position(ray, self.t)
        self.eyev = -ray.direction
        self.normalv = intersection.object.normal_at(self.point)

        if dot(self.normalv, self.eyev) < 0:
            self.inside = True
            self.normalv = - self.normalv
        else:
            self.inside = False

        self.over_point = self.point + self.normalv * EPSILON
        self.under_point = self.point - self.normalv * EPSILON

        self.reflectv = reflect(ray.direction, self.normalv)

        self.n1, self.n2 = self.compute_refractive_indexes(intersection, xs)

    def compute_refractive_indexes(self, this_intersection, intersections):
        if not intersections:
            return None, None

        containers = []
        for i in intersections:
            if i == this_intersection:
                n1 = self._compute_refractive_index(containers)

            if i.object in containers:
                containers.remove(i.object)
            else:
                containers.append(i.object)

            if i == this_intersection:
                n2 = self._compute_refractive_index(containers)
                break
        return n1, n2

    @staticmethod
    def _compute_refractive_index(containers):
        if not containers:
            n = 1
        else:
            n = containers[-1].material.refractive_index
        return n

    @property
    def t(self):
        return self.intersection.t

    @property
    def object(self):
        return self.intersection.object

    def __str__(self):
        return f'''Computations:
    intersection = {self.intersection}
    ray = {self.ray}
    point = {self.point}
    eyev = {self.eyev}
    normalv = {self.normalv}
    inside = {self.inside}
'''


def prepare_computations(intersection, ray, xs=None):
    return Computations(intersection, ray, xs)

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
