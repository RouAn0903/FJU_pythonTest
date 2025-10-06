n = eval(input())
for i in range(n):
    nol = eval(input())
    target = eval(input())
    ls = input().split(' ')
    for x in range(nol-1):
        for y in range(x+1, nol):
            if eval(ls[x]) + eval(ls[y]) == target:
                print(f"{x} {y}")
                break