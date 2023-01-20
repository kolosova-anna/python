# Представлен список чисел.
# Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

from random import sample

len_list = int(input('Введите длину списка:'))

my_list = sample(range(1, len_list * 2), len_list)
my_new_list = [my_list[i] for i in range (1, len_list) if my_list[i] > my_list[i -1]]
print (my_list)
print (my_new_list)

