from abc import ABC, abstractmethod

from ray_tracer.material import Material


class Shape(ABC):
    __slots__ = ("material")

    def __init__(self, material=None):
        self.material = Material()

    @abstractmethod
    def intersect(self, ray):
        pass

    @abstractmethod
    def normal_at(self, world_point):
        pass


def set_transform(shape, transform):
    shape.transform = transform
    return shape


def normal_at(shape, world_point):
    return shape.normal_at(world_point)

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
