n = eval(input())
for i in range(n):
    num = input().split(' ')
    LS = []
    for num2 in num:
        x = int(num2)
        if (x >= 1 and x <= 49) and x not in LS:
            LS.append(x)
        else:
            print("No")
            break
    if len(LS) == 7:
        print("Yes")