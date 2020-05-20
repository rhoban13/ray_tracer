from ray_tracer.colors import Color, BLACK
from ray_tracer.intersections import Intersections, intersect, hit, prepare_computations
from ray_tracer.lights import point_light
from ray_tracer.material import lighting
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
    intersections = Intersections()
    for o in world.objects:
        intersections.extend(intersect(o, ray))

    return intersections


def shade_hit(world, comps):
    return lighting(
        comps.object.material,
        world.light,
        comps.point,
        comps.eyev,
        comps.normalv)


def color_at(world, ray):
    intersections = intersect_world(world, ray)
    a_hit = hit(intersections)
    if a_hit is None:
        print("No hit")
        return BLACK
    comps = prepare_computations(a_hit, ray)
    return shade_hit(world, comps)
