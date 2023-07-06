word = 'python'
my_list = []

for letter in word:
    my_list.append(letter)

print(my_list)

# List comprehension
word = 'python'
my_list = [letter for letter in word]
print(my_list)

my_list = [n for n in range(0,21,2)]
print(my_list)

my_list = [n / 2  for n in range(0,21,2)]
print(my_list)

my_list = [n if n * 2 > 10 else "no" for n in range(0,21,2) ]
print(my_list)

feet  = [10, 20, 30, 40, 50]
meters = [f * 0.3048 for f in feet]
print(meters)
