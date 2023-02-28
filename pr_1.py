def is_multiply_of_5_and_7(number):
    if number % 5 == 0 and number % 7 == 0:
        return f'{number} is multiply of 5 and 7'
    else:
        return f"{number} isn't multiply of 5 and 7"


if __name__ == '__main__':
    nr = float(input("number: "))
    print(is_multiply_of_5_and_7(nr))
