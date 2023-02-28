def sum_of_digits(number):
    number = list(number)
    sum = 0
    loop = len(number)
    while loop > 0:
        for i in number:
            i = int(i)
            sum += i
        return sum


def condition():
    list_of_nr = []
    for i in range(100, 201):
        if sum_of_digits(str(i)) % 2 == 0:
            list_of_nr.append(i)
    return list_of_nr


if __name__ == '__main__':
    print(condition())