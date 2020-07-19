import math

from ray_tracer.rays import Ray, transform, position
from ray_tracer.tuples import Point, Vector



# @step(u'{r} = Ray(Point({x:InterestingRealNumbers}, {y:InterestingRealNumbers}, {z:InterestingRealNumbers}), Vector({dx:InterestingRealNumbers}, {dy:InterestingRealNumbers}, {dz:InterestingRealNumbers}))')
# def step_impl(context, r, x, y, z, dx, dy, dz):
#     _r = Ray(Point(x, y, z), Vector(dx, dy, dz))
#     setattr(context, r, _r)

@step(u'{r} = Ray(Point({x:g}, {y:g}, {z:g}), Vector({dx:g}, {dy:g}, {dz:g}))')
def step_impl(context, r, x, y, z, dx, dy, dz):
    _r = Ray(Point(x, y, z), Vector(dx, dy, dz))
    setattr(context, r, _r)


@step(u'{r} = Ray(Point({x:InterestingTrigValue}, {y:InterestingTrigValue}, {z:InterestingTrigValue}), Vector({dx:InterestingTrigValue}, {dy:InterestingTrigValue}, {dz:InterestingTrigValue}))')
def step_impl(context, r, x, y, z, dx, dy, dz):
    context.execute_steps(f"given {r} = Ray(Point({x}, {y}, {z}), Vector({dx}, {dy}, {dz}))")


@step(u'{r} = Ray({origin}, {direction})')
def step_impl(context, r, origin, direction):
    _origin = getattr(context, origin)
    _direction = getattr(context, direction)
    _r = Ray(_origin, _direction)
    setattr(context, r, _r)


@when(u'{ray_out} = transform({ray_in}, {matrix})')
def step_impl(context, ray_out, ray_in, matrix):
    _ray_in = getattr(context, ray_in)
    _matrix = getattr(context, matrix)
    _ray_out = transform(_ray_in, _matrix)
    setattr(context, ray_out, _ray_out)

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
