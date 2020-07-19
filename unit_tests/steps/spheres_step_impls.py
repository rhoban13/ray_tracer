import math

from behave import given, when, step

from ray_tracer.intersections import intersect
from ray_tracer.shapes import set_transform, Sphere
from ray_tracer.transformations import Scaling, Translation, rotation_z
from ray_tracer.tuples import Point

from gherkin_table_parser import set_props_from_table

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


@step(u'set_transform({sphere}, Scaling({dx:g}, {dy:g}, {dz:g}))')
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
    _n = _s.normal_at(_p)
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
    _s = set_transform(_s, _m)
    setattr(context, s, _s)

@when(u'{n} = normal_at({s}, Point(0, √2/2, -√2/2))')
def step_impl(context, n, s):
    _val = math.sqrt(2)/2
    context.execute_steps(f'when {n} = normal_at({s}, Point(0, {_val}, -{_val}))')


@step(u'{thing}.{property_}.{other_property_} = {value:g}')
def step_impl(context, thing, property_, other_property_, value):
    _thing = getattr(context, thing)
    _property = getattr(_thing, property_)
    setattr(_property, other_property_, value)


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

def glass_sphere():
    s = Sphere()
    s.material.transparency = 1.0
    s.material.refractive_index = 1.5
    return s


@given(u'{s} = glass_sphere()')
def step_impl(context, s):
    _s = glass_sphere()
    setattr(context, s, _s)


@given(u'{s} = glass_sphere() with')
def step_impl(context, s):
    _s = glass_sphere()
    set_props_from_table(context, _s)
    setattr(context, s, _s)


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
