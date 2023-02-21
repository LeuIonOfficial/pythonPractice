def fibonacci_series(x):
    num1, num2 = 0, 1
    for i in range(x):
        print(num1)
        num1, num2 = num2, num1 + num2


x = int(input("How many iterations: "))
fibonacci_series(x)
