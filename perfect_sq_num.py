import math

n = eval(input())
for i in range(n):
    ls = input().split(' ')
    a = int(ls[0])
    b = int(ls[1])
    x = math.ceil(a**0.5)
    y = math.floor(b**0.5)
    sum = 0
    for j in range(x, y+1):
        sum += (j*j)
    print(sum)

