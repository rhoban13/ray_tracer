from abc import ABC, abstractmethod

from ray_tracer.intersections import Intersections, Intersection
from ray_tracer.material import Material
from ray_tracer.rays import transform
from ray_tracer.tuples import normalize


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


class InvalidInnerShape(Exception):
    pass


class TransformedShape(Shape):
    __slots__ = ("transform", "inner")

    '''A decorator applying a transformation to a concrete class'''
    def __init__(self, shape, transform):
        if isinstance(shape, TransformedShape):
            raise InvalidInnerShape("Only able to decorate a concrete shape with a single transform")
        self.transform = transform
        self.inner = shape

    def __str__(self):
        return f"TransformedShape(transform={self.transform},\n inner={self.inner},\n material={self.material})"

    @property
    def material(self):  # Not sure this should be here
        return self.inner.material

    @material.setter
    def material(self, value):
        self.inner.material = value

    def __eq__(self, other):
        return self.inner.material == other.material and \
                self.inner.__eq__(other.inner) and \
                self.transform == other.transform

    def intersect(self, ray):
        local_ray = transform(ray, self.transform.inverse())
        inner_intersections = self.inner.intersect(local_ray)
        return Intersections(*(Intersection(i.t, self) for i in inner_intersections))

    def normal_at(self, world_point):
        inv_ = self.transform.inverse()
        object_point = inv_ * world_point

        object_normal = self.inner.normal_at(object_point)
        linear_component = self.transform.linear_component()
        world_normal = linear_component.inverse().transpose() * object_normal
        return normalize(world_normal)


def set_transform(shape, transform):
    return TransformedShape(shape, transform)


def normal_at(shape, world_point):
    return shape.normal_at(world_point)
