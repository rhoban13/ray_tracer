import logging
import math
from pathlib import Path

from ray_tracer.canvas import canvas_to_png
from ray_tracer.camera import Camera
from ray_tracer.colors import Color
from ray_tracer.lights import point_light
from ray_tracer.material import Material
from ray_tracer.sphere import Sphere
from ray_tracer.transformations import Scaling, Translation, rotation_x, rotation_y, view_transform
from ray_tracer.tuples import Point, Vector
from ray_tracer.world import World


def floor_material():
    material = Material()
    material.color = Color(1, .9, .9)
    material.specular = 0
    return material


def make_floor():
    output = Sphere()
    output.transform = Scaling(10, .01, 10)
    output.material = floor_material()
    return output


def make_wall(theta):
    wall = Sphere()
    wall.transform = Translation(0, 0, 5) * rotation_y(theta) * rotation_x(math.pi/2) * Scaling(10, .01, 10)
    wall.material = floor_material()
    return wall


def make_middle():
    middle = Sphere()
    middle.transform = Translation(-0.5, 1, 0.5)
    middle.material = Material()
    middle.material.color = Color(0.1, 1, 0.5)
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3
    return middle


def make_right():
    right = Sphere()
    right.transform = Translation(1.5, 0.5, -0.5) * Scaling(0.5, 0.5, 0.5)
    right.material = Material()
    right.material.color = Color(0.5, 1, 0.1)
    right.material.diffuse = 0.7
    right.material.specular = 0.3
    return right


def make_left():
    left = Sphere()
    left.transform = Translation(-1.5, 0.33, -0.75) * Scaling(0.33, 0.33, 0.33)
    left.material = Material()
    left.material.color = Color(1, 0.8, 0.1)
    left.material.diffuse = 0.7
    left.material.specular = 0.3
    return left


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(filename)s:%(lineno)s %(name)s %(message)s')

    objects = (
        make_floor(),
        make_wall(-math.pi/4),
        make_wall(math.pi/4),
        make_middle(),
        make_right(),
        make_left()
    )

    light = point_light(Point(-10, 10, -10), Color(1, 1, 1))
    world = World(objects=objects, light=light)

    camera = Camera(1000, 500, math.pi/3)
    camera.transform = view_transform(Point(0, 1/5, -5), Point(0, 1, 0), Vector(0, 1, 0))

    canvas = camera.render(world)

    path = Path(__file__).parent / "chap7.png"
    canvas_to_png(str(path), canvas)


if __name__ == "__main__":
    main()