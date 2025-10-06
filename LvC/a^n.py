k = eval(input())
for i in range(k):
    s = input().split(' ')
    a = eval(s[0])
    b = eval(s[1])
    n = 0
    while a ** n <= b:
        n +=1
    print(n-1)