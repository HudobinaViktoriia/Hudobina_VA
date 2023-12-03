# 2
print('№2')
def find_point(x1, x2, y1, y2, z1, z2):
    # тангенсы углов для каждой точки
    tan_x = y2 / x2
    tan_y = z2 / y2
    tan_z = x2 / z2

    # Находим минимальный тангенс
    min_tan = min(tan_x, tan_y, tan_z)

    if min_tan == tan_x:
        return (x1, x2)
    elif min_tan == tan_y:
        return (y1, y2)
    else:
        return (z1, z2)

x1 = int(input('Введите х1: '))
x2 = int(input('Введите х2: '))
y1 = int(input('Введите y1: '))
y2 = int(input('Введите y2: '))
z1 = int(input('Введите z1: '))
z2 = int(input('Введите z2: '))
min_point = find_point(x1, x2, y1, y2, z1, z2)
print("Координаты точки с минимальным углом:", min_point)
