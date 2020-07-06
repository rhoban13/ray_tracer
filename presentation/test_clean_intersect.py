from ray_tracer.rays import Ray
from ray_tracer.tuples import Point, Vector

from presentation.clean_intersect import (
    intersect,
    intersect_stem,
    intersect_wing1,
    intersect_wing2
)

# stem tests
def test_ray_parallel_to_stem():
    ray = Ray(Point(-1, 0, 1), Vector(0, 1, 1))
    assert [] == intersect_stem(ray)


def test_ray_intersects_stem():
    ray = Ray(Point(0, 0, -1), Vector(1, 0, 0))
    assert [0] == intersect_stem(ray)


def test_ray_misses_stem():
    ray = Ray(Point(0, 1, 0), Vector(1, 0, 1))
    assert [] == intersect_stem(ray)


# wing1 tests
def test_ray_parallel_to_wing1():
    ray = Ray(Point(1, 1, 0), Vector(0, 1, -1))
    assert [] == intersect_wing1(ray)


def test_ray_intersects_wing1():
    ray = Ray(Point(1, 0, -1), Vector(0, 0, 1))
    assert [1] == intersect_wing1(ray)


def test_ray_misses_to_wing1():
    ray = Ray(Point(-1, 0, 0), Vector(0, 1, 1))
    assert [] == intersect_wing1(ray)


# wing2 tests
def test_ray_parallel_to_wing2():
    ray = Ray(Point(-1, 1, 0), Vector(0, 1, 1))
    assert [] == intersect_wing2(ray)


def test_ray_intersects_wing2():
    ray = Ray(Point(-1, 0, -1), Vector(0, 0, 1))
    assert [1] == intersect_wing2(ray)


def test_ray_misses_to_wing2():
    ray = Ray(Point(1, 0, 0), Vector(0, 1, -1))
    assert [] == intersect_wing2(ray)
