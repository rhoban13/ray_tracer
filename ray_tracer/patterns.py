import math


class Pattern:
    pass


class StripePattern(Pattern):
    def __init__(self, color1, color2):
        self.a = color1
        self.b = color2


def stripe_pattern(color1, color2):
    return StripePattern(color1, color2)


def stripe_at(pattern, point):
    if math.floor(point.x) % 2 == 0:
        return pattern.a
    return pattern.b



