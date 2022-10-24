class Logger:
    def __enter__(self):
        print("Open database connection for logging")
        return self

    def __exit__(self, type, value, traceback):
        print("type:", type)
        print("value:", value)
        print("traceback:", traceback)
        print("Close database connection")

    def log(self, message):
        print("Log to database:", message)

with Logger() as logger:
    logger.log("Start division")
    a = 10
    b = 0
    print(a / b)
    logger.log("End division")

print("The end")