Feature: Intersections

Scenario: An intersection encapsulates t and object
  Given s = Sphere()
  When i = Intersection(3.5, s)
  Then i.t == 3.5
    And i.object == s

Scenario: Precomputing the state of an intersection
  Given r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    And shape = Sphere()
    And i = Intersection(4, shape)
  When comps = prepare_computations(i, r)
  Then comps.t == i.t
    And comps.object == i.object
    And comps.point == Point(0, 0, -1)
    And comps.eyev == Vector(0, 0, -1)
    And comps.normalv == Vector(0, 0, -1)

Scenario: Precomputing the reflection vector
  Given shape = Plane()
    And r = Ray(Point(0, 1, -1), Vector(0, -√2/2, √2/2)) 
    And i = Intersection(√2, shape)                      
  When comps = prepare_computations(i, r)
  Then comps.reflectv == Vector(0, math.sqrt(2)/2, math.sqrt(2)/2)                

Scenario: The hit, when an intersection occurs on the outside
  Given r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    And shape = Sphere()
    And i = intersection(4, shape)
  When comps = prepare_computations(i, r)
  Then comps.inside == False

Scenario: The hit, when an intersection occurs on the inside
  Given r = Ray(Point(0, 0, 0), Vector(0, 0, 1))
    And shape = Sphere()
    And i = intersection(1, shape)
  When comps = prepare_computations(i, r)
  Then comps.point == Point(0, 0, 1)
    And comps.eyev == Vector(0, 0, -1)
    And comps.inside == True
      # normal would have been (0, 0, 1), but is inverted!
    And comps.normalv == Vector(0, 0, -1)
 
Scenario: The hit should offset the point
  Given r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    And shape = Sphere() with:
      | transform | Translation(0, 0, 1) |
    And i = intersection(5, shape)
  When comps = prepare_computations(i, r)
  Then comps.over_point.z < -EPSILON/2
    And comps.point.z > comps.over_point.z

Scenario: The under point is offset below the surface
  Given r = Ray(Point(0, 0, -5), Vector(0, 0, 1))
    And shape = glass_sphere() with:
      | transform | Translation(0, 0, 1) |
    And i = Intersection(5, shape)
    And xs = Intersections(i)
  When comps = prepare_computations(i, r, xs)
  Then comps.under_point.z > EPSILON/2
    And comps.point.z < comps.under_point.z

Scenario: Aggregating intersections
  Given s = Sphere()
    And i1 = Intersection(1, s)
    And i2 = Intersection(2, s)
  When xs = Intersections(i1, i2)
  Then xs.count == 2
    And xs[0].t == 1
    And xs[1].t == 2

Scenario: The hit, when all intersections have positive t
  Given s = Sphere()
    And i1 = Intersection(1, s)
    And i2 = Intersection(2, s)
    And xs = Intersections(i2, i1)
  When i = hit(xs)
  Then i == i1

Scenario: The hit, when some intersections have negative t
  Given s = Sphere()
    And i1 = Intersection(-1, s)
    And i2 = Intersection(1, s)
    And xs = Intersections(i2, i1)
  When i = hit(xs)
  Then i == i2

Scenario: The hit, when all intersections have negative t
  Given s = Sphere()
    And i1 = Intersection(-2, s)
    And i2 = Intersection(-1, s)
    And xs = Intersections(i2, i1)
  When i = hit(xs)
  Then i is nothing

Scenario: The hit is always the lowest nonnegative intersection
  Given s = Sphere()
  And i1 = Intersection(5, s)
  And i2 = Intersection(7, s)
  And i3 = Intersection(-3, s)
  And i4 = Intersection(2, s)
  And xs = Intersections(i1, i2, i3, i4)
When i = hit(xs)
Then i == i4

Scenario Outline: Finding n1 and n2 at various intersections
  Given A = glass_sphere() with:
      | transform                 | Scaling(2, 2, 2) |
      | material.refractive_index | 1.5              |
    And B = glass_sphere() with:
      | transform                 | Translation(0, 0, -0.25) |
      | material.refractive_index | 2.0                      |
    And C = glass_sphere() with:
      | transform                 | Translation(0, 0, 0.25) |
      | material.refractive_index | 2.5                     |
    And r = Ray(Point(0, 0, -4), Vector(0, 0, 1))
    And xs = intersections_shorthand(2:A, 2.75:B, 3.25:C, 4.75:B, 5.25:C, 6:A)
  When comps = prepare_computations(xs[<index>], r, xs)  
  Then comps.n1 == <n1>
    And comps.n2 == <n2>             

  Examples:
    | index | n1  | n2  |
    | 0     | 1.0 | 1.5 |                 
    | 1     | 1.5 | 2.0 |
    | 2     | 2.0 | 2.5 |
    | 3     | 2.5 | 2.5 |
    | 4     | 2.5 | 1.5 |
    | 5     | 1.5 | 1.0 |

Scenario: The Schlick approximation under total internal reflection
  Given shape = glass_sphere()
    And r = Ray(Point(0, 0, √2/2), Vector(0, 1, 0))
    And xs = intersections_shorthand(-√2/2:shape, √2/2:shape)
  When comps = prepare_computations(xs[1], r, xs)
    And reflectance = schlick(comps)
  Then reflectance == 1.0

Scenario: The Schlick approximation with a perpendicular viewing angle
  Given shape = glass_sphere()
    And r = Ray(Point(0, 0, 0), Vector(0, 1, 0))
    And xs = intersections_shorthand(-1:shape, 1:shape)
  When comps = prepare_computations(xs[1], r, xs)
    And reflectance = schlick(comps)
  Then np.round(reflectance, 2) == 0.04

Scenario: The Schlick approximation with small angle and n2 > n1
  Given shape = glass_sphere()
    And r = Ray(Point(0, 0.99, -2), Vector(0, 0, 1))
    And xs = intersections_shorthand(1.8589:shape)
  When comps = prepare_computations(xs[0], r, xs)
    And reflectance = schlick(comps)
  Then np.round(reflectance, 5) == 0.48873

# Scenario: An intersection can encapsulate `u` and `v`
#   Given s â† triangle(point(0, 1, 0), point(-1, 0, 0), point(1, 0, 0))
#   When i â† intersection_with_uv(3.5, s, 0.2, 0.4)
#   Then i.u = 0.2
#     And i.v = 0.4
