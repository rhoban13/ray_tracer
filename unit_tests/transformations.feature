Feature: Matrix Transformations

Scenario: Multiplying by a translation matrix
  Given transform = Translation(5, -3, 2)
    And p = Point(-3, 4, 5)
   Then transform * p == Point(2, 1, 7)

Scenario: Multiplying by the inverse of a translation matrix
  Given transform = Translation(5, -3, 2)
    And inv = inverse(transform)
    And p = Point(-3, 4, 5)
   Then inv * p == Point(-8, 7, 3)

Scenario: Translation does not affect vectors
  Given transform = Translation(5, -3, 2)
    And v = Vector(-3, 4, 5)
   Then transform * v == v

Scenario: A scaling matrix applied to a point
  Given transform = Scaling(2, 3, 4)
    And p = Point(-4, 6, 8)
   Then transform * p == Point(-8, 18, 32)

Scenario: A scaling matrix applied to a vector
  Given transform = Scaling(2, 3, 4)
    And v = Vector(-4, 6, 8)
   Then transform * v == Vector(-8, 18, 32)

Scenario: Multiplying by the inverse of a scaling matrix
  Given transform = Scaling(2, 3, 4)
    And inv = inverse(transform)
    And v = Vector(-4, 6, 8)
   Then inv * v == Vector(-2, 2, 2)

Scenario: Reflection is scaling by a negative value
  Given transform = Scaling(-1, 1, 1)
    And p = Point(2, 3, 4)
   Then transform * p == Point(-2, 3, 4)

Scenario: Rotating a point around the x axis
  Given p = Point(0, 1, 0)
    And half_quarter = rotation_x(π / 4)
    And full_quarter = rotation_x(π / 2)
  Then half_quarter * p == Point(0, math.sqrt(2)/2, math.sqrt(2)/2)
    And full_quarter * p == Point(0, 0, 1)

Scenario: The inverse of an x-rotation rotates in the opposite direction
  Given p = Point(0, 1, 0)
    And half_quarter = rotation_x(π / 4)
    And inv = inverse(half_quarter)
  Then inv * p == Point(0, math.sqrt(2)/2, -math.sqrt(2)/2)

Scenario: Rotating a point around the y axis
  Given p = Point(0, 0, 1)
    And half_quarter = rotation_y(π / 4)
    And full_quarter = rotation_y(π / 2)
  Then half_quarter * p == Point(math.sqrt(2)/2, 0, math.sqrt(2)/2)
    And full_quarter * p == Point(1, 0, 0)

Scenario: Rotating a point around the z axis
  Given p = Point(0, 1, 0)
    And half_quarter = rotation_z(π / 4)
    And full_quarter = rotation_z(π / 2)
  Then half_quarter * p == Point(-math.sqrt(2)/2, math.sqrt(2)/2, 0)
    And full_quarter * p == Point(-1, 0, 0)

Scenario: A shearing transformation moves x in proportion to y
  Given transform = Shearing(1, 0, 0, 0, 0, 0)
    And p = Point(2, 3, 4)
  Then transform * p == Point(5, 3, 4)

Scenario: A shearing transformation moves x in proportion to z
  Given transform = Shearing(0, 1, 0, 0, 0, 0)
    And p = Point(2, 3, 4)
  Then transform * p == Point(6, 3, 4)

Scenario: A shearing transformation moves y in proportion to x
  Given transform = Shearing(0, 0, 1, 0, 0, 0)
    And p = Point(2, 3, 4)
  Then transform * p == Point(2, 5, 4)

Scenario: A shearing transformation moves y in proportion to z
  Given transform = Shearing(0, 0, 0, 1, 0, 0)
    And p = Point(2, 3, 4)
  Then transform * p == Point(2, 7, 4)

Scenario: A shearing transformation moves z in proportion to x
  Given transform = Shearing(0, 0, 0, 0, 1, 0)
    And p = Point(2, 3, 4)
  Then transform * p == Point(2, 3, 6)

Scenario: A shearing transformation moves z in proportion to y
  Given transform = Shearing(0, 0, 0, 0, 0, 1)
    And p = Point(2, 3, 4)
  Then transform * p == Point(2, 3, 7)

Scenario: Individual transformations are applied in sequence
  Given p = Point(1, 0, 1)
    And A = rotation_x(π / 2)
    And B = Scaling(5, 5, 5)
    And C = Translation(10, 5, 7)
  # apply rotation first
  When p2 = A * p
  Then p2 == Point(1, -1, 0)
  # then apply scaling
  When p3 = B * p2
  Then p3 == Point(5, -5, 0)
  # then apply translation
  When p4 = C * p3
  Then p4 == Point(15, 0, 7)

Scenario: Chained transformations must be applied in reverse order
  Given p = Point(1, 0, 1)
    And A = rotation_x(π / 2)
    And B = Scaling(5, 5, 5)
    And C = Translation(10, 5, 7)
  When T = C * B * A
  Then T * p == Point(15, 0, 7)