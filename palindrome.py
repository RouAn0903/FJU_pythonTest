n = eval(input())
for i in range(n):
    s = input()
    rs = s[::-1]
    if s == rs:
        print("Yes")
    else:
        print("No")