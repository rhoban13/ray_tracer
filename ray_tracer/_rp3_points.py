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

    def __add__(self, other):
        return RP3Point(*(self.ndarray + other.ndarray))

    def __sub__(self, other):
        return RP3Point(*(self.ndarray - other.ndarray))

    def __neg__(self):
        """
        Not sure this one is a good idea to implmement
        """
        return RP3Point(*(-self.ndarray))

    def __mul__(self, scalar):
        return RP3Point(*(scalar * self.ndarray))

    def __truediv__(self, scalar):
        return RP3Point(*(self.ndarray / scalar))

    def to_affine(self):
        self.ndarray = self.ndarray / self.w

class Point(_RP3Point):
    """
    This represents a point in the affine pacth of RP^3
    This is identified with a eucliden point in R^3
    """
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 1)

    def __eq__(self, other):
        assert isinstance(other, Point)
        self.to_affine()
        other.to_affine()
        return np.array_equal(self.ndarray, other.ndarray)
        
    def __add__(self, other):
        assert isinstance(other, Vector)
        return super().__add__(other)

    def __sub__(self, other):
        assert isinstance(other, Point) or isinstance(other, Vector)
        return super().__sub__(other)

    def __str__(self):
        return f"Point({round(self.x, 2)}, {round(self.y, 2)}, {round(self.z, 2)})"
    
class Vector(_RP3Point):
    """
    This represents a point at the boundary at infinity in RP^3
    This is identified with a direction in R^3
    """
    def __init__(self, x, y, z):
        super().__init__(x, y, z, 0)

    def __eq__(self, other):
        assert isinstance(other, Vector)
        return np.array_equal(self.ndarray[:-1], other.ndarray[:-1])

    def __str__(self):
        return f"Vector({round(self.x, 2)}, {round(self.y, 2)}, {round(self.z, 2)})"
    
def RP3Point(x, y, z, w):
    if w == 0:
        return Vector(x, y, z)
    else:
        return Point(x, y, z)

def magnitude(v):
    assert isinstance(v, Vector)
    return np.linalg.norm(v.ndarray[:-1])

def normalize(v):
    assert isinstance(v, Vector)
    mag = magnitude(v)
    if mag == 0:
        return v
    return v / magnitude(v)

def dot(v, w):
    assert isinstance(v, Vector)
    assert isinstance(w, Vector)
    return np.dot(v.ndarray, w.ndarray)

def cross(v, w):
    assert isinstance(v, Vector)
    assert isinstance(w, Vector)
    return Vector(*np.cross(v.ndarray[:-1], w.ndarray[:-1]))
