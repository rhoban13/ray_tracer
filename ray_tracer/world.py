from ray_tracer.colors import BLACK
from ray_tracer.intersections import Intersections, hit, prepare_computations
from ray_tracer.material import lighting
from ray_tracer.rays import Ray


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
            intersections.extend(o.intersect(ray))
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
        intersections = self.intersect_world(ray)
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
