# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Негафибоначчи
# in
# 8
# out
# -21 13 -8 5 -3 2 -1 1 0 1 1 2 3 5 8 13 21
# in
# 5
# out
# 5 -3 2 -1 1 0 1 1 2 3 5

num = int (input ('Введите число: '))

def negafibonacci (n):
    fib_list = []
    fib_list = [0] * (2 * n + 1)
    k = n * 2 + 1
    fib_list [n + 1] = 1
    fib_list [n - 1] = 1
    i = n + 2
    if n % 2 != 0:
        while i < k:
            if i % 2 != 0:
                fib_list [i] = fib_list [i - 1] + fib_list [i - 2]
                fib_list [n - 2] = fib_list [i] * -1
                i += 1
                n -= 1
            else:
                fib_list [i] = fib_list [i - 1] + fib_list [i - 2]
                fib_list [n - 2] = fib_list [i]
                i += 1
                n -= 1
    else:
        while i < k:
            if i % 2 != 0:
                fib_list [i] = fib_list [i - 1] + fib_list [i - 2]
                fib_list [n - 2] = fib_list [i]
                i += 1
                n -= 1
            else:
                fib_list [i] = fib_list [i - 1] + fib_list [i - 2]
                fib_list [n - 2] = fib_list [i] * -1
                i += 1
                n -= 1
    return fib_list

negafibonacci_list = negafibonacci (num)
print (negafibonacci_list)