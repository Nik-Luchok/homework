"""

Write is_year_leap() function

"""


def main():
    # take input from the user
    year = input("Provide a year: ")

    # validate data
    try:
        year = int(year)
    except (ValueError, TypeError):
        print("Please provide a valid year number")
        return

    # call the function, print an answer
    if is_year_leap(year):
        print("This is the Leap year")
    else:
        print("This is not the Leap year")


def is_year_leap(year):
    if (year % 4) == 0:
        if (year % 400) == 0:
            return True
        elif (year % 100) == 0:
            return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    main()
