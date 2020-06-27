Feature: Clipping Shapes


Scenario: Clipping intersect == inner.intersect inside the clipping box
  Given s = test_shape()
    And r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
   When xs = intersect(s, r)
   Then xs.count == 1 
    And xs[0].object == s
