import logging
import math
from pathlib import Path

from ray_tracer.canvas import canvas_to_png
from ray_tracer.camera import Camera
from ray_tracer.clipped_shape import ClippedShape
from ray_tracer.colors import Color, BLUE, WHITE
from ray_tracer.lights import point_light
from ray_tracer.material import Material
from ray_tracer.transformations import view_transform, rotation_z
from ray_tracer.tuples import Point, Vector
from ray_tracer.world import World

from examples.crooked_plane import crooked_plane

def draw_objects(objects):
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(filename)s:%(lineno)s %(name)s %(message)s')

    lights = [
        point_light(Point(10, 10, 15), WHITE),
        point_light(Point(-10, -10, 15), WHITE)
    ]
    world = World(objects=objects, light=lights)


    camera = Camera(100, 50, math.pi/3)
    camera.transform = view_transform(Point(12, -6, 10), Point(0, 0, 0), Vector(0, 0, 1))
    canvas = camera.render(world)

    path = Path(__file__).parent / "output.png"
    canvas_to_png(str(path), canvas)



def main():
    shape = ClippedShape(crooked_plane())
    #shape.transform = ReflectionXZ()
    shape.material = Material()
    shape.material.color = Color(1, .2, 1)
    objects = (shape,)
    draw_objects(objects)


if __name__ == "__main__":
    main()
