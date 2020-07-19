
from ray_tracer.tuples import R4Vector, Point, Vector, normalize, reflect, is_r4vector
from ray_tracer.colors import Color

@given(u'{name} = R4Vector({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, name, x, y, z, w):
    setattr(context, name,  R4Vector(x, y, z, w))

@given(u'{name} = Point({x:g}, {y:g}, {z:g})')
def step_impl(context, name, x, y, z):
    setattr(context, name, Point(x, y, z))

@given(u'{name} = Vector({x:g}, {y:g}, {z:g})')
def step_impl(context, name, x, y, z):
    setattr(context, name, Vector(x, y, z))

@given(u'{n} = Vector({dx:InterestingTrigValue}, {dy:InterestingTrigValue}, {dz:InterestingTrigValue})')
def step_impl(context, n, dx, dy, dz):
    setattr(context, n, Vector(dx, dy, dz))

@given(u'{name} = Color({red:g}, {green:g}, {blue:g})')
def step_impl(context, name, red, green, blue):
    setattr(context, name, Color(red, green, blue))

@when(u'{name} = normalize({v})')
def step_impl(context, name, v):
    _v = getattr(context, v)
    setattr(context, name, normalize(_v))

@when(u'{a3} = {a1} + {a2}')
def step_impl(context, a3, a1, a2):
    _a1 = getattr(context, a1)
    _a2 = getattr(context, a2)
    setattr(context, a3, _a1 + _a2)

@when(u'{p3} = {p1} - {p2}')
def step_impl(context, p3, p2, p1):
    _p1 = getattr(context, p1)
    _p2 = getattr(context, p2)
    setattr(context, p3, _p1 - _p2)

# @then(u'a is a point')
# def step_impl(context):
#     assert is_point(context.a)
 

# @then(u'a is not a point')
# def step_impl(context):
#     assert not is_point(context.a)
    
# @then(u'a is a vector')
# def step_impl(context):
#     assert is_vector(context.a)

# @then(u'a is not a vector')
# def step_impl(context):
#     assert not is_vector(context.a)



@then(u'{a} projects to a {type_checker:ElementIn3D}')
def step_impl(context, a, type_checker):
    _a = getattr(context, a)
    assert is_r4vector(_a)
    p = _a.project()
    assert type_checker(p)


@then(u'{a} does not project to a {type_checker:ElementIn3D}')
def step_impl(context, a, type_checker):
    _a = getattr(context, a)
    assert is_r4vector(_a)
    p = _a.project()
    assert not type_checker(p)


@then(u'{q} projects to {p}')
def step_impl(context, q, p):
    _q = getattr(context, q)
    _p = getattr(context, p)
    assert is_r4vector(_q)
    assert _q.project() == _p


@when(u'{r} = reflect({v}, {n})')
def step_impl(context, r, v, n):
    _v = getattr(context, v)
    _n = getattr(context, n)
    _r = reflect(_v, _n)
    setattr(context, r, _r)
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
