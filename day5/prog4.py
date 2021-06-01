# create a class cal1 that will calculate square number. create setdata() method which has one parameter that contain number.create display() method that will calculate square


class cal4:
    def setdata(self, num):
        self.n = num

    def display(self):
        return (self.n*self.n)


obj = cal4()
obj.setdata(3)
print(obj.display())
