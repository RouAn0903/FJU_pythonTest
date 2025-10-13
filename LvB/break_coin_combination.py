def Ex5(N1):
    F = N1 // 5
    return (F+1)

def Ex10(N2):
    F = N2 // 10
    CT = 0
    for i in range(F+1):
        CT += Ex5(N2-i*10)
    return CT

def Ex50(N3):
    F = N3 // 50
    CT = 0
    for i in range(F+1):
        CT += Ex10(N3-i*50)
    return CT


N = eval(input())
for i in range(N):
    X = eval(input())
    print(Ex50(X))