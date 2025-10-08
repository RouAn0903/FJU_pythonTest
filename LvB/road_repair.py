N =eval(input())
for i in range(N):
    LS = input().split(' ')
    LX= input().split(' ')
    n = int(LS[0])
    r = int(LS[1])
    if n == r:
        print('*')
    else:
        LA = []
        for j in range(1, n+1): #總共人數(工牌)
            LA.append(str(j))
        for lx in LX:
            if lx in LA:    #去掉回來的人(工牌)
                LA.remove(lx)
        for la in LA:
            print(f"{la} ", end = '')
        print('')