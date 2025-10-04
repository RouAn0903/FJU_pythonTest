n = int(input())  
for i in range(n):
    oN = input()  
    # 8 >> 10
    D = int(oN, 8)  

    # 10 >> 4
    xS = ''
    while D > 0:
        xS = str(D % 4) + xS
        D //= 4
    print(xS)