#  File: Geometry.py

#  Description: Contains several classes for objects of various geometrical shapes in a 3d space, within the classes are a varitey of functions to measure and test different aspects of the objects.

#  Student Name: Michael Walter 

#  Student UT EID: AJC5423

#  Partner Name: Andrew Cheung

#  Partner UT EID: MJW3895

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 6/17/21

#  Date Last Modified:

import math
def find_points_cube(a_cube):
    minX = a_cube.x - (a_cube.side/2.0)
    minY = a_cube.y - (a_cube.side/2.0)
    minZ = a_cube.z - (a_cube.side/2.0)
    maxX = a_cube.x + (a_cube.side/2.0)
    maxY = a_cube.y + (a_cube.side/2.0)
    maxZ = a_cube.z + (a_cube.side/2.0)

    crnr1= (maxX,minY,maxZ)
    crnr2= (maxX,minY,minZ)
    crnr3= (minX,minY,minZ)
    crnr4= (minX,minY,maxZ) 

    crnr5= (maxX,maxY,maxZ)
    crnr6= (maxX,maxY,minZ)
    crnr7= (minX,maxY,minZ)
    crnr8= (minX,maxY,maxZ)

    return [crnr1, crnr2, crnr3, crnr4, crnr5, crnr6, crnr7, crnr8]

def find_points_cyl(a_cyl):
    cyl_point1 = (a_cyl.x - a_cyl.radius, a_cyl.y, a_cyl.z + a_cyl.height/2.0) 
    cyl_point2 = (a_cyl.x, a_cyl.y - a_cyl.radius, a_cyl.z + a_cyl.height/2.0)
    cyl_point3 = (a_cyl.x + a_cyl.radius, a_cyl.y, a_cyl.z + a_cyl.height/2.0)
    cyl_point4 = (a_cyl.x, a_cyl.y + a_cyl.radius, a_cyl.z + a_cyl.height/2.0)
    cyl_point5 = (a_cyl.x - a_cyl.radius, a_cyl.y, a_cyl.z - a_cyl.height/2.0)
    cyl_point6 = (a_cyl.x, a_cyl.y - a_cyl.radius, a_cyl.z - a_cyl.height/2.0)
    cyl_point7 = (a_cyl.x + a_cyl.radius, a_cyl.y, a_cyl.z - a_cyl.height/2.0)
    cyl_point8 = (a_cyl.x, a_cyl.y + a_cyl.radius, a_cyl.z - a_cyl.height/2.0)
    return [cyl_point1, cyl_point2, cyl_point3, cyl_point4, cyl_point5, cyl_point6, cyl_point7, cyl_point8]

def find_points_sphere(a_sphere):
    sphere_point1 = (a_sphere.x, a_sphere.y, a_sphere.z + a_sphere.radius)
    sphere_point2 = (a_sphere.x, a_sphere.y, a_sphere.z - a_sphere.radius)
    sphere_point3 = (a_sphere.x, a_sphere.y - a_sphere.radius, a_sphere.z)
    sphere_point4 = (a_sphere.x, a_sphere.y + a_sphere.radius, a_sphere.z)
    sphere_point5 = (a_sphere.x + a_sphere.radius, a_sphere.y, a_sphere.z)
    sphere_point6 = (a_sphere.x - a_sphere.radius, a_sphere.y, a_sphere.z)
    return [sphere_point1, sphere_point2, sphere_point3, sphere_point4, sphere_point5, sphere_point6]

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0.0, y = 0.0, z = 0.0):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)

  # create a string representation of a Point
  # returns a string of the form (x, y, z)
  def __str__ (self):
    return ('({}, {}, {})').format(self.x, self.y, self.z)

  # get distance to another Point object
  # other is a Point object
  # returns the distance as a floating point number
  def distance (self, other):
    d = math.sqrt(((other.x-self.x)**2)+((other.y-self.y)**2)+(other.z-self.z)**2)
    return d

  # test for equality between two points
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    tol = 1.0e-6                                                                                                 # INCORPORATED TOLERANCE METHOD
    return (((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol) and (abs(self.z - other.z) < tol))) # REMOVED "IF-ELSE" -> JUST RETURN BOOLEAN IN 1 LINE 6/19 8:39PM


class Sphere (object):
    # constructor with default values
  def __init__ (self, x = 0.0, y = 0.0, z = 0.0, radius = 1.0):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.radius = float(radius)
    self.center = Point(x,y,z)

  # returns string representation of a Sphere of the form:
  # Center: (x, y, z), Radius: value
  def __str__ (self):
    return "Center: ({}, {}, {}), Radius: {}".format(self.x, self.y, self.z, self.radius) # CHANGED "sph = {str}" to "return {str}"

  # compute surface area of Sphere
  # returns a floating point number
  def area (self):
    return (4*math.pi)*(self.radius**2)

  # compute volume of a Sphere
  # returns a floating point number
  def volume (self):
    return (4.0/3*math.pi)*(self.radius**3)                        # CHANGED TO 1 LINE, RETURN VOLUME WITH NO INTERMEDIATE VARIABLE "v" 6/19 8:49 PM

  # determines if a Point is strictly inside the Sphere
  # p is Point object
  # returns a Boolean
  def is_inside_point (self, p):
    Xmax = self.x + self.radius
    Xmin = self.x - self.radius
    Ymax = self.y + self.radius
    Ymin = self.y - self.radius # DEBUGGED ERROR: CHANGED "x + radius" TO " y - radius" 9:06 PM
    Zmax = self.z + self.radius
    Zmin = self.z - self.radius

    # print(f"X: ({Xmin},{Xmax}); Y: ({Ymin},{Ymax}); Z: ({Zmin},{Zmax})") # DEBUGGING. REMOVE LATER 9:06 PM
    # print(f"Point: ({p.x},{p.y},{p.z})")
    return(p.distance(self.center) < self.radius)
    #return (Xmin<p.x<Xmax and Ymin<p.y<Ymax and Zmin<p.z<Zmax) # REMOVED EXTRANEOUS "if-else" STATEMENTS, JUST RETURN BOOLEAN 6/19 8:53 PM

  # determine if another Sphere is strictly inside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, other):
      other_sphere_points_lst = find_points_sphere(other)
    #   print("List of points is: ", other_sphere_points_lst)
      condition = True
      for i in range(0, 6):
        sphere_point = other_sphere_points_lst[i]
        sphere_point = Point(sphere_point[0],sphere_point[1],sphere_point[2])
        # print("Sphere point to check is: ", sphere_point)
        if not self.is_inside_point(sphere_point):
            condition = False
            break
    #   print("This is: ",condition)
      return condition

  # determine if another Sphere is strictly outside this Sphere
  # other is a Sphere object
  # returns a Boolean
  def is_outside_sphere (self, other):
      other_sphere_points_lst = find_points_sphere(other)
    #   print("List of points is: ", other_sphere_points_lst)
      condition = True
      for i in range(0, 6):
        sphere_point = other_sphere_points_lst[i]
        sphere_point = Point(sphere_point[0],sphere_point[1],sphere_point[2])
        # print("Sphere point to check is: ", sphere_point)
        if self.is_inside_point(sphere_point):
            condition = False
            break
    #   print("This is: ",condition)
      return condition

  # determine if a Cube is strictly inside this Sphere
  # determine if the eight corners of the Cube are inside 
  # the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube):
      other_cube_points_lst = find_points_cube(a_cube)
    #   print("List of points is: ", other_cube_points_lst)
      condition = True
      for i in range(0, 8):
        cube_point = other_cube_points_lst[i]
        cube_point = Point(cube_point[0],cube_point[1],cube_point[2])
        # print("Cube point to check is: ", cube_point)
        if not self.is_inside_point(cube_point):
            condition = False
            break
    #   print("This is: ", condition)
      return condition

  def is_outside_cube (self, a_cube):
      other_cube_points_lst = find_points_cube(a_cube)
    #   print("List of points is: ", other_cube_points_lst)
      condition = True
      for i in range(0, 8):
        cube_point = other_cube_points_lst[i]
        cube_point = Point(cube_point[0],cube_point[1],cube_point[2])
        # print("Cube point to check is: ", cube_point)
        if self.is_inside_point(cube_point):
            condition = False
            break
    #   print("This is: ", condition)
      return condition


  # determine if a Cylinder is strictly inside this Sphere
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cyl (self, a_cyl): # I corrected your code
      other_cyl_points_lst = find_points_cyl(a_cyl)
    #   print("List of points is: ", other_cyl_points_lst)
      condition = True
      for i in range(0, 8):
        cyl_point = other_cyl_points_lst[i]
        cyl_point = Point(cyl_point[0],cyl_point[1],cyl_point[2])
        # print("Cyl point to check is: ", cyl_point)
        if not self.is_inside_point(cyl_point):
            condition = False
            break
    #   print("This is: ", condition)
      return condition

  # determine if 
  # determine if another Sphere intersects this Sphere
  # there is a non-zero volume of intersection
  # other is a Sphere object
  # returns a Boolean
  def does_intersect_sphere (self, other):
      return (not self.is_inside_sphere(other)) and (not self.is_outside_sphere(other))



  # determine if a Cube intersects this Sphere
  # there is a non-zero volume of intersection
  # there is at least one corner of the Cube in 
  # the Sphere
  # a_cube is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, a_cube): 
      return (not self.is_inside_cube(a_cube)) and (not self.is_outside_cube(a_cube))

  # return the largest Cube object that is circumscribed
  # by this Sphere
  # all eight corners of the Cube are on the Sphere
  # returns a Cube object
  def circumscribe_cube (self): # I did this, I think it should be right
    d = self.radius*2
    cube_side = ((d**2)/2)**(1/2)
    return Cube(self.x, self.y, self.z, cube_side)
    


class Cube (object):
  # Cube is defined by its center (which is a Point object)
  # and side. The faces of the Cube are parallel to x-y, y-z,
  # and x-z planes.
  def __init__ (self, x = 0.0, y = 0.0, z = 0.0, side = 1.0):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.side = float(side)
    self.center = Point(x,y,z)

  # string representation of a Cube of the form: 
  # Center: (x, y, z), Side: value
  def __str__ (self):
    return('Center: ({}, {}, {}), Side: {}'.format(self.x, self.y, self.z, self.side))

  # compute the total surface area of Cube (all 6 sides)
  # returns a floating point number
  def area (self):
    return(6*(self.side**2))


  # compute volume of a Cube
  # returns a floating point number
  def volume (self):
    return(self.side**3)

  # determines if a Point is strictly inside this Cube
  # p is a point object
  # returns a Boolean
  def is_inside_point (self, p):
    min_x = self.x - (self.side/2)
    min_y = self.y - (self.side/2)
    min_z = self.z - (self.side/2)
    max_x = self.x + (self.side/2) # cleaned up formatting and variable names to meet Python standard coding conventions
    max_y = self.y + (self.side/2)
    max_z = self.z + (self.side/2)
    return ((min_x < p.x < max_x) and (min_y < p.y < max_y) and (min_z < p.z < max_z))

  # determine if a Sphere is strictly inside this Cube or
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere):
      other_sphere_points_lst = find_points_sphere(a_sphere)
    #   print("List of points is: ", other_sphere_points_lst)
      condition = True
      for i in range(0, 6):
        sphere_point = other_sphere_points_lst[i]
        sphere_point = Point(sphere_point[0],sphere_point[1],sphere_point[2])
        # print("Sphere point to check is: ", sphere_point)
        if not self.is_inside_point(sphere_point):
            condition = False
            break
    #   print("This is: ",condition)
      return condition

  # determine if another Cube is strictly inside this Cube
  # other is a Cube object
  # returns a Boolean
  def is_inside_cube (self, other):
      other_cube_points_lst = find_points_cube(other)
    #   print("List of points is: ", other_cube_points_lst)
      condition = True
      for i in range(0, 8):
        cube_point = other_cube_points_lst[i]
        cube_point = Point(cube_point[0],cube_point[1],cube_point[2])
        # print("Cube point to check is: ", cube_point)
        if not self.is_inside_point(cube_point):
            condition = False
            break
    #   print("This is: ", condition)
      return condition

  def is_outside_cube (self, a_cube):
      other_cube_points_lst = find_points_cube(a_cube)
    #   print("List of points is: ", other_cube_points_lst)
      condition = True
      for i in range(0, 8):
        cube_point = other_cube_points_lst[i]
        cube_point = Point(cube_point[0],cube_point[1],cube_point[2])
        # print("Cube point to check is: ", cube_point)
        if self.is_inside_point(cube_point):
            condition = False
            break
    #   print("This is: ", condition)
      return condition

  # determine if a Cylinder is strictly inside this Cube
  # a_cyl is a Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, a_cyl):
      other_cyl_points_lst = find_points_cyl(a_cyl)
    #   print("List of points is: ", other_cyl_points_lst)
      condition = True
      for i in range(0, 8):
        cyl_point = other_cyl_points_lst[i]
        cyl_point = Point(cyl_point[0],cyl_point[1],cyl_point[2])
        # print("Cyl point to check is: ", cyl_point)
        if not self.is_inside_point(cyl_point):
            condition = False
            break
    #   print("This is: ", condition)
      return condition

  # determine if another Cube intersects this Cube
  # there is a non-zero volume of intersection
  # there is at least one vertex of the other Cube
  # in this Cube
  # other is a Cube object
  # returns a Boolean
  def does_intersect_cube (self, other):
    return (not self.is_inside_cube(other)) and (not self.is_outside_cube(other))
        
  # determine the volume of intersection if this Cube 
  # intersects with another Cube
  # other is a Cube object
  # returns a floating point number
  def intersection_volume (self, other): 
    cube_self_corner = find_points_cube(self)
    cube_self_corner_1 = cube_self_corner[2]  #(minx,miny,minz) finding opposite corners of self cube
    cube_self_corner_2 = cube_self_corner[4]  #(maxx,maxy,maxz)

    cube_other_corner = find_points_cube(other)
    cube_other_corner_1 = cube_other_corner[2] #(minx,miny,minz) finding opposite corner of other cube
    cube_other_corner_2 = cube_other_corner[4] #(maxx,maxy,maxz)

    if self.does_intersect_cube(other)==False:
      return (0.0)
    else:
      dim_1 = max(min(cube_self_corner_2[0],cube_other_corner_2[0])-max(cube_self_corner_1[0], cube_other_corner_1[0]),0) #testing to see which corner is the min and which is the max then determining the distance between them,
      dim_2 = max(min(cube_self_corner_2[1],cube_other_corner_2[1])-max(cube_self_corner_1[1], cube_other_corner_1[1]),0) #if it is less than zero it returns zero
      dim_3 = max(min(cube_self_corner_2[2],cube_other_corner_2[2])-max(cube_self_corner_1[2], cube_other_corner_1[2]),0)
      return dim_1 * dim_2 * dim_3

  # return the largest Sphere object that is inscribed
  # by this Cube
  # Sphere object is inside the Cube and the faces of the
  # Cube are tangential planes of the Sphere
  # returns a Sphere object
  def inscribe_sphere (self):
    return(Sphere(self.x,self.y,self.z, self.side/2.0))


class Cylinder (object):
  # Cylinder is defined by its center (which is a Point object),
  # radius and height. The main axis of the Cylinder is along the
  # z-axis and height is measured along this axis
  def __init__ (self, x = 0.0, y = 0.0, z = 0.0, radius = 1.0, height = 1.0):
    self.x = float(x)
    self.y = float(y)
    self.z = float(z)
    self.radius = float(radius)
    self.height = float(height)

  # returns a string representation of a Cylinder of the form: 
  # Center: (x, y, z), Radius: value, Height: value
  def __str__ (self):
    return'Center: ({}, {}, {}), Radius: {}, Height: {}'.format(self.x,self.y,self.z,self.radius,self.height)

  # compute surface area of Cylinder
  # returns a floating point number
  def area (self):
    return((2*math.pi*self.radius*self.height)+(2*math.pi*self.radius**2))

  # compute volume of a Cylinder
  # returns a floating point number
  def volume (self):
    return(math.pi*(self.radius**2)*self.height)

  # determine if a Point is strictly inside this Cylinder
  # p is a Point object
  # returns a Boolean
  def is_inside_point (self, p): # I completely changed up this section. Removed all extraneous computations and simplified the process.
    cyl_min_x = self.x - self.radius
    cyl_max_x = self.x + self.radius
    cyl_min_y = self.y - self.radius
    cyl_max_y = self.y + self.radius
    cyl_min_z = self.z - self.height/2
    cyl_max_z = self.z + self.height/2
    return ((cyl_min_x < p.x < cyl_max_x) and (cyl_min_y < p.y < cyl_max_y) and (cyl_min_z < p.z < cyl_max_z))

  # determine if a Sphere is strictly inside this Cylinder
  # a_sphere is a Sphere object
  # returns a Boolean
  def is_inside_sphere (self, a_sphere): 
      other_sphere_points_lst = find_points_sphere(a_sphere)
    #   print("List of points is: ", other_sphere_points_lst)
      condition = True
      for i in range(0, 6):
        sphere_point = other_sphere_points_lst[i]
        sphere_point = Point(sphere_point[0],sphere_point[1],sphere_point[2])
        # print("Sphere point to check is: ", sphere_point)
        if not self.is_inside_point(sphere_point):
            condition = False
            break
    #   print("This is: ",condition)
      return condition

  # determine if a Cube is strictly inside this Cylinder
  # determine if all eight corners of the Cube are in
  # the Cylinder
  # a_cube is a Cube object
  # returns a Boolean
  def is_inside_cube (self, a_cube): 
      other_cube_points_lst = find_points_cube(a_cube)
    #   print("List of points is: ", other_cube_points_lst)
      condition = True
      for i in range(0, 8):
        cube_point = other_cube_points_lst[i]
        cube_point = Point(cube_point[0],cube_point[1],cube_point[2])
        # print("Cube point to check is: ", cube_point)
        if not self.is_inside_point(cube_point):
            condition = False
            break
    #   print("This is: ", condition)
      return condition

  # determine if another Cylinder is strictly inside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_inside_cylinder (self, other): 
      other_cyl_points_lst = find_points_cyl(other)
    #   print("List of points is: ", other_cyl_points_lst)
      condition = True
      for i in range(0, 8):
        cyl_point = other_cyl_points_lst[i]
        cyl_point = Point(cyl_point[0],cyl_point[1],cyl_point[2])
        # print("Cyl point to check is: ", cyl_point)
        if not self.is_inside_point(cyl_point):
            condition = False
            break
    #   print("This is: ", condition)
      return condition

  # determine if another Cylinder is strictly outside this Cylinder
  # other is Cylinder object
  # returns a Boolean
  def is_outside_cylinder (self, other): 
      other_cyl_points_lst = find_points_cyl(other)
    #   print("List of points is: ", other_cyl_points_lst)
      condition = True
      for i in range(0, 8):
        cyl_point = other_cyl_points_lst[i]
        cyl_point = Point(cyl_point[0],cyl_point[1],cyl_point[2])
        # print("Cyl point to check is: ", cyl_point)
        if self.is_inside_point(cyl_point):
            condition = False
            break
    #   print("This is: ", condition)
      return condition

  # determine if another Cylinder intersects this Cylinder
  # there is a non-zero volume of intersection
  # other is a Cylinder object
  # returns a Boolean
  def does_intersect_cylinder (self, other): 
    return (not self.is_inside_cylinder(other)) and (not self.is_outside_cylinder(other))


def main():
    p = Point(-3.0, 2.0, 1.0)
    q = Point(2.0, -1.0, 3.0)
    sphereA= Sphere(2.0, 1.0, 3.0, 4.0)
    sphereB = Sphere(-1.0, -2.0, -3.0, 5.0)
    cubeA = Cube(2.0, 1.0, -3.0, 4.0)
    cubeB = Cube(3.0, 2.0, -4.0, 3.0)
    cylA = Cylinder(-2.0, 1.0, -3.0, 5.0, 4.0)
    cylB = Cylinder(1.0, 5.0, 3.0, 4.0, 2.0)

    p2 = Point(2.0, 8.0, 1.0)
    sphereA2= Sphere(2.0, 7.0, 3.0, 8.0)
    #print(sphereA.circumscribe_cube())
    #print(sphereA2.is_inside_point(p2))
    #print(p2.distance(sphereA2.center)<sphereA2.radius)
    #print(sphereA2.radius)
    if p.distance(Point()) > q.distance(Point()):
        print("Distance of Point p from the origin is greater than the distance of Point q from the origin")
    else:
        print("Distance of Point p from the origin is not greater than the distance of Point q from the origin")

    if sphereA.is_inside_point(p):
        print("Point p is inside sphereA")
    else:
        print("Point p is not inside sphereA")

    if sphereA.is_inside_sphere(sphereB):
        print("sphereB is inside sphereA")
    else:
        print("sphereB is not inside sphereA")

    if sphereA.is_inside_cube(cubeA):
        print("cubeA is inside sphereA")
    else:
        print("cubeA is not inside sphereA")

    if sphereA.is_inside_cyl(cylA):
        print("cylA is inside sphereA")
    else:
        print("cylA is not inside sphereA")

    if sphereB.does_intersect_sphere(sphereA):
        print("sphereA does intersect sphereB")
    else:
        print("sphereA does not intersect sphereB")

    if sphereB.does_intersect_cube(cubeB):
        print("cubeB does intersect sphereB")
    else:
        print("cubeB does not intersect sphereB")

    largest_cube_circumscribed_by_sphereA = sphereA.circumscribe_cube()
    if largest_cube_circumscribed_by_sphereA.volume() >  cylA.volume():
         print("Volume of the largest Cube that is circumscribed by sphereA is greater than the volume of cylA")
    else:
         print("Volume of the largest Cube that is circumscribed by sphereA is not greater than the volume of cylA")

    
    if cubeA.is_inside_point(p):
        print("Point p is inside cubeA")
    else:
        print("Point p is not inside cubeA")

    if cubeA.is_inside_sphere(sphereA):
        print("sphereA is inside cubeA")
    else:
        print("sphereA is not inside cubeA")

    if cubeA.is_inside_cube(cubeB):
        print("cubeB is inside cubeA")
    else:
        print("cubeB is not inside cubeA")

    if cubeA.is_inside_cylinder(cylA):
        print("cylA is inside cubeA")
    else:
        print("cylA is not inside cubeA")

    if cubeB.does_intersect_cube(cubeA):
        print("cubeA does intersect cubeB")
    else:
        print("cubeA does not intersect cubeB")
    
    if cubeA.intersection_volume(cubeB)>sphereA.volume():
      print("Intersection volume of cubeA and cubeB is greater than the volume of sphereA")
    else:
      print("Intersection volume of cubeA and cubeB is not greater than the volume of sphereA")
    
    largest_sphere_inscribed_cubeA = cubeA.inscribe_sphere().area()
    surface_area_cylA = cylA.area()
    if largest_sphere_inscribed_cubeA > surface_area_cylA:
         print("Surface area of the largest Sphere object inscribed by cubeA is greater than the surface area of cylA")
    else:
         print("Surface area of the largest Sphere object inscribed by cubeA is not greater than the surface area of cylA")


    if cylA.is_inside_point(p):
        print("Point p is inside cylA")
    else:
        print("Point p is not inside cylA")
    
    if cylA.is_inside_sphere(sphereA):
        print("sphereA is inside cylA")
    else:
        print("sphereA is not inside cylA")
    
    if cylA.is_inside_cube(cubeA):
        print("cubeA is inside cylA")
    else:
        print("cubeA is not inside cylA")

    if cylA.is_inside_cylinder(cylB):
        print("cylB is inside cylA")
    else:
        print("cylB is not inside cylA")

    if cylA.does_intersect_cylinder(cylB):
        print("cylB does intersect cylA")
    else:
        print("cylB does not intersect cylA")

main()
