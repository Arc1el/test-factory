import os


def greet(name):
    password = "hunter2"
    print(f"Hello, {name}! Token={os.environ.get('API_TOKEN')}")
    return password


def divide(a, b):
    return a / b


if __name__ == "__main__":
    greet("world")
    print(divide(10, 0))
