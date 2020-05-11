from numbers import Number
from math import isclose

import numpy as np


class Color:
    def __init__(self, red, green, blue):
        self.ndarray = np.array((red, green, blue))
    
    @property
    def red(self):
        return self.ndarray[0]
    
    @property
    def green(self):
        return self.ndarray[1]
    
    @property
    def blue(self):
        return self.ndarray[2]

    def __eq__(self, other):
        assert isinstance(other, Color), f"Can't compare {type(other)}"
        return self.to_pixel() == other.to_pixel()
    
    def __add__(self, other):
        assert isinstance(other, Color)
        return Color(*(self.ndarray + other.ndarray))

    def __sub__(self, other):
        assert isinstance(other, Color)
        return Color(*(self.ndarray-other.ndarray))

    def __mul__(self, other):
        if isinstance(other, Number):
            return Color(*(other*self.ndarray))
        elif isinstance(other, Color):
            return self._hadamard_product(other)
        else:
            raise TypeError(f"Unexpected type {type(other)}")

    def __str__(self):
        return f"Color({self.red}, {self.green}, {self.blue})"

    def _hadamard_product(self, other):
        return Color(*(np.multiply(self.ndarray, other.ndarray)))

    def to_pixel(self):
        """Return a tuple for self where each component is an int between 0 & 255"""
        def truncate(x):
            if x > 1:
                return 255
            if x < 0:
                return 0
            return round(255 * x)
        return tuple( truncate(x) for x in self.ndarray)

RED = Color(1, 0, 0)
GREEN = Color(0, 1, 0)
BLUE = Color(0, 0, 1)
BLACK = Color(0, 0, 0)
WHITE = Color(1, 1, 1)