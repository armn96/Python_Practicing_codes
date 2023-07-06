"""Tuples are immutable"""

my_tup = (1, 2, 3, 4, 5)
print(type(my_tup))
print(my_tup[0])
print(my_tup[-2])

t = (5, 5.6, 'FFF')
print(t)

my_tup = (1, 2, (10,20),3, 4, 5)
print(my_tup[2][0])

my_tup = list(my_tup)
print(my_tup)

t = (1,2,3)
x, y, z = t
print(x,y,z)

t2 = (1,2,3,1)
print(len(t2))
print(t2.count(1))
print(t2.index(2))