n = eval(input())
for i in range(n):
    s = input()
    cls = []
    for j in range(10):
        cls.append(0)
    for S in s:
        if S in "0123456789":
            cls[int(S)] += 1 
    rv = ''
    for CLS in cls:
        rv +=str(CLS)
    print(rv)
