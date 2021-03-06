from ray_tracer.colors import Color
from ray_tracer.patterns import (
    stripe_pattern,
    pattern_at_shape,
    set_pattern_transform,
    gradient_pattern,
    ring_pattern,
    checkers_pattern
)
from ray_tracer.transformations import Translation, Scaling
from ray_tracer.tuples import Point

from test_pattern import test_pattern

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


@when(u'{c} = pattern_at_shape({pattern}, {object_}, Point({x:g}, {y:g}, {z:g}))')
def step_impl(context, c, pattern, object_, x, y, z):
    _pattern = getattr(context, pattern)
    _object = getattr(context, object_)
    p = Point(x, y, z)
    _c = pattern_at_shape(_pattern, _object, p)
    setattr(context, c, _c)


@given(u'set_pattern_transform({pattern}, Scaling({dx:g}, {dy:g}, {dz:g}))')
def step_impl(context, pattern, dx, dy, dz):
    _pattern = getattr(context, pattern)
    _pattern = set_pattern_transform(_pattern, Scaling(dx, dy, dz))
    setattr(context, pattern, _pattern)


@step(u'set_pattern_transform({pattern}, Translation({dx:g}, {dy:g}, {dz:g}))')
def step_impl(context, pattern, dx, dy, dz):
    _pattern = getattr(context, pattern)
    _pattern = set_pattern_transform(_pattern, Translation(dx, dy, dz))
    setattr(context, pattern, _pattern)





@given(u'{pattern} = test_pattern()')
def step_impl(context, pattern):
    _pattern = test_pattern()
    setattr(context, pattern, _pattern)


@when(u'{c} = pattern_at_shape({pattern}, {shape}, Point({x:g}, {y:g}, {z:g}))')
def step_impl(context, c, pattern, shape, x, y, z):
    _pattern = getattr(context, pattern)
    _shape = getattr(context, shape)
    p = Point(x, y, z)
    _c = pattern_at_shape(_pattern, _shape, p)
    setattr(context, c, _c)


@given(u'{pattern} = gradient_pattern({color1}, {color2})')
def step_impl(context, pattern, color1, color2):
    _color1 = getattr(context, color1)
    _color2 = getattr(context, color2)
    _pattern = gradient_pattern(_color1, _color2)
    setattr(context, pattern, _pattern)


@given(u'{pattern} = ring_pattern({color1}, {color2})')
def step_impl(context, pattern, color1, color2):
    _color1 = getattr(context, color1)
    _color2 = getattr(context, color2)
    _pattern = ring_pattern(_color1, _color2)
    setattr(context, pattern, _pattern)


@given(u'{pattern} = checkers_pattern({color1}, {color2})')
def step_impl(context, pattern, color1, color2):
    _color1 = getattr(context, color1)
    _color2 = getattr(context, color2)
    _pattern = checkers_pattern(_color1, _color2)
    setattr(context, pattern, _pattern)

# Copyright 2020 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
