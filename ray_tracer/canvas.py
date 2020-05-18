import cv2
import numpy as np

from ray_tracer.colors import Color

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
        pixel = color.to_pixel()
        self._image[y][x] = pixel

def pixel_at(canvas, x, y):
    return canvas.pixel_at(x, y)

def write_pixel(canvas, x, y, color):
    canvas.write_pixel(x, y, color)

def canvas_to_ppm(canvas):
    '''
    opencv uses BGR, our Canvas uses RGB.  
    Transform that here before writing
    '''
    as_bgr = np.flip(canvas._image, 2)
    cv2.imwrite("foo.ppm", as_bgr)
    image = cv2.imread("foo.ppm")
    return np.flip(image, 2)

def canvas_to_png(filepath, canvas):
    '''
    opencv uses BGR, our Canvas uses RGB.  
    Transform that here before writing
    '''
    as_bgr = np.flip(canvas._image, 2)
    cv2.imwrite(filepath, canvas._image)
