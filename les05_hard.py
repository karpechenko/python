# coding: UTF-8

import os
import sys
import easy

print('--------------------')
print('Путь - ', sys.argv)
print('--------------------')

do = {'help':easy.print_help,
      'lstdir':easy.list_cur_dir,
      'crdir':easy.create_dir,
      'rmdir':easy.rem_dir,
      'cp':easy.copy_file,
      'rm':easy.rem_file,
      'cd':easy.change_dir,
      'ls':easy.full_path
      }

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print('Задан неверный ключ')
        print('задайте ключ help для получения справки')


# Не разобрался с переходом в папку по относительному пути.
# Функция перехода не доделана
