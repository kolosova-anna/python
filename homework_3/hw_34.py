# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76
# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

from random import random
number = int (input('Введите количество элементов: '))

def find_difference (num):
    new_list = []
    for i in range (num):
        new_list.append (round ((random() * 10), 2))
    print(new_list)

    num_min = new_list[0]
    num_max = new_list[0]
    i = 1
    while i < len(new_list):
        if new_list[i] < num_min:
            num_min = new_list[i]
        i += 1
    print ('min =', (num_min))

    i = 1
    while i < len(new_list):
        if new_list[i] > num_max:
            num_max = new_list[i]
        i += 1
    print ('max =', (num_max))

    num_1 = round (num_min - int(num_min), 2)
    num_2 = round (num_max - int(num_max), 2)
    resalt = round ((num_2 - num_1), 2)

    print ('differense =', (resalt))


find_difference (number)