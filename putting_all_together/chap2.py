import argparse
from dataclasses import dataclass
from pathlib import Path

from ray_tracer.canvas import Canvas, canvas_to_png
from ray_tracer.colors import Color
from ray_tracer.tuples import Point, normalize, Vector


@dataclass
class Projectile:
    position: Point
    velocity: Vector

    def __str__(self):
        return f"Projectile(position={self.position}, velocity={self.velocity})"


@dataclass
class Environment:
    gravity: Vector
    wind: Vector


def tick(env, proj):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return Projectile(position, velocity)


def main(canvas_dimensions):
    start = Point(0, 1, 0)
    velocity = normalize(Vector(1, 1.8, 1)) * 11.25
    p = Projectile(start, velocity)

    gravity = Vector(0, -0.1, 0)
    wind = Vector(-0.01, 0, 0)
    e = Environment(gravity, wind)

    print(canvas_dimensions)
    c = Canvas(*canvas_dimensions)

    while p.position.y > 0:
        x, y = int(p.position.x), c.height - int(p.position.y)
        print(x, y)
        print(p.position)
        c.write_pixel(x, y, Color(0, 0, 1))
        p = tick(e, p)

    print(f"p has landed at {p}")
    path = Path(__file__).parent / "chap2.png"
    canvas_to_png(str(path), c)


if __name__ == "__main__":
    resolutions = {'low': (100, 50), 'high': (1000, 500)}
    parser = argparse.ArgumentParser()
    parser.add_argument('resolution', choices=resolutions.keys())
    args = parser.parse_args()
    print(f"{__file__}: Not regenerating this one, don't care")
    #main(resolutions[args.resolution])
