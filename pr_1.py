def get_reversed_integer(number):

    reversed_number = number[::-1]
    return int(reversed_number)


if __name__ == '__main__':
    nr = input("number: ")
    print(get_reversed_integer(nr))