import numpy as np

from ray_tracer.canvas import Canvas, pixel_at, write_pixel, canvas_to_ppm
from ray_tracer.colors import Color

@given(u'{name} = Canvas({width:d}, {height:d})')
def step_impl(context, name, width, height):
    c = Canvas(width, height)
    setattr(context, name, Canvas(width, height))


@when(u'write_pixel({canvas}, {x:d}, {y:d}, {color})')
def step_impl(context, canvas, x, y, color):
    _canvas = getattr(context, canvas)
    _color = getattr(context, color)
    write_pixel(_canvas, x, y, _color) 


@then(u'every pixel of {canvas} is Color(0, 0, 0)')
def step_impl(context, canvas):
    c = getattr(context, canvas)
    for i in range(0, c.width):
        for j in range(0, c.height):
            assert pixel_at(c, i, j) == Color(0, 0, 0)


@then(u'pixel_at({canvas}, {x:d}, {y:d}) = {color}')
def step_impl(context, canvas, x, y, color):
    c = getattr(context, canvas)
    pixel_at(c, x, y)


@when(u'{ppm} = canvas_to_ppm({canvas})')
def step_impl(context, ppm, canvas):
    _canvas = getattr(context, canvas)
    _ppm = canvas_to_ppm(_canvas)
    setattr(context, ppm, _ppm)


@then(u'the body of {ppm} is')
def step_impl(context, ppm):
    _ppm = getattr(context, ppm)
    expected_lines = context.text.split("\n")
    lines = tuple(int(x) for line in expected_lines for x in line.split(" "))
    lines = np.reshape(lines, _ppm.shape)
    assert np.array_equal(lines, _ppm)

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
