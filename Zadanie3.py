# 1
n = int(input('Ввведите число n: '))
m = int(input('Введите число m: '))
z = int(input('Введите число z: '))
y = n+m+z
print('Сумма n+m+z=', y)
# 2
n = int(input('Длина 1-го катета: '))
m = int(input('Длина 2-го катета: '))
s = 1/2*n*m
print('Площадь прямоугольного треугольника: ', s)
# 3
n = int(input('Количество минут прошедших с начала суток: '))
hours = n % (60*24)//60
minutes = n % 60
print(f'{hours}:{minutes}')
# 4
a = int(input('Расстояние между рядами: '))
b = int(input('Расстояние между дырочками в ряду: '))
n = int(input('Количество дырочек в каждом ряду: '))
l = int(input('Длина свободного конца шнурка: '))
print(2*l+(2*n-1)*a+2*(n-1)*b)
# 5
a = int(input('Число 1: '))
b = int(input('Число 2: '))
c = int(input('Число 3: '))
if b >= a <= c:
    print(a)
elif a >= b <= c:
    print(b)
else:
    print(c)
# 6
a1 = int(input('Строка первой клетки: '))
b1 = int(input('Столбец первой клетки: '))
a2 = int(input('Строка второй клетки: '))
b2 = int(input('Столбец второй клетки: '))
if (a1+b1+a2+b2) % 2 == 0:
    print('Да')
else:
    print('Нет')
# 7
a = int(input('Год:'))
if (a % 4 == 0) and (a % 100 != 0) or (a % 400 == 0):
    print('Да')
else:
    print('Нет')
# 8
a = int(input('Первое число='))
b = int(input('Второе число='))
c = int(input('Тертье число='))
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)
# 9
n = int(input('n='))
m = int(input('m='))
k = int(input('k='))
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Да')
else:
    print('Нет')