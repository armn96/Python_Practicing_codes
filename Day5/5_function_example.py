"""coffee_price = [("cappucino", 1.5),
                          ('espresso', 1.2),
                          ('mocha', 1.9)]

for coffee , price in coffee_price:
    print(coffee, price)
    print(price * 0.45)

def most_expensive_coffee(list_of_prices):
    highest_price = 0
    my_most_expensive_coffee = ' '

    for coffee, price in list_of_prices:
        if price > highest_price:
            highest_price =price
            my_most_expensive_coffee = coffee
        else:
            pass

    return (my_most_expensive_coffee, highest_price)



coffee , price = most_expensive_coffee(coffee_price)
print(f"The most expensive coffe is {coffee} and the price is {price}")"""


cars = [("Nissan", 1000),
        ("Bugatti", 10000),
        ("Toyota", 999),
        ("Ferrari", 20000),
        ("Tata", 500)]
def max_price_of_car(max_cars_price_list):
    highest_price = 0
    expensive_car = " "

    for car_name, price in max_cars_price_list:
        if  price > highest_price:
            highest_price = price
            expensive_car = car_name
    else:
        pass

    return (expensive_car, highest_price)

def min_price_of_car(min_cars_price_list):
    lowest_price = 0
    highest_price = 0
    cheap_car = " "

    for car_name, price in min_cars_price_list:
        if price > highest_price:
            highest_price = price
        elif lowest_price < highest_price:
            lowest_price = price
            cheap_car = car_name

    else:
        pass

    return (cheap_car, lowest_price )


expensive_car, highest_price = max_price_of_car(cars)
print(f"The most expensive car is {expensive_car} and the price of this car is {highest_price}")

cheap_car, lowest_price = min_price_of_car(cars)
print(f"The most cheapest  car is {cheap_car} and the price of this car is {lowest_price}")












