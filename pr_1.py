def get_area_of_triangle(a: int, b: int, c: int):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return f"Area of Triangle with parameters {a,b,c} is {float(area):.2f}"


a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

print(get_area_of_triangle(a,b,c))