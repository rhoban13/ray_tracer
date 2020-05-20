from ray_tracer.colors import Color
from ray_tracer.lights import point_light
from ray_tracer.tuples import Point


@step(u'{world}.light = point_light(Point({x:g}, {y:g}, {z:g}), Color({red:g}, {green:g}, {blue:g}))')
def step_impl(context, world, x, y, z, red, green, blue):
    _world = getattr(context, world)
    _world.light = point_light(Point(x, y, z), Color(red, green, blue))


@step(u'{light} = point_light(Point({x:g}, {y:g}, {z:g}), Color({red:g}, {green:g}, {blue:g}))')
def step_impl(context, light, x, y, z, red, green, blue):
    p = Point(x, y, z)
    c = Color(red, green, blue)
    setattr(context, "_p", p)
    setattr(context, "_c", c)
    context.execute_steps('given light = point_light(_p, _c)')


@step(u'{light} = point_light({position}, {intensity})')
def step_impl(context, light, position, intensity):
    _position = getattr(context, position)
    _intensity = getattr(context, intensity)
    _light = point_light(_position, _intensity)
    setattr(context, light, _light)
