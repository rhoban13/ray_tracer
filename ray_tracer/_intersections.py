
class Intersection:
    def __init__(self, t, object_):
        self.t = t
        self.object = object_

class Intersections:
    def __init__(self, *args):
        self.intersections = tuple(args)
    
    def __getitem__(self, index):
        return self.intersections[index]

    @property
    def count(self):
        return len(self.intersections)


def hit(intersections):
    s = sorted(intersections, key=lambda intersection: intersection.t)
    for intersection in s:
        if intersection.t >=0:
            return intersection

