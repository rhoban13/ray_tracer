import itertools
import re

from ray_tracer.colors import Color
from ray_tracer.transformations import Scaling, Translation  # noqa: F401

from test_pattern import test_pattern


def set_props_from_table(context, shape):
    for row in itertools.chain([context.table.headings], context.table):
        k, v = row
        if k.startswith('material'):
            _, materialprop = k.split('.')
            if materialprop == "color":
                rgb = [float(p) for p in re.findall('\d+\.?\d*', v)]
                value = Color(*rgb)
            elif materialprop == "pattern":
                if v != "test_pattern()":
                    raise NotImplementedError("Only test_pattern is implemented")
                value = test_pattern()
            else:
                value = float(v)
            setattr(shape.material, materialprop, value)
        elif k == "transform":
            t = eval(v)
            shape.transform = t
        else:
            raise NotImplementedError(f"{k} is not implemented")
