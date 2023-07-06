my_list = ['a', 'b', 'c']
print(my_list)
print(type(my_list))

result =  len(my_list)
print(result)

result = my_list[0:2]
print(result)

another_list = ['hello', 55, 65.5]
print(another_list)

my_list1 = ['a', 'b', 'c']
my_list2 = ['d','e','f']
my_list3 = my_list1+my_list2
my_list3[0] = "Alpha" # We cannot do it in string
#append
my_list3.append("g")
#pop
deleted = my_list3.pop()
print(my_list3)
print(deleted)

# sort list
list1 = ['g','b','a','d','c']
list1.sort()
list2  = list1
print(list2)

# reverse
list1.reverse()
print(list1 )





