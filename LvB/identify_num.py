def Comp(X, Y):
    L = len(X)
    RV = 0
    for i in range(L):
        if X[i] != Y[i]:
            RV += 1
    return RV

N = eval(input())
for i in range(N):
    S = input()
    RV = 0
    if len(S) == 3:
        if Comp(S, 'one') <= 1:
            RV = 1
        if Comp(S, 'two') <= 1:
            RV = 2
    if len(S) == 5:
        if Comp(S, 'three') <= 1:
            RV = 3
        if Comp(S, 'eight') <= 1:
            RV = 8
    
    print(RV)
