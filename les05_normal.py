# coding: UTF-8

import os
import sys
import easy

print('--------------------')
print('Путь - ', sys.argv)
print('--------------------')
answer = input('Начать работу с директориями? Y/N :')
while answer != 'n':
    if answer == 'y':    
        print('Вы можете выполнить следующие действия:')
        print('[1] - Сменить текущую директорию')
        print('[2] - Просмотреть содержимое текущей директории')
        print('[3] - Создать директорию')
        print('[4] - Удалить директорию')
        print('-------------------')

        do = {'1':easy.ch_dir,
              '2':easy.list_cur_dir,
              '3':easy.create_dir,
              '4':easy.rem_dir
              }

        try:
            key = input('Введите номер желаемого действия:')
        except IndexError:
            key = None

        if key:
            if do.get(key):
                do[key]()
            else:
                print('Задан неверный ключ')
                print('Повторите, задав верный ключ')
                
        answer = input('Продолжить Y/N ?')
        
    elif answer == 'n':
        print('Работа завершена')
        
    else:
        print('неизвестная команда')
        break
