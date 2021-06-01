# create a class cal5 that will calculate area of rectangle.create constructor method which has two parameters.create callArea() method that will calculate area of rectangle.create display() method that will display area of rectangle.

class cal5():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def callArea(self):
        self.area = self.x*self.y

    def display(self):
        print("Area of square is = ", self.area)


calc = cal5(3, 4)
calc.callArea()
calc.display()
