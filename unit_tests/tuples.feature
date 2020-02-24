Feature: Tuples, Vectors, and Points

Scenario: A Point has nonzero w coordinate
  Book: A tuple with w=1.0 is a point
  Given a = make_rp3_point(4.3, -4.2, 3.1, 1.0)
   Then a.x = 4.3
    And a.y = -4.2
    And a.z = 3.1
    And a.w = 1.0
    And a is a point
    And a is not a vector


Scenario: A Vector has a w coordinate == 0 
  Book: A tuple with w=0 is a vector
  Given a = make_rp3_point(4.3, -4.2, 3.1, 0.0)
  Then a.x = 4.3
    And a.y = -4.2
    And a.z = 3.1
    And a.w = 0.0
    And a is not a point
    And a is a vector

Scenario: Point() creates tuples with w=1
  Given p = Point(4, -4, 3)
    And q = make_rp3_point(4, -4, 3, 1)
   Then p == q

Scenario: Vector() creates tuples with w=0
  Given v = Vector(4, -4, 3)
    And w = make_rp3_point(4, -4, 3, 0)
   Then v == w