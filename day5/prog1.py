# create a class cal1 that will calculate sum of three numbers. create setdata() method which has three parameters that contains numbers.create display() method that will calculate sum and display sum


class cal1:
    def setdata(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        print("Sum = ", self.x+self.y+self.z)


calc = cal1()
calc.setdata(4, 5, 6)
calc.display()
