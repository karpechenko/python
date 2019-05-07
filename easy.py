# coding: UTF-8

import os
import sys
from shutil import rmtree
from shutil import copy

def print_help():
    print('--------------------')
    print('help - получить справку')
    print('lstdir - Просмотреть содержимое текущей директории')
    print('crdir - Создать директорию')
    print('rmdir - Удалить директорию')
    print('cp - копировать файл. Имя файла указать вторым параметром')
    print('rm - удалить файл. Имя файла указать вторым параметром')
    print('ls - показать полный путь к текущей директории')
    print('cd - сменить текущую директорию. Указать путь к директории вторым параметром')
    print('-------------------')

def ch_dir():
    try:
        path = input('Ввведите полный путь до желаемой директории:')
        os.chdir(path)
        if path == os.getcwd():
            print('Текущая директория успешно изменена -', os.getcwd())
    except FileNotFoundError:
        print('Невозможно перейти')
        print('Путь указан неверно')

def list_cur_dir():
    print(os.listdir(os.getcwd()))

def create_dir():
    try:
        dir_name = input('Задайте имя директории:')
        os.mkdir(dir_name)
        print('Директория {} создана'.format(dir_name))
        print(os.getcwd() + '/' + dir_name)
    except FileExistsError:
        print('Невозможно создать директорию')
        print('Директория {} уже существует'.format(dir_name))
        print(os.getcwd() + '/' + dir_name)

def rem_dir():
    try:
        dir_name = input('Введите имя директории, которую желаете удалить:')
        path = (os.getcwd() + '/' + dir_name)
        rmtree(path)
        if not os.path.exists(path):
            print('Директрория {} удалена'.format(dir_name))
    except FileNotFoundError:
        print('Невозможно удалить')
        print('Директория с именем {} отсутствует'.format(dir_name))

def copy_file():
    try:
        file_name = sys.argv[2]
    except IndexError:
        file_name = None
    if not file_name:
        print('Не удалось скопировать файл')
        print('Вторым параметром необходимо указать имя файла')
    else:
        try:
            name = os.getcwd() + '/' + file_name
            newfile = os.path.splitext(name)[0] + '_copy' + os.path.splitext(name)[1]
            copy(name, newfile)
            if os.path.exists(newfile):
                print('Файл {} был успешно создан'.format(new_file))
        except FileNotFoundError:
            print('Не удалось удалить файл')
            print('В текущей директории файла с таким именем не существует')

def rem_file():
    try:
        file_name = sys.argv[2]
    except IndexError:
        file_name = None
    if not file_name:
        print('Не удалось удалить файл')
        print('Вторым параметром необходимо указать имя файла')
    path = os.path.join(os.getcwd(), file_name)
    try:
        answer = input('Вы уверены, что хотите удалить {} Y/N ?'.format(file_name))
        if answer == 'y':
            os.remove(path)
            if not os.path.exists(path):
                    print('Файл {} был успешно удален'.format(file_name))
        elif answer == 'n':
            print('Удаление {} отменено'.format(file_name))
        else:
            print('Неверный ввод подтверждения')
            print('Удаление {} отменено'.format(file_name))
    except FileNotFoundError:
            print('Не удалось удалить файл')
            print('В текущей директории файла с таким именем не существует')

def full_path():
    print('Полный путь - ', os.getcwd())

def change_dir():
    try:
        path = sys.argv[2]
    except IndexError:
        path = None
    if not path:
        print('Не удалось перейти')
        print('Необходимо указать путь к желаемой директории вторым параметром')
    try:
        os.chdir(path)
        if path == os.getcwd():
            print('Текущая директория успешно изменена -', os.getcwd())
    except FileNotFoundError:
        print('Невозможно перейти')
        print('Директория указана неверно')
    

