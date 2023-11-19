from tkinter import N
# 1
def F(A, B):
    if A <= B:
     for i in range(A, B + 1):
         print(i)
    else:
        print('A должно быть меньше или равно B!')
A = int(input("Введите А: "))
B = int(input("Введите В: "))
F(A, B)

# 2
a = int(input('Введите А: '))
b = int(input('Введите В: '))
if a < b:
    for i in range(a, b + 1):
        print(i)
else:
    for i in range(a, b - 1, -1):
        print(i)

# 3
def F(A, B):

 if A>B:
    for i in range(A, B - 1, -1):
        if i % 2 != 0:
            print(i)
 else:
    print('А должно быть больше В')
A = int(input('A: '))
B = int(input('B: '))
F(A, B)
# 4
n = int(input())
sum = 0
for i in range(n):
    sum += int(input())
print(sum)
# 5
def F(n):
    s = (n * (n+1) // 2) ** 2
    print(s)
n = int(input())
# 6
res = 1
m = int(input())
for i in range(1, m + 1):
    res *= i
print(res)
# 7
n = int(input())
partial_factorial = 1
partial_sum = 0
for i in range(1, n + 1):
    partial_factorial *= i
    partial_sum += partial_factorial
print(partial_sum)
# 8
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep='', end='')
    print()
# 9
def f(N):
    if N <= 0:
        return 0
    elif N == 1:
        return 1
    s = 0
    p = 0
    c = 1

    for i in range(2, N + 1):
        next = p + c
        s += c
        p = c
        c = next

    return s
g = int(input())
r = f(N)
print(r)