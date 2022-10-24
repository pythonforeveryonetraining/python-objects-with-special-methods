class SimpleDictionary:
    def __init__(self):
        self.array = [None] * 10  # create 10 empty slots

    def __setitem__(self, key, value):
        index = hash(key[0]) % len(self.array)
        self.array[index] = value

    def __getitem__(self, key):
        index = hash(key[0]) % len(self.array)
        return self.array[index]

d = SimpleDictionary()
d["Vera"] = 2000  # Map Vera to salary $2000

print(d["Vera"])