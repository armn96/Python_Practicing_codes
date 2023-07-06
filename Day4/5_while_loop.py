"""break
  continue
  pass -- do nothing"""

coins = 5
while coins > 0:
    print(f"I have {coins} coins")
    coins = coins -1
else:
    print("I have no money anymore")

answer = "y"
while answer == "y":
    answer = input("do you want to continue(y/n): ")
else:
    print("Thank you")

# pass
answers = 'p'
while answers == 'y':
    pass

name = input("Your name:")
for letter in name:
    if letter == 'r':
        break
    print(letter)


name = input("Your name:")
for letter in name:
    if letter == 'r':
        continue
    print(letter)