from behave import register_type
from parse_type import TypeBuilder

from ray_tracer.intersections import Intersection, Intersections, hit, prepare_computations
from ray_tracer.rays import Ray


@step(u'{i} = Intersection({t:g}, {obj})')
def step_impl(context, i, t, obj):
    _obj = getattr(context, obj)
    _i = Intersection(t, _obj)
    setattr(context, i, _i)


list_of_strings = TypeBuilder.make_list(str)
register_type(ListOfStrings=list_of_strings)

@step(u'{xs} = Intersections({args:ListOfStrings})')
def step_impl(context, xs, args):
    list_of_intersection = [getattr(context, i) for i in args]
    _xs = Intersections(*list_of_intersection)
    setattr(context, xs, _xs)


@when(u'{i} = hit({xs})')
def step_impl(context, i, xs):
    _xs = getattr(context, xs)
    _i = hit(_xs)
    setattr(context, i, _i)


@then(u'{i} is nothing')
def step_impl(context, i):
    _i = getattr(context, i)
    assert _i is None


@when(u'{comps} = prepare_computations({i}, {r})')
def step_impl(context, comps, i, r):
    _i = getattr(context, i)
    assert isinstance(_i, Intersection)
    _r = getattr(context, r)
    assert isinstance(_r, Ray)

    _comps = prepare_computations(_i, _r)
    setattr(context, comps, _comps)