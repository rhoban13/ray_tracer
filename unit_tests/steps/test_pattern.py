from ray_tracer.colors import Color
from ray_tracer.patterns import Pattern, TransformedPattern
from ray_tracer.transformations import Identity

class TestPattern(Pattern):
    def pattern_at(self, point):
        return Color(point.x, point.y, point.z)


def test_pattern():
    return TransformedPattern(TestPattern(), Identity())
