from dataclasses import dataclass

from ray_tracer import Point, normalize, Vector, Color
from ray_tracer.canvas import Canvas, canvas_to_ppm

@dataclass
class Projectile:
    position: Point
    velocity: Vector

    def __str__(self):
        return f"Projectile(position={self.position}, velocity={self.velocity})"

@dataclass
class Environment:
    gravity: Vector
    wind: Vector

def tick(env, proj):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return Projectile(position, velocity)

start = Point(0,1,0)
velocity = normalize(Vector(1,1.8,1))* 11.25
p = Projectile(start, velocity)

gravity = Vector(0, -0.1, 0)
wind =  Vector(-0.01, 0, 0)
e = Environment(gravity, wind)

c = Canvas(900, 550)

while p.position.y > 0:
    p = tick(e, p)
    x, y  = int(p.position.x), int(p.position.y)
    print(f"writing {x}, {y}")
    c.write_pixel(x, y, Color(100,0,0))

print(c._image)
print(f"p has landed at {p}")
canvas_to_ppm(c)

    
