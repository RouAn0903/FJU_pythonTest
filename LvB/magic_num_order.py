N = eval(input())
for i in range(N):
    LS = input().split(' ')
    Max = -1
    Min = -1
    RV = "YES"
    for ls in LS:
        NowV = int(ls)
        if Max == -1:
            Max = NowV
            Min = NowV
        else:
            if NowV <= Max and NowV > Min:
                RV = "NO"
                break
            else:
                if NowV < Min:
                    Min = NowV
                elif NowV > Max:
                    Max = NowV
    print(RV)