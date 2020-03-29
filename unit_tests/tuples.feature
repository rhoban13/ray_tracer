Feature: Tuples, Vectors, and Points

Scenario: A Point has nonzero w coordinate
  Book: A tuple with w=1.0 is a point
  Given a = R4Vector(4.3, -4.2, 3.1, 1.0)
   Then a.x == 4.3
    And a.y == -4.2
    And a.z == 3.1
    And a.w == 1.0
    And a is a point
    And a is not a vector

Scenario: A tuple with w=0 is a vector
  Given a = R4Vector(4.3, -4.2, 3.1, 0.0)
  Then a.x == 4.3
    And a.y == -4.2
    And a.z == 3.1
    And a.w == 0.0
    And a is not a point
    And a is a vector

Scenario: Point() creates tuples with w=1
  Given p = Point(4, -4, 3)
    And q = R4Vector(4, -4, 3, 1)
   Then p == q

Scenario: Vector() creates tuples with w=0
  Given v = Vector(4, -4, 3)
    And w = R4Vector(4, -4, 3, 0)
   Then v == w

Scenario: Adding two tuples
  Given a1 = R4Vector(3, -2, 5, 1)
    And a2 = R4Vector(-2, 3, 1, 0)
   Then a1 + a2 == R4Vector(1, 1, 6, 1)

Scenario: Subtracting two points
  Given p1 = Point(3, 2, 1)
    And p2 = Point(5, 6, 7)
  Then p1 - p2 == Vector(-2, -4, -6)

Scenario: Subtracting a vector from a point
  Given p = Point(3, 2, 1)
    And v = Vector(5, 6, 7)
   Then p - v == Point(-2, -4, -6)

Scenario: Subtracting two vectors
  Given v1 = Vector(3, 2, 1)
    And v2 = Vector(5, 6, 7)
  Then v1 - v2 == Vector(-2, -4, -6)

Scenario: Subtracting a vector from the zero vector
  Given zero = Vector(0, 0, 0)
    And v = Vector(1, -2, 3)
   Then zero - v == Vector(-1, 2, -3)

Scenario: Negating a tuple
  Given a = R4Vector(1, -2, 3, -4)
  Then -a == R4Vector(-1, 2, -3, 4)

Scenario: Multiplying a tuple by a scalar
  Given a = R4Vector(1, -2, 3, -4)
  Then a * 3.5 == R4Vector(3.5, -7, 10.5, -14)

Scenario: Multiplying a tuple by a fraction
  Given a = R4Vector(1, -2, 3, -4)
  Then a * 0.5 == R4Vector(0.5, -1, 1.5, -2)

Scenario: Dividing a tuple by a scalar
  Given a = R4Vector(1, -2, 3, -4)
  Then a / 2 == R4Vector(0.5, -1, 1.5, -2)

Scenario: Computing the magnitude of vector(1, 0, 0)
  Given v = Vector(1, 0, 0)
  Then magnitude(v) == 1

Scenario: Computing the magnitude of vector(1, 2, 3)
  Given v = Vector(1, 2, 3)
   Then magnitude(v) == sqrt(14)

Scenario: Normalizing vector(4, 0, 0) gives (1, 0, 0)
  Given v = vector(4, 0, 0)
  Then normalize(v) == Vector(1, 0, 0)

Scenario: Normalizing vector(1, 2, 3)
  Given v = Vector(1, 2, 3)
   Then normalize(v) == Vector(1/sqrt(14), 2/sqrt(14), 3/sqrt(14))

Scenario: The magnitude of a normalized vector
  Given v = Vector(1, 2, 3)
  When norm = normalize(v)
  Then magnitude(norm) == 1

Scenario: The dot product of two tuples
  Given a = Vector(1, 2, 3)
    And b = Vector(2, 3, 4)
  Then dot(a, b) == 20

Scenario: The cross product of two vectors
  Given a = Vector(1, 2, 3)
    And b = Vector(2, 3, 4)
  Then cross(a, b) == Vector(-1, 2, -1)
    And cross(b, a) == Vector(1, -2, 1)

Scenario: Colors are (red, green, blue) tuples
  Given c = Color(-0.5, 0.4, 1.7)
  Then c.red == -0.5
    And c.green == 0.4
    And c.blue == 1.7

Scenario: Adding colors
  Given c1 = Color(0.9, 0.6, 0.75)
    And c2 = Color(0.7, 0.1, 0.25)
   Then c1 + c2 == Color(1.6, 0.7, 1.0)

Scenario: Subtracting colors
  Given c1 = Color(0.9, 0.6, 0.75)
    And c2 = Color(0.7, 0.1, 0.25)
   Then c1 - c2 == Color(0.2, 0.5, 0.5)

Scenario: Multiplying a color by a scalar
  Given c = Color(0.2, 0.3, 0.4)
  Then c * 2 == Color(0.4, 0.6, 0.8)

Scenario: Multiplying colors
  Given c1 = Color(1, 0.2, 0.4)
    And c2 = Color(0.9, 1, 0.1)
   Then c1 * c2 == Color(0.9, 0.2, 0.04)



Scenario: Convert color to pixel
  Added by me, ensure to_pixel scales & truncates
  Given c = Color(1.5, 0.5, -2)
   Then c.to_pixel() == (255, 128 ,0)