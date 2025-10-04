n = eval(input())
for i in range(n):
    nol = eval(input())
    target = eval(input())
    ls = input().split(' ')
    key = False
    rv = ''
    for x in range(nol-1):
        for y in range(x+1, nol):
            if eval(ls[x]) + eval(ls[y]) == target:
                key = True
                rv = f'{x} {y}'
            if key:
                break
        if key:
            break
    print(rv)    
