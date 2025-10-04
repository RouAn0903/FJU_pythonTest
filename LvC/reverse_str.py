n = eval(input())
for i in range(n):
    s = input().strip()
    rev = s[::-1]
    print(",".join(rev))