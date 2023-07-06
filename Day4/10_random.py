from random import *
"""
There are 5 main random methods:
1. randint()
2.uniform()
3.random()
4.choice()
5.shuffle()
"""

# 1. randint() ----(random integer)
my_random = randint(1,50)
print(my_random)

# uniform() ---- float values
my_random = uniform(1,50)
print(my_random)

# random
my_random = random()
print(my_random)

# choice()
color = ['blue', 'teal', 'yellow', 'red', 'black']
my_random = choice(color)
print(my_random)

# shuffle()
numbers = list(range(5,50,5))
shuffle(numbers)
print(numbers)


