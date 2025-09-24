n = eval(input())
for i in range(n):
    num = input().split()
    if num == sorted(num):
        print("YES")
    else:
        print("NO")
