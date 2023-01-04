# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# in
# 54
# out
# [2, 3, 3, 3]


def simple_denominators (n):
    new_list = []
    digit = n
    i = 2
    while i <= digit:
        if digit % i == 0:
            new_list.append (i)
            digit //= i
        else:
            i+=1

    return new_list

num = int(input('Введите число: '))
denominators_list = simple_denominators (num)
print (denominators_list)         