import math
k = eval(input())
for i in range(k):
    a = float(input())
    b = float(input())
    sum = math.ceil(a - b)
    print(int(sum))
