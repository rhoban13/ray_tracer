from ray_tracer.colors import Color
from ray_tracer.lights import point_light
from ray_tracer.tuples import Point


@step(u'{world}.light = point_light(Point({x:g}, {y:g}, {z:g}), Color({red:g}, {green:g}, {blue:g}))')
def step_impl(context, world, x, y, z, red, green, blue):
    _world = getattr(context, world)
    _world.light = point_light(Point(x, y, z), Color(red, green, blue))


@step(u'{light} = point_light(Point({x:g}, {y:g}, {z:g}), Color({red:g}, {green:g}, {blue:g}))')
def step_impl(context, light, x, y, z, red, green, blue):
    p = Point(x, y, z)
    c = Color(red, green, blue)
    setattr(context, "_p", p)
    setattr(context, "_c", c)
    context.execute_steps('given light = point_light(_p, _c)')


@step(u'{light} = point_light({position}, {intensity})')
def step_impl(context, light, position, intensity):
    _position = getattr(context, position)
    _intensity = getattr(context, intensity)
    _light = point_light(_position, _intensity)
    setattr(context, light, _light)

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
