def get_area_of_triangle(a: int, b: int, c: int):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return f'Circle area {float(area):.2f} with parameters {a,b,c}'


if __name__ == "__main__":
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    print(get_area_of_triangle(a,b,c))
