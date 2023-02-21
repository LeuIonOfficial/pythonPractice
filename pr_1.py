def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False


year = 2024

if leap_year(year):
    print(year, 'is a leap year')
else:
    print(year, 'isnt a leap year')
