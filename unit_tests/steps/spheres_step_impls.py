from ray_tracer import Sphere, intersect, set_transform
from ray_tracer.transformations import Scaling, Translation

@given(u'{s} = Sphere()')
def step_impl(context, s):
    _s = Sphere()
    setattr(context, s, _s)

@when(u'{xs} = intersect({s}, {r})')
def step_impl(context, xs, s, r):
    _s = getattr(context, s)
    _r = getattr(context, r)
    _xs = intersect(_s, _r)
    setattr(context, xs, _xs)


@when(u'set_transform({sphere}, Scaling({dx:g}, {dy:g}, {dz:g}))')
def step_impl(context, sphere, dx, dy, dz):
    _transform = Scaling(dx, dy, dz)
    setattr(context, "transform", _transform)
    context.execute_steps(f'when set_transform({sphere}, transform)')


@when(u'set_transform({sphere}, Translation({dx:g}, {dy:g}, {dz:g}))')
def step_impl(context, sphere, dx, dy, dz):
    _transform = Translation(dx, dy, dz)
    setattr(context, "transform", _transform)
    context.execute_steps(f'when set_transform({sphere}, transform)')


@when(u'set_transform({sphere}, {transform})')
def step_impl(context, sphere, transform):
    _sphere = getattr(context, sphere)
    _transform = getattr(context, transform)
    set_transform(_sphere, _transform)
