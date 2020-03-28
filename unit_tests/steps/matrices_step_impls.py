import numpy as np

def table_to_matrix(table):
    matrix = np.array([tuple(float(x) for x in table.headings)])
    for row in table:
        matrix = np.append(matrix, [tuple(float(cell) for cell in row)], axis=0)
    return matrix

@given(u'the following matrix {name}')
def step_impl(context, name): 
    setattr(context, name, table_to_matrix(context.table))

@given(u'the following {n:d}x{m:d} matrix {name}')
def step_impl(context, n, m, name):
    matrix = table_to_matrix(context.table)
    assert matrix.shape == (n, m), f"{matrix.shape} != {(n,m)}"
    setattr(context, name, matrix)

@then(u'{A} * {B} is the following 4x4 matrix')
def step_impl(context, A, B):
    _A = getattr(context, A)
    _B = getattr(context, B)
    expected = table_to_matrix(context.table)
    assert np.array_equal(_A.dot(_B), expected)