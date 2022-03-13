"""Class vs instance attributes"""
import random
import hashlib

class ShippingContainer(object):
    """A generic class to demonstrate class attributes"""

    # Define class attribute / class variable
    next_id = 1

    @classmethod
    def _get_next_id(cls):
        container_id = cls.next_id
        cls.next_id += 1  # update class variable
        return container_id

    @staticmethod
    def _get_random_number():
        return random.randint(1000, 5000)

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.container_id = self._get_next_id()
        self._security_number = self._get_random_number()

    @classmethod
    def from_csv_string(cls, csv_string):
        """This is another way to create an instance.
        It is common to use class methods as alternative constructors"""
        code, contents = csv_string.split(',')
        return cls(code, contents)

    @classmethod
    def other_from_csv_string(cls, csv_string, *args, **kwargs):
        """improved version of previous method. This new alternative constructor (INITIALIZER) makes inheritance
        easier. Making it easier to """
        code, contents = csv_string.split(',')
        return cls(code, contents, *args,**kwargs)

    @property
    def security_number(self):
        return self._security_number


if __name__ == "__main__":
    c1 = ShippingContainer("Panza", "Bikes")
    c2 = ShippingContainer("Cluster", "Bones")
    c3 = ShippingContainer("Penny", "Makeup")

    print("Container ids")
    print("c1", c1.container_id)
    print("c2", c2.container_id)
    print("c3", c3.container_id)
    print()

    print("next_id class variable")
    print("ShippingContainer class", ShippingContainer.next_id)
    print("Class instance", c2.next_id)
    print()

    print("reassigning next_id from instance:")
    c1.next_id = 10
    print("c1", c1.next_id)  # c1 now has a next_id attribute (self.next_id)
    print("c2", c2.next_id)  # c2 DOES NOT have a next_id attribute. It fetches next id from the class
    print("Class", ShippingContainer.next_id)
    print()

    print("reassigning next_id from class:")
    ShippingContainer.next_id = 20
    print("c1", c1.next_id)  # c1 now has a next_id attribute (self.next_id)
    print("c2", c2.next_id)  # c2 DOES NOT have a next_id attribute. It fetches next id from the class
    print("c3", c3.next_id)
    print()

    print("Showing that next_id is NOT an instance attribute unless we specifically assign it to a class"
          " (as we did with c1)")
    print("c1", c1.__dict__)
    print("c2", c2.__dict__)
    print("c3", c3.__dict__)
    print()

    # instantiating a class from an alternative constructor
    print("Instantiating with @classmethod")
    input_string = "Panza,Books"
    c4 = ShippingContainer.from_csv_string(input_string)
    print(c4)
    print(c4.__dict__)
