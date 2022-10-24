class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Programmer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

p = Programmer("Vera", 2000, "Python")
print(f"{p.name} (${p.salary}) programs in {p.programming_language}")
