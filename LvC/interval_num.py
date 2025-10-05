def NoDS(X):
    LS = []
    for x in X:
        if x not in LS:
            LS.append(x)
    return len(LS)

n = eval(input())
for i in range(n):
    S = input()
    Key1 = False
    Key2 = False
    if NoDS(S) == 2:
        Key1 = True
    
    if S[0] != S[1] and S[1] != S[2] and S[2] != S[3]:
        Key2 = True
    
    if Key1 and Key2:
        print("Yes")
    else:
        print("No")