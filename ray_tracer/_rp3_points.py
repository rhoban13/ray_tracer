from numbers import Number
import numpy as np

from typing import Any

class _RP3Point:
    def __init__(self, x: Number, y: Number, z: Number, w: Number):
        for coord in (x, y, z, w):
            assert isinstance(coord, Number),  f"{coord} is not a Number"

        self.ndarray = np.array((x, y, z, w))

    @property
    def x(self):
        return self.ndarray[0]

    @property
    def y(self):
        return self.ndarray[1]

    @property
    def z(self):
        return self.ndarray[2]

    @property
    def w(self):
        return self.ndarray[3]

    def __eq__(self, other):
        if self.w == 0:
            return np.array_equal(self.ndarray[:-1], other.ndarray[:-1])
        else:
            self.to_affine()
            other.to_affine()
            return np.array_equal(self.ndarray, other.ndarray)
        
    def to_affine(self):
        self.ndarray = self.ndarray / self.w

class Point(_RP3Point):
    """
    This represents a point in the affine pacth of RP^3
    This is identified with a eucliden point in R^3
    """
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 1)


class Vector(_RP3Point):
    """
    This represents a point at the boundary at infinity in RP^3
    This is identified with a direction in R^3
    """
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 0)


def make_rp3_point(x, y, z, w):
    if w == 0:
        return Vector(x, y, z)
    else:
        return Point(x, y, z)
