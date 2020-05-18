import itertools
import re

from ray_tracer.colors import Color
from ray_tracer.sphere import Sphere
from ray_tracer.transformations import Scaling
from ray_tracer.world import World, default_world, intersect_world, shade_hit

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
        print(row)
        k,v = row
        print("WTF", k)
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
            _s.transform = value
        else:
            raise NotImplementedError("Unexpected table")
    setattr(context, s, _s)


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


@when(u'{c} = shade_hit({world}, {comps})')
def step_impl(context, c, world, comps):
    _world = getattr(context, world)
    _comps = getattr(context, comps)
    _c = shade_hit(_world, _comps)
    setattr(context, c, _c)
