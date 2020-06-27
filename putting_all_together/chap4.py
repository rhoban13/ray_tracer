import math
from pathlib import Path

from ray_tracer.colors import RED, GREEN
from ray_tracer.tuples import Point, Vector
from ray_tracer.transformations import rotation_z
from ray_tracer.canvas import Canvas, canvas_to_png


def main():
    c = Canvas(200, 200)
    adjustment = Vector(c.width/2, c.height/2 ,0)
    radius = 3 * c.width / 8
    center = Point(0, 0, 0) + adjustment
    c.write_pixel(int(center.x), int(center.y), RED)

    twelve = Point(0, radius, 0)
    points = [twelve]
    for k in range(12):
        R = rotation_z(k * math.pi / 6)
        points.append(R * twelve)
    points = [p + adjustment for p in points]

    for p in points:
        c.write_pixel(int(p.x), int(p.y), GREEN)

    path = Path(__file__).parent / "chap4.png"
    canvas_to_png(str(path), c)


if __name__ == "__main__":
    main()
