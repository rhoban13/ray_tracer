import argparse
import logging
import math

import imageio
import numpy as np
from pathlib import Path


from ray_tracer.canvas import canvas_to_png
from ray_tracer.camera import Camera
from ray_tracer.colors import Color, WHITE, BLUE, GREEN
from ray_tracer.lights import point_light
from ray_tracer.material import Material
from ray_tracer.patterns import gradient_pattern
from ray_tracer.shapes import ClippedShape, CrookedPlane
from ray_tracer.transformations import view_transform, Scaling
from ray_tracer.tuples import Point, Vector
from ray_tracer.world import World


def make_single_frame(objects, view_transform_, camera_resolution):
    lights = [
        point_light(Point(10, 10, 15), WHITE),
        point_light(Point(-10, -10, 15), WHITE)
    ]
    world = World(objects=objects, light=lights)
    camera = Camera(*camera_resolution, math.pi/3)
    camera.transform = view_transform_
    canvas = camera.render(world)
    return canvas


def main(resolution):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(filename)s:%(lineno)s %(name)s %(message)s')

    shape = ClippedShape(CrookedPlane())
    shape.material = Material()
    shape.material.color = Color(1, .2, 1)
    shape.material.transparency = 1.0
    shape.material.refractive_index = 1.5
    objects = (shape,)

    rad = 6
    camera_height = .8 * rad
    frames = []
    for t in np.arange(0, math.pi, .1 * math.pi):
        logging.info("New Frame %s", t)
        camera_position = Point(rad * math.cos(t), rad * math.sin(t), camera_height)
        vt = view_transform(camera_position, Point(0, 0, 0), Vector(0, 0, 1))
        canvas = make_single_frame(objects, vt, resolution)
        frames.append(canvas._image)

    path = Path(__file__).parent / "chap11.gif"
    imageio.mimsave(str(path), frames, duration=0.25)


if __name__ == "__main__":
    resolutions = {'low': (100, 50), 'high': (1000, 500)}
    parser = argparse.ArgumentParser()
    parser.add_argument('resolution', choices=resolutions.keys())
    args = parser.parse_args()
    main(resolutions[args.resolution])


 

    #imageio.mimsave("examples/glass_crooked_plane.gif", frames, duration=0.25)

# Copyright 2020 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
