#  Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
# in
# 11
# out
# 1011

number = int (input ('Введите десятичное число: '))

def from_decimal_to_binary (num):
    new_num = []
    while num:
        new_num.append (num % 2)
        num = num // 2 
    bin_num = 0
    i = len(new_num) - 1
    while i >= 0:
        bin_num = bin_num * 10 + new_num[i]
        i -= 1
    return bin_num

binary_num = from_decimal_to_binary (number)
print (binary_num)