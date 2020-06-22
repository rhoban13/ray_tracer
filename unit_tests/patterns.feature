Feature: Patterns

Background:
  Given black = Color(0, 0, 0)
    And white = Color(1, 1, 1)

Scenario: Creating a stripe pattern
  Given pattern = stripe_pattern(white, black)
  Then pattern.inner.a == white
    And pattern.inner.b == black

Scenario: A stripe pattern is constant in y
  Given pattern = stripe_pattern(white, black)
  Then pattern_at(pattern, Point(0, 0, 0)) == white
    And pattern_at(pattern, Point(0, 1, 0)) == white
    And pattern_at(pattern, Point(0, 2, 0)) == white

Scenario: A stripe pattern is constant in z
  Given pattern = stripe_pattern(white, black)
  Then pattern_at(pattern, Point(0, 0, 0)) == white
    And pattern_at(pattern, Point(0, 0, 1)) == white
    And pattern_at(pattern, Point(0, 0, 2)) == white

Scenario: A stripe pattern alternates in x
  Given pattern = stripe_pattern(white, black)
  Then pattern_at(pattern, Point(0, 0, 0)) == white
    And pattern_at(pattern, Point(0.9, 0, 0)) == white
    And pattern_at(pattern, Point(1, 0, 0)) == black
    And pattern_at(pattern, Point(-0.1, 0, 0)) == black
    And pattern_at(pattern, Point(-1, 0, 0)) == black
    And pattern_at(pattern, Point(-1.1, 0, 0)) == white

Scenario: Stripes with an object transformation
  Given object = Sphere()
    And set_transform(object, Scaling(2, 2, 2))
    And pattern = stripe_pattern(white, black)
  When c = pattern_at_shape(pattern, object, Point(1.5, 0, 0))
  Then c == white

Scenario: Stripes with a pattern transformation
  Given object = Sphere()
    And pattern = stripe_pattern(white, black)
    And set_pattern_transform(pattern, Scaling(2, 2, 2))
  When c = pattern_at_shape(pattern, object, Point(1.5, 0, 0))
  Then c == white

Scenario: Stripes with both an object and a pattern transformation
  Given object = Sphere()
    And set_transform(object, Scaling(2, 2, 2))
    And pattern = stripe_pattern(white, black)
    And set_pattern_transform(pattern, Translation(0.5, 0, 0))
  When c = pattern_at_shape(pattern, object, Point(2.5, 0, 0))
  Then c == white

Scenario: The default pattern transformation
  Given pattern = test_pattern()
  Then pattern.transform == Identity()

Scenario: Assigning a transformation
  Given pattern = test_pattern()
  When set_pattern_transform(pattern, Translation(1, 2, 3))
  Then pattern.transform == Translation(1, 2, 3)

Scenario: A pattern with an object transformation
  Given shape = Sphere()
    And set_transform(shape, Scaling(2, 2, 2))
    And pattern = test_pattern()
  When c = pattern_at_shape(pattern, shape, Point(2, 3, 4))
  Then c == Color(1, 1.5, 2)

Scenario: A pattern with a pattern transformation
  Given shape = Sphere()
    And pattern = test_pattern()
    And set_pattern_transform(pattern, Scaling(2, 2, 2))
  When c = pattern_at_shape(pattern, shape, Point(2, 3, 4))
  Then c == Color(1, 1.5, 2)

Scenario: A pattern with both an object and a pattern transformation
  Given shape = Sphere()
    And set_transform(shape, Scaling(2, 2, 2))
    And pattern = test_pattern()
    And set_pattern_transform(pattern, Translation(0.5, 1, 1.5))
  When c = pattern_at_shape(pattern, shape, Point(2.5, 3, 3.5))
  Then c == Color(0.75, 0.5, 0.25)

Scenario: A gradient linearly interpolates between colors
  Given pattern = gradient_pattern(white, black)
  Then pattern_at(pattern, Point(0, 0, 0)) == white
    And pattern_at(pattern, Point(0.25, 0, 0)) == Color(0.75, 0.75, 0.75)
    And pattern_at(pattern, Point(0.5, 0, 0)) == Color(0.5, 0.5, 0.5)
    And pattern_at(pattern, Point(0.75, 0, 0)) == Color(0.25, 0.25, 0.25)

Scenario: A ring should extend in both x and z
  Given pattern = ring_pattern(white, black)
  Then pattern_at(pattern, Point(0, 0, 0)) == white
    And pattern_at(pattern, Point(1, 0, 0)) == black
    And pattern_at(pattern, Point(0, 0, 1)) == black
    # 0.708 = just slightly more than âˆš2/2
    And pattern_at(pattern, Point(0.708, 0, 0.708)) == black

Scenario: Checkers should repeat in x
  Given pattern = checkers_pattern(white, black)
  Then pattern_at(pattern, Point(0, 0, 0)) == white
    And pattern_at(pattern, Point(0.99, 0, 0)) == white
    And pattern_at(pattern, Point(1.01, 0, 0)) == black

Scenario: Checkers should repeat in y
  Given pattern = checkers_pattern(white, black)
  Then pattern_at(pattern, Point(0, 0, 0)) == white
    And pattern_at(pattern, Point(0, 0.99, 0)) == white
    And pattern_at(pattern, Point(0, 1.01, 0)) == black

Scenario: Checkers should repeat in z
  Given pattern = checkers_pattern(white, black)
  Then pattern_at(pattern, Point(0, 0, 0)) == white
    And pattern_at(pattern, Point(0, 0, 0.99)) == white
    And pattern_at(pattern, Point(0, 0, 1.01)) == black
