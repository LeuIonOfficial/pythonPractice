def get_average_of_set_of_int(set_of_int):
    sum = 0
    for el in range(len(set_of_int)):
        sum += el
    return sum / len(set_of_int)


a = [4, 5, 6, 7, 2, 1, 4, 5]

print(get_average_of_set_of_int(a))
