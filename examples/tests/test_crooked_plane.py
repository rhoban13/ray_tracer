from ray_tracer.rays import Ray
from ray_tracer.tuples import Point, Vector

from examples.crooked_plane import DefaultCrookedPlane, crooked_plane


def test_parallel_to_stem_does_not_interect():
    # Given
    origin = Point(1, 0, 1)
    direction = Vector(0, 5, 7)
    ray = Ray(origin, direction)

    # When
    cp = DefaultCrookedPlane()
    intersections = cp.intersect_stem(ray)

    # Then
    assert not intersections


def test_intersects_stem():
    # Given
    origin = Point(1, 0, 1)
    direction = Vector(-1, 0, 0)
    ray = Ray(origin, direction)

    # When
    cp = DefaultCrookedPlane()
    intersection = cp.intersect_stem(ray)

    # Then
    assert intersection.t == 1


def test_parallel_to_wing1():
    # Given
    origin = Point(1, 1, 0)
    direction = Vector(0, 1, -1)
    ray = Ray(origin, direction)

    # When
    cp = DefaultCrookedPlane()
    intersections = cp.intersect_wing1(ray)

    # Then
    assert not intersections


def test_intersects_wing1():
    # Given
    origin = Point(1, 1, 0)
    direction = Vector(0, 0, -1)
    ray = Ray(origin, direction)

    # When
    cp = DefaultCrookedPlane()
    intersections = cp.intersect(ray)

    # Then
    assert intersections.count == 1
    intersection = intersections[0]
    assert intersection.t == 1


def test_misses_wing1():
    # Given
    origin = Point(-1, 1, 0)
    direction = Vector(0, 0, -1)
    ray = Ray(origin, direction)

    # When
    cp = DefaultCrookedPlane()
    intersections = cp.intersect(ray)

    # Then
    assert not intersections


def test_parallel_to_wing2():
    # Given
    origin = Point(-1, 1, 0)
    direction = Vector(0, 1, 1)
    ray = Ray(origin, direction)

    # When
    cp = DefaultCrookedPlane()
    intersections = cp.intersect_wing2(ray)

    # Then
    assert not intersections


def test_intersects_wing2():
    # Given
    origin = Point(-1, 1, 0)
    direction = Vector(0, 0, 1)
    ray = Ray(origin, direction)

    # When
    cp = DefaultCrookedPlane()
    intersection = cp.intersect_wing2(ray)

    # Then
    assert intersection.t == 1


def test_misses_wing2():
    # Given
    origin = Point(1, 1, 0)
    direction = Vector(0, 0, 1)
    ray = Ray(origin, direction)

    # When
    cp = DefaultCrookedPlane()
    intersections = cp.intersect_wing2(ray)

    # Then
    assert not intersections


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
    p = Point(-3, 5, 5)

    # When
    cp = DefaultCrookedPlane()
    n = cp.normal_at(p)

    # Then
    assert n == Vector(0, 1, -1)
