def IsANO(sX):
    lenX = len(sX)
    CV = 0
    for sx in sX:
        CV += int(sx) ** lenX
    if CV == int(sX):
        return True
    else:
        return False

k = eval(input())
for i in range(k):
    LS = input().split(' ')
    ST = int(LS[0])
    ED = int(LS[1])
    RLS = []
    for j in range(ST, ED+1):
        if IsANO(str(j)):
            RLS.append(j)
    
    if len(RLS) == 0:
        print("none")
    else:
        for rls in RLS:
            print(f"{rls} ", end='')
        print('')