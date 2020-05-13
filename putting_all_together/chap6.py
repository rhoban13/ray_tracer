from pathlib import Path

import time

from ray_tracer import Point, Sphere, RED, WHITE, Ray, normalize, intersect, hit, Material, Color, point_light, position, normal_at, lighting
from ray_tracer.canvas import Canvas, write_pixel, canvas_to_png




ray_origin = Point(0, 0, -5)

# Init canvas
wall_z = 10
wall_size = 7
canvas_pixels = 100 #900
pixel_size = wall_size / canvas_pixels
half = wall_size / 2

def paint():
    canvas = Canvas(canvas_pixels, canvas_pixels)

    shape = Sphere()
    shape.material = Material()
    shape.material.color = Color(1, .2, 1)

    light = point_light(Point(-10, 10, -10), WHITE)

    for y in range(canvas_pixels - 1):
        world_y = half - pixel_size * y
        if y % 10 == 0:
            print(f"world_y {world_y}")
        for x in range(canvas_pixels - 1):
            world_x = -half + pixel_size * x
            spot_on_wall = Point(world_x, world_y, wall_z)
            r = Ray(ray_origin, normalize(spot_on_wall - ray_origin))
            xs = intersect(shape, r)

            a_hit = hit(xs)
            if a_hit is not None:  
                point = position(r, a_hit.t)
                normal = normal_at(a_hit.object, point)
                eye = -r.direction
                color = lighting(a_hit.object.material, light, point, eye, normal)
                write_pixel(canvas, x, y, color)
    return canvas

import cProfile
import pstats
start = time.perf_counter()
with cProfile.Profile() as pr:
    canvas = paint()
stop = time.perf_counter()
print(f"Time elapsed = {(stop - start)} sec")
stats = pstats.Stats(pr).sort_stats('tottime')
stats.print_stats()
#stats.print_callers()

#path = Path(__file__).parent / "chap6.png"
#canvas_to_png(str(path), canvas)
#done_write = time.perf_counter()
#print(f"Writing png took {(done_write - stop)} sec") 