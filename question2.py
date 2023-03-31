#Question
'''
Create a shape program, that has the shapes:

Triangle,
Square,
Circle,
Hexagon,
Pentagon.

you must store how many points they have and what shape they are. 
Also have a method called describe which outputs what the shape is and how many points it has.

add them all to a list and output there describe methods.

Hints: Try to use inheritance and polymorphism.
'''

class Shape():
    def __init__(self, points, shape):
        self.points = points
        self.shape  = shape

    def describe(self):
        return self.shape + ' shape, It has ' +str(self.points)+ ' points'

class Triangle(Shape):
    def __init__(self, points, shape, colour):
        super().__init__(points, shape)

class Square(Shape):
    def __init__(self, points, shape):
        super().__init__(points, shape)

class Circle(Shape):
    def __init__(self, points, shape):
        super().__init__(points, shape)

class Hexagon(Shape):
    def __init__(self, points, shape):
        super().__init__(points, shape)

class Pentagon(Shape):
    def __init__(self, points, shape):
        super().__init__(points, shape)

    def describe(self):
        return self.shape + ' shape, It has ' +str(self.points)+ ' points'

def Main():

    shapes = [
        Triangle(3, "Triangle", "White"),
        Square(4, "Square"),
        Circle(0, "Circle"),
        Hexagon(6, "Hexagon"),
        Pentagon(5, "Pentagon")
        ]

    for shape in shapes:
        print(shape.describe(),"\n")

if __name__=='__main__':
    Main()
