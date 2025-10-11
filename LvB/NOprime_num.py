def IsP(oN):
    for i in range(2, int(oN**0.5)+1):
        if oN % i == 0:
            return False
    return True

N = eval(input())
for i in range(N):
    Xth = int(input())
    NowNum = 2
    Nth = 1
    if Xth == 1:
        print(2)
    else:
        while Xth != Nth:
            if NowNum == 2:
                NowNum = 3
            else:
                NowNum += 2
            
            if IsP(NowNum):
                Nth += 1 
        print(NowNum)