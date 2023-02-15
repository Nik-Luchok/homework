"""
Написать программу определяющую високосный год.
Пользователь вводит номер года, программа должна
ответить високосный это год или нет.

Из википедии:
год, номер которого кратен 400, — високосный;
остальные годы, номер которых кратен 100, — невисокосные
(например, годы 1700, 1800, 1900, 2100, 2200, 2300);
остальные годы, номер которых кратен 4, — високосные[5];
все остальные годы — невисокосные.

"""
# take input from the user
year = input("Provide a year: ")

try:
    year = int(year)
    if (year % 4) == 0:
        if (year % 400) == 0:
            print("This is the Leap year")
        elif (year % 100) == 0:
            print("This is not the Leap year")
        else:
            print("This is the Leap year")
    else:
        print("This is not the Leap year")
except (ValueError, TypeError):
    print("Please provide a valid year number")
