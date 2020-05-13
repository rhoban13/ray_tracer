from numbers import Number
import numpy as np

from typing import Any

class _R4Vector:
    def __init__(self, x: Number, y: Number, z: Number, w: Number):
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
        _result = self.ndarray + other.ndarray
        return R4Vector(_result[0], _result[1], _result[2], _result[3])
        #return R4Vector(*(self.ndarray + other.ndarray))

    def __sub__(self, other):
        _result = self.ndarray - other.ndarray
        return R4Vector(_result[0], _result[1], _result[2], _result[3])
        #return R4Vector(*(self.ndarray - other.ndarray))

    def __neg__(self):
        return R4Vector(*(-self.ndarray))

    def __mul__(self, scalar: Number):
        assert isinstance(scalar, Number)
        return R4Vector(*(scalar * self.ndarray))
 
    def __truediv__(self, scalar: Number):
        assert isinstance(scalar, Number)
        return R4Vector(*(self.ndarray / scalar))
    
    def project_onto_xyz(self):
        return Vector(self.ndarray[0], self.ndarray[1], self.ndarray[2], 0)


class Point(_R4Vector):
    """
    This represents a point in the affine patch of RP^3, 
    identified with a eucliden point in R^3
    """
    def __init__(self, x, y ,z, w=1):
        assert w != 0
        super().__init__(x, y, z, w)

    def __eq__(self, other):
        assert isinstance(other, Point), f"rhs has type {type(other)}"
        return np.allclose(self.ndarray, other.ndarray)
        #return np.array_equal(self.ndarray, other.ndarray)
        
    def __add__(self, other):
        assert isinstance(other, Vector)
        return super().__add__(other)

    def __sub__(self, other):
        assert isinstance(other, Point) or isinstance(other, Vector)
        return super().__sub__(other)

    def __str__(self):
        return f"Point({round(self.x, 2)}, {round(self.y, 2)}, {round(self.z, 2)})"
    
class Vector(_R4Vector):
    """
    This represents a point at the boundary at infinity in RP^3
    This is identified with a direction in R^3
    """
    def __init__(cls, x, y, z, w=0):
        assert w == 0
        super().__init__(x, y, z, w)

    def __eq__(self, other):
        assert isinstance(other, Vector)
        return np.allclose(self.ndarray, other.ndarray, atol=1e-5)
        #return np.array_equal(self.ndarray, other.ndarray)

    def __str__(self):
        return f"Vector({round(self.x, 5)}, {round(self.y, 5)}, {round(self.z, 5)})"

    def magnitude(self):
        return np.linalg.norm(self.ndarray)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return self
        return Vector(*(self.ndarray / mag))

def R4Vector(x, y, z, w):
    if w == 0:
        return Vector(x, y, z, w)
    else:
        return Point(x, y, z, w)


def magnitude(v):
    assert isinstance(v, Vector)
    return v.magnitude()


def normalize(v):
    assert isinstance(v, Vector)
    return v.normalize()


def dot(v, w):
    assert isinstance(v, Vector), f"v is a {type(v)}"
    assert isinstance(w, Vector), f"w is a {type(w)}"
    return np.dot(v.ndarray, w.ndarray)


def cross(v, w):
    assert isinstance(v, Vector)
    assert isinstance(w, Vector)
    return Vector(*np.cross(v.ndarray[:-1], w.ndarray[:-1]))


def reflect(vecin, normal):
    return vecin - normal * 2 * dot(vecin, normal)