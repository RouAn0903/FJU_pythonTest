k = eval(input())
for i in range(k):
    LS = input().split(' ')
    dLS = [] #不同的
    pLS = [] #得獎的
    for ls in LS:
        if ls not in dLS:
            dLS.append(ls)
            ct = LS.count(ls)
            if ct >= 3:
                pLS.append(int(ls))
    if len(pLS) > 1:
        pLS.sort()
        print(pLS[1])
    elif len(pLS) == 1:
        print(pLS[0])
    else:
        print('0')