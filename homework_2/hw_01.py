#  Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

num = input('Введите число: ')
m = len(num)
num = float(num)
num *= 10 ** (int(m)- 2)
num = int(num)

if num < 0:
    num = num * -1

sum = 0

while num >= 10:
    sum = sum + num % 10
    num = num // 10

sum = sum + num

print(sum)