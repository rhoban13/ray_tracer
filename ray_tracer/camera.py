from functools import partial
import logging
from multiprocessing import get_context, log_to_stderr
import numpy as np
import os

from ray_tracer.canvas import Canvas, overlay
from ray_tracer.rays import Ray
from ray_tracer.transformations import Transformation
from ray_tracer.tuples import Point, normalize


class Camera:
    def __init__(self, hsize, vsize, field_of_view):
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = Transformation(np.eye(4))

        half_view = np.round(np.tan(field_of_view/2), 5)
        aspect = hsize / vsize
        if aspect >= 1:
            self.half_width = half_view
            self.half_height = half_view / aspect
        else:
            self.half_height = half_view
            self.half_width = half_view * aspect

        self.pixel_size = (self.half_width * 2) / hsize

        self.logger = None

    def ray_for_pixel(self, x, y):
        xoffset = (x + .5) * self.pixel_size
        yoffset = (y + .5) * self.pixel_size

        world_x = self.half_width - xoffset
        world_y = self.half_height - yoffset

        pixel = self.transform.inverse() * Point(world_x, world_y, -1)
        origin = self.transform.inverse() * Point(0, 0, 0)

        direction = normalize(pixel - origin)
        return Ray(origin, direction)

    def _process_slice(self, world, y_range):
        image = Canvas(self.hsize, self.vsize)
        total_cols = len(y_range)
        for y in y_range:
            percent_completed = int(100 * (y-y_range[0])/total_cols)
            self.logger.info(f"{percent_completed}% completed")
            for x in range(0, self.hsize - 1):
                ray = self.ray_for_pixel(x, y)
                color = world.color_at(ray)
                image.write_pixel(x, y, color)
        return image

    def _render_multiprocess(self, world):
        self.logger = log_to_stderr()
        self.logger.setLevel(logging.INFO)

        num_cores = os.cpu_count()
        y_range = np.arange(0, self.vsize - 1)
        splits = np.array_split(y_range, num_cores)
        with get_context("spawn").Pool() as pool:
            fp = partial(self._process_slice, world)
            images = pool.map(fp, splits)
        return overlay(*images)

    def _render_single_process(self, world):
        self.logger = logging.getLogger(__name__)
        y_range = np.arange(0, self.vsize - 1)
        image = self._process_slice(world, y_range)
        return image

    def render(self, world):
        return self._render_multiprocess(world)
        # return self._render_single_process(world)


def ray_for_pixel(camera, x, y):
    return camera.ray_for_pixel(x, y)


def render(camera, world):
    return camera.render(world)

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
