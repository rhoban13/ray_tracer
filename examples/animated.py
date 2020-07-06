import logging
import math

import imageio
import numpy as np

from ray_tracer.camera import Camera
from ray_tracer.colors import Color, WHITE, BLUE, GREEN
from ray_tracer.lights import point_light
from ray_tracer.material import Material
from ray_tracer.patterns import gradient_pattern
from ray_tracer.shapes import ClippedShape, CrookedPlane
from ray_tracer.transformations import view_transform, Scaling
from ray_tracer.tuples import Point, Vector
from ray_tracer.world import World


def make_single_frame(objects, view_transform_):
    lights = [
        point_light(Point(10, 10, 15), WHITE),
        point_light(Point(-10, -10, 15), WHITE)
    ]
    world = World(objects=objects, light=lights)
    camera = Camera(1000, 500, math.pi/3)
    camera.transform = view_transform_
    canvas = camera.render(world)
    return canvas


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(filename)s:%(lineno)s %(name)s %(message)s')

    shape = ClippedShape(CrookedPlane())
    shape.material = Material()
    shape.material.color = Color(1, .2, 1)
    #shape.material.pattern = gradient_pattern(BLUE, GREEN)
    #shape.material.pattern.transform = Scaling(4, 2, 2)
    objects = (shape,)

    rad = 6
    camera_height = .8 * rad
    frames = []
    for t in np.arange(0, math.pi, .1 * math.pi):
        logging.info("New Frame %s", t)
        camera_position = Point(rad * math.cos(t), rad * math.sin(t), camera_height)
        vt = view_transform(camera_position, Point(0, 0, 0), Vector(0, 0, 1))
        canvas = make_single_frame(objects, vt)
        frames.append(canvas._image)

    imageio.mimsave("examples/crooked_plane.gif", frames, duration=0.25)


    # with imageio.get_writer('examples/crooked_plane.gif', mode='I') as writer:
    #     for t in np.arange(0, math.pi, .2 * math.pi):
    #         logging.info("New Frame %s", t)
    #         camera_position = Point(rad * math.cos(t), rad * math.sin(t), rad)
    #         vt = view_transform(camera_position, Point(0, 0, 0), Vector(0, 0, 1))
    #         canvas = make_single_frame(objects, vt)
    #         writer.append_data(canvas._image)


if __name__ == "__main__":
    main()
