"""
Программа запрашивает ввод, с клавиатуры, целых чисел, пока не будет введён 0.
Как только пользователь введёт 0 (ноль), программа должна посчитать и вывести
на экран следующие результаты (без учёта последнего 0):
• количество введённых чисел 
• их сумму
• среднее арифметическое всех введённых чисел 
• максимальное и минимальное значение 
• количество чётных и не чётных значений

"""


def main():
    # take input from the user in the loop
    number = user_input()

    # declare variables
    total = 0
    number_sum = 0
    mean = 0
    number_max = number
    number_min = number
    even = 0
    odd = 0

    # check input and loop fro more input
    while number != 0:
        # calculate total number of inputs
        total += 1

        # sum
        number_sum += number

        # calculate Arithmetic mean
        mean = number_sum / total

        # max and min value
        if number > number_max:
            number_max = number

        if number < number_min:
            number_min = number

        # quantity of even and odd values
        if number % 2 == 0:
            even += 1
        else:
            odd += 1

        # promt for an input
        number = user_input()

    # print total, mean, max, min, odd and even quantity
    print(f"Total number of inputs: {total}")
    print(f"Sum: {number_sum}")
    print(f"Arithmetic mean: {mean}")
    print(f"Max: {number_max} Min: {number_min}")
    print(f"Even numbers: {even}, Odd numbers: {odd}")


def user_input():
    # promts the user for an integer input, converts it to an int and returns
    while True:
        number = input("Provide integer: ")
        try:
            number = int(number)
            return number
        except ValueError:
            print("Provide valid integer")
            continue


if __name__ == "__main__":
    main()