# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]

from random import randint

def num_list (n):
    new_list =[]
    for i in range (0, n):
        new_list.append (randint (1, 10))
    return new_list

def check_nums (new_list):
    unique_nums = []
    for i in range (len(new_list)):
        for j in range (len(new_list)):
            if new_list[i] == new_list[j] and i != j:
                break
        else:
            unique_nums.append (new_list[i])
    return unique_nums

    
num = int(input('Введите количество элементов: '))

if num > 0:
    num_list = num_list (num)
else:
    print ('Количество элементов должно быть больше 0')
print(num_list)

unique_nums_list = check_nums (num_list)
print (unique_nums_list)
