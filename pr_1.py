my_dict = {
    1: 1,
    2: 2,
    3: 3,
    'home': 'car'
}


def print_all_items_from_dict(dict):
    for k, v in dict.items():
        print(k, v)


print_all_items_from_dict(my_dict)
