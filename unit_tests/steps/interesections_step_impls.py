from behave import register_type
from parse_type import TypeBuilder

from ray_tracer.intersections import Intersection, Intersections, hit, prepare_computations, EPSILON
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


@then(u'comps.over_point.z < -EPSILON/2')
def step_impl(context):
    _comps = getattr(context, "comps")
    assert _comps.over_point.z < - EPSILON/2



@then(u'comps.point.z > comps.over_point.z')
def step_impl(context):
    _comps = getattr(context, "comps")
    assert _comps.point.z > _comps.over_point.z

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
