"""
1.upper() - use uppercase
2.lower() - use lowercase
3.split() - separate into parts(list)
4.join() - put items together
5.find() - find a sub-string
6.replace() - use for replacing a sub-string
There are also many dont forget to check them on google.
"""
text = "We are going to learn six methods today"
#upper()
result = text.upper()
print(result)

result = text[4].upper()
print(result)

#lower()
result = text.lower()
print(result)

#split()
result = text.split(" ")
print(result)

result = text[4].split(" ")
print(result)

result = text.split("o")
print(result)

#join()
a = "Learning"
b = "Python"
c = "is"
d = "amazing"
e = " ".join([a,b,c,d])
print(e)

#find()
result = text.find("s")
print(result)

#replace()
result = text.replace("e","x")
print(result)




