from ray_tracer import RP3Point, Point, Vector

@given(u'{name} = RP3Point({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, name, x, y, z, w):
    setattr(context, name,  RP3Point(x, y, z, w))

@given(u'{name} = Point({x:g}, {y:g}, {z:g})')
def step_impl(context, name, x, y, z):
    setattr(context, name, Point(x, y, z))

@given(u'{name} = Vector({x:g}, {y:g}, {z:g})')
def step_impl(context, name, x, y, z):
    setattr(context, name, Vector(x, y, z))

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

@then(u'a.{coordinate} = {val:g}')
def step_impl(context, coordinate, val):
    assert getattr(context.a, coordinate) == val

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

@then(u'{lhs} == {rhs}')
def step_impl(context, lhs, rhs):
    _lhs = getattr(context, lhs)
    _rhs = getattr(context, rhs)
    assert _lhs == _rhs