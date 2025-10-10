def PLatin(oS):
    rS = oS[1:] + oS[0] + 'ay'
    return rS.upper()


k = eval(input())
for i in range(k):
    LS = input().split(' ')
    RV = ''
    for ls in LS:
        if RV == "":
            RV = PLatin(ls)
        else:
            RV += (" " + PLatin(ls))
    print(RV)
