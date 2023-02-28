def check_prime(nr):
    if nr < 2:
        return False
    for i in range(2, int(nr ** 0.5) + 1):
        if nr % i == 0:
            return False
    return True


def generate_prime_numbers(b):
    list_of_nr = []
    for i in range(1, b + 1):
        if check_prime(i):
            list_of_nr.append(i)
    return list_of_nr


if __name__ == '__main__':
    print(generate_prime_numbers(19))
