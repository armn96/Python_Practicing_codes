from random import *
# list
sticks = ['-', '--', '---', '----']

# mixing sticks
def mix(my_list):
    shuffle(my_list)
    return my_list

# choose number
def try_your_luck():
    a_try = " "
    while a_try not in ["1", "2", "3", "4"]:
        a_try = input("Choose Number: ")

    # shuffle(a_try)
    return int(a_try)

# check players try
def verify_try(a_list, a_try):
    if a_list[a_try-1] == "-":
        print("Clean the dishes")
    else:
        print("You are in the safe zone")

    print(f"You got {a_list[a_try-1]}")


sticks_mix = mix(sticks)
selection = try_your_luck()
result = verify_try(sticks_mix, selection)

"""stick = ['-','--','---','----']

def mixing_the_stick(my_list):
    shuffle(my_list)
    return my_list


def choose_your_number():
    a_try = " "
    while  a_try not in  ['1', '2', '3', '4']:
        a_try = input("choose your number: ")

    return int(a_try)


def final_result(my_list, a_try):

    if my_list[a_try-1] == '-':
        print("You have to clean the dishes")
    else:
        print("You are in the safe zone")

    print(f"You got {my_list[a_try-1]}")

    return  my_list, a_try



mixing = mixing_the_stick(stick)
choosing_number = choose_your_number()
your_luck = final_result(mixing, choosing_number)"""















