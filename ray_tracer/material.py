from dataclasses import dataclass

from ray_tracer.colors import Color, BLACK
from ray_tracer.patterns import Pattern, stripe_at
from ray_tracer.tuples import normalize, dot, reflect


@dataclass
class Material:
    color: Color = Color(1, 1, 1)
    ambient: float = .1
    diffuse: float = .9
    pattern: Pattern = None
    specular: float = .9
    shininess: float = 200.0


def lighting(material, light, point, eyev, normalv, in_shadow=False):

    if material.pattern is not None:
        color = stripe_at(material.pattern, point)
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
