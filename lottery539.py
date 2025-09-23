lottery = input().split(' ')
n = eval(input())
for i in range(n):
    num = input().split(' ')
    count = 0
    for num2 in num:
        if num2 in lottery:
            count+=1
    print(count)