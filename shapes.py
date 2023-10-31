# ADD YOUR SHAPES CLASSES HERE
import math

class Shape:
    pass

class Rectangle(Shape):
     
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area
    
    def get_perimeter(self):
        perimeter = self.width * 2 + self.height * 2
        return perimeter
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area (self):
        area = math.pi * (self.radius * self.radius)
        return area
    
    def get_perimeter(self):
        perimeter = (2*(math.pi)) * self.radius
        return perimeter
    
circ = Rectangle(1,9)
print(circ.get_area())