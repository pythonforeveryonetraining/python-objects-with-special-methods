class UserImageFactory:
    def __init__(self, database_connection):
        self.database_connection = database_connection

    def __call__(self, user_name):
        print("Access database", self.database_connection)
        return f"Image object for {user_name}"

f = UserImageFactory("sqlite")
image = f("vera")
print(image)
