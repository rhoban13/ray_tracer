from ray_tracer.rays import Ray
from ray_tracer.shapes.crooked_plane import DefaultCrookedPlane
from ray_tracer.tuples import Point, Vector


# stem tests
def test_ray_parallel_to_stem():
    # Given
    cp = DefaultCrookedPlane()
    ray = Ray(Point(-1, 0, 1), Vector(0, 1, 1))

    # When
    xs = cp.intersect_stem(ray)

    # Then
    assert xs is None


def test_ray_intersects_stem():
    # Given
    cp = DefaultCrookedPlane()
    ray = Ray(Point(0, 0, -1), Vector(1, 0, 0))

    # When
    xs = cp.intersect_stem(ray)

    # Then
    assert xs.t == 0


def test_ray_misses_stem():
    # Given
    cp = DefaultCrookedPlane()
    ray = Ray(Point(0, 1, 0), Vector(1, 0, 1))

    # When
    xs = cp.intersect_stem(ray)

    # Then
    assert xs is None


# wing1 tests
def test_ray_parallel_to_wing1():
    # Given
    cp = DefaultCrookedPlane()
    ray = Ray(Point(1, 1, 0), Vector(0, 1, -1))

    # When
    xs = cp.intersect_wing1(ray)

    # Then
    xs is None


def test_ray_intersects_wing1():
    # Given
    cp = DefaultCrookedPlane()
    ray = Ray(Point(1, 0, -1), Vector(0, 0, 1))

    # When
    xs = cp.intersect_wing1(ray)

    # Then
    assert xs.t == 1


def test_ray_misses_to_wing1():
    # Given
    cp = DefaultCrookedPlane()
    ray = Ray(Point(-1, 0, 0), Vector(0, 1, 1))

    # When
    xs = cp.intersect_wing1(ray)

    # Then
    assert xs is None


# wing2 tests
def test_ray_parallel_to_wing2():
    # Given
    cp = DefaultCrookedPlane()
    ray = Ray(Point(-1, 1, 0), Vector(0, 1, 1))

    # When
    xs = cp.intersect_wing2(ray)

    # Then
    assert xs is None


def test_ray_intersects_wing2():
    # Given
    cp = DefaultCrookedPlane()
    ray = Ray(Point(-1, 0, -1), Vector(0, 0, 1))

    # When
    xs = cp.intersect_wing2(ray)

    # Then
    assert xs.t == 1


def test_ray_misses_to_wing2():
    # Given
    cp = DefaultCrookedPlane()
    ray = Ray(Point(1, 0, 0), Vector(0, 1, -1))

    # When
    xs = cp.intersect_wing2(ray)
    assert xs is None


def test_normal_at_stem():
    # Given
    p = Point(0, .5, 1)

    # When
    cp = DefaultCrookedPlane()
    n = cp.normal_at(p)

    # Then
    assert n == Vector(1, 0, 0)


def test_normal_at_wing1():
    # Given
    p = Point(3, 5, -5)

    # When
    cp = DefaultCrookedPlane()
    n = cp.normal_at(p)

    # Then
    assert n == Vector(0, 1, 1)


def test_normal_at_wing2():
    # Given
    p = Point(-3, 5, -5)

    # When
    cp = DefaultCrookedPlane()
    n = cp.normal_at(p)

    # Then
    assert n == Vector(0, 1, -1)

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
