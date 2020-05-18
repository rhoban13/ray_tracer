import numpy as np

from ray_tracer.material import Material
from ray_tracer.transformations import Transformation, inverse
from ray_tracer.tuples import Point, dot, normalize


class Sphere:
    def __init__(self, transform=None, material=None):    
        self.transform = Transformation(np.eye(4))
        self.material = Material()

    def __eq__(self, other):
        return self.transform == other.transform \
                and self.material == other.material

    def __str__(self):
        return f"Sphere(transform={self.transform}, material={self.material})"


def set_transform(sphere, transform):
    sphere.transform = transform


def normal_at(sphere, world_point):
    inv_ = sphere.transform.inverse()
    object_point = inv_ * world_point
    object_normal = object_point - Point(0, 0, 0)
    linear_component = sphere.transform.linear_component()
    world_normal = linear_component.inverse().transpose() * object_normal
    return normalize(world_normal)
