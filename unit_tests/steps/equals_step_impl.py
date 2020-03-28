import ast
import math

import numpy as np

from ray_tracer import *
from ray_tracer.canvas import pixel_at

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
        assert np.array_equal(_lhs, _rhs)
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