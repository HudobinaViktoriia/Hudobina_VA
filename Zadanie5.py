# 1
def F(N):
    for i in range(1, N):
        s = i*i
        print(s)
N = int(input())
F(N)
# 2
def F(n):
    if n > 2:
        for i in range(1, n + 1):
            if n % i == 0 and i!=1:
                print(i)
                break

n = int(input())

F(n)
# 3
def F(n):
    r = 1
    p = 0
    while r * 2 <= n:
        r *= 2
        p += 1
    print(p, r) # (показатель, степень)
n = int(input())
F(n)
# 4
def F(x,y):
    d = 1
    while x < y:
        x = x + x * 0.10
        d += 1
    print(d)
x = float(input())
y = float(input())
F(x, y)
# 5
def F(n):
    c = 0
    while True:
        if n == 0:
            break
        c += 1
    print(c)
n  = int(input())
F(n)
# 6
def F(n):
    c = 0 #кол-во элементов последовательности
    l = 0 #сумма элементов последовательности
    while True:
        if n == 0:
            break
        l += n
        c += 1
    print(l/c)
n  = int(input())
F(n)
# 7
def F(n):
    c = 0
    previous = None
    while True:
        if n == 0:
            break
        if previous is not None and n > previous:
            c += 1
        previous = n
    print(c)
n = int(input())
F(n)
# 8
def F(n):
    c = 0
    previous = None
    while True:
        if n == 0:
            break
        if previous is not None and n > previous:
            c += 1
        previous = n
    print(c)
n = int(input())
F(n)