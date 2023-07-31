class Shape:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=self.radius*self.radius
        print(f"{area}")

class triangle(Shape):
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def area(self):
        area=(0.5)*self.b*self.h
        print(f"area of triangle:{area}")


        
class circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        area=(3.14)*self.radius*self.radius
        print(f"area of circle:{area}")


def area_of_shape(shape):
    return shape.area()


t=triangle(5,6)
area_of_shape(t)
c=circle(5)
area_of_shape(c)

# area of triangle:15.0
# area of circle:78.5