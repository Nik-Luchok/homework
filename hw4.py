"""
Дано целое, положительное, ТРЁХЗНАЧНОЕ число. Например: 123, 867, 374.
Необходимо его перевернуть. Например, если ввели число 123, то должно
получиться на выходе ЧИСЛО 321. ВАЖНО! Работать только счислами.
Строки, оператор IF и циклы использовать НЕЛЬЗЯ!

На выходе ОБЯЗАТЕЛЬНО должно быть ЧИСЛО!!!
"""


def main():
    # take user input
    while True:
        number = input("3 digit Number: ")
        try:
            number = int(number)

            if number < 100 or number > 999:
                print("Number must be 3 digit")
                continue
            break
        except ValueError:
            print("Number must be an integer")

    # reverse without for loop (stupid)
    digit = number % 10
    new_number = digit * 100

    number = number // 10

    digit = number % 10
    new_number += digit * 10

    number = number // 10

    digit = number % 10
    new_number += digit * 1

    print(new_number)


if __name__ == "__main__":
    main()
