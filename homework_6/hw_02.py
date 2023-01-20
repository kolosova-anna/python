# Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]

n = int(input('Введите число > 20:'))
def list_20_21 (num):
    new_list = []
    if n > 20:
        new_list = [i for i in range (20, n + 1) if (i % 20 == 0 or i % 21 == 0)]
    else:
        print ('Введено значение < 20')
    return new_list

print (list_20_21(n))