k = eval(input())
for i in range(k):
    num = input().split(' ')
    n = int(num[0])
    f = int(num[1])
    r = 0.5*f - n
    c = 2*n -0.5*f
    if r == int(r) and c == int(c) and r >= 0 and c >= 0:
        print(f"{int(r)} {int(c)}")
    else:
        print("False")