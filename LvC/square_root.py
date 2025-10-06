k = eval(input())
for i in range(k):
    num = input().split(' ')
    x = int(num[0])
    n = int(num[1])
    found = False

    for j in range(int(x**(1/n))+2):
        if j**n == x:
            print(j)
            found = True
            break
    if not found:
        print("No")