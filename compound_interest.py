n = eval(input())
for i in range(n):
    num = input().split(' ')
    P = eval(num[0])
    r = eval(num[1])/100
    t = eval(num[2])
    F = P * ((1+(r/12))**(12*t))
    print(f'{F:.0f}')