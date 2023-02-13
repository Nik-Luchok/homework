# First Homework
"""n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
 Сколько яблок достанется каждому школьнику? 
Сколько яблок останется в корзинке? 
Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).
"""

# Promt the user for the number of apples given, and the number of kids, convert to ints
while True:
    apples = input("Apples: ")
    # validate data
    # try a code snippet, if raised an error - tell the user
    try:
        # convert to an int, raise ValueError if str isnt convertable to an int
        apples = int(apples)

        # check if positive
        if apples < 0:
            print("Number must be a positive integer! 0, 1, 2, 3...")
            continue

        # if everything is okay, continue the programm, thus break the loop
        break
    except ValueError:
        print("Error, please provide an int")

# promt for the number of kids
while True:
    kids = input("Kids: ")
    # validate data
    # try a code snippet, if raised an error - tell the user
    try:
        # convert to an int, raise ValueError if str isnt convertable to an int
        kids = int(kids)

        # check if positive
        if kids < 0:
            print("Number must be a positive integer! 0, 1, 2, 3...")
            continue

        # if everything is okay, continue the programm, thus break the loop
        break
    except ValueError:
        print("Error, please provide an int")

# calculate number of apples each kid has and the leftover
print(f"Each kid has: {apples // kids} number of apples")
print(f"Apples left in basket: {apples % kids}")


