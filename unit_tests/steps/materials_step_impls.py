from ray_tracer import Material, lighting

@given(u'{m} = Material()')
def step_impl(context, m):
    _m = Material()
    setattr(context, m, _m)


@when(u'{result} = lighting({material}, {light}, {position}, {eyev}, {normalv})')
def step_impl(context, result, material, light, position, eyev, normalv):
    _material = getattr(context, material)
    _light = getattr(context, light)
    _position = getattr(context, position)
    _eyev = getattr(context, eyev)
    _normalv = getattr(context, normalv)

    _result = lighting(_material, _light, _position, _eyev, _normalv)
    setattr(context, result, _result)