import math

from ray_tracer.intersections import intersect
from ray_tracer.sphere import Sphere, set_transform, normal_at
from ray_tracer.transformations import Scaling, Translation, rotation_z
from ray_tracer.tuples import Point


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


@step(u'set_transform({sphere}, Translation({dx:g}, {dy:g}, {dz:g}))')
def step_impl(context, sphere, dx, dy, dz):
    _transform = Translation(dx, dy, dz)
    setattr(context, "transform", _transform)
    context.execute_steps(f'when set_transform({sphere}, transform)')


@when(u'{n} = normal_at({s}, Point({x:g}, {y:g}, {z:g}))')
def step_impl(context, n, s, x, y, z):
    _s = getattr(context, s)
    _p = Point(x, y, z)
    _n = normal_at(_s, _p)
    setattr(context, n, _n)

@when(u'n = normal_at({s}, Point(√3/3, √3/3, √3/3))')
def step_impl(context, s):
    _val = math.sqrt(3)/3
    context.execute_steps(f'when n = normal_at({s}, Point({_val}, {_val}, {_val}))')


@given(u'{m} = Scaling(1, 0.5, 1) * rotation_z(π/5)')
def step_impl(context, m):
    _m = Scaling(1, 0.5, 1) * rotation_z(math.pi/5)
    setattr(context, m, _m)


@step(u'set_transform({s}, {m})')
def step_impl(context, s, m):
    _s = getattr(context, s)
    _m = getattr(context, m)
    set_transform(_s, _m)


@when(u'{n} = normal_at({s}, Point(0, √2/2, -√2/2))')
def step_impl(context, n, s):
    _val = math.sqrt(2)/2
    context.execute_steps(f'when {n} = normal_at({s}, Point(0, {_val}, -{_val}))')


# @when(u'{lhs} = {rhs}.{property_}')
# def step_impl(context, lhs, rhs, property_):
#     _rhs = getattr(context, rhs)
#     _lhs = getattr(_rhs, property_)
#     setattr(context, lhs, _lhs)

@step(u'{thing}.{property_} = {value:g}')
def step_impl(context, thing, property_, value):
    _thing = getattr(context, thing)
    setattr(_thing, property_, value)

@step(u'{thing}.{property_} = {value}')
def step_impl(context, thing, property_, value):
    _thing = getattr(context, thing)
    _value = getattr(context, value)
    setattr(_thing, property_, _value)

@when(u'{m} = {s}.material')
def step_impl(context, m, s):
    _s = getattr(context, s)
    setattr(context, m, _s.material)

