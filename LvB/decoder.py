N = eval(input())
for i in range(N):
    LS = input().split(' ')
    shift = int(LS[0])
    CODE = LS[1]
    LE = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    RV = ''
    for code in CODE:
        ORI = LE.index(code)
        NRI = int(ORI) - shift
        if NRI < 0:
            NRI += 26
        RV += LE[NRI]
    print(RV)