from .clipped_shape import ClippedShape
from .crooked_plane import CrookedPlane
from .plane import Plane
from .shape import Shape, set_transform
from .sphere import Sphere
from .transformed_shape import TransformedShape

_shapes = [
    ClippedShape,
    CrookedPlane,
    Plane,
    Shape,
    Sphere,
    TransformedShape
]

__all__ = _shapes + [set_transform]
