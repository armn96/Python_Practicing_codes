"""**kwargs is for dictionaries"""

"""def a_sum(**kwargs):

   total = 0
   for key, value in kwargs.items():
       print(f'{key} = {value}')

       total += value

   return total


print(a_sum(x = 3, y = 5, z = 2))"""


def test(number1, number2, *args, **kwargs):
    print(f"The first number is {number1}")
    print(f"The second number is {number2}")

    for item in args:
        print(f"arg : {item}")

    for key, value in kwargs.items():
       print(f'{key} = {value}')


"""test(25,14,(25,23,25), x=2,y=5,z =6)"""
"""                          OR                                """
arg = [100,200,300,400]
kwargs = {'x': 'one', 'y': 'two', 'z': 'three'}
test(25,52,*arg,**kwargs)


