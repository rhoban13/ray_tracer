import numpy as np

from behave import register_type
from parse_type import TypeBuilder

from ray_tracer.transformations import Transformation


def table_to_matrix(table):
    foo = [tuple(float(x) for x in table.headings)]
    matrix = np.array(foo)
    for row in table:
        matrix = np.append(matrix, [tuple(float(cell) for cell in row)], axis=0)
    return Transformation(matrix)

@given(u'the following matrix {name}')
def step_impl(context, name): 
    setattr(context, name, table_to_matrix(context.table))

@given(u'the following {n:d}x{m:d} matrix {name}')
def step_impl(context, n, m, name):
    matrix = table_to_matrix(context.table)
    assert matrix.shape == (n, m), f"{matrix.shape} != {(n,m)}"
    setattr(context, name, matrix)

@then(u'{expr} is the following {n:d}x{m:d} matrix')
def step_impl(context, expr, n, m):
    expected = table_to_matrix(context.table)
    setattr(context, "expected", expected)

    
    print(expected)
    print("====")
    print(expr)

    context.execute_steps(f"then {expr} == expected")
    assert expected.shape == (n, m)

@then(u'{expr} is the following matrix')
def step_impl(context, expr):
    expected = table_to_matrix(context.table)
    setattr(context, "expected", expected)
    context.execute_steps(f"then {expr} == expected")

parse_is_or_is_not = TypeBuilder.make_enum({"is": True, "is not": False})
register_type(IsOrIsNot=parse_is_or_is_not)

@then(u'{name} {x:IsOrIsNot} invertible')
def step_impl(context, name, x):
    _name = getattr(context, name)
    if x:
        assert _name.det() != 0
    else:
        assert _name.det() == 0


@given(u'C = A * B')
def step_impl(context):
    _A = getattr(context, "A")
    _B = getattr(context, "B")
    _C = _A * _B
    setattr(context, "C", _C)
