class Todo:
    def __init__(self, todo_id, text):
        self.todo_id = todo_id
        self.text = text

    def __eq__(self, other):
        return self.todo_id == other.todo_id

todos = [
    Todo(1, "Call Harry"),
    Todo(2, "Buy milk"),
    Todo(3, "Read book")
]

json = {"todo_id": 2, "text": "Buy milk and cookies"}
updated_todo = Todo(json["todo_id"], json["text"])

print(updated_todo in todos)

todo = Todo(4, "Install sound drivers")
print(todo not in todos)
