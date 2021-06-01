# Create a class cal6 that will calculate area of a square. Create setdata() method that should take length from the user. Create area() method that will calculate area . Create display() method that will display area .

class cal6:
    def setdata(self, l):
        self.l = l

    def display(self):
        print("Area of square is = ", self.l*self.l)


l = int(input("Enter length: "))


calc = cal6()
calc.setdata(l)
calc.display()
