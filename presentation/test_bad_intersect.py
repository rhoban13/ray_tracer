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
