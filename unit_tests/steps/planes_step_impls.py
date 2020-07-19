from behave import given, then

from ray_tracer.shapes import Plane

from gherkin_table_parser import set_props_from_table


@given(u'{p} = Plane()')
def step_impl(context, p):
    _p = Plane()
    setattr(context, p, _p)


@then(u'{xs} is empty')
def step_impl(context, xs):
    _xs = getattr(context, xs)
    assert not _xs


@given(u'{shape} = Plane() with')
def step_impl(context, shape):
    _shape = Plane()
    set_props_from_table(context, _shape)
    setattr(context, shape, _shape)

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
