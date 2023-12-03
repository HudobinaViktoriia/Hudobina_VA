# Вариант 13
# №1
print('№1')
def find_minimum(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Введите элемент: "))
            row.append(element)
        matrix.append(row)

    for i in range(rows):
        if (i + 1) % 2 == 0:
            min_number = min(matrix[i])
            print(matrix)
            print(f"Наименьшее число в строке {i + 1}: {min_number}")

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

find_minimum(rows, cols)
