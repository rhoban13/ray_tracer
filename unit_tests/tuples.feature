Feature: Tuples, Vectors, and Points

Scenario: A Point has nonzero w coordinate
  Book: A tuple with w=1.0 is a point
  Given a = RP3Point(4.3, -4.2, 3.1, 1.0)
   Then a.x = 4.3
    And a.y = -4.2
    And a.z = 3.1
    And a.w = 1.0
    And a is a point
    And a is not a vector


Scenario: A Vector has a w coordinate == 0 
  Book: A tuple with w=0 is a vector
  Given a = RP3Point(4.3, -4.2, 3.1, 0.0)
  Then a.x = 4.3
    And a.y = -4.2
    And a.z = 3.1
    And a.w = 0.0
    And a is not a point
    And a is a vector

Scenario: Point() creates tuples with w=1
  Given p = Point(4, -4, 3)
    And q = RP3Point(4, -4, 3, 1)
   Then p == q

Scenario: Vector() creates tuples with w=0
  Given v = Vector(4, -4, 3)
    And w = RP3Point(4, -4, 3, 0)
   Then v == w

Scenario: Adding two RP3Points
  Book: Adding two tuples
  Given a1 = RP3Point(3, -2, 5, 1)
    And a2 = RP3Point(-2, 3, 1, 0)
    And expected = RP3Point(1, 1, 6, 1)
   When a3 = a1 + a2
   Then a3 == expected

Scenario: Subtracting two points
  Given p1 = Point(3, 2, 1)
    And p2 = Point(5, 6, 7)
    And expected = Vector(-2, -4, -6)
  When p3 = p1 - p2 
  Then p3 == expected