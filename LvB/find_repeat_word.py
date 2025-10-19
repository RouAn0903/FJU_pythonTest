N = eval(input())
for i in range(N):
    LS = input().split(' ')
    WLS = []
    CLS = []
    for ls in LS:
        if ls not in WLS:
            WLS.append(ls)
        elif ls in WLS:
            CLS.append((ls, LS.count(ls)))
    for cls in CLS:
        print(f'{cls[0]},{cls[1]}')