n = eval(input())
for i in range(n):
    num = list(map(int, input().split()))
    if len(num) == 7 and all(1 <= x <= 49 for x in num) and len(set(num)) == 7:
        print("Yes")
    else:
        print("No")