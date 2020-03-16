from ray_tracer.canvas import Canvas, pixel_at, write_pixel, canvas_to_ppm
from ray_tracer import Color

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

@then(u'lines {start:d}-{end:d} of {ppm} are')
def step_impl(context, start, end, ppm):
    _ppm = getattr(context, ppm)[start-1:end]
    body_lines = context.text.split("\n")
    print(_ppm)
    print(body_lines)
    assert len(_ppm) == len(body_lines)

    for i in range(len(_ppm)):
        assert _ppm[i] == body_lines[i], f"{_ppm[i]} != {body_lines[i]}"

