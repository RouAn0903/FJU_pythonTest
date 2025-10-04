n = eval(input())
for i in range(n):
    coin = eval(input())
    paper = coin
    candy = coin
    while paper >= 3:
        c = paper // 3
        paper -= (3*c)
        candy += c
        paper += c
    print(candy)
