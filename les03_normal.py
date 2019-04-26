# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


# В решении есть недочет. Первый и второй элементы ряда = 1 и 2 вместо 1 и 1,
# что сбивает нумерацию на 1. Не придумал как это исправить :(

def fibonacci(n, m):
    if n >= m:
        return 'Диапазон задан неверно'
    f_list = []
    i = 0
    f1 = 0
    f2 = 1
    while i != m:
        f3 = f1 + f2
        f1 = f2
        f2 = f3
        i += 1
        if i >= n:
            f_list.append(f3)
    return f_list

start = int(input('Введите начальный элемент: '))
end = int(input('Введите конечный элемент: '))
print(fibonacci(start, end))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


# Применил алгоритм сортировки выбором. Он работает быстрее пузырькового

def sort_to_max(origin_list):
    n = 0
    list1 = []
    while n <= len(origin_list) + 2:
        for i in origin_list:
            min_value = min(origin_list)
            min_value_index = origin_list.index(min_value)
            list1.append(min_value)
            origin_list.pop(min_value_index)
            original_list = list1
        n += 1
    return list1

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Пытался в аргументы вставить функцию по умолчанию для проверки элементов на
#  True False, в случае если функция не указана. Не получилось

def filter_function(func, iterator):
    res_list = []
    for i in iterator:
        if func(i) == True:
            res_list.append(i)
    return res_list




iterator = [-12, -11, 0, 2, 2.5, 4, 4, 10, 20]
func = lambda x: x > 0

print(filter_function(func, iterator))


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def paral_check(*arjs):
    a1 = str(input('Введите x1, y1 через запятую: '))
    a2 = str(input('Введите x2, y2 через запятую: '))
    a3 = str(input('Введите x3, y3 через запятую: '))
    a4 = str(input('Введите x4, y4 через запятую: '))
    if float(a1[0:a1.find(',')]) == float(a2[0:a2.find(',')]):
        if float(a3[0:a3.find(',')]) == float(a4[0:a4.find(',')]):
            if float(a1[a1.find(',')+1:]) == float(a4[a4.find(',')+1:]):
                if float(a2[a2.find(',')+1:]) == float(a3[a3.find(',')+1:]):
                    return 'Точки являются вершинами параллелограмма'
    else:
        return 'Точки не являются вершинами параллелограмма'

print(paral_check())
