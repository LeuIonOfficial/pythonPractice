def sum_of_digits(number):
    sum = 0
    loop = len(number)
    while loop > 0:
        for i in number:
            i = int(i)
            sum += i
        return sum


if __name__ == '__main__':
    nr = list(input('numbers: ').split())
    print(sum_of_digits(nr))