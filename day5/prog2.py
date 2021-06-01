# create a class cal2 that will calculate area of circle.create setdata() method that should take radius from the user.create area method that will calculate area.create display() method that will display area.
from math import pi


class cal2():
    def setdata(self, r):
        self.r = r

    def display(self):
        print("Area of circle is = ", pi*self.r*self.r)


r = int(input("Enter radius: "))


calc = cal2()
calc.setdata(r)
calc.display()
