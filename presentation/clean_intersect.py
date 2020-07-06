from ray_tracer.shapes.crooked_plane import minkowski_norm


def intersect(ray):
    '''Find the intersections of ray with the standard crooked plane'''
    return intersect_stem(ray) + intersect_wing1(ray) + intersect_wing2(ray)

def intersect_stem(ray):
    intersections = []
    if ray.direction.x != 0:  # Not parallel to stem
        t = -ray.origin.x / ray.direction.x
        intersection_point = ray.origin + t * ray.direction

        if minkowski_norm(intersection_point) < 0:
            intersections.append(t)
    return intersections

def intersect_wing1(ray):
    intersections = []
    if ray.direction.y != - ray.direction.z:  # Not parallel to wing1
        t = - (ray.origin.y + ray.origin.z)/(ray.direction.y + ray.direction.z)
        intersection_point = ray.origin + t * ray.direction
        if intersection_point.x >= 0:
            intersections.append(t)
    return intersections

def intersect_wing2(ray):
    intersections = []
    if ray.direction.y != ray.direction.z:  # Not parallel to wing2
        t = - (ray.origin.y - ray.origin.z)/(ray.direction.y - ray.direction.z)
        intersection_point = ray.origin + t * ray.direction
        if intersection_point.x <= 0:
            intersections.append(t)
    return intersections

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
