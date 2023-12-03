# Вариант 13
# 1
print('№1')
def chk_arm(n):
    nn = n
    d = []
    while n > 0:
        d.append(n % 10)
        n = n // 10
    k = len(d)
    ss = sum(map(lambda x: x ** k, d))
    return nn == ss
for i in range(1, int(input('Введите число: ')) + 1):
    if chk_arm(i):
        print(i)

