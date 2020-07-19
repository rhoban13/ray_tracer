import math

from ray_tracer.colors import BLACK
from ray_tracer.intersections import Intersections, hit, prepare_computations
from ray_tracer.lights import Light
from ray_tracer.material import lighting
from ray_tracer.rays import Ray
from ray_tracer.tuples import dot


class UnexectedLightType(RuntimeError):
    pass


class World:
    __slots__ = ("objects", "light")

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

    def shade_hit(self, comps, remaining=5):
        reflected = self.reflected_color(comps, remaining)
        refracted = self.refracted_color(comps, remaining)

        if isinstance(self.light, Light):
            shadowed = is_shadowed(self, comps.over_point)
            surface = lighting(
                comps.object.material,
                comps.object,
                self.light,
                comps.point,
                comps.eyev,
                comps.normalv,
                shadowed,
            )
            return surface + reflected + refracted

        assert isinstance(self.light, list), f"light is {self.light}"
        output = BLACK + reflected + refracted
        for light in self.light:
            shadowed = is_shadowed(self, comps.over_point, light)
            output += lighting(
                    comps.object.material,
                    comps.object,
                    light,
                    comps.point,
                    comps.eyev,
                    comps.normalv,
                    shadowed,
            )
        return output

    def color_at(self, ray, remaining=5):
        intersections = self.intersect_world(ray)
        a_hit = hit(intersections)
        if a_hit is None:
            return BLACK
        comps = prepare_computations(a_hit, ray)
        return self.shade_hit(comps, remaining)

    def add_object(self, object_):
        if self.objects is None:
            self.objects = [object_]
        else:
            self.objects.append(object_)

    def reflected_color(self, comps, remaining=5):
        if remaining <= 0:
            return BLACK
        if comps.object.material.reflective == 0:
            return BLACK
        reflect_ray = Ray(comps.over_point, comps.reflectv)
        color = self.color_at(reflect_ray, remaining-1)
        return color * comps.object.material.reflective

    def refracted_color(self, comps, remaining):
        if comps.object.material.transparency == 0:
            return BLACK

        if remaining == 0:
            return BLACK

        n_ratio = comps.n1 / comps.n2
        cos_i = dot(comps.eyev, comps.normalv)
        sin2_t = n_ratio ** 2 * (1-cos_i ** 2)
        if sin2_t > 1:
            return BLACK

        cos_t = math.sqrt(1-sin2_t)
        direction = comps.normalv * (n_ratio * cos_i - cos_t) - comps.eyev * n_ratio
        refract_ray = Ray(comps.under_point, direction)
        color = self.color_at(refract_ray, remaining - 1) * comps.object.material.transparency
        return color


def intersect_world(world, ray):
    return world.intersect_world(ray)


def shade_hit(world, comps, remaining=5):
    return world.shade_hit(comps, remaining)


def color_at(world, ray):
    return world.color_at(ray)


def is_shadowed(world, point, light=None):
    if light is None:  # This is pretty inefficient.  It recomputes intersections below for each light
        light = world.light
    v = light.position - point
    distance = v.magnitude()
    direction = v.normalize()

    r = Ray(point, direction)
    intersections = intersect_world(world, r)

    h = hit(intersections)
    if h is not None and h.t < distance:
        return True
    else:
        return False


def reflected_color(world: World, comps, remaining=5):
    return world.reflected_color(comps, remaining)


def refracted_color(world: World, comps, remaining):
    return world.refracted_color(comps, remaining)

# Copyright 2020 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
