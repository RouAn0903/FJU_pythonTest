K = eval(input())
for i in range(K):
    LS = input().replace(' ', '')
    
    R1 = ''
    R2 = ''
    for j in range(len(LS)):
        if j % 2 == 0:
            R1 += LS[j]
        else:
            R2 += LS[j]
    
    RV = R1 + R2
    print(RV.upper())
