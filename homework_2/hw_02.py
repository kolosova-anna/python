# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N в виде списка.
# 1 - 1 * 1, 2 - 1 * 2, 3 - 1 * 2 * 3, 4 - 1 * 2 * 3 * 4 и т.д.
# - 4 -> [1, 2, 6, 24]
# - 6 -> [1, 2, 6, 24, 120, 720]

n = int(input('Введите натуральное число: '))
num = 1
print(num, end = ' ')
for k in range (2, n + 1):
    num = num * k
    k += 1
    print(num, end = ' ')
