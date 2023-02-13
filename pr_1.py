def is_number_even_or_not():
    number = float(input("number: "))
    if number % 2 == 0:
        return f"number {number} is even!"
    else:
        return f"number {number} is odd"


if __name__ == "__main__":
    print(is_number_even_or_not())
