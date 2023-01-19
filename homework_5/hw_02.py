# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ

# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ

# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

from os import path
from itertools import groupby
from itertools import starmap

def encoding (text = 'text_words.txt', code = 'code_words.txt'):
    if path.exists(text):
        with open (text, 'r') as file_1, \
                open (code, 'w') as file_2:
            for i in file_1:
                file_2.write (''.join([f'{len(list(v))}{ch}' for ch, v in groupby(i)]))
    else:
        print('Такого файла не существует')


def decoding (code = 'code_words.txt'):
    if path.exists(code):
        with open (code, 'r') as file_1:
            t = ''
            for i in file_1:
                letters = []
                for j in i.strip():
                    if j.isdigit():
                        t += j
                    else:
                        letters.append([int(t),j])
                        t = ''
                print(''.join(starmap(lambda x, y: x * y, letters)))
            print (letters)
    else:
        print('Такого файла не существует')

encoding ()
decoding ()
