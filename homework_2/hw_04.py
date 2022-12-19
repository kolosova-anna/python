# Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

num_list = []
n = int (input ('Enter the value of N: '))
for i in range (0, n*2 + 1):
    num_list.append (-n + i)
print (num_list)

i = int (input ('Position one: '))
j = int (input ('Position two: '))
if 0 < i <= (n*2 +1) and 0 < j <= (n*2 + 1):
    product = num_list[i-1] * num_list[j-1]
    print(product)
else:
    print('There is no position')