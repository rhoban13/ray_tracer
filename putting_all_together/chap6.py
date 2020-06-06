import cProfile
from pathlib import Path
import pstats

from ray_tracer.canvas import Canvas, write_pixel, canvas_to_png
from ray_tracer.colors import Color, RED, WHITE
from ray_tracer.intersections import intersect, hit
from ray_tracer.lights import point_light
from ray_tracer.material import Material, lighting
from ray_tracer.rays import Ray, position
from ray_tracer.sphere import Sphere, normal_at
from ray_tracer.tuples import Point, normalize


ray_origin = Point(0, 0, -5)

# Init canvas
wall_z = 10
wall_size = 7
canvas_pixels = 500 #900
pixel_size = wall_size / canvas_pixels
half = wall_size / 2

canvas = Canvas(canvas_pixels, canvas_pixels)

shape = Sphere()
shape.material = Material()
shape.material.color = Color(1, .2, 1)

light = point_light(Point(-10, 10, -10), WHITE)


def get_color(a_hit, ray):
    point = position(ray, a_hit.t)
    normal = normal_at(a_hit.object, point)
    eye = -ray.direction
    color = lighting(a_hit.object.material, light, point, eye, normal)
    return color


def cast_this_point(canvas_x, canvas_y, world_x, world_y):
    spot_on_wall = Point(world_x, world_y, wall_z)
    ray = Ray(ray_origin, normalize(spot_on_wall - ray_origin))
    xs = intersect(shape, ray)
    a_hit = hit(xs)
    if a_hit is not None:
        color = get_color(a_hit, ray)
        write_pixel(canvas, canvas_x, canvas_y, color)


def paint():
    for y in range(canvas_pixels - 1):
        world_y = half - pixel_size * y
        if y % 100 == 0:
            print(f"world_y {world_y}")
        for x in range(canvas_pixels - 1):
            world_x = -half + pixel_size * x
            cast_this_point(x, y, world_x, world_y)


with cProfile.Profile() as pr:
    paint()

stats = pstats.Stats(pr).sort_stats('tottime')
stats.print_stats(.25)

path = Path(__file__).parent / "chap6.png"
canvas_to_png(str(path), canvas)
