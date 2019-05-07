# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# coding: UTF-8

import os
import sys

print('---------------------')
print('path - ', sys.argv)

def print_help():
    print('---------------------')
    print('help - справка')
    print('mkdirs - cоздать папки dir_1-dir_9 в текущей директории')
    print('remdirs - удалить папки dir_1 -dir_9 из текущей директории')
    print('---------------------')

def make_dirs():
    i = 1
    while i != 10:
        try:
            dir_name = 'dir_{}'.format(i)
            os.mkdir(dir_name)
            print('Директория {} создана'.format(dir_name))
        except FileExistsError:
            print('Директория {} уже существует'.format(dir_name))
        i += 1

def rem_dirs():
    i = 1
    while i != 10:
        try:
            dir_name = 'dir_{}'.format(i)
            os.rmdir(dir_name)
            print('Директория {} удалена'.format(dir_name))
        except FileNotFoundError:
            print('Директории {} не существует'.format(dir_name))
        except OSError:
            print('Директория {} содержит файлы или папки'.format(dir_name))
            print('Очистите директорию {} и повторите удаление'.format(dir_name))
        i += 1

do = {'help':print_help,
     'mkdirs':make_dirs,
     'remdirs':rem_dirs
     }

try:
    key = sys.argv[1]
except:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print('Задан неверный ключ')
        print('Укажите ключ help для получения справки')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# coding: UTF-8

import os
import sys

print('---------------------')
print('path - ', sys.argv)

def print_help():
    print('---------------------')
    print('help - справка')
    print('lstdir - отобразить файлы и папки текущей директории')
    print('---------------------')
    
def list_cur_dir():
    print(os.listdir('.'))

do = {'help':print_help,
     'lstdir':list_cur_dir,
     }

try:
    key = sys.argv[1]
except:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print('Задан неверный ключ')
        print('Укажите ключ help для получения справки')


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

# coding: UTF-8

import os
import sys
from shutil import copy

print('---------------------')
print('path - ', sys.argv)

def print_help():
    print('---------------------')
    print('help - справка')
    print('cpfile - создать копию исполняемого файла')
    print('---------------------')
    
def launch_file_copy():
    full_name = os.path.basename(sys.argv[0])
    name = os.path.splitext(full_name)[0]
    newfile = name + '_copy.py'
    copy(sys.argv[0], newfile)
    if os.path.exists(newfile):
        print('Файл', newfile, 'был успешно создан')

do = {'help':print_help,
     'cpfile':launch_file_copy,
     }

try:
    key = sys.argv[1]
except:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print('Задан неверный ключ')
        print('Укажите ключ help для получения справки')
