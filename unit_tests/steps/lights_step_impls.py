from ray_tracer import point_light, Point, Color


@step(u'{light} = point_light(Point({x:g}, {y:g}, {z:g}), Color({red:g}, {green:g}, {blue:g}))')
def step_impl(context, light, x, y, z, red, green, blue):
    p = Point(x, y, z)
    c = Color(red, green, blue)
    setattr(context, "_p", p)
    setattr(context, "_c", c)
    context.execute_steps(f'given light = point_light(_p, _c)')



@step(u'{light} = point_light({position}, {intensity})')
def step_impl(context, light, position, intensity):
    _position = getattr(context, position)
    _intensity = getattr(context, intensity)
    _light = point_light(_position, _intensity)
    setattr(context, light, _light)
