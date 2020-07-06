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
        return Color(*(self._image[y][x])/255)

    def write_pixel(self, x, y, color):
        pixel = color.to_pixel()
        self._image[y][x] = pixel


def overlay(*canvases):
    '''Create a new canvas by overlaying canvasses on top of each other'''
    output_ndarray = np.sum(canvas._image for canvas in canvases)
    shape = output_ndarray.shape
    assert shape[2] == 3
    output = Canvas(shape[0], shape[1])
    output._image = output_ndarray
    return output


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
    # as_bgr = np.flip(canvas._image, 2)
    cv2.imwrite(filepath, canvas._image)

# Copyright 2020 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
