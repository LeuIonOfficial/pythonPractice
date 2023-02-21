def add(x, y):
    return x + y


def substract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


while True:

    print("""
  1: for add,
  2: for substract,
  3: for multiply,
  4: for divide  
  """)

    option = int(input("Option: "))

    num1 = float(input("Num 1: "))
    num2 = float(input("Num 2: "))

    if option == 1:
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result:.2f}")
    elif option == 2:
        result = substract(num1, num2)
        print(f"{num1} - {num2} = {result:.2f}")
    elif option == 3:
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result:.2f}")
    elif option == 4:
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result:.2f}")
    else:
        continue
