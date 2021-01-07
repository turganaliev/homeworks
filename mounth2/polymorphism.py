from math import pi

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b

class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return pi * self.r * 2

class Square:
    def __init__(self, s):
        self.s = s

    def get_area(self):
        return self.s * self.s


areas = [Rectangle(3, 4), Circle(5), Square(4)]
for i in areas:
    print(i.get_area())