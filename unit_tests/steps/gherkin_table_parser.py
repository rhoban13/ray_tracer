import itertools
import re

from ray_tracer.colors import Color
from ray_tracer.transformations import Scaling, Translation  # noqa: F401

from test_pattern import test_pattern


def set_props_from_table(context, shape):
    for row in itertools.chain([context.table.headings], context.table):
        k, v = row
        if k.startswith('material'):
            _, materialprop = k.split('.')
            if materialprop == "color":
                rgb = [float(p) for p in re.findall('\d+\.?\d*', v)]
                value = Color(*rgb)
            elif materialprop == "pattern":
                if v != "test_pattern()":
                    raise NotImplementedError("Only test_pattern is implemented")
                value = test_pattern()
            else:
                value = float(v)
            setattr(shape.material, materialprop, value)
        elif k == "transform":
            t = eval(v)
            shape.transform = t
        else:
            raise NotImplementedError(f"{k} is not implemented")

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
