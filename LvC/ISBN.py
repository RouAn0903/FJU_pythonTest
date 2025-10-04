n = eval(input())
for i in range(n):
    s = input()
    sum = 0
    for j in range(len(s)):
        sum += int(s[j])*(j+1)
    d = sum%11
    if d == 10:
        print(f"{s}X")
    else:
        print(f"{s}{d}")
