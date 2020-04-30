import math

import numpy as np

from . import Point, dot, Intersection, Intersections
from ray_tracer.transformations import Transformation, inverse
from ray_tracer._rays import transform


class Sphere:
    def __init__(self, center=Point(0, 0, 0), radius=1):
        self.transform = Transformation(np.eye(4))

def intersect(sphere, ray):
    '''
    This is solution to ||(ray.origin + t * ray.direction) - sphere.center|| == sphere.radius
    Strong assumption now that sphere = Sphere()
    '''
    center = Point(0,0,0)
    radius = 1

    ray2 = transform(ray, inverse(sphere.transform))
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

def set_transform(sphere, transform):
    sphere.transform = transform