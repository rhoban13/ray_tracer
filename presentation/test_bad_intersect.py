from ray_tracer.rays import Ray
from ray_tracer.tuples import Point, Vector

from presentation.bad_intersect import intersect


# stem tests
def test_ray_parallel_to_stem():
    ray = Ray(Point(-1, 0, 1), Vector(0, 1, 1))
    assert [] == intersect(ray)


def test_ray_intersects_stem():
    ray = Ray(Point(0, 0, -1), Vector(1, 0, 0))
    assert [0] == intersect(ray)


def test_ray_misses_stem():
    ray = Ray(Point(-1, 1, 0), Vector(1, 0, 0))
    assert [] == intersect(ray)


# wing1 tests
def test_ray_parallel_to_wing1():
    ray = Ray(Point(1, 1, 0), Vector(0, 1, -1))
    assert [] == intersect(ray)


def test_ray_intersects_wing1():
    ray = Ray(Point(1, 0, -1), Vector(0, 0, 1))
    assert [1] == intersect(ray)


def test_ray_misses_to_wing1():
    ray = Ray(Point(-1, 0, 0), Vector(0, 1, 1))
    assert [] == intersect(ray)


# wing2 tests
def test_ray_parallel_to_wing2():
    ray = Ray(Point(-1, 1, 0), Vector(0, 1, 1))
    assert [] == intersect(ray)


def test_ray_intersects_wing2():
    ray = Ray(Point(-1, 0, -1), Vector(0, 0, 1))
    assert [1] == intersect(ray)


def test_ray_misses_to_wing2():
    ray = Ray(Point(1, 0, 0), Vector(0, 1, -1))
    assert [] == intersect(ray)

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
