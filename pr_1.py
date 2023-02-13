def get_product_of_set_of_int(set_of_int):
    product = 1
    for el in set_of_int:
        product = el * product
    return product


a = [4, 5, 6, 7, 8, 9, 10]

print(get_product_of_set_of_int(a))
