def D2N2(x):
    if x == 0:
        return "0"
    rv = ""
    while x != 0:
        x, r = divmod(x, -2)  # 商與餘數
        if r < 0:             # Python 的 divmod 在負基底會給負餘數，要修正
            x += 1
            r += 2
        rv = str(r) + rv
    return rv

n = eval(input())
for i in range(n):
    iD = eval(input())
    print(D2N2(iD))