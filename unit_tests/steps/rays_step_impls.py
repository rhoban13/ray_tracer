from ray_tracer.rays import Ray, transform, position
from ray_tracer.tuples import Point, Vector


@when(u'{r} = Ray({origin}, {direction})')
def step_impl(context, r, origin, direction):
    _origin = getattr(context, origin)
    _direction = getattr(context, direction)
    _r = Ray(_origin, _direction)
    setattr(context, r, _r)


@given(u'{r} = Ray(Point({x:g}, {y:g}, {z:g}), Vector({dx:g}, {dy:g}, {dz:g}))')
def step_impl(context,r, x, y, z, dx, dy, dz):
    _r = Ray(Point(x, y, z), Vector(dx, dy, dz))
    setattr(context, r, _r)


@when(u'{ray_out} = transform({ray_in}, {matrix})')
def step_impl(context, ray_out, ray_in, matrix):
    _ray_in = getattr(context, ray_in)
    _matrix = getattr(context, matrix)
    _ray_out = transform(_ray_in, _matrix)
    setattr(context, ray_out, _ray_out)
