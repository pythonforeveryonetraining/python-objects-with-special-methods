class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, value):
        self.items.append(value)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        print(index)
        return self.items[index]

todo_list = TodoList()
todo_list.add_item("Call Harry")
todo_list.add_item("Clean sink")
todo_list.add_item("Read book")

print(f"The list has {len(todo_list)} items.")
print(todo_list[1:3])
