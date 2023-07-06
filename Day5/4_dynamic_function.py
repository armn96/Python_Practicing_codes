""" functions & loops & if-elif-else"""
def check_3_digits(number):
     return number in range(100, 1000)


sum = 512 + 30
result = check_3_digits(sum)
print(result)


def check_3_digits(list1):

    list2 = []
    for item in list1:
        if item in range(100, 1000):
            list2.append(item)
        else:
            pass

    return list2


a = int(input("Enter how many time do you want to input number: "))
list3 = []
for i in range(a):
    list3.append(int(input("Enter Lists number : ")))

result = check_3_digits(list3)
print(result)
