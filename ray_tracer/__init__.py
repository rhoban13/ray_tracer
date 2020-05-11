from ._rp3_points import R4Vector, Point, Vector, magnitude, normalize, dot, cross, reflect

from ._colors import Color, RED, GREEN, BLUE, BLACK, WHITE

from ._rays import Ray, position

from ._intersections import Intersection, Intersections, hit

from ._sphere import Sphere, intersect, set_transform, normal_at

from ._lights import point_light

from ._material import Material, lighting