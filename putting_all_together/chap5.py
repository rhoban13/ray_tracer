from pathlib import Path

from ray_tracer.canvas import Canvas, write_pixel, canvas_to_png
from ray_tracer.colors import RED
from ray_tracer.intersections import intersect, hit
from ray_tracer.rays import Ray
from ray_tracer.shapes import Sphere
from ray_tracer.tuples import Point, normalize

ray_origin = Point(0, 0, -5)

wall_z = 10
wall_size = 7
canvas_pixels = 100
pixel_size = wall_size / canvas_pixels
half = wall_size / 2


canvas = Canvas(canvas_pixels, canvas_pixels)
shape = Sphere()

for y in range(canvas_pixels - 1):
    world_y = half - pixel_size * y
    for x in range(canvas_pixels - 1):
        world_x = -half + pixel_size * x

        position = Point(world_x, world_y, wall_z)
        r = Ray(ray_origin, normalize(position-ray_origin))
        xs = intersect(shape, r)
        if hit(xs) is not None:
            write_pixel(canvas, x, y, RED)

path = Path(__file__).parent / "chap5.png"
canvas_to_png(str(path), canvas)
