import ast
import math

import numpy as np

from ray_tracer.canvas import pixel_at
from ray_tracer.colors import Color
from ray_tracer.material import Material
from ray_tracer.patterns import pattern_at
from ray_tracer.rays import position
from ray_tracer.transformations import Transformation, Scaling, Translation, Identity
from ray_tracer.tuples import Point, R4Vector, Vector, normalize, magnitude, dot, cross


def _get_names_needed(*expressions):
    output = set()
    for expr in expressions:
        root = ast.parse(expr)
        names =  set(node.id for node in ast.walk(root) if isinstance(node, ast.Name))
        output.update(names)
    return output


@then(u'{lhs} == {rhs}')
def step_impl(context, lhs, rhs):
    _locals = {
        'sqrt': math.sqrt
    }
    for name in _get_names_needed(lhs, rhs):
        if name in globals():
            continue
        if name in _locals:
            continue
        assert name in context, f"{name} is not in context"
        _locals[name] = getattr(context, name)

    _lhs = eval(lhs, globals(), _locals)
    _rhs = eval(rhs, globals(), _locals)
    if isinstance(_lhs, np.ndarray) and isinstance(_rhs, np.ndarray):
        assert np.allclose(_lhs, _rhs, atol=1e-05), f"{_lhs} != {_rhs}"
    else:
        assert _lhs == _rhs, f"{_lhs} != {_rhs}"


@then(u'{lhs} != {rhs}')
def step_impl(context, lhs, rhs):
    try:
        context.execute_steps(f"then {lhs} == {rhs}")
    except AssertionError:
        pass
    else:
        assert False, f"{lhs} == {rhs}"

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
