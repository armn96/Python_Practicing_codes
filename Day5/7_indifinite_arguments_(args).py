def a_sum(*args):
    return sum(args)
""" OR
    total = 0
    for arg in args:
        total = total + arg
    return  total
"""

print((a_sum(5,5,5,80)))