"""
In sets elements are not repeated...
they don't have any indexes.
cannot include list and dictionaries in sets.
only includes tuple.
"""

my_set = set([1, 2, 3, 4])
print(type(my_set))
print(my_set)

other_set = {1, 2 , 3 , 4, 4 }
print(other_set)

my_sets1 = {1,2,3,(25,32,63),4}
print(my_sets1)

print(len(my_sets1))
print(2 in my_sets1)

# set joining .UNION()
s1 = {1,2,3}
s2 = {3, 4 ,5}
s3 = s1.union(s2)
print(s3)

s1.add(45)
print(s1)

s1.remove(45)
print(s1)

s1.discard(7)
print(s1)

print(s1.pop())

s1.clear()
print(s1)

