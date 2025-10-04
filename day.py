def DayoftheYear(tY,tM,tD):
    if tM == 1:
        return tD
    elif tM == 2:
        return 31 + tD
    else:
        IsLY = False
        if tY % 4 == 0:
            if tY % 100 != 0:
                IsLY = True
            if tY % 400 == 0:
                IsLY = True
        dls = [0,31,28,31,30,31,30,31,31,30,31,30,31]
        if IsLY:
            dls[2] = 29
        CT = tD
        for m in range(1,tM):
            CT += dls[m]
        return CT
        


n = eval(input())
for i in range(n):
    ls = input().split(' ')
    y =int(ls[0])
    m =int(ls[1])
    d =int(ls[2])
    # 2000 1 1 >> day1 >> week1
    # 2000 1 3 >> day3 >> week3
    CT = DayoftheYear(y,m,d)
    if y > 2000:
        for Y in range(2000,y):
            CT += DayoftheYear(y,12,31)
    CT += 5
    w = CT % 7
    if w == 0:
        print(7)
    else:
        print(w)