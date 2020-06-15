Feature: Abstract Shapes

Scenario: The default transformation
  Given s = test_shape()
  #Then s.transform == Transformation(np.eye(4))

Scenario: Assigning a transformation
  Given s = test_shape()
  When set_transform(s, Translation(2, 3, 4))
  Then s.transform == Translation(2, 3, 4)

Scenario: The default material
  Given s = test_shape()
  When m = s.material
  Then m == Material()

Scenario: Assigning a material
  Given s = test_shape()
    And m = Material()
    And m.ambient = 1
  When s.material = m
  Then s.material == m

Scenario: Intersecting a scaled shape with a ray
  Given r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    And s = test_shape()
  When set_transform(s, Scaling(2, 2, 2))
    And xs = intersect(s, r)
  Then s.inner.saved_ray.origin == Point(0, 0, -2.5)
   And s.inner.saved_ray.direction == Vector(0, 0, 0.5)

Scenario: Intersecting a translated shape with a ray
  Given r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    And s = test_shape()
  When set_transform(s, translation(5, 0, 0))
    And xs = intersect(s, r)
  Then s.inner.saved_ray.origin == Point(-5, 0, -5)
    And s.inner.saved_ray.direction == Vector(0, 0, 1)

Scenario: Computing the normal on a translated shape
  Given s = test_shape()
  When set_transform(s, Translation(0, 1, 0))
    And n = normal_at(s, Point(0, 1.70711, -0.70711))
  Then n == Vector(0, 0.70711, -0.70711)

Scenario: Computing the normal on a transformed shape
  Given s = test_shape()
    And m = Scaling(1, 0.5, 1) * rotation_z(π/5)
  When set_transform(s, m)
    And n = normal_at(s, Point(0, √2/2, -√2/2))
  Then n == Vector(0, 0.97014, -0.24254)

# Scenario: A shape has a parent attribute
#   Given s â† test_shape()
#   Then s.parent is nothing

# Scenario: Converting a point from world to object space
#   Given g1 â† group()
#     And set_transform(g1, rotation_y(Ï€/2))
#     And g2 â† group()
#     And set_transform(g2, scaling(2, 2, 2))
#     And add_child(g1, g2)
#     And s â† sphere()
#     And set_transform(s, translation(5, 0, 0))
#     And add_child(g2, s)
#   When p â† world_to_object(s, point(-2, 0, -10))
#   Then p = point(0, 0, -1)

# Scenario: Converting a normal from object to world space
#   Given g1 â† group()
#     And set_transform(g1, rotation_y(Ï€/2))
#     And g2 â† group()
#     And set_transform(g2, scaling(1, 2, 3))
#     And add_child(g1, g2)
#     And s â† sphere()
#     And set_transform(s, translation(5, 0, 0))
#     And add_child(g2, s)
#   When n â† normal_to_world(s, vector(âˆš3/3, âˆš3/3, âˆš3/3))
#   Then n = vector(0.2857, 0.4286, -0.8571)

# Scenario: Finding the normal on a child object
#   Given g1 â† group()
#     And set_transform(g1, rotation_y(Ï€/2))
#     And g2 â† group()
#     And set_transform(g2, scaling(1, 2, 3))
#     And add_child(g1, g2)
#     And s â† sphere()
#     And set_transform(s, translation(5, 0, 0))
#     And add_child(g2, s)
#   When n â† normal_at(s, point(1.7321, 1.1547, -5.5774))
#   Then n = vector(0.2857, 0.4286, -0.8571)
