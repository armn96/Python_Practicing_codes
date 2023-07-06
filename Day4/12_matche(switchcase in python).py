"""series = 'N-02'

if series == 'N-01':
    print("Samsung")
elif series == 'N-02':
    print("Nokia")
elif series == "N-03":
    print("Motorolla")
else:
    print("Your model is not listed")"""

"""series = input("Enter you Series:")
match series :
     case 'N-01':
          print("Samsung")
     case  'N-02':
          print("Nokia")
     case  "N-03":
          print("Motorolla")
     case _:
          print("Your model is not listed")"""


client = {
     'name': 'Arman',
     'age' : 30,
     'occupation' : 'Doctor'}

movie = {
     'title' : 'Matrix',
     'credits' : {'main_star' : 'keaunu reeves',
                        'director': "Lana & Lily"},
}

items = [client, movie, "book"]

for i in items:
     match i:
          case {'name': name,
                   'age': age,
                   'occupation': occupation}:
                   print("It is a client")
                   print(name, age , occupation)
          case { 'title' : title,
                      'credits' : {
                          'main_star': main_star,
                          'director': director}}:
                      print("This is a movie")
                      print (title, main_star, director)
          case _:
               print("I dont know what this is")






