"""
find the biggest powwer of 2, that don't exceed given number

"""
# take user input
number = input("Positive integer: ")
base_number = 2
degree = 0
result = 1

# validate user data
if not number.isdigit():
    print("Please give valid positive integer")
    exit()

number = int(number)
if number == 0:
    print("Please give positive integer other than 0")
    exit()
# print number
print(number, end="\t")

# calculate max degree of 2 befor exceeding given number

while (result * base_number) <= number:
    result = result * base_number
    degree += 1

# print results
print(f"{degree} {result}", end="\t")
print(f"{base_number} ** {degree} = {result}")
