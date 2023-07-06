"""def count_prime_num(num):

    flag = False

    if num == 1:
        print("This is not a prime number")

    elif num > 1:
        for i in range(2, num):
            if (num % i == 0):
                flag = True
                break
        if flag:
            print(f'{num} is not a prime number')
        else:
            print(f"{num} is a prime number")


number = input('Enter a numbe: ')
count_prime_num(int(number))"""



def count_prime(number):

     prime_numbers = [2]
     iteration = 3

     if number < 2:
         return 0

     while iteration <= number:
         for n in range(3, iteration, 2):
             if iteration %n == 0:
                 iteration += 2
                 break
         else:
                 prime_numbers.append(iteration)
                 iteration += 2
     print(prime_numbers)
     return len(prime_numbers)


print(count_prime(15))

