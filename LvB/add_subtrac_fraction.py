def Plus(X, Y):
    XLS = X.split('/')
    a = int(XLS[0])
    b = int(XLS[1])
    YLS = Y.split('/')
    c = int(YLS[0])
    d = int(YLS[1])
    e = (a*d + c*b)
    f = (b*d)
    e, f = Simp(e, f)   
    return f"{e}/{f}"

def Simp(iA, iB):

    #     21  |  35
    # 1   14  |  21    1  
    #      7     14    2
    #            14

    iS, iL = iA, iB
    if iS > iL:
        iS, iL = iB, iA
    
    M = 2
    while M > 1:
        M = iL % iS
        if M >= 1:
            iL = iS
            iS = M
    if M == 1:
        iS = 1
    return int(iA/iS), int(iB/iS)

N = eval(input())
for i in range(N):
    LS = input().split(' ')
    A = LS[0]
    for j in range(1, len(LS)):
        A = Plus(A, LS[j])
    print(A)