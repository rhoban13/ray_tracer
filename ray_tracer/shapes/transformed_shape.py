from ray_tracer.intersections import Intersections, Intersection
from ray_tracer.rays import transform
from ray_tracer.transformations import Identity
from ray_tracer.tuples import normalize

from .shape import Shape


class TransformedShape(Shape):
    __slots__ = ("transform", "inner")

    '''A decorator applying a transformation to a concrete class'''
    def __init__(self, shape, transform=None):
        # super().__init__()
        self.transform = transform if transform else Identity()
        self.inner = shape

    def __str__(self):
        return f"TransformedShape(transform={self.transform},\n inner={self.inner},\n material={self.material})"

    @property
    def material(self):  # Not sure this should be here
        return self.inner.material

    @material.setter
    def material(self, value):
        self.inner.material = value

    def __eq__(self, other):
        return self.inner.material == other.material and \
                self.inner.__eq__(other.inner) and \
                self.transform == other.transform

    def intersect(self, ray):
        local_ray = transform(ray, self.transform.inverse())
        inner_intersections = self.inner.intersect(local_ray)
        return Intersections(*(Intersection(i.t, self) for i in inner_intersections))

    def normal_at(self, world_point):
        inv_ = self.transform.inverse()
        object_point = inv_ * world_point

        object_normal = self.inner.normal_at(object_point)
        linear_component = self.transform.linear_component()
        world_normal = linear_component.inverse().transpose() * object_normal
        return normalize(world_normal)


class InvalidInnerShape(Exception):
    pass

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
