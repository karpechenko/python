
__author__ = 'Карпеченко Владимир Сергеевич'

# Задача-1: Дано произвольное целое число (число заранее неизвестно).
# Вывести поочередно цифры исходного числа (порядок вывода цифр неважен).
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании решите задачу с применением цикла for.

# Вариант 1:

a = int(input('Введите целое число: '))
i = 1
b = 1

while int(b) != 0:
    b = a / (10**i)
    i += 1
    
i = i - 2
b = 10**i

while a != 0:   
    c = int(a / b)
    print(c)
    a = a - b * c
    b = b / 10

# Вариант 2:

a = int(input('Введите целое число: '))

while a != 0:
    b = a / 10
    a = int(b)
    b = int(round((b - a), 1) * 10)
    print(b)


# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную 
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

a = int(input('Введите значение А: '))
print('A = ', a)
b = int(input('Введите значение В: '))
print('B = ', b)

answer = input('Заменить значения А и В местами - Enter')
c = a
a = b
b = c
print('A = ', a)
print('B = ', b)


# Задача-3: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользование данным ресурсом только с 18 лет"

user_age = int(input('Укажите Ваш возраст: '))
access_age = 18

if user_age >= access_age:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')
