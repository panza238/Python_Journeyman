"""Method inheritance"""
from class_attributes import ShippingContainer
import random


class RefrigeratedContainer(ShippingContainer):

    equipo = "BOKE"

    def __init__(self, owner_code, contents, temperature):
        """I am overriding the parent class' __init__ method"""
        # With super().__init__ I am calling the parent's class initializer (miss-called "constructor")
        super().__init__(owner_code, contents)  # super() invokes the parent class
        self._temp = temperature
        self._security_number = self._get_random_number()
        self._team = RefrigeratedContainer.equipo

    @staticmethod
    def _get_random_number():
        """This is overriding the previous _get_random_number() static_method"""
        return random.randint(100, 999)

    @property
    def team(self):
        """The property decorator allows me to use .team as an attribute"""
        return self._team


if __name__ == "__main__":
    c1 = ShippingContainer("Panza", "Books")
    c2 = RefrigeratedContainer("Penny", "Meat", "10")

    print("c1", c1._security_number)
    print("c2", c2._security_number)
    print()
    print("Dicts:")
    print("c1", c1.__dict__)
    print("c2", c2.__dict__)
    print()

    # Create a container from @classmethod alternative initializer
    print("Inheritance and alternative constructors!")
    csv_string = "Cluster,Muesitos"
    try:
        c3 = RefrigeratedContainer.from_csv_string(csv_string)
    except TypeError:
        print("This fails because from_csv_string method cannot accommodate the extra argument 'temperature'")
        print("We have to use *args and **kwargs to make it work.")
        c3 = RefrigeratedContainer.other_from_csv_string(csv_string, temperature=10)
    print("c3, created from inherited alternative initializer", c3.__dict__)
    print(c3.team)
    c3.team = "BOQUITA"
    print(c3.team)  # Notice that, in spite of being a method, I can call team as an attribute!
