N = eval(input())
for i in range(N):
    LS = input().split(' ')
    NLS = []
    CLS = []
    for ls in LS:
        if ls not in NLS:
            NLS.append(ls)
            CLS.append(LS.count(ls))
    print(max(CLS))
