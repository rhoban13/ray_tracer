from numbers import Number
import numpy as np

from typing import Any

class _R4Vector:
    def __init__(self, ndarray):
        self.ndarray = ndarray

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
        assert isinstance(other, _R4Vector), f"rhs has type {type(other)}"
        return np.allclose(self.ndarray, other.ndarray)

    def __add__(self, other):
        return _R4Vector(self.ndarray + other.ndarray)

    def __sub__(self, other):
        return _R4Vector(self.ndarray - other.ndarray)

    def __neg__(self):
        return _R4Vector(-self.ndarray)

    def __mul__(self, scalar: Number):
        assert isinstance(scalar, Number)
        return _R4Vector(scalar * self.ndarray)
 
    def __truediv__(self, scalar: Number):
        assert isinstance(scalar, Number)
        return _R4Vector(self.ndarray / scalar)
    
    def project_onto_xyz(self):
        _result = self.ndarray.copy()
        _result[3] = 0
        return _Vector(_result)

    def project(self):
        '''return the image of self in the standard affine patch of RP3'''
        if self.ndarray[3] == 0:
            return _Vector(self.ndarray)
        else:
            return _Point(self.ndarray)

class _Point:
    """
    This represents a point in the affine patch of RP^3, 
    identified with a eucliden point in R^3
    """
    def __init__(self, ndarray):
        assert ndarray[3] == 1
        self.ndarray = ndarray

    def __eq__(self, other):
        assert isinstance(other, _Point), f"rhs has type {type(other)}"
        return np.allclose(self.ndarray, other.ndarray)

    def __add__(self, other):
        assert isinstance(other, _Vector)
        return _Point(self.ndarray + other.ndarray)

    def __sub__(self, other):
        return fromndarray(self.ndarray - other.ndarray)

    def __neg__(self):
        return _Point(-self.ndarray)

    def __str__(self):
        return f"_Point({round(self.x, 2)}, {round(self.y, 2)}, {round(self.z, 2)})"
    
    def project_onto_xyz(self):
        _result = self.ndarray.copy()
        _result[3] = 0
        return _Vector(_result)


class _Vector:
    """
    This represents a point at the boundary at infinity in RP^3
    This is identified with a direction in R^3
    """
    def __init__(self, ndarray):
        assert ndarray[3] == 0
        self.ndarray = ndarray

    def __eq__(self, other):
        assert isinstance(other, _Vector)
        return np.allclose(self.ndarray, other.ndarray, atol=1e-5)

    def __add__(self, other):
        assert isinstance(other, _Vector)
        return _Vector(self.ndarray + other.ndarray)

    def __neg__(self):
        return _Vector(-self.ndarray)

    def __sub__(self, other):
        assert isinstance(other, _Vector)
        return _Vector(self.ndarray - other.ndarray)

    def __mul__(self, scalar: Number):
        assert isinstance(scalar, Number)
        return _Vector(scalar * self.ndarray)

    def __str__(self):
        return f"_Vector({round(self.x, 5)}, {round(self.y, 5)}, {round(self.z, 5)})"

    def magnitude(self):
        return np.linalg.norm(self.ndarray)

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return self
        return _Vector(self.ndarray / mag)

    def project_onto_xyz(self):
        return self

# Public creators using individual coordinates
def Point(x, y, z):
    return _Point(np.array((x, y, z, 1)))


def Vector(x, y, z):
    return _Vector(np.array((x, y, z, 0)))


def R4Vector(x, y, z, w):
    return _R4Vector(np.array((x, y, z, w)))


def fromndarray(ndarray):
    if ndarray[3] == 1:
        return _Point(ndarray)
    if ndarray[3] == 0:
        return _Vector(ndarray)
    return _Point(ndarray/ndarray[-1])


def is_point(thing):
    return isinstance(thing, _Point)


def is_vector(thing):
    return isinstance(thing, _Vector)


def is_r4vector(thing):
    return isinstance(thing, _R4Vector)


def magnitude(v):
    assert isinstance(v, _Vector)
    return v.magnitude()


def normalize(v):
    assert isinstance(v, _Vector)
    return v.normalize()


def dot(v, w):
    #assert isinstance(v, _Vector), f"v is a {type(v)}"
    #assert isinstance(w, _Vector), f"w is a {type(w)}"
    return np.dot(v.ndarray, w.ndarray)


def cross(v, w):
    assert isinstance(v, _Vector)
    assert isinstance(w, _Vector)
    return Vector(*(np.cross(v.ndarray[:-1], w.ndarray[:-1])))


def reflect(vecin, normal):
    return vecin - normal * 2 * dot(vecin, normal)