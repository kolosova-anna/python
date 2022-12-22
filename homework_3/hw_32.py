# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample
num = int(input('Введите количество элементов: '))
new_list = sample (range (1, num * 2), num)
print(new_list)

def product_of_numbers (num_list):
    new_numbers = []
    for i in range (len(num_list) // 2):
        new_numbers.append (num_list[i] * num_list[-1 - i])
    if len(num_list) % 2 != 0:
        new_numbers.append (num_list[len(num_list) // 2])
        return new_numbers
    else:
        return new_numbers
    
new_num_list = product_of_numbers (new_list)
print (new_num_list)