import itertools
import re

from behave import given, when, then, step

from ray_tracer.colors import Color
from ray_tracer.lights import point_light
from ray_tracer.shapes import set_transform, Sphere
from ray_tracer.transformations import Scaling, Translation  # noqa
from ray_tracer.tuples import Point
from ray_tracer.world import World, intersect_world, shade_hit, color_at, is_shadowed



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
    for row in itertools.chain([context.table.headings], context.table):
        k, v = row
        if k.startswith('material'):
            _, materialprop = k.split('.')
            if materialprop == "color":
                rgb = [float(p) for p in re.findall('\d+\.?\d*', v)]
                value = Color(*rgb)
            else:
                value = float(v)
            print("setting", materialprop, " to ", value)
            setattr(_s.material, materialprop, value)
        elif k == 'transform':
            value = eval(v)
            _s = set_transform(_s, value)
        else:
            raise NotImplementedError("Unexpected table")
    setattr(context, s, _s)


def default_world():
    light = point_light(Point(-10, 10, -10), Color(1, 1, 1))
    s1 = Sphere()
    s1.material.color = Color(.8, 1.0, .6)
    s1.material.diffuse = .7
    s1.material.specular = .2

    s2 = set_transform(Sphere(), Scaling(.5, .5, .5))

    return World(objects=(s1, s2), light=light)

@step(u'{w} = default_world()')
def step_impl(context, w):
    
    setattr(context, w, default_world())


@then(u'{world} contains {object_}')
def step_impl(context, world, object_):
    _world = getattr(context, world)
    _object = getattr(context, object_)
    print(_object)
    print(_world.objects)
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
