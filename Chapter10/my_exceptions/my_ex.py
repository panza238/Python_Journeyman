"""Exceptions"""


def mro_exapmple_1():
    list1 = [1, 2, 3]
    dict1 = {"one": 1, "two":2}

    try:
        a = list1[3]
    except IndexError as e:
        print("Handling:", str(e))

    try:
        b = dict1["three"]
    except KeyError as e:
        print("Handling:", str(e))


def mro_exapmple_2():
    list1 = [1, 2, 3]
    dict1 = {"one": 1, "two": 2}

    try:
        a = list1[3]
    except LookupError as e:
        print("Handling:", str(e))

    try:
        b = dict1["three"]
    except LookupError as e:
        print("Handling:", str(e))


class MyCustomException(Exception):
    """This is my own exception.
    I have to invesitgate about how it works... But I have a good reference here."""

    def __init__(self):
        super().__init__()

    def __str__(self):
        return "This is MY exception... not so sure how does it work, but it is nice to know I have a reference here"

    def __repr__(self):
        return "This is MY exception... not so sure how does it work, but it is nice to know I have a reference here"


def my_exception_example():
    if (a := 1) == 1:
        raise MyCustomException


if __name__ == "__main__":
    # Both exceptions have a common mother class in their MRO. Both inherit from LookupError
    print(KeyError.__mro__)
    print(IndexError.__mro__)
    mro_exapmple_1()
    mro_exapmple_2()
    my_exception_example()
