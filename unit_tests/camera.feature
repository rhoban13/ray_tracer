Feature: Camera

Scenario: Constructing a camera
  #Given hsize = 160
  #  And vsize = 120
  #  And field_of_view = π/2
  When c = Camera(160, 120, π/2)
  Then c.hsize == 160
    And c.vsize == 120
    And c.field_of_view == math.pi/2
    And c.transform == Transformation(np.eye(4))
    #And c.transform = identity_matrix

Scenario: The pixel size for a horizontal canvas
  Given c = Camera(200, 125, π/2)
  Then c.pixel_size == 0.01

Scenario: The pixel size for a vertical canvas
  Given c = Camera(125, 200, π/2)
  Then c.pixel_size == 0.01

Scenario: Constructing a ray through the center of the canvas
  Given c = Camera(201, 101, π/2)
  When r = ray_for_pixel(c, 100, 50)
  Then r.origin == Point(0, 0, 0)
    And r.direction == Vector(0, 0, -1)

Scenario: Constructing a ray through a corner of the canvas
  Given c = Camera(201, 101, π/2)
  When r = ray_for_pixel(c, 0, 0)
  Then r.origin == Point(0, 0, 0)
    And r.direction == Vector(0.66519, 0.33259, -0.66851)

Scenario: Constructing a ray when the camera is transformed
  Given c = Camera(201, 101, π/2)
   And R = rotation_y(π/4)
   And T = Translation(0, -2, 5)
  When c.transform = R * T
    And r = ray_for_pixel(c, 100, 50)
  Then r.origin == Point(0, 2, -5)
   And r.direction == Vector(math.sqrt(2)/2, 0, -math.sqrt(2)/2)
    #And r.direction == Vector(√2/2, 0, -√2/2)

Scenario: Rendering a world with a camera
  Given w = default_world()
    And c = Camera(11, 11, π/2)
    And from = Point(0, 0, -5)
    And to = Point(0, 0, 0)
    And up = Vector(0, 1, 0)
    And vt = view_transform(from, to, up)
    And c.transform = vt
    #And c.transform = view_transform(from, to, up)
  When image = render(c, w)
  Then pixel_at(image, 5, 5) == Color(0.38066, 0.47583, 0.2855)
