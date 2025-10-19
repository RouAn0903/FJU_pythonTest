def returNum(X):
    c100 = X // 100
    c10  = (X - c100*100) // 10
    c1 = X - c100*100 - c10*10
    
    RV = ''
    if c100 > 0:
        for i in range(c100):
            RV += '^'
    if c10 > 0:
        for i in range(c10):
            RV += '>'
    if c1 > 0:
        for i in range(c1):
            RV += '/'
    
    return RV
    
N = eval(input())
for i in range(N):
    S = input()
    sum = 0
    for s in S:
        if s == '/':
            sum += 1
        elif s == '>':
            sum += 10
        elif s == '^':
            sum += 100
    print(f'{sum} {returNum(sum)}')
