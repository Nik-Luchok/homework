"""
8_|_|_|_|_|_|_|_|_|
7_|_|_|_|_|_|_|_|_|
6_|_|_|*|_|*|_|_|_|
5_|_|*|_|_|_|*|_|_|
4_|_|_|_|*|_|_|_|_|
3_|_|*|_|_|_|*|_|_|
2_|_|_|*|_|*|_|_|_|
1_|_|_|_|_|_|_|_|_|
   a b c d e f g h
Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом
направлении и на одну клетку по горизонтали,
или наоборот. Даны две различные клетки шахматной доски, определите, может ли
конь попасть с первой клетки на вторую одним ходом.

Понадобится оператор if, and, or, возможно пригодится функция abs(),
но не обязательно.
"""
# declare 2 dicts and a list
pos_current_dict = {}
pos_desired_dict = {}

# take input from user - 1.chess figure position and 2. where he wants to go
# DATA example: g5 or G5. others aren't acceptable
while True:
    pos_current = input("Current Knight's position (A6, B3..): ")

    # validate data
    if len(pos_current) != 2:
        print("Input must be: A6, B8, H3...")
        continue

    if not pos_current[0].isalpha():
        print("Input must be: A6, B8, H3...")
        continue
    if not pos_current[1].isnumeric():
        print("Input must be: A6, B8, H3...")
        continue

    # convert data for later and validate whether values are in range 1-8 A-H
    pos_current = pos_current.upper()
    pos_current_dict["char"] = ord(pos_current[0])
    if pos_current_dict["char"] > ord("H"):
        print("Letter must be from A to H")
        continue

    pos_current_dict["num"] = int(pos_current[1])
    if pos_current_dict["num"] < 1 or pos_current_dict["num"] > 8:
        print("Number must be from 1 to 8")
        continue

    # if all good break the loop
    break

while True:
    pos_desired = input("Desired Knight's position (A6, B3..): ")

    # validate data
    if len(pos_desired) != 2:
        print("Input must be: A6, B8, H3...")
        continue

    if not pos_desired[0].isalpha():
        print("Input must be: A6, B8, H3...")
        continue
    if not pos_desired[1].isnumeric():
        print("Input must be: A6, B8, H3...")
        continue

    # convert data for later and validate whether values are in range 1-8 A-H
    pos_desired = pos_desired.upper()
    pos_desired_dict["char"] = ord(pos_desired[0])
    if pos_desired_dict["char"] > ord("H"):
        print("Letter must be from A to H")
        continue

    pos_desired_dict["num"] = int(pos_desired[1])
    if pos_desired_dict["num"] < 1 or pos_desired_dict["num"] > 8:
        print("Number must be from 1 to 8")
        continue

    # if all good break the loop
    break


# check if desired position attainable
"""
                            Logic explanation
 Knigt goes on 2 positions straigt (along number axis or letter axis) and on
 1 position to the side (opposite axis). So there are 2 cirkumstances wee
 need to check to see if the desired position attainable by the knight.
"""

a = abs(pos_desired_dict["char"] - pos_current_dict["char"])
b = abs(pos_desired_dict["num"] - pos_current_dict["num"])

if (a == 2 and b == 1) or (a == 1 and b == 2):
    print("You can make such move")
else:
    print("You can not make such move")
