import math

import numpy as np

from ray_tracer import Point, Vector


class Transformation:
    def __init__(self, arr):
        self.ndarray = np.array(arr)

    def inverse(self):
        return Transformation(np.linalg.inv(self.ndarray))

    def __mul__(self, other):
        if isinstance(other, Transformation):
            return Transformation(np.dot(self.ndarray, other.ndarray))

        assert isinstance(other, Point)  \
                or isinstance(other, Vector)
        return np.dot(self.ndarray, other)


class Translation(Transformation):
    def __init__(self, x, y, z):
        super().__init__([
                [1, 0, 0, x],
                [0, 1, 0, y],
                [0, 0, 1, z],
                [0, 0, 0, 1]
        ])

    def inverse(self):
        return Translation(
            -self.ndarray[0,3], 
            -self.ndarray[1,3],
            -self.ndarray[2,3]
        )

class Scaling(Transformation):
    def __init__(self, x, y, z):
        super().__init__([
                [x, 0, 0, 0],
                [0, y, 0, 0],
                [0, 0, z, 0],
                [0, 0, 0, 1]
        ])

    def inverse(self):
        return Scaling(
            1/self.ndarray[0, 0],
            1/self.ndarray[1, 1],
            1/self.ndarray[2, 2]
        )

# Ugly - think here
class RotationX(Transformation):
    def __init__(self, radians):
        super().__init__([
                [1, 0, 0, 0],
                [0, math.cos(radians), -math.sin(radians), 0],
                [0, math.sin(radians), math.cos(radians), 0],
                [0, 0, 0, 1]
        ])
        self._angle = radians

    def inverse(self):
        return type(self)(-self._angle)

class RotationY(Transformation):
    def __init__(self, radians):
        super().__init__([
                [math.cos(radians), 0, math.sin(radians), 0],
                [0, 1, 0, 0],
                [math.sin(radians), 0, math.cos(radians), 0],
                [0, 0, 0, 1]
        ])
        self._angle = radians

    def inverse(self):
        return type(self)(-self._angle)


class RotationZ(Transformation):
    def __init__(self, radians):
        super().__init__([
                [math.cos(radians), -math.sin(radians), 0, 0],
                [math.sin(radians), math.cos(radians), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
        ])
        self._angle = radians

    def inverse(self):
        return type(self)(-self._angle)


def rotation_x(radians):
    return RotationX(radians)


def rotation_y(radians):
    return RotationY(radians)


def rotation_z(radians):
    return RotationZ(radians)


class Shearing(Transformation):
    def __init__(self, xy, xz, yx, yz, zx, zy):
        super().__init__([
            [1, xy, xz, 0],
            [yx, 1, yz, 0],
            [zx, zy, 1, 0],
            [0, 0, 0, 1]
        ])


def inverse(transformation):
    return transformation.inverse()