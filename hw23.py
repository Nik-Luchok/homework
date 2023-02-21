"""

Given the length of a square, return a tuple(Perimeter, area, diagonal)

"""
# import math module
from math import sqrt


def main():

    # promt the user of an input
    while True:
        try:
            square_side = int(input("Square side length: "))
            break
        except ValueError:
            continue

    # call our function
    perimeter, area, diagonal = square(square_side)

    # print results
    print("Perimeter: ", perimeter)
    print("Area: ", area)
    print("Diagonal: ", diagonal)


def square(square_side):
    # preimeter
    perimeter = square_side * 4

    # area
    area = square_side ** 2

    # diagonal
    diagonal = sqrt(2) * square_side

    # return a tuple
    return (perimeter, area, diagonal)


if __name__ == "__main__":
    main()
