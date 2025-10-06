n = eval(input())
for i in range(n):
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    x3 = float(input())
    y3 = float(input())
    a = ((x2-x1)**2 + (y2-y1)**2)**0.5
    b = ((x3-x2)**2 + (y3-y2)**2)**0.5
    c = ((x1-x3)**2 + (y1-y3)**2)**0.5
    s = (a+b+c)/2
    A = (s*(s-a)*(s-b)*(s-c))**0.5
    print(f"{A:.3f}")
