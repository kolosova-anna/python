# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22
# in
# 4
# out
# [4, 2, 4, 9]
# 8

from random import sample
num = int(input('Введите количество элементов: '))
new_list = sample (range (1, num * 2), num)
print(new_list)

def sum_elem (list_1):
    sum_numbers = 0
    i = 0
    while i < len(list_1):
        sum_numbers += list_1[i]
        i += 2
    return sum_numbers

print('Сумма элементов нечетных позиций = ', sum_elem(new_list))