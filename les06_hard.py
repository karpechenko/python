# Вариант единичного подсчета по ФИО сотрудника:

import os

class Worker:
    def __init__(self, full_name, position, salary, hour_rate, working_hours):
        self.full_name = full_name
        self.position = position
        self.salary = int(salary)
        self.hour_rate = int(hour_rate)
        self.working_hours = int(working_hours)

    def wages(self):
        if self.working_hours == self.hour_rate:
            return self.salary 
        elif self.working_hours < self.hour_rate:
            return self.salary / self.hour_rate * self.working_hours
        else:
            return (self.working_hours - self.hour_rate) * (self.salary / self.hour_rate) * 2 + self.salary

worker = input('Введите ФИО работника:')

directory = '.../data'

path = os.path.join(directory, 'workers.txt')
with open(path, 'r', encoding='UTF-8') as f:
    for line in f:
        if worker in line:
            full_name = line.split()[0]  + ' ' + line.split()[1] + ' ' + line.split()[2]
            position = line.split()[3]
            salary = line.split()[4]
            hour_rate = line.split()[5]
            break

path = os.path.join(directory, 'hours_of.txt')
with open(path, 'r', encoding='UTF-8') as f:
    for line in f:
        if worker in line:
            working_hours = line.split()[3]
            break
try:            
    worker = Worker(full_name, position, salary, hour_rate, working_hours)
    print(worker.wages())
except NameError:
    print('Информация о данном сотруднике отсутствует, либо ФИО введены неверно')
except ValueError:
    print('ФИО работника не были введены')


# Вариант общего подсчета ЗП всех сотрудников с записью в файл:

import os

class Worker:
    def __init__(self, full_name, position, salary, hour_rate, working_hours):
        self.full_name = full_name
        self.position = position
        self.salary = int(salary)
        self.hour_rate = int(hour_rate)
        self.working_hours = int(working_hours)

    def wages(self):
        if self.working_hours == self.hour_rate:
            wages_list.append(self.full_name + '-' + str(self.salary))
        elif self.working_hours < self.hour_rate:
            wages_list.append(self.full_name + '-' + str((self.salary / self.hour_rate * self.working_hours)))
        else:
            wages_list.append(self.full_name + '-' + str((self.working_hours - self.hour_rate) * (self.salary / self.hour_rate) * 2 + self.salary))
        
wages_list = []

directory = '.../data'

path = os.path.join(directory, 'workers.txt')
with open(path, 'r', encoding='UTF-8') as f:
    for line in f:
        if 'Имя' in line:
            continue
        full_name = line.split()[0]  + ' ' + line.split()[1] + ' ' + line.split()[2]
        position = line.split()[3]
        salary = line.split()[4]
        hour_rate = line.split()[5]
        path = os.path.join(directory, 'hours_of.txt')
        with open(path, 'r', encoding='UTF-8') as f:
            for line in f:
                if full_name in line:
                    working_hours = line.split()[3]
        worker = Worker(full_name, position, salary, hour_rate, working_hours)
        worker.wages()

path = os.path.join(directory, 'wages.txt')
with open(path, 'w', encoding='UTF-8') as f:
    for wages in wages_list:
        f.write(wages + '\n')
