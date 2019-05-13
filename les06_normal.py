#                _______ Классы _________ 
class Person:
    def __init__(self, surname, name, patronymic):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic

class Class_room:
    def __init__(self, class_name, students = [], subjects = []):
        self.class_name = class_name
        self.students = students
        self.subjects = subjects
        class_list.append(self)

class Student(Person):
    def __init__(self, surname, name, patronymic, class_name):
        Person.__init__(self, surname, name, patronymic)
        self.class_name = class_name
        students_list.append(self)

    def full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic

class Parent(Person):
    def __init__(self, surname, name, patronymic, child_name):
        Person.__init__(self, surname, name, patronymic)
        self.child_name = child_name
        parents_list.append(self)

    def full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic

class Teacher(Person):
    def __init__(self, surname, name, patronymic, subject):
        Person.__init__(self, surname, name, patronymic)
        self.subject = subject
        teachers_list.append(self)

    def full_name(self):
        return self.surname + ' ' + self.name + ' ' + self.patronymic

#                _______ Функции _________    

def cl_name_list():
    lst = [cl.class_name for cl in class_list]
    print(lst)

def st_in_class():
    entry = input('Укажите класс: ')
    lst = [cl.class_name for cl in class_list]
    if entry not in lst:
        print('Такого класса в школе не существует')
    for cl in class_list:
        if cl.class_name == entry:
            print(cl.students)

def st_subjects():
    try:
        entry = input('Введите ФИО ученика:')
        for st in students_list:
            if st.full_name() == entry:
                clname = st.class_name
        for cl in class_list:
            if cl.class_name == clname:
                print('--------------------')
                print(entry)
                print(clname)
                for subj in cl.subjects:
                    for teacher in teachers_list:
                        if teacher.subject == subj:
                            print(teacher.full_name() + ' - ' + subj)
                print('--------------------')
    except UnboundLocalError:
        print('Ученика с такими данными не обнаруженно')

def st_parents():
    try:
        entry = input('Введите ФИО ученика:')
        name = entry.split()[0] + ' ' + entry.split()[1]
        for prt in parents_list:
            if prt.child_name == name:
                print(prt.full_name())
    except IndexError:
        print('Ученика с такими данными не обнаруженно')

def tch_in_class():
    entry = input('Укажите класс:')
    lst = [cl.class_name for cl in class_list]
    if entry not in lst:
        print('Такого класса в школе не существует')
    for cl in class_list:
        if cl.class_name == entry:
            for subj in cl.subjects:
                for teacher in teachers_list:
                    if teacher.subject == subj:
                            print(teacher.full_name() + ' - ' + subj)

#                _______ Объекты, списки _________ 

students_list = []

student_1 = Student('Земцовский', 'Виктор', 'Егорович', '5А')
student_2 = Student('Юдина', 'Диана', 'Дмитриевна', '5Б')
student_3 = Student('Северинов', 'Владимир', 'Витальевич', '6А')
student_4 = Student('Гусева', 'Наталья', 'Павловна', '6Б')
student_5 = Student('Караев', 'Антон', 'Юрьевич', '7А')
student_6 = Student('Лескова', 'Елена', 'Николаевна', '7Б')
student_7 = Student('Янкин', 'Евгений', 'Аркадиевич', '7А')
student_8 = Student('Фетисова', 'Изабелла', 'Васильевна', '5А')
student_9 = Student('Беленков', 'Дмитрий', 'Станиславович', '5Б')
student_10 = Student('Гуренко', 'Ксения', 'Андреевна', '6А')
student_11 = Student('Шульгин', 'Алексей', 'Константинович', '6Б')
student_12 = Student('Алых', 'Валерия', 'Леонидовна', '7А')
student_13 = Student('Кутлыев', 'Андрей', 'Денисович', '7Б')
student_14 = Student('Кирилевич', 'Виктория', 'Владиславовна', '5А')
student_15 = Student('Лыков', 'Евгений', 'Александрович', '5Б')
student_16 = Student('Каратеева', 'Александра', 'Евгеньевна', '6А')
student_17 = Student('Седых', 'Руслан', 'Генадьевич', '6Б')
student_18 = Student('Ярмолинская', 'Евгения', 'Павловна', '7А')
student_19 = Student('Рябцев', 'Александр', 'Михайлович', '7Б')
student_20 = Student('Квасова', 'Анастасия', 'Алексеевна', '5А')
student_21 = Student('Ларин', 'Олег', 'Максимович', '5Б')
student_22 = Student('Кутякова', 'Александра', 'Викторовна', '6А')
student_23 = Student('Лазаренко', 'Вячеслав', 'Андреевич', '6Б')
student_24 = Student('Семянина', 'Милана', 'Васильевна', '7А')
student_25 = Student('Кацук', 'Павел', 'Эдуардович', '7Б')
student_26 = Student('Салихов', 'Сергей', 'Владимирович', '5А')
student_27 = Student('Майсак', 'Богдана', 'Рубеновна', '5Б')
student_28 = Student('Усачев', 'Константин', 'Петрович', '6А')
student_29 = Student('Смотрова', 'Варвара', 'Дмитриевна', '6Б')
student_30 = Student('Шерстов', 'Максим', 'Александрович', '7А')
student_31 = Student('Травникова', 'Ольга', 'Евгениевна', '7Б')

parents_list = []

parent_m_1 = Parent('Земцовская', 'Елизавета', 'Васильевна', 'Земцовский Виктор')
parent_f_1 = Parent('Земцовский', 'Егор', 'Олегович', 'Земцовский Виктор')
parent_m_2 = Parent('Юдина', 'Ольга', 'Павловна', 'Юдина Диана')
parent_f_2 = Parent('Юдин', 'Дмитрий', 'Сергеевич', 'Юдина Диана')
parent_m_3 = Parent('Северинова', 'Наталья', 'Юрьевна', 'Северинов Владимир')
parent_f_3 = Parent('Северинов', 'Виталий', 'Александрович', 'Северинов Владимир')
parent_m_4 = Parent('Гусева', 'Валентина', 'Петровна', 'Гусева Наталья')
parent_f_4 = Parent('Гусев', 'Павел', 'Глебович', 'Гусева Наталья')
parent_m_5 = Parent('Караева', 'Галина', 'Васильевна', 'Караев Антон')
parent_f_5 = Parent('Караев', 'Юрий', 'Федорович', 'Караев Антон')
parent_m_6 = Parent('Лескова', 'Надежда', 'Григорьвна', 'Лескова Елена')
parent_f_6 = Parent('Лесков', 'Николай', 'Петрович', 'Лескова Елена')
parent_m_7 = Parent('Янкина','Нина', 'Васильевна', 'Янкин Евгений')
parent_f_7 = Parent('Янкин', 'Аркадий', 'Владимирович', 'Янкин Евгений')
parent_m_8 = Parent('Фетисова', 'Елена', 'Андреевна', 'Фетисова Изабелла')
parent_f_8 = Parent('Фетисов', 'Василий', 'Дмитриевич', 'Фетисова Изабелла')
parent_m_9 = Parent('Беленкова', 'Светлана', 'Генадиевна', 'Беленков Дмитрий')
parent_f_9 = Parent('Беленков', 'Станислав', 'Владиславович', 'Беленков Дмитрий')
parent_m_10 = Parent('Гуренко', 'Алла', 'Борисовна', 'Гуренко Ксения')
parent_f_10 = Parent('Гуренко', 'Андрей', 'Викторович', 'Гуренко Ксения')
parent_m_11 = Parent('Шульгина', 'Татьяна', 'Кондратьевна', 'Шульгин Алексей')
parent_f_11 = Parent('Шульгин', 'Константин', 'Александрович', 'Шульгин Алексей')
parent_m_12 = Parent('Алых', 'Ольга', 'Аркадиевна', 'Алых Валерия')
parent_f_12 = Parent('Алых', 'Леонид', 'Игоревич', 'Алых Валерия')
parent_m_13 = Parent('Кутлыева', 'Наталья', 'Леонидовна', 'Кутлыев Андрей')
parent_f_13 = Parent('Кутлыев', 'Денис', 'Викторович', 'Кутлыев Андрей')
parent_m_14 = Parent('Кирилевич', 'Яна', 'Петровна', 'Кирилевич Виктория')
parent_f_14 = Parent('Кирилевич', 'Владислав', 'Эдуардович', 'Кирилевич Виктория')
parent_m_15 = Parent('Лыкова', 'Томара', 'Владимировна', 'Лыков Евгений')
parent_f_15 = Parent('Лыков', 'Александр', 'Васильевич', 'Лыков Евгений')
parent_m_16 = Parent('Каратеева', 'Вера', 'Сергеевна', 'Каратеева Александра')
parent_f_16 = Parent('Каратеев', 'Евгений', 'Степанович', 'Каратеева Александра')
parent_m_17 = Parent('Седых', 'Варвара', 'Викторовна', 'Седых Руслан')
parent_f_17 = Parent('Седых', 'Генадий', 'Олегович', 'Седых Руслан')
parent_m_18 = Parent('Ярмолинская', 'Надежда', 'Васильевна', 'Ярмолинская Евгения')
parent_f_18 = Parent('Ярмолинский', 'Павел', 'Андреевич', 'Ярмолинская Евгения')
parent_m_19 = Parent('Рябцева', 'Диана', 'Мартыновна', 'Рябцев Александр')
parent_f_19 = Parent('Рябцев', 'Михаил', 'Владимирович', 'Рябцев Александр')
parent_m_20 = Parent('Квасова', 'Евгения', 'Захаровна', 'Квасова Анастасия')
parent_f_20 = Parent('Квасов', 'Алексей', 'Петрович', 'Квасова Анастасия')
parent_m_21 = Parent('Ларина', 'Виктория', 'Юрьевна', 'Ларин Олег')
parent_f_21 = Parent('Ларин', 'Максим', 'Давидович', 'Ларин Олег')
parent_m_22 = Parent('Кутякова', 'Людмила', 'Станиславовна', 'Кутякова Александра')
parent_f_22 = Parent('Кутяков', 'Виктор', 'Львович', 'Кутякова Александра')
parent_m_23 = Parent('Лазаренко', 'Валерия', 'Павловна', 'Лазаренко Вячеслав')
parent_f_23 = Parent('Лазаренко', 'Андрей', 'Абрамович', 'Лазаренко Вячеслав')
parent_m_24 = Parent('Семянина', 'Надежда', 'Дмитриевна', 'Семянина Милана')
parent_f_24 = Parent('Семянин', 'Василий', 'Антонович', 'Семянина Милана')
parent_m_25 = Parent('Кацук', 'Лада', 'Витальевна', 'Кацук Павел')
parent_f_25 = Parent('Кацук', 'Эдуард', 'Павлович', 'Кацук Павел')
parent_m_26 = Parent('Салихова', 'Татьяна', 'Валерьевна', 'Салихов Сергей')
parent_f_26 = Parent('Салихов', 'Владимир', 'Хасанович', 'Салихов Сергей')
parent_m_27 = Parent('Майсак', 'Анна', 'Леонидовна', 'Майсак Богдана')
parent_f_27 = Parent('Майсак', 'Рубен', 'Назарович', 'Майсак Богдана')
parent_m_28 = Parent('Усачева', 'Эльвира', 'Даниловна', 'Усачев Константин')
parent_f_28 = Parent('Усачев', 'Петр', 'Николаевич', 'Усачев Константин')
parent_m_29 = Parent('Смотрова', 'Инна', 'Ивановна', 'Смотрова Варвара')
parent_f_29 = Parent('Смотров', 'Дмитрий', 'Андреевич', 'Смотрова Варвара')
parent_m_30 = Parent('Шерстова', 'Маргарита', 'Василиевна', 'Шерстов Максим')
parent_f_30 = Parent('Шерстов', 'Александр', 'Александрович', 'Шерстов Максим')
parent_m_31 = Parent('Травникова', 'Наталья', 'Аркадиевна', 'Травникова Ольга')
parent_f_31 = Parent('Травников', 'Евгений', 'Богданович', 'Травникова Ольга')

teachers_list = []

teacher_1 = Teacher('Тимофеева', 'Алена', 'Степановна', 'Русский язык')
teacher_2 = Teacher('Абрамова', 'Ольга', 'Егоровна', 'Литература')
teacher_3 = Teacher('Доронина', 'Эмма', 'Леонидовна', 'Алгебра')
teacher_4 = Teacher('Антонова', 'Зинаида', 'Рубеновна', 'Геометрия')
teacher_5 = Teacher('Стрелкова', 'Елизавета', 'Сергеевна', 'Химия')
teacher_6 = Teacher('Тарасова', 'Татьяна', 'Степановна', 'Физика')
teacher_7 = Teacher('Киселев', 'Арсений', 'Эдуардович', 'Иностранный язык')
teacher_8 = Teacher('Киселева', 'Анфиса', 'Андреевна', 'Биология')
teacher_9 = Teacher('Рожкова', 'Виктория', 'Владимировна', 'Физкультура')
teacher_10 = Teacher('Козлов', 'Анатолий', 'Мартынович', 'История')
teacher_11 = Teacher('Яковлев', 'Максим', 'Анатольевич', 'География')
teacher_12 = Teacher('Копылов', 'Александр', 'Викторович', 'Информатика')
teacher_13 = Teacher('Фадеев', 'Артур', 'Денисович', 'ОБЖ')
teacher_14 = Teacher('Тереньтьва', 'Вера', 'Ефимовна', 'Черчение')
teacher_15 = Teacher('Ларионов', 'Константин', 'Валерьевич', 'Труд')

fifth_class_subjects = ['Русский язык', 'Литература', 'Алгебра', 'Геометрия', 'История', 'География',
                     'ОБЖ', 'Труд', 'Физкультура']
sixth_class_subjects = ['Русский язык', 'Литература', 'Алгебра', 'Геометрия', 'История', 'География',
                     'ОБЖ', 'Труд', 'Черчение', 'Биология', 'Физика', 'Физкультура', 'Иностранный язык']
seventh_class_subjects =  ['Русский язык', 'Литература', 'Алгебра', 'Геометрия', 'История', 'География',
                     'ОБЖ', 'Труд', 'Черчение', 'Биология', 'Физика', 'Информатика', 'Химия', 
                     'Физкультура', 'Иностранный язык']

class_list = []

class1 = Class_room('5А', [student.surname for student in students_list if student.class_name == '5А'],
                    fifth_class_subjects)
class2 = Class_room('5Б', [student.surname for student in students_list if student.class_name == '5Б'],
                    fifth_class_subjects)
class3 = Class_room('6А', [student.surname for student in students_list if student.class_name == '6А'],
                    sixth_class_subjects)
class4 = Class_room('6Б', [student.surname for student in students_list if student.class_name == '6Б'],
                    sixth_class_subjects)
class5 = Class_room('7А', [student.surname for student in students_list if student.class_name == '7А'],
                    seventh_class_subjects)
class6 = Class_room('7Б', [student.surname for student in students_list if student.class_name == '7Б'],
                    seventh_class_subjects)

#                _______ Скрипт _________

answer = input('Начать работу? Y/N :')
while answer != 'n' or answer !='N' or answer !='т' or answer !='Т':
    if answer == 'y' or answer =='Y' or answer =='н' or answer =='Н':    
        print('Вы можете выполнить следующие действия:')
        print('[1] - Получить полный список всех классов школы')
        print('[2] - Получить список всех учеников в указанном классе')
        print('[3] - Получить список всех предметов указанного ученика')
        print('[4] - Получить ФИО родителей указанного ученика')
        print('[5] - Получить список всех учителей, преподающих в указанном классе')

        do = {'1':cl_name_list,
              '2':st_in_class,
              '3':st_subjects,
              '4':st_parents,
              '5':tch_in_class
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
        
    elif answer == 'n' or answer =='N' or answer =='т' or answer =='Т':
        print('Работа завершена')
        break
    else:
        print('неизвестная команда')
        break
