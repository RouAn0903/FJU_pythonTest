N = eval(input())
for i in range(N):
    X = int(input())
    di = 2
    FLS = []
    while di <= int(X**0.5):
        if X % di == 0:
            FLS.append(di)
            X = int(X / di)
        else:
            di += 1
    FLS.append(X)

    RV = ''
    for fls in FLS:
        if RV == '':
            RV = str(fls)
        else:
            RV += (' '+ str(fls))
    print(RV)
