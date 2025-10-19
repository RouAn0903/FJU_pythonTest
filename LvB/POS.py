def getChange(x):
    Ct50 = x // 50
    V = x - (50*Ct50)
    Ct10 = V // 10
    V = V - (10*Ct10)
    Ct5 = V // 5
    Ct1 = V - (5*Ct5)

    RV = ''
    if Ct50 > 0:
        for i in range(Ct50):
            if RV == '':
                RV = f'50'
            else:
                RV += f' 50'
    
    if Ct10 > 0:
        for i in range(Ct10):
            if RV == '':
                RV = f'10'
            else:
                RV += f' 10'

    if Ct5 > 0:
        for i in range(Ct5):
            if RV == '':
                RV = f'5'
            else:
                RV += f' 5'

    if Ct1 > 0:
        for i in range(Ct1):
            if RV == '':
                RV = f'1'
            else:
                RV += f' 1'
    
    return RV
    

N = eval(input())
for i in range(N):
    LS = input().split(' ')
    n = eval(LS[0])
    RV = ''
    for j in range(1,len(LS), 2):
        Price = eval(LS[j])
        Pay = eval(LS[j+1])
        if Price > Pay:
            if RV == '':
                RV = '-1'
            else:
                RV += ' -1'
        elif Price < Pay:
            if RV == '':
                RV = getChange(Pay-Price)
            else:
                RV += f' {getChange(Pay-Price)}'
    print(RV)
        