n = eval(input())
for i in range(n):
    num = input().strip()
    result = ""

    for j in num:
        if j == '0':
            result += '1'
        else:
            result += '0'

    print(result)
