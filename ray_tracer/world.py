from ray_tracer.colors import Color, BLACK
from ray_tracer.intersections import Intersections, intersect, hit, prepare_computations
from ray_tracer.lights import point_light
from ray_tracer.material import lighting
from ray_tracer.rays import Ray
from ray_tracer.sphere import Sphere
from ray_tracer.transformations import Scaling
from ray_tracer.tuples import Point


class World():
    __slots__ = ('objects', 'light')

    def __init__(self, objects=None, light=None):
        self.objects = objects
        self.light = light

    def __str__(self):
        return f"World <objects={self.objects}, light={self.light}"

    def intersect_world(self, ray):
        intersections = Intersections()
        for o in self.objects:
            intersections.extend(intersect(o, ray))
        return intersections

    def shade_hit(self, comps):
        shadowed = is_shadowed(self, comps.over_point)
        return lighting(
            comps.object.material,
            self.light,
            comps.point,
            comps.eyev,
            comps.normalv,
            shadowed)

    def color_at(self, ray):
        intersections = intersect_world(self, ray)
        a_hit = hit(intersections)
        if a_hit is None:
            return BLACK
        comps = prepare_computations(a_hit, ray)
        return shade_hit(self, comps)

    def add_object(self, object_):
        if self.objects is None:
            self.objects = [object_]
        else:
            self.objects.append(object_)


def default_world():
    light = point_light(Point(-10, 10, -10), Color(1, 1, 1))
    s1 = Sphere()
    s1.material.color = Color(.8, 1.0, .6)
    s1.material.diffuse = .7
    s1.material.specular = .2

    s2 = Sphere()
    s2.transform = Scaling(.5, .5, .5)

    return World(objects=(s1, s2), light=light)


def intersect_world(world, ray):
    return world.intersect_world(ray)


def shade_hit(world, comps):
    return world.shade_hit(comps)


def color_at(world, ray):
    return world.color_at(ray)


def is_shadowed(world, point):
    v = world.light.position - point
    distance = v.magnitude()
    direction = v.normalize()

    r = Ray(point, direction)
    intersections = intersect_world(world, r)

    h = hit(intersections)
    if h is not None and h.t < distance:
        return True
    else:
        return False
