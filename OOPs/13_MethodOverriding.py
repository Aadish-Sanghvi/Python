class Shape:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def area(self):
      return self.x * self.y

class Circle(Shape):
    def __init__(self, radius):
    #   self.radius = radius
      super().__init__(radius, radius)

    def area(self):
        return 3.14 *  super().area()
    
class Rectangle(Shape):
    def __init__(self, width, breadth):
    #   self.width = width
    #   self.breadth = breadth
      super().__init__(width, breadth)

    def area(self):
      return super().area()
      
# rec = Shape(3, 5)
# print(rec.area())

c = Circle(5)
print(c.area())

d = Rectangle(3,6)
print(d.area())