k = eval(input())
for i in range(k):
    ls = input().split(' ')
    noD = int(ls[0])
    s = ls[1]
    width = int(len(s)/noD)
    st = 0
    ed = st + width
    RV = ''
    for d in range(noD):
        dS = s[st:ed]
        RV += dS[::-1]
        st = ed
        ed = st + width
    print(RV)