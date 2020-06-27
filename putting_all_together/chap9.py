import argparse
import logging
import math
from pathlib import Path

from ray_tracer.canvas import canvas_to_png
from ray_tracer.camera import Camera
from ray_tracer.colors import Color
from ray_tracer.lights import point_light
from ray_tracer.material import Material
from ray_tracer.shapes import set_transform, Sphere, Plane
from ray_tracer.transformations import Scaling, Translation, view_transform
from ray_tracer.tuples import Point, Vector
from ray_tracer.world import World


def floor_material():
    material = Material()
    material.color = Color(1, .9, .9)
    material.specular = 0
    return material


def make_floor():
    output = Plane()
    output = set_transform(output, Scaling(10, .01, 10))
    output.material = floor_material()
    return output


def make_middle():
    middle = set_transform(Sphere(), Translation(-0.5, 1, 0.5))
    middle.material = Material()
    middle.material.color = Color(0.1, 1, 0.5)
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3
    return middle


def make_right():
    right = set_transform(Sphere(), Translation(1.5, 0.5, -0.5) * Scaling(0.5, 0.5, 0.5))
    right.material = Material()
    right.material.color = Color(0.5, 1, 0.1)
    right.material.diffuse = 0.7
    right.material.specular = 0.3
    return right


def make_left():
    left = set_transform(Sphere(), Translation(-1.5, 0.33, -0.75) * Scaling(0.33, 0.33, 0.33))
    left.material = Material()
    left.material.color = Color(1, 0.8, 0.1)
    left.material.diffuse = 0.7
    left.material.specular = 0.3
    return left


def main(canvas_dimensions):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(filename)s:%(lineno)s %(name)s %(message)s')

    objects = (
        make_floor(),
        make_middle(),
        make_right(),
        make_left()
    )

    light = point_light(Point(-10, 10, -10), Color(1, 1, 1))
    world = World(objects=objects, light=light)

    camera = Camera(*canvas_dimensions, math.pi/3)
    camera.transform = view_transform(Point(0, 1/5, -5), Point(0, 1, 0), Vector(0, 1, 0))

    canvas = camera.render(world)

    path = Path(__file__).parent / "chap9.png"
    canvas_to_png(str(path), canvas)


if __name__ == "__main__":
    resolutions = {'low': (100, 50), 'high': (1000, 500)}
    parser = argparse.ArgumentParser()
    parser.add_argument('resolution', choices=resolutions.keys())
    args = parser.parse_args()
    main(resolutions[args.resolution])
