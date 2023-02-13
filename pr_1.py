
# (30°C x 1.8) + 32 = 86°F
def centigrade_to_fahrenheit():
    centigrade = float(input("Centigrade's: "))
    fahrenheit = (centigrade * 1.8) + 32
    return f'{float(fahrenheit):.2f} Fahrenheit'


if __name__ == "__main__":
    print(centigrade_to_fahrenheit())