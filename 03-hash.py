class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def __eq__(self, other):
        return self.emp_id == other.emp_id

    def __hash__(self):
        return self.emp_id

e1 = Employee(1, "Vera")
e2 = Employee(2, "Chuck")

buddies = {e1: e2}
print(buddies[e1].name)

e1.emp_id = 7  # this is a bad idea!
print(buddies[e1])
