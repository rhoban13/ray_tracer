import argparse
from pathlib import Path

from ray_tracer.canvas import Canvas, write_pixel, canvas_to_png
from ray_tracer.colors import Color, WHITE
from ray_tracer.intersections import intersect, hit
from ray_tracer.lights import point_light
from ray_tracer.material import Material, lighting
from ray_tracer.rays import Ray, position
from ray_tracer.shapes import Sphere
from ray_tracer.tuples import Point, normalize

ray_origin = Point(0, 0, -5)
wall_z = 10
wall_size = 7
light = point_light(Point(-10, 10, -10), WHITE)
shape = Sphere()
shape.material = Material()
shape.material.color = Color(1, .2, 1)


def get_color(a_hit, ray):
    point = position(ray, a_hit.t)
    normal = a_hit.object.normal_at(point)
    eye = -ray.direction
    color = lighting(a_hit.object.material, a_hit.object, light, point, eye, normal)
    return color


def cast_this_point(canvas, canvas_x, canvas_y, world_x, world_y):
    spot_on_wall = Point(world_x, world_y, wall_z)
    ray = Ray(ray_origin, normalize(spot_on_wall - ray_origin))
    xs = intersect(shape, ray)
    a_hit = hit(xs)
    if a_hit is not None:
        color = get_color(a_hit, ray)
        write_pixel(canvas, canvas_x, canvas_y, color)


def paint(canvas_pixels):
    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2

    canvas = Canvas(canvas_pixels, canvas_pixels)

    for y in range(canvas_pixels - 1):
        world_y = half - pixel_size * y
        for x in range(canvas_pixels - 1):
            world_x = -half + pixel_size * x
            cast_this_point(canvas, x, y, world_x, world_y)
    return canvas


def main():
    resolutions = {'low': 100, 'high': 500}
    parser = argparse.ArgumentParser()
    parser.add_argument('resolution', choices=resolutions.keys())
    args = parser.parse_args()

    canvas = paint(resolutions[args.resolution])
    path = Path(__file__).parent / "chap6.png"
    canvas_to_png(str(path), canvas)


if __name__ == "__main__":
    main()
