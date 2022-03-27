"""Module to test the context manager"""


class LoggingContextManager(object):
    """My own custom context manager"""

    def __enter__(self):
        print("This is printed when the with statement is executed")
        return "This text is bound to the reference in the as clause"

    def __exit__(self, exc_type, exc_val, exc_tb):
        """The __exit__ method takes in three arguments to handle exceptions"""
        if exc_type is None:
            print("Ran successfully! No exceptions found")
        else:
            print(f"Exception found!"
                  f"{exc_type}, {exc_val}, {exc_tb}")
