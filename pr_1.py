def get_average_of_10():
    list_of_numbers = []
    total = 0
    loop = 1
    while loop < 11:
        number = float(input(f'Loop {loop}/10 number: '))
        list_of_numbers.append(number)
        total += number
        loop += 1
    return f'list of your number: {list_of_numbers} \n' \
           f'Total: {total} \n' \
           f'Average: {total / len(list_of_numbers)}'


if __name__ == '__main__':
    print(get_average_of_10())
