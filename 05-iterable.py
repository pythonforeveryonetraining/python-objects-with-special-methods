class SuperRange:
    def __init__(self, min, max):
        self.min = min
        self.max = max

    def __iter__(self):
        self.current = self.min
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current - 1
        else:
            raise StopIteration


for x in SuperRange(3, 9):
    print(x)
