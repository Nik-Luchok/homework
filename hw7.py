"""
From given positive integer print all squares(^2) of positive integers
which do not exceed the given number
eg:
i = 50,  1, 4, 9, 16, 25, 36, 49
"""

# take input from the user
i = input("Positive integer: ")

# validate data
if not i.isdigit():
    print("provide positive integer")

# print i
print(i, "\t")

# convert str to an int
i = int(i)

# initialize
square = i

while square < i:
    print
