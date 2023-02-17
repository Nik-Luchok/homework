
# print this figure. user inputs height
#   A         *
#           *   *
#         *       *
#       *           *
#     *               *
#   *                   *
# * * * * * * * * * * * * *


rows = input("Height: ")
try:
    rows = int(rows)
    if rows < 1:
        raise ValueError
except ValueError:
    print("Provide valid integer value")
    exit()

# print the pyramid
for row in range(rows - 1):
    # for each row
    # print first part of the pyramid
    for cell in range(rows - (row + 1)):
        print(" ", end=" ")
    print(" *", end="")

    # the whitespace between pyramids
    for cell in range(row - 1):
        print(" ", end=" ")

    # print second pyramid
    for cell in range(row):
        print(" ", end=" ")

        if cell == row - 1:
            print(" *", end="")

    # print new line
    print()

# print the last line of the pyramid
for row in range(rows*2 - 1):
    print(" *", end="")

print()
