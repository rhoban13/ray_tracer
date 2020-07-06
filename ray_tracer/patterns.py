from abc import ABC, abstractmethod
import math

from ray_tracer.transformations import Identity


class Pattern(ABC):
    @abstractmethod
    def pattern_at(self, world_point):
        pass


class StripePattern(Pattern):
    def __init__(self, color1, color2):
        super().__init__()
        self.a = color1
        self.b = color2

    def pattern_at(self, point):
        if math.floor(point.x) % 2 == 0:
            return self.a
        return self.b


class GradientPattern(Pattern):
    def __init__(self, color1, color2):
        super().__init__()
        self.color1 = color1
        self.color2 = color2

    def pattern_at(self, point):
        distance = self.color2 - self.color1
        fraction = point.x - math.floor(point.x)
        return self.color1 + distance * fraction


class RingPattern(Pattern):
    def __init__(self, color1, color2):
        super().__init__()
        self.color1 = color1
        self.color2 = color2

    def pattern_at(self, point):
        if math.floor(math.sqrt(point.x**2 + point.z**2)) % 2 == 0:
            return self.color1
        else:
            return self.color2

class CheckersPattern(Pattern):
    def __init__(self, color1, color2):
        super().__init__()
        self.color1 = color1
        self.color2 = color2

    def pattern_at(self, point):
        if (math.floor(point.x) + math.floor(point.y) + math.floor(point.z)) % 2 == 0:
            return self.color1
        else:
            return self.color2


class TransformedPattern(Pattern):
    __slots__ = ("inner")

    def __init__(self, inner: Pattern, transform):
        super().__init__()
        self.inner = inner
        self.transform = transform

    def pattern_at(self, object_point):
        pattern_point = self.transform.inverse() * object_point
        return self.inner.pattern_at(pattern_point)


def stripe_pattern(color1, color2):
    return TransformedPattern(StripePattern(color1, color2), Identity())


def gradient_pattern(color1, color2):
    return TransformedPattern(GradientPattern(color1, color2), Identity())


def ring_pattern(color1, color2):
    return TransformedPattern(RingPattern(color1, color2), Identity())


def checkers_pattern(color1, color2):
    return TransformedPattern(CheckersPattern(color1, color2), Identity())


def pattern_at(pattern, point):
    return pattern.pattern_at(point)


def pattern_at_shape(pattern: Pattern, shape, world_point):
    # Wierd - should the conversion to an object_point be a member of the object?
    object_point = shape.transform.inverse() * world_point
    return pattern.pattern_at(object_point)


def set_pattern_transform(pattern: Pattern, transform):
    return TransformedPattern(pattern, transform)

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
