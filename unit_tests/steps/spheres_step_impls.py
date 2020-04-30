from ray_tracer import Sphere, intersect

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
