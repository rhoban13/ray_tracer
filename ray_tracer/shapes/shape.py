from abc import ABC, abstractmethod

from ray_tracer.material import Material


class Shape(ABC):
    __slots__ = ("material")

    def __init__(self, material=None):
        self.material = Material()

    @abstractmethod
    def intersect(self, ray):
        pass

    @abstractmethod
    def normal_at(self, world_point):
        pass


def set_transform(shape, transform):
    shape.transform = transform
    return shape


def normal_at(shape, world_point):
    return shape.normal_at(world_point)
