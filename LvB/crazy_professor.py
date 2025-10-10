def C2E(cS):
    CLS = ['d', 'm', 'b', 'g', 't', 'h', 'j', 'k', 'p', 'l', ';', "'", '.', ',', '[', ']', 'e', 'y', 'f', 'u', 'o', 'n', 'r', 'v', 'i', 'c', ' ']
    ELS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    RV = ''
    for cs in cS:
        idex = CLS.index(cs)
        RV += ELS[idex]
    return RV

N = eval(input())
for i in range(N):
    CS = input()
    ES = C2E(CS)
    print(ES) 