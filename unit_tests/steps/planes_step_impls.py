from behave import given, then

from ray_tracer.plane import Plane


@given(u'{p} = Plane()')
def step_impl(context, p):
    _p = Plane()
    setattr(context, p, _p)


@then(u'{xs} is empty')
def step_impl(context, xs):
    _xs = getattr(context, xs)
    assert not _xs
