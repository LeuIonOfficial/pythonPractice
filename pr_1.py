def post_nr_in_list(my_list):
    x = int(input('Index of place: '))
    nr = int(input('NR you want to place: '))
    my_list[x] = nr
    return my_list


if __name__ == '__main__':
    new_list = [4, 2, 4, 5, 6, 7, 8, 91]
    print(post_nr_in_list(new_list))
