class DirectoryItem:
    def __init__(self, name):
        self.name = name
        self.is_directory = name.endswith("/")

    def __str__(self):
        return self.name

    def __lt__(self, other):
        if self.is_directory == other.is_directory:
            return self.name < other.name
        return self.is_directory

directory = [
    DirectoryItem("log.txt"),
    DirectoryItem("settings/"),
    DirectoryItem("test.txt"),
    DirectoryItem("archive/"),
    DirectoryItem("config.txt"),
]

for d in sorted(directory):
    print(d)

