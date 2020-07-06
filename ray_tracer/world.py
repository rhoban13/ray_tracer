from ray_tracer.colors import BLACK
from ray_tracer.intersections import Intersections, hit, prepare_computations
from ray_tracer.lights import Light
from ray_tracer.material import lighting
from ray_tracer.rays import Ray


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

    def shade_hit(self, comps):
        if isinstance(self.light, Light):
            shadowed = is_shadowed(self, comps.over_point)
            return lighting(
                comps.object.material,
                comps.object,
                self.light,
                comps.point,
                comps.eyev,
                comps.normalv,
                shadowed,
            )
        assert isinstance(self.light, list), f"light is {self.light}"
        output = BLACK
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
