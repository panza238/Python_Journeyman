"""Module to demonstrate closures"""

x = """
    This variable can be whatever I like. It will not be printed.
    It will be shadowed by the x variable inside the scope of the function.
    This will never print
"""


def first_class_function(x="This WON'T be printed either!"):
    """I will define a function inside this function to demonstrate closures
    in the def statement, x is a parameter
    in the code-block x is a local variable"""
    x = "This will be covered by the closure"

    def closure_function():
        print(x)

    return closure_function
# So, the idea is that once the main function has returned the closure function, variable x disappears
# This is because x is defined within the scope of the function. So it basically dies with it.
# But, the closure "covers" x, because closure_function needs x


def main():
    fn = first_class_function()
    fn()
    print(type(fn))
    print(fn.__closure__)  # This will show that it is storing a str object in a "cell"

# En vez de hacer esto... es mucho más cómodo hacer tu paquete ejecutable que ejecutar un script dentro de tu paquete
# Por eso es util el modulo __main__.py.py


if __name__ == "__main__.py":
    main()
