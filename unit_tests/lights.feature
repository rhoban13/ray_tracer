Feature: Lights

Scenario: A point light has a position and intensity
  Given intensity = Color(1, 1, 1)
    And a_position = Point(0, 0, 0)
  When light = point_light(a_position, intensity)
  Then light.position == a_position
    And light.intensity == intensity