import numpy as np

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


def ray_for_pixel(camera, x, y):
    xoffset = (x + .5) * camera.pixel_size
    yoffset = (y + .5) * camera.pixel_size

    world_x = camera.half_width - xoffset
    world_y = camera.half_height - yoffset
    print(world_x)
    print(world_y)

    pixel = camera.transform.inverse() * Point(world_x, world_y, -1)
    print(pixel)
    origin = camera.transform.inverse() * Point(0, 0, 0)
    print(origin)
    direction = normalize(pixel - origin)
    return Ray(origin, direction)
