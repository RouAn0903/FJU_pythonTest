n = eval(input())
for i in range(n):
    str = input().split(' ')
    l = 0
    for y in str:    
        if len(y) >= 10:
            l += 1
    print(l)