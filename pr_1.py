def multiples_3_range_10_50():
    list_of_nr = []
    for i in range(10, 51):
        if i % 3 == 0:
            list_of_nr.append(i)
    return list_of_nr


if __name__ == '__main__':
    print(multiples_3_range_10_50())
