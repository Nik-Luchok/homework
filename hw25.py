"""

Write season() function, takes as an argument the month number
1-12, gives back the name of the season(summer, winter, autumn, spring) as a string

"""


def main():
    # take an input from the user
    month = input("Provide a Month number: ")

    # validate data
    try:
        month = int(month)

        if not 1 <= month <= 12:
            raise ValueError
    except ValueError:
        print("Give a valid int value from 1 to 12")
        return

    # print the result
    print(season(month))


def season(month: int):
    if month <= 2 or month == 12:
        return "Winter"
    elif month <= 5:
        return "Spring"
    elif month <= 8:
        return "Summer"
    else:
        return "Autumn"


if __name__ == "__main__":
    main()
