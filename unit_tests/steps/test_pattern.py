from ray_tracer.colors import Color
from ray_tracer.patterns import Pattern, TransformedPattern
from ray_tracer.transformations import Identity


class TestPattern(Pattern):
    def pattern_at(self, point):
        return Color(point.x, point.y, point.z)


def test_pattern():
    return TransformedPattern(TestPattern(), Identity())

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
