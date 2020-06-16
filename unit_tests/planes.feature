Feature: Planes

Scenario: The normal of a plane is constant everywhere
  Given p = Plane()
  When n1 = normal_at(p, Point(0, 0, 0))
    And n2 = normal_at(p, Point(10, 0, -10))
    And n3 = normal_at(p, Point(-5, 0, 150))
  Then n1 == Vector(0, 1, 0)
    And n2 == Vector(0, 1, 0)
    And n3 == Vector(0, 1, 0)

Scenario: Intersect with a ray parallel to the plane
  Given p = Plane()
    And r = Ray(Point(0, 10, 0), Vector(0, 0, 1))
  When xs = intersect(p, r)
  Then xs is empty

Scenario: Intersect with a coplanar ray
  Given p = Plane()
    And r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
  When xs = intersect(p, r)
  Then xs is empty

Scenario: A ray intersecting a plane from above
  Given p = Plane()
    And r = Ray(Point(0, 1, 0), Vector(0, -1, 0))
  When xs = intersect(p, r)
  Then xs.count == 1
    And xs[0].t == 1
    And xs[0].object == p

Scenario: A ray intersecting a plane from below
  Given p = Plane()
    And r = Ray(Point(0, -1, 0), Vector(0, 1, 0))
  When xs = intersect(p, r)
  Then xs.count == 1
    And xs[0].t == 1
    And xs[0].object == p
