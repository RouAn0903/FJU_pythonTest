price = eval(input())
buyNum = eval(input())
LS = input().split(' ')
CLS = []
NLS = []
for ls in LS:
    if ls not in CLS:
        CLS.append(ls)
        NLS.append(LS.count(ls))
for cls in CLS:
    pay = price * NLS[CLS.index(cls)]
    print(f'{cls}: {price} * {NLS[CLS.index(cls)]} = {pay}')