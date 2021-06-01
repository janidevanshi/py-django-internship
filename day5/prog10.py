# Create a arith class. The class should have a parameterized constructor and methods to add, subtract and multiply two numbers and to return the answers.
class arith:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b


obj = arith(4, 5)
print(obj.sum())
print(obj.sub())
print(obj.mul())
