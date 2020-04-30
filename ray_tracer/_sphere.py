import math

from . import Point, dot, Intersection, Intersections

class Sphere:
    def __init__(self, center=Point(0, 0, 0), radius=1):
        self.center = center
        self.radius = radius

def intersect(sphere, ray):
    '''
    This is solution to ||(ray.origin + t * ray.direction) - sphere.center|| == sphere.radius
    Strong assumption now that sphere = Sphere()
    '''
    sphere_to_ray = ray.origin - sphere.center
    a = dot(ray.direction, ray.direction)
    b = 2 * dot(ray.direction, sphere_to_ray)
    c = dot(sphere_to_ray, sphere_to_ray) - 1
    discriminant = b**2 - 4 * a * c
    
    if discriminant < 0:
        return Intersections()
    
    t1 = (-b - math.sqrt(discriminant)) / (2 * a)
    t2 = (-b + math.sqrt(discriminant)) / (2 * a)
    return Intersections(Intersection(t1, sphere), Intersection(t2, sphere))
