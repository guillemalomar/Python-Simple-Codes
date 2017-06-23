
class Shape(object):

    def __init__(self, *args):
        if len(args) == 3:
            self.object = Triangle(*args)
        elif len(args) == 2:
            if args[0] == args[1]:
                self.object = Square(*args)
            else:
                self.object = Rectangle(*args)
        else:
            print "Error, wrong constructor"

    def draw(self):
        return self.object.name

    def get_area(self):
        return self.object.get_area()

class Rectangle(Shape):

    def __init__(self, *args):
        self.width = args[0]
        self.height = args[1]
        self.name = 'Rectangle'

    def get_area(self):
        return self.width * self.height

class Square(Shape):

    def __init__(self, *args):
        self.width = args[0]
        self.height = args[1]
        self.name = 'Square'

    def get_area(self):
        return self.width * self.height

class Triangle(Shape):

    def __init__(self, *args):
        self.a = float(args[0])
        self.b = float(args[1])
        self.c = float(args[2])
        self.name = 'Triangle'

    def get_area(self):
        # calculate the semi-perimeter
        s = (self.a + self.b + self.c) / 2

        # calculate the area
        area = (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5
        return area
        return 0

myTriangle = Shape(2, 3, 4)
print "myTriangle.name:", myTriangle.draw()
print "myTriangle.area:", myTriangle.get_area()

mySquare = Shape(4, 4)
print "mySquare.name:", mySquare.draw()
print "mysquare.area:", mySquare.get_area()

myRectangle = Shape(2, 3)
print "myRectangle.name:", myRectangle.draw()
print "myRectangle.area:", myRectangle.get_area()
