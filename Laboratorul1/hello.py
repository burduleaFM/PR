import os


def hello(name):
    if not name:
        print("Lipseste numele")
    else:
        print("Hello " + name)


hello(input("NUme:"))
