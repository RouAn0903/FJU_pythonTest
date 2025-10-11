N = eval(input())
for i in range(N):
    x = eval(input())
    NoS = x
    NoB = x
    NoC = x
    while NoB >= 4 or NoC >= 3:
        NoExtra = 0
        if NoB >= 4:
            A = NoB // 4
            NoExtra += A
            NoB -= (4*A)
        if NoC >= 3:
            B = NoC // 3
            NoExtra += B
            NoC -= (3*B)

        NoS += NoExtra
        NoB += NoExtra
        NoC += NoExtra
    
    print(NoS)