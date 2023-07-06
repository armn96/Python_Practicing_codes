name = ['Arman', 'Rumman', 'Tanvir']
for item in name:
    print(f"Hello {item}")

my_list = ['a','b','c','d']
for letter in my_list:
    letter_index = my_list.index(letter)+1
    print(f"Letter {letter_index}: {letter}")

my_list = ['Paul', "Laura", "Luis", "Zak", "Arman"]
for name in my_list:
    if name.startswith("L"):
        print(name)

number = [1,2,3,4,10,11 ]
my_value = 0
for num in number:
    my_value = my_value + num
    print(my_value)

print(my_value)

word = "python"
for ltr in word:
    print(ltr)

for letter in (1,2,3,4,5):
    print(letter)

for a, b, c in [[1,2,3],[4,5,6],[7,8,9]]:
    print(a)
    print(b)
    print(c)

dic = {"key1" : "a", "key2": "b", "key3": "c"}
for item in dic.items():
    print(item)

for item in dic.values():
    print(item)

for k, v in dic.items():
    print(k , v)