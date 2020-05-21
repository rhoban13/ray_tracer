import math

import numpy as np

from ray_tracer.tuples import (
    fromndarray, is_point, is_vector, is_r4vector,
    cross, normalize
)


class Transformation:
    __slots__ = ('ndarray', '_inverse_ndarray', '_inverse_transformation', '_transpose_transformation')

    def __init__(self, arr, inverse_ndarray=None):
        self.ndarray = np.array(arr)
        if inverse_ndarray is not None:
            self._inverse_ndarray = inverse_ndarray
        elif np.linalg.det(self.ndarray) != 0:
            self._inverse_ndarray = np.linalg.inv(self.ndarray)
        else:
            self._inverse_ndarray = None

        # Lazily set
        self._inverse_transformation = None
        self._transpose_transformation = None

    def inverse(self):
        assert self._inverse_ndarray is not None
        if self._inverse_transformation is None:
            self._inverse_transformation = Transformation(self._inverse_ndarray, self.ndarray)
            self._inverse_transformation._inverse_transformation = self  # circular ref, should use weak ref
        return self._inverse_transformation

    def transpose(self):
        if self._transpose_transformation is None:
            self._transpose_transformation = Transformation(np.transpose(self.ndarray))
        self._transpose_transformation._transpose_transformation = self  # circular ref, should use weak ref
        return self._transpose_transformation

    def linear_component(self):
        '''Return the linear piece of this projective transformation'''
        c = self.ndarray.copy()
        for i in range(2):
            c[(3, i)] = 0
            c[(i, 3)] = 0
        return Transformation(c, np.linalg.inv(c))

    def det(self):
        return np.linalg.det(self.ndarray)

    def __mul__(self, other):
        if is_point(other) or is_vector(other):
            return fromndarray(np.dot(self.ndarray, other.ndarray))
        elif is_r4vector(other):
            return other.__class__(np.dot(self.ndarray, other.ndarray))
        elif isinstance(other, Transformation):
            return Transformation(np.dot(self.ndarray, other.ndarray))

    def __eq__(self, other):
        assert isinstance(other, Transformation)
        return np.allclose(self.ndarray, other.ndarray, atol=1e-5)

    def __str__(self):
        return str(self.ndarray)

    @property
    def shape(self):
        return self.ndarray.shape

    def __getitem__(self, indexes_tuple):
        assert len(indexes_tuple) == 2
        assert isinstance(indexes_tuple, tuple)
        return self.ndarray[indexes_tuple]


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
        # Note - Left hand rule!
        super().__init__([
                [math.cos(radians), 0, math.sin(radians), 0],
                [0, 1, 0, 0],
                [-math.sin(radians), 0, math.cos(radians), 0],
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


def transpose(transformation):
    return transformation.transpose()


def view_transform(from_, to, up):
    forward = normalize(to - from_)
    left = cross(forward, normalize(up))
    true_up = cross(left, forward)
    orientation = Transformation(np.stack((
        left.ndarray,
        true_up.ndarray,
        -forward.ndarray,
        [0, 0, 0, 1]
    )))
    translation = Translation(-from_.x, -from_.y, -from_.z)
    return orientation * translation
