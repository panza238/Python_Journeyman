"""Deep dive into comprehensions!"""
from pprint import pprint as pp

# Multi input comprehensions (for for)
comp1 = [(x, y) for x in range(3) for y in range(4)]
pp(comp1)
l1 = ['sex', 'blood', 'sugar', 'magik']
l2 = ['red', 'hot', 'chilli', 'peppers']
comp2 = [item1 + item2 for item1 in l1 for item2 in l2]
pp(comp2)

# MAP objects! Map objects are iterators (lazy evaluation)
print('\nMAP OBJECTS')
map1 = map(len, l2)
print(map1)
print(list(zip(l2, map1)))  # Nice example of the zip method!
try:
    next(map1)
except StopIteration:
    print("Iterator depleted!")

print("\nOne function, multiple inputs")
def join_strings(s1, s2):
    return s1 + s2

map2 = map(join_strings, l1, l2)
print(list(map2))

# Filter function:
print("\nFilter function!")
def is_odd(n):
    return n % 2 != 0

l3 = list(range(1, 11))
f1 = filter(is_odd, l3)
f2 = filter(lambda n: n % 2 == 0, l3)
print(f1)
print("f1 is for evens!", list(f1))
print("f2", f2)
print("f2 is for evens!", list(f2))

# Reduce!
from functools import reduce
import operator
print('\nREDUCE!')
sum1 = reduce(operator.add, l3)
print("Sum from 1 to 10:", sum1)
