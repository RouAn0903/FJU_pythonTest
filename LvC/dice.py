n = eval(input())
for i in range(n):
    dice = input().split(' ')
    if dice[0] == dice[1] == dice[2]:
        print("Yes")
    else:
        print("No")
