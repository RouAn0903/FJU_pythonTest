N = eval(input())
for i in range(N):
    X = int(input())
    K = ''
    for j in range(1, X+1):
        K += str(j)
    CTLS = [0,0,0,0,0,0,0,0,0,0]
    for k in K:
        idx = int(k)
        CTLS[idx] += 1
    
    RV = ''
    for ctls in CTLS:
        if RV == '':
            RV = str(ctls)
        else:
            RV += (' '+str(ctls))
    print(RV)