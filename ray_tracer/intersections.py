import heapq
import math

from ray_tracer.rays import position
from ray_tracer.sphere import normal_at
from ray_tracer.rays import transform
from ray_tracer.tuples import Point, dot


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

    @property
    def count(self):
        return len(self._list_of_t)

    def extend(self, intersections):
        self._list_of_t = list(heapq.merge(self._list_of_t, intersections._list_of_t))


def hit(intersections):
    s = sorted(intersections, key=lambda intersection: intersection.t)
    for intersection in s:
        if intersection.t >=0:
            return intersection


def intersect(sphere, ray):
    '''
    This is solution to ||(ray.origin + t * ray.direction) - sphere.center|| == sphere.radius
    Strong assumption now that sphere = Sphere()
    '''
    center = Point(0,0,0)
    radius = 1

    ray2 = transform(ray, sphere.transform.inverse())
    sphere_to_ray = ray2.origin - center
    a = dot(ray2.direction, ray2.direction)
    b = 2 * dot(ray2.direction, sphere_to_ray)
    c = dot(sphere_to_ray, sphere_to_ray) - radius
    discriminant = b**2 - 4 * a * c
    
    if discriminant < 0:
        return Intersections()
    
    t1 = (-b - math.sqrt(discriminant)) / (2 * a)
    t2 = (-b + math.sqrt(discriminant)) / (2 * a)
    return Intersections(Intersection(t1, sphere), Intersection(t2, sphere))


class Computations:
    def __init__(self, intersection, ray):
        self.intersection = intersection
        self.ray = ray

        self.point = position(ray, self.t)
        self.eyev = -ray.direction
        self.normalv = normal_at(self.object, self.point)
        
        if dot(self.normalv, self.eyev) < 0:
            self.inside = True
            self.normalv = - self.normalv
        else:
            self.inside = False

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
