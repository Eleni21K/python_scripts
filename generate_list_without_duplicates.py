'''
Take two lists and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
Write this using at least one list comprehension. 
Extra:

Randomly generate two lists to test this
'''

import random

a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result = [i for i in set(a) if i in b]
print(result)

