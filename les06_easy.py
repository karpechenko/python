# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sides(self):
        ab = ((self.b[0] - self.a[0]) ** 2 + (self.b[1] - self.a[1]) ** 2) ** 0.5
        bc = ((self.c[0] - self.b[0]) ** 2 + (self.c[1] - self.b[1]) ** 2) ** 0.5
        ca = ((self.c[0] - self.a[0]) ** 2 + (self.c[1] - self.a[1]) ** 2) ** 0.5
        return [ab, bc, ca]

    def perimeter(self):
        return self.sides()[0] + self.sides()[1] + self.sides()[2]
    
    def square(self):
        p = self.perimeter() / 2
        return ((p * (p - self.sides()[0]) * (p - self.sides()[1]) * (p - self.sides()[2])) ** 0.5)

    def max_height(self):
        max_h = 0
        for i in self.sides():
            h = (self.square()) * 2 / i
            if h > max_h:
                max_h = h
        return max_h

triangle1 = Triangle([1, 7], [3, 5], [4, 9])

print(f'Стороны треугольника: {triangle1.sides()[0]}, {triangle1.sides()[1]}, {triangle1.sides()[2]}')
print(f'Периметр треугольника: {triangle1.perimeter()}')
print(f'Площадь треугольника: {triangle1.square()}')
print(f'Максимальная высота треугольника: {triangle1.max_height()}')


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def isequal(self):
        if self.sides()[4] == self.sides()[5]:
            return True
        else:
            return False

    def sides(self):
        ab = ((self.b[0] - self.a[0]) ** 2 + (self.b[1] - self.a[1]) ** 2) ** 0.5
        bc = ((self.c[0] - self.b[0]) ** 2 + (self.c[1] - self.b[1]) ** 2) ** 0.5
        cd = ((self.d[0] - self.c[0]) ** 2 + (self.d[1] - self.c[1]) ** 2) ** 0.5
        da = ((self.a[0] - self.d[0]) ** 2 + (self.a[1] - self.d[1]) ** 2) ** 0.5
        ac = ((self.c[0] - self.a[0]) ** 2 + (self.c[1] - self.a[1]) ** 2) ** 0.5
        bd = ((self.d[0] - self.b[0]) ** 2 + (self.d[1] - self.b[1]) ** 2) ** 0.5
        return [ab, bc, cd, da, ac, bd]

    def perimeter(self):
        return self.sides()[0] + self.sides()[1] + self.sides()[2] + self.sides()[3]

    def square(self):
        p1 = self.sides()[0] + self.sides()[1] + self.sides()[4]
        p2 = self.sides()[2] + self.sides()[3] + self.sides()[4]
        s1 = ((p1 * (p1 - self.sides()[0]) * (p1 - self.sides()[1]) * (p1 - self.sides()[4])) ** 0.5)
        s2 = ((p2 * (p2 - self.sides()[2]) * (p2 - self.sides()[3]) * (p2 - self.sides()[4])) ** 0.5)
        return s1 + s2

trapeze1 = Trapeze([1, 1], [3, 4], [5, 4], [7, 1])

print(f'Трапеция является равнобедренной:  {trapeze1.isequal()}')
print(f'Длина стороны трапеции ab: {trapeze1.sides()[0]}')
print(f'Длина стороны трапеции bc: {trapeze1.sides()[1]}')
print(f'Длина стороны трапеции cd: {trapeze1.sides()[2]}')
print(f'Длина стороны трапеции da: {trapeze1.sides()[3]}')
print(f'Периметр трапеции: {trapeze1.perimeter()}')
print(f'Площадь трапеции: {trapeze1.square()}')

