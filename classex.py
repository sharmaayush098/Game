class Circle(object):

    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius**2 * Circle.pi * 2


a = Circle(4)
print(a.area())
