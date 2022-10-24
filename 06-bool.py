class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __bool__(self):
        return len(self.name) > 0 and self.salary > 0

e = Employee("Vera", 0)
if e:
    print(e)
