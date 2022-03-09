"""How do decorators work? In thi episode I'll show you this and much more!"""
import functools


def only_ascii(f):
    """This will be my decorator.
    the f parameter must be a callable
    and it will return another callable"""

    # This decorator allows to get the __name__ and __doc__ attributes from f, instead of only_ascii
    @functools.wraps(f)
    def wrap(*args, **kwargs):
        """This function wil 'wrap around' the input funciton.
        This is the callable I am going to return in the end"""
        print("Hello from the wrapper!\nThis is the decorator code running")
        # JUST A WRAPPER
        a = ascii(f(*args, **kwargs))
        # Returns the return value of the function!
        return a
    # RETURNS CALLABLE!
    return wrap


# The decorator is implemented in the function's definition
@only_ascii
def northern_city():
    return "Tromsø"


# ANY CALLABLE CAN BE A DECORATOR
class ClassCounter(object):

    def __init__(self, f, magic_number=0):
        self._f = f
        self._count = 0
        self._magic_number = magic_number

    def __call__(self, *args, **kwargs):
        """Here, the __call__ method will act as the wrapper!
        So, the class is the decorator. Since the class implements the __call__method, it is callable.
        The class then returns the __call__ method, which is the callable returned to be executed"""
        self._count += 1
        print(f"Ran {self._count} times")
        return_value = self._f(*args, **kwargs)
        # This is the wrapper!
        # It is not returning a callable, but the result of the execution.
        # The ClassCounter class is actually returning the callable. Which is the __call__ method!!
        return return_value


class InstanceCounter(object):
    """Same approach than ClassCounter, but different. In this case, an instance of the class
    will be the decorator. So the __call__ method will be the decorator, and we are going to have to define
    a wrapper function inside this method"""

    def __init__(self):
        pass

    def __call__(self, f):
        """This will be my decorator!! This MUST return a callable!"""
        counter = 0  # THIS WILL BE COVERED BY THE WRAPPER CLOSURE!

        def wrapper(*args, **kwargs):
            nonlocal counter
            counter += 1
            print(f"Calling {f}")
            return_value = f(*args, **kwargs)
            print(f"Ran {counter} times")
            # This returns a value!
            return return_value
        # This returns a callable!
        return wrapper


class NotSoObvious(object):
    """I don't quite understand how this works
    But, if I use it as a decorator on my_test_function, It works as I intend it to"""
    def __init__(self, f):
        self._f = f
        self._count = 0

    def __call__(self, *args, return_value=20, **kwargs):
        """by implementing the __call__ method I make the class a callable object.
            So, I will be able to use it as a decorator!
            The class IS the decorator. So __call__ is the wrapper"""
        print("This will print before the function is ran")
        f_return = self._f(*args, return_value + self._count, **kwargs)
        self._count += 1
        print(f"So far, the function ran {self._count} times")

        # The return value is not the callable itself... but a call to the previously defined function!
        # This is great for a NOT SO OBVIOUS PYTHON post!
        # This returns a return value. The class returns the callable, which is __call__ !
        return f_return
# I now understand how it works!!

""" Decided to save this "mistake", since it might be useful
        def __call__(self):
        \"""by implementing the __call__ method I make the class a callable object.
            So, I will be able to use it as a decorator!
            The class IS the decorator. So __call__ is the wrapper\"""

        def wrapper(*args, **kwargs):
            print("This will print before the function is ran")
            f_return = self._f(*args, **kwargs)
            self._count += 1  # The _count attribute will keep track of how many times is the function used
            print(f"So far, the function ran {self._count} times")
            return f_return

        # The return value is not the callable itself... but a call to the previously defined function!
        # This is great for a NOT SO OBVIOUS PYTHON post!
        # This returns a return value. The class returns the callable, which is __call__ !
        return wrapper(return_value=10 + self._count)"""


# A decorator factory: it returns decorators
def check_non_negative(index):
    """Decorator Factory
    It creates a validator decorator, based on the index parameter"""
    # This is the actual decorator
    def validator(f):
        """Decorator to be returned"""
        #  This is the wrapper function
        @functools.wraps(f)  # This decorator works even in the decorator factory!! Nice!
        def wrap(*args):
            """wrapper function"""
            if args[index] < 0:
                raise ValueError('Argument {} must be non-negative.'.format(index))
            # Wrap returns a value
            return f(*args)
        # Validator returns a callable. IT IS A DECORATOR!
        return wrap
    # check_non_negative returns a callable, the decorator!!!
    return validator


@ClassCounter
def test_function_01(return_value=10):
    print(f"This is the function running, and the return value will be {return_value}")
    return return_value


inst_counter = InstanceCounter()
@inst_counter
def test_function_02():
    print("This function just prints this... Not much more")


@NotSoObvious
def test_function_03(return_value=10):
    print(f"Function 03 running. Return value: {return_value}")
    return return_value


class DecoratedMethods(object):
    """The methods in this class will be decorated"""

    def __init__(self):
        self._text = "This is the class' text.\n" \
                     "ASCII: a e i o u\n" \
                     "NON-ASCII: ü ö ï ë ä\n"

    @only_ascii
    def decorated_method(self):
        print(self._text)
        return self._text


@check_non_negative(1)  # This checks that list[1] (1 is PARAMETER!) is not negative. If it is, it will raise an exception
def create_list(value, size):
    print("Hello from the create_list function! If the size is negative, this will not print!")
    return [value] * size
