from behave import register_type, given, when
from parse_type import TypeBuilder

from ray_tracer.material import Material, lighting
from ray_tracer.tuples import Point


@given(u'{m} = Material()')
def step_impl(context, m):
    _m = Material()
    setattr(context, m, _m)


parse_bool = TypeBuilder.make_enum({"True": True, "False": False})
register_type(BoolType=parse_bool)



@when(u'{result} = lighting({material}, {object_}, {light}, Point({x:g},{y:g},{z:g}), {eyev}, {normalv}, {in_shadow:BoolType})')
def step_impl(context, result, material, object_, light, x, y, z, eyev, normalv, in_shadow):
    _position = Point(x, y, z)
    setattr(context, "position", _position)
    context.execute_steps(f"when {result} = lighting({material}, {object_}, {light}, position, {eyev}, {normalv}, {in_shadow})")


@when(u'{result} = lighting({material}, {object_}, {light}, {position}, {eyev}, {normalv}, {in_shadow:BoolType})')
def step_impl(context, result, material, object_, light, position, eyev, normalv, in_shadow):
    _material = getattr(context, material)
    _object = getattr(context, object_)
    _light = getattr(context, light)
    _position = getattr(context, position)
    _eyev = getattr(context, eyev)
    _normalv = getattr(context, normalv)

    _result = lighting(_material, _object, _light, _position, _eyev, _normalv, in_shadow)
    setattr(context, result, _result)


@when(u'{result} = lighting({material}, {object_}, {light}, {position}, {eyev}, {normalv})')
def step_impl(context, result, material, object_, light, position, eyev, normalv):
    context.execute_steps(f"when {result} = lighting({material}, {object_}, {light}, {position}, {eyev}, {normalv}, False)")

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
