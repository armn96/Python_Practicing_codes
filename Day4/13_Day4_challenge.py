from random import *
name = input("Enter Your name: ")
print(f"Well {name}, I've thought of a number between 1 and 100 and youhave only eight tries to guess it. What number do you think it is")

tries = 9
num = randint(1,100)
while tries > 0:
    tries = tries -1
    if tries == 0:
        print("Game Over")
        print(f"The secret key is {num}")
        break
    secret_key = int(input("Enter the secret key: "))
    if (secret_key <=  0 or secret_key >= 101) :
        print("You choose a number outside the range")
    elif secret_key < num:
        print("Wrong number, You choose lower number")
    elif secret_key > num:
        print("Wrong number, You choose higher number")
    elif secret_key ==  num:
        print("Congratulations!!\n You Win")
        break
    else:
        print("Invalid")





