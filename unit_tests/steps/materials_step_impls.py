from behave import register_type, given, when
from parse_type import TypeBuilder

from ray_tracer.material import Material, lighting


@given(u'{m} = Material()')
def step_impl(context, m):
    _m = Material()
    setattr(context, m, _m)


    

parse_bool = TypeBuilder.make_enum({"True": True, "False": False})
register_type(BoolType=parse_bool)


@when(u'{result} = lighting({material}, {light}, {position}, {eyev}, {normalv}, {in_shadow:BoolType})')
def step_impl(context, result, material, light, position, eyev, normalv, in_shadow):
    _material = getattr(context, material)
    _light = getattr(context, light)
    _position = getattr(context, position)
    _eyev = getattr(context, eyev)
    _normalv = getattr(context, normalv)

    _result = lighting(_material, _light, _position, _eyev, _normalv, in_shadow)
    setattr(context, result, _result)


@when(u'{result} = lighting({material}, {light}, {position}, {eyev}, {normalv})')
def step_impl(context, result, material, light, position, eyev, normalv):
    context.execute_steps(f"when {result} = lighting({material}, {light}, {position}, {eyev}, {normalv}, False)")



