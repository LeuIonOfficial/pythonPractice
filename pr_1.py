x = int(input('Nth term: '))

num1, num2 = 0, 1

list_of_fibonacci_numbers = [num1, num2]

for i in range(x - 1):
    result = num1 + num2
    num1, num2 = num2, result
    list_of_fibonacci_numbers.append(result)

print(list_of_fibonacci_numbers[-1])
