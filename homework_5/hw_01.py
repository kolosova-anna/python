# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

from random import sample

count = int(input('Введите количество слов:'))
if count >= 1:
    word = 'abc'
    words_list = ["".join(sample (word, k= 3)) for i in range (count)]
    print (*words_list, sep=" ")
    
    res = list(filter(lambda i: i != 'abc', words_list))
    print(*res, sep=" ")
else:
    print("Введено некорректное значение")
