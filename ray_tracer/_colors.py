from numbers import Number
from math import isclose

class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __eq__(self, other):
        assert isinstance(other, Color)
        return isclose(self.red, other.red) and \
               isclose(self.green, other.green) and \
               isclose(self.blue, other.blue)
    
    def __add__(self, other):
        assert isinstance(other, Color)
        return Color(self.red + other.red, \
                     self.green + other.green, \
                     self.blue + other.blue)
    def __sub__(self, other):
        assert isinstance(other, Color)
        return Color(self.red - other.red, \
                     self.green - other.green, \
                     self.blue - other.blue)

    def __mul__(self, other):
        if isinstance(other, Number):
            return Color(other*self.red, other*self.green, other*self.blue)
        elif isinstance(other, Color):
            return Color(self.red * other.red,
                         self.green * other.green,
                         self.blue  * other.blue)
        else:
            raise TypeError(f"Unexpected type {type(other)}")

    def __str__(self):
        return f"Color({self.red}, {self.green}, {self.blue})"
