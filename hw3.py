"""
В школе решили набрать три новых математических класса.
Так как занятия по математике у них проходят в одно и то же время,
было решено выделить кабинет для каждого класса и купить в них новые парты.
За каждой партой может сидеть не больше двух учеников. Известно количество
учащихся в каждом из трёх классов. Сколько всего нужно закупить парт чтобы
их хватило на всех учеников? Программа получает на вход три натуральных числа:
количество учащихся в каждом из трех классов.

Использовать только арифметические операторы. (Подсказка: понадобятся // + и %)
"""
# global variable tables
tables = 0

# Promt user for the input
for class_num in range(3):
    while True:
        try:
            students = input(f"Students in {class_num + 1} class: ")

            # validate data
            students = int(students)
            if students < 0:
                print("Provide a positive value")
                continue

            # calculate the number of tables needed
            tables = tables + students // 2

            if students % 2 != 0:
                tables += 1
            break
        except ValueError:
            print("The number must be integer")

# print the result
print(tables)
