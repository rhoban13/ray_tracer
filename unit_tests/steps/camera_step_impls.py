import math

from behave import register_type, step, when
from parse_type import TypeBuilder

from ray_tracer.camera import Camera, ray_for_pixel, render


parse_interesting_angles = TypeBuilder.make_enum({
    "0": 0,
    "π/2": math.pi/2,
    "π": math.pi
})
register_type(InterestingAngle=parse_interesting_angles)


@step(u'{c} = camera({hsize:n}, {vsize:n}, {field_of_view:InterestingAngle})')
def step_impl(context, c, hsize, vsize, field_of_view):
    _c = Camera(hsize, vsize, field_of_view)
    setattr(context, c, _c)


@when(u'{r} = ray_for_pixel({camera}, {x:n}, {y:n})')
def step_impl(context, r, camera, x, y):
    _camera = getattr(context, camera)
    _r = ray_for_pixel(_camera, x, y)
    setattr(context, r, _r)


@when(u'{image} = render({camera}, {world})')
def step_impl(context, image, camera, world):
    _camera = getattr(context, camera)
    _world = getattr(context, world)
    _image = render(_camera, _world)
    setattr(context, image, _image)

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
