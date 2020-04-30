Feature: Rays

Scenario: Creating and querying a ray
  Given origin = Point(1, 2, 3)
    And direction = Vector(4, 5, 6)
  When r = Ray(origin, direction)
  Then r.origin == origin
    And r.direction == direction

Scenario: Computing a point from a distance
  Given r = Ray(Point(2, 3, 4), Vector(1, 0, 0))
  Then position(r, 0) == Point(2, 3, 4)
    And position(r, 1) == Point(3, 3, 4)
    And position(r, -1) == Point(1, 3, 4)
    And position(r, 2.5) == Point(4.5, 3, 4)

Scenario: Translating a ray
  Given r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
    And m = Translation(3, 4, 5)
  When r2 = transform(r, m)
  Then r2.origin == Point(4, 6, 8)
    And r2.direction == Vector(0, 1, 0)

Scenario: Scaling a ray
  Given r = Ray(Point(1, 2, 3), Vector(0, 1, 0))
    And m = scaling(2, 3, 4)
  When r2 = transform(r, m)
  Then r2.origin == Point(2, 6, 12)
    And r2.direction == Vector(0, 3, 0)