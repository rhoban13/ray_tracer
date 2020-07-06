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
