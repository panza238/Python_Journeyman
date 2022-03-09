"""Module to define the function factory"""


class FunctionFactory(object):
    """An object that will create different functions"""

    def __init__(self, default_exp=2):
        self._default_exp = default_exp

    def __del__(self):
        print('Deleting FunctionFactory object')

    def raise_to(self, exp):
        """return function that raises a number to an exp"""
        def raise_to_exp(num):
            return pow(base=num, exp=exp)

        return raise_to_exp

    def power_factory(self, *exps):
        """generate power functions from exps"""
        return (self.raise_to(exp) for exp in exps)
