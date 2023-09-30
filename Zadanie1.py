# 1
print("Курс Основы программирования начался")
# 2
print(16823 * 12302 % 3092)
# 3
name = input("введите свое имя: ")
age = int(input('введите свой возраст: '))
x = 16 - age
if 0 < age < 75:
    if name == "Иван":
        print("Людей с именем Иван быть не должно")
    elif age >= 16:
        print("Поздравляем вы поступили в ВГУИТ")
    elif age < 16:
        if x == 1:
            print('Сначала нужно окончить школу!')
            print("Вам осталось учиться в школе: " + str(x) + ' год!')
        if x >= 5:
            print('Сначала нужно окончить школу!')
            print("Вам осталось учиться в школе: " + str(x) + ' лет!')
        if 1 < x < 5:
            print('Сначала нужно окончить школу!')
            print("Вам осталось учиться в школе: " + str(x) + ' года!')
else:
    print("недопустимый возраст")
# 4
seconds = int(input('Количество секунд: '))
days = seconds // 86400
hours = (seconds % 86400) // 3600
minutes = (seconds % 3600) // 60
sec = seconds % 60
print(days, hours, minutes, sec)
# 5
n = int(input('Введите число: '))
m = n + n**2 + n**3 + n**4 + n**5
print(m)
# 6
x = int(input('Введите значение x: '))
y = int(input('Введите значение y: '))
z = x
x = y
y = z
print('x=', x)
print('y=', y)
# 7
n = int(input('Введите число: '))
if n % 2 == 0:
    print('Четное число!')
else:
    print('Нечетное число!')