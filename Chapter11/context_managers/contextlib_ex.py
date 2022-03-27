"""Module to demonstrate how contextlib works!"""
import contextlib
import sys


@contextlib.contextmanager
def my_cm(my_var):
    try:
        print("I'm managing this context")
        yield my_var

        print("This prints in case of successful execution")

    except Exception as e:
        print("This prints in case of an EXCEPTION",
              sys.exc_info())
        # propagate the exception upwards.
        # otherwise, it "swallows" the exception
        raise e
