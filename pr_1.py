def check_prime(nr):
    if nr < 2:
        return False
    for i in range(2, int(nr ** 0.5) + 1):
        if nr % i == 0:
            return False
    return True


if __name__ == '__main__':
    number = int(input("Number you want to check: "))
    if check_prime(number):
        print(f'{number} is a prime number')
    else:
        print(f'{number} is not a prime number')
