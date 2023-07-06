names = ["Arman", "Rumman", "Labib"]
age = [27,23,14]
cities = ['Newyork', 'London', 'Bangladesh']
combination = list(zip(names, age, cities))
print(combination)

for name, age, city in combination:
    print(f'{name} is {age} year old and lives in {city} ')