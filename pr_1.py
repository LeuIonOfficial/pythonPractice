import math


def get_circle_info_given_radius(radius):
    circumference = 2 * math.pi * radius
    area = math.pi * radius * radius
    return f"{float(circumference):.2f}, {float(area):.2f}"


radius = int(input('Radius: '))

print(get_circle_info_given_radius(radius))
