# Вариант 13
# 1
print('№1')
from random import randint
arr = [randint(1, 10) for _ in range(30)]
out = dict()
for i, a in enumerate(arr):
    if a in out:
        out[a].append(i)
    else:
        out[a] = [i]
for k, v in out.items():
    if len(v) > 1:
        print(f'{k} :', *v)
# 2
print('№2')
x = [int(input('Введите числа: ')) for _ in range(8)]
print(x)
x = [2*a if a < 15 else a for a in x]
print(x)
