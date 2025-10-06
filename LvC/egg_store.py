N = eval(input())
for i in range(N):
    s = input().split(' ')
    k = eval(s[0])
    p = s[1:k+1]
    n = s[k+1:]
    sum = 0
    for j in range(k):
        sum += (eval(p[j])*eval(n[j]))
    print(sum)    