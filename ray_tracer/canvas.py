import cv2
import numpy as np

from . import Color

class Canvas:
    def __init__(self, width, height):
        self._image = np.zeros((height, width, 3), dtype=np.uint8)

    @property
    def width(self):
        return self._image.shape[1]
    
    @property
    def height(self):
        return self._image.shape[0]

    def pixel_at(self, x, y):
        return Color(*(self._image[y][x]))
    
    def write_pixel(self, x, y, color):
        self._image[y][x] = (color.red, color.green, color.blue)
    
def pixel_at(canvas, x, y):
    return canvas.pixel_at(x, y)

def write_pixel(canvas, x, y, color):
    canvas.write_pixel(x, y, color)

def canvas_to_ppm(canvas):
    cv2.imwrite("foo.ppm", canvas._image)
    with open("foo.ppm") as f:
        return f.read().split("\n")
