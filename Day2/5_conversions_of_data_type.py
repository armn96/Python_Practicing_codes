# two types of conversion
# 1.implicit - done automatically by python
# 2.explicit - user need to convert one data to another.
num1 = 20
print(type(num1))
num2 = 20.5
print(type(num2))
num1 = num1+num2
print(num1)

age = (input("Tell me your age:"))
age = int(age)
new_age = 1 + age
print(f"Your new age will be {new_age}")