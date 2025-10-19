N = eval(input())
for i in range(N):
    S = input().replace('-','').replace('(','').replace(')','')
    count = 0
    total = 0
    for s in S:
        if eval(s) == 0:
            count += 11
            total += count*2
        else:
            count += eval(s) + 1
            total += count*2

        count = 0
    print(total)
