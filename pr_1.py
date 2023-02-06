import math


def is_number_even_or_not():
    number = float(input("number: "))
    if number % 2 == 0:
        return f"number {number} is even!"
    else:
        return f"number {number} is odd"


# (30°C x 1.8) + 32 = 86°F
def centigrade_to_fahrenheit(centigrade: float):
    fahrenheit = (centigrade * 1.8) + 32
    return f'{float(fahrenheit):.2f}'


def get_area_of_triangle(a: int, b: int, c: int):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


def get_average_of_set_of_int(set_of_int):
    sum = 0
    for el in range(len(set_of_int)):
        sum += el
    return sum / len(set_of_int)


def get_product_of_set_of_int(set_of_int):
    product = 1
    for el in set_of_int:
        product = el * product
    return product


def get_circle_info_given_radius(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * radius * radius
    return circumference, area


def is_multiply_with_5():
    number = float(input("number: "))
    if number % 5 == 0:
        return True
    else:
        return False


def is_multiply_with_5_and_7():
    number = float(input("number: "))
    if number % 5 == 0 and number % 7 == 0:
        return f'{number} is multiply with 5 and 7'
    else:
        return f"{number} isn't multiply with 5 and 7"


def get_average_of_10():
    list_of_numbers = []
    total = 0
    loop = 0
    while loop < 10:
        number = float(input(f'Loop {loop}/9 number: '))
        list_of_numbers.append(number)
        total += number
        loop += 1
    return list_of_numbers, total


def get_reversed_integer():
    number = input("number: ")
    reversed_number = number[::-1]
    return int(reversed_number)


def get_geometric_mean():
    numbers = [int(x) for x in input("Enter n numbers separated by spaces: ").split()]
    given_numbers = len(numbers)
    product = 1

    for i in numbers:
        product *= i

    geometric_mean = product ** (1 / given_numbers)

    return geometric_mean


def sum_of_digits():
    number = list(input())
    sum = 0
    loop = len(number)
    print(loop)
    while loop > 0:
        for i in number:
            i = int(i)
            sum += i 
        return sum 

if __name__ == "__main__":
    print(sum_of_digits())
