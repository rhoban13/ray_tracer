import math

from behave import register_type, step, when
from parse_type import TypeBuilder

from ray_tracer.camera import Camera, ray_for_pixel


parse_interesting_angles = TypeBuilder.make_enum({
    "0": 0,
    "π/2": math.pi/2,
    "π": math.pi
})
register_type(InterestingAngle=parse_interesting_angles)


@step(u'{c} = camera({hsize:g}, {vsize:g}, {field_of_view:InterestingAngle})')
def step_impl(context, c, hsize, vsize, field_of_view):
    _c = Camera(hsize, vsize, field_of_view)
    setattr(context, c, _c)


@when(u'{r} = ray_for_pixel({camera}, {x:g}, {y:g})')
def step_impl(context, r, camera, x, y):
    _camera = getattr(context, camera)
    _r = ray_for_pixel(_camera, x, y)
    setattr(context, r, _r)
