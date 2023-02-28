def is_multiply_with_5(number):
    if number % 5 == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    nr = float(input("number: "))
    print(is_multiply_with_5(nr))
