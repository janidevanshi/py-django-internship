# Consider an employee class, which contains fields such as name and designation. And a subclass, which contains a field salary. Write a program for inheriting this relation.

class Fields():
    def info(self, name, designation):
        print("My name is ", name)
        print("my designation is", designation)


class subfield(Fields):
    def salary(self, salary):
        print("My salary is ", salary)


employee = subfield()
employee.info("Devanshi", "Software developer")
employee.salary(40000)
