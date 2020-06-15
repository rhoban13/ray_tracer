from functools import partial
import logging
from multiprocessing import Pool
import numpy as np

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
        for y in y_range:
            logging.info("Working pixels y=%s", y)
            for x in range(0, self.hsize - 1):
                ray = self.ray_for_pixel(x, y)
                color = world.color_at(ray)
                image.write_pixel(x, y, color)
        return image

    def render(self, world):
        num_cores = 1 #8
        y_range = np.arange(0, self.vsize - 1)
        splits = np.array_split(y_range, num_cores)
        
        fp = partial(self._process_slice, world)
        # pool = Pool(num_cores)
        # images = pool.map(fp, splits)
        # pool.close()
        # pool.join()
        images = map(fp, splits)
        return overlay(*images)


def ray_for_pixel(camera, x, y):
    return camera.ray_for_pixel(x, y)


def render(camera, world):
    return camera.render(world)
