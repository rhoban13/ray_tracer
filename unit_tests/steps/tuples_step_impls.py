from ray_tracer import make_rp3_point, Point, Vector

@given(u'{name} = make_rp3_point({x:g}, {y:g}, {z:g}, {w:g})')
def step_impl(context, name, x, y, z, w):
    setattr(context, name,  make_rp3_point(x, y, z, w))

@given(u'{name} = Point({x:g}, {y:g}, {z:g})')
def step_impl(context, name, x, y, z):
    setattr(context, name, Point(x, y, z))

@given(u'{name} = Vector({x:g}, {y:g}, {z:g})')
def step_impl(context, name, x, y, z):
    setattr(context, name, Vector(x, y, z))

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
