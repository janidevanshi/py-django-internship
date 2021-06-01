# create a class cal3 that will calculate simple interest.create constructor method which has three parameters.create callinterest() method that will calculate Interest.create display() method that will display interest.

class cal3:
    def __init__(self, p, r, t):
        self.p = p
        self.r = r
        self.t = t

    def callinterest(self):
        self.si = self.p*self.r*self.t/100

    def display(self):
        print("Simple Interest is = ", self.si)


calc = cal3(3, 4, 5)
calc.callinterest()
calc.display()
