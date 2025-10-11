N = eval(input())
for i in range(N):
    LS = input().split(' ')
    X = LS[0]
    Y = LS[1]
    LX = len(X)
    LY = len(Y)
    if LX != LY:
        if LX > LY:
            while(len(X) > len(Y)):
                Y = '0' + Y
        else:
            while(len(X) < len(Y)):
                X = '0' + X
    
    L = len(X)
    CT = 0
    plus = 0
    for j in range(-1, -L-1, -1):
        T = int(X[j]) + int(Y[j]) + plus
        if T > 9:
            CT +=1
            plus = 1
        else:
            plus = 0
    print(CT)