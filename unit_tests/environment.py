import math

from behave import register_type
from parse import with_pattern
from parse_type import TypeBuilder

from ray_tracer.tuples import is_point, is_vector


parse_interesting_trig_values = TypeBuilder.make_enum({
    "0": 0,
    "√2/2": math.sqrt(2)/2,
    "1": 1,
    "√2": math.sqrt(2),
    "-√2/2": -math.sqrt(2)/2,
    "-1": -1,
    "-3": -3  # This is stoopid - try to define my own parser below
})
register_type(InterestingTrigValue=parse_interesting_trig_values)


# @with_pattern(r'\g+')
# def _parse_float(text):
#     return float(text)


# parse_reals = TypeBuilder.make_variant([parse_interesting_trig_values, _parse_float])
# register_type(InterestingRealNumbers=parse_reals)



parse_point_or_vector = TypeBuilder.make_enum({
    "point": is_point,
    "vector": is_vector,
})
register_type(ElementIn3D=parse_point_or_vector)
