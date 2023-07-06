my_dictionary = {'c1' : 'value1', 'c2' : 'value2'}
print(my_dictionary)

result = my_dictionary['c1']
print(result)

customer = {'name' : 'John',
                      'last name': 'lennon',
                      'weight' : 88,
                      'height' : 1.76}
query = (customer['height'])
print(query)

dic = {
    1 : 55,
    2 : [10,20,30],
    3: {'s1' : 100, 's2' : 200}
}
print(dic[2][2])
print(dic[3]['s2'])

dic1 = {'k1' : ['a', 'b', 'c'], 'k2': ['d', 'e', 'f']}
print((dic1['k2'][1]).upper())

#add in dict
dic2 = {
    'Name' : 'Arman',
    'Id' : 123456,
    'address' : 'Kazla'
}
print(dic2)
dic2['age']  = 30
print(dic2)

print(dic2.keys())
print(dic2.values())
print(dic2.items() )