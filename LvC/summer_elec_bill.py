n = eval(input())
for i in range(n):
    elec = input().split(',')
    e1 = int(elec[0])
    e2 = int(elec[1])
    e3 = int(elec[2])
    A = int((e1+e2)*4.71 + e3*1.85 + 75)
    B = int(e1*6.49 + e2*4.26 + e3*1.85 + 75)
    if A == B:
        print(f"E{A}")
    elif A < B:
        print(f"A{A}")
    else:
        print(f"B{B}")