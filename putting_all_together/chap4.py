import math
from pathlib import Path

from ray_tracer.colors import RED, GREEN
from ray_tracer.tuples import Point, Vector
from ray_tracer.transformations import rotation_z
from ray_tracer.canvas import Canvas, canvas_to_png


def main():
    c = Canvas(200, 200)
    adjustment = Vector(c.width/2, c.height/2 ,0)
    radius = 3 * c.width / 8
    center = Point(0, 0, 0) + adjustment
    c.write_pixel(int(center.x), int(center.y), RED)

    twelve = Point(0, radius, 0)
    points = [twelve]
    for k in range(12):
        R = rotation_z(k * math.pi / 6)
        points.append(R * twelve)
    points = [p + adjustment for p in points]

    for p in points:
        c.write_pixel(int(p.x), int(p.y), GREEN)

    path = Path(__file__).parent / "chap4.png"
    canvas_to_png(str(path), c)


if __name__ == "__main__":
    main()

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
