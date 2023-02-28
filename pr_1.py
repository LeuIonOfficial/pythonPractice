def get_geometric_mean(numbers):
    given_numbers = len(numbers)
    product = 1

    for i in numbers:
        product *= i

    geometric_mean = product ** (1 / given_numbers)

    return geometric_mean


if __name__ == '__main__':
    nr = [int(x) for x in input("Enter n numbers separated by spaces: ").split()]
    print(get_geometric_mean(nr))