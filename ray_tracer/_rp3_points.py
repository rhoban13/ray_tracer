from numbers import Number
import numpy as np

from typing import Any

class _R4Vector:
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
        return R4Vector(*(self.ndarray + other.ndarray))

    def __sub__(self, other):
        return R4Vector(*(self.ndarray - other.ndarray))

    def __neg__(self):
        return R4Vector(*(-self.ndarray))

    def __mul__(self, scalar: Number):
        assert isinstance(scalar, Number)
        return R4Vector(*(scalar * self.ndarray))
 
    def __truediv__(self, scalar: Number):
        assert isinstance(scalar, Number)
        return R4Vector(*(self.ndarray / scalar))
    
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        if method != "__call__":
            return NotImplemented

        my_inputs = []
        for input in inputs:
            if isinstance(input, self.__class__):
                my_inputs.append(input.ndarray)
            else:
                my_inputs.append(input)
        
        from_base = ufunc(*my_inputs, **kwargs)
        return self.__class__(*from_base)
        

    def __array_function__(self, func, types, args, kwargs):
        if func not in HANDLED_FUNCTIONS:
            return NotImplemented
        # https://docs.scipy.org/doc/numpy/user/basics.dispatch.html
        if types != (np.ndarray, self.__class__):
            return NotImplemented
        return HANDLED_FUNCTIONS[func](*args, **kwargs)

HANDLED_FUNCTIONS = dict()

def implements(np_function):
    "Register an __array_function__ implementation for DiagonalArray objects."
    def decorator(func):
        HANDLED_FUNCTIONS[np_function] = func
        return func
    return decorator

@implements(np.dot)
def dot(A, b):
    return R4Vector(*(A.dot(b.ndarray)))

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
        return np.array_equal(self.ndarray, other.ndarray)

    def __str__(self):
        return f"Vector({round(self.x, 2)}, {round(self.y, 2)}, {round(self.z, 2)})"


def R4Vector(x, y, z, w):
    if w == 0:
        return Vector(x, y, z, w)
    else:
        return Point(x, y, z, w)


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
