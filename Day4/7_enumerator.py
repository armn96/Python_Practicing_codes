"""Enumerator used to find indexes very simply """

my_list = ['a','b','c']
index = 0

for index, item in enumerate(my_list):
    print(index, item)

for index, item in enumerate(range(50, 55)):
    print(index, item)


my_list1 = ['a','b','c','d']
my_tuples = list(enumerate(my_list1))
print(my_tuples)
print(my_tuples[0][1])