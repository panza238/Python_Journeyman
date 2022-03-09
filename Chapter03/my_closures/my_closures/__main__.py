"""__main__ module to make the package an executable"""
# Should I chmod the package??
from decorator_example import (
    northern_city,
    test_function_01,
    test_function_02,
    test_function_03,
    DecoratedMethods,
    create_list
)

# Demonstrating the use of the first decorator.
print("Function as decorator")
city_name = northern_city()
print(city_name)
print()
# Demonstrating the use of the Class as a decorator.
print("Class as decorator")
test_function_01()
test_function_01()
test_function_01()
print("Showing type for test_function_01", test_function_01)
# This prints an instance of the ClassCounter class used as a decorator
print()
# Demonstrating the use of an instance as a decorator.
print("Instance as decorator")
test_function_02()
test_function_02()
print("Showing type for test_function_02", test_function_02)
# This prints the function defined inside the instance used as a decorator
print("Showing closures for test_function_02", test_function_02.__closure__)
print()
# Demonstrating the thing I built
print("Function 03. Understanding decorators")
test_function_03()
test_function_03()
test_function_03()
print()
# Demonstrating decorated methods
print("Decorated methods")
dm_instance = DecoratedMethods()
print('Function printed:')
b = dm_instance.decorated_method()
print('Function returned:',b)
print()
# DECORATOR FACTORIES:
print("Decorator factories")
list1 = create_list(1, 2)
# list2 = create_list(3, -4)
print(create_list)
