# print this figure. user inputs height
#   A         *
#           * * *
#         * * * * *
#       * * * * * * *
#     * * * * * * * * *
#   * * * * * * * * * * *
# * * * * * * * * * * * * *
#   *                   * 
#     *               *
#       *           *
#         *       *
#           *   *
#             *


# collecting user input
rows = input("Height of the pyramid: ")

# validate user data
try:
    rows = int(rows)

    if rows < 1:
        raise ValueError
except ValueError:
    print("Provide valid integer value")
    exit()

# print the top part
for row in range(rows):
    # print the first pyramid
    # print white space
    for cell in range(rows - (row + 1)):
        print("  ", end="")

    # print stars
    for cell in range(row + 1):
        print("*", end=" ")

    # print the second pyramid, which height is lower by 1
    for cell in range(row):
        print("*", end=" ")

    # print newline
    print()

# print the bottom part
for row in range(1, rows):
    # print the first pyramid
    # print white space
    for cell in range(row):
        print("  ", end="")

    # print stars
    print("*", end=" ")

    # print white space
    for cell in range(rows - (row + 1)):
        print("  ", end="")

    # print the second pyramid, which height is lower by 1
    # print white space
    for cell in range(rows - (row + 1) - 1):
        print("  ", end="")

    # print star
    if row != rows - 1:
        print("*", end=" ")

    # print newline
    print()