"""Implementing my own iterator."""


class ExampleIterator(object):
    """Example of the implementation of an iterator"""
    def __init__(self):
        self.index = 0
        self.data = [1, 2, 3]

    def __iter__(self):
        """This method is necessary to generate the iterator"""
        return self

    def __next__(self):
        """This is the method that will be called when next() is called on the object
        This method will literally return the next item."""
        if self.index >= len(self.data):
            # Iterator depleted.
            raise StopIteration()
        rslt = self.data[self.index]
        self.index += 1
        return rslt

# From the REPL, I can import the Example iterator.
