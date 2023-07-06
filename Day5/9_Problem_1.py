"""def return_distincts(*args):
    if sum(args) > 15:
        print("Highest Number")
    elif sum(args) < 10:
        print("Lowest Number")
    elif sum(args) >= 10 and sum(args) <= 15:
        print(f"The intermediate value is {sum(args)+1}")
    else:
        print("What!!!")

return_distincts(3,3,3,5,5)"""

def return_distincts(a,b,c):
    a_sum  = a+b+c
    a_list = [a,b,c]
    if a_sum > 15:
        print(max(a_list))
    elif a_sum < 10:
        print(min(a_list))
    else:
        a_list.sort()
        print(a_list[1])


return_distincts(5,6,2)