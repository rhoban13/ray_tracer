from dataclasses import dataclass

from ray_tracer.colors import Color, BLACK
from ray_tracer.patterns import Pattern, pattern_at_shape
from ray_tracer.tuples import normalize, dot, reflect


@dataclass
class Material:
    color: Color = Color(1, 1, 1)
    ambient: float = .1
    diffuse: float = .9
    pattern: Pattern = None
    specular: float = .9
    shininess: float = 200.0
    reflective: float = 0.0
    transparency: float = 0.0
    refractive_index: float = 1


def lighting(material, object_, light, point, eyev, normalv, in_shadow=False):

    if material.pattern is not None:
        color = pattern_at_shape(material.pattern, object_, point)
    else:
        color = material.color

    # combine the surface color with the light's color/intensity
    effective_color = color * light.intensity

    # find the direction to the light source
    lightv = normalize(light.position - point)

    # compute the ambient contribution
    ambient = effective_color * material.ambient

    # light_dot_normal representst the cosine of the angle between the
    # light vector and the normal vector.  A negative number means teh
    # light is on the other side of the surface
    light_dot_normal = dot(lightv, normalv)
    if light_dot_normal < 0:
        diffuse = BLACK
        specular = BLACK
    else:
        # compute the diffuse contribution
        diffuse = effective_color * material.diffuse * light_dot_normal

        # reflect_dot_eye represents the cosine of the angle between the
        # refletion vector and the eye vector.  A negative number means the
        # light relfects away from the eye
        reflectv = reflect(-lightv, normalv)
        reflect_dot_eye = dot(reflectv, eyev)

        if reflect_dot_eye <= 0:
            specular = BLACK
        else:
            # compute the specular contribution
            factor = pow(reflect_dot_eye, material.shininess)
            specular = light.intensity * material.specular * factor

    if in_shadow:
        return ambient

    # Add the three contributions together to get the final shading
    return ambient + diffuse + specular

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
