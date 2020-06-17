from ray_tracer.colors import Color
from ray_tracer.patterns import stripe_at, stripe_pattern

@given(u'{material}.pattern = stripe_pattern(Color({r1:g}, {g1:g}, {b1:g}), Color({r2:g}, {g2:g}, {b2:g}))')
def step_impl(context, material, r1, g1, b1, r2, g2, b2):
    _material = getattr(context, material)
    _material.pattern = stripe_pattern(Color(r1, g1, b1), Color(r2, g2, b2))
    setattr(context, material, _material)


@given(u'{pattern} = stripe_pattern(Color({r1:g}, {g1:g}, {b1:g}), Color({r2:g}, {g2:g}, {b2:g}))')
def step_impl(context, pattern, r1, g1, b1, r2, g2, b2):
    _pattern = stripe_pattern(Color(r1, g1, b1), Color(r2, g2, b2))
    setattr(context, pattern, _pattern)


@given(u'{pattern} = stripe_pattern({color1}, {color2})')
def step_impl(context, pattern, color1, color2):
    _color1 = getattr(context, color1)
    _color2 = getattr(context, color2)
    _pattern = stripe_pattern(_color1, _color2)
    setattr(context, pattern, _pattern)
