import heapq


from ray_tracer.rays import position
from ray_tracer.tuples import dot


class Intersection:
    def __init__(self, t, object_):
        self.t = t
        self.object = object_

    def __lt__(self, other):
        return self.t < other.t


class Intersections:
    def __init__(self, *args):
        self._list_of_t = list(args)
        heapq.heapify(self._list_of_t)

    def __getitem__(self, index):
        return self._list_of_t[index]

    #def __bool__(self):
    #    return bool(self._list_of_t)

    @property
    def count(self):
        return len(self._list_of_t)

    def extend(self, intersections):
        self._list_of_t = list(heapq.merge(self._list_of_t, intersections._list_of_t))


def hit(intersections):
    s = sorted(intersections, key=lambda intersection: intersection.t)
    for intersection in s:
        if intersection.t >= 0:
            return intersection


def intersect(shape, ray):
    return shape.intersect(ray)


EPSILON = 1e-5


class Computations:
    def __init__(self, intersection, ray):
        self.intersection = intersection
        self.ray = ray

        self.point = position(ray, self.t)
        self.eyev = -ray.direction
        self.normalv = self.object.normal_at(self.point)

        if dot(self.normalv, self.eyev) < 0:
            self.inside = True
            self.normalv = - self.normalv
        else:
            self.inside = False

        self.over_point = self.point + self.normalv * EPSILON

    @property
    def t(self):
        return self.intersection.t

    @property
    def object(self):
        return self.intersection.object

    def __str__(self):
        return f'''Computations:
    intersection = {self.intersection}
    ray = {self.ray}
    point = {self.point}
    eyev = {self.eyev}
    normalv = {self.normalv}
    inside = {self.inside}
'''


def prepare_computations(intersection, ray):
    return Computations(intersection, ray)
