Feature: Materials

Background:
  Given m = Material()
    And position = Point(0, 0, 0)

Scenario: The default material
  Given m = Material()
  Then m.color == Color(1, 1, 1)
    And m.ambient == 0.1
    And m.diffuse == 0.9
    And m.specular == 0.9
    And m.shininess == 200.0

# Scenario: Reflectivity for the default material
#   Given m â† material()
#   Then m.reflective = 0.0

# Scenario: Transparency and Refractive Index for the default material
#   Given m â† material()
#   Then m.transparency = 0.0
#     And m.refractive_index = 1.0

Scenario: Lighting with the eye between the light and the surface
  Given eyev = Vector(0, 0, -1)
    And normalv = Vector(0, 0, -1)
    And light = point_light(Point(0, 0, -10), Color(1, 1, 1))
  When result = lighting(m, light, position, eyev, normalv)
  Then result == Color(1.9, 1.9, 1.9)

Scenario: Lighting with the eye between light and surface, eye offset 45°
  Given eyev = Vector(0, √2/2, -√2/2)
    And normalv = Vector(0, 0, -1)
    And light = point_light(Point(0, 0, -10), Color(1, 1, 1))
  When result = lighting(m, light, position, eyev, normalv)
  Then result == Color(1.0, 1.0, 1.0)

Scenario: Lighting with eye opposite surface, light offset 45°
  Given eyev = Vector(0, 0, -1)
    And normalv = Vector(0, 0, -1)
    And light = point_light(Point(0, 10, -10), Color(1, 1, 1))
  When result = lighting(m, light, position, eyev, normalv)
  Then result == Color(0.7364, 0.7364, 0.7364)

Scenario: Lighting with eye in the path of the reflection vector
  Given eyev = Vector(0, -√2/2, -√2/2)
    And normalv = Vector(0, 0, -1)
    And light = point_light(Point(0, 10, -10), Color(1, 1, 1))
  When result = lighting(m, light, position, eyev, normalv)
  Then result == Color(1.6364, 1.6364, 1.6364)

Scenario: Lighting with the light behind the surface
  Given eyev = Vector(0, 0, -1)
    And normalv = Vector(0, 0, -1)
    And light = point_light(Point(0, 0, 10), Color(1, 1, 1))
  When result = lighting(m, light, position, eyev, normalv)
  Then result == Color(0.1, 0.1, 0.1)

Scenario: Lighting with the surface in shadow
  Given eyev = Vector(0, 0, -1)
    And normalv = Vector(0, 0, -1)
    And light = point_light(Point(0, 0, -10), Color(1, 1, 1))
    #And in_shadow = true
  When result = lighting(m, light, position, eyev, normalv, True)
  Then result == Color(0.1, 0.1, 0.1)

Scenario: Lighting with a pattern applied
  Given m.pattern = stripe_pattern(Color(1, 1, 1), Color(0, 0, 0))
    And m.ambient = 1
    And m.diffuse = 0
    And m.specular = 0
    And eyev = Vector(0, 0, -1)
    And normalv = Vector(0, 0, -1)
    And light = point_light(Point(0, 0, -10), Color(1, 1, 1))
  When c1 = lighting(m, light, Point(0.9, 0, 0), eyev, normalv, False)
    And c2 = lighting(m, light, Point(1.1, 0, 0), eyev, normalv, False)
  Then c1 == Color(1, 1, 1)
    And c2 == Color(0, 0, 0)
