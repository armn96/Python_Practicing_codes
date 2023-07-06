"""There are three logical operators
1. AND
2.OR
3.NOT
"""

my_bool = 4 < 5 and 5 > 6
print(my_bool)

my_bool = (4 < 5) and (5 == 2+3)
print(my_bool)

my_bool = (55 == 55) and ('dog' == 'dog')
print(my_bool)

my_bool = 1 == 10 or 3 == 30
print(my_bool)

text = "This sentence is short"
my_bool = ('sentence' in text) or ('python' in text)
print(my_bool)

my_bool = not "a" != "a"
print(my_bool)