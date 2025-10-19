while True:
    LS = input()
    if LS == '0':
        break
    else:
        LS = LS.split(' ')
        PLS = []
        for ls in LS:
            PLS.append(eval(ls))

        COST = 0
        while len(PLS) > 1:    
            PLS.sort()
            NPT = PLS[0] + PLS[1]
            COST += NPT
            PLS.pop(0)  # 移除索引值為0的值[0]
            PLS.pop(0)  # 移除索引值為0的值[1]
            PLS.append(NPT)
        print(COST)