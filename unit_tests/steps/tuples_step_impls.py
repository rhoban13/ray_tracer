import ast

from ray_tracer import * # ugh

@given(u'{name} = RP3Point({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, name, x, y, z, w):
    setattr(context, name,  RP3Point(x, y, z, w))

@given(u'{name} = Point({x:g}, {y:g}, {z:g})')
def step_impl(context, name, x, y, z):
    setattr(context, name, Point(x, y, z))

@given(u'{name} = Vector({x:g}, {y:g}, {z:g})')
def step_impl(context, name, x, y, z):
    setattr(context, name, Vector(x, y, z))

@given(u'{name} = Color({red:g}, {green:g}, {blue:g})')
def step_impl(context, name, red, green, blue):
    setattr(context, name, Color(red, green, blue))

@when(u'{name} = normalize({v})')
def step_impl(context, name, v):
    _v = getattr(context, v)
    setattr(context, name, normalize(_v))

@when(u'{a3} = {a1} + {a2}')
def step_impl(context, a3, a1, a2):
    _a1 = getattr(context, a1)
    _a2 = getattr(context, a2)
    setattr(context, a3, _a1 + _a2)

@when(u'{p3} = {p1} - {p2}')
def step_impl(context, p3, p2, p1):
    _p1 = getattr(context, p1)
    _p2 = getattr(context, p2)
    setattr(context, p3, _p1 - _p2)

@then(u'{a}.{coordinate} = {val:g}')
def step_impl(context, a, coordinate, val):
    _a = getattr(context, a)
    assert getattr(_a, coordinate) == val

@then(u'a is a point')
def step_impl(context):
    assert isinstance(context.a, Point)

@then(u'a is not a point')
def step_impl(context):
    assert not isinstance(context.a, Point)
    
@then(u'a is a vector')
def step_impl(context):
    assert isinstance(context.a, Vector)

@then(u'a is not a vector')
def step_impl(context):
    assert not isinstance(context.a, Vector)

def _get_names_needed(*expressions):
    output = set()
    for expr in expressions:
        root = ast.parse(expr)
        names =  set(node.id for node in ast.walk(root) if isinstance(node, ast.Name))
        output.update(names)
    return output

@then(u'{lhs} == {rhs}')
def step_impl(context, lhs, rhs):
    import math
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
    assert _lhs == _rhs, f"{_lhs} != {_rhs}"
