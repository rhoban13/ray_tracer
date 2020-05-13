import math

from behave import register_type
from parse_type import TypeBuilder

from ray_tracer._rp3_points import _Point
from ray_tracer.transformations import (
    inverse, Translation, Scaling, 
    rotation_x, rotation_y, rotation_z,
    Shearing, Transformation
)

@given(u'{transform} = Translation({x:g}, {y:g}, {z:g})')
def step_impl(context, transform, x, y, z):
    _transform = Translation(x, y, z)
    setattr(context, transform, _transform)

@given(u'{transform} = Scaling({x:g}, {y:g}, {z:g})')
def step_impl(context, transform, x, y, z):
    _transform = Scaling(x, y, z)
    setattr(context, transform, _transform)

@given(u'{name} = inverse({transform})')
def step_impl(context, name, transform):
    _transform = getattr(context, transform)
    inv = inverse(_transform)
    setattr(context, name, inv)

parse_rotation_axis = TypeBuilder.make_enum({
    "rotation_x": rotation_x, 
    "rotation_y": rotation_y,
    "rotation_z": rotation_z
})
register_type(RotationBy=parse_rotation_axis)

@given(u'{transform} = {rotation:RotationBy}(π / {n:g})')
def step_impl(context, transform, rotation, n):
    _transform = rotation(math.pi/n)
    setattr(context, transform, _transform)

@given(u'{transform} = Shearing({xy:g}, {xz:g}, {yx:g}, {yz:g}, {zx:g}, {zy:g})')
def step_impl(context, transform, xy, xz, yx, yz, zx, zy):
    _transform = Shearing(xy, xz, yx, yz, zx, zy)
    setattr(context, transform, _transform)

@when(u'{lhs} = {C} * {B} * {A}')
def step_impl(context, lhs, C, B, A):
    _A = getattr(context, A)
    _B = getattr(context, B)
    _C = getattr(context, C)
    assert isinstance(_A, Transformation)
    assert isinstance(_B, Transformation)
    assert isinstance(_C, Transformation)
    _lhs = _C * _B * _A
    setattr(context, lhs, _lhs)

@when(u'{lhs} = {T} * {p}')
def step_impl(context, lhs, T, p):
    _T = getattr(context, T)
    _p = getattr(context, p)
    assert isinstance(_T, Transformation), print(f"{_T} is not a Transformation")
    assert isinstance(_p, _Point), print(f"{_p} is not a Point")

    _lhs = _T * _p
    setattr(context, lhs, _lhs)

