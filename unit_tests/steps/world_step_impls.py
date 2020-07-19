from behave import given, when, then, step

from ray_tracer.colors import Color
from ray_tracer.intersections import Computations
from ray_tracer.lights import point_light
from ray_tracer.shapes import set_transform, Sphere
from ray_tracer.transformations import Scaling, Translation  # noqa
from ray_tracer.tuples import Point
from ray_tracer.world import World, intersect_world, shade_hit, color_at, is_shadowed, reflected_color, refracted_color

from gherkin_table_parser import set_props_from_table


@given(u'{w} = World()')
def step_impl(context, w):
    setattr(context, w, World())


@then(u'{w} contains no objects')
def step_impl(context, w):
    _w = getattr(context, w)
    assert _w.objects is None


@then(u'{w} has no light source')
def step_impl(context, w):
    _w = getattr(context, w)
    assert _w.light is None


@given(u'{s} = Sphere() with')
def step_impl(context, s):
    _s = Sphere()
    set_props_from_table(context, _s)
    setattr(context, s, _s)


def default_world():
    light = point_light(Point(-10, 10, -10), Color(1, 1, 1))
    s1 = Sphere()
    s1.material.color = Color(.8, 1.0, .6)
    s1.material.diffuse = .7
    s1.material.specular = .2

    s2 = set_transform(Sphere(), Scaling(.5, .5, .5))

    return World(objects=[s1, s2], light=light)

@step(u'{w} = default_world()')
def step_impl(context, w):
    setattr(context, w, default_world())


@then(u'{world} contains {object_}')
def step_impl(context, world, object_):
    _world = getattr(context, world)
    _object = getattr(context, object_)
    assert _object in _world.objects


@when(u'{xs} = intersect_world({w}, {r})')
def step_impl(context, xs, w, r):
    _w = getattr(context, w)
    _r = getattr(context, r)
    _xs = intersect_world(_w, _r)
    setattr(context, xs, _xs)


@given(u'{shape} = the {first_or_second} object in {world}')
def step_impl(context, shape, first_or_second, world):
    _world = getattr(context, world)
    if first_or_second == 'first':
        setattr(context, shape, _world.objects[0])
    elif first_or_second == 'second':
        setattr(context, shape, _world.objects[1])
    else:
        raise NotImplementedError('Unknown')


@when(u'{c} = shade_hit({world}, {comps}, {remaining:d})')
def step_impl(context, c, world, comps, remaining):
    _world = getattr(context, world)
    _comps = getattr(context, comps)
    _c = shade_hit(_world, _comps, remaining)
    setattr(context, c, _c)


@when(u'{c} = shade_hit({world}, {comps})')
def step_impl(context, c, world, comps):
    _world = getattr(context, world)
    _comps = getattr(context, comps)
    _c = shade_hit(_world, _comps)
    setattr(context, c, _c)


@when(u'{c} = color_at({w}, {r})')
def step_impl(context, c, w, r):
    _w = getattr(context, w)
    _r = getattr(context, r)
    _c = color_at(_w, _r)
    setattr(context, c, _c)


@then(u'is_shadowed({w}, {p}) is false')
def step_impl(context, w, p):
    _w = getattr(context, w)
    _p = getattr(context, p)
    assert not is_shadowed(_w, _p)


@then(u'is_shadowed({w}, {p}) is true')
def step_impl(context, w, p):
    _w = getattr(context, w)
    _p = getattr(context, p)
    assert is_shadowed(_w, _p)


@given(u'{s} is added to {world}')
def step_impl(context, s, world):
    _s = getattr(context, s)
    _world = getattr(context, world)
    _world.add_object(_s)

@when(u'{color} = reflected_color({w}, {comps}, {remaining:g})')
def step_impl(context, color, w, comps, remaining):
    _w = getattr(context, w)
    _comps = getattr(context, comps)
    _color = reflected_color(_w, _comps, remaining)
    setattr(context, color, _color)


@when(u'{color} = reflected_color({w}, {comps})')
def step_impl(context, color, w, comps):
    _w = getattr(context, w)
    _comps = getattr(context, comps)
    _color = reflected_color(_w, _comps)
    setattr(context, color, _color)


@then(u'color_at({w}, {r}) should terminate successfully')
def step_impl(context, w, r):
    _w = getattr(context, w)
    _r = getattr(context, r)

    # This will raise RecursionError if we don't terminate successfully
    color_at(_w, _r)


@when(u'{c} = refracted_color({w}, {comps}, {remaining:d})')
def step_impl(context, c, w, comps, remaining):
    _w = getattr(context, w)
    assert isinstance(_w, World)

    _comps = getattr(context, comps)
    assert isinstance(_comps, Computations)

    _c = refracted_color(_w, _comps, remaining)
    setattr(context, c, _c)


@given(u'{shape} has')
def step_impl(context, shape):
    _shape = getattr(context, shape)
    set_props_from_table(context, _shape)


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
